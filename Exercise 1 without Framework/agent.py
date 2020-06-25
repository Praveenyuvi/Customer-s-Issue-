# This is the Code That Exceutes the Customers's issues and add's them in the queue and can preview the list of customers waiting for the issues.
#Where the Customer can remove himself from the queue and it automatically Updates the rest of the customer where the id and issue time is changed or Updated.




import random
import prettytable

def start(count,f,d,k,res,wait):
    if(count==0):
        f = 0
        if(a==1):
            p=0
            print("\nWelcome... \nyour ID is customer",+f,"\n")
            print("Waiting Time for the  issue is ",+p," min\n")
            print("Your issue will be  resolved  in  ",+d,"sec\n")
            print("Thank you \n")
            count = 1
            return count,f,d,p
    else:
        if(k==f):
            f = count[1]+ 1
            print("\nWelcome... \nyour ID is customer", +f,"\n")
            print("Agent is already resolving other.... Customer's issues\n")
            print("Waiting Time for the  issue is",+(res[f-1]))
            print("Please Wait......\n Your issue will be  resolved  in  ",+d,"sec\n")
            print("Thank you \n")
            count = 1
            return count, f,d,res[f-1]+10
        else:
            print("\nWelcome... \nyour ID is customer",+f,"\n")
            print("Agent is already resolving other Customer's issues\n")
            print("Waiting Time for the  issue is",+(res[f-1]),"\n")
            print("Please Wait......\n Your issue will be  resolved  in  ",+d,"sec\n")
            print("Thank you\n ")
            count = 1
            return count,f,d,res[f-1]



def remove(count,f,k,res,e):
    h=0
    e = int(input("please enter your id\n"))
    if (e > count[1]):
        print("\nsorry Invalid Customer Id\n")
        breakpoint()
    else:
        if (e <= count[1]):
            print("\nyou Have been removed from queue\n")
            print("Sorry For the Inconvenience....\n")
            print("---->customer", +(e + 1), "your id is change to", +(e), "as customer ", +e,"has left from the queue")
            print("     And customer", +(e + 1), "your time is change to", +res[(e)], "from your actual time which is ", +res[(e+1)],"\n")
            for h in range(2, (count[1])):
                # print(len(res))
                if((e+h)<len(res)):# because of more id generating than existing
                    print("---->customer", +(e + h), "your id is change to", +(e+h - 1), "as customer ", +e, "has left from the queue")
                    print("     And customer", +(e + h), "your time is change to", +res[((e+h - 2))+1], "from your actual time which is ", +res[(e+h)], "\n\n")
        f=e+h
        k=h+1
        return f,k,(h + 1),e


count=0
d = 0
z=0
y=0
f=0
k=0
res = []
res1=[]
time1=[]
time_left=0
wait=[]
e=0
w = z
arrive = []
arrive1=0
sorted=[]
u=0
id="none"
while True:
    print("1.Customer enter 1 to add in queue\n2.Remove me from Queue\n3.Preview the list of Customer before me\n4.Question for the Answer as per mentioned in the Assignment\n5.exit\n")
    a=int(input("enter the no\n"))
    if(a==1):
        d += random.randint(10, 25)
        b=start(count,f,d,k,res,wait)
        res.append(d)
        count=b
        f=f+1
        res1.append(count[1])
        time1.append(count[2])
        wait.append(count[3])
        w=0
        if(z<=w):
            for x in range(1, (count[1] + 1)):
                arrive1=random.randint(10, 25)
            arrive.append(arrive1)
            arrive.sort()
        else:
            #print(z)
            for x in range(1, (count[1] + 1)):
                arrive1+=10
            arrive.append(arrive1)
            arrive.sort()
    elif(a==2):
        j=remove(count,f,k,res,e)
        f=j[1]
        y=j[2]+5
        z=j[2]
        id=j[3]
        arrive.remove(arrive[id])
    elif(a==3):
        table = prettytable.PrettyTable(['Customer ID','Time Issue Resolvment Start in sec ','Time issue Resolvment Ended in sec','Your arrived time in sec','Customers Id Removed from List Recently is ',])
        if(y<=(count[1]+1)):
            for x in range(0, (len(res1))):
                table.add_row([res1[x],wait[x],time1[x],arrive[x],id])
            print(table)
        else:
            print("\nCustomer Whose id is not changed")
            for x in range(0,(id)):
                table.add_row([res1[x], wait[x], time1[x],arrive[x],id])
            print(table)
            print("\nCustomer Updated list")
            for x in range(id, z):
                value=str(res1[x]+1)
                value1=str(res1[x])
                value2=str(wait[x+1])
                value3=str(wait[x])
                value4=str(time1[x+1])
                value5=str(time1[x])
                table.add_row([str((value) +' has changed the id to '+ value1),str("your time " +(value2) + ' sec is reduced to  '+ value3+' sec'),str("your time " +(value4) + ' sec is reduced to  '+ value5 +' sec'),arrive[x],id])
            res1.remove(res1[x+1])
            res.remove(res[x+1])
            wait.remove(wait[x+1])
            time1.remove(time1[x+1])
            print(table)
        y-=5
    elif (a == 4):
        print("Yes,I have worked in Web Based that is Flask for my college project of Creating a Automatic TimeTable Generator \nwhere Flask was used  , that is for back end used python and the front end (GUI) used which is HTML5.\n")
    else:
        exit()
