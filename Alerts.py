import requests,smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#website= requests.get('https://www.flipkart.com/apple-ipad-7th-gen-32-gb-rom-10-2-inch-wi-fi-only-space-grey/p/itm9b1d54fb06bd6?pid=TABFHF3ATXZ42TW8&lid=LSTTABFHF3ATXZ42TW8CVH9IT&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=291847d4-13d9-4606-a519-e69fea0fd0e9.TABFHF3ATXZ42TW8.SEARCH&ppt=sp&ppn=sp&ssid=zneklf7sq25gbe2o1608191352192&qH=af1b4711365308d5')
website = requests.get('https://www.flipkart.com/apple-ipad-8th-gen-32-gb-rom-10-2-inch-wi-fi-only-space-grey/p/itm3cc7ba36f500a?pid=TABFVZD2CHSWPBYX&otracker=wishlist&lid=LSTTABFVZD2CHSWPBYXZV3DTN&fm=organic&iid=12b2f5c0-e4e9-4c04-ad1d-4339371eb4f4.TABFVZD2CHSWPBYX.PRODUCTSUMMARY&ppt=hp&ppn=homepage&ssid=ffd29dn99mxchtkw1608191323670')

if "BUY NOW" in website.text:
    s = smtplib.SMTP("smtp.gmail.com", 587) 
    s.starttls()
    email = 'your_email'
    pwd = 'your_pwd'
    recipient = 'recepient_mail'
    s.login(email,pwd)
    msg = MIMEMultipart("alternative")
    msg["Subject"]= "Your Ipad is available"
    msg["From"]=email
    msg["To"]=recipient
    text = "The Ipad on your wishlist is available. Go buy it right now!!"
    msg.attach(MIMEText(text, "plain"))
    s.sendmail(email,recipient, msg.as_string())
    s.quit()
    print("Mail Sent!")
