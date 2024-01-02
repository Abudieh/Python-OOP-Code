from abc import ABC,abstractmethod

class date:
    def __init__(self,D,M,Y):
        self._Day=D
        self._Month=M
        self._Year=Y
        
    def setDay(self,d):
        self._Day=d
        
    def setMonth(self,m):
        self._Month=m
        
    def setYear(self,y):
        self._Year=y
        
    def getYear(self):
        return self._Year
    
    def getMonth(self):
        return self._Month
    
    def getDay(self):
        return self._Day
    
    def __str__(self):
        return str(self._Day)+'/'+str(self._Month)+'/'+str(self._Year)
    
class name:
    def __init__(self,fname,sname,lname):
        self._fname=fname
        self._sname=sname
        self._lname=lname
    
    def setfname(self,fn):
        self._fname=fn
    
    def setsname(self,sn):
        self._sname=sn
    
    def setlname(self,sn):
        self._lname=sn
        
    def __str__(self):
        return self._fname+" "+self._sname+" "+self._lname
    
    def __eq__(self,n2):
        return self._fname==n2._fname and self._sname==n2._sname and self._lname==n2._lname
        
    
        
    
class Member(ABC):
    def __init__(self,name,DOB,status,noChildren,DOH,DOR,specialist,degree):
        self._name=name
        self._DOB=DOB
        self._status=status
        self._noChildren=noChildren
        self._DOH=DOH
        self._DOR=DOR
        self._specialist=specialist
        self._degree=degree

    def getname(self):
        return self._name
    

    def getDOB(self):
        return self._DOB

    def getstatus(self):
        return self._status

    def setstatus(self,newstatus):
        self._status=newstatus

    def getnoChildren(self):
        return self._noChildren
    
    def setnoChildren(self,newNoChildren):
        self._noChildren=newNoChildren

    def getDOH(self):
        return self._DOH

    def getDOR(self):
        return self._DOR
    
    def setDOR(self,newDOR):
        self._DOR=newDOR

    def getspecialist(self):
        return self._specialist

    def getdegree(self):
        return self._degree

    def setdegree(self,newdegree):
        self._degree=newdegree

    @abstractmethod
    def getSalary(self):
        pass
    
    def printDetails(self):
        print("Category: "+type(self).__name__)
        print("Name: "+str(self._name))
        print("Date of Birth: "+str(self._DOB))
        print("Status: "+self._status)
        print("Number of children: "+str(self._noChildren))
        print("Date of Hire: "+str(self._DOH))
        print("Date of resignation: "+str(self._DOR))
        print("Specialist: "+self._specialist)
        print("Degree: "+self._degree)
    
    def __str__(self):
        if self._DOR==None:
            return str(self._name)+':'+str(self._DOB)+':'+self._status+':'+str(self._noChildren)+':'+str(self._DOH)+':NO DOR:'+self._specialist+':'+self._degree
        else:
            return str(self._name)+':'+str(self._DOB)+':'+self._status+':'+str(self._noChildren)+':'+str(self._DOH)+':'+str(self._DOR)+':'+self._specialist+':'+self._degree
        



class Employee(Member):
    baseSalary=220
    diplomaBonus=50
    bscBonus=100
    masterBonus=120
    phdBonus=300
    marriedBonus=50
    childBonus=20
    def __init__(self, name, DOB, status, noChildren, DOH, DOR, specialist, degree):
        super().__init__(name, DOB, status, noChildren, DOH, DOR, specialist, degree)


    def getSalary(self):
        salary=self.baseSalary
        if self._degree == "Diploma":
            salary+=self.diplomaBonus
        elif self._degree == "BSc":
            salary+=self.bscBonus
        elif self._degree == "Master":
            salary+=self.masterBonus
        else:
            salary+=self.phdBonus
        if self._status == "Married":
            salary+=self.marriedBonus
        if self._noChildren < 3:
            salary+=(self.childBonus*self._noChildren)
        else:
            salary+=(self.childBonus*3)

        return salary*0.95
    
    def __str__(self):
        return super().__str__()

     




class Trainer(Member):
    def __init__(self, name, DOB, status, noChildren, DOH, DOR, specialist, degree,institution,evaluation):
        super().__init__(name, DOB, status, noChildren, DOH, DOR, specialist, degree)
        self._institution=institution
        self._evaluation=evaluation
        
    def printCertificate(self,):
        print("Name:",self._name)
        print("Period: From",self._DOH,"to",self._DOR)
        print("Evaluation:",self._evaluation)
    
    def getSalary(self):
        return 50
    
    def setevaluation(self,e):
        self._evaluation=e
    
    def getevaluation(self):
        return self._evaluation
    
    def printDetails(self):
        super().printDetails()
        print("Institution:",self._institution)
        print("Evaluation:",self._evaluation)
    
    def __str__(self):
        if self._evaluation==None:
            return super().__str__()+':'+self._institution+':'+'NO EV'
        else:
            return super().__str__()+':'+self._institution+':'+str(self._evaluation)
    
    
        
        
class Worker(Member):
    __rate=10
    def __init__(self, name, DOB, status, noChildren, DOH, DOR, specialist, degree,NoHours):
        super().__init__(name, DOB, status, noChildren, DOH, DOR, specialist, degree)
        self._NoHours=NoHours

    def getSalary(self):
        return self.__rate*self._NoHours
    
    def printDetails(self):
        super().printDetails()
        print("Number of hours worked: "+str(self._NoHours))
    
    def __str__(self):
        return super().__str__()+':'+str(self._NoHours)+' Hours'
        
        
        
changesdone=False
def readfileintolist(filename):
    MFile=open(filename+".txt","r")
    Mlist=[]
    for line in MFile:
        l=line.rstrip().split(":")
        if l[0]!='Constants':
            fullname=name(l[1].split()[0],l[1].split()[1],l[1].split()[2])
            Dateofbirth=date(int(l[2].split('/')[0]),int(l[2].split('/')[1]),int(l[2].split('/')[2]))
            Dateofhire=date(int(l[5].split('/')[0]),int(l[5].split('/')[1]),int(l[5].split('/')[2]))
            if l[6]=="NO DOR":
                Dateofresignation=None
            else:
                Dateofresignation=date(int(l[6].split('/')[0]),int(l[6].split('/')[1]),int(l[6].split('/')[2]))
            
            if l[0]=="Employee":
                Mlist.append(Employee(fullname,Dateofbirth,l[3],int(l[4]),Dateofhire,Dateofresignation,l[7],l[8]))
            elif l[0]=="Trainer":
                if l[10]=="NO EV":
                    Mlist.append(Trainer(fullname,Dateofbirth,l[3],int(l[4]),Dateofhire,Dateofresignation,l[7],l[8],l[9],None))
                else:
                    Mlist.append(Trainer(fullname,Dateofbirth,l[3],int(l[4]),Dateofhire,Dateofresignation,l[7],l[8],l[9],float(l[10])))
            else:
                Mlist.append(Worker(fullname,Dateofbirth,l[3],int(l[4]),Dateofhire,Dateofresignation,l[7],l[8],int(l[9].split()[0])))
        else:
            Employee.baseSalary=float(l[1].split("=")[1])
            Employee.diplomaBonus=float(l[2].split("=")[1])
            Employee.bscBonus=float(l[3].split("=")[1])
            Employee.masterBonus=float(l[4].split("=")[1])
            Employee.phdBonus=float(l[5].split("=")[1])
            Employee.marriedBonus=float(l[6].split("=")[1])
            Employee.childBonus=float(l[7].split("=")[1])
            
    return Mlist
    

def writefile(filename,Mlist):
    f=open(filename+".txt","w")
    for m in Mlist:
        if isinstance(m,Employee):
            f.write('Employee:'+str(m)+'\n')
        elif isinstance(m,Trainer):
            f.write('Trainer:'+str(m)+'\n')
        else:
            f.write('Worker:'+str(m)+'\n')
    f.write("Constants:"+"base="+str(Employee.baseSalary)+":diploma="+str(Employee.diplomaBonus)+":bsc="+str(Employee.bscBonus)+":master="+str(Employee.masterBonus)+":phd="+str(Employee.phdBonus)+":married="+str(Employee.marriedBonus)+":child="+str(Employee.childBonus))
    f.close()


def PrintMenu():
    print("Choose a Service: ")
    print("1- Add Member")
    print("2- Delete Member")
    print("3- Search for member by name")
    print("4- Get Member with highest salary")
    print("5- Get Financial report")
    print("6- Get report of all Employees")
    print("7- Get report of all Trainers")
    print("8- Get Report of all Workers")
    print("9- Member resignation")
    print("10- Change details about employee salary calculation method")
    print("11- Set evaluation for trainer")
    print("12- Print Trainer Certificate")
    print("0-Exit")


def createname():
    fname=input("Enter first name: ")
    sname=input("Enter middle name: ")
    lname=input("Enter family name: ")
    print("-------------------------------")
    return name(fname,sname,lname)

def createdate():
    year=int(input("Enter Year: "))
    while year>2023:
        year=int(input("Enter a year before 2024: "))
    if (year%4==0 and year%100!=0) or (year%400==0):
        leap=True
    else:
        leap=False
        
    month=int(input("Enter Month (1-12): "))
    while month<1 or month >12:
        month=int(input("Please enter a month from 1-12: "))
        
    day=int(input("Enter Day: "))
    while (day>31 or day<1) and month in [1,3,5,7,8,10,12]:
        day=int(input("Enter a day from 1-31: "))
    while (day>30 or day<1) and month in [4,6,9,11]:
        day=int(input("Enter a day from 1-30: "))
    while leap and month==2 and (day>29 or day<1):
        day=int(input("Enter a day from 1-29: "))
    while not leap and month==2 and (day>28 or day<1):
        day=int(input("Enter a day from 1-28: "))
    
    return date(day,month,year)


def AddMember(Mlist):
    global changesdone
    choice=input("Enter member type (E: Employee, T: Trainer, W: Worker)\n")
    while choice not in ['E','T','W']:
       choice=input("Please Enter one of the following letters (E: Employee, T: Trainer, W: Worker)\n")
    print("Name:-")
    mname=createname()
    for m in Mlist:
        if mname==m.getname():
            c=input("Member Already exists, Enter 'D' to see his/her details, or 'M' to go back to menu: ")
            while c not in ['D','M']:
                c=input("Please enter 'D' or 'M': ")
            if c=='D':
                m.printDetails()
            print("------------------------------------------------------")
            return
    print("------------------------------------------------------------")
    print("Date of Birth:-")
    mDOB=createdate()
    print("------------------------------------------------------------")
    status=input("Status (M: Married, S: Single): ")
    while status not in ['M','S']:
        status=input("Enter M or S only (M: Married, S: Single): ")
    if status=='M':
        mstatus='Married'
    else:
        mstatus="Single"
    print("--------------------------------------------------------------")
    mchildren=int(input("Enter number of children: "))
    print("--------------------------------------------------------------")
    print("Date of Hire:- ")
    mDOH=createdate()
    mDOR=None
    print("--------------------------------------------------------------")
    mspecialist=input("Enter specialist: ")
    print("--------------------------------------------------------------")
    degreedict={'D': 'Diploma', 'B': 'BSc', 'M': 'Master', 'P': 'Ph.D.'}
    degree=input("Enter Degree (D: Diploma, B: BSc, M: Master, P: Ph.D.): ")
    while degree not in degreedict.keys():
        degree=input("Please Enter one of the following (D: Diploma, B: BSc, M: Master, P: Ph.D.): ")
    mdegree=degreedict[degree]
    
    if choice=='E':
        Mlist.append(Employee(mname,mDOB,mstatus,mchildren,mDOH,mDOR,mspecialist,mdegree))
        changesdone=True
    elif choice=='T':
        print("----------------------------------------------------------")
        minstitution=input("Institution: ")
        Mlist.append(Trainer(mname,mDOB,mstatus,mchildren,mDOH,mDOR,mspecialist,mdegree,minstitution,None))
        changesdone=True
    else:
        mhours=int(input("Number of hours worked: "))
        while mhours<0:
            mhours=int(input("Please Enter a nonnegative number: "))
        Mlist.append(Worker(mname,mDOB,mstatus,mchildren,mDOH,mDOR,mspecialist,mdegree,mhours))
        changesdone=True
    print("--------------------------------------------------------------")
        
def Deletemember(Mlist):
    global changesdone
    print("Name of member you want to delete:- ")
    membername=createname()
    deleted=False
    for m in Mlist:
        if membername==m.getname():
            Mlist.remove(m)
            changesdone=True
            deleted=True
            break
    if not deleted:
        print("Member not found.")
    else:
        print("Member deleted successfully.")
    print("--------------------------------------------------------------")
        
            
def Searchformember(Mlist):
    print("Name of member you want to search for: ")
    mname=createname()
    found=False
    for m in Mlist:
        if m.getname()==mname:
            if m.getDOR()!=None:
                print("RESIGNED")
            m.printDetails()
            found=True
            break
    if found==False:
        print("Member not found.")
    print("--------------------------------------------------------------")          
              
def printHighestSalary(Mlist):
    max=0
    for m in Mlist:
        if m.getDOR()==None and m.getSalary()>max:
            max=m.getSalary()
    print("Member/s with highest salary:- ")
    for m in Mlist:
        if m.getSalary()==max and m.getDOR()==None:
            print(m.getname(),str(m.getSalary())+'JOD')
    print("--------------------------------------------------------------")
    
def printfinancialreport(Mlist):
    total=0
    for m in Mlist:
        if m.getDOR()==None:
            print(m.getname(),m.getSalary())
            total+=m.getSalary()
    print("----------------------------")
    print("Total: ",total)
    print("--------------------------------------------------------------")
          
    
def printreportofcategory(Mlist,category):
    found=False
    if category == "E":
        for m in Mlist:
            if isinstance(m,Employee):
                if m.getDOR()!=None:
                    print("RESIGNED")
                found=True
                m.printDetails()
                print("-----------------------------")
    elif category == "T":
        for m in Mlist:
            if isinstance(m,Trainer):
                if m.getDOR()!=None:
                    print("RESIGNED")
                found=True
                m.printDetails()
                print("-----------------------------")
    else:
        for m in Mlist:
            if isinstance(m,Worker):
                if m.getDOR()!=None:
                    print("RESIGNED")
                found=True
                m.printDetails()
                print("-----------------------------")
    if not found:
        print("No Current members")
        print("-----------------------------")
    
def Resignation_of_Member(Mlist):
    global changesdone
    print("Name of resigned member:- ")
    mname=createname()
    foundmember=False
    for m in Mlist:
        if mname==m.getname():
            foundmember=True
            if m.getDOR()==None:
                print("Date of Resignation:- ")
                DOR=createdate()
                m.setDOR(DOR)
                changesdone=True
            else:
                print("Member already resigned in",m.getDOR())
            break
    if not foundmember:
        print("Member not found.")
    print("--------------------------------------------------------------")

def Employee_Salary_Calculation():
    global changesdone
    cont=True
    while cont:
        print("Choose what you want to change:-")
        print("1- Change Base Salary")
        print("2- Change Diploma Bonus")
        print("3- Change BSc Bonus")
        print("4- Change Master Bonus")
        print("5- Change Ph.D. Bonus")
        print("6- Change Married Bonus")
        print("7- Change Child Bonus") 
        print("0- Back to menu")
        choice=int(input())
        while choice not in [0,1,2,3,4,5,6,7]:
            choice=int(input("Choose from 0 to 7: "))
        if choice==0:
            cont=False
        elif choice==1:
            b=float(input("Enter new Base Salary: "))
            while b<0:
                b=float(input("Enter a positive number: "))
            Employee.baseSalary=b
            changesdone=True
        elif choice==2:
            b=float(input("Enter new Diploma Bonus: "))
            while b<0:
                b=float(input("Enter a positive number: "))
            Employee.diplomaBonus=b
            changesdone=True
        elif choice==3:
            b=float(input("Enter new BSc Bonus: "))
            while b<0:
                b=float(input("Enter a positive number: "))
            Employee.bscBonus=b
            changesdone=True
        elif choice==4:
            b=float(input("Enter new Master Bonus: "))
            while b<0:
                b=float(input("Enter a positive number: "))
            Employee.masterBonus=b
            changesdone=True
        elif choice==5:
            b=float(input("Enter new Ph.D. Bonus: "))
            while b<0:
                b=float(input("Enter a positive number: "))
            Employee.phdBonus=b
            changesdone=True
        elif choice==6:
            b=float(input("Enter new Married Bonus: "))
            while b<0:
                b=float(input("Enter a positive number: "))
            Employee.marriedBonus=b
            changesdone=True
        else:
            b=float(input("Enter new Child Bonus: "))
            while b<0:
                b=float(input("Enter a positive number: "))
            Employee.childBonus=b
            changesdone=True
        print("-------------------------------")
    print("--------------------------------------------------------------")
    

def Giveevaluation(Mlist):
    global changesdone
    print("Choose trainer to evaluate: ")
    i=0
    listofacceptedchoices=[]
    listoftrainerindexes=[]
    for m in Mlist:
        if isinstance(m,Trainer):
            i+=1
            print(str(i)+'-',m.getname())
            listofacceptedchoices.append(i)
            listoftrainerindexes.append(Mlist.index(m))
    choice=int(input())
    while choice not in listofacceptedchoices:
        choice=int(input("Please enter one of the following numbers "+str(listofacceptedchoices)+': '))
    
    mmbr=Mlist[listoftrainerindexes[choice-1]]
        
    if mmbr.getevaluation()==None:
        e=float(input("Enter evaluation for "+str(mmbr.getname())+' (0-100): '))
        while e<0 or e>100:
            e=float(input("Please enter a number from 0-100: "))
        mmbr.setevaluation(e)
        changesdone=True
    
    else:
        if mmbr.getDOR()!=None:
            print(mmbr.getname(),"already resigned on",mmbr.getDOR(),"with evaluation =",mmbr.getevaluation())
        
        else:
            e=float(input("Enter new evaluation for "+str(mmbr.getname())+' (0-100): '))
            while e<0 or e>100:
                e=float(input("Please enter a number from 0-100: "))
            mmbr.setevaluation(e)
            changesdone=True
   
    
def printCertificate(Mlist):
    global changesdone
    print("Name of Trainer:- ")
    mname=createname()
    found=False
    for m in Mlist:
        if m.getname()==mname:
            found=True
            if not isinstance(m,Trainer):
                print(m.getname(),'is not a trainer.')
            else: 
                if m.getDOR()==None:
                   print("Date of training end:- ")
                   DOR=createdate()
                   m.setDOR(DOR)
                   changesdone=True
                if m.getevaluation()==None:
                    e=float(input("Enter evaluation (0-100): "))
                    while e<0 or e>100:
                        e=float(input("Please enter a number from 0-100: "))
                    m.setevaluation(e)
                    changesdone=True
                m.printCertificate()
            break
    if not found:
        print("Member doesn't exist.")
    print("--------------------------------------------------------------")
        
        

def main():
    memberlist=readfileintolist("Members")
    dontstop=True
    while dontstop:
        PrintMenu()
        choice=int(input())
        while choice not in [0,1,2,3,4,5,6,7,8,9,10,11,12]:
            choice=int(input("Choose service from 1 to 12, Or 0 to exit: "))
        if choice==0:
            dontstop=False
        elif choice==1:
            AddMember(memberlist)
        elif choice==2:
            Deletemember(memberlist)
        elif choice==3:
            Searchformember(memberlist)
        elif choice==4:
            printHighestSalary(memberlist)
        elif choice==5:
            printfinancialreport(memberlist)
        elif choice==6:
            printreportofcategory(memberlist,'E')
        elif choice==7:
            printreportofcategory(memberlist,'T')
        elif choice==8:
           printreportofcategory(memberlist,'W')
        elif choice==9:
            Resignation_of_Member(memberlist)
        elif choice==10:
            Employee_Salary_Calculation()
        elif choice==11:
            Giveevaluation(memberlist)
        else:
            printCertificate(memberlist)
    
    if changesdone:
        saveordiscard=input("Enter 'S' to save changes, or 'D' to discard: ")
        while saveordiscard not in ['S','D']:
            saveordiscard=input("Please enter only S or D: ")
        if saveordiscard=='S':
            writefile("Members",memberlist)  
        print("Exiting...") 

main()