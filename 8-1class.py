#计算BMI指数
class BMI:
    def __init__(self,name,age,weight,height):
        self.__name=name
        self.__age=age
        self.__weight=weight
        self.__height=height
    def getBMI(self):
        bmi=self.__weight/(self.__height*self.__height)
        return round(bmi*100)/100
    def getStatus(self):
            bmi=self.getBMI()
            if bmi<18.5:
                return "偏瘦"
            elif bmi<24:
                return "正常"
            elif bmi<30:
                return "偏胖"
            else:
                return "肥胖"
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getWeight(self):
        return self.__weight
    def getHeight(self):
        return self.__height
#程序从这里开始运行
bmi1=BMI("zs",21,64,1.70)
print(bmi1.getName(),"的BMI是",bmi1.getBMI(),bmi1.getStatus())

        
        
                        
            


        
    