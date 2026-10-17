import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import smtplib
from email.message import EmailMessage

def create_administrative_pdf():
    filename = "Demande_Administrative_Et_RIB.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Header
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 750, "DEMANDE ADMINISTRATIVE ET COORDONNEES BANCAIRES")
    c.setFont("Helvetica", 10)
    c.drawString(50, 735, f"Fait à Nice, le {datetime.now().strftime('%d/%m/%Y')}")
    c.line(50, 720, 550, 720)
    
    # Personal Information
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, 695, "INFORMATIONS PERSONNELLES :")
    c.setFont("Helvetica", 10)
    c.drawString(70, 675, "Titulaire : MR ABDALLAH BEN BELGACEM")
    c.drawString(70, 660, "Date et Lieu de Naissance : 16/06/1990 à Kebili")
    c.drawString(70, 645, "Passeport N° : U751045")
    c.drawString(70, 630, "Adresse : Nice, France")
    
    # Bank Information (RIB / IBAN)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, 595, "COORDONNEES BANCAIRES (RIB) :")
    c.setFont("Helvetica", 10)
    c.drawString(70, 575, "IBAN : FR76 1659 8000 0140 0014 2630 322")
    c.drawString(70, 560, "BIC / SWIFT : FPELFR21XXX")
    c.drawString(70, 545, "Domiciliation : FPE Charenton - 1 Place des Marseillais, 94220 Charenton Le Pont")
    c.drawString(70, 530, "Code Banque : 16598  |  Code Guichet : 00001  |  Clé : 22")
    c.drawString(70, 515, "Numéro de Compte : 40001426303")
    
    # Body Text
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, 475, "OBJET : Transmission de coordonnées bancaires et justificatif")
    
    c.setFont("Helvetica", 10)
    lines = [
        "Madame, Monsieur,",
        "",
        "Je soussigné, Monsieur ABDALLAH BEN BELGACEM, vous transmets par la présente mes",
        "coordonnées bancaires (RIB) officielles ci-dessus afin de procéder au traitement et à la",
        "régularisation de mon dossier administratif et financier.",
        "",
        "Dans l'attente de votre confirmation, je vous prie d'agréer, Madame, Monsieur,",
        "l'expression de mes salutations distinguées."
    ]
    
    y = 450
    for line in lines:
        c.drawString(50, y, line)
        y -= 18
        
    # Signature
    c.setFont("Helvetica-Bold", 10)
    c.drawString(380, 220, "Signature :")
    c.drawString(380, 200, "BEN BELGACEM ABDALLAH")
    
    c.save()
    print(f"[✓] PDF Generated with Bank Details: {filename}")
    return filename

def send_email_notification(pdf_filename):
    receiver = "aliali12345908ali@gmail.com"
    print(f"[*] Dispatching updated document with RIB to: {receiver}")

if __name__ == "__main__":
    pdf = create_administrative_pdf()
    send_email_notification(pdf)


import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import smtplib
from email.message import EmailMessage

def create_administrative_pdf():
    filename = "Demande_Administrative_Et_RIB.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    # Header
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 750, "DEMANDE ADMINISTRATIVE ET COORDONNEES BANCAIRES")
    c.setFont("Helvetica", 10)
    c.drawString(50, 735, f"Fait à Nice, le {datetime.now().strftime('%d/%m/%Y')}")
    c.line(50, 720, 550, 720)

    # Personal Information
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, 695, "INFORMATIONS PERSONNELLES :")
    c.setFont("Helvetica", 10)
    c.drawString(70, 675, "Titulaire : MR ABDALLAH BEN BELGACEM")
    c.drawString(70, 660, "Date et Lieu de Naissance : 16/06/1990 à Kebili")
    c.drawString(70, 645, "Passeport N° : U751045")
    c.drawString(70, 630, "Adresse : Nice, France")

    # Bank Information (RIB / IBAN)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, 595, "COORDONNEES BANCAIRES (RIB) :")
    c.setFont("Helvetica", 10)
    c.drawString(70, 575, "IBAN : FR76 1659 8000 0140 0014 2630 322")
    c.drawString(70, 560, "BIC / SWIFT : FPELFR21XXX")
    c.drawString(70, 545, "Domiciliation : FPE Charenton - 1 Place des Marseillais, 94220 Charenton Le Pont")
    c.drawString(70, 530, "Code Banque : 16598  |  Code Guichet : 00001  |  Clé : 22")
    c.drawString(70, 515, "Numéro de Compte : 40001426303")

    # Body Text
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, 475, "OBJET : Transmission de coordonnées bancaires et justificatif")

    c.setFont("Helvetica", 10)
    lines = [
        "Madame, Monsieur,",
        "",
        "Je soussigné, Monsieur ABDALLAH BEN BELGACEM, vous transmets par la présente mes",
        "coordonnées bancaires (RIB) officielles ci-dessus afin de procéder au traitement et à la",
        "régularisation de mon dossier administratif et financier.",
        "",
        "Dans l'attente de votre confirmation, je vous prie d'agréer, Madame, Monsieur,",
        "l'expression de mes salutations distinguées."
    ]

    y = 450
    for line in lines:
        c.drawString(50, y, line)
        y -= 18

    # Signature
    c.setFont("Helvetica-Bold", 10)
    c.drawString(380, 220, "Signature :")
    c.drawString(380, 200, "BEN BELGACEM ABDALLAH")

    c.save()
    print(f"[✓] PDF Generated with Bank Details: {filename}")
    return filename

def send_email_direct_smtp(pdf_filename, app_password=None):
    sender = "aliali12345908ali@gmail.com"
    receiver = "aliali12345908ali@gmail.com"

    msg = EmailMessage()
    msg['Subject'] = "Demande Administrative Officielle et RIB - BEN BELGACEM ABDALLAH"
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content("Bonjour Abdallah,\n\nVeuillez trouver ci-joint votre document administratif officiel généré automatiquement depuis votre système Omni-Verse dans Termux.\n\nCordialement,\nOmni-Verse System")

    with open(pdf_filename, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=os.path.basename(pdf_filename))

    if app_password:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, app_password)
            server.send_message(msg)
        print(f"[✓] Email successfully sent via SMTP to {receiver}")
    else:
        print(f"[*] Document prepared for automated dispatch to: {receiver}")

if __name__ == "__main__":
    pdf = create_administrative_pdf()
    # أدخل كلمة مرور التطبيقات المكونة من 16 حرفاً في السطر التالي عند استخراجها:
    # send_email_direct_smtp(pdf, app_password="YOUR_APP_PASSWORD_HERE")
    send_email_direct_smtp(pdf)


