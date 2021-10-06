import multiprocessing
import os
import random
import threading
import time


class Singleton: 
    ''' limits instance of class to one <-- break this case without "thread" lock
    '''
    _instance = "GeeksforGeeks"
    # def __new__(cls, *args, **kwargs): 
    #     if cls._instance is None: 
    #         cls._instance = super().__new__(cls) 
    #     return cls._instance
    
    # def __init__(self, ret_value):
    #     ret_value.value = id(self._instance)
    #     print(ret_value.value)
    #     print(f'pid: {os.getpid()}, __init__ done for {id(self)}')
    @staticmethod
    def getInstance():
 
        """Static Access Method"""
        if Singleton._instance == 'GeeksforGeeks':
            Singleton()
        return Singleton._instance
 
    def __init__(self):
 
        """virtual private constructor"""
        if Singleton._instance != 'GeeksforGeeks':
            raise Exception ("This class is a singleton class !")
        else:
            Singleton._instance = self

            print('Singleton instance:', id(Singleton._instance))  # delete me

# inst = Singleton()
# inst2 = Singleton()
# assert inst == inst2

def fail_singleton(n):
    for i in range(n):
        # thread_i = threading.Thread(
        #     target=Singleton
        # )
        # thread_i.start()
        proc_i = multiprocessing.Process(
            target=Singleton.getInstance,
        )
        proc_i.start()

# fail_singleton(2)


import threading
 
class SingletonDoubleChecked(object):
 
    # resources shared by each and every instance
 
    __singleton_instance = None
 
    @classmethod
    def instance(cls):

        if not cls.__singleton_instance:
            cls.__singleton_instance = cls()
 
        return cls.__singleton_instance
 
# main method
if __name__ == '__main__':
 
    # create class X
    class X(SingletonDoubleChecked):
        pass
 
    # create class Y
    class Y(SingletonDoubleChecked):
        pass
 
    A1, A2 = X.instance(), X.instance()
    B1, B2 = Y.instance(), Y.instance()
 
    assert A1 is not B1
    assert A1 is A2
    assert B1 is B2
 
    print('A1 : ', A1)
    print('A2 : ', A2)
    print('B1 : ', B1)
    print('B2 : ', B2)
        