from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import math
import Batman as batman_class
import Spiderman as spiderman_class

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('9mmNkcLlO51C2GI5QMQ/CC349TpruYMH51hINPrcUvFiwm77PayskD+BGcAmtT2U81ZHB6kapfaxID4dOsUPIC5RvknhwR07rwKOh7daIiHsZ5IoS+7gvO5yWsOgKDcrPf0T6beC+WRG1MeQ2SiB4wdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fd0185a3712599d0b41e27952d117746')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    global superhero, appmodel



    if(superhero == 'init' or msg =='#重選英雄'):
        superhero = 'init'
        appmodel = 0
        Batman.Reset()
        Spiderman.Reset()


        if(msg == '選擇蝙蝠俠'):
            superhero = 'batman'
            #message = TextSendMessage(text="嗨~我是高雅帥氣的蝙蝠俠，我喜歡有深度有內涵的音樂，像是周杰倫和蘇打綠的音樂，就很配得上我這上流階級。")
            message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://images.vexels.com/media/users/17482/122067/raw/c54c2aed3949cf58bdf5a8586d2cddff-batman-vector.png',
                    #title='Menu',
                    text='嗨~我是高雅帥氣的蝙蝠俠，我喜歡有內涵的音樂，像是周杰倫和蘇打綠的音樂，就很配得上我這上流階級。',
                    actions=[
                        MessageTemplateAction(
                            label='猜歌詞遊戲',
                            text='#猜歌詞遊戲'
                        ),
                        MessageTemplateAction(
                            label='對話閒聊(temp)',
                            text='#對話閒聊'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        elif(msg == '選擇蜘蛛人'):
            superhero = 'spiderman'
            message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSVenbHVd6xwubCu-HvLLJmexP--ToC2YbkO_O0xPJkkQeRmSQB',
                    #title='Menu',
                    text='哈囉~我是年輕有活力的蜘蛛人。我偏愛跟我一樣的青年歌手，像是韋禮安、李佳薇和徐佳瑩都是我最愛的',
                    actions=[
                        MessageTemplateAction(
                            label='猜歌詞遊戲',
                            text='#猜歌詞遊戲'
                        ),
                        MessageTemplateAction(
                            label='對話閒聊(temp)',
                            text='#對話閒聊'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        else:
            message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    #thumbnail_image_url='https://example.com/image.jpg',
                    #title='Menu',
                    text='哈囉，歡迎來到超級英雄聯盟，今天有三位超級英雄可以陪你聊天玩遊戲，請自由選擇一位吧，每個超級英雄都會帶你經歷不一樣的超級時光！！',
                    actions=[
                        MessageTemplateAction(
                            label='蝙蝠俠',
                            text='選擇蝙蝠俠'
                        ),
                        MessageTemplateAction(
                            label='蜘蛛人',
                            text='選擇蜘蛛人'
                        ),
                        MessageTemplateAction(
                            label='邱比特(temp)',
                            text='選擇邱比特'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    else:
        if(msg == '#猜歌詞遊戲' and appmodel==0):
            appmodel = 1
            line_bot_api.reply_message(event.reply_token,
                TextSendMessage(text= "你心中一定想著某首歌吧，給我一些提示讓我猜猜看唄~~\n\n若輸入「給我歌曲」，則給出猜測的歌曲\n若輸入「生成歌詞」，我會唱一句歌詞給你\n\n Game Start!!"))
        elif(msg == '#對話閒聊' and appmodel==0):
            appmodel = 2
            line_bot_api.reply_message(event.reply_token,
                TextSendMessage(text= "(說明對話閒聊的規則)\n Game Start!!"))
        else:
            # 根據選定的超級英雄及模式到對應的功
            # 蝙蝠俠模式
            if(superhero=='batman'):
                if(msg=="#再玩一次"):
                    Batman.Reset()
                    line_bot_api.reply_message(event.reply_token,
                        TextSendMessage(text= "猜歌詞遊戲，重新開始!!"))
                if(msg == '#是'):
                    Batman.addWhiteList()
                    line_bot_api.reply_message(event.reply_token,
                        TextSendMessage(text= "哈哈，我們繼續~~"))
                elif(msg == '#不是'):
                    Batman.addBlackList()
                    line_bot_api.reply_message(event.reply_token,
                        TextSendMessage(text= "ㄎㄎ，再給我一些提示吧"))
                else:
                    val = Batman.run(msg)

                    if(val[0]==0):
                        print("給歌曲url")
                        message = TemplateSendMessage(
                            alt_text='Carousel template',
                            template=CarouselTemplate(
                                columns=[
                                    CarouselColumn(
                                        #title='this is menu1',
                                        text='歌單',
                                        actions=[
                                            URITemplateAction(
                                                label='推薦歌曲1 (點擊收聽)',
                                                uri='https://www.youtube.com/watch?v=TMB6-YflpA4'
                                            ),
                                            MessageTemplateAction(
                                                label='再玩一次',
                                                text='#再玩一次'
                                            ),
                                            MessageTemplateAction(
                                                label='重選英雄',
                                                text='#重選英雄'
                                            )
                                            
                                        ]
                                    ),
                                    CarouselColumn(
                                        #title='this is menu1',
                                        text='歌單',
                                        actions=[
                                            URITemplateAction(
                                                label='推薦歌曲2 (點擊收聽)',
                                                uri='https://www.youtube.com/watch?v=Bbp9ZaJD_eA'
                                            ),
                                            MessageTemplateAction(
                                                label='再玩一次',
                                                text='#再玩一次'
                                            ),
                                            MessageTemplateAction(
                                                label='重選英雄',
                                                text='#重選英雄'
                                            )
                                            
                                        ]
                                    ),
                                    CarouselColumn(
                                        #title='this is menu1',
                                        text='歌單',
                                        actions=[
                                            URITemplateAction(
                                                label='推薦歌曲3 (點擊收聽)',
                                                uri='https://www.youtube.com/watch?v=xWzlwGVQ6_Q'
                                            ),
                                            MessageTemplateAction(
                                                label='再玩一次',
                                                text='#再玩一次'
                                            ),
                                            MessageTemplateAction(
                                                label='重選英雄',
                                                text='#重選英雄'
                                            )
                                            
                                        ]
                                    )
                                ]
                            )
                        )
                        line_bot_api.reply_message(event.reply_token, message)
                    elif(val[0]==10):
                        line_bot_api.reply_message(event.reply_token,
                            TextSendMessage(text= val[1]))
                    elif(val[0]==1):
                        print("回應lys")
                        line_bot_api.reply_message(event.reply_token,
                            TextSendMessage(text= val[1]))
                    elif(val[0]==2):
                        print("要更多提示")
                        line_bot_api.reply_message(event.reply_token,
                            TextSendMessage(text= val[1]))
                    else:
                        message = TemplateSendMessage(
                            alt_text='Confirm template',
                            template=ConfirmTemplate(
                                text=val[1],
                                actions=[
                                    MessageTemplateAction(
                                        label='是',
                                        text='#是'
                                    ),
                                    MessageTemplateAction(
                                        label='不是',
                                        text='#不是'
                                    )
                                ]
                            )
                        )
                        line_bot_api.reply_message(event.reply_token, message)        
            elif(superhero=='spiderman'):
                if(msg=="#再玩一次"):
                    Spiderman.Reset()
                    line_bot_api.reply_message(event.reply_token,
                        TextSendMessage(text= "猜歌詞遊戲，重新開始!!"))
                if(msg == '#是'):
                    Spiderman.addWhiteList()
                    line_bot_api.reply_message(event.reply_token,
                        TextSendMessage(text= "哈哈，我們繼續~~"))
                elif(msg == '#不是'):
                    Spiderman.addBlackList()
                    line_bot_api.reply_message(event.reply_token,
                        TextSendMessage(text= "ㄎㄎ，再給我一些提示吧"))
                else:
                    val = Spiderman.run(msg)

                    if(val[0]==0):
                        print("給歌曲url")
                        message = TemplateSendMessage(
                            alt_text='Carousel template',
                            template=CarouselTemplate(
                                columns=[
                                    CarouselColumn(
                                        #title='this is menu1',
                                        text='歌單',
                                        actions=[
                                            URITemplateAction(
                                                label='推薦歌曲1 (點擊收聽)',
                                                uri='https://www.youtube.com/watch?v=TMB6-YflpA4'
                                            ),
                                            MessageTemplateAction(
                                                label='再玩一次',
                                                text='#再玩一次'
                                            ),
                                            MessageTemplateAction(
                                                label='重選英雄',
                                                text='#重選英雄'
                                            )
                                            
                                        ]
                                    ),
                                    CarouselColumn(
                                        #title='this is menu1',
                                        text='歌單',
                                        actions=[
                                            URITemplateAction(
                                                label='推薦歌曲2 (點擊收聽)',
                                                uri='https://www.youtube.com/watch?v=Bbp9ZaJD_eA'
                                            ),
                                            MessageTemplateAction(
                                                label='再玩一次',
                                                text='#再玩一次'
                                            ),
                                            MessageTemplateAction(
                                                label='重選英雄',
                                                text='#重選英雄'
                                            )
                                            
                                        ]
                                    ),
                                    CarouselColumn(
                                        #title='this is menu1',
                                        text='歌單',
                                        actions=[
                                            URITemplateAction(
                                                label='推薦歌曲3 (點擊收聽)',
                                                uri='https://www.youtube.com/watch?v=xWzlwGVQ6_Q'
                                            ),
                                            MessageTemplateAction(
                                                label='再玩一次',
                                                text='#再玩一次'
                                            ),
                                            MessageTemplateAction(
                                                label='重選英雄',
                                                text='#重選英雄'
                                            )
                                            
                                        ]
                                    )
                                ]
                            )
                        )
                        line_bot_api.reply_message(event.reply_token, message)
                    elif(val[0]==10):
                        line_bot_api.reply_message(event.reply_token,
                            TextSendMessage(text= val[1]))
                    elif(val[0]==1):
                        print("回應lys")
                        line_bot_api.reply_message(event.reply_token,
                            TextSendMessage(text= val[1]))
                    elif(val[0]==2):
                        print("要更多提示")
                        line_bot_api.reply_message(event.reply_token,
                            TextSendMessage(text= val[1]))
                    else:
                        message = TemplateSendMessage(
                            alt_text='Confirm template',
                            template=ConfirmTemplate(
                                text=val[1],
                                actions=[
                                    MessageTemplateAction(
                                        label='是',
                                        text='#是'
                                    ),
                                    MessageTemplateAction(
                                        label='不是',
                                        text='#不是'
                                    )
                                ]
                            )
                        )
                        line_bot_api.reply_message(event.reply_token, message)        
            

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    Batman = batman_class.Hero("batman")
    Spiderman = spiderman_class.Hero("spiderman")
    

    superhero = 'init'
    # init -> 初始狀態
    # batman -> 蝙蝠俠
    # spiderman -> 蜘蛛人

    appmodel = 0
    # 0 -> 初始狀態
    # 1 -> 猜歌詞遊戲
    # 2 -> 生成對話遊戲
    # 3 -> 對話閒聊
    app.run(host='0.0.0.0', port=port)