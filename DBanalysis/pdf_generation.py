import pandas as pd
from datetime import *
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus.flowables import KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from statsmodels.tsa.arima.model import ARIMA

images_and_captions = []
images_and_captionsal = []
date_format = "%Y-%m-%d"

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
    x = df['month']
    y_columns = df.columns[1:5].to_list()
    for column in y_columns:
        plt.plot(x, df[column], label = column)
    plt.legend()
    plt.title('Monthly Total Pax by airlines')
    plt.xlabel('date')
    plt. grid(axis= 'y', color= 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('Total_Pax_AL.png')

    max_last = df.loc[:, df.columns != 'month'].idxmax()
    min_last = df.loc[:, df.columns != 'month'].idxmin()
    
    paragraphstr = f"""This graph indicates the total passengers per month grouped by airlines."""
    
    images_and_captionsal.append({'image_path': 'Total_Pax_AL.png', 
                                  'caption': 'Monthly total passengers from airlines with the most passenger',
                                  'para':paragraphstr})
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
    max_last = df.loc[:, df.columns != 'month'].idxmax()
    min_last = df.loc[:, df.columns != 'month'].idxmin()
    paragraphstr = f"""This graph indicates the average revenue per month grouped by airlines."""
    images_and_captionsal.append({'image_path': 'Avg_Rev_AL.png',
                                   'caption': 'Monthly average revenue from airlines with the most passenger',
                                   'para':paragraphstr})
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

    max_last = df.loc[:, df.columns != 'month'].idxmax()
    min_last = df.loc[:, df.columns != 'month'].idxmin()
    paragraphstr = f"""This graph indicates the average yield per month grouped by airlines."""
    
    images_and_captionsal.append({'image_path': 'Avg_yield_AL.png',
                                   'caption': 'Monthly average yield from airlines with the most passenger',
                                   'para':paragraphstr})
    plt.show()

def totalPax(df):
    df['Trend'] = df['pax'].rolling(window = 4).mean()
    plt.plot(df['month'], df['pax'], label = 'Monthly total pax', color='#294173')
    plt.plot(df['month'], df['Trend'], label='4-Month time series Trend', color='red', linestyle='--')
    
    model = ARIMA(df['pax'], order=(4,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps = 12)

    last_date = df.iloc[-1,0]
    forecast_dates = pd.date_range(start = last_date, periods = 12, inclusive = 'right', freq = 'M')

    plt.plot(forecast_dates, forecast, label = '12-Month Forecast', linestyle = '--')

    plt.title('Monthly Total PAX with trend and forecast')
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('total pax')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('sum_pax.png')
    max = df.loc[df['pax'].idxmax()]
    min = df.loc[df['pax'].idxmin()]
    paragraphstr = f"""This graph shows the total passengers traveled per month in this route. The highest number of passenger 
                        per month is {max['pax']}, which happened in {max['month'].to_period(freq = 'M')}. 
                        The lowest number of passenger per month is {min['pax']}, which happened in {min['month'].to_period(freq = 'M')}
                          As of {df.iloc[-1,0]}, the total monthly passenger is {df.iloc[-1,2]}. \n"""
    
    lastrow = df.iloc[-1]
    seclastrow = df.iloc[-2]
    
    if (lastrow['Trend'] >= seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general upward trend according to the trend present in total passengers. "
    elif (lastrow['Trend'] < seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general downward trend according to the trend present in total passengers. Please note this is just a prediction, it may not be 100% accurate. "

    images_and_captions.append({'image_path': 'sum_pax.png',
                                'caption': 'Monthly total passengers from desired route',
                                'para':paragraphstr})
    plt.show()

def avgYields(df):
    df['Trend'] = df['yield'].rolling(window = 4).mean()
    plt.plot(df['month'], df['yield'], label = 'Monthly average yield', color='#294173')
    plt.plot(df['month'], df['Trend'], label='4-Month time series Trend', color='red', linestyle='--')

    model = ARIMA(df['yield'], order=(4,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps = 12)

    last_date = df.iloc[-1,0]
    forecast_dates = pd.date_range(start = last_date, periods = 12, inclusive = 'right', freq = 'M')

    plt.plot(forecast_dates, forecast, label = '12-Month Forecast', linestyle = '--')

    plt.title('Monthly Average Yield')
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('Average Yield')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_yields.png')

    max = df.loc[df['yield'].idxmax()]
    min = df.loc[df['yield'].idxmin()]
    paragraphstr = f"""This graph shows the average yield per month in this route. The highest average yield
                        per month is {max['yield']}, which happened in {max['month'].to_period(freq = 'M')}.
                        The lowest average yield per month is {min['yield']}, which happened in {min['month'].to_period(freq = 'M')}
                        As of {df.iloc[-1,0]}, the average monthly yield is {df.iloc[-1,1]}. \n"""
    lastrow = df.iloc[-1]
    seclastrow = df.iloc[-2]

    if (lastrow['Trend']>= seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general upward trend according to the trend present in average yields. "
    elif (lastrow['Trend'] < seclastrow['Trend']):
        paragraphstr =  paragraphstr + "There is a general downward trend according to the trend present in average yields. Please note this is just a prediction, it may not be 100% accurate. "
    
    images_and_captions.append({'image_path': 'avg_yields.png', 
                                'caption': 'Monthly average yield from desired route',
                                'para': paragraphstr})
    
    plt.show()

def totalSeats(df):
    df['Trend'] = df['seats'].rolling(window = 4).mean()
    plt.plot(df['month'], df['seats'], label = 'Monthly average seats', color='#294173')
    plt.plot(df['month'], df['Trend'], label='4-Month time series Trend', color='red', linestyle='--')

    model = ARIMA(df['seats'], order=(4,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps = 12)

    last_date = df.iloc[-1,0]
    forecast_dates = pd.date_range(start = last_date, periods = 12, inclusive = 'right', freq = 'M')

    plt.plot(forecast_dates, forecast, label = '12-Month Forecast', linestyle = '--')
    
    plt.title('Monthly Total Seats')
    plt.xlabel('month-year')
    plt.legend()
    plt.ylabel('Total Seats')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.ticklabel_format(style = 'plain', axis = 'y')
    plt.savefig('sum_seats.png')
    max = df.loc[df['seats'].idxmax()]
    min = df.loc[df['seats'].idxmin()]
    paragraphstr = f"""This graph shows the total seats provided for this route per month. The highest number of seats 
                        per month is {max['seats']}, which happened in {max['month'].to_period(freq = 'M')}.
                        The lowest number of seats per month is {min['seats']}, which happened in {min['month'].to_period(freq = 'M')}
                        As of {df.iloc[-1,0]}, the total monthly seats is {df.iloc[-1,5]}. \n"""
    lastrow = df.iloc[-1]
    seclastrow = df.iloc[-2]

    if (lastrow['Trend']>= seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general upward trend according to the trend present in total seats. "
    elif (lastrow['Trend'] < seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general downward trend according to the trend present in total seats. Please note this is just a prediction, it may not be 100% accurate. "
    
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
    
    plt.plot(forecast_dates, forecast, label = '12-Month Forecast', linestyle = '--')

    plt.title('Monthly Average Revenue')
    plt.legend()
    plt.xlabel('month-year')
    plt.ylabel('Average Revenue')
    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_rev.png')
    max = df.loc[df['rev'].idxmax()]
    min = df.loc[df['rev'].idxmin()]
    paragraphstr = f"""This graph shows the average revenue per month in this route. The highest revenue averaged per month 
                        is {max['rev']}, which happened in {max['month'].to_period(freq = 'M')}.
                        The lowest revenue averaged per month is {min['rev']}, which happened in {min['month'].to_period(freq = 'M')}
                        As of {df.iloc[-1,0]}, the average monthly revenue is {df.iloc[-1,4]}. \n"""
    lastrow = df.iloc[-1]
    seclastrow = df.iloc[-2]

    if (lastrow['Trend']>= seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general upward trend according to the trend present in average revenue. "
    elif (lastrow['Trend'] < seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general downward trend according to the trend present in average revenue. Please note this is just a prediction, it may not be 100% accurate. "
    
    images_and_captions.append({'image_path': 'avg_rev.png',
                                 'caption': 'Monthly average revenue from desired route',
                                 'para':paragraphstr})
    plt.show()
    
def porig(df):
    df['Trend'] = df['porig'].rolling(window = 4).mean()
    plt.plot(df['month'], df['porig'], label = 'Monthly average %poo origin', color='#294173')
    plt.plot(df['month'], df['Trend'], label='4-Month time series Trend', color='red', linestyle='--')
    
    model = ARIMA(df['porig'], order=(4,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps = 12)

    last_date = df.iloc[-1,0]
    forecast_dates = pd.date_range(start = last_date, periods = 12, inclusive = 'right', freq = 'M')
    plt.plot(forecast_dates, forecast, label = '12-Month Forecast', linestyle = '--')

    plt.title('Monthly average %poo origin with trend and forecast')
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('%poo origin')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_poo.png')
    max = df.loc[df['porig'].idxmax()]
    min = df.loc[df['porig'].idxmin()]

    plt.plot(forecast_dates, forecast, label = '12-Month Forecast', linestyle = '--')
    paragraphstr = f"""This graph shows the average passenger of origin in this route, which indicates the amount 
                    of passenger with residency from the country this flight departed from.
                        The highest percentage of passenger of origin 
                        per month is {max['porig']}, which happened in {max['month'].to_period(freq = 'M')}.
                        The lowest percentage of passenger of origin per month is {min['porig']}, which happened in {min['month'].to_period(freq = 'M')}
                        As of {df.iloc[-1,0]}, the average monthly passenger of origin in percentage is {df.iloc[-1,3]}. \n"""
    lastrow = df.iloc[-1]
    seclastrow = df.iloc[-2]

    if (lastrow['Trend']>= seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general upward trend according to the trend present in average passengers from country of origin. "
    elif (lastrow['Trend'] < seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general downward trend according to the trend present in total passengers from country of origin. Please note this is just a prediction, it may not be 100% accurate. "
    
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
    
    plt.plot(forecast_dates, forecast, label = '12-Month Forecast', linestyle = '--')

    # df.plot(kind = 'line', x = 'month', y= 'ask', c = '#294173', legend = False)
    plt.title('Average ASK')
    plt.legend()
    plt.xlabel('month-year')
    plt.ylabel('ASK')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.ticklabel_format(style = 'plain', axis = 'y')
    plt.savefig('avg_ask.png')
    max = df.loc[df['ask'].idxmax()]
    min = df.loc[df['ask'].idxmin()]
    paragraphstr = f"""This graph shows the average available seat kilometers per month in this route. The highest available seat kilometers 
                        per month is {max['ask']}, which happened in {max['month'].to_period(freq = 'M')}.
                        The lowest available seat kilometers per month is {min['ask']}, which happened in {min['month'].to_period(freq = 'M')}
                          As of {df.iloc[-1,0]}, the average monthly available seat kilometers is {df.iloc[-1,5]}. \n"""
    
    lastrow = df.iloc[-1]
    seclastrow = df.iloc[-2]

    if (lastrow['Trend']>= seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general upward trend according to the trend present in available seat kilometers. "
    elif (lastrow['Trend'] < seclastrow['Trend']):
        paragraphstr = paragraphstr + "There is a general downward trend according to the trend present in available seat kilometers. Please note this is just a prediction, it may not be 100% accurate. "

    images_and_captions.append({'image_path': 'sum_pax.png',
                                'caption': 'Monthly total passengers from desired route',
                                'para':paragraphstr})
    plt.show()

def add_images_and_captions(df, aldf, origin, dest, pdf_filename, images_and_captions):
    story = []
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    title_style = styles['Title']

    title = Paragraph(title_generation(origin, dest), title_style)
    story.append(title)

    intro = Paragraph(intro_generation(origin, dest))
    story.append(intro)

    story.append(Spacer(1,0.2*inch))
    secpstr = """
            The first part of this report displays the total number of passenger passenger, 
            average yield, total seats available, average revenue, average monthly passenger of origin, and 
            average available seat kilometers. Each graph will include a time series trend modeled by ARIMA,
            which is an indicator of future growth for that particular dataset. It will also include a 12 month
            forecast based on previous data.
            """
    sec = Paragraph(secpstr)
    story.append(sec)

    story.append(Spacer(1,0.2*inch))
    thirdpstr = """
            Please note that the trend and predictions in this graph is purely based on previous data,
            and may be inaccurate in the real world. Additionally, the accuracy of forecast will decrease
            with time, hence it is only suggested to use the first 3-4 month of the forecast.
    """
    third = Paragraph(thirdpstr)
    story.append(third)

    styles = getSampleStyleSheet()
    centered_style = ParagraphStyle(name='CenteredStyle', parent=styles['Normal'], alignment=TA_CENTER)
    story.append(Spacer(1, 0.2*inch))  
    for item in images_and_captions:
        tempstry = []
        image = Image(item['image_path'], width=4*inch, height=3*inch)
        caption = Paragraph(item['caption'], centered_style)
        p = item.get('para')
        
        pgraph = Paragraph(p, styles['Normal'])
        
        data = [[image], [caption]]
        table = Table(data)

        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER')
        ]))
        tempstry.append(pgraph)
        tempstry.append(table)
        tempstry.append(Spacer(1,0.2*inch))
        story.append(KeepTogether(tempstry))

    alintro = alstr_generation(origin, dest, aldf)
    story.append(Paragraph(alintro))

    for item in images_and_captionsal:
        tstry = []
        image = Image(item['image_path'], width=4*inch, height=3*inch)
        caption = Paragraph(item['caption'], centered_style)
        p = item.get('para')
        pgraph = Paragraph(p, styles['Normal'])

        data = [[image], [caption]]
        table = Table(data)
        
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER')
        ]))
        tstry.append(pgraph)
        tstry.append(table)
        tstry.append(Spacer(1,0.2*inch))
        story.append(KeepTogether(tstry))
        
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

    gstr = f""" The second part of this report analyses the top 4 airlines with the most passengers travelling 
                from {originstr} to {deststr} are {alstr}, which includes total passengers, average yield and average revenue."""

    return gstr