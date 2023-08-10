class parent1:
    def p1(self):
        print("this is parent1 function")
class parent2(parent1):
    def p1(self):
         print("this is parent2 class function")
class child1(parent1):
    def p1(self):
        print("this is child1 class")
class child2(parent2,child1):
    def p1(self):
        print("this is child2 function")
obj = child2()
obj.p1()
parent2.p1(obj)
child1.p1(obj)
child2.p1(obj)