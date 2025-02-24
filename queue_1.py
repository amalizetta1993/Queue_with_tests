"""Модуль организации очереди и работы с ней.

В модуле есть класс очереди Queue со следующими методами:
    - метод инициализации __init__
    - метод enqueue (добавляет элемент в очередь)
    - метод enqueue (удаляет элемент из очереди)
    - метод show (выводит данные всей очереди)
    - метод isEmpty (проверяем, есть ли данные в очереди)
    - метод isFull (проверяем, заполнилась очередь целиком)
 
"""

class Queue:

    def __init__(self, size, queue=None):
        self.__size = size
        if not queue:
            self.__queue = []
        else:
            self.__queue = queue
            
    def isFull(self):
        if len(self.__queue) == self.__size:
            print('Очередь заполнилась')
            return True
        else:
            return False   
    
    def enqueue(self, data):
        if data == 'Очередь пуста':
            return
        if self.isFull() == False:
            self.__queue.append(data)
        
    def dequeue(self):
        if not self.__queue:
            return 'Очередь пуста'
        return self.__queue.pop(0)
    
    def show(self):
        return print(f'Данные очереди: {self.__queue}')
    
    def isEmpty(self):
        if len(self.__queue) == 0:
            print('Очередь пуста')
            return True
        print('В очереди есть данные')
        return False
if __name__ == '__main__':
    print('Приложение для создания и работы с очередью')  
    f = int(input('Создайте свою очередь. Напишите размер очереди: '))
    k = list(input('Напишите данные для очереди: '))    
    q = Queue(f, k)
    act = ''
    while act != '0':
        print('')
        act = input('''Что вы хотите сделать с очередью?
                isFull (проверить, заполнена ли очередь)
                enqueue (добавить данные в очередь)
                dequeue (удалить данные из очереди)
                show (показать все данные в очереди)
                isEmpty (проверить, пустая очередь или нет)
                0 - для выхода из программы
                
                ''')
        if act == 'isFull':
            q.isFull()
        elif act == 'enqueue':
            q.enqueue(input('Введите данные: '))
        elif act == 'dequeue':
            q.dequeue()
        elif act == 'show':
            q.show()
        elif act == 'isEmpty':
            q.isEmpty()
        print('')
            
