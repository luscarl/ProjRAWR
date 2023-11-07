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


