from konlpy.tag import Okt

okt = Okt()

text = "KoNLPy를 사용하여 한국어 텍스트를 분석합니다."
tokens = okt.morphs(text)

print(tokens)
