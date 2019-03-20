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
Generate bit(s): 4096, Generate time: 0:02:43.970605
#RSA密钥产生时间随密钥位数成指数倍增加(产生原理决定:随机产生大质数,Miller-Robin筛选,位数越多,计算量越大)


Encry&Decry time(NOT Divided):
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
#未分组加密存在单次加密长度限制，一般不在实践中使用

Encry&Decry time(Divided):
# key_bit = 256 group
Status : str_length = 10, key_bit = 256;
	Encry time:  0:00:00 , Decry time: 0:00:00
	Encry_str=HPaYTSrEYG
	Decry_str=HPaYTSrEYG
	Compare: match
Status : str_length = 100, key_bit = 256;
	Encry time:  0:00:00 , Decry time: 0:00:00.000998
	Encry_str=oAIJLlUvkqsDghrrxeHjiqcSdtXyYGnkTvfHznVgWJUxUovVFtnVULwENenkQTjMxRBXXiEEfYnNcShBAIkvkLsYzDqTIydxVjAN
	Decry_str=oAIJLlUvkqsDghrrxeHjiqcSdtXyYGnkTvfHznVgWJUxUovVFtnVULwENenkQTjMxRBXXiEEfYnNcShBAIkvkLsYzDqTIydxVjAN
	Compare: match
Status : str_length = 1000, key_bit = 256;
	Encry time:  0:00:00.000998 , Decry time: 0:00:00.016954
	Encry_str=vvuGusiCywstVEweYjcjcHOFlfkTyLlahzdLDuAljjtsoAfVcdedvibqivVAepKbvcTnyLgwRDxnh......
	Decry_str=vvuGusiCywstVEweYjcjcHOFlfkTyLlahzdLDuAljjtsoAfVcdedvibqivVAepKbvcTnyLgwRDxnh......
	Compare: match
Status : str_length = 10000, key_bit = 256;
	Encry time:  0:00:00.012967 , Decry time: 0:00:00.176567
	Encry_str=rlxagLCeNrLllPUZpdXBXbAESXAZJcNGUyzjvUolMDbXDliLqupGvsuAYQINXMTygFGKdJqGHfhUrYGhLnXdIaWQVYqh......
	Decry_str=rlxagLCeNrLllPUZpdXBXbAESXAZJcNGUyzjvUolMDbXDliLqupGvsuAYQINXMTygFGKdJqGHfhUrYGhLnXdIaWQVYqh......
	Compare: match
	
# key_bit = 512 group	
Status : str_length = 10, key_bit = 512;
	Encry time:  0:00:00 , Decry time: 0:00:00.001994
	Encry_str=JniYdDXHyI
	Decry_str=JniYdDXHyI
	Compare: match
Status : str_length = 100, key_bit = 512;
	Encry time:  0:00:00 , Decry time: 0:00:00.001993
	Encry_str=naZFoWpqqUQbrxaadqdBhbQiSvUGRZcWImHjhrsoIQHIsYWeAkguYHcVBmyuJTivcpQRjNUZUzdJnwTBwRuGcsrEtdHjuQXSASTK
	Decry_str=naZFoWpqqUQbrxaadqdBhbQiSvUGRZcWImHjhrsoIQHIsYWeAkguYHcVBmyuJTivcpQRjNUZUzdJnwTBwRuGcsrEtdHjuQXSASTK
	Compare: match
Status : str_length = 1000, key_bit = 512;
	Encry time:  0:00:00.000997 , Decry time: 0:00:00.024951
	Encry_str=iVfTwSWMOIHZIwtuNkEsVbBjkAYiBJaxZMWNYLROoFUCKQDAQeCtOMckgAoTMWcrmTnAOoQPXNQeh......
	Decry_str=iVfTwSWMOIHZIwtuNkEsVbBjkAYiBJaxZMWNYLROoFUCKQDAQeCtOMckgAoTMWcrmTnAOoQPXNQeh......
	Compare: match
Status : str_length = 10000, key_bit = 512;
	Encry time:  0:00:00.007947 , Decry time: 0:00:00.239327
	Encry_str=CKTUzNxLFYgwtgeCcvVghnfbNSqYkJfvEDgGNbvnlJmtSEUBeOwIMrxxojztiPDQMELKSiWYoRgsCMwSIAdYdLMYkihC......
	Decry_str=CKTUzNxLFYgwtgeCcvVghnfbNSqYkJfvEDgGNbvnlJmtSEUBeOwIMrxxojztiPDQMELKSiWYoRgsCMwSIAdYdLMYkihC......
	Compare: match

# key_bit = 1024 group
Status : str_length = 10, key_bit = 1024;
	Encry time:  0:00:00 , Decry time: 0:00:00.005980
	Encry_str=TjkGezTtoT
	Decry_str=TjkGezTtoT
	Compare: match
Status : str_length = 100, key_bit = 1024;
	Encry time:  0:00:00 , Decry time: 0:00:00.005951
	Encry_str=LXkUwFTtmgHTTUMJvMEFqYBimYWdJRuUWqySHfMmvEVEhIBCUkKdBqbSHDsXxzYcUQBIesQIAwogJGksbKwtoMLazUJAlVepbAlb
	Decry_str=LXkUwFTtmgHTTUMJvMEFqYBimYWdJRuUWqySHfMmvEVEhIBCUkKdBqbSHDsXxzYcUQBIesQIAwogJGksbKwtoMLazUJAlVepbAlb
	Compare: match
Status : str_length = 1000, key_bit = 1024;
	Encry time:  0:00:00.000997 , Decry time: 0:00:00.051890
	Encry_str=gisHTVhzpKMyrtvpYyCiWvjDpTriqOYMUPIHpoIhTpCkPHDdnEJRdWyaKSSMKXkUmHHTftYKpgyLn......
	Decry_str=gisHTVhzpKMyrtvpYyCiWvjDpTriqOYMUPIHpoIhTpCkPHDdnEJRdWyaKSSMKXkUmHHTftYKpgyLn......
	Compare: match
Status : str_length = 10000, key_bit = 1024;
	Encry time:  0:00:00.006955 , Decry time: 0:00:00.511632
	Encry_str=ERzVCwdzuxwiVpjEoulwTMdXYjWYNFCvlnOIJVPQQrSzPNrFpiuEMfNdsnPZeyltwlBkNCpHOUMvBXvsFmvzDesVtCgi......
	Decry_str=ERzVCwdzuxwiVpjEoulwTMdXYjWYNFCvlnOIJVPQQrSzPNrFpiuEMfNdsnPZeyltwlBkNCpHOUMvBXvsFmvzDesVtCgi......
	Compare: match

# key_bit = 2048 group
Status : str_length = 10, key_bit = 2048;
	Encry time:  0:00:00 , Decry time: 0:00:00.035904
	Encry_str=cwVvVPegiX
	Decry_str=cwVvVPegiX
	Compare: match
Status : str_length = 100, key_bit = 2048;
	Encry time:  0:00:00 , Decry time: 0:00:00.036908
	Encry_str=cXPSdIwhcEWQBOVqbANvLzqRxheKAbfOCExpewkEqJFpsRCkqXvVpdfjoeVIHfUHdQUoXTHaINidEyTdLFHmPnlUmytbolEwORpA
	Decry_str=cXPSdIwhcEWQBOVqbANvLzqRxheKAbfOCExpewkEqJFpsRCkqXvVpdfjoeVIHfUHdQUoXTHaINidEyTdLFHmPnlUmytbolEwORpA
	Compare: match
Status : str_length = 1000, key_bit = 2048;
	Encry time:  0:00:00.001990 , Decry time: 0:00:00.189488
	Encry_str=qmBLPLMtmBgDGZkMCPbZKKOPUOavsQIdBqrpaEMswiPOPykpfCULxniwTAJESgEvjEcqrMaiNnthT......
	Decry_str=qmBLPLMtmBgDGZkMCPbZKKOPUOavsQIdBqrpaEMswiPOPykpfCULxniwTAJESgEvjEcqrMaiNnthT......
	Compare: match
Status : str_length = 10000, key_bit = 2048;
	Encry time:  0:00:00.011001 , Decry time: 0:00:01.509962
	Encry_str=HQFFCxLWMzgdOKjqFeOsSXhXdgLKUCeOKOnoqeKkUaTlAcrqinRoovqQsfdyEnUGzOSDCDpGpuCfhmhspdnpdzCaYrpP......
	Decry_str=HQFFCxLWMzgdOKjqFeOsSXhXdgLKUCeOKOnoqeKkUaTlAcrqinRoovqQsfdyEnUGzOSDCDpGpuCfhmhspdnpdzCaYrpP......
	Compare: match
#加密时间随密钥位数增加成倍增大；
#当待加密数据未单次加密长度时，加密时间一般较短
#当待加密超出了单次加密长度限制时，通常采用分组的方案，此时消耗时间随分块数增加线性增加