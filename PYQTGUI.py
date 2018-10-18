import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import pyqtSlot
import time
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'CALCULATOR'
        self.left = 300
        self.top = 300
        self.width = 500
        self.height = 500
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: black");
        button1 = QPushButton('1', self)
        button1.setStyleSheet("background-color: red");
       
        button1.move(100,120)
        button1.resize(60,60)
        button3 = QPushButton('3', self)
        button3.setStyleSheet("background-color: red");
       
        button3.move(220,120)
        button3.resize(60,60)
        button4 = QPushButton('4', self)
        button4.setStyleSheet("background-color: red");
       
        button4.move(100,180)
        button4.resize(60,60)
        button5 = QPushButton('5', self)
        button5.setStyleSheet("background-color: red");
       
        button5.move(160,180)
        button5.resize(60,60)
        button6 = QPushButton('6', self)
        button6.setStyleSheet("background-color: red");
      
        button6.move(220,180)
        button6.resize(60,60)
        button7 = QPushButton('7', self)
        button7.setStyleSheet("background-color: red");
       
        button7.move(100,240)
        button7.resize(60,60)
        button8 = QPushButton('8', self)
        button8.setStyleSheet("background-color: red");
      
        button8.move(160,240)
        button8.resize(60,60)
        button2 = QPushButton('2', self)
        button2.setStyleSheet("background-color: red");
      
        button2.move(160,120)
        button2.resize(60,60)
        button9 = QPushButton('9', self)
        button9.setStyleSheet("background-color: red");
       
        button9.move(220,240)
        button9.resize(60,60)
        button0 = QPushButton('0', self)
        button0.setStyleSheet("background-color: red");
      
        button0.move(220,300)
        button0.resize(60,60)
        buttonp = QPushButton('+', self)
        buttonp.setStyleSheet("background-color: red");
       
        buttonp.move(300,120)
        buttonp.resize(60,60)
        buttona = QPushButton('AND', self)
        buttona.setStyleSheet("background-color: red");
      
        buttona.move(300,180)
        buttona.resize(60,60)
        
        buttono = QPushButton('OR', self)
        buttono.setStyleSheet("background-color: red");
      
        buttono.move(300,240)
        buttono.resize(60,60)
        buttonc = QPushButton('2\'C', self)
        buttonc.setStyleSheet("background-color: red");
       
        buttonc.move(300,300)
        buttonc.resize(60,60)
        buttone = QPushButton('=', self)
        buttone.setStyleSheet("background-color: red");
       
        buttone.move(160,300)
        buttone.resize(60,60)
        buttonac = QPushButton('AC', self)
        buttonac.setStyleSheet("background-color: red");
      
        buttonac.move(100,300)
        buttonac.resize(60,60)
        












        self.textbox = QLineEdit(self)
        self.textbox.setStyleSheet("background-color: white");
        self.textbox.move(100,60)
        
        self.textbox.resize(260,60)
        self.timeDisplay = QLCDNumber(self.textbox)
        self.timeDisplay.setDigitCount(1)
        self.timeDisplay.display('0')
        self.timeDisplay.resize(260,60)
        self.textbox2= QLineEdit(self)
        self.textbox2.setStyleSheet("background-color: white");
        self.textbox2.move(100,400)
        self.textbox2.resize(260,60)
        

        
     
       
        
 

        self.show()
        button1.clicked.connect(self.on_click1)
        button2.clicked.connect(self.on_click2)
        button3.clicked.connect(self.on_click3)
        button4.clicked.connect(self.on_click4)
        button5.clicked.connect(self.on_click5)
        button6.clicked.connect(self.on_click6)
        button7.clicked.connect(self.on_click7)
        button8.clicked.connect(self.on_click8)
        button9.clicked.connect(self.on_click9)
        button0.clicked.connect(self.on_click0)
        buttonp.clicked.connect(self.on_clickp)
        buttona.clicked.connect(self.on_clicka)
        buttono.clicked.connect(self.on_clicko)
        buttonc.clicked.connect(self.on_clickc)
        buttone.clicked.connect(self.on_clicke)
        buttonac.clicked.connect(self.on_clickac)




    @pyqtSlot()
    def on_click1(self):
       
        
        self.timeDisplay.display('1')
        f=open("D:\\input.txt", "a+")
        f.write("1 ")
        f.close()
        

    @pyqtSlot()
    def on_click2(self):
        f=open("D:\\input.txt", "a+")
        f.write("2 ")
        f.close()
        text=QLCDNumber(self.textbox)
        #self.textbox.setText("2")
        self.timeDisplay.display('2')
    @pyqtSlot()
    def on_click3(self):
        f=open("D:\\input.txt", "a+")
        f.write("3 ")
        f.close()
        self.timeDisplay.display('3')
    @pyqtSlot()
    def on_click4(self):
        f=open("D:\\input.txt", "a+")
        f.write("4 ")
        f.close()
        self.timeDisplay.display('4')
    @pyqtSlot()
    def on_click5(self):
        f=open("D:\\input.txt", "a+")
        f.write("5 ")
        f.close() 
        self.timeDisplay.display('5')
    @pyqtSlot()
    def on_click6(self):
        f=open("D:\\input.txt", "a+")
        f.write("6 ")
        f.close() 
        self.timeDisplay.display('6')
    @pyqtSlot()
    def on_click7(self):
        f=open("D:\\input.txt", "a+")
        f.write("7 ")
        f.close() 
        self.timeDisplay.display('7')
    @pyqtSlot()
    def on_click8(self):
        f=open("D:\\input.txt", "a+")
        f.write("8 ")
        f.close() 
        self.timeDisplay.display('8')
    @pyqtSlot()
    def on_click9(self):
        f=open("D:\\input.txt", "a+")
        f.write("9 ")
        f.close() 
        self.timeDisplay.display('9')
    @pyqtSlot()
    def on_click0(self):
        f=open("D:\\input.txt", "a+")
        f.write("0 ")
        f.close() 
        self.timeDisplay.display('0')
    @pyqtSlot()
    def on_clickp(self):
        f=open("D:\\input.txt", "a+")
        f.write("+ ")
        f.close() 
    @pyqtSlot()
    def on_clicka(self):
        f=open("D:\\input.txt", "a+")
        f.write("& ")
        f.close() 
    @pyqtSlot()
    def on_clicko(self):
        f=open("D:\\input.txt", "a+")
        f.write("| ")
        f.close()
    @pyqtSlot()
    def on_clickc(self):
        f=open("D:\\input.txt", "a+")
        f.write("2scomplement")
        f.close()
    @pyqtSlot()
    def on_clicke(self):
        f=open("D:\\input.txt", "r")
        line=f.read()
        f.close()
        num1=0
        num2=0
        op=str()
        instruction=[]
        wordlist=line.split(" ")
        num1=int(wordlist[0])
        op=wordlist[1]
        if(op!="2scomplement"):
            num2=int(wordlist[2])
        else:num2=="0000"
        str1=str(bin(num1))
        str2=str(bin(num2))
        z1=6-len(str1)
        z2=6-len(str2)
        newstr1="0"*z1+str1[2:len(str1)]
        newstr2="0"*z2+str2[2:len(str2)]
        instruction.append(newstr1)
        
        instruction.append(newstr2)
       
        if(op=="+"):
            
            instruction.append("00")
            

        elif(op=='&'):
            
            instruction.append("01")
        elif(op=="|"):
           
            instruction.append("10")
        elif(op=="2scomplement"):
           
            instruction.append("11")
        inst="".join(instruction)
        newinst=str()
        for i in range(len(inst)-1):
            newinst+=inst[i]
            newinst+="_"
        newinst+=inst[len(inst)-1]
        f=open('D:\\input.txt','w')
        f.write(newinst)
        f.close()
        time.sleep(0.5)
        f=open('D:\\output.txt','r')
        number=f.read()
        f.close()
        self.textbox2.setText(number)
        if(number=="0000001"):self.timeDisplay.display('0')
        if(number=="1001111"):self.timeDisplay.display('1')
        if(number=="0010010"):self.timeDisplay.display('2')
        if(number=="0000110"):self.timeDisplay.display('3')
        if(number=="1001100"):self.timeDisplay.display('4')
        if(number=="0100100"):self.timeDisplay.display('5')
        if(number=="0100000"):self.timeDisplay.display('6')
        if(number=="0001111"):self.timeDisplay.display('7')
        if(number=="0000000"):self.timeDisplay.display('8')
        if(number=="0000100"):self.timeDisplay.display('9')
        if(number=="1111111"):self.timeDisplay.display('E')
        f=open('D:\\input.txt','w')
        f.close()

            
        






        f.close()  
    @pyqtSlot()
    def on_clickac(self):
        f=open("D:\\input.txt", "w")
        f.write("")
        f.close()
        self.timeDisplay.display('0')
        self.textbox2.setText("")
   

   
         
        
         
         
         
         
         
         
         
         
         
        

       
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())