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


#change color names manually to get the proper csvs - no time for the extra

    with open('purple.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(color_list)
        writer.writerow(family_list)
        writer.writerow(la_list)
        writer.writerow(decs_list)

#print(get_details_by_color("purple"))
