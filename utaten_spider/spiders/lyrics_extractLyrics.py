import re

##########################################################################
# General Regex Functions

def regex_remove(string,regex):
    pattern = re.compile(regex)

    poslist = []
    # find matches
    for iter in pattern.finditer(string):
        poslist.append(iter.span())

    print poslist
    # precautionary - ensure sorted and no overlap
    for i in range(len(poslist)):
        if not (poslist[i][0] < poslist[i][1]):
            assert False
        if i < len(poslist)-2:
            if not (poslist[i][1] <= poslist[i+1][0]):
                assert False

    # remove from the back so subsequent index positions are not affected
    for start, stop in poslist[::-1]:
        string = string[:start] + string[stop:]

    return string

def tokenize_string(string,regex):
    """
    :param string: string, to extract tokens from
    :param regex: string, regex expression of token(s)
    :return: list of tokens, (regex match) , (nonregex match until regex match)
    """
    pattern = re.compile(regex)

    poslist = []
    # find matches
    for iter in pattern.finditer(string):
        poslist.append(iter.span())

    # precautionary - ensure sorted and no overlap
    for i in range(len(poslist)):
        if not (poslist[i][0] < poslist[i][1]):
            assert False
        if i < len(poslist) - 1: #everything but the last
            if not (poslist[i][1] <= poslist[i + 1][0]):
                assert False

    tokens = []
    for i in range(len(poslist)):
        start,stop = poslist[i]
        # add nonregex string before first regex token
        if i == 0:
            if start >0:
               tokens.append(string[:start])

        # add current regex token
        tokens.append(string[start:stop])

        # add nonregex string after current regex token
        if i < len(poslist) - 1:
            nextstart = poslist[i+1][0]
            if stop != nextstart:
                tokens.append(string[stop:nextstart])
        else:
            if stop< len(string):
                tokens.append(string[stop:])

    return tokens

##########################################################################
# Specific Functions

def custom_parseToken(string):
    """
    parse furigana, kana, english, <br>, others(space,symbols,etc) and as token(string) surrounded in specific tag
    note: regex expr should not overlap or else output is unpredictable
    :param string: regex/non regex token
    :return: if token matches regex, return corresponding function(string) output else string
    """
    # furigana, kana, english, <br>, others(space,symbols,etc)
    furigana_regex = u'<span class="ruby"><span class="rb">[^<>]+</span><span class="rt">[^<>]+</span></span>'
    furigana_p = re.compile(furigana_regex)
    kana_regex = u'(([\u3041-\u3096]|[\u309a-\u309f]|[\u30a0-\u30ff])+)'
    kana_p = re.compile(kana_regex)

    # Tags defined here
    furiTag = u'<furiganaGroup>'
    kanjiTag = u'<kanjiGroup>'
    kanaTag = u'<kanaGroup>'

    if furigana_p.match(string) != None: # if furigana
        kanji_regex = u'<span class="rb">([^<>]+)</span>'
        kanji_p = re.compile(kanji_regex)
        kanji = kanji_p.findall(string)[0]

        kana_regex = u'<span class="rt">([^<>]+)</span>'
        kana_p = re.compile(kana_regex)
        kana = kana_p.findall(string)[0]


        return furiTag + kanjiTag + kanji + kanjiTag + kanaTag + kana + kanaTag +furiTag

    elif kana_p.match(string) != None: # if kana
        return kanaTag + string + kanaTag

    # else do nothing
    return string

def process_lyrics(response):
    lyricsSelector = 'div.lyricBody div.medium'
    string_list = response.css(lyricsSelector).extract()
    assert len(string_list) == 1
    string = string_list[0]

    # furiganaGroup/<br>/kanaGroup
    regextokens = \
        u'(<span class="ruby"><span class="rb">([^<>]+)</span><span class="rt">([^<>]+)</span></span>)' + \
        u'|' + \
        u'(<br>)' + \
        u'|' + \
        u'(([\u3041-\u3096]|[\u309a-\u309f]|[\u30a0-\u30ff])+)'
    # hirgana [\u3041-\u3096]|[\u309a-\u309f]
    # katakana [\u30a0-\u30ff]

    # remove div tags and linebreaks
    regex = '(<div class="medium">)|(</div>)|(\n)'
    string = regex_remove(string, regex)

    tokens = tokenize_string(string, regextokens)
    for i in range(len(tokens)):
        tokens[i] = custom_parseToken(tokens[i])

    # save it to file:
    return tokens


def write_tokens_to_file(path,tokens):
    """
    write a list of string(token) to a file separated by \n
    """
    f = open(path,'w')
    for token in tokens:
        f.write(token.encode('utf8'))
        f.write('\n')
    f.close()



if __name__ == "__main__":
    path = 'C:/Users/bryanp/Desktop/tutorial/test_lyrics_sign.txt'
    f = open(path,'r')
    string = f.read().decode('utf8')
    f.close()

    # remove div open close tags and line breaks of html
    # line breaks in lyrics are represented by <br>
    regex = '(<div class="medium">)|(</div>)|(\n)'
    string = regex_remove(string,regex)
    print string

    tokens = process_lyrics(string)
    write_tokens_to_file('Flow-Sign.txt', tokens)


