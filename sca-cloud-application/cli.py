import sys
from sys import platform
 
if sys.platform =="linux" or platform== "linux2":
   print ("The os is Linux")
   
elif sys.platform =="darwin":
   print ("The os is Windows")
   
else:
 sys.platform =="win32"
 print ("The os is Mac")
  
# args = sys.argv[1:]
# def install_software(self):
#  for arg in args:
#   print('softwares installed are:{}'.format(len(args)))
  
# software = ["node.js"]

# if __name__== "__main__":
#    software()

