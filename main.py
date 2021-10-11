from flask import Flask,render_template,request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from email.mime.base import MIMEBase
from email import encoders


app = Flask(__name__)
OWN_EMAIL = "spamhereacc111@gmail.com"
OWN_PASSWORD = "spam_account123"


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/mail", methods = ["GET", "POST"])
def mail():
    if request.method == "POST":
        data = request.form

        send_email(data["username"],data["name"],[data['file']],[data['mail']])

    return render_template("mail.html", msg_sent = False)


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



if __name__ == "__main__":
    app.run(debug=True)