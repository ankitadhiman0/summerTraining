class grandparent:
    def GPprint():
        print("this is grandparent function")
class parent(grandparent):
    def Pprint():
        print("this is a parent class function")

class child(parent):
    def Cprint():
        print("this is parent class function")
cobj = child
cobj.Pprint()
cobj.GPprint()

        
    
    