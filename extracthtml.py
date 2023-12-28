
#Extracting html content  using regular expression
import re
html_content = """
<html>
<head>
<title>Profile: Aphrodite</title>
</head>
<body bgcolor="yellow">
<center>
<br><br>
<img src="/static/aphrodite.gif" />
<h2>Name: Aphrodite</h2>
<br><br>
Favorite animal: Dove
<br><br>
Favorite color: Red
<br><br>
Hometown: Mount Olympus
</center>
</body>
</html>
"""


def extract_html(html_content):

    # Define a regex pattern to match the desired information
    pattern = re.search(r'<title>(.*?)</title>.*?<h2>Name: (.*?)</h2>.*?Favorite animal: (.*?)<.*?Favorite color: (.*?)<.*?Hometown: (.*?)<', html_content,re.DOTALL)

    if pattern:
        title, name, animal, color, hometown = pattern.groups()
        print(f"Title: {title}")
        print(f"Name: {name}")
        print(f"Favorite Animal: {animal}")
        print(f"Favorite Color: {color}")
        print(f"Hometown: {hometown}")

extract_html(html_content)       

