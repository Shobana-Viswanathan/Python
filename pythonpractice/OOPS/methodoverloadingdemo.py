class Example:
    def method(self,a,b=None):
        if b is None:
            print("single argument:{a}")
        elif isinstance(a,str) and isinstance(b,str):
            print("Two strings:{a},{b}")
        else:
            print(f"Mixed types:{a},{b}")
obj=Example()
obj.method(1)
obj.method(1,2)
obj.method("hello","world")
obj.method(1,"world")

   