# from threading import Thread
# from flask_mail import Message
# from app import app, mail
#
#
# def send_async_mail(_app, msg):
#     with app.app_context():
#         try:
#             mail.send(msg)
#         except ConnectionRefusedError:
#             raise InternalServerError("[MAIL SERVER] not working")
#
#
# def send_email(subject, sender, recipients, text_body, html_body):
#     msg = Message(subject, sender=sender, recipients=recipients)
#     msg.body = text_body
#     msg.html = html_body
#     Thread(target=send_async_mail, args=(app, msg)).start()