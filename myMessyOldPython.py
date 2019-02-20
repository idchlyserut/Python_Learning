"""

Needs to be run in Processing tho ._.

"""
def readFile(a):
   with open(a) as f:
    res = [[x for x in ln.split()] for ln in f];
    for i in range(len(res)):
       for j in range(len(res[i])):
           try:
               res[i][j] = int(res[i][j]);
           except:
               continue;
    f.close();        
   return res;

def writeFile(a, l):
   q="";
   f = open(a, "w");
   for i in range(len(l)):
      for j in range(len(l[i])):
       if j <= len(l[i]):
        q = q+" "+str(l[i][j]);
       if j==0:
        q = str(l[i][j]);
       if j+1 == len(l[i]):
        f.write(q+"\n");
   q="";
   f.close();
def drawGif(pos, path, name, a, frames):
    if pos[2]:
        image(loadImage(path+name+str(a)+'.png'), pos[0], pos[1], pos[2], pos[3]);
    else:
        image(loadImage(path+'/'+name+str(a)+'.png'), pos[0], pos[1], 100, 100);
    a += 1;
    return a;
def overRect(x, y, w, h):
  if mouseX >= x and mouseX <= x+w and mouseY >= y and mouseY <= y+h:
    return 1;
  else:
    return 0;

def clearScr():
    fill(255,255,255);
    rect(0,0,width,height);
    fill(0,0,0); 
    
def ItemRender(currentFIndex, pos): # gives an array with all info needed for rendering an item in the fridge
    age = readFile('data/age.txt')
    item = currentF[currentFIndex]; # item is to get the Item in question from currentF
    # sytax of res = [(item type{cake, slice etc.}), (number of), (age array)]
    
    # ----- Build item information array -----
    
    itemInfo = [info[item[0]][3], item[1]];
    # a and b simplify the following loop
    a = age[currentFIndex];
    b = float(info[item[0]][2]);
    itemInfo.append(a);    
        # color gradiant equations are used below (added too end of item info)
    for i in range(len(a)):
        af = float(a[i]);        
        itemInfo[2][i] = [round((af/b)*255+100), round((af/b)*-255+255)];
    # ----- Build render array for all positions and dimentions of each peice relative to position of item ------
    
    res = []; # final render array
    k = 0;
    if itemInfo[0] == 0: # square slice
        w = int(round(len(itemInfo[2])/2))+1;       
        for i in range(w):
            e = [];
            if i == 0:
                e.append(itemInfo[2][k]);
                k+=1;
            else:
                for j in range(2):                                 
                    if k < len(itemInfo[2]):
                        e.append(itemInfo[2][k]);
                        k+=1;
            res.append(e);
        final = [];
        dim = [];
        for i in range(len(res)):
            for j in range(len(res[i])):
                if i == 0:
                    dim = [25*j+pos[0]+10, 25*i+pos[1], 20, 20, res[i][j]];
                else:
                    dim = [25*j+pos[0], 25*i+pos[1], 20, 20, res[i][j]];
                final.append(dim);
        res = final;
    elif itemInfo[0] == 1: # circluar cake
        res=[];
    elif itemInfo[0] == 2: # skinny slice
        res = itemInfo[2];
        final = [];
        dim = [];
        for i in range(len(res)):
                dim = [pos[0], 20*i+pos[1], 50, 15, res[i]];
                final.append(dim);
        res = final;
    elif itemInfo[0] == 3: # cake slice  
        res = itemInfo[2];
        final = [];
        dim = [];
        for i in range(len(res)):
                dim = [pos[0], 25*i+pos[1], 50, 20, res[i]];
                final.append(dim);
        res = final;    
    elif itemInfo[0] == 4: # tart
        for i in range(len(itemInfo[2])):
            e = [];
            for j in range(1):                
                if k < len(itemInfo[2]):
                    e.append(itemInfo[2][k]);
                    k+=1;
            res.append(e);
        final = [];
        dim = [];
        for i in range(len(res)):
            for j in range(len(res[i])):
                if (i%2) == 0:
                    dim = [25*j+pos[0]+10, 25*i+pos[1]+10, 25, 25, res[i][j]];
                else:
                    dim = [25*j+pos[0]+35, 25*i+pos[1]+10, 25, 25, res[i][j]];
                final.append(dim);
        res = final;
    
    # ----- Draw Item on canvus ------
    
    if itemInfo[0] == 0 or itemInfo[0] == 2 or itemInfo[0] == 3:
        for i in range(len(res)):
            # if the age is 0(just taken out of the freezer) fill blue
            if res[i][4][0] == 100.0 and res[i][4][1] == 255.0:
                 fill('0x7DA6FC'); 
            else:
                fill(res[i][4][0], res[i][4][1], 0);               
            rect(res[i][0],res[i][1]-10,res[i][2],res[i][3]);
    if itemInfo[0] == 4:
        for i in range(len(res)):
            if res[i][4][0] == 100.0 and res[i][4][1] == 255.0:
                 fill('0x7DA6FC');
            else: 
                fill(res[i][4][0], res[i][4][1], 0);               
            ellipse(res[i][0],res[i][1]-10,res[i][2],res[i][3]);
    print(res);

def loadFridge():
    res = [];
    oldAlert = [];
    age = readFile('data/age.txt');
    print(currentF);
    for i in range(len(currentF)):
       refId = currentF[i][0];
       amountNeeded = info[refId][1] - currentF[i][1];
       pres = [info[refId][0], amountNeeded];
       res.append(pres);
       a=0
       for j in range(len(age[i])):
          if age[i][j] >= info[refId][2]:
             a += 1;
       if a > round(currentF[i][1]*(2/3)):
          oldAlert.append([refId, a]);
    x = 100;
    y = 100;  
    text(' ---- Restock List ---- ',x,y);
    y = y+25;
    for i in range(len(res)):
       if int(res[i][1]) > 0:
          text(str(res[i][1])+'x '+ res[i][0],x,y);
          y = y + 25;
       if int(res[i][1]) < 0:
          text(str(res[i][0])+' over stock by '+str(-1*res[i][1]),x,y);
          y = y + 25;
    if len(oldAlert):
       text(' !-- Fridge Life Warning for:',x,y)
       y = y + 25;
       for i in range(len(oldAlert)):
          text(info[oldAlert[i][0]][0]+', '+ str(oldAlert[i][1])+' of them are over fridge life.',x,y);
          y = y + 25;
    class d:
        def act(self):
            global clickableFields;
            clickableFields = [];
            restockCheckOff();
    e = d();        
    clickableFields.append(Button(x+10,y+30, 175, 40, '0x44F291', e));
    text('Proceed to Restock List', x+15, y + 55);
       

        
        
def checkAge():    
    age = readFile('data/age.txt');
    alert = [];
    for i in range(len(age)):
       for j in range(len(age[i])):
          if age[i][j] > info[currentF[i][0]][2]:
             alert.append([currentF[i][0], currentF[i], age[i]]);
    return alert;

def drawFridge(fridgeRenderPos):
    clearScr()
    class a:
        def act(self):
            global clickableFields;
            clickableFields = [];
            checkFridge(0);
    class b:
        def act(self):
            global clickableFields;
            clickableFields = [];
            mainMenu();
    c = a();
    d = b();
    clickableFields.append(Button(10,10,50,50,'0x989898',c));
    clickableFields.append(Button(960,960,50,50,'0x6D3DBC',d));    
    text('Make a fridge item count..', 70, 25);
    text('Main Menu', 875, 985);
    fill('0x828290')
    for i in range(3):
        rect(fridgeRenderPos[0], fridgeRenderPos[1]+200*i, 400, 150)
    shelfCon = readFile('data/shelfCon.txt');
    pos = [0,0];
    for i in range(len(shelfCon)):
        pos[1] = fridgeRenderPos[1]+50+200*i;
        pos[0] = 0;
        for j in range(len(shelfCon[i])):
            pos[0] = fridgeRenderPos[0]+50+100*j;
            ItemRender(shelfCon[i][j], pos);
    fill(0,0,0)        
def restockCheckOff():
    global clickableFields;
    clickableFields = [];
    clearScr();
    
    
class inital:
     def act(self):
        a = ''.join(currentTextField.currentText);        
        currentTextField.currentText = [];
        print(a)        
        return a;           
class TextField:
    def __init__(self,x,y,func):
        self.pos = [x,y];
        if(func != 0):
            self.enter = func;            
        else:            
            self.enter = inital();    
        self.currentText = [];


def keyPressed():
    fill(255,255,255);
    noStroke();
    rect(currentTextField.pos[0], currentTextField.pos[1]-15, 10*len(currentTextField.currentText), 25 )
    fill(0,0,0);
    stroke(0,0,0); 
    if currentTextField:
        print(keyCode)
        if int(keyCode) == 8:
            try:
                currentTextField.currentText.pop(len(currentTextField.currentText)-1);
            except:
                print('error- No text in field to delete')
        elif int(keyCode) == 10:
            a = currentTextField.enter.act();   
        elif int(keyCode) != 17 and int(keyCode) != 16:        
            currentTextField.currentText.insert(len(currentTextField.currentText), key);
            print(currentTextField.currentText);        
        for x in range(len(currentTextField.currentText)):    
            text(currentTextField.currentText[x], currentTextField.pos[0]+10*x, currentTextField.pos[1]);
    else:
        rect(0,0,100,100);
        
def mousePressed(): 
    for i in range(len(clickableFields)):       
        if overRect(clickableFields[i].x, clickableFields[i].y, clickableFields[i].w, clickableFields[i].h) == 1:
            clickableFields[i].clicked.act();
            break;

class Button:
    def __init__(self,x,y,w,h,c,func):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;
        self.colour = c;
        self.clicked = func;
        fill(c);
        rect(x,y,w,h);
        fill(0,0,0);
        
def mainMenu():
    global clickableFields;
    clearScr();
    textSize(20);
    fill('0x6A0F0F')
    text('~Select Function~', 40,40)
    fill(0,0,0)
    textSize(15)
    class a:
        def act(self):
            global clickableFields;
            clickableFields = [];
            checkFridge(0);
    class b:
        def act(self):
            global clickableFields;
            clickableFields = [];
            drawFridge([500, 100]);
            loadFridge();
            
    c = a();
    d = b();
    clickableFields = [Button(50,60,50,50,'0x989898',c), Button(50,120,50,50,'0x989898',d)];
    text('Make a fridge item count..', 125,80);
    text('Display restock list and age heat map..',125,140);
def setup():    
    global info, currentF, currentFz, currentTextField, clickableFields;
    info = readFile('data/Info.txt');
    currentF = readFile('data/currentF.txt');
    currentFz = readFile('data/currentFz.txt');
    size(1000, 1000);
    background(255,255,255);
    currentTextField = TextField(100,700,0)    
    mainMenu();   
def draw():
    return 0;
class checked:
    def __init__(self, x):
        self.num = x;
    def act(self):
        print(self.num)
        global currentTextField
        a = ''.join(currentTextField.currentText);                   
        currentTextField.currentText = [];
        print(currentTextField.currentText)
        count = int(a);
        currentF[self.num][1] = count;
        if(self.num < 4):
            b = self.num
            checkFridge(b+1);
        else:
            e = readFile('data/currentF.txt');
            # update the freezer of any unexpected counts before saving currentf to data
            updateFreezer(e, currentF)
            writeFile('data/currentF.txt', currentF);
            updateAge();
            currentTextField = TextField(0,0,0);
            fill(255,255,255);
            rect(0,0,width,height);
            fill(0,0,0); 
            drawFridge([500, 100]);    
            loadFridge();
def updateFreezer(preF, curF):
    global currentFz;
    print(currentFz);
    for i in range(len(curF)):
        a = 0;
        if curF[i][1] > preF[i][1]:            
            print(info[curF[i][0]][0]);            
            for j in range(len(currentFz)):
                if currentFz[j][0] == curF[i][0]:
                    if currentFz[j][1] <= 0:
                        print('!-- ERROR impossible count recorded, no more of '+info[curF[j][0]][0]+' to be added from prev count');
                        a = a+1;
                        break;
                    else:
                        currentFz[j][1] = currentFz[j][1] - (curF[i][1]-preF[i][1]);
                        a = a+1;
                        break;
        if a == 0:
            print('!-- ERROR impossible count recorded, no more of item to be added from prev count')        
    print(currentFz);
    return 0;
def updateAge():
    age = readFile('data/age.txt')
    for i in range(len(age)):
        if currentF[i][1] < len(age[i]):
            for x in range(len(age[i])-currentF[i][1]):
                age[i].pop();
        elif currentF[i][1] > len(age[i]):
            print('Unexpected count of item '+info[currentF[i][0]][0]+', '+str(currentF[i][1]-len(age[i]))+' greater then last recorded')
            for x in range(currentF[i][1]-len(age[i])):
                age[i] = [0] + age[i]
                
    writeFile('data/age.txt', age);
class b:
        def act(self):
            global clickableFields;
            clickableFields = [];
            drawFridge([500, 100]);
            loadFridge();
def checkFridge(x):
    global currentTextField, clickableFields;
    d = b();  
    clearScr();   
    text('Number of ' + info[currentF[x][0]][0] + ': ',80,700) 
    clickableFields = [Button(40,690,20,20,'0x717070',checked(x)), Button(300,690,30,30,'0xF24949',d)];   
    currentTextField = TextField(100,800,checked(x))
    
