import os
import time
import pickle

class Machine:
    color=None
    model=None
    engine=None
    kpp=None
    akum=None

while True:
    saves = open("Save.txt", "a", encoding="UTF-8")  # для записи
    deletes = open("Deletes.txt", "w", encoding="UTF-8")  # для редактирования конфигураций
    Spisok = list(map(str, open('Save.txt', encoding='UTF-8')))  # для чтения работы вывода и тд
    print('1. Добавить машину')
    print('2. Редактировать машину')
    print('3. Посмотреть состояние машины')
    print('4. Список машин')
    print('5. Удаление машин')
    print('6. Взаимодействие')
    print('7. Тест первый') #проверка на заполнение
    print('7.2 Тест первый 2 ч')
    print('8. Тест второй') #последняя модель + кол-во машин
    print('9. Тест третий') #очистка
    s = saves.tell()

    a = input()

    if a == '1':
        Machine.model = input('Введите модель: ')
        Machine.engine=input('Введите двигатель: ')
        Machine.akum=input('Введите аккумулятор: ')
        Machine.kpp=input('Введите коробку переключения передач: ')
        Machine.color=input('Введите цвет: ')
        saves.write(Machine.model+','+Machine.engine+','+Machine.akum+','+Machine.kpp+','+Machine.color+',\n')
        print('----------------------')
        print('конфигурация сохранена')
        print('----------------------')

    elif a == '2':
        cnt = 0
        for i in range(len(Spisok)):
            q = str(Spisok[i])
            if len(q) > 9:
                q = q.split(',')
                cnt += 1
                print(cnt, '-', q[0])
            else:
                continue
        x = int(input())
        if x>0:
            print('1. Поменять модель')
            print('2. Поменять цвет')
            print('3. Поменять двигатель')
            print('4. Поменять кпп')
            print('5. Поменять акум')
            print('0. Назад')
            b = input()



            if b == '1':
                print('Введите модель')
                newmodel = input()
                cnt = 0
                for i in range(len(Spisok)):
                    q = str(Spisok[i])
                    if len(q) > 9:
                        q = q.split(',')
                        cnt += 1
                        if cnt==x:
                            Machine.model=newmodel
                            Machine.engine = q[1]
                            Machine.akum = q[2]
                            Machine.kpp = q[3]
                            Machine.color = q[4]
                            deletes.write(
                                Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                        else:
                            Machine.model = q[0]
                            Machine.engine = q[1]
                            Machine.akum = q[2]
                            Machine.kpp = q[3]
                            Machine.color = q[4]
                            deletes.write(
                                Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                    else:
                        continue



            if b == '2':
                print('Введите цвет')
                newcolor = input()
                cnt=0
                for i in range(len(Spisok)):
                    q = str(Spisok[i])
                    if len(q) > 9:
                        q = q.split(',')
                        cnt += 1
                        if cnt==x:
                            Machine.model=q[0]
                            Machine.engine = q[1]
                            Machine.akum = q[2]
                            Machine.kpp = q[3]
                            Machine.color = newcolor
                            deletes.write(
                                Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                        else:
                            Machine.model = q[0]
                            Machine.engine = q[1]
                            Machine.akum = q[2]
                            Machine.kpp = q[3]
                            Machine.color = q[4]
                            deletes.write(
                                Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                    else:
                        continue





            if b == '3':
                print('Введите двигатель')
                newengine = input()
                cnt = 0
                for i in range(len(Spisok)):
                    q = str(Spisok[i])
                    if len(q) > 9:
                        q = q.split(',')
                        cnt += 1
                        if cnt == x:
                            Machine.model = q[0]
                            Machine.engine = newengine
                            Machine.akum = q[2]
                            Machine.kpp = q[3]
                            Machine.color = q[4]
                            deletes.write(
                                Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                        else:
                            Machine.model = q[0]
                            Machine.engine = q[1]
                            Machine.akum = q[2]
                            Machine.kpp = q[3]
                            Machine.color = q[4]
                            deletes.write(
                                Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                    else:
                        continue

            if b == '4':
                print('Введите кпп')
                newkpp = input()
                cnt = 0
                for i in range(len(Spisok)):
                    q = str(Spisok[i])
                    if len(q) > 9:
                        q = q.split(',')
                        cnt += 1
                        if cnt == x:
                            Machine.model = q[0]
                            Machine.engine = q[1]
                            Machine.akum = q[2]
                            Machine.kpp = newkpp
                            Machine.color = q[4]
                            deletes.write(
                                Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                        else:
                            Machine.model = q[0]
                            Machine.engine = q[1]
                            Machine.akum = q[2]
                            Machine.kpp = q[3]
                            Machine.color = q[4]
                            deletes.write(
                                Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                    else:
                        continue



            if b == '5':
                print('Введите акум')
                newakum = input()
                cnt = 0
                for i in range(len(Spisok)):
                    q = str(Spisok[i])
                    if len(q) > 9:
                        q = q.split(',')
                        cnt += 1
                        if cnt == x:
                            Machine.model = q[0]
                            Machine.engine = q[1]
                            Machine.akum = newakum
                            Machine.kpp = q[3]
                            Machine.color = q[4]
                            deletes.write(
                                Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                        else:
                            Machine.model = q[0]
                            Machine.engine = q[1]
                            Machine.akum = q[2]
                            Machine.kpp = q[3]
                            Machine.color = q[4]
                            deletes.write(
                                Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                    else:
                        continue



            if b == '0':
                continue

            saves.close()
            deletes.close()
            os.remove('Save.txt')
            os.rename('Deletes.txt', 'Save.txt')

    elif a == '3':
        cnt = 0
        for i in range(len(Spisok)):
            q = str(Spisok[i])
            if len(q) > 9:
                q = q.split(',')
                cnt += 1
                print(cnt, '-', q[0])
            else:
                continue
        x = int(input())
        if x > 0:
            cnt=0
            for i in range(len(Spisok)):
                q = str(Spisok[i])
                if len(q) > 9:
                    q = q.split(',')
                    cnt += 1
                    if cnt==x:
                        print('Модель:',q[0])
                        print('Двигатель:',
                        q[1])
                        print('Аккумулятор:',
                        q[2])
                        print('Коробка передач:',
                        q[3])
                        print('Цвет:',
                        q[4])
                else:
                    continue

    elif a == '4':
        cnt=0
        for i in range(len(Spisok)):
            q = str(Spisok[i])
            if len(q) > 9:
                q = q.split(',')
                cnt += 1
                print(cnt,'-',q[0])
            else:
                continue

    elif a == '5':
        cnt = 0
        for i in range(len(Spisok)):
            q = str(Spisok[i])
            if len(q) > 9:
                q = q.split(',')
                cnt += 1
                print(cnt, '-', q[0])
            else:
                continue
        x = int(input())
        if x > 0:
            cnt = 0
            for i in range(len(Spisok)):
                q = str(Spisok[i])
                if len(q) > 9:
                    q = q.split(',')
                    cnt += 1
                    if cnt == x:
                        continue
                    else:
                        Machine.model = q[0]
                        Machine.engine = q[1]
                        Machine.akum = q[2]
                        Machine.kpp = q[3]
                        Machine.color = q[4]
                        deletes.write(
                            Machine.model + ',' + Machine.engine + ',' + Machine.akum + ',' + Machine.kpp + ',' + Machine.color + ',\n')
                else:
                    continue

            saves.close()
            deletes.close()
            os.remove('Save.txt')
            os.rename('Deletes.txt', 'Save.txt')

    elif a == '6':
        Ldoor = '[ ]'
        Rdoor = '[ ]'
        Lights = '[ ]'
        Lwind = '[ ]'
        Rwind = '[ ]'
        while True:
            print(
                '1.Фары: ' + Lights + '\n'
                                      '2.Левая дверь: ' + Ldoor + '\n'
                                                                  '3.Правая дверь: ' + Rdoor + '\n'
                                                                                               '4.Левое окно: ' + Lwind + '\n'
                                                                                                                          '5.Правое окно: ' + Rwind + '\n'
                                                                                                                                                      '0 для выхода \n')
            breloque = int(input())

            if breloque == 1:
                if Lights == '[ ]':
                    Lights = '[X]'
                else:
                    Lights = '[ ]'

            if breloque == 2:
                if Ldoor == '[ ]':
                    Ldoor = '[X]'
                else:
                    Ldoor = '[ ]'
            if breloque == 3:
                if Rdoor == '[ ]':
                    Rdoor = '[X]'
                else:
                    Rdoor = '[ ]'
            if breloque == 4:
                if Lwind == '[ ]':
                    Lwind = '[X]'
                else:
                    Lwind = '[ ]'
            if breloque == 5:
                if Rwind == '[ ]':
                    Rwind = '[X]'
                else:
                    Rwind = '[ ]'
            if breloque == 0:
                break

    elif a == '7':
        d = saves.tell()
        print('введите кол-во машин')
        k = int(input())
        starttime = time.time()
        for a1 in range(k):
            a2 = str(a1 + 1)
            saves.write(a2 + ',' + 'engine' + ',' + 'akum' + ',' + 'kpp' + ',' + 'color' + ',\n')
        fulltime = time.time() - starttime
        deletes.close()
        saves.close()



    elif a == '8':
        cnt=0
        for a1 in range(len(Spisok)):
            q = str(Spisok[a1])
            if len(q) > 9:
                q = q.split(',')
                cnt += 1
                k=q[0]
        deletes.close()
        saves.close()
        print('---------------------------------------------------------------')
        print('последняя конфигурация в списке имеет номер',k,('всего машин',cnt))
        print('---------------------------------------------------------------')
