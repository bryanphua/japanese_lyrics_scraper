import scrapy
from lyrics_extractLyrics import process_lyrics,write_tokens_to_file,regex_remove
# ~Lyrics Structure~ #
# div.lyricBody
# 	div.medium
# 		span.ruby
# 			span.rb katakana
# 			span.rt furigana
# 		SINGLE
# 		kana
#
# line splits by <br> or \n in extract text

class UtatenLyricsSpider(scrapy.Spider):
    name = "utaten_lyrics_spider"

    def start_requests(self):
        urls = [
            # haruka kanata
            'http://utaten.com/lyric/ASIAN+KUNG-FU+GENERATION/%E9%81%A5%E3%81%8B%E5%BD%BC%E6%96%B9/#sort=popular_sort_asc',
            # flow sign
            #'http://utaten.com/lyric/FLOW/Sign/#sort=popular_sort_asc',
            # joe closer
            #'http://utaten.com/lyric/%E4%BA%95%E4%B8%8A%E3%82%B8%E3%83%A7%E3%83%BC/CLOSER/#sort=popular_sort_asc',
            # silouhette
            #'http://utaten.com/lyric/KANA-BOON/%E3%82%B7%E3%83%AB%E3%82%A8%E3%83%83%E3%83%88/#sort=popular_sort_asc'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):#r'"medium">\n[^(span)]+<span class="ruby">'+ \

        #self.extractLyrics(response)
        print 'title'
        title = self.extractTitle(response)
        f = open('titletest.txt','w')
        f.write(title.encode('utf-8'))
        f.close()


    # if lyrics/artist/songname -> extractLyrics(response)
    @staticmethod
    def extractLyrics(response):

        # extract lyrics
        tokens = process_lyrics(response)
        filename = response.url.split('/')[-3] +' - '+response.url.split('/')[-2]+'.txt'
        write_tokens_to_file(filename,tokens)




    def extractData(text):
        pass



