# -*- coding: utf-8 -*-
import re

def kana_to_roma(io_in,io_out):
    hira_roma_dict = {
        # #### long vowels - can remove?
        # u'おお': 'o', u'おう': 'o',
        # u'こう': 'ko', u'そう': 'so', u'とう': 'to', u'のう': 'no', u'ほう': 'ho', u'もう': 'mo', u'ろう': 'ro',
        # u'ごう': 'go', u'ぞう': 'zo', u'どう': 'do', u'ぼう': 'bo',
        # u'ゆう': 'yu', u'よう': 'yo',
        # u'きょう': 'kyo', u'しょう': 'sho', u'ちょう': 'cho', u'にょう': 'nyo', u'ひょう': 'hyo', u'みょう': 'myo', u'りょう': 'ryo',
        #
        # monographs-gojuon
        u'あ': 'a', u'い': 'i', u'う': 'u', u'え': 'e', u'お': 'o',
        u'か': 'ka', u'き': 'ki', u'く': 'ku', u'け': 'ke', u'こ': 'ko',
        u'さ': 'sa', u'し': 'shi', u'す': 'su', u'せ': 'se', u'そ': 'so',
        u'た': 'ta', u'ち': 'chi', u'つ': 'tsu', u'て': 'te', u'と': 'to',
        u'な': 'na', u'に': 'ni', u'ぬ': 'nu', u'ね': 'ne', u'の': 'no',
        u'は': 'ha', u'ひ': 'hi', u'ふ': 'fu', u'へ': 'he', u'ほ': 'ho',
        u'ま': 'ma', u'み': 'mi', u'む': 'mu', u'め': 'me', u'も': 'mo',
        u'や': 'ya', u'ゆ': 'yu', u'よ': 'yo',
        u'ら': 'ra', u'り': 'ri', u'る': 'ru', u'れ': 're', u'ろ': 'ro',
        u'わ': 'wa', u'を': 'wo', u'ん': 'n',
    
        # diacritics(gojuon vs handakuten)
        u'が': 'ga', u'ぎ': 'gi', u'ぐ': 'gu', u'げ': 'ge', u'ご': 'go',
        u'ざ': 'za', u'じ': 'ji', u'ず': 'zu', u'ぜ': 'ze', u'ぞ': 'zo',
        u'だ': 'da', u'ぢ': 'ji', u'づ': 'zu', u'で': 'de', u'ど': 'do',
        u'ば': 'ba', u'び': 'bi', u'ぶ': 'bu', u'べ': 'be', u'ぼ': 'bo',
        u'ぱ': 'pa', u'ぴ': 'pi', u'ぷ': 'pu', u'ぺ': 'pe', u'ぽ': 'po',
    
        u'う゛': 'vu', u'ゔ': 'vu',
        u'う゛ぁ': 'va', u'ゔぁ': 'va',
        u'う゛ぃ': 'vi', u'ゔぃ': 'vi',
        u'う゛ぇ': 've', u'ゔぇ': 've',
        u'う゛ぉ': 'vo', u'ゔぉ': 'vo',
    
        # yoon
        u'きゃ': 'kya', u'きゅ': 'kyu', u'きょ': 'kyo',
        u'しゃ': 'sha', u'しゅ': 'shu', u'しょ': 'sho',
        u'ちゃ': 'cha', u'ちゅ': 'chu', u'ちょ': 'cho',
        u'にゃ': 'nya', u'にゅ': 'nyu', u'にょ': 'nyo',
        u'ひゃ': 'hya', u'ひゅ': 'hyu', u'ひょ': 'hyo',
        u'みゃ': 'mya', u'みゅ': 'myu', u'みょ': 'myo',
        u'りゃ': 'rya', u'りゅ': 'ryu', u'りょ': 'ryo',
    
        u'ぎゃ': 'gya', u'ぎゅ': 'gyu', u'ぎょ': 'gyo',
        u'じゃ': 'ja', u'じゅ': 'ju', u'じょ': 'jo',
        u'ぢゃ': 'dya', u'ぢゅ': 'dyu', u'ぢょ': 'dyo',  # ?
        u'びゃ': 'bya', u'びゅ': 'byu', u'びょ': 'byo',
        u'ぴゃ': 'pya', u'ぴゅ': 'pyu', u'ぴょ': 'pyo',
    
        # sokuon
        u'っか': 'kka', u'っき': 'kki', u'っく': 'kku', u'っけ': 'kke', u'っこ': 'kko',
        u'っさ': 'ssa', u'っし': 'sshi', u'っす': 'ssu', u'っせ': 'sse', u'っそ': 'sso',
        u'った': 'tta', u'っち': 'tchi', u'っつ': 'ttsu', u'って': 'tte', u'っと': 'tto',
        u'っは': 'hha', u'っひ': 'hhi', u'っふ': 'ffu', u'っへ': 'hhe', u'っほ': 'hho',
        u'っや': 'yya', u'っゆ': 'yyu', u'っよ': 'yyo',
        u'っら': 'rra', u'っり': 'rri', u'っる': 'rru', u'っれ': 'rre', u'っろ': 'rro',
        u'っが': 'gga', u'っぎ': 'ggi', u'っぐ': 'ggu', u'っげ': 'gge', u'っご': 'ggo',
        u'っざ': 'zza', u'っじ': 'jji', u'っず': 'zzu', u'っぜ': 'zze', u'っぞ': 'zzo',
        u'っだ': 'dda', u'っぢ': 'jji', u'っづ': 'zzu', u'っで': 'dde', u'っど': 'ddo',
        u'っば': 'bba', u'っび': 'bbi', u'っぶ': 'bbu', u'っべ': 'bbe', u'っぼ': 'bbo',
        u'っぱ': 'ppa', u'っぴ': 'ppi', u'っぷ': 'ppu', u'っぺ': 'ppe', u'っぽ': 'ppo',
        u'っう゛ぁ': 'vva', u'っう゛ぃ': 'vvi', u'っう゛': 'vvu', u'っう゛ぇ': 'vve', u'っう゛ぉ': 'vvo',
        u'っゔぁ': 'vva', u'っゔぃ': 'vvi', u'っゔ': 'vvu', u'っゔぇ': 'vve', u'っゔぉ': 'vvo',
    
        u'っきゃ': 'kkya', u'っきゅ': 'kkyu', u'っきょ': 'kkyo',
        u'っしゃ': 'ssha', u'っしゅ': 'sshu', u'っしょ': 'ssho',
        u'っちゃ': 'tcha', u'っちゅ': 'tchu', u'っちょ': 'tcho',
        u'っひゃ': 'hhya', u'っひゅ': 'hhyu', u'っひょ': 'hhyo',
        u'っりゃ': 'rrya', u'っりゅ': 'rryu', u'っりょ': 'rryo',
        u'っぎゃ': 'ggya', u'っぎゅ': 'ggyu', u'っぎょ': 'ggyo',
        u'っじゃ': 'jja', u'っじゅ': 'jju', u'っじょ': 'jjo',
        u'っぢゃ': 'ddya', u'っぢゅ': 'ddyu', u'っぢょ': 'ddyo',
        u'っびゃ': 'bbya', u'っびゅ': 'bbyu', u'っびょ': 'bbyo',
        u'っぴゃ': 'ppya', u'っぴゅ': 'ppyu', u'っぴょ': 'ppyo',
    
        # n w vowels (separate)
        u'んあ': "n'a", u'んい': "n'i", u'んう': "n'u", u'んえ': "n'e", u'んお': "n'o",
    
        # mini
        u'ぁ': 'a', u'ぃ': 'i', u'ぅ': 'u', u'ぇ': 'e', u'ぉ': 'o',
        u'っ': '',  # stand alone nothing
        u'ゃ': 'ya', u'ゅ': 'yu', u'ょ': 'yo',
        u'ゎ': 'wa',
        u'ゐ': 'i|wi', u'ゑ': 'e|we',
    
        # u'　':' ',
        # u'０': '0', u'１': '1', u'２': '2', u'３': '3', u'４': '4',
        # u'５': '5', u'６': '6', u'７': '7', u'８': '8', u'９': '9',
        #
        # u'Ａ': 'a', u'Ｂ': 'b', u'Ｃ': 'c', u'Ｄ': 'd', u'Ｅ': 'e', u'Ｆ': 'f', u'Ｇ': 'g', u'Ｈ': 'h', u'Ｉ': 'i',
        # u'Ｊ': 'j', u'Ｋ': 'k', u'Ｌ': 'l', u'Ｍ': 'm', u'Ｎ': 'n', u'Ｏ': 'o', u'Ｐ': 'p', u'Ｑ': 'q', u'Ｒ': 'r',
        # u'Ｓ': 's', u'Ｔ': 't', u'Ｕ': 'u', u'Ｖ': 'v', u'Ｗ': 'w', u'Ｘ': 'x', u'Ｙ': 'y', u'Ｚ': 'z',
        #
        # u'ａ': 'a', u'ｂ': 'b', u'ｃ': 'c', u'ｄ': 'd', u'ｅ': 'e', u'ｆ': 'f', u'ｇ': 'g', u'ｈ': 'h', u'ｉ': 'i',
        # u'ｊ': 'j', u'ｋ': 'k', u'ｌ': 'l', u'ｍ': 'm', u'ｎ': 'n', u'ｏ': 'o', u'ｐ': 'p', u'ｑ': 'q', u'ｒ': 'r',
        # u'ｓ': 's', u'ｔ': 't', u'ｕ': 'u', u'ｖ': 'v', u'ｗ': 'w', u'ｘ': 'x', u'ｙ': 'y', u'ｚ': 'z',
    }
    
    kata_roma_dict={
        # monographs-gojuon
        u'ア':'a', u'イ':'i', u'ウ':'u', u'エ':'e', u'オ':'o',
        u'カ':'ka', u'キ':'ki', u'ク':'ku', u'ケ':'ke', u'コ':'ko',
        u'サ':'sa', u'シ':'shi', u'ス':'su', u'セ':'se', u'ソ':'so',
        u'タ':'ta', u'チ':'chi', u'ツ':'tsu', u'テ':'te', u'ト':'to',
        u'ナ':'na', u'ニ':'ni', u'ヌ':'nu', u'ネ':'ne', u'ノ':'no',
        u'ハ':'ha', u'ヒ':'hi', u'フ':'fu', u'ヘ':'he', u'ホ':'ho',
        u'マ':'ma', u'ミ':'mi', u'ム':'mu', u'メ':'me', u'モ':'mo',
        u'ヤ':'ya', u'ユ':'yu', u'ヨ':'yo',
        u'ラ':'ra', u'リ':'ri', u'ル':'ru', u'レ':'re', u'ロ':'ro',
        u'ワ':'wa', u'ヰ':'wi', u'ヱ':'we', u'ヲ':'wo',
        u'ン':'n',
    
        # special case (include or not)
        u'ディ':'di', u'ドゥ':'du', u'ウォ':'wo', u'ウィ':'wi',
    
        # diacritics(gojuon vs handakuten)
        u'ガ':'ga', u'ギ ':'gi', u'グ':'gu', u'ゲ':'ge', u'ゴ':'go',
        u'ザ':'za', u'ジ':'ji', u'ズ':'zu', u'ゼ':'ze', u'ゾ':'zo',
        u'ダ':'da', u'ヂ':'ji', u'ヅ ':'zu', u'デ':'de', u'ド':'do',
        u'バ ':'ba', u'ビ':'bi', u'ブ':'bu', u'ベ':'be', u'ボ':'bo',
        u'パ':'pa', u'ピ':'pi', u'プ':'pu', u'ペ':'pe', u'ポ':'po',
    
        # yoon
        u'キャ':'kya', u'キュ':'kyu', u'キョ':'kyo',
        u'シャ':'sha', u'シュ':'shu', u'ショ':'sho',
        u'チャ':'cha', u'チュ':'chu', u'チョ':'cho',
        u'ニャ':'nya', u'ニュ':'nyu', u'ニョ':'nyo',
        u'ヒャ':'hya', u'ヒュ':'hyu', u'ヒョ':'hyo',
        u'ミャ':'mya', u'ミュ':'myu', u'ミョ':'myo',
        u'リャ':'rya', u'リュ':'ryu', u'リョ':'ryo',
    
        u'ギャ':'gya', u'ギュ':'gyu', u'ギョ':'gyo',
        u'ジャ':'ja', u'ジュ':'ju', u'ジョ':'jo',
        u'ヂャ':'dya', u'ヂュ':'dyu', u'ヂョ':'dyo',  # ?
        u'ビャ':'bya', u'ビュ':'byu', u'ビョ':'byo',
        u'ピャ':'pya', u'ピュ':'pyu', u'ピョ':'pyo',
    
        # n vowels
        u'ンア':"n'a", u'ンイ':"n'i", u'ンウ':"n'u", u'ンエ':"n'e", u'ンオ':"n'o",
    
        # mini
        u'ァ':'a', u'ィ':'i', u'ゥ':'u', u'ェ':'e', u'ォ':'o',
        u'ッ':'',  # stand alone nothing
        u'ャ':'ya', u'ュ':'yu', u'ョ':'yo',
        u'ヮ':'wa',
        u'ヵ':'ka', u'ヶ':'ke',
        u'ヷ':'va', u'ヸ':'vi', u'ヴ':'vu', u'ヹ':'ve', u'ヺ':'vo',
        # u'ー'
    
        # sokuon
    
        u'ッカ':'kka', u'ッキ':'kki', u'ック':'kku', u'ッケ':'kke', u'ッコ':'kko',
        u'ッサ':'ssa', u'ッシ':'sshi', u'ッス':'ssu', u'ッセ':'sse', u'ッソ':'sso',
        u'ッタ':'tta', u'ッチ':'cchi', u'ッツ':'ttsu', u'ッテ':'tte', u'ット':'tto',
        u'ッナ':'nna', u'ッニ':'nni', u'ッヌ':'nnu', u'ッネ':'nne', u'ッノ':'nno',
        u'ッハ':'hha', u'ッヒ':'hhi', u'ッフ':'ffu', u'ッヘ':'hhe', u'ッホ':'hho',
        u'ッマ':'mma', u'ッミ':'mmi', u'ッム':'mmu', u'ッメ':'mme', u'ッモ':'mmo',
        u'ッヤ':'yya', u'ッユ':'yyu', u'ッヨ':'yyo',
        u'ッラ':'rra', u'ッリ':'rri', u'ッル':'rru', u'ッレ':'rre', u'ッロ':'rro',
        u'ッワ':'wwa', u'ッウィ':'wwi', u'ッヰ':'wwi', u'ッヱ':'wwe', u'ッヲ':'wwo', u'ッウォ':'wwo',
        u'ッガ':'gga', u'ッギ ':'ggi', u'ッグ':'ggu', u'ッゲ':'gge', u'ッゴ':'ggo',
        u'ッザ':'zza', u'ッジ':'jji', u'ッズ':'zzu', u'ッゼ':'zze', u'ッゾ':'zzo',
        u'ッダ':'dda', u'ッヂ':'jji', u'ッディ':'jji', u'ッヅ ':'zzu', u'ッドゥ':'zzu', u'ッデ':'dde', u'ッド':'ddo',
        u'ッバ ':'bba', u'ッビ':'bbi', u'ッブ':'bbu', u'ッベ':'bbe', u'ッボ':'bbo',
        u'ッパ':'ppa', u'ッピ':'ppi', u'ップ':'ppu', u'ッペ':'ppe', u'ッポ':'ppo',
    
        u'ッキャ':'kkya', u'ッキュ':'kkyu', u'ッキョ':'kkyo',
        u'ッシャ':'ssha', u'ッシュ':'sshu', u'ッショ':'ssho',
        u'ッチャ':'ccha', u'ッチュ':'cchu', u'ッチョ':'ccho',
        u'ッニャ':'nnya', u'ッニュ':'nnyu', u'ッニョ':'nnyo',
        u'ッヒャ':'hhya', u'ッヒュ':'hhyu', u'ッヒョ':'hhyo',
        u'ッミャ':'mmya', u'ッミュ':'mmyu', u'ッミョ':'mmyo',
        u'ッリャ':'rrya', u'ッリュ':'rryu', u'ッリョ':'rryo',
        u'ッギャ':'ggya', u'ッギュ':'ggyu', u'ッギョ':'ggyo',
        u'ッジャ':'jja', u'ッジュ':'jju', u'ッジョ':'jjo',
        u'ッヂャ':'ddya', u'ッヂュ':'ddyu', u'ッヂョ':'ddyo',
        u'ッビャ':'bbya', u'ッビュ':'bbyu', u'ッビョ':'bbyo',
        u'ッピャ':'ppya', u'ッピュ':'ppyu', u'ッピョ':'ppyo',
    }
    
    
    def get_sub_function(convdict):
        string = u"""
        <kanromGroup>
            <kanaGroup>{}<kanaGroup>
            <romaGroup>{}<romaGroup>
        <kanromGroup>
              """
        def sub_function(match):
            return  string.format(match.group(0),convdict[match.group(0)])
        return sub_function
    
    
    # make a regex pattern w keys sorted in descending length
    hira_regex = re.compile("|".join(sorted(hira_roma_dict.keys(),key=len,reverse=True)))
    kata_regex = re.compile("|".join(sorted(kata_roma_dict.keys(),key=len,reverse=True)))
    
    f_in = open(io_in,'r')
    string = ''.join(f_in.readlines())
    string = string.decode('utf-8')
    f_in.close()
    
    furi_regex = re.compile(u'<furiganaGroup>(.+)<furiganaGroup>')
    kana_regex = re.compile(u'<kanaGroup>(.+)<kanaGroup>')
 
    # get rid of furi group tag, replace with containing kana
    string = furi_regex.sub(lambda x: kana_regex.search(x.group(1)).group(1),string)
    # get rid of kana group tag, replace with containing kana
    string = kana_regex.sub(lambda x: x.group(1),string)
    # remove \n in file
    string = re.compile(u'\n').sub(lambda x:'',string)
    
    string = hira_regex.sub(get_sub_function(hira_roma_dict),string)
    string = kata_regex.sub(get_sub_function(kata_roma_dict),string)

    f_out = open(io_out,'w')
    f_out.write(string.encode('utf-8'))
    f_out.close()


if __name__ == '__main__':
    filelist = [
    #closer

    'C:/Users/bryanp/Desktop/utaten_spider/Joe Inoue - Closer (kanjikana).txt',
    #haruka kanata
    'C:/Users/bryanp/Desktop/utaten_spider/AKG - haruka kanata (kanjikana).txt',
    #sign
    'C:/Users/bryanp/Desktop/utaten_spider/FLOW - Sign (kanjikana).txt',
    #silhouette
    'C:/Users/bryanp/Desktop/utaten_spider/KANA-BOON - silhouette (kanjikana).txt'
    ]
    i = 0
    for file in filelist:
        i+=1
        kana_to_roma(file,'song_{}.txt'.format(i))