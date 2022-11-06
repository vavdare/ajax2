
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import json

bot = telebot.TeleBot('5480602651:AAGvewdneoSnj2UcHB3u1lhYvIe1YRanoNM')

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name


def get_prices():
    coins = ["BTC", "ETH", "BNB", "XRP", "ADA", "DOT", "LINK",  "SOL", "AAVE"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD".format(",".join(coins))).json()["RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "TotalSupply": crypto_data[i]["USD"]["SUPPLY"],
            "MarketCap": crypto_data[i]["USD"]["MKTCAP"],
            "Highday": crypto_data[i]["USD"]["HIGHDAY"],
            "Lowday": crypto_data[i]["USD"]["LOWDAY"],
            "Market": crypto_data[i]["USD"]["LASTMARKET"],
            "TotalVolume": crypto_data[i]["USD"]["TOTALVOLUME24HTO"]
 
            
 
        }

    return data
      
if __name__ == "__main__":
    print(get_prices())  
    
    

url2 = "https://deep-index.moralis.io/api/v2/erc20/0x2c24Ca4375c9912F4004317b8aA23576730c77AF/price?chain=bsc"
headers =  {
    "Accept": "application/json",
    "X-API-Key": "mPh1GgKt6FGABAPsMRHYwvhckITKChDsiyBqvZE0IYTfLjfBgxspoGJriqfMAOfm"
}
       
response2 = requests.get(url2, headers=headers)
resp = response2.json()
print(resp)

key = "https://api.binance.com/api/v3/ticker/price?symbol={message.text}USDT"
data2 = requests.get(key)
data22 = data2.json()
 

def keyboard(key_type="start"):
    markup = ReplyKeyboardMarkup(True) 
    if key_type == "start":
        markup.add(KeyboardButton('English'),KeyboardButton('Farsi'))
    elif key_type == "Farsi":
        markup.add(KeyboardButton("قیمت ارز آژاکس"),KeyboardButton("آدرس کانترکت ارز آژاکس"))
        markup.add(KeyboardButton("پشتیبانی"),KeyboardButton("آموزش ارز دیجیتال"),KeyboardButton("کانال اخبار آژاکس"),KeyboardButton("قیمت ارزهای برتر بازار"),KeyboardButton('سایت رسمی ارز آژاکس'))
         
    elif key_type == "آموزش ارز دیجیتال":
        markup.add(KeyboardButton('۲. ثبت نام در سایت آژاکس'),KeyboardButton('۱. وایت پیپر ارز آژاکس'))
        markup.add(KeyboardButton('۴. تکمیل اطلاعات ثبت نام در سایت'),KeyboardButton('۳. دریافت لینک معرفی و ارسال آن'))
        markup.add(KeyboardButton('۶. اضافه کردن توکن آژاکس در پنکیک سوآپ (اندروید)'),KeyboardButton('۵. اضافه کردن توکن آژاکس به تراست والت(اندروید)'))
        markup.add(KeyboardButton('۸. اضافه کردن ارز آژاکس به متامسک'),KeyboardButton('۷. اتصال پنکیک سواپ به تراست والت'))
        markup.add(KeyboardButton("۱۰. برداشت از سایت و انتقال آن به کیف پول"),KeyboardButton('۹. اضافه کردن اسمارت چین و پنکیک سوآپ به متامسک'))
        markup.add(KeyboardButton('بازگشت به منو'))
    elif key_type == 'قیمت ارز آژاکس':
    	markup.add(KeyboardButton('bscscan'))
    	markup.add(KeyboardButton('نمودار چارت آژاکس'))
    	markup.add(KeyboardButton('قیمت ارز دلخواه شما در صرافی بایینس'))
    	markup.add(KeyboardButton('بازگشت به منو'))
    elif key_type == "English":
    	markup.add(KeyboardButton("Ajax Token Price"),KeyboardButton("Ajax Token Contract"))
    	markup.add(KeyboardButton('Support'),KeyboardButton('Learning about Ajax'),KeyboardButton('Ajax channel'),KeyboardButton('Top Crypto price'),KeyboardButton('Ajax Website'))
    elif key_type == 'Ajax Token Price':
        markup.add(KeyboardButton('bscscan'))
        markup.add(KeyboardButton('Price candle chart'))
        markup.add(KeyboardButton('Binance realtime price'))
        markup.add(KeyboardButton('Back to Menu'))
    elif key_type == 'Learning about Ajax':
        markup.add(KeyboardButton('1.Ajax White paper'),KeyboardButton('2.Signup in Ajax Website'))
        markup.add(KeyboardButton('3.How to Get Referral Link & send it'),KeyboardButton('4.Complete Signup'))
        markup.add(KeyboardButton('5.Add Ajax token to Trustwallet(android)'),KeyboardButton('6.Add Ajax token to Pancakeswap(android)'))
        markup.add(KeyboardButton('7.Connecting Pancakeswap to Trustwallet'),KeyboardButton('8.Add Ajax token to Metamask'))
        markup.add(KeyboardButton('9.Add Smartchain & Pancakeswap to Metamask'),KeyboardButton('10.Withdraw & transfering to Wallet from Website'))
        markup.add(KeyboardButton('Back to Menu')) 
    return markup	      	
    

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,'Welcome to Ajax Foundation bot, Please chose your language :\n\nسلام به ربات آژاکس خوش آمدید. لطفا زبان خود را انتخاب کنید :\n Farsi=فارسی',reply_markup=keyboard())
    
@bot.message_handler(commands=["Farsi"])
def Farsi_message(message):
    bot.send_message(message.chat.id,"سلام به ربات آژاکس خوش آمدید. لطفا انتخاب کنید ::",reply_markup=keyboard('Farsi'))
    
@bot.message_handler(commands=["English"])
def English_message(message):
    bot.send_message(message.chat.id,'Welcome to Ajax Foundation bot, Please chose :',reply_markup=keyboard('English'))
    
    

@bot.message_handler(func=lambda message:True)
def all_messages(message):
    if message.text == "پشتیبانی":
        bot.send_message(message.chat.id,"@Pedro7091\n\n @Mostafa_627",reply_markup=keyboard("پشتیبانی"))
    elif message.text == "Support":
        bot.send_message(message.chat.id,"@Pedro7091\n\n @Mostafa_627",reply_markup=keyboard("Support"))
    elif message.text == "Farsi":
        bot.send_message(message.chat.id," لطفا انتخاب کنید",reply_markup=keyboard('Farsi'))
    elif message.text == "English":
        bot.send_message(message.chat.id,'Please chose',reply_markup=keyboard('English'))
    elif message.text == "آموزش ارز دیجیتال":
        bot.send_message(message.chat.id,"لطفا ویدئو مورد نظر را انتخاب کنید ::",reply_markup=keyboard("آموزش ارز دیجیتال"))
    elif message.text == "Learning about Ajax":
        bot.send_message(message.chat.id,"Please chose the Video :",reply_markup=keyboard("Learning about Ajax"))
    
    elif message.text == "سایت رسمی ارز آژاکس":
        bot.send_message(message.chat.id," https://Ajax.foundation",reply_markup=keyboard('سایت رسمی ارز آژاکس'))
    elif message.text == "Ajax Website":
        bot.send_message(message.chat.id," https://Ajax.foundation",reply_markup=keyboard('Ajax Website'))
        
    elif message.text == "آدرس کانترکت ارز آژاکس":
        bot.send_message(message.chat.id,"0x31a423c56715C8074Df3a29A25F6BD3385A91D61",reply_markup=keyboard("آدرس کانترکت ارز آژاکس"))
    elif message.text == "Ajax Token Contract":
        bot.send_message(message.chat.id,"0x31a423c56715C8074Df3a29A25F6BD3385A91D61",reply_markup=keyboard("Ajax Token Contract"))
    
    elif message.text == "کانال اخبار آژاکس":
        bot.send_message(message.chat.id,"کانال فارسی : https://t.me/AJAXFoundationChannel_fa\n\nکانال انگلیسی  : https://t.me/AjaxFoundationChannel",reply_markup=keyboard("کانال اخبار آژاکس"))

    elif message.text == "Ajax channel":
        bot.send_message(message.chat.id,"  : https://t.me/AJAXFoundationChannel_fa Farsi Channel\n\n   : https://t.me/AjaxFoundationChannel English Channel",reply_markup=keyboard("Ajax channel"))
    
    elif message.text == "۱. وایت پیپر ارز آژاکس":
      
        video = open('/tmp/white1.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    elif message.text == "1.Ajax White paper":
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)   
    elif message.text == '2.Signup in Ajax Website':
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    elif message.text == '3.How to Get Referral Link & send it':
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    elif message.text == '4.Complete Signup':
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    elif message.text == '5.Add Ajax token to Trustwallet(android)':
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    elif message.text == '6.Add Ajax token to Pancakeswap(android)':
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    elif message.text == '7.Connecting Pancakeswap to Trustwallet':
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    elif message.text == '8.Add Ajax token to Metamask':
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    elif message.text == '9.Add Smartchain & Pancakeswap to Metamask':
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    elif message.text == '10.Withdraw & transfering to Wallet from Website':
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    elif message.text == "۲. ثبت نام در سایت آژاکس":
      
        video = open('/tmp/signup2.mp4', 'rb')
        bot.send_video(message.chat.id,video)
        
    elif message.text == "۳. دریافت لینک معرفی و ارسال آن":
      
        video = open('/tmp/referlink3.mp4', 'rb')
        bot.send_video(message.chat.id,video)
        
    elif message.text == "۴. تکمیل اطلاعات ثبت نام در سایت":
      
        video = open('/tmp/infoajax4.mp4', 'rb')
        bot.send_video(message.chat.id,video)
    
    elif message.text == "۵. اضافه کردن توکن آژاکس به تراست والت(اندروید)":
      
        video = open('/tmp/ajaxtotrust5.mp4', 'rb')
        bot.send_video(message.chat.id,video)
   
    elif message.text == "۶. اضافه کردن توکن آژاکس در پنکیک سوآپ (اندروید)":
      
        video = open('/tmp/referlink3.mp4', 'rb')
        bot.send_video(message.chat.id,video)      
     
     
    elif message.text == " ۷.  اتصال پنکیک سواپ به تراست والت":
      
        video = open('/tmp/pantotrust7.mp4', 'rb')
        bot.send_video(message.chat.id,video)
     
    elif message.text == "۸. اضافه کردن ارز آژاکس به متامسک":
      
        video = open('/tmp/referlink3.mp4', 'rb')
        bot.send_video(message.chat.id,video)                                                                 
    elif message.text == "۹. اضافه کردن اسمارت چین و پنکیک سوآپ به متامسک":
      
        video = open('/tmp/addSpancaketometa9.mp4', 'rb')
        bot.send_video(message.chat.id,video)
   
    elif message.text == "۱۰. برداشت از سایت و انتقال آن به کیف پول":
      
        video = open('/tmp/withdraw10.mp4', 'rb')
        bot.send_video(message.chat.id,video)   
                                                                
    elif message.text == "قیمت ارزهای برتر بازار":
     crypto_data = get_prices()
     for i in crypto_data:
       coin=crypto_data[i]["coin"]
       price=crypto_data[i]["price"]
       MarketCap=crypto_data[i]["MarketCap"]
       Highday=crypto_data[i]["Highday"]
       Lowday=crypto_data[i]["Lowday"]
       TotalSupply=crypto_data[i]["TotalSupply"]
       Volume24H=crypto_data[i]["TotalVolume"]
       message2=f" {coin} = {price:,}\n\nبالاترین قیمت روز = {Highday:,}\nپایین ترین قیمت روز = {Lowday:,}\nحجم معاملات امروز = {Volume24H:,}\nمارکت کپ = {MarketCap:,}\nتعداد کل ارز = {TotalSupply:,}\n\n"
       bot.send_message(message.chat.id,message2,reply_markup=keyboard("قیمت ارزهای برتر بازار"))

    elif message.text == "قیمت ارز آژاکس":
        price = resp['nativePrice']['value']
        priceUSD = resp['usdPrice']
        message3 = f"قیمت : {priceUSD:.6f}  USD\n\n تعداد کل ارز : 1,900,000,000,000\n\n PancakeSwap V2"
        bot.send_message(message.chat.id,message3,reply_markup=keyboard("قیمت ارز آژاکس"))
    
    elif message.text == "Top Crypto price":
     crypto_data = get_prices()
     for i in crypto_data:
       coin=crypto_data[i]["coin"]
       price=crypto_data[i]["price"]
       MarketCap=crypto_data[i]["MarketCap"]
       Highday=crypto_data[i]["Highday"]
       Lowday=crypto_data[i]["Lowday"]
       TotalSupply=crypto_data[i]["TotalSupply"]
       Volume24H=crypto_data[i]["TotalVolume"]
       message2=f" {coin} = {price:,}\n\nHighest price of day = {Highday:,}\nLowest price of day = {Lowday:,}\nVolume 24H  = {Volume24H:,}\nMarketCap = {MarketCap:,}\nTotal supply  = {TotalSupply:,}\n\n"
       bot.send_message(message.chat.id,message2,reply_markup=keyboard("Top Crypto price"))

    elif message.text == "Ajax Token Price":
        price = resp['nativePrice']['value']
        priceUSD = resp['usdPrice']
        message3 = f"Price : {priceUSD:.6f}  USD\n\n Total supply : 1,900,000,000,000\n\n PancakeSwap V2"
        bot.send_message(message.chat.id,message3,reply_markup=keyboard("Ajax Token Price"))
    elif message.text  == 'بازگشت به منو':
    	bot.send_message(message.chat.id,"/Farsi",reply_markup=keyboard('Farsi'))
    elif message.text  == 'Back to Menu':
    	bot.send_message(message.chat.id,"/English",reply_markup=keyboard('English'))	
    elif message.text =='bscscan':
    	bot.send_message(message.chat.id,'https://bscscan.com/token/0x2c24Ca4375c9912F4004317b8aA23576730c77AF')
    
    elif message.text =='نمودار چارت آژاکس':
    	bot.send_message(message.chat.id,"برای نمایش سایت لطفا فیلترشکن خود را خاموش کنید")
    	bot.send_message(message.chat.id,'https://poocoin.app/tokens/0x2c24ca4375c9912f4004317b8aa23576730c77af') 	
    elif message.text =='Price candle chart':
    	bot.send_message(message.chat.id,'https://poocoin.app/tokens/0x2c24ca4375c9912f4004317b8aa23576730c77af') 	
    while message.text == 'Binance realtime price':
        msg = bot.reply_to(message, """\
what is your Symbol ? like BTC,ETH,ADA'
\nIf you want chose another symbol,go to menu and chose again""")
        bot.register_next_step_handler(msg, process_name_step)
        break
    while message.text == 'قیمت ارز دلخواه شما در صرافی بایینس':
    	 msg2 = bot.reply_to(message,"نام ارز مورد نظر خود را وارد کنید :\nمثال : BTC,ETH,ADA\nو برای انتخاب دوباره بر روی منو کلیک کنید")
    	 bot.register_next_step_handler(msg2,process_name_step2)
    	 break
def process_name_step(message):
 chat_id = message.chat.id
 name = message.text.upper()
 user = User(name)
 user_dict[chat_id] = user
 message6= "https://api.binance.com/api/v3/ticker/price?symbol="+user.name+"USDT"
 data2 = requests.get(message6)
 data22 = data2.json()
 message5=f"{data22['symbol']} price is {data22['price']}"
 print(message5)
 bot.send_message(message.chat.id,message5)
def process_name_step2(message):
    
        chat_id = message.chat.id
        name = message.text.upper()
        user = User(name)
        user_dict[chat_id] = user

        bot.send_message(chat_id, 'ارز شما = ' + user.name +"USDT" )
        message7= "https://api.binance.com/api/v3/ticker/price?symbol="+user.name+"USDT"
        data2 = requests.get(message7)
        data22 = data2.json()
        message8=f"{data22['symbol']} : {data22['price']}"
        print(message8)
        bot.send_message(message.chat.id,message8)        
 
bot.infinity_polling()

