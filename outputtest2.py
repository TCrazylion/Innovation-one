import sys
fw=open("resultlist.txt","a")
fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
fw.close()
import modifypart as mp

fw=open("resultlist.txt","a")
fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
fw.close()
class A:
    fw=open("resultlist.txt","a")
    fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
    fw.close()
    def modify1(self):
        fw=open("resultlist.txt","a")
        fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
        fw.close()
        print('not modify')

    fw=open("resultlist.txt","a")
    fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
    fw.close()
    def modify2(self):
        fw=open("resultlist.txt","a")
        fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
        fw.close()
        print('not modify in 2')

fw=open("resultlist.txt","a")
fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
fw.close()
def main():
    fw=open("resultlist.txt","a")
    fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
    fw.close()
    for i in range(3):
        fw=open("resultlist.txt","a")
        fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
        fw.close()
        a=mp.modify(i)
        fw=open("resultlist.txt","a")
        fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
        fw.close()
        a.modify1()
    fw=open("resultlist.txt","a")
    fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
    fw.close()
    b=0
    fw=open("resultlist.txt","a")
    fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
    fw.close()
    while True:
       fw=open("resultlist.txt","a")
       fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
       fw.close()
       b+=1
       fw=open("resultlist.txt","a")
       fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
       fw.close()
       if b>=10:
           fw=open("resultlist.txt","a")
           fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
           fw.close()
           break
    fw=open("resultlist.txt","a")
    fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
    fw.close()
    for i in range(3):
        fw=open("resultlist.txt","a")
        fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
        fw.close()
        a=mp.modify(i)
        fw=open("resultlist.txt","a")
        fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
        fw.close()
        a.modify2()

fw=open("resultlist.txt","a")
fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
fw.close()
if __name__=='__main__':
    fw=open("resultlist.txt","a")
    fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
    fw.close()
    main()
fw=open("resultlist.txt","a")
fw.write(__file__.split("/")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
fw.close()


