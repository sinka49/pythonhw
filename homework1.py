# -*- coding: utf-8 -*- 
#!/usr/bin/python

import sys

class Questions:
     question = ""
     right_answer = ""
     def set_question(self, new_question):
          self.question = new_question
     def set_right_answer(self, new_right_answer):
          self.right_answer = new_right_answer
     def check_value(self,variant):
          if (self.right_answer == variant):
              print('\nПравильно\n')
              return True
          else:
              print('\nНеправильно\n')
              return False
if sys.version_info[0] == 2:
    _input = raw_input
else:
    _input = input

count_errors = 0
array_questions = [["Существует ли в Python тип данных complex? (Формат ответа: да - 1, нет - 0)","1"],
["Как называется Специальный тип данных для обозначения 'ничего', 'пустоты'? (Формат ответа - название типа, либо 'не существует')","None"],
["Что такое elif в Python? Варианты ответа: 1 - Цикл с пост-условием  2 - Цикл с пред-условием	 3 - Расширение оператора выбора  (Формат ответа: 1/2/3)","3"],
["Что такое тернарные выражения? Варианты ответа: 1 - условная операция				 2 - Цикл с пред-условием	 (Формат ответа: 1/2/3)", "1"],
["Есть ли в Python цикл с пост-условием? (Формат ответа: да - 1, нет - 0)" , "0"],
["Какие переменные называются локальными? Варианты ответа: 1 - переменные объявленые в модуле (файле)				 2 - объявлены внутри функции	 (Формат ответа: 1/2)","2"],
["Какая команда инициализирует папку как git проект? Варианты ответа: 1 - git commit	 2 - git push origin nameOfBranch				 3 - git init				 (Формат ответа: 1/2/3)","3"]]
i = 0
while(i < len(array_questions)): 
    obj = Questions()
    obj.set_question(array_questions[i][0])
    obj.set_right_answer(array_questions[i][1])
    variant = _input(obj.question)
    result = obj.check_value(variant)
    if (result):
        i += 1 
    else: 
        count_errors += 1

print(" ")
if (count_errors > 0):
    print("Количество ошибок", count_errors)
_input('Вы ответили на все вопросы!!! Молодец!!!')