from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import io


class EmlGenerator:
    @staticmethod
    def generate(content, filename="example", **kwargs):
        # Create the container email message
        msg = MIMEMultipart()
        msg["From"] = "from@example.com"
        msg["To"] = "to@example.com"
        msg["Subject"] = "Test Email"

        body = content
        msg.attach(MIMEText(body, "plain"))

        if "attachment" in kwargs:
            attachment_content = content
        else:
            attachment_content = "This is the content of the attachment."
        attachment = io.BytesIO(attachment_content.encode("utf-8"))
        attachment_name = "attachment.txt"

        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", f"attachment; filename={attachment_name}"
        )

        msg.attach(part)

        # Write the email message to a file
        with open(f"{filename}.eml", "w") as f:
            f.write(msg.as_string())
