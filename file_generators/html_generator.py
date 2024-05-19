class HtmlGenerator:
    @staticmethod
    def generate(content, filename="example", **kwargs):
        # Define the HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sample HTML Page</title>
        </head>
        <body>
            <h1>Welcome to My Website</h1>
            <p>This is a sample paragraph in the HTML file.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>{content}</li>
            </ul>
        </body>
        </html>
        """

        # Write the HTML content to the file
        with open(f"{filename}.html", "w") as file:
            file.write(html_content)
