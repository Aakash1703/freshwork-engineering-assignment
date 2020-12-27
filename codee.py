import threading 
import time

d={} 


def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and len(value)<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

"""for read operation
use syntax "read(key_name)" """
            
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                i=str(key)+":"+str(b[0]) #to return the value in the format i.e.,"key_name:value"
                print(i)
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            i=str(key)+":"+str(b[0])
            print(i)

"""for delete operation
use syntax "delete(key_name)" """

def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key is successfully deleted")
