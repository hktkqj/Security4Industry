System info:
Processor	Intel(R) Core(TM) i5-6300HQ CPU @ 2.30GHz，2301 Mhz，4 Core(s)，4 Logical Processor(s)	
Physical Memory(RAM)	16.0 GB	


RSA key generate time:
Generate bit(s): 64, Generate time: 0:00:00
Generate bit(s): 128, Generate time: 0:00:00.002992
Generate bit(s): 256, Generate time: 0:00:00.013963
Generate bit(s): 512, Generate time: 0:00:00.014959
Generate bit(s): 1024, Generate time: 0:00:00.565489
Generate bit(s): 2048, Generate time: 0:00:17.954991
#Generate bit(s): 4096, Generate time: 0:02:43.970605
#RSA密钥产生时间随密钥位数成指数倍增加(产生原理决定:随机产生大质数,Miller-Robin筛选,位数越多,计算量越大)


Encry&Decry time(Not grouped):
Status: len = 4, key_bit = 256; Encry_time = 0:00:00, Decry_time = 0:00:00
Status: len = 16, key_bit = 256; Encry_time = 0:00:00, Decry_time = 0:00:00
Status: len = 64, key_bit = 256; ERROR: Unavailable

Status: len = 4, key_bit = 512; Encry_time = 0:00:00, Decry_time = 0:00:00.001967
Status: len = 16, key_bit = 512; Encry_time = 0:00:00, Decry_time = 0:00:00.000998
Status: len = 64, key_bit = 512; ERROR: Unavailable

Status: len = 4, key_bit = 1024; Encry_time = 0:00:00, Decry_time = 0:00:00.005978
Status: len = 16, key_bit = 1024; Encry_time = 0:00:00, Decry_time = 0:00:00.004987
Status: len = 64, key_bit = 1024; Encry_time = 0:00:00, Decry_time = 0:00:00.005982

Status: len = 4, key_bit = 2048; Encry_time = 0:00:00, Decry_time = 0:00:00.035877
Status: len = 16, key_bit = 2048; Encry_time = 0:00:00, Decry_time = 0:00:00.034908
Status: len = 64, key_bit = 2048; Encry_time = 0:00:00, Decry_time = 0:00:00.040889
#加密时间随密钥位数增加成倍增大；
#当待加密数据未单次加密长度时，加密时间一般较短
#当待加密超出了单次加密长度限制时，通常采用分组的方案，此时消耗时间随分块数增加线性增加