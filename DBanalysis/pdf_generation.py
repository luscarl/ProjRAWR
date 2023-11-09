import pandas as pd

import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from statsmodels.tsa.arima.model import ARIMA

images_and_captions = []
images_and_captionsal = []

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
    print(trdf)
    (topal, talpax, taly, talrev) = aldf
    formatPNGdf(trdf)
    formatPNGal(aldf)
    add_images_and_captions(rdf, topal, origin, dest, 'output.pdf', images_and_captions)

def alpax(df):
    x = df['month']
    y_columns = df.columns[1:5].to_list()
    for column in y_columns:
        plt.plot(x, df[column], label = column)
    plt.legend()
    plt.title('Monthly Total Pax by airlines')
    plt.xlabel('date')
    plt. grid(axis= 'y', color= 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('Total_Pax_AL.png')
    paragraphstr = f"""As of {df.iloc[-1,0]},"""
    images_and_captionsal.append({'image_path': 'Total_Pax_AL.png', 'caption': 'Monthly total passengers from airlines with the most passenger'})
    plt.show()

def alrev(df):
    x = df['month']
    y_columns = df.columns[1:5].to_list()
    for column in y_columns:
        plt.plot(x, df[column], label = column)
    plt.legend()
    plt.title('Monthly average revenue by airlines')
    plt.xlabel('date')
    plt. grid(axis= 'y', color= 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('Avg_Rev_AL.png')
    images_and_captionsal.append({'image_path': 'Avg_Rev_AL.png', 'caption': 'Monthly average revenue from airlines with the most passenger'})
    plt.show()

def alyield(df):
    x = df['month']
    y_columns = df.columns[1:5].to_list()
    for column in y_columns:
        plt.plot(x, df[column], label = column)
    plt.legend()
    plt.title('Monthly average yield by airlines')
    plt.xlabel('date')
    plt. grid(axis= 'y', color= 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('Avg_yield_AL.png')
    images_and_captionsal.append({'image_path': 'Avg_yield_AL.png', 'caption': 'Monthly average yield from airlines with the most passenger'})
    plt.show()

def totalPax(df):
    df['Trend'] = df['pax'].rolling(window = 4).mean()
    plt.plot(df['month'], df['pax'], label = 'Monthly total pax', color='#294173')
    plt.plot(df['month'], df['Trend'], label='12-Month time series Trend', color='red', linestyle='--')
    
    model = ARIMA(df['pax'], order=(4,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps = 12)

    last_date = df.iloc[-1,0]
    forecast_dates = pd.date_range(start = last_date, periods = 12, inclusive = 'right', freq = 'M')
    print(forecast)
    plt.plot(forecast_dates, forecast, label = '12-Month Forecast', linestyle = '--')

    paragraphstr = f"""As of {df.iloc[-1,0]}, the total monthly passenger is {df.iloc[-1,2]}. \n"""

    plt.title('Monthly Total PAX with trend and forecast')
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('total pax')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('sum_pax.png')
    images_and_captions.append({'image_path': 'sum_pax.png',
                                'caption': 'Monthly total passengers from desired route',
                                'para':paragraphstr})
    plt.show()

def avgYields(df):
    df.plot(kind = 'line', x = 'month', y= 'yield', c = '#294173', legend = False)
    plt.title('Monthly Average Yields')
    plt.xlabel('date')
    plt.ylabel('Average Yields')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_yields.png')
    paragraphstr = f"""As of {df.iloc[-1,0]}, the average monthly yield is {df.iloc[-1,1]}. \n"""
    images_and_captions.append({'image_path': 'avg_yields.png', 
                                'caption': 'Monthly average yield from desired route',
                                'para': paragraphstr})
    
    plt.show()

def totalSeats(df):
    df.plot(kind = 'line', x = 'month', y= 'seats', c = '#294173', legend = False)
    plt.title('Monthly Total Seats')
    plt.xlabel('month-year')
    plt.ylabel('Total Seats')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.ticklabel_format(style = 'plain', axis = 'y')
    plt.savefig('sum_seats.png')
    paragraphstr = f"""As of {df.iloc[-1,0]}, the total monthly seats is {df.iloc[-1,5]}. \n"""
    images_and_captions.append({'image_path': 'sum_seats.png', 
                                'caption': 'Monthly sum of seats from desired route',
                                'para':paragraphstr})
    plt.show()

def rev(df):
    df['Trend'] = df['rev'].rolling(window = 4).mean()
    plt.plot(df['month'], df['rev'], label = 'Monthly average revenue', color='#294173')
    plt.plot(df['month'], df['Trend'], label='12-Month time series Trend', color='red', linestyle='--')
    
    model = ARIMA(df['rev'], order=(4,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps = 12)

    last_date = df.iloc[-1,0]
    forecast_dates = pd.date_range(start = last_date, periods = 12, inclusive = 'right', freq = 'M')
    print(forecast)
    plt.plot(forecast_dates, forecast, label = '12-Month Forecast', linestyle = '--')

    # df.plot(kind = 'line', x = 'month', y= 'rev', c = '#294173', legend = False)
    plt.title('Monthly Average Revenue')
    plt.legend()
    plt.xlabel('month-year')
    plt.ylabel('Average Revenue')
    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_rev.png')
    paragraphstr = f"""As of {df.iloc[-1,0]}, the average monthly revenue is {df.iloc[-1,4]}. \n"""
    images_and_captions.append({'image_path': 'avg_rev.png',
                                 'caption': 'Monthly average revenue from desired route',
                                 'para':paragraphstr})
    plt.show()
    
def porig(df):
    df.plot(kind = 'line', x = 'month', y= 'porig', c = '#294173', legend = False)
    plt.title('Average Passenger of Origin')
    plt.xlabel('month-year')
    plt.ylabel('% Passenger of Origin')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_poo.png')
    paragraphstr = f"""As of {df.iloc[-1,0]}, the average monthly passenger of origin in percentage is {df.iloc[-1,3]}. \n"""
    images_and_captions.append({'image_path': 'avg_poo.png', 
                                'caption': 'Monthly average passenger of origin from desired route',
                                'para': paragraphstr})
    plt.show()

def ask(df):
    df['Trend'] = df['ask'].rolling(window = 4).mean()
    plt.plot(df['month'], df['ask'], label = 'Monthly average ask', color='#294173')
    plt.plot(df['month'], df['Trend'], label='12-Month time series Trend', color='red', linestyle='--')
    
    model = ARIMA(df['ask'], order=(4,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps = 12)

    last_date = df.iloc[-1,0]
    forecast_dates = pd.date_range(start = last_date, periods = 12, inclusive = 'right', freq = 'M')
    print(forecast)
    plt.plot(forecast_dates, forecast, label = '12-Month Forecast', linestyle = '--')

    # df.plot(kind = 'line', x = 'month', y= 'ask', c = '#294173', legend = False)
    plt.title('Average ASK')
    plt.legend()
    plt.xlabel('month-year')
    plt.ylabel('ASK')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.ticklabel_format(style = 'plain', axis = 'y')
    plt.savefig('avg_ask.png')
    paragraphstr = f"""As of {df.iloc[-1,0]}, the average monthly ASK is {df.iloc[-1,6]}. \n"""
    images_and_captions.append({'image_path': 'avg_ask.png',
                                'caption': 'Monthly average yield from desired route',
                                'para': paragraphstr})
    plt.show()

def add_images_and_captions(df, aldf, origin, dest, pdf_filename, images_and_captions):
    story = []
    styles = getSampleStyleSheet()
    title_style = styles['Title']

    title = Paragraph(title_generation(origin, dest), title_style)
    story.append(title)

    intro = Paragraph(intro_generation(origin, dest))
    story.append(intro)
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    

    styles = getSampleStyleSheet()
    centered_style = ParagraphStyle(name='CenteredStyle', parent=styles['Normal'], alignment=TA_CENTER)
    
    for item in images_and_captions:
        image = Image(item['image_path'], width=4*inch, height=3*inch)
        caption = Paragraph(item['caption'], centered_style)
        p = item.get('para')
        print(item.keys())
        pgraph = Paragraph(p, styles['Normal'])
        story.append(pgraph)
        data = [[image], [caption]]
        table = Table(data)
        
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER')
        ]))
        
        
        story.append(table)
        story.append(Spacer(1, 0.2*inch))  

    for item in images_and_captionsal:
        image = Image(item['image_path'], width=4*inch, height=3*inch)
        caption = Paragraph(item['caption'], centered_style)
        
        data = [[image], [caption]]
        table = Table(data)
        
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ]))
        para = Paragraph(f"This is a paragraph before the table", styles['Normal'])
        story.append(para)
        story.append(table)
        story.append(Spacer(1, 0.2*inch))  

    doc.build(story)

def title_generation(origin, dest):
    originstr = ''
    deststr = ''
    for orig in origin:
        originstr = originstr + f"{orig} "
    for d in dest:
        deststr = deststr + f"{d} "

    if len(dest) == 0:
        return f"Report of flights from {originstr}"

    return f"Report: Data for flights from {originstr} to {deststr}"

def intro_generation(origin, dest):
    originstr = ''
    deststr = ''
    for orig in origin:
        originstr = originstr + f"{orig} "
    for d in dest:
        deststr = deststr + f"{d} "

    if len(dest) == 0:
        return f"""This report focuses on key performance metrics and
        trends on data which have potential impacts on flights from {originstr}. 
        The report includes a variety of data,
          including the total number of passengers, average revenue,
            yield, and passenger of origin. \n \n
            """

    str = f"""This report focuses on key performance metrics and
        trends on data which have potential impacts on flights from {originstr} to {deststr}. 
        The report includes a variety of data,
          including the total number of passengers, average revenue,
            yield, and passenger of origin. \n \n
            """
    return str
    
def alstr_generation(origin, dest, aldf):
    originstr = ''
    deststr = ''
    alstr = ''
    for orig in origin:
        originstr = originstr + f"{orig} "
    for d in dest:
        deststr = deststr + f"{d} "
    al = aldf['airline'].to_list()
    for a in al:
        alstr = alstr + f"{a} "

    gstr = f""" The top 4 airlines with the most passengers travelling 
                from {originstr} to {deststr} are {alstr}. The analysis of airline is of below."""
