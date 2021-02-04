import re

s1 = '''Иван Иванович! 
Нужен ответ на письмо от ivanoff@ivan-chai.ru . 
Не забудьте поставить в копию 
serge'o-lupin@mail.ru- это важно.'''

s2 = ''' NO: foo.@ya.ru, foo@.ya.ru 
PARTLY: boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru '''

regular = "[\S-]+@[\w-]+\.\S{2,4}"

result1 = re.findall(regular, s1)
result2 = re.findall(regular, s2)

print(result2)
print(result1)