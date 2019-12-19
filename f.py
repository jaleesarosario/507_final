import requests
from bs4 import BeautifulSoup
import csv
import plotly.graph_objs as go
import sqlite3
import plotly.graph_objects as go
import plotly.figure_factory as ff


#### Part 2 ####

#Scrape Flower Page is via scrap.py
#create floral db
DBNAME = 'Floral.db'
#Create Floral Db
try:
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    statement = '''
        DROP TABLE IF EXISTS 'Colors';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Flowers';
    '''
    cur.execute(statement)

    statement = '''
        CREATE TABLE 'Colors' (
            'ColorId' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Colors' TEXT NOT NULL
        );
    '''
    cur.execute(statement)
    statement = '''
        CREATE TABLE 'Flowers' (
                'FlowerId' INTEGER PRIMARY KEY AUTOINCREMENT,
                'Common Name' TEXT NOT NULL,
                'Family Name' TEXT NOT NULL,
                'Latin Name' TEXT NOT NULL,
                'Description' TEXT NOT NULL,
                'ColorID' INTEGER NOT NULL
        );
    '''
    cur.execute(statement)
    conn.commit()

except:
    print("SQLite Table Error!")


#Finish + Unittest!
try:
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    with open('brown.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for row in enumerate(reader):
            insertion = (None, row[0],row[1],row[2],row[3],row[4])
            statement = 'INSERT INTO "Flowers"'
            statement += 'VALUES (?,?,?,?)'
            cur.execute(statment, insertion)
    cursor.commit()
    conn.close()
except:
    print('Populating db error!')

#finish the sqlite logic!!!!!

def hbar_plot():
    fig = go.Figure(go.Bar(
    x=[31, 27, 6, 1, 15, 9, 19, 6, 22, 7],
    y=['White', 'Yellow', 'Orange', 'Brown', 'Red', 'Magenta', 'Pink', 'Lavender', 'Purple', 'Blue'],
    orientation='h'))
    fig.update_layout(title_text= 'Basic Bar of Flowers by Colors')
    return fig.show()

def pie_plot():
    labels = ['White', 'Yellow', 'Orange', 'Brown', 'Red', 'Magenta', 'Pink', 'Lavender', 'Purple', 'Blue']
    values=[31, 27, 6, 1, 15, 9, 19, 6, 22,7]
    fig = go.Figure(data=[go.Pie(labels=labels,values=values)])
    fig.update_layout(title_text= 'Percent of Flowers by Colors')
    return fig.show()

def funnel_plot():
    fig = go.Figure(go.Funnelarea(text = ['White', 'Yellow', 'Orange', 'Brown', 'Red', 'Magenta', 'Pink', 'Lavender', 'Purple', 'Blue'],
    values = [31, 27, 6, 1, 15, 9, 19, 6, 22,7]))
    fig.update_layout(title_text= 'Funnel of Flowers by Colors')
    return fig.show()

def sun_plot():
    fig =go.Figure(go.Sunburst(labels=['White', 'Yellow', 'Orange', 'Brown', 'Red', 'Magenta', 'Pink', 'Lavender', 'Purple', 'Blue'],
    parents=['White', 'Yellow', 'Orange', 'Brown', 'Red', 'Magenta', 'Pink', 'Lavender', 'Purple', 'Blue'],
    values=[31, 27, 6, 1, 15, 9, 19, 6, 22, 7],
    branchvalues="total",))

    fig.update_layout(title_text= 'Brust of Flowers by Colors')
    return fig.show()

def load_help():
    with open('help.txt') as f:
        return f.read()


def interactive_prompt():
    help_txt = load_help()
    pie = pie_plot()
    hbar = hbar_plot()
    sun = sun_plot()
    funnel = funnel_plot()
    floweramt = ['31', '27', '6', '1', '15', '9', '19', '6', '22','7']
    response = ''
    while response != 'exit':
        response = input('Welcome! | Start with "help" | Search by Color | End with "exit" : ')
        if response == 'help':
            print(help_txt)
            continue
        elif response == 'white':
            print('There are ' +  floweramt[0]  + ' white flowers in the database!')
            continue
        elif response == 'yellow':
            print('There are ' +  floweramt[1]  + ' yellow flowers in the database!')
            continue
        elif response == 'orange':
            print('There are ' +  floweramt[2]  + ' orange flowers in the database!')
            continue
        elif response == 'brown':
            print('There are ' +  floweramt[3]  + ' brown flowers in the database!')
            continue
        elif response == 'red':
            print('There are ' +  floweramt[4]  + ' red flowers in the database!')
            continue
        elif response == 'magenta':
            print('There are ' +  floweramt[5]  + ' magenta flowers in the database!')
            continue
        elif response == 'pink':
            print('There are ' +  floweramt[6]  + ' pink flowers in the database!')
            continue
        elif response == 'lavender':
            print('There are ' +  floweramt[7]  + ' lavender flowers in the database!')
            continue
        elif response == 'purple':
            print('There are ' +  floweramt[8]  + ' purple flowers in the database!')
            continue
        elif response == 'blue':
            print('There are ' +  floweramt[9]  + ' blue flowers in the database!')
            continue
        elif response == 'exit':
            print('Go smell the flowers!')
            break


#Interactive Prompt
if __name__=="__main__":
    interactive_prompt()
