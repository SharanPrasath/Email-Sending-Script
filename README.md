# Email-Sending-Script
<h3>HOME PAGE</h3>
<img src = "SS1.png"/>
<h3>SEND EMAIL PAGE</h3>
<img src = "SS2.png"/>
<h3>Technologies Used</h3>
<ul>
  <li>Flask Framework</li>
  <li>Imp Libraries : SMTP and MIME</li>
  </ul>

``` 
from flask import Flask,render_template,request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from email.mime.base import MIMEBase
from email import encoders

```
<ul>
  <li>First of all importing all libraries</li>
  <li>SMTP(Simple mail transfer protocal only allowes data that is simple i.e messages , text , etc</li>
  <li>MIME(Multipurpose Internet Mail Extensions) this library helps us to tranfer or send attachments in terms of binary code</li>
 </ul>
 
 ```
 
app = Flask(__name__)
OWN_EMAIL = "spamhereacc111@gmail.com"
OWN_PASSWORD = "spam_account123"


@app.route('/')
def home():
    return render_template("index.html")
 
 ```
<ul>
  <li>Now declaring a flask object and variables that have username and password</li>
  <li>Using Flask rendering the homepage first using render_template function</li>
</ul>  

```
def send_email(uname,name, file,mail):
    assert type(mail) == list
    assert type(file) == list

    msg = MIMEMultipart()
    msg['From'] = OWN_EMAIL
    msg['To'] = ','.join(mail)
    msg['Subject'] = f"{uname},\n{name}"

    msg.attach(MIMEText(name))
    for r, d, f in os.walk("c:\\"):
        for files in f:
            if files == file[0]:
                filepath = os.path.join(r, files)



    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filepath, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"'
                    % os.path.basename(filepath))
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(OWN_EMAIL, OWN_PASSWORD)
    server.sendmail(OWN_EMAIL, mail, msg.as_string())
    server.quit()

```

<ul>
  <li>This is the main functionality on the backend</li>
  <li>Function accepts subject , file as a list , to address as a list , and the message</li>
  <li>Create MIMEMultipart function<, declaring from email and the to email address and the subject key which has the value of the subject that is entered</li>
  <li>Now I did a for loop that loops through each and every files and directories , if there is a match with the filename, the filepath is stored under the variable filepath </li>
  <li>This is done inorder to avoid errors like FileNotFoundError which occurs if there is no path and only file name is formed</li>
  <li>Declare object of MIMEbase class and use set payload function to update the message and open read the file.</li>
  <li>Now use add_header function which has content disposition which says what type of format the message is it. In this case it is a attachment. Now use the attach function passing the attachment as parameter</li>
  <li>For the final functionality use SMTP server to decalre what type of host we are using , in our case it is gmail.</li>
  <li>Finally start the server , login using the credentials declared already. Now use sendmail function to send the mail which has the sender EmailID , to address and the message . Close the server</li>
</ul>

```

@app.route("/mail", methods = ["GET", "POST"])
def mail():
    if request.method == "POST":
        data = request.form
        try:
            send_email(data["username"],data["name"],[data['file']],[data['mail']])
        except:
            return render_template("mail.html")
    
        else:
            return render_template("mail.html", msg_sent = True)
        
    return render_template("mail.html", msg_sent = False)

```

<ul>
  <li>This function is where data of the form submitted is retrieved using POST method</li>
  <li>data is retrived using request module, which contains data in the format of keys and values</li>
  <li>Now I am using Try Excpet and Else in order to except errors</li>
  <li>Under the Try method send_email function which accepts the username or subject, the message, the file in the format of list and the to address in the form of list</li>
</ul>


