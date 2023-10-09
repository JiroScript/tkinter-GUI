import codecs
import json
# ファイルを開く(書き込みモード)
csm01={}
csm01={'顧客名':'守銭奴スチール','建屋':'ニューギンザビル','ア':'1'}
print(csm01)
print(type(csm01))
#辞書型を文字列に
str=json.dumps(csm01)
print(json.loads(str))
print(type(str))
f = codecs.open("data.txt","w","utf-8")
#text = "鎌鼬,A,1"str = 
text =''

f.write(text)

# ファイルを閉じる
f.close()
