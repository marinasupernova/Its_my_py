import re

s1 = "Вечер за окном. / Еще один день прожит. / Жизнь скоротечна..."
s2 = "Просто текст"
s3 = "Как вишня расцвела! / Она с коня согнала / И князя-гордеца."
s4 = "На голой ветке / Ворон сидит одиноко… / Осенний вечер!"
s5 = "Тихо, тихо ползи, / Улитка, по склону Фудзи, / Вверх, до самых высот!"
s6 = "Жизнь скоротечна… / Думает ли об этом / Маленький мальчик."

def haiku_checker(string):

    sentences = string.lower().split("/")
    if len(sentences) != 3:
        return False
    counters = []
    for sentence in sentences:
        vowels = re.findall("[аеёиоуыэюя]", sentence)
        counters.append(len(vowels))
    if counters[0] == 5 and counters[1] == 7 and counters[2] == 5:
        return True
    else:
        return False

   
print(haiku_checker(s1))
print(haiku_checker(s2))
print(haiku_checker(s3))
print(haiku_checker(s4))
print(haiku_checker(s5))
print(haiku_checker(s6))