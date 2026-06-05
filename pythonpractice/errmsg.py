import traceback


try :
    int("hello")
except ValueError as e :
    #print(type(e).__name__)
     print(str(e))
    #print(traceback.print_exc())
