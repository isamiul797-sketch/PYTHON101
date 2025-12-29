from abc import ABC , abstractmethod

class Father(ABC): 

    @abstractmethod
    def vote(self):
        pass

class Son(Father):
    def vote(self):
        print("Vote for ABC")


obj = Son()
print(obj.vote())