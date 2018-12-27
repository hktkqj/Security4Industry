#RSABase功能：
    为每个模块提供封装好的RSA加密解密功能
##def rsa_encry(d_str,key_in) 
    提供加密功能
    输入：d_str为待加密的字符串，key_in为一个公钥类class PublicKey(AbstractKey)
    输出：加密后经utf-8编码的type=bytes

##res_decry(d_byte,key_in)
    提供解密功能
    输入：d_byte为待解密的Bytes，key_in为解密所需的私钥类class PrivateKey(AbstractKey)
    输出：解密后的字符串type=str

##def encode_pubkey(key_in)
    负责将公钥编码成可供传输用的bytes流
    输入：key_in为待加密的公钥类class PublicKey(AbstractKey)
    输出：编码后可供传输的type=bytes
    
##def encode_privkey(key_in)
    负责将私钥编码成可供传输用的bytes流
    输入：key_in为待加密的私钥类class PrivateKey(AbstractKey)
    输出：编码后可供传输的type=bytes

##def gen_pubkey(str_pubkey) && def gen_privkey(str_privkey)
    将编码好的密钥字符串(type=str)转换回对应的密钥类
    输入：str_pubkey/str_privkey为待转换的字符串
    输出：若字符串符合要求，会返回一个对应的密钥类(class PublicKey/class PrivateKey)
    
##def savekey2file(key,file_name)
    负责将密钥文件保存至文件
    输入：key为一个编码后的字符串(type=str)，file_name为保存文件名
    输出：none 只会在调用文件的目录下产生对应文件
    
##def readkeybyfile(file_name)
    从文件中读取key，并产生对应的密钥
    输入：一个文件名file_name(type=str)
    输出：从对应文件名中读取到的密钥，返回一个密钥类(class PublicKey/class PrivateKey)