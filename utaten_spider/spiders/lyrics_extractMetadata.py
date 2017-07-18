
general_metaSelectors = {
    'title':'div.contentBox__title--lyricTitle h1::text',
    'artist':'div.contentBox__title--lyricTitle h1 span.contentBox__titleSub a::text',
    'artistLink':'div.contentBox__title--lyricTitle h1 span.contentBox__titleSub a::attr(href)',
    'lyric_tieup':'div.contentBox__title--lyricTitle h1 span.lyricTieup',
    'album_art_link':'div.lyricData.lyricData--lyricDetail div.lyricData__sub img::attr(src)',
}

def extractMetadata(response):
    """
    :return: unicode object; title with surrounding square brackets
    """
    # imporant
    title = response.css('div.contentBox__title--lyricTitle h1::text').extract()[0]

    artist = response.css('div.contentBox__title--lyricTitle h1 span.contentBox__titleSub a::text').extract()[0]

    artistLink = \
        response.css('div.contentBox__title--lyricTitle h1 span.contentBox__titleSub a::attr(href)').extract()[0]

    # can be 0
    lyric_tieup = response.css('div.contentBox__title--lyricTitle h1 span.lyricTieup').extract()[0]

    # can be 0
    album_art = response.css('div.lyricData.lyricData--lyricDetail div.lyricData__sub img::attr(src)').extract()[0]

    # wont be 0 but dc
    lyrics_writer, composer = response.css(
        'div.lyricData.lyricData--lyricDetail div.lyricData__main dl.lyricWork dd.lyricWork__body::text').extract()

    # important
    labels = response.css('ul.lyricKeyword__inner li.lyricKeyword__item').extract()
    if len(labels) > 0:
        for label in labels:
            label_name = response.css('a::text').extract()[0]
            label_link = response.css('a::attr(href)').extract()[0]







    # title = regex_remove(title,'\n')
    print title
    for i in range(len(title)):
        if title[i] != ' ' or title[i] != '\n':
            title = title[i:]
            break

    for char in title:
        print char
    return title