import subprocess
import os

list_file=os.listdir("/home/tronghuan/Documents/python/download")

path="/home/tronghuan/Documents/python/download"
path_Of_All_File=[]
for x in list_file:
    path_Of_All_File.append(os.path.join(path,x))
namenode_link = "/user/tronghuan/cao_anh/download"

def put_Toan_bo_file():
    c=len(path_Of_All_File)
    i=0
    for x in path_Of_All_File:
        if x==c:
            break  
        try:

            cmd_PUT=f"hdfs dfs -put {x} " + namenode_link
            try:
                result=subprocess.Popen(cmd_PUT,shell=True)
                result.wait()
                print("Tai len HDFS thanh cong !")
                i+=1         
            except:
                print("failed")
                continue

        except:
            print("that bai !")  

def xoa_sau_khi_put():
    c=len(path_Of_All_File)
    i=0
    for x in path_Of_All_File:
        if x==c:
            break  
        try:
            cmd_rm=f"rm -r {x}"
            try:
                result=subprocess.Popen(cmd_rm,shell=True)
                result.wait()
                print("xoa file thanh cong !")
                i+=1         
            except:
                print("failed")
                continue

        except:
            print("that bai !") 

put_Toan_bo_file()
#xoa_sau_khi_put()