from bs4 import BeautifulSoup



with open('nba.html', 'rb') as fd:
    with open('nba.txt', 'a') as fd2:
        soup = BeautifulSoup(fd.read(), 'html.parser')
        tbody = soup.find_all('tbody', class_ = 'Crom_body__UYOcU')[0]
        player_info = tbody.find_all('tr')
        for player in player_info:
            allInfo = player.find_all('td')
            playerName = allInfo[1].text.strip()
            playerAverage = allInfo[5].text.strip()
            info = f'{playerName},{playerAverage}\n'
            fd2.write(info)
    