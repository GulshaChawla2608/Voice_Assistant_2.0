import webbrowser as wb
import  speech_recognition as sr
import pyttsx3
import os
import getpass



pyttsx3.speak("Hello Team, Joy here How can i help you?")
print("--------------Welcome to my automation world-----------------".center(125))

pyttsx3.speak("Enter your password here")
passwd = getpass.getpass("Enter your password:")
if passwd!="gc":
   print("password incorrect")
   exit()

while True:
    print("\t \t Tell me your requirement... i am listening : ", end='')
    r= sr.Recognizer()
    with sr.Microphone() as source:
        pyttsx3.speak("Start Saying Your Requirements...")
        audio= r.listen(source)
        print("Speech Done")
        ch= r.recognize_google(audio)
    if (("how" in ch) or ("help" in ch)):
        pyttsx3.speak("I can help you in following ways such as")
        pyttsx3.speak("Running Basic Linux Commands")
        print("1.Running Basic Linux Commands".center(120))
        pyttsx3.speak("Automating AWS Cloud using AWS-CLI")
        print("2.Automating AWS Cloud using AWS-CLI".center(120))
        pyttsx3.speak("Creation of LVM architecture and sharing limited storage to master node via data node")
        print("3.Creation of LVM architecture and sharing limited storage to master node via data node")
        pyttsx3.speak("Automation of docker container")
        print("4.Automation of docker container")
      # ------>Basic Linux Commands<-----------
    elif(("linux" in ch) or ("basic" in ch)):
        pyttsx3.speak("As per your choice,now i will run some basic linux commands for you")
        pyttsx3.speak("Which system you want to do run linux commands Local or Remote")
        s= input("Which system you want to do run linux commands (local/remote)? :")
        if s=="remote":
            ip=input("Enter remote system IP :")
            cmd=input("Enter command name you want to run : ")
            os.system("ssh root@{0} {1}".format(ip,cmd))
        else :
            print("Enter correct IP!!")
        
  #--------->AWS-Cloud using AWS-CLI<-----------
    elif (("AWS" in ch) or ("cloud" in ch)):
        pyttsx3.speak("As per your choice,now i will automate aws cloud using AWS-CLI")
        pyttsx3.speak("I can do following things for you in AWS-CLI such as:")
        pyttsx3.speak("Creating a new key pair")
        print(">>Creating a new key pair<<".center(120))
        pyttsx3.speak("Creating a security group")
        print(">>Creating a security group<<".center(120))
        pyttsx3.speak("Launching a new ec2-instance in mumbai region")
        print(">>Launching a new ec2-instance in mumbai region<<".center(120))
        pyttsx3.speak("Launching a ebs volume")
        print(">>Launching a EBS volume<<".center(120))
        pyttsx3.speak("Attaching your EBS volume to your launched instance")
        print(">>Attaching your EBS volume to your launched instance<<".center(120))
        pyttsx3.speak("Creation of S3 bucket")
        print(">>Creation of S3 bucket<<".center(120))
        pyttsx3.speak("Copying file from local pc to AWS S3 bucket")
        print(">>Copying file from local pc to AWS S3 bucket<<".center(120))
        pyttsx3.speak("Creation of Cloud Front Distribution")
        print(">>Creation of Cloud Front Distribution<<".center(120))
       #Commands of AWS-CLI
    
    
    elif(("create" in ch) or ("new" in ch) or ("key" in ch)):
        key=input("Enter your key-name:")
        os.system("aws ec2 create-key-pair --key-name {0}".format(key))
        pyttsx3.speak("Creating a new key pair for you")
        wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#KeyPairs:")
    elif(("configure" in ch) or ("security" in ch) or ("group" in ch)):
        sg=input("Enter your security group name :")
        ds=input("Enter group description :")
        os.system("aws ec2 create-security-group --group-name {0} --description {1}".format(sg,ds))
        pyttsx3.speak("Configuring your aws security group")
        wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#SecurityGroups:")
    elif(("ec2" in ch) or ("instances" in ch)):
        id=input("Enter image id :")
        key=input("Enter key name :") 
        sg=input("Enter security group id :")
        os.system("aws ec2 run-instances --image-id {0} --count 1 --instance-type t2.micro --key-name {1} --security-group-ids {2} --subnet-id subnet-a9959dc1".format(id,key,sg))
        pyttsx3.speak("Launching a new ec2 instance for you")
        wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:sort=keyName")
    elif(("launch" in ch) or ("volume" in ch)):
        size=input("Enter your volume size :")
        os.system("aws ec2 create-volume --volume-type gp2 --size {0} --availability-zone ap-south-1a".format(size))
        pyttsx3.speak("Launching an ebs volume of 1GiB in mumbai region")
        wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:sort=desc:createTime")
    elif "attach" in ch:
        vid=input("Enter volume id:")
        im=input("Enter image id :")
        os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/sdf".format(vid,im))
        pyttsx3.speak("Your EBS volume is successfully attached to your launched instance")
        wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:sort=desc:createTime")
    elif "bucket" in ch :
        bk=input("Enter a name creating bucket : ")
        os.system("aws s3api create-bucket --bucket {0} --region ap-south-1  --acl public-read  --create-bucket-configuration LocationConstraint=ap-south-1".format(bk))
        pyttsx3.speak("Creating a S3 bucket")
        wb.open("https://s3.console.aws.amazon.com/s3/home?region=ap-south-1#")
    elif "copy" in ch:
        os.system("aws s3 cp C:\\Users\\gulsh\\Desktop\\logo.jpg s3://gc2662 --acl public-read")
        pyttsx3.speak("Your image has been successfully uploaded")
        wb.open("https://s3.console.aws.amazon.com/s3/home?region=ap-south-1#")
    elif "distribution" in ch :
        os.system("aws cloudfront create-distribution --origin-domain-name gc2662.s3.amazonaws.com")
        pyttsx3.speak("Creating cloud front distribution,please wait for few minutes..till we deploy")
        wb.open("https://console.aws.amazon.com/cloudfront/home?region=ap-south-1#")
    
   #------->LVM Architecture<-----------------
    elif "architecture" in ch:
        pyttsx3.speak("As per your choice,now i will create LVM architecture and share limited storage to master node via node")
        pyttsx3.speak("Which system you want to do run linux commands Local or Remote")
        s= input("Which system you want to do run linux commands (local/remote)? :")
        if s=="remote":
            ip=input("Enter remote system IP :")
            os.system("ssh root@{0}".format(ip))
            pyttsx3.speak("Login to remote system is successfull")
        else:
            print("Enter correct IP!!")

    elif(("tell" in ch) or ("about" in ch) and ("yourself" in ch)):
        pyttsx3.speak("I will do following things such as..")
        print("I will do following things such as :".center(120))
        pyttsx3.speak("Creation of physical volumes")
        print(">>Creation of physical volumes<<".center(120))
        pyttsx3.speak("Creation of Volume Group")
        print(">>Creation of Volume Group<<".center(120))
        pyttsx3.speak("Partition of your Logical Volume")
        print(">>Partition of your Logical Volume<<".center(120))
        pyttsx3.speak("Loading of driver for your storage")
        print(">>Loading of driver for your storage<<".center(120))
        pyttsx3.speak("Formatting of LVM partition")
        print(">>Formatting of LVM partition<<".center(120))
        pyttsx3.speak("Mounting LVM partition to Data Node Storage")
        print(">>Mounting LVM partition to Data Node Storage<<".center(120))
    elif "show" in ch:
        os.sytem("ssh root@192.168.43.211 fdisk -l")
        pyttsx3.speak("These are the hard disks currently this system has..")
    elif "physical" in ch:
        os.system("ssh root@192.168.43.211")
        pv=input("Enter your hard disk name:")
        os.system("ssh root@192.168.43.211 pvcreate {0}".format(pv))
        pyttsx3.speak("Partition volume has been successfully created")
    elif "verify" in ch:
        pv=input("Which hard disk to display:")
        os.system("ssh root@192.168.43.211 pvdisplay {0}".format(pv))
    elif (("logical"in ch) or ("hard" in ch) or ("disk" in ch)):
        vol=input("Enter volume name:")
        pv1=input("Enter name of PV1:")
        pv2=input("Enter name of PV2:")
        os.system("ssh root@192.168.43.211 vgcreate {0} {1} {2}".format(vol,pv1,pv2))
        pyttsx3.speak("Volume group has been successfully created")
        print("Volume group has been successfully created".center(120))
    elif "display"in ch:
        vol=input("Enter VG name:")
        os.system("ssh root@192.168.43.211 vgdisplay {0}".format(vol))
        pyttsx3.speak("Volume Group having size 16GB displayed")
    elif "partition" in ch:
        size=input("Enter size of partition:")
        pt_name=input("Enter partition name:")
        lv=input("Enter LV name:")
        os.system("ssh root@192.168.43.211 lvcreate --size {0} --name {1} {2}".format(size,pt_name,lv))
        pyttsx3.speak("Partition has been successfully created")
        print("Partition has been successfully created".center(120))
    elif "details" in ch:
        vg_name=input("Enter VG name:")
        pt_name=input("Enter partition name :")
        os.system("ssh root@192.168.43.211 lvdisplay {0}/{1}".format(vg_name,pt_name))
    elif "driver" in ch:
        os.system("ssh root@192.168.43.211 udevadm settle")  
        pyttsx3.speak("Driver has been successfully loaded..now you can easily interact with storage of VG")
        print("Driver loaded..".center(120))
    elif "format" in ch:
        os.system("ssh root@192.168.43.211 mkfs.ext4 /dev/arthvg/gc1")
        pyttsx3.speak("VG has been successfully formatted..")
        print("VG has been successfully formatted..".center(120))
    elif "mount" in ch:
        os.system("ssh root@192.168.43.211 mount /dev/arthvg/gc1 /dn1")
        pyttsx3.speak("Partition has been successfully mounted to master node via data node providing limited storage")
        print("Partition has been successfully mounted to master node via data node providing limited storage".center(120))
    elif (("hadoop" in ch) or ("report" in ch)):
        os.system("ssh root@192.168.43.87 hadoop dfsadmin -report")
        pyttsx3.speak("Displaying hadoop report")
        print("Displaying hadoop report 1 data node is connected".center(120))
    elif (("datanode" in ch) or ("slave" in ch)) :
        os.system("ssh root@192.168.43.211 hadoop-daemon.sh start datanode")
        pyttsx3.speak("Data Node has been started")
        print("Data Node has been started".center(120))
    elif (("masternode" in ch) or ("name" in ch)):
        os.system("ssh root@192.168.43.87 hadoop-daemon.sh start masternode")
        pyttsx3.speak("Master node has been started...")
        print("Master node has been started...")
    elif "storage" in ch:
        os.system("ssh root@192.168.43.211")
    #--------->Docker Automation<---------------
    elif "docker"in ch:
        pyttsx3.speak("As per your choice,now i will automate docker container for you")
        pyttsx3.speak("Which system you want to do run docker commands Local or Remote")
        s= input("Which system you want to do run docker commands (local/remote)? :")
        if s=="remote":
            ip=input("Enter remote system IP :")
            os.system("ssh root@{0}".format(ip))
            pyttsx3.speak("Login to remote system is successfull")
        else:
            print("Enter correct IP!!")
    elif(("what" in ch) or ("do" in ch)):
        pyttsx3.speak("I can do followings things in container such as")
        pyttsx3.speak("Displaying your docker images")
        print(">>Displaying your docker images<<".center(120))
        pyttsx3.speak("Pulling docker images from docker.hub.com")
        print(">>Pulling docker images from docker.hub.com<<".center(120))
        pyttsx3.speak("Launching  and running a new os inside container")
        print(">>Launching a new os inside container<<".center(120))
        pyttsx3.speak("To display launched o.s inside container")
        print(">>To display launched o.s inside container<<".center(120))
        pyttsx3.speak("Launching a webserver inside docker container")
        print(">>Launching a webserver inside docker container<<".center(120))
        pyttsx3.speak("Removing all stopped containers")
        print(">>Removing all stopped containers<<".center(120))
    elif "images" in ch:
        pyttsx3.speak("Displaying your images")
        os.system("ssh root@192.168.43.211 docker images")
    elif "pull" in ch:
        pyttsx3.speak("To pull docker images from docker.hub.com enter image here")
        pull=input("Enter image name to pull:")
        os.system("ssh root@192.168.43.211 docker pull {0}".format(pull))
        pyttsx3.speak("CentOS image has been pulled successfully")
    elif "server" in ch:
        pyttsx3.speak("To launch webserver you need to remotely login to system")
        os.system("ssh root@192.168.43.211")
    elif "remove" in ch:
        os.system("ssh root@192.168.43.211 docker rm `docker ps -a -q`")
        pyttsx3.speak("Your all containers are successfully removed")
        print("Your all containers are successfully removed...".center(120))
    elif (("ok" in ch) or ("bye" in ch)):
        break
    else:
        pyttsx3.speak("I didn't get you")
    
pyttsx3.speak("Thank you everyone for having me,signing off...Good Day")   
print("Thank you everyone for having me,signing off...Good Day".center(125))   

      



         
      

       
       

       
    
    


    
    
    
