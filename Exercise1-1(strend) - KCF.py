t = ['T','a','d','o',' ','i','s',' ','t','h','e',' ','c','a','n','d','y',' ','b','e','e','t','l','e']
#d = ['S','p','u','d',' ','l','i','k','e','s',' ','t','o',' ','e','a','t',' ','b','e','e','t','l','e']
a = ['b','e','e','t','l','e']

#Write a function strend(t,a), which returns 1 if the list a occurs at the end of the list t, and zero otherwise

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
print(strend(t,a))