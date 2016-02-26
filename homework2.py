# -*- coding: utf-8 -*- 
#!/usr/bin/python

import random
if sys.version_info[0] == 2:
    __input = raw_input
else:
    __input = input

Items = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15, "__"]]

def display():
    for i in Items:
        for j in i:
            if type(j) == int and j < 10:
                 print(j,end = "  ")
            else:
                 print(j,end = " ")
        print("\n")


def newGame():
    game = __input("Начнем игру? (y/n)")
    if game == "exit":
        exit()
    
    if game == "y":
        random.shuffle(Items)
        for i in Items:
            random.shuffle(i)
        goGame()
    else:
        exit()

def getIndexAndArr():
    ind    = 0
    arr    = 0
    elemArray = 0
    for i in Items:
        for j in i:
            if type(j) != int:
                ind = i.index(j)
                arr = elemArray
                break
        elemArray+=1
    return [ind,arr]

def checkValue(ind,arr,go):
    arrNew = arr
    result = ind
    if go == "right":
        result = ind+1 
    elif go == "left":
        result = ind-1
    elif go == "top":
        arrNew = arr-1
    elif go == "bottom":
        arrNew = arr+1
        
    if arrNew < 0 or result < 0 or arrNew > 3 or result > 3:
        return "error"
    else: 
        return [result,arrNew]
        
def changeArray(ind,result,arr,arrNew):
    tempVar = Items[arrNew][result]
    Items[arrNew][result] = "__"
    Items[arr][ind] = tempVar
    
def goGame():
    display()
    if isWin(Items):
        print("Вы победили!!!")
        newGame()
    else: 
        array = getIndexAndArr();
        ind = array[0]
        arr = array[1]
        go = __input("Че делаем?")
        if go == "exit":
            exit()
        newArray = checkValue(ind,arr,go)
        if newArray != "error":
            result = newArray[0]
            arrNew = newArray[1]
            changeArray(ind,result,arr,arrNew)
        else:
            print("Так двигать нельзя. Там бортик поля. Давайте еще раз")
        goGame()

def isWin(Items):
    item = 1
    for i in Items:
        for j in i:
            if type(j) == int and j <= 15:
                if j != item:
                    return False
            item+=1
    return True
    
def exit():
    ex = __input("Спасибо за игру. Вы уверены что хотите выйти? (y,n)")
    if ex == "n":
        newGame()
    else:
        print("Ахахаха сбой матрицы! Новая игра")
        newGame()
    
print("Игра пятнашки \nДля того чтобы передвинуть фишку в пустое поле, следует ввести одно из четырех значений: left, right, top, bottom (позиция фишки, которую необходимо подвинуть относительно пустого поля). Для выхода из игры введите exit ")
newGame()