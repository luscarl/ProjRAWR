import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.flowables import PageBreak


def formatPNGdf(df):
    totalPax(df)
    avgYields(df)
    totalSeats(df)
    rev(df)
    porig(df)
    ask(df)

def formatPDF(trdf, aldf, origin, dest):
    formatPNGdf(trdf)




def totalPax(df):
    df.plot(kind = 'line', x = 'month',y = 'pax', c = '#294173', legend = False)
    plt.title('Monthly Total PAX')
    plt.xlabel('date')
    plt.ylabel('total pax')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('sum_pax.png')
    plt.show()

def avgYields(df):
    df.plot(kind = 'line', x = 'month', y= 'yield', c = '#294173', legend = False)
    plt.title('Monthly Average Yields')
    plt.xlabel('date')
    plt.ylabel('Average Yields')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_yields.png')
    plt.show()

def totalSeats(df):
    df.plot(kind = 'line', x = 'month', y= 'seats', c = '#294173', legend = False)
    plt.title('Monthly Total Seats')
    plt.xlabel('month-year')
    plt.ylabel('Total Seats')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('sum_seats.png')
    plt.show()

def rev(df):
    df.plot(kind = 'line', x = 'month', y= 'rev', c = '#294173', legend = False)
    plt.title('Monthly Average Revenue')
    plt.xlabel('month-year')
    plt.ylabel('Average Revenue')
    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_rev.png')
    plt.show()
    
def porig(df):
    df.plot(kind = 'line', x = 'month', y= 'porig', c = '#294173', legend = False)
    plt.title('Average Passenger of Origin')
    plt.xlabel('month-year')
    plt.ylabel('% Passenger of Origin')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_poo.png')
    plt.show()

def ask(df):
    df.plot(kind = 'line', x = 'month', y= 'ask', c = '#294173', legend = False)
    plt.title('Average ASK')
    plt.xlabel('month-year')
    plt.ylabel('ASK')
    plt.grid( color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.ticklabel_format(style = 'plain', axis = 'y')
    plt.savefig('avg_ask.png')
    plt.show()
