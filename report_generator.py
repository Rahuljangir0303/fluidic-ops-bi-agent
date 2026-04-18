from reportlab.platypus import SimpleDocTemplate, Paragraph

def create_pdf(insights, recommendations):
    doc = SimpleDocTemplate("reports/report.pdf")
    content = []

    content.append(Paragraph("Business Insights Report", None))

    for i in insights:
        content.append(Paragraph(i, None))

    for r in recommendations:
        content.append(Paragraph(r, None))

    doc.build(content)