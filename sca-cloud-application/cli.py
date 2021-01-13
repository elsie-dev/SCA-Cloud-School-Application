import sys
from sys import platform


def main():
    print('in main')
    # args = sys.argv[1:]
    # print('count of args :: {}'.format(len(args)))
    # for arg in args:
    #     print('passed argument :: {}'.format(arg))

    # my_function('hello world')

    # my_object = MyClass('Thomas')
    # my_object.say_name()


    
if sys.platform =="linux" or platform== "linux2":
   print ("linux")
   
elif sys.platform =="darwin":
   print ("windows")
   

else:
 sys.platform =="win32"
 print ("mac")
  



if __name__== "__main__":
    main()