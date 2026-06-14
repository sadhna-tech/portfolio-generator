name = input("Enter your name: ")
role = input("Enter your role: ")
skills = input("Enter skills (comma separated): ")
projects = input("Enter projects (comma separated): ")
email = input("Enter email: ")

html_content = f"""
<!DOCTYPE html>
<html>
<head>
<title>{name} Portfolio</title>
<style>
body {{
    font-family: Arial;
    margin: 40px;
}}
h1 {{
    color: #333;
}}
.section {{
    margin-top: 20px;
}}
</style>
</head>

<body>

<h1>{name}</h1>
<h3>{role}</h3>

<div class="section">
<h2>Skills</h2>
<p>{skills}</p>
</div>

<div class="section">
<h2>Projects</h2>
<p>{projects}</p>
</div>

<div class="section">
<h2>Contact</h2>
<p>{email}</p>
</div>

</body>
</html>
"""

with open("portfolio.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Portfolio generated successfully!")
print("File saved as portfolio.html")