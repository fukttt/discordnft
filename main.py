import requests
import time
import sys

counter = {}
conf = {
    'telegramToken': 'TG_TOKEN',
    'discordToken': 'DS_TOKEN',
    'chat_id': 'CHAT_ID'
}
def getLastMessage(channelName, channelId, channelImage):
    try:
        headers = {'accept': '*/*',
                   'authorization': conf['discordToken'],
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
                   'x-debug-options': 'bugReporterEnabled',
                   'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InJ1IiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA1NjkxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
                   }
        r = requests.get('https://discord.com/api/v9/channels/'+channelId+'/messages?limit=50', headers=headers)
        data = r.json()
        if channelName in counter:
            if data[0]['id'] != counter[channelName]:
                # write to telegram
                r = requests.get('https://api.telegram.org/bot'+conf['telegramToken']+'/sendPhoto?chat_id='+conf['chat_id']+'&caption=@username\nДоступно новое сообщение в канале '+channelName+' ['+data[0]['timestamp']+'] \n' + data[0]['content'] + '&photo=' + channelImage +'&parse_mode=markdown', headers=headers)
        else:
            r = requests.get('https://api.telegram.org/bot' + conf['telegramToken'] + '/sendPhoto?chat_id=' + conf[
                'chat_id'] + '&caption=Инициализация в канале ' + channelName + '\n__Последнее сообщение__:\n' + data[0]['content'] + '&photo=' + channelImage +'&parse_mode=markdown', headers=headers)
        counter[channelName] = data[0]['id']
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

if __name__ == "__main__":
    while True:
        getLastMessage("*Warsaken.Wencod*", "913531949908385822", "https://cdn.discordapp.com/icons/839530514469355581/a_2b19675c60059b17a66b1dd2e00e42eb.png?size=300")
        getLastMessage("*Warsaken.Hoard*", "914289108988362792", "https://cdn.discordapp.com/icons/839530514469355581/a_2b19675c60059b17a66b1dd2e00e42eb.png?size=300")
        getLastMessage("*RealmsOFArkova.Giveaway*", "874518142485946378", "https://cdn.discordapp.com/icons/867118825480519720/e03fff1b0f66d64bda41c448c4680b74.png?size=300")
        getLastMessage("*DragonsValley.Giveaway*", "908615007472873492", "https://cdn.discordapp.com/icons/875740058353823794/a_305de82bfbbf4ec780236107535e3a7b.png?size=300")
        getLastMessage("*BeastGarden.Giveaway*", "866689249218265098", "https://cdn.discordapp.com/icons/853579680229752862/74d64ec974e47eadad1bc9552658aecf.png?size=300")
        getLastMessage("*CosmosEleven.Giveaway*", "888811986979291160", "https://cdn.discordapp.com/icons/877280237895942144/d06e62582106b1ea9c72438be95d3472.png?size=300")
        getLastMessage("*TheApocalyptics.Giveaway*", "840217221606277131", "https://cdn.discordapp.com/icons/838335599357329439/a_c12280606583c44d8385217d4fe25f2e.png?size=300")
        getLastMessage("*ZombieCoin.Giveaway*", "865812621440843777", "https://cdn.discordapp.com/icons/864977070261796864/120988e356f3be4e4c579ca1a847f709.png?size=300")
        getLastMessage("*MoonStones.Giveaway*", "864869866002448384", "https://cdn.discordapp.com/icons/843892782640005170/a_5e9f6a952a0832def86c3d1382e2b32e.png?size=300")
        getLastMessage("*DracoDice.Giveaway*", "891318519348731974", "https://cdn.discordapp.com/icons/888403994349809694/9d1cded4f8535328478e2e99811b7bad.png?size=300")
        getLastMessage("*SuperScience.Giveaway*", "883148004813574174", "https://cdn.discordapp.com/icons/883144283270570094/851252864e1d8a9a1a4c5899bd38f879.png?size=300")
        getLastMessage("*SpaceX.Anouncements*", "909075736676167761", "https://cdn.discordapp.com/icons/900754027342606377/79509f0f8284f2ec673c87a302f7c227.png?size=300")
        getLastMessage("*ElvenWorld.Giveaway*", "904784252510552074", "https://cdn.discordapp.com/icons/895322499917701161/a_3dd43b5861ac9492b7a841b2595a156e.png?size=96")

        #Засыпаем на 10 секунд
        time.sleep(10)

