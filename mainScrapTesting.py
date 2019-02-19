nameList = ["John"] # array.. list in python;

def eir(a): #makes a list of int for the loop to assign
     if isinstance(a, list):
      return range(len(a))

def main():
    print("Hello world")
    nameList.append("Jackson")    
    for x in eir(nameList): 
     print(nameList[x])

main()

