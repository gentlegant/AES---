import base64
from Crypto.Cipher import AES
import os
# import sys, getopt

KEY='lsakdalfjsadfn45'
Des_IV = 'fucktoen1234abcd' # 自定IV向量
class AES_ENCRYPT():
    def __init__(self):
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        self.aes = AES.new(KEY)
        # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    #return type bytes
    def encrypt(self, bytes):
           
        add = 16 - len(bytes)% 16
        add%=16
 
        bytes+= (b'\0' * add)   

        return self.aes.encrypt(bytes)         
    #return type bytes
    def decrypt(self, bytes):
        bytes=self.aes.decrypt(bytes)
        return bytes.strip(b'\0')
MyAES=AES_ENCRYPT()      

def parse_file(allfilename,parse):
    # path_name=os.path.split(allfilename)
    
    ext=allfilename[-3:]
    if(parse and ext!="AES"):
        print(allfilename)
        with open(allfilename,'rb') as bin:
            bindata=bin.read()
            en_str= MyAES.encrypt(bindata)
            with open(allfilename+".AES",'wb') as out:
                out.write(en_str)
    elif(ext=="AES" or ext=="DES"):
        print(allfilename)
        with open(allfilename,'rb') as bin:
            bindata=bin.read()
            en_str= MyAES.decrypt(bindata)
            with open(allfilename[:-4],'wb') as out:
                out.write(en_str)
    else:
        return
    os.remove(allfilename)


def parse_dir(path,parse):
  
    lis=os.listdir(path)
    for i in lis:
        allpath=path+'\\'+i
        if(os.path.isfile(allpath)):
            print(1)
            parse_file(allpath,parse)
        if(os.path.isdir(allpath)):
            parse_dir(allpath,parse)



parse_dir(r"C:\Users\james\Desktop\UUmtu\output\可爱的大奶美女谢芷馨Sindy床上写真图片",True)
