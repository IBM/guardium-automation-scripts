use demo_db;
-- "Test Data"
insert into testTable (text) values ('xxx');
insert into testTable (text) values ('yyy');
insert into testTable (text,id) values ('Tansel',5);

-- "XSS":
insert into testTable(text, id) values ('<IMG SRC=javascript:alert(&quot;XSS&quot;)>', 3);
insert into testTable(text,id) values('<BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert(\"XSS\")>',7);
select * from testTable where text='<IMG SRC=javascript:alert(&quot;XSS&quot;)>';
delete from testTable where text='<BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert(\"XSS\")>';
select * from testTable where text=/*'<IMG SRC=javascript:alert(&quot;XSS&quot;)>'*/'xxx';
select * from testTable where text=/*'<IMG SR*//*C=javascri/*pt:ale*//*rt(&qu*//*ot;X/*SS&q*//*uot;)>'*/'xxx';

-- "Tautology":
select * from testTable where text='xxx' or 15=15;
select * from testTable where text='xxx' or (1 and 1 = 1);
select text from testTable where text=' or 1=1 or ''=';

-- "Side_Channel":
insert into testTable(text) values('sleep(5)--');
select * from testTable where text='sleep(12)#';

-- "Denial_Of_Service": 
insert into testTable(text) values('benchmark(123456)');
select * from testTable where text='),(select%20if(count(*)!=-1,benchmark(3000000,MD5(1)),benchmark(3000000)))/*';

-- "OS_Commands": 
select * from testTable where text='&lt;!--#exec%20cmd=&quot;/usr/bin/id;--&gt;';
select * from testTable where text='& ping -n 30 127.0.0.1 &';
select * from testTable where text='$;/usr/bin/id';
select * from testTable where text='cat /etc/passwd';
select * from testTable where text='<?php system(\"sleep 10\");?>';
