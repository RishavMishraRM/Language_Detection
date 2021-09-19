# Python program to demonstrate
# langdetect


from langdetect import detect


# Specifying the language for
# detection
print(detect("GitHub is a Open Source Porta;"))
print(detect("это компьютерный портал для гиков"))
print(detect(" es un portal informático para geeks"))
print(detect("是面向极客的计算机科学门户"))
print(detect("geeks के लिए एक कंप्यूटर विज्ञान पोर्टल है"))
print(detect("は、ギーク向けのコンピューターサイエンスポータルです。"))
