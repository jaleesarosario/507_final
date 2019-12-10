import requests
from bs4 import BeautifulSoup
import csv
import plotly.graph_objs as go
import sqlite3
import plotly.graph_objects as go
import plotly.figure_factory as ff


#### Part 1 ####

#Scrape Flower Page
def get_details_by_color(color):
    color_num = 0
    color_id = []
    color_list = []
    link_list = []
    family_list = []
    la_list = []
    decs_list = []
    one_flower = []
    baseurl = 'http://researcharchive.calacademy.org'
    white_wf = baseurl + '/research/botany/wildflow/color.asp?c=' + color
    header = {'User-agent': 'Mozilla/5.'}
    page_text = requests.get(white_wf, headers=header).text
    page_soup = BeautifulSoup(page_text,'html.parser')
    wfresults = page_soup.findAll(True, {'class':["wfresultname"]})

    if color == 'white':
        color_num = 1
    elif color == 'yellow':
        color_num = 2
    elif color == 'orange':
        color_num = 3
    elif color == 'brown':
        color_num = 4
    elif color == 'red':
        color_num = 5
    elif color == 'pink':
        color_num = 6
    elif color == 'magenta':
        color_num = 7
    elif color == 'lavender':
        color_num = 8
    elif color == 'purple':
        color_num = 9
    elif color == 'blue':
        color_num = 10

    for item in wfresults:
        link_list.append(item.find("a")['href'])
        #print(item)

    for color in wfresults:
        wfcommon = color.find(True, {'class':["wfcolorNames"]})
        color_list.append(wfcommon.getText())

    for fam in wfresults:
        family = fam.find(True, {'class':["wfname"]})
        family_list.append(family.getText())

    for lat in wfresults:
        latin = lat.find(True, {'class':["wfname wfitalic"]})
        la_list.append(latin.getText())

        for link in link_list:
            wf = baseurl + '/research/botany/wildflow/' + link
            page_text2 = requests.get(wf, headers=header).text
            page_soup2 = BeautifulSoup(page_text2,'html.parser')
            decs = page_soup2.find(True, {'id':"wfdescription_column"})
            wfdecs = decs.find(True, {'class':['bodytext']})
            decs_list.append(wfdecs.getText())


    return color_num, color_list, family_list, la_list, decs_list

Create Floral CSV & Populate with Soup Data
with open('floral.csv', 'w', newline='') as f:
    color_ID = ['Color', 'Common Name', 'Family Name', 'Latin Name', 'Description']
    writer = csv.writer(f)
    writer.writerow(color_ID)
    writer.writerow(get_details_by_color("white"))
    writer.writerow(get_details_by_color("yellow"))
    writer.writerow(get_details_by_color("orange"))
    writer.writerow(get_details_by_color("brown"))
    writer.writerow(get_details_by_color("red"))
    writer.writerow(get_details_by_color("pink"))
    writer.writerow(get_details_by_color("magenta"))
    writer.writerow(get_details_by_color("lavender"))
    writer.writerow(get_details_by_color("purple"))
    writer.writerow(get_details_by_color("blue"))

with open('colors.csv', 'w', newline='') as f:
    color_ID = ['White', 'Yellow', 'Orange', 'Brown', 'Red','Pink', 'Magenta', 'Lavender', 'Purple', 'Blue']
    color_num = [1,2,3,4,5,6,7,8,9,10]
    writer = csv.writer(f)
    writer.writerow(color_ID)
    writer.writerow(color_num)

#create floral db
DBNAME = 'Floral.db'
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
            'White' INTEGER,
            'Yellow' INTEGER,
            'Orange' INTEGER,
            'Brown' INTEGER,
            'Red' INTEGER,
            'Pink' INTEGER,
            'Magenta' INTEGER,
            'Lavender' INTEGER,
            'Purple' INTEGER,
            'Blue' INTEGER
        );
    '''
    cur.execute(statement)

    statement = '''
        CREATE TABLE 'Flowers' (
            'ColorId' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Common Name' TEXT NOT NULL,
            'Family Name' TEXT NOT NULL,
            'Latin Name' TEXT NOT NULL,
            'Description' TEXT NOT NULL
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

    with open('floral.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            cur.execute('INSERT')

    with open('color.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            cur.excute('INSERT INTO Colors ()')

    cursor.commit()
    cursor.close()
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
