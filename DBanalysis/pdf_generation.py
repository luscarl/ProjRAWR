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

def totalPax(df):
    df.plot(kind = 'line', x = 'month',y = 'pax', c = '#294173', legend = False)
    plt.title('Monthly Total PAX')
    plt.xlabel('date')
    plt.ylabel('total pax')
    plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('sum_pax.png')

def avgYields(df):
    df.plot(kind = 'line', x = 'month', y= 'yield', c = '#294173', legend = False)
    plt.title('Monthly Average Yields')
    plt.xlabel('date')
    plt.ylabel('Average Yields')
    plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_yields.png')

def totalSeats(df):
    df.plot(kind = 'line', x = 'month', y= 'seats', c = '#294173', legend = False)
    plt.title('Monthly Total Seats')
    plt.xlabel('month-year')
    plt.ylabel('Total Seats')
    plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('sum_seats.png')

def rev(df):
    df.plot(kind = 'line', x = 'month', y= 'rev', c = '#294173', legend = False)
    plt.title('Monthly Average Revenue')
    plt.xlabel('month-year')
    plt.ylabel('Average Revenue')
    plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_rev.png')
    
def porig(df):
    df.plot(kind = 'line', x = 'month', y= 'porig', c = '#294173', legend = False)
    plt.title('Average Passenger of Origin')
    plt.xlabel('month-year')
    plt.ylabel('% Passenger of Origin')
    plt.grid(axis = 'y', color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.savefig('avg_poo.png')




