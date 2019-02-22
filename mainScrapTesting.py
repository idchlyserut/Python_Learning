
class custList:
     def __init__(self,x):
         self.val = x
     def eir(self):    
      return range(len(self.val))
               

nameList = ["John"] # array.. list in python;
firstNameList = custList(["david","greg","will"])
lastNameList = custList(["Rut", "Smith", "Chapman", "Greens", "Durian"]) 
def eir(a): #makes a list of int for the loop to assign
     if isinstance(a, list):
      return range(len(a))
def findIdiey():
     f = []
     for x in firstNameList.eir():
       if firstNameList.val[x] is "Idiey":
          f.append(x)
          break 
     for y in lastNameList.eir():
       if lastNameList.val[y] is "Rut":
          f.append(y)
          break     
     return f 
     
def fullNameMix(f,l):
     return firstNameList.val[f] + lastNameList.val[l]


def strend(inp, comp):
    if len(comp)>len(inp):
        return 0
    else:    
        i = 1
        while i<=len(comp):
            j = 1
            if inp[len(inp)-i] != comp[len(comp)-i]:
                j = 0
                break
            i+=1
        return j  
    
def main():
    
    print("Hello world")
    nameList.append("Jackson")    
    for x in eir(nameList): 
     print(nameList[x])
    for y in firstNameList.eir():
         print(firstNameList.val[y])
    firstNameList.val.extend(["Idiey","popschin"])
    for y in firstNameList.eir():
         print(firstNameList.val[y])
    for x in range(len(firstNameList.val[len(firstNameList.val)-1])):
         print(firstNameList.val[len(firstNameList.val)-1][x])  
    Id = findIdiey()
    person = fullNameMix(3,0)
    if strend(person, lastNameList.val[Id[1]]) == 1:
      if strend(person[0:(len(person)-len(lastNameList.val[Id[1]]))], firstNameList.val[Id[0]])==1:
        print("*GASP* hhheyyy candy beetlleee~~~ <3") 
      else:
       print("Hawi Idiey... sib?")     
    else:
      print("Hi. ._.")             
main()

