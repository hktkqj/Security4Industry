#MES模块
    包含了以下几个文件：
    |---(${ip},${port}).key             不同NC设备的公钥
    |---MES.cfg                         保存了MES设备的配置信息
    |---MESconfig.py                    可通过该脚本间接修改MES配置
    |---MESconnect.py                   MES主要服务文件
    |---RSAbase.py                      提供RSA使用支持，详见Encry-Decry下readme.md