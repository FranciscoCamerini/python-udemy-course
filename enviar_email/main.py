from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

email = ''
senha = ''

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Francisco Camerini', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Francisco Camerini'
msg['to'] = 'francisco.camerini@gmail.com'
msg['subject'] = 'Email de teste'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.png', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, senha )
        smtp.send_message(msg)
        print('Email enviado com sucesso.')
    except Exception as e:
        print('Email não enviado...')
        print('Erro: ', e)
        
