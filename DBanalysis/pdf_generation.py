import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER

images_and_captions = []

def formatPNGdf(df):
    totalPax(df)
    avgYields(df)
    totalSeats(df)
    rev(df)
    porig(df)
    ask(df)

def formatPNGal(df):
    (topal, talpax, taly, talrev) = df
    alpax(talpax)
    alyield(taly)
    alrev(talrev)


def formatPDF(trdf, aldf, rdf, origin, dest):
    (topal, talpax, taly, talrev) = aldf
    formatPNGdf(trdf)
    formatPNGal(aldf)
    add_images_and_captions(rdf, topal, origin, dest, 'output.pdf', images_and_captions)

def alpax(df):
    print(df)
    x = df['month']
    y_columns = df.columns[1:5].to_list()
    for column in y_columns:
        plt.plot(x, df[column], label = column)
    plt.legend()
    plt.title('Monthly Total Pax by airlines')
    plt.xlabel('date')
    plt. grid(axis= 'y', color= 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('Total_Pax_AL.png')
    images_and_captions.append({'image_path': 'Total_Pax_AL.png', 'caption': 'Monthly total passengers from airlines with the most passenger'})
    plt.show()

def alrev(df):
    print(df)
    x = df['month']
    y_columns = df.columns[1:5].to_list()
    for column in y_columns:
        plt.plot(x, df[column], label = column)
    plt.legend()
    plt.title('Monthly average revenue by airlines')
    plt.xlabel('date')
    plt. grid(axis= 'y', color= 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('Avg_Rev_AL.png')
    images_and_captions.append({'image_path': 'Avg_Rev_AL.png', 'caption': 'Monthly average revenue from airlines with the most passenger'})
    plt.show()

def alyield(df):
    print(df)
    x = df['month']
    y_columns = df.columns[1:5].to_list()
    for column in y_columns:
        plt.plot(x, df[column], label = column)
    plt.legend()
    plt.title('Monthly average yield by airlines')
    plt.xlabel('date')
    plt. grid(axis= 'y', color= 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('Avg_yield_AL.png')
    images_and_captions.append({'image_path': 'Avg_yield_AL.png', 'caption': 'Monthly average yield from airlines with the most passenger'})
    plt.show()

def totalPax(df):
    df['Trend'] = df['pax'].rolling(window = 4).mean()
    plt.plot(df['month'], df['pax'], label = 'Monthly total sum', color='#294173')
    plt.plot(df['month'], df['Trend'], label='12-Month time series Trend', color='red', linestyle='--')
    plt.title('Monthly Total PAX with trend')
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('total pax')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('sum_pax.png')
    images_and_captions.append({'image_path': 'sum_pax.png', 'caption': 'Monthly total passengers from desired route'})
    plt.show()

def avgYields(df):
    df.plot(kind = 'line', x = 'month', y= 'yield', c = '#294173', legend = False)
    plt.title('Monthly Average Yields')
    plt.xlabel('date')
    plt.ylabel('Average Yields')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_yields.png')
    images_and_captions.append({'image_path': 'avg_yields.png', 'caption': 'Monthly average yield from desired route'})
    plt.show()

def totalSeats(df):
    df.plot(kind = 'line', x = 'month', y= 'seats', c = '#294173', legend = False)
    plt.title('Monthly Total Seats')
    plt.xlabel('month-year')
    plt.ylabel('Total Seats')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.ticklabel_format(style = 'plain', axis = 'y')
    plt.savefig('sum_seats.png')
    images_and_captions.append({'image_path': 'sum_seats.png', 'caption': 'Monthly sum of seats from desired route'})
    plt.show()

def rev(df):
    df.plot(kind = 'line', x = 'month', y= 'rev', c = '#294173', legend = False)
    plt.title('Monthly Average Revenue')
    plt.xlabel('month-year')
    plt.ylabel('Average Revenue')
    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_rev.png')
    images_and_captions.append({'image_path': 'avg_rev.png', 'caption': 'Monthly average revenue from desired route'})
    plt.show()
    
def porig(df):
    df.plot(kind = 'line', x = 'month', y= 'porig', c = '#294173', legend = False)
    plt.title('Average Passenger of Origin')
    plt.xlabel('month-year')
    plt.ylabel('% Passenger of Origin')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_poo.png')
    images_and_captions.append({'image_path': 'avg_poo.png', 'caption': 'Monthly average passenger of origin from desired route'})
    plt.show()

def ask(df):
    df.plot(kind = 'line', x = 'month', y= 'ask', c = '#294173', legend = False)
    plt.title('Average ASK')
    plt.xlabel('month-year')
    plt.ylabel('ASK')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.ticklabel_format(style = 'plain', axis = 'y')
    plt.savefig('avg_ask.png')
    images_and_captions.append({'image_path': 'avg_ask.png', 'caption': 'Monthly average yield from desired route'})
    plt.show()

def add_images_and_captions(df, aldf, origin, dest, pdf_filename, images_and_captions):
    story = []
    styles = getSampleStyleSheet()
    title_style = styles['Title']

    # Create a title paragraph
    title = Paragraph("", title_style)
    story.append(title)

    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    

    styles = getSampleStyleSheet()
    centered_style = ParagraphStyle(name='CenteredStyle', parent=styles['Normal'], alignment=TA_CENTER)
    
    for item in images_and_captions:
        image = Image(item['image_path'], width=4*inch, height=3*inch)
        caption = Paragraph(item['caption'], centered_style)
        
        data = [[image], [caption]]
        table = Table(data)
        
        # Apply table style
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ]))
        para = Paragraph(f"This is a paragraph before the table", styles['Normal'])
        story.append(para)
        story.append(table)
        story.append(Spacer(1, 0.2*inch))  # Add space between images

    doc.build(story)

def title_generation(origin, dest):
    return "Report of title"