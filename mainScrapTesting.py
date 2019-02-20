
class custList:
     def __init__(self,x):
         self.val = x
     def eir(self):    
      return range(len(self.val))
               

nameList = ["John"] # array.. list in python;
testNameList = custList(["david","greg","will"])

def eir(a): #makes a list of int for the loop to assign
     if isinstance(a, list):
      return range(len(a))

def main():
    print("Hello world")
    nameList.append("Jackson")    
    for x in eir(nameList): 
     print(nameList[x])
    for y in testNameList.eir():
         print(testNameList.val[y])
    testNameList.val.extend(["idiey","popschin"])
    for y in testNameList.eir():
         print(testNameList.val[y])      
main()
