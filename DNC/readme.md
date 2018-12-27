#DNC模块
    DNC模块分为几个部分：
    |---DNCservice.py              提供主要DNC服务
    |---DNCconfig.py               提供DNC配置选项
    |---DNC.cfg                    DNC配置文件
    |---Device.cfg                 保存了下属NC设备信息
    |---(MES.key)                  用于保存MES的公钥（每次启动时更新）
    |---Record.log                 日志文件，记录了每次登陆即操作的时间
    |---RSAbase.py                 提供RSA使用支持，详见Encry-Decry下readme.md
    