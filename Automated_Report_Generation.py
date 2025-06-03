from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import inch
import pandas as pd

# Load CSV data
df = pd.read_csv("data.csv")

# Calculate statistics
average_score = df["Score"].mean()
top_scorer = df.loc[df["Score"].idxmax()]

# Setup PDF
file_name = "enhanced_score_report.pdf"
pdf = canvas.Canvas(file_name, pagesize=LETTER)
width, height = LETTER

# Add Title
pdf.setFont("Helvetica-Bold", 20)
pdf.setFillColor(colors.darkblue)
pdf.drawString(50, height - 60, "🎓 Student Score Report")

# Add Subtitle
pdf.setFont("Helvetica-Oblique", 12)
pdf.setFillColor(colors.black)
pdf.drawString(50, height - 90, "Generated using Python and ReportLab")

# Draw separator line
pdf.setStrokeColor(colors.grey)
pdf.line(50, height - 100, width - 50, height - 100)

# Prepare Table Data
table_data = [["Name", "Score"]] + df.values.tolist()

# Create Table
table = Table(table_data, colWidths=[2.5 * inch, 1.5 * inch])

# Apply styling
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])
table.setStyle(style)

# Draw the table on the PDF
table.wrapOn(pdf, width, height)
table.drawOn(pdf, 50, height - 300)

# Draw Summary Statistics
pdf.setFont("Helvetica-Bold", 12)
pdf.setFillColor(colors.green)
pdf.drawString(50, height - 320 - len(df)*20, f"Average Score: {average_score:.2f}")

pdf.setFillColor(colors.red)
pdf.drawString(50, height - 340 - len(df)*20, f"Top Scorer: {top_scorer['Name']} ({top_scorer['Score']} points)")

# Footer
pdf.setFillColor(colors.grey)
pdf.setFont("Helvetica-Oblique", 10)
pdf.drawString(50, 40, "© Generated with Python | ReportLab")

# Save the PDF
pdf.save()

print("✅ Enhanced PDF report generated as 'enhanced_score_report.pdf'")
