‎mport os
‎import telebot
‎import google.generativeai as genai
‎
‎၁။ လျှို့ဝှက်ကီးများ (Secrets) ကို ပြန်ခေါ်ယူခြင်း
‎TELEGRAM_TOKEN = os.environ.get("8960371678:AAHRMLQ2U7wmwMwEBJV9b6iH3Ji5-uR3ptA")
‎GEMINI_API_KEY = os.environ.get("AQ.Ab8RN6IV-8LOPHUBHyFr8Z5a8Gj1Wii4ZydvvlABQ7-j-n7BKQ")
‎
‎၂။ Gemini AI ကို ချိတ်ဆက်ခြင်း
‎genai.configure(api_key=AQ.Ab8RN6IV-8LOPHUBHyFr8Z5a8Gj1Wii4ZydvvlABQ7-j-n7BKQ)
‎model = genai.GenerativeModel('gemini-1.5-pro')
‎
‎၃။ Telegram Bot ကို တည်ဆောက်ခြင်း
‎bot = telebot.TeleBot(8960371678:AAHRMLQ2U7wmwMwEBJV9b6iH3Ji5-uR3ptA)
‎
‎၄။ /start ဟု နှိပ်လိုက်လျှင် Bot မှ ပြန်လည်နှုတ်ဆက်မည့် စာ
‎@bot.message_handler(commands=['start', 'help'])
‎def send_welcome(message):
‎    welcome_text = (
‎        "🎬 မင်္ဂလာပါ! ကျွန်တော်ကတော့ Movie Recap ဇာတ်ညွှန်းတွေကို အလိုအလျောက်ရေးပေးမယ့် AI Bot လေးပါ။\n\n"
‎        "ရုပ်ရှင်နာမည် ဒါမှမဟုတ် ဇာတ်လမ်းအကျဉ်းကို စာနဲ့ ရိုက်ပို့ပေးလိုက်ပါ။ ချက်ချင်း ဇာတ်ညွှန်းရေးပေးပါမယ်။\n"
‎        "(ဗီဒီယိုဖိုင် တိုက်ရိုက်လက်ခံနိုင်ဖို့ကိုတော့ အခုမှ ဆက်ပြီး တည်ဆောက်နေဆဲ ဖြစ်ပါတယ်။)"
‎    )
‎    bot.reply_to(message, welcome_text)
‎
‎၅။ စာသားရောက်လာလျှင် Gemini သို့ပို့၍ ဇာတ်ညွှန်းရေးခိုင်းခြင်း
‎@bot.message_handler(func=lambda message: True)
‎def handle_message(message):
‎စောင့်ခိုင်းသည့် စာအရင်ပို့ထားခြင်း
‎    bot.reply_to(message, "⏳ ဇာတ်ညွှန်း စတင်ရေးဆွဲနေပါပြီ... ခဏလေး စောင့်ပေးပါဗျာ။")
‎
‎    try:
‎Gemini သို့ ပို့မည့် အမိန့် (Prompt)
‎        prompt = f"""
‎        You are an expert YouTube scriptwriter specializing in "Movie Recap" videos. 
‎        Please write an engaging YouTube movie recap script for this movie/plot: "{message.text}".
‎        Write the script fully in Burmese (မြန်မာဘာသာဖြင့်သာ ရေးပေးပါ).
‎        Make it sound natural and exciting.
‎        """
‎
‎AI မှ အဖြေတောင်းခြင်း
‎        response = model.generate_content(prompt)
‎
‎ရလာသော ဇာတ်ညွှန်းကို Telegram သို့ ပြန်ပို့ခြင်း
‎        bot.reply_to(message, response.text)
‎
‎    except Exception as e:
‎        bot.reply_to(message, f"❌ အမှားအယွင်းဖြစ်သွားပါသည်: {e}")
‎
‎၆။ Bot ကို အမြဲတမ်း နားစွင့်နေစေရန် Run ထားခြင်း
‎print("Bot စတင် အလုပ်လုပ်နေပါပြီ...")
‎bot.polling(none_stop=True)
‎
