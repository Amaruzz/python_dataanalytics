class Demo:
    def __init__(self):
        self.name="Amarjith"  #Public
        self._age=21          #Protected
        self.__salary=50000    #Private

    def show(self):
        print("Inside the class")
        print("Public:",self.name )
        print("Protected:",self._age )
        print("Private:",self.__salary )


obj=Demo()
print(obj.show())      