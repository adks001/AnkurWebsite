import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf():
    pdf_path = os.path.join(os.path.dirname(__file__), "resume.pdf")
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Custom Styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#4f46e5"), # indigo-600
        spaceAfter=4
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0f172a"), # slate-900
        spaceAfter=4
    )
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#475569") # slate-600
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#4f46e5"),
        spaceBefore=10,
        spaceAfter=6,
        borderPadding=2
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#334155") # slate-700
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155"),
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )
    
    company_style = ParagraphStyle(
        'CompanyStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#0f172a")
    )
    
    role_style = ParagraphStyle(
        'RoleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#4f46e5")
    )

    story = []

    # 1. Header (Name, Subtitle, Contact Info)
    story.append(Paragraph("ANKUR KUMAR SINGH", name_style))
    story.append(Paragraph("Senior Data & Product Professional Consultant | 13+ Years Experience", subtitle_style))
    story.append(Paragraph("📍 Bangalore, India  |  ✉️ adks001@gmail.com  |  🔗 linkedin.com/in/adks001", contact_style))
    story.append(Spacer(1, 10))
    
    # Horizontal Rule
    hr = Table([['']], colWidths=[540], rowHeights=[1])
    hr.setStyle(TableStyle([
        ('LINEABOVE', (0,0), (-1,-1), 1.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(hr)
    story.append(Spacer(1, 8))

    # 2. Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    summary_text = (
        "Results-driven Data & Product professional with over 13 years of experience specializing in "
        "product management, data analytics, and business analysis. Actively leveraging Generative AI, "
        "Microsoft Copilot, and AI-assisted analytics to accelerate product delivery, automate insights, "
        "and transform complex datasets into actionable, decision-ready solutions in corporate banking "
        "and contact center environments."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 8))

    # 3. Core purging competencies / skills
    story.append(Paragraph("KEY TECHNICAL COMPETENCIES", section_heading))
    skills_data = [
        [
            Paragraph("<b>Banking Domain Expertise</b>", body_style),
            Paragraph("<b>Stakeholder & Vendor Management</b>", body_style),
            Paragraph("<b>Agile Product Ownership</b>", body_style)
        ],
        [
            Paragraph("<b>Regulatory & Compliance Adoption</b>", body_style),
            Paragraph("<b>Contact Center Analytics</b>", body_style),
            Paragraph("<b>Generative AI, RAG & Prompting</b>", body_style)
        ],
        [
            Paragraph("<b>Power BI & Tableau</b>", body_style),
            Paragraph("<b>SQL & Data Analytics</b>", body_style),
            Paragraph("<b>AWS Cloud & GitHub Copilot</b>", body_style)
        ]
    ]
    skills_table = Table(skills_data, colWidths=[180, 180, 180])
    skills_table.setStyle(TableStyle([
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 8))

    # 4. Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_heading))
    
    # Synechron
    story.append(Paragraph("<b>Synechron</b> (Aug 2021 - Present)  |  <b>PMO Lead / Asst. Manager Data BA / Product Owner</b>", company_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("• <b>Morgan Stanley:</b> Morgan Stanley | Wealth Management Contact Center Analytics: Leading AI-driven analytics and Genesys Cloud IVR migrations to transform interaction data into actionable, role-based dashboards. Partnering with engineering squads to deploy Generative AI use cases—including call summarization and agent productivity metrics—successfully reducing manual analysis effort by 30%", bullet_style))
    story.append(Paragraph("• <b>BNY Mellon:</b> BNY Mellon | IAM Adoption Program: Managed a 70-member team onboarding ~1,000 global applications annually onto a centralized SailPoint platform. Standardized access governance across multiple business lines and streamlined tracking with custom JIRA dashboards.", bullet_style))
    story.append(Paragraph("• <b>First Abu Dhabi Bank:</b> First Abu Dhabi Bank | Core T24 Modernization & PMO: Managed PMO delivery coordinates for core T24 banking modernization and data migrations. Steered cross-product consumer protection regulation alignments and compliance mapping, achieving flawless PwC audit sign-offs.", bullet_style))
    story.append(Spacer(1, 6))

    # Gravity iLabs
    story.append(Paragraph("<b>Gravity iLabs</b> (Dec 2019 - Aug 2021)  |  <b>Business Analyst / Product Owner / Scrum Master</b>", company_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("• <b>Government & Higher Australian Clients:</b> Spearheaded agile delivery and customized strategic Jira and Power BI dashboards to drive enterprise performance monitoring for premium public sector clients.", bullet_style))
    story.append(Spacer(1, 6))

    # TCS
    story.append(Paragraph("<b>Tata Consultancy Services</b> (Jan 2013 - Dec 2019)  |  <b>Subject Matter Expert / IT Analyst</b>", company_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("• <b>Citibank NA (Client Site):</b> Served as Subject Matter Expert and Business Analyst across North American retail banking applications, ServiceNow implementations, and internal Six Sigma audit portals.", bullet_style))
    story.append(Spacer(1, 8))

    # 5. Education
    story.append(Paragraph("EDUCATION", section_heading))
    edu_text = "<b>Bachelor of Engineering (B.E.)</b>  |  Rajiv Gandhi Proudyogiki Vishwavidyalaya, Bhopal  |  <i>Graduated: 2012</i>"
    story.append(Paragraph(edu_text, body_style))

    # Build the document
    doc.build(story)
    print("PDF generated successfully.")

if __name__ == "__main__":
    generate_pdf()
