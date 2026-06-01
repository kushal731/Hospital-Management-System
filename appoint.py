from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def cardiology_appointment_pdf(patient_name, phone, email, date, token):
    file_name = "Cardiology_Appointment.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    # Hospital Header
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height-50, "City Hospital")
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, height-70, "Cardiology Department Appointment Slip")

    # Patient Details
    c.setFont("Helvetica", 12)
    c.drawString(80, height-120, f"Patient Name : {patient_name}")
    c.drawString(80, height-140, f"Phone Number : {phone}")
    c.drawString(80, height-160, f"Email        : {email}")
    c.drawString(80, height-180, f"Appointment Date : {date}")
    c.drawString(80, height-200, f"Token Number : {token}")
    c.drawString(80, height-220, "Department   : Cardiology")

    # Divider Line
    c.line(70, height-240, width-70, height-240)

    # Instructions
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(80, height-260, "Instructions:")
    c.setFont("Helvetica", 10)
    c.drawString(100, height-280, "- Please arrive 15 minutes before your scheduled time.")
    c.drawString(100, height-300, "- Bring previous medical records and test results.")
    c.drawString(100, height-320, "- Contact reception for any queries.")

    # Footer
    c.setFont("Helvetica", 9)
    c.drawCentredString(width/2, 50, "Thank you for choosing City Hospital. Wishing you good health.")

    c.save()
    print(f"PDF saved as {file_name}")

# Example usage
cardiology_appointment_pdf(
    patient_name="Kushal",
    phone="9876543210",
    email="kushal@example.com",
    date="2026-05-28",
    token="CARD123"
)
