# Security4Industry
Update 11.24:
Finished MES console and basic DNC service:
	run DNC\DNCservice.py first to start DNC service
	then run MES\MESconnect.py to start up MES console


Update 11.26:
Finished MES console function and status request between DNC & NC :
    MES ---(Send status request)---> DNC ---(Request status by argument(s))---> NC (Get status)
    |<------(Send all status)------|     |  <-----(Send back self status)-----|
    run NC\NCservice.py to start up NC device;
    run DNC\DNCservice.py first to start DNC service;
	then run MES\MESconnect.py to start up MES console;
	You can use status funtion only(by now)
Further details&bugs please Issue.