import sys





fw=open("resultlist.txt","a")
fw.write(__file__.split("\\")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
fw.close()
class A:
    fw=open("resultlist.txt","a")
    fw.write(__file__.split("\\")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
    fw.close()
    def modify1(self):
        fw=open("resultlist.txt","a")
        fw.write(__file__.split("\\")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
        fw.close()
        print('modified in kind b')

    fw=open("resultlist.txt","a")
    fw.write(__file__.split("\\")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
    fw.close()
    def modify2(self):
        fw=open("resultlist.txt","a")
        fw.write(__file__.split("\\")[-1]+":"+str(sys._getframe().f_lineno+2)+"\n")
        fw.close()
        print('modified in kind b 2')
