import re

################################### Metadata functions ############################################3
def extractTitle(response):
    try:
        title = response.css('div.contentBox__title--lyricTitle h1::text').extract()[0]
        for i in range(len(title)):
            if title[i] != ' ' or title[i] != '\n':
                title = title[i:]
                return title
    except:
        return None

def extractArtist(response):
    try:
        artist = response.css('div.contentBox__title--lyricTitle h1 span.contentBox__titleSub a::text').extract()[0]
    except:
        artist = None
    return artist

def extractArtistLink(response):
    try:
        artistLink = \
            response.css('div.contentBox__title--lyricTitle h1 span.contentBox__titleSub a::attr(href)').extract()[0]
    except:
        artistLink = None
    return artistLink


def extractSideTitle(response):
    # can be 0 (right of no ge qu)
    try:
        lyric_tieup = response.css('div.contentBox__title--lyricTitle h1 span.lyricTieup').extract()[0]
    except:
        lyric_tieup = None
    return lyric_tieup

def extractAlbumArtLink(response):
    try:
        album_art_link = response.css('div.lyricData.lyricData--lyricDetail div.lyricData__sub img::attr(src)').extract()[0]
    except:
        album_art_link = None
    return album_art_link

def extractComposers(response):
    try:
        lyrics_writer, composer = response.css(
            'div.lyricData.lyricData--lyricDetail div.lyricData__main dl.lyricWork dd.lyricWork__body::text').extract()
        return lyrics_writer,composer
    except:
        return None,None

def extractLabels(response):
    """returns a list of tuples (labelname,labellink)"""
    labellist = []
    labels = response.css('ul.lyricKeyword__inner li.lyricKeyword__item').extract()
    if len(labels) > 0:
        for label in labels:
            try:
                label_name = response.css('a::text').extract()[0]
            except:
                label_name = None
            try:
                label_link = response.css('a::attr(href)').extract()[0]
            except:
                label_link = None
            labeltuple = (label_name,label_link)
            labellist.append(labeltuple)
    return labellist

def extractEmotion(response):
    cssmatch = response.css('div.gauge__button button.mostVoted').extract()
    if len(cssmatch) == 1:
        cssmatch = cssmatch[0]
        matches = re.findall('mostVoted {.*}Btn"', cssmatch)
        if len(matches) != 1:
            mostvoted = None
        else:
            mostvoted = matches[0]
    else:
        mostvoted = None
    return mostvoted

#########################################################################
def extractMetadata(response):
    """
    returns a dictionary
    extract metadata from a lyircs page to store into database might need cleaning up
    """
    lyriccomposer = extractComposers(response)
    return dict(
        title = extractTitle(response),
        artist = extractArtist(response),
        artistLink = extractArtistLink(response),
        lyric_sideTitle = extractSideTitle(response),
        album_art_link = extractAlbumArtLink(response),
        lyrics_writer = lyriccomposer[0],
        composer = lyriccomposer[1],
        label_list = extractLabels(response),
        emotion = extractEmotion(response),
    )