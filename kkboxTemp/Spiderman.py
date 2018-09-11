import requests
import math
import json

class Hero():
    def __init__(self, name):
        self.name = name
        # 存入歌曲的kkboxID
        self.songIDList = []
        # 黑白名單
        self.whitelist = []
        self.blacklist = []
        #選擇的作者
        self.chooseArtist = ""
        self.index = 0



    def run(self, msg):
        #使用者想要歌曲了
        if(msg.find("給我歌曲")!=-1):
            res = self.getSongURL()
            return [0,"give_song"]
        elif(msg.find("生成歌詞")!=-1):
                return [10,"~~~生成歌詞~~~"]
        else:
            #非關鍵字類
            response = self.getBotResponse(msg) #取得chatterbot的回應
            #print("response = " + str(response))
            if(self.index==0):
                # return [0]["Lry"]
                #self.index +=1
                return [1,response[0]['Lys']]
            elif(self.index==1):
                self.index +=1
                return [2,"恩恩，再給我一些提示"]
            else:
                self.index = 0;
                return  [3,"你喜歡某某歌手齁"]

    def getBotResponse(self,msg):
        #這邊進行連接server api的程式
        url = "http://140.138.77.90:6666/sum?userinput=" + msg
        r = requests.get(url)
        print(r.text)
        APImsg = r.text.split(",")
        n = len(APImsg)
        valueArray = []
        for i in range(0,int(math.floor(n/4))):
            Obj = {
                "Singer":APImsg[4*i],
                "kkID":APImsg[4*i + 1],
                "Lys":APImsg[4*i + 2],
                "SongName":APImsg[4*i + 3]
            }
            valueArray.append(Obj)
        # 此時，valueArray為以下結構，並且事已經照configence降冪排了了
        #[
        # {
        #   'Singer': string,
        #   'kkID': string,
        #   'Lys': string,
        #   'SongName': string
        # },
        # ...
        #]
        # 將結果存起來
        for dd in valueArray:
            self.SaveSongMsg(dd)
        return valueArray
        


    def SaveSongMsg(self,data):
        #print("in getSongID_andSave()")
        if(len(self.songIDList) == 0):
            insideData = {
                'ID':data['kkID'],
                'times':1,
                'Artists':data['Singer'],
                'SongName':data['SongName']
            }
            self.songIDList.append(insideData)
        else:
            dd = [d for d in self.songIDList if d.get('ID')==data['kkID']]
            if(len(dd) == 0): #如果不存在
                insideData = {
                    'ID':data['kkID'],
                    'times':1,
                    'Artists':data['Singer'],
                    "SongName":data['SongName']
                }
                self.songIDList.append(insideData)
            else:
                for i in range(len(self.songIDList)):
                    if(self.songIDList[i]['ID'] == data['kkID']):
                        self.songIDList[i]['times'] = self.songIDList[i]['times'] + 1
                        break


    def addWhiteList(self):
        #增加 白名單 的程式碼
        print("加入白名單")
    
    def addBlackList(self):
        #增加 黑名單 的程式碼
        print("加入黑名單")

    def Reset(self):
        # 存入歌曲的kkboxID
        self.songIDList = []
        # 黑白名單
        self.whitelist = []
        self.blacklist = []
        #選擇的作者
        self.chooseArtist = ""
        self.index = 0

    def getSongURL(self):
        print("In getSongURL")
        print(self.songIDList[0]['SongName'])
        self.songIDList = sorted(self.songIDList, key=lambda s: s['times'], reverse=True)
        print(self.songIDList)
        size = len(self.songIDList)
        urlList = []
        if(size < 3):
            for dd in self.songIDList:
                print("ID = " + str(dd['ID']))
                r = requests.get('http://140.138.77.90:3005/youtubeLink/' + dd['ID'])
                rData = json.loads(r.text)
                urlList.append(rData["youtubeLink"])
        else:
            for i in range(3):
                print("URL~~ http://140.138.77.90:3005/youtubeLink/"+self.songIDList[i]['ID'])
                r = requests.get('http://140.138.77.90:3005/youtubeLink/' + self.songIDList[i]['ID'])
                rData = json.loads(r.text)
                urlList.append(rData["youtubeLink"])
        print("urlList = "+ str(urlList))
        return "~~give url~~"
