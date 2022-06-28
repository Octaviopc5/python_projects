import time


class FiboIter():
     
     
    def __init__(self, max_number:int):
        self.max_number = max_number

     #we need to creat the elements needed for the iterator
     # and the retunr the object itself in iter
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter +=1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux =self.n1 + self.n2
            
            #We declare a limit for our iterator, otherwise its infinite
            if self.aux >= self.max_number:
                raise StopIteration

            #self.n1 = self.n2
            #self.n2 = self.aux
            #More simplistic way of coding it
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

if __name__ == "__main__":
    fibonacci = FiboIter(5000)
    
    for element in fibonacci:
        print(element)
        time.sleep(0.1)



