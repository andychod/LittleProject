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
            return [0,"give_song"]
        elif(msg.find("生成歌詞")!=-1):
            	return [10,"~~~生成歌詞~~~"]
        else:
            #非關鍵字類
            response = self.getBotResponse(msg) #取得chatterbot的回應
            #print("response = " + str(response))
            if(self.index==0):
                # return [0]["Lry"]
                self.index +=1
                return [1,"回應歌詞"]
            elif(self.index==1):
                self.index +=1
                return [2,"恩恩，再給我一些提示"]
            else:
                self.index = 0;
                return  [3,"你喜歡某某歌手齁"]


    def getBotResponse(self,msg):
        #這邊進行連接server api的程式

        #回傳值
        #[
        #  {
        #   "confidence": float,
        #   "kkboxID": string,
        #   "Artists":  string,
        #   Lry": string,
        #   "SongName": string
        #   },
        #   ...
        # ]
        return_list = []
        # 將結果存起來
        for dd in return_list:
            self.SaveSongMsg(dd)
        return_list = sorted(return_list, key=lambda s: s['confidence'], reverse=True)
        #("return_list = "+ str(return_list))
        return return_list


    def SaveSongMsg(self,data):
        #print("in getSongID_andSave()")
        if(len(self.songIDList) == 0):
            insideData = {
                'ID':data['kkboxID'],
                'times':1,
                'Artists':data['Artists'],
                "Confidence":data['confidence']
            }
            self.songIDList.append(insideData)
        else:
            dd = [d for d in self.songIDList if d.get('ID')==data['kkboxID']]
            if(len(dd) == 0): #如果不存在
                insideData = {
                    'ID':data['kkboxID'],
                    'times':1,
                    'Artists':data['Artists'],
                    "Confidence":data['confidence']
                }
                self.songIDList.append(insideData)
            else:
                for i in range(len(self.songIDList)):
                    if(self.songIDList[i]['ID'] == data['kkboxID']):
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