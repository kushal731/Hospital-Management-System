import random as r
import mysql.connector 
from flask import Flask , render_template,request,redirect,url_for,session
from flask.views import MethodView
from flask_mail import Mail, Message # type: ignore
from pymongo import MongoClient
import qrcode 
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os 
# cd Hospital mangement system
# venv\Scripts\activate
# python app.py
# venv\Scripts\Activate.ps1

# npm run build to connect react
client = MongoClient("mongodb://localhost:27017/")
    
# Access database and collection
# cdn link for qr code generator

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["MAIL_SERVER"] = "smtp.gmail.com"  # SMTP Server
app.config["MAIL_PORT"] = 587  # Port for TLS
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config['MAIL_USERNAME'] = "kushaltr454@gmail.com"
app.config['MAIL_PASSWORD'] = "rhvw tsfs dpni hizz"
app.config['MAIL_DEFAULT_SENDER'] = "kushaltr454@gmail.com"


mail = Mail(app)
conn=mysql.connector.connect(host='localhost',user='root',password='6361142946@kus',database='app')
my_cursor=conn.cursor()

#---------------------------------------------------This is about Login page ----------------------------------------------------------------------------------------------------------
@app.route("/")
def login():
    return render_template("login.html")

@app.route("//login1", methods=["POST"])
def loginver():
    email = request.form.get("Email").strip()      # strip whitespace
    npass_word = request.form.get("npass_word").strip()
    session['email_login'] = email
    if email=="" :
        return render_template("login.html", message="kindy Enter your email and password")
    if npass_word=="" :
        return render_template("login.html", message="kindy Enter your password")
    # if email=="kushaltr454@gmail.com" :
    #     return render_template("login.html", message="kindy Enter your email and password")
    my_cursor.execute("SELECT npass_word FROM app.account_1 WHERE nemail = %s", (email,))
    res = my_cursor.fetchone()

    if res:
        stored_password = res[0].strip()
        if email=="kushaltr454@gmail.com" :
            if npass_word == stored_password:
                return redirect(url_for("home_admin"))
    if res:
        stored_password = res[0].strip()

        if npass_word == stored_password:
            return redirect(url_for("home"))
        else:
            return render_template("login.html", message="The password is incorrect")
    else:
        return render_template("login.html", message="Account not found, please create one")

# -----------------------------------------------------------------------------------------------------------------------------

def otp():
    Otp=r.randint(100000,999999)
    return Otp
@app.route("/Get_OTP" ,methods=["POST"])
def forgot():
    Email=request.form.get("Email").strip()
    my_cursor.execute("select nemail from app.account_1 where nemail=%s",(Email,))
    ver_email=my_cursor.fetchone()
    if ver_email:
        
        pos=otp()
        session['otp'] = pos
        session['ver_email'] = ver_email
        
        msg = Message(
                subject="Your OTP Code for Verification",
                recipients=[Email]
            )
        msg.body = f'''Hello,\n\n
            Your One-Time Password (OTP) is: {pos}\n
            Please enter this code in the application to complete your verification.\n
            This code will expire in 10 minutes.
            Thank you,\n
            Hospital Management System Team
        '''
            # Attach the PDF
        mail.send(msg)
        print("Email sent successfully!")
        return render_template("forgot_OPT.html")
    else:
        return render_template("forgot_pass.html",Message="Enter gmail is not exist so create a account")
    
# 
@app.route("/Enter_OTP" ,methods=["POST"])
def verify_otp():
    En_OTP=request.form.get("En_OTP").strip()
    ne_En_OTP=int(En_OTP)
    pos = session.get('otp')
    if ne_En_OTP==pos:
        return render_template("update_pass.html")
    return render_template("forgot_OPT.html",Message="wrong opt")


@app.route("/froget1" ,methods=["POST"])
def forget_pass():
    
    return render_template("forgot_pass.html")


@app.route("/update_password" ,methods=["POST"])
def update_password():
    new_password = request.form.get("update_password").strip()
    
    # Ensure email is a string, not a tuple
    email_tuple = session.get('ver_email')
    if isinstance(email_tuple, tuple):
        email = email_tuple[0]
    else:
        email = email_tuple

    sql = "UPDATE app.account_1 SET npass_word = %s WHERE nemail = %s"
    values = (new_password, email)

    my_cursor.execute(sql, values)
    conn.commit()

    return render_template("update_pass.html", Message="Password updated")

#---------------------------------------------------This is about Create account page ---------------------------------------------------------------------------------------------------------

@app.route("/Create_account")
def Create_account():
    return render_template("Create_account.html")

@app.route("/create_acc", methods=["POST"])
def account():
    Cname=request.form.get("Cname")
    Clname=request.form.get("Clname")
    dob=request.form.get("DOB")
    phone=request.form.get("phone")
    nemail=request.form.get("email")
    npass_word=request.form.get("npass_word")
    
    my_cursor.execute("select nemail from app.account_1 where nemail=(%s)",(nemail,))
    res=my_cursor.fetchone()
    
    if res:
        return "The email exits"
    else:
        my_cursor.execute("insert into app.account_1 (cname,clname,dob,phone,nemail,npass_word) values (%s ,%s ,%s , %s ,%s ,%s)",
        (Cname,Clname,dob,phone,nemail,npass_word))
        conn.commit()
        return redirect(url_for("home"))

#---------------------------------------------------This is about home page ----------------------------------------------------------------------------------------------------------
@app.route("/home_admin")
def home_admin():
    return render_template("index_admin.html")
conn.commit()

@app.route("/responses")
def responses():
    return render_template("responses.html")
conn.commit()

@app.route("/home")
def home():
    return render_template("index.html")
conn.commit()

@app.route("/enter", methods=["POST"])
def submit():
    name = request.form.get("AAname")
    fid=r.randint(1,100)
    n1=name[0]
    n2=n1.isupper()
    name[0]=n2
    my_cursor.execute("SELECT dname FROM departments WHERE dname = %s", (name,))

    res=my_cursor.fetchone()
    if res:
        sql = "INSERT INTO app.nodejs (id, name) VALUES (%s, %s)"
        values = (fid,name)
        my_cursor.execute(sql, values)
        session['dept'] = name
        return redirect(url_for("department_page", dept=name))
    elif():
        return f"Department '{name}' was not found."
        
    conn.commit()
    return f"Data saved: {name}, {fid}"

#---------------------------------------------------This is about department page ----------------------------------------------------------------------------------------------------------

@app.route("/department/<dept>")
def department_page(dept):
    session['dept'] = dept
    # Render template dynamically based on department name
    return render_template(f"{dept}.html") 


@app.route("/search", methods=["POST"])
def departsearch():
    name = request.form.get("AAname")
    fid=r.randint(1,100)

    my_cursor.execute("SELECT dname FROM departments WHERE dname = %s", (name,))

    res=my_cursor.fetchone()
    if res:
        sql = "INSERT INTO app.nodejs (id, name) VALUES (%s, %s)"
        values = (fid,name)
        my_cursor.execute(sql, values)
        session['dept'] = name
        return redirect(url_for("department_page", dept=name))
    elif():
        return f"Department '{name}' was not found."
        
    conn.commit()
    return f"kindly enter the department name"

# @app.route("/Appcar_submit", methods=["POST"])
class dept_back(MethodView):
    def __init__(self):
        self.name=None
        self.phono=None
        self.email=None
        self.token=None
        self.dept =None
        
    def qr(self):
        # Data you want to encode
        data = f"""
        "name": {self.name},
            "email": {self.email},
            "token": {self.token},
            "phono": {self.phono},
            "dept": {self.dept}
        """
        url="http://192.168.29.39:5000/"

        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # controls size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data
        qr.add_data(data)
        qr.add_data(url)
        qr.make(fit=True)

        # Generate image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save to file
        img.save(f"{self.name}_{self.phono}_qr.png")
        return f"{self.name}_{self.phono}_qr.png"
    
    def send_email(self):
        # Create message
        msg = Message(
            subject="Your Appointment Slip",
            recipients=[self.email]
        )
        msg.body = f"Dear {self.name},\n\nPlease find attached your appointment slip for {self.dept} department.\n\nRegards,\nCity Hospital"

        # Attach the PDF
        with app.open_resource(self.file_name) as fp:
            msg.attach(
                f"{self.dept}_{self.phono}_Appointment.pdf",
                "application/pdf",
                fp.read()
            )

        mail.send(msg)
        print("Email sent successfully!")

    
    def pdf(self):
        import os

        self.file_name = os.path.join(
            "static", "patient_appointment", "cardiology", "Data",
            f"{self.dept}_{self.phono}_Appointment.pdf"
            )


        # file_name = f".\\templates\patient_appointment\cardiology\Data{self.dept}_{self.phono}_Appointment.pdf"
        c = canvas.Canvas(self.file_name, pagesize=A4)
        width, height = A4

        # Hospital Header
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width/2, height-50, "City Hospital")
        c.setFont("Helvetica", 12)
        c.drawCentredString(width/2, height-70, f"{self.dept} Department Appointment Slip")

        # QR Code / Logo (placed top-left)
        c.drawImage(f"{self.name}_{self.phono}_qr.png", 70, height-180, width=100, height=100)

        # Patient Details (aligned to the right of QR code)
        c.setFont("Helvetica", 12)
        c.drawString(200, height-120, f"Patient Name : {self.name}")
        c.drawString(200, height-140, f"Phone Number : {self.phono}")
        c.drawString(200, height-160, f"Email        : {self.email}")
        c.drawString(200, height-180, f"Token Number : {self.token}")
        c.drawString(200, height-200, f"Department   : {self.dept}")

        # Divider Line
        c.line(70, height-220, width-70, height-220)

        # Instructions
        c.setFont("Helvetica-Oblique", 11)
        c.drawString(80, height-240, "Instructions:")
        c.setFont("Helvetica", 10)
        c.drawString(100, height-260, "- Please arrive 15 minutes before your scheduled time.")
        c.drawString(100, height-280, "- Bring previous medical records and test results.")
        c.drawString(100, height-300, "- Contact reception for any queries.")

        # Footer
        c.setFont("Helvetica", 9)
        c.drawCentredString(width/2, 50, "Thank you for choosing City Hospital. Wishing you good health.")

        c.save()
        print(f"PDF saved as {self.file_name}")
        return 
    
    def calling(self):
        
        self.qr()
        self.pdf()
    
    def tokengenerate(self):
       
        self.dept = session.get('dept').strip()
        my_cursor.execute(
        "SELECT MAX(token) FROM app.appoint WHERE dept = %s",
        (self.dept,)
        )
        highest_token = my_cursor.fetchone()[0]

        # If no token exists yet, start at 1
        if highest_token is None:
            new_token = 1
            self.token=new_token
        else:
            new_token = highest_token + 1
            self.token=new_token
            
        return
            
    
    def post(self):
        self.tokengenerate()
        self.name=request.form.get("Aname").strip()
        self.phono=request.form.get("Aphone")
        self.email=request.form.get("Aemail")
        
        self.dept = session.get('dept').strip()
        
        my_cursor.execute("insert into app.appoint (Aname,Aphone,Aemail,token,dept) values (%s ,%s ,%s , %s ,%s)",
            (self.name,self.phono,self.email,self.token,self.dept))
        conn.commit()
        
        db = client["contact"]
        collection = db["contact_details"]
        customer = {
            "name": self.name,
            "email": self.email,
            "token": self.token,
            "phono": self.phono,
            "dept": self.dept
        }
        collection.insert_one(customer)
        self.calling()
        self.send_email()
        return render_template(f"{self.dept}.html", message1=f"{self.dept}_{self.phono}_Appointment.pdf")
    
app.add_url_rule("/Appcar_submit", view_func=dept_back.as_view("dept_back"))

class dept_back_res(MethodView):
    def __init__(self):
        self.name=None
        self.phono=None
        self.email=None
        self.token=None
        self.dept =None
        self.reportcode=None
        self.dept_number=None
        
    def ReportCode(self):
        self.token=request.form.get("token")
        self.dept = session.get('dept').strip()
        my_cursor.execute(
        "SELECT MAX(token) FROM app.reportcode WHERE dept = %s",
        (self.dept,)
        )
        highest_token = my_cursor.fetchone()[0]
        my_cursor.execute(
        "SELECT id FROM app.departments WHERE dept = %s",
        (self.dept,)
        )
        self.dept_number=my_cursor.fetchone()
        
        # If no token exists yet, start at 1
        if highest_token is None:
            new_token = f"{self.name}_{self.phono}_{self.dept_number}_{1}"
            self.reportcode=new_token
        else:
            new_token = highest_token + 1
            self.reportcode=new_token
            
        return
    
    def qr(self):
        # Data you want to encode
        data = f"""
        "name": {self.name},
            "email": {self.email},
            "token": {self.token},
            "phono": {self.phono},
            "dept": {self.dept}
        """
        url="http://192.168.29.39:5000/"

        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # controls size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data
        qr.add_data(data)
        qr.add_data(url)
        qr.make(fit=True)

        # Generate image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save to file
        img.save(f"{self.name}_{self.phono}_qr.png")
        return f"{self.name}_{self.phono}_qr.png"
    
    def send_email(self):
        # Create message
        msg = Message(
            subject="Your Appointment Slip",
            recipients=[self.email]
        )
        msg.body = f"Dear {self.name},\n\nPlease find attached your appointment slip for {self.dept} department.\n\nRegards,\nCity Hospital"

        # Attach the PDF
        with app.open_resource(self.file_name) as fp:
            msg.attach(
                f"{self.dept}_{self.phono}_Appointment.pdf",
                "application/pdf",
                fp.read()
            )

        mail.send(msg)
        print("Email sent successfully!")

    
    def pdf(self):
        import os

        self.file_name = os.path.join(
            "static", "patient_appointment", "cardiology", "Data",
            f"{self.dept}_{self.phono}_Appointment.pdf"
            )

        # file_name = f".\\templates\patient_appointment\cardiology\Data{self.dept}_{self.phono}_Appointment.pdf"
        c = canvas.Canvas(self.file_name, pagesize=A4)
        width, height = A4

        # Hospital Header
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width/2, height-50, "City Hospital")
        c.setFont("Helvetica", 12)
        c.drawCentredString(width/2, height-70, f"{self.dept} Department report Slip")

        # QR Code / Logo (placed top-left)
        c.drawImage(f"{self.name}_{self.phono}_qr.png", 70, height-180, width=100, height=100)

        # Patient Details (aligned to the right of QR code)
        c.setFont("Helvetica", 12)
        c.drawString(200, height-120, f"Patient Name : {self.name}")
        c.drawString(200, height-140, f"Phone Number : {self.phono}")
        c.drawString(200, height-160, f"Email        : {self.email}")
        c.drawString(200, height-180, f"Token Number : {self.token}")
        c.drawString(200, height-200, f"Department   : {self.dept}")
        

        # Divider Line
        c.line(70, height-220, width-70, height-220)

        # Instructions
        c.setFont("Helvetica-Oblique", 11)
        c.drawString(80, height-240, "Instructions:")
        c.setFont("Helvetica", 10)
        c.drawString(100, height-260, "- Please arrive 15 minutes before your scheduled time.")
        c.drawString(100, height-280, "- Bring previous medical records and test results.")
        c.drawString(100, height-300, "- Contact reception for any queries.")

        # Footer
        c.setFont("Helvetica", 9)
        c.drawCentredString(width/2, 50, "Thank you for choosing City Hospital. Wishing you good health.")

        c.save()
        print(f"PDF saved as {self.file_name}")
        return 
    
    def calling(self):
        self.qr()
        self.pdf()
        
    def post(self):
        self.dept = session.get('dept')
        
        self.name=request.form.get("Aname").strip()
        self.phono=request.form.get("Aphone")
        self.token=request.form.get("token")
        self.email=request.form.get("Aemail")
        
        self.dept = session.get('dept').strip()
        
        my_cursor.execute("insert into app.appoint (Aname,Aphone,Aemail,token,dept) values (%s ,%s ,%s , %s ,%s)",
            (self.name,self.phono,self.email,self.token,self.dept))
        conn.commit()
        
        db = client["contact"]
        collection = db["results_details"]
        customer = {
            "name": self.name,
            "email": self.email,
            "token": self.token,
            "phono": self.phono,
            "dept": self.dept
        }
        collection.insert_one(customer)
        self.calling()
        self.send_email()
        return render_template(f"{self.dept}.html", message1=f"{self.dept}_{self.phono}_Appointment.pdf")
    
app.add_url_rule("//rescar_submit", view_func=dept_back_res.as_view("dept_back_res"))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_message', methods=['POST'])
def contact_back():
    # Match form field names from your HTML form
    name = request.form.get('Con_name')
    phone = request.form.get('Con_phone')
    email = request.form.get('Con_email')
    message = request.form.get('con_message')
    city=request.form.get('Con_city')
    
    # Connect to local MongoDB
    db = client["contact"]
    collection = db["contact_details"]
    # Insert a single document (dict only)
    customer = {"name": name, "phone":phone,"email": email, "city":city, "message": message}
    collection.insert_one(customer)
    
    print("successful")
    return render_template("contact.html", mess="The details are taken by the software.Our team will contact you")

@app.route('/about')
def about():
    return render_template('about.html')

def dapartment_name():
    dapartment=session.get('dept')
    return dapartment

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)