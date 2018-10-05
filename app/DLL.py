#!/home/maria/quack/venv/bin/python

class DoubleLinkedListCell(object):        #класс ячейки двусвязного списка                       
    def __init__(self, elem = None, prev__item= None, next__item = None):   #data - содержимое ячейки , prevc - предыдущая ячейка , nextc - следующая ячейка
        self.elem = elem
        self.prev__item = prev__item
        self.next__item = next__item

class DoubleLinkedList(object):                                    #класс двусвязного списка
    def __init__(self, first__item = None, last__item = None, length = 0):     #first - начало списка, last - конец списка, length -  длина списка
        self.first__item = first__item
        self.last__item = last__item
        self.length = length

    def len(self):                                              #вывод длины списка
       return self.length


    def unshift(self, x):                                   #добавление ячейки в начало списка   
        self.length = self.length + 1;
        if self.first__item == None: 
            self.first__item = DoubleLinkedListCell(x, None, None);       
            self.last__item = self.first__item;
        else:
            self.first__item = DoubleLinkedListCell(x, None, self.first__item);
            self.first__item.next__item.prev__item = self.first__item
            
    def push(self, x):                                         #добавление ячейки в конец списка
        self.length = self.length + 1;
        if self.first__item == None:
            self.first__item = DoubleLinkedListCell(x, None, None)
            self.last__item = self.first__item
        elif self.first__item == self.last__item: 
            self.last__item = DoubleLinkedListCell(x, self.first__item, None)
            self.first__item.next__item = self.last__item

        else:
            current = DoubleLinkedListCell(x, self.last__item, None)
            self.last__item.next__item = current;
            self.last__item = current;


    def addTo(self, x, i):            #добавление на определенное место i
        self.length = self.length + 1;
        if self.first__item  == None:
            self.first__item = DoubleLinkedListCell(x, None, None);
            self.last__item = self.first__item
        elif i == 0:
            self.first__item = DoubleLinkedListCell(x, None, self.first__item)
            self.first__item.next__item.prev__item = self.first__item
        else:
            current = self.first__item;
            count = 0;
            while current != None:
                #print('c:',count)
                if count == i - 1:
                    #print('found')
                    if current.next__item == None:
                        current.next__item = DoubleLinkedListCell(x, current, current.next__item)
                        #print(1,current.next__item.elem)
                        self.last__item = current.next__item
                    else:
                        #print(2,current.next__item.elem)
                        current.next__item = DoubleLinkedListCell(x, current, current.next__item)
                        current.next__item.next__item.prev__item = current.next__item
                    break;
                count = count + 1
                current = current.next__item            
                

    def shift(self):                    #удаление первой ячейки
        if self.first__item.next__item == None:
            self.length = 0
            self.first__item =  None
            self.last__item = None
        else:
            self.length = self.length - 1
            self.first__item = self.first__item.next__item
            self.first__item.prev__item = None;



    def deleteFrom(self, i):                             #удаление ячейки с номером i
        if (self.first__item == None):
            print("DoubleLinkedList is empty")
        elif ((self.first__item == self.last__item) and (i == 0)):
            self.length = 0
            self.first__item = None
            self.last__item = None
        else:
            current = self.first__item;
            count = 0;
            if self.length > i:
                self.length = self.length - 1;
                while current != None:
                    if count == i - 1:
                        if current.next__item.next__item == None:
                            self.last__item = current.last__item
                        else:
                            current.next__item = current.next__item.next__item
                            current.next__item.prev__item = current
                        break;
                    current = current.next__item



    def give(self, i):                          #вывод ячейки с номером i
        if self.length < i:
            return None
        else:
            current = self.first__item
            count = 0;
            while current != None:
                if count == i:
                    return current.elem
                    break
                current = current.next__item
                count = count + 1
   

    def find(self,i):                           #поиск всех элементов с заданным значением и возвращение множества индексов
        count = 0
        current = self. first__item
        res = set()
        while count < self.length:
            if current.elem == i:
                res.add(count)
            count = count + 1
            current = current.next__item
        return res



    def delete(self,i):                             #удаление ячеек со значением i
        if ((self.length == 1) and (self.first__item.elem == i)):
            self.length = 0
            self.first__item = None
            self.last__item = None
        elif (self.length > 1):
            count = 0
            deleted = 0  
            current = self.first__item
            while count < self.length:
                if current.elem == i:
                    if count == 0:
                        self.first__item = self.first__item.next__item
                        self.first__item.prev__item = None

                    elif current == self.last__item:
                        self.last__item.prev__item.next__item = None
                        self.last__item = self.last__item.prev__item
                        

                    else:
                        current.prev__item.next__item = current.next__item
                        current.next__item.prev__item = current.prev__item
                    deleted = deleted + 1

                count = count + 1
                current = current.next__item

            self.length = self.length - deleted        
  

    def contains(self,i):                         #проверяет, есть ли ячейки со значением i
        count = 0
        res = False
        current = self. first__item
        while count < self.length:
            if current.elem == i:
                res = True
                break
            count = count + 1
            current = current.next__item
        return res


    def first(self):                              #возвращает  первый элемент
        return self.first__item
        
    def last(self):                               #возвращает последний элемента
        return self.last__item


    def pop(self):
        if self.length == 0:
            return None
        elif self.last__item == self.first__item:
            self.length = 0
            self.first__item = None
            self.first__item = None
        else:
            self.length = self.length - 1
            self.last__item = self.last__item.prev__item
            self.last__item.next__item = None


