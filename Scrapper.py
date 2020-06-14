from bs4 import BeautifulSoup as ScraP
from urllib.request import urlopen as uReq
import openpyxl as opxl

List = []



Top_100_Mobile = opxl.Workbook()
iOS_Top_100 = Top_100_Mobile.get_sheet_by_name('Sheet')
iOS_Top_100.title = "iOS Top 100"


iOS_Top_100['A1'] = "Game Name"
iOS_Top_100['B1'] = "URL"



#my_url = 'https://itunes.apple.com/us/genre/ios-games/id6014?mt=8'
my_url = 'https://itunes.apple.com/jp/genre/ios-games/id6014?mt=8'


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = ScraP(page_html, "html.parser")

coloumn = page_soup.find_all("div", {"class": "column"})
game_list_1 = coloumn[0].find_all('li')
for game_rank in range(len(game_list_1)):
    List.append([game_list_1[game_rank].text])
    List[game_rank].append(game_list_1[game_rank].a["href"])
    #print(game_list_1[game_rank].text, "   ", game_list_1[game_rank].a["href"])


coloumn_2 = page_soup.find_all("div", {"class": "column"})
game_list_2 = coloumn[1].find_all('li')
for game_rank in range(20):
    List.append([game_list_1[game_rank].text])
    List[game_rank+80].append(game_list_1[game_rank].a["href"])
    #print(game_list_2[game_rank].text, "   ", game_list_2[game_rank].a["href"])

for i in range(100):
    iOS_Top_100['A' + str(i+2)] = List[i][0]
    iOS_Top_100['B' + str(i+2)] = List[i][1]

Top_100_Mobile.save('F:\\jobs\\Games_List.xlsx')



