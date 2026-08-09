msg_id,timestamp,app_protocol,src_app,dst_app,message,src_port,dst_port,protocol,layer,payload_size,latency_ms,src_ip,dst_ip
1,0.000000,HTTP,client_browser,www.example.com,GET /index.html HTTP/1.1,51820,80,TCP,Application,450,12.50,192.168.1.15,93.184.216.34
2,0.015400,HTTP,www.example.com,client_browser,HTTP/1.1 200 OK,80,51820,TCP,Application,1200,12.80,93.184.216.34,192.168.1.15
3,1.203000,HTTP,client_browser,info.cern.ch,GET /hypertext/WWW/TheProject.html HTTP/1.1,51822,80,TCP,Application,480,45.20,192.168.1.15,188.184.21.108
4,1.248000,HTTP,info.cern.ch,client_browser,HTTP/1.1 200 OK,80,51822,TCP,Application,850,45.50,188.184.21.108,192.168.1.15
5,2.050000,HTTP,client_browser,testphp.vulnweb.com,POST /login.php HTTP/1.1,51824,80,TCP,Application,600,88.10,192.168.1.15,44.228.249.3
6,2.150000,HTTP,testphp.vulnweb.com,client_browser,HTTP/1.1 302 Found,80,51824,TCP,Application,320,89.00,44.228.249.3,192.168.1.15
7,4.500000,HTTP,client_browser,httpbin.org,GET /ip HTTP/1.1,51826,80,TCP,Application,410,110.50,192.168.1.15,54.173.190.106
8,4.620000,HTTP,httpbin.org,client_browser,HTTP/1.1 200 OK (JSON Data),80,51826,TCP,Application,550,111.20,54.173.190.106,192.168.1.15
9,5.100000,HTTP,client_browser,www.testingmcafeesites.com,GET /robots.txt HTTP/1.1,51828,80,TCP,Application,390,22.00,192.168.1.15,104.21.5.1
10,5.125000,HTTP,www.testingmcafeesites.com,client_browser,HTTP/1.1 404 Not Found,80,51828,TCP,Application,430,22.40,104.21.5.1,192.168.1.15
11,6.005000,HTTP,client_browser,neverssl.com,GET / HTTP/1.1,51830,80,TCP,Application,460,150.10,192.168.1.15,34.223.12.11
12,6.160000,HTTP,neverssl.com,client_browser,HTTP/1.1 200 OK,80,51830,TCP,Application,1500,151.00,34.223.12.11,192.168.1.15
13,8.400000,HTTP,client_browser,www.example.com,GET /images/logo.png HTTP/1.1,51820,80,TCP,Application,440,13.10,192.168.1.15,93.184.216.34
14,8.415000,HTTP,www.example.com,client_browser,HTTP/1.1 200 OK (Image Data),80,51820,TCP,Application,1460,13.50,93.184.216.34,192.168.1.15
15,8.418000,HTTP,www.example.com,client_browser,HTTP/1.1 200 OK (Image Data cont.),80,51820,TCP,Application,1100,13.60,93.184.216.34,192.168.1.15
16,10.00000,HTTP,client_browser,info.cern.ch,HEAD / HTTP/1.1,51822,80,TCP,Application,350,46.00,192.168.1.15,188.184.21.108
17,10.05000,HTTP,info.cern.ch,client_browser,HTTP/1.1 200 OK,80,51822,TCP,Application,400,46.50,188.184.21.108,192.168.1.15
18,12.50000,HTTP,client_browser,httpbin.org,POST /post HTTP/1.1,51826,80,TCP,Application,700,112.00,192.168.1.15,54.173.190.106
19,12.65000,HTTP,httpbin.org,client_browser,HTTP/1.1 200 OK,80,51826,TCP,Application,650,113.00,54.173.190.106,192.168.1.15
20,15.00000,HTTP,client_browser,www.example.com,GET /favicon.ico HTTP/1.1,51820,80,TCP,Application,420,12.90,192.168.1.15,93.184.216.34
21,16.20000,HTTP,client_browser,admin.internal.net,GET /admin/users HTTP/1.1,51832,80,TCP,Application,400,15.00,192.168.1.15,10.0.0.5
22,16.22000,HTTP,admin.internal.net,client_browser,HTTP/1.1 403 Forbidden,80,51832,TCP,Application,300,15.20,10.0.0.5,192.168.1.15
23,18.50000,HTTP,client_browser,api.myservice.com,DELETE /resource/123 HTTP/1.1,51834,80,TCP,Application,380,55.00,192.168.1.15,172.16.254.1
24,18.60000,HTTP,api.myservice.com,client_browser,HTTP/1.1 500 Internal Server Error,80,51834,TCP,Application,350,55.50,172.16.254.1,192.168.1.15
25,20.00000,HTTP,client_browser,old-site.com,GET / HTTP/1.1,51836,80,TCP,Application,410,110.00,192.168.1.15,198.51.100.1
26,20.15000,HTTP,old-site.com,client_browser,HTTP/1.1 301 Moved Permanently,80,51836,TCP,Application,450,110.50,198.51.100.1,192.168.1.15
27,20.20000,HTTP,client_browser,new-site.com,GET / HTTP/1.1,51836,80,TCP,Application,410,115.00,192.168.1.15,198.51.100.2
28,20.35000,HTTP,new-site.com,client_browser,HTTP/1.1 200 OK,80,51836,TCP,Application,1200,115.50,198.51.100.2,192.168.1.15
29,22.00000,HTTP,hacker_script,bank-login.com,POST /login user=admin pass=123456,52000,80,TCP,Application,450,40.00,192.168.1.100,203.0.113.5
30,22.05000,HTTP,bank-login.com,hacker_script,HTTP/1.1 401 Unauthorized,80,52000,TCP,Application,300,40.50,203.0.113.5,192.168.1.100
31,22.10000,HTTP,hacker_script,bank-login.com,POST /login user=admin pass=password,52000,80,TCP,Application,450,40.00,192.168.1.100,203.0.113.5
32,22.15000,HTTP,bank-login.com,hacker_script,HTTP/1.1 401 Unauthorized,80,52000,TCP,Application,300,40.50,203.0.113.5,192.168.1.100
33,22.20000,HTTP,hacker_script,bank-login.com,POST /login user=admin pass=qwerty,52000,80,TCP,Application,450,40.00,192.168.1.100,203.0.113.5
34,22.25000,HTTP,bank-login.com,hacker_script,HTTP/1.1 401 Unauthorized,80,52000,TCP,Application,300,40.50,203.0.113.5,192.168.1.100
35,22.30000,HTTP,hacker_script,bank-login.com,POST /login user=admin pass=admin123,52000,80,TCP,Application,450,40.00,192.168.1.100,203.0.113.5
36,22.35000,HTTP,bank-login.com,hacker_script,HTTP/1.1 302 Found (Login Success),80,52000,TCP,Application,350,40.50,203.0.113.5,192.168.1.100
37,25.00000,HTTP,client_browser,cdn.stream.com,GET /video/movie.mp4 HTTP/1.1,51840,80,TCP,Application,400,25.00,192.168.1.15,10.10.10.10
38,25.05000,HTTP,cdn.stream.com,client_browser,HTTP/1.1 206 Partial Content (Bytes 0-1000),80,51840,TCP,Application,1460,25.50,10.10.10.10,192.168.1.15
39,25.06000,HTTP,cdn.stream.com,client_browser,HTTP/1.1 206 Partial Content (Bytes 1001-2000),80,51840,TCP,Application,1460,25.60,10.10.10.10,192.168.1.15
40,25.07000,HTTP,cdn.stream.com,client_browser,HTTP/1.1 206 Partial Content (Bytes 2001-3000),80,51840,TCP,Application,1460,25.70,10.10.10.10,192.168.1.15
41,25.08000,HTTP,cdn.stream.com,client_browser,HTTP/1.1 206 Partial Content (Bytes 3001-4000),80,51840,TCP,Application,1460,25.80,10.10.10.10,192.168.1.15
42,25.09000,HTTP,cdn.stream.com,client_browser,HTTP/1.1 206 Partial Content (Bytes 4001-5000),80,51840,TCP,Application,1460,25.90,10.10.10.10,192.168.1.15
43,30.00000,HTTP,mobile_app,api.weather.com,GET /v1/forecast?city=TelAviv HTTP/1.1,51850,80,TCP,Application,350,60.00,192.168.1.20,140.82.121.4
44,30.12000,HTTP,api.weather.com,mobile_app,HTTP/1.1 200 OK (JSON Forecast),80,51850,TCP,Application,800,61.00,140.82.121.4,192.168.1.20
45,30.50000,HTTP,mobile_app,api.weather.com,GET /v1/forecast?city=Haifa HTTP/1.1,51850,80,TCP,Application,350,60.00,192.168.1.20,140.82.121.4
46,30.62000,HTTP,api.weather.com,mobile_app,HTTP/1.1 200 OK (JSON Forecast),80,51850,TCP,Application,800,61.00,140.82.121.4,192.168.1.20
47,35.00000,HTTP,smart_fridge,iot.cloud.com,POST /telemetry temp=4c HTTP/1.1,51860,80,TCP,Application,300,120.00,192.168.1.50,52.95.12.1
48,35.24000,HTTP,iot.cloud.com,smart_fridge,HTTP/1.1 201 Created,80,51860,TCP,Application,250,121.00,52.95.12.1,192.168.1.50
49,40.00000,HTTP,client_browser,intranet.corp,OPTIONS /api/data HTTP/1.1,51870,80,TCP,Application,320,10.00,192.168.1.15,10.0.0.80
50,40.02000,HTTP,intranet.corp,client_browser,HTTP/1.1 204 No Content (CORS Allowed),80,51870,TCP,Application,280,10.50,10.0.0.80,192.168.1.15
51,40.10000,HTTP,client_browser,intranet.corp,PUT /api/data/update/5 HTTP/1.1,51870,80,TCP,Application,500,11.00,192.168.1.15,10.0.0.80
52,40.15000,HTTP,intranet.corp,client_browser,HTTP/1.1 200 OK (Update Success),80,51870,TCP,Application,350,11.50,10.0.0.80,192.168.1.15
53,45.00000,HTTP,dev_tool,staging.server.com,TRACE /debug-me HTTP/1.1,51880,80,TCP,Application,300,95.00,192.168.1.99,198.51.100.55
54,45.19000,HTTP,staging.server.com,dev_tool,HTTP/1.1 405 Method Not Allowed,80,51880,TCP,Application,350,96.00,198.51.100.55,192.168.1.99
55,50.00000,HTTP,client_browser,ads.tracker.com,GET /pixel.gif HTTP/1.1,51890,80,TCP,Application,400,30.00,192.168.1.15,172.217.1.1
56,50.06000,HTTP,ads.tracker.com,client_browser,HTTP/1.1 200 OK (GIF Data),80,51890,TCP,Application,450,30.50,172.217.1.1,192.168.1.15
57,55.00000,HTTP,client_browser,shop.com,POST /cart/add id=555 HTTP/1.1,51900,80,TCP,Application,500,50.00,192.168.1.15,20.112.52.29
58,55.10000,HTTP,shop.com,client_browser,HTTP/1.1 503 Service Unavailable,80,51900,TCP,Application,400,50.50,20.112.52.29,192.168.1.15
59,55.50000,HTTP,client_browser,shop.com,POST /cart/add id=555 HTTP/1.1,51902,80,TCP,Application,500,50.00,192.168.1.15,20.112.52.29
60,55.60000,HTTP,shop.com,client_browser,HTTP/1.1 200 OK (Added to Cart),80,51902,TCP,Application,450,50.50,20.112.52.29,192.168.1.15
61,60.00000,HTTP,backup_sys,cloud.storage,PUT /backup/daily.zip HTTP/1.1,51910,80,TCP,Application,1500,150.00,192.168.1.200,104.18.10.1
62,60.30000,HTTP,cloud.storage,backup_sys,HTTP/1.1 100 Continue,80,51910,TCP,Application,100,150.50,104.18.10.1,192.168.1.200
63,60.40000,HTTP,backup_sys,cloud.storage,Data Chunk 1 (Binary),51910,80,TCP,Application,1400,150.00,192.168.1.200,104.18.10.1
64,60.70000,HTTP,cloud.storage,backup_sys,HTTP/1.1 201 Created,80,51910,TCP,Application,300,151.00,104.18.10.1,192.168.1.200
65,65.00000,HTTP,client_browser,news.site.com,GET /latest-news HTTP/1.1,51920,80,TCP,Application,420,18.00,192.168.1.15,151.101.1.1
66,65.03600,HTTP,news.site.com,client_browser,HTTP/1.1 200 OK (HTML),80,51920,TCP,Application,1400,18.50,151.101.1.1,192.168.1.15
67,65.04000,HTTP,client_browser,news.site.com,GET /css/styles.css HTTP/1.1,51922,80,TCP,Application,400,18.00,192.168.1.15,151.101.1.1
68,65.08000,HTTP,news.site.com,client_browser,HTTP/1.1 200 OK (CSS),80,51922,TCP,Application,900,18.50,151.101.1.1,192.168.1.15
69,66.00000,HTTP,client_browser,news.site.com,GET /logout HTTP/1.1,51920,80,TCP,Application,350,18.00,192.168.1.15,151.101.1.1