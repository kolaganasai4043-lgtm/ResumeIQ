from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("resume_new.pdf", pagesize=letter)
c.setFont("Helvetica", 12)

lines = [
    "KOLA GANA SAI",
    "Python Developer | Flask | SQL | Git | Machine Learning",
    "",
    "SKILLS",
    "Python, Flask, Django, SQL, Git, Java, Machine Learning",
    "Data Analysis, AWS, NLP, Pandas, Numpy",
    "",
    "PROJECTS",
    "ResumeIQ - AI Resume Analyzer using Python Flask NLP",
    "Student Management System - Java",
    "SQL Data Analysis Project",
]

y = 750
for line in lines:
    c.drawString(50, y, line)
    y -= 20

c.save()
print("Resume PDF created!")