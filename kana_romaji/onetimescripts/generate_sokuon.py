# -*- coding: utf-8 -*-
from __future__ import unicode_literals
kanadict = {# monographs-gojuon
    # monographs-gojuon
   # u'ア': 'a', u'イ': 'i', u'ウ': 'u', u'エ': 'e', u'オ': 'o',
    u'カ': 'ka', u'キ': 'ki', u'ク': 'ku', u'ケ': 'ke', u'コ': 'ko',
    u'サ': 'sa', u'シ': 'shi', u'ス': 'su', u'セ': 'se', u'ソ': 'so',
    u'タ': 'ta', u'チ': 'chi', u'ツ': 'tsu', u'テ': 'te', u'ト': 'to',
    u'ナ': 'na', u'ニ': 'ni', u'ヌ': 'nu', u'ネ': 'ne', u'ノ': 'no',
    u'ハ': 'ha', u'ヒ': 'hi', u'フ': 'fu', u'ヘ': 'he', u'ホ': 'ho',
    u'マ': 'ma', u'ミ': 'mi', u'ム': 'mu', u'メ': 'me', u'モ': 'mo',
    u'ヤ': 'ya', u'ユ': 'yu', u'ヨ': 'yo',
    u'ラ': 'ra', u'リ': 'ri', u'ル': 'ru', u'レ': 're', u'ロ': 'ro',
    u'ワ': 'wa', u'ヰ': 'wi', u'ヱ': 'we', u'ヲ': 'wo',
    u'ン': 'n',

    # special case (include or not)
    u'ディ': 'di', u'ドゥ': 'du', u'ウォ': 'wo', u'ウィ': 'wi',

    # diacritics(gojuon vs handakuten)
    u'ガ': 'ga', u'ギ ': 'gi', u'グ': 'gu', u'ゲ': 'ge', u'ゴ': 'go',
    u'ザ': 'za', u'ジ': 'ji', u'ズ': 'zu', u'ゼ': 'ze', u'ゾ': 'zo',
    u'ダ': 'da', u'ヂ': 'di', u'ヅ ': 'du', u'デ': 'de', u'ド': 'do',
    u'バ ': 'ba', u'ビ': 'bi', u'ブ': 'bu', u'ベ': 'be', u'ボ': 'bo',
    u'パ': 'pa', u'ピ': 'pi', u'プ': 'pu', u'ペ': 'pe', u'ポ': 'po',

    u'キャ': 'kya', u'キュ': 'kyu', u'キョ': 'kyo',
    u'シャ': 'sha', u'シュ': 'shu', u'ショ': 'sho',
    u'チャ': 'cha', u'チュ': 'chu', u'チョ': 'cho',
    u'ニャ': 'nya', u'ニュ': 'nyu', u'ニョ': 'nyo',
    u'ヒャ': 'hya', u'ヒュ': 'hyu', u'ヒョ': 'hyo',
    u'ミャ': 'mya', u'ミュ': 'myu', u'ミョ': 'myo',
    u'リャ': 'rya', u'リュ': 'ryu', u'リョ': 'ryo',

    u'ギャ': 'gya', u'ギュ': 'gyu', u'ギョ': 'gyo',
    u'ジャ': 'ja', u'ジュ': 'ju', u'ジョ': 'jo',
    u'ヂャ': 'dya', u'ヂュ': 'dyu', u'ヂョ': 'dyo',  # ?
    u'ビャ': 'bya', u'ビュ': 'byu', u'ビョ': 'byo',
    u'ピャ': 'pya', u'ピュ': 'pyu', u'ピョ': 'pyo',
}
soku = u'ッ'
string = ''

sokuondict = {}
for item in kanadict.iteritems():
    hira,roma = item
    newhira = soku+hira
    newroma = roma[0]+roma
    print roma[0]
    try:
        sokuondict[roma[0]].append((newroma, newhira))
    except KeyError:
        sokuondict[roma[0]] = []
        sokuondict[roma[0]].append((newroma,newhira))

string =u''
for key in sokuondict.keys():
    string += key+u'\n'
    for value in sokuondict[key]:
        newroma,newhira = value
        string += 'u\'{}\':\'{}\',\n'.format(newhira,newroma)
f = open('sokuon2.txt','w')
f.write(string.encode('utf-8'))
f.close()