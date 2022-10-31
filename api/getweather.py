import requests

# Get data uchun
def checkweather(data):
    bulut = 0
    quyosh = 0
    if "#svg-symbol-cloud" in data:
        bulut = 1
    if "#svg-symbol-moon" in data:
        oy = 1   
    if "#svg-symbol-sun" in data:
        quyosh = 1
    tomchilar = data.count("#svg-symbol-drop")
    if bulut == 1:
        if quyosh == 1:
            if tomchilar > 0:
                text = "🌦"
            else:
                text = "🌥"
        elif tomchilar > 0:
            text = "🌧"
        else:
            text = "☁️"
    elif quyosh == 1:
        text = "☀️"
    else:
        text = "☁️"
    return text


havodict = {
    "48°" : "9°",
    "49°" : "9°",
    "50°" : "10°",
    "51°" : "10°",
    "52°" : "11°",
    "53°" : "12°",
    "54°" : "13°",
    "55°" : "13°",
    "56°" : "13°",
    "57°" : "14°",
}

def Gethavo(havo):
    try:
        havo = havodict.get(havo)
    except:
        havo = havo
    return havo

    
def getdata(data):
    havo = data.split('class="DetailsSummary--tempValue--jEiXE">')
    havo = havo[1].split('</span>')
    havoholati = havo[1].split('class="DetailsSummary--extendedData--307Ax">')
    havoholati = havoholati[1].split("</span>")
    yomgirextimoli = data.split('<span data-testid="PercentageValue">')
    yomgirextimoli = yomgirextimoli[1].split('</span>')
    sticker = checkweather(data)
    havo = Gethavo(havo[0])
    return [sticker, havo, havoholati[0], yomgirextimoli[0]]

url = "https://weather.com/weather/hourbyhour/l/33c0f7b1947c47dc2c6eb51f0411c58549e0573a6f20b8584ff36c797b7de3e1?par=samsung_widget"
data = requests.get(url)
alldata = data.text

bugun1 = alldata.split('class="HourlyForecast--longDate--J_Pdh">')
bugun = bugun1[1].split('</h2>')
vaqt = bugun[1].split('class="DetailsSummary--daypartName--kbngc">')

res_list = []
def getweather():
    for i in range(1, len(vaqt)):
        soat = vaqt[i].split('</h3>')
        data = getdata(vaqt[i])
        res_list.append([soat[0], data])
    return res_list






