import streamlit as st

st.set_page_config(page_title="Guri's Chatbot", page_icon="🤖")

st.title("🤖 Guri's Chatbot")
st.write("Welcome! Ask me anything.")

qa = {

# Greetings
"hi":"Hi! Welcome to Guri's Chatbot 😊",
"hii":"Hi! Welcome to Guri's Chatbot 😊",
"hello":"Hello! Welcome to Guri's Chatbot 😊",
"hlo":"Hello! Welcome to Guri's Chatbot 😊",
"hey":"Hey! Welcome 😊",
# Punjabi Daily Conversation

"hor":"Hor dasso ji 😊",
"hor ki haal":"Sab vadhiya. Tusi sunao?",
"kive":"Main vadhiya haan. Tusi kive ho?",
"kive aa":"Main theek haan 😊",
"kive ho":"Main vadhiya haan. Tusi dasso?",
"kive ho ji":"Main theek haan ji. Tusi sunao?",
"ki haal":"Main theek haan. Tuhada ki haal aa?",
"ki haal aa":"Sab changa. Tusi sunao?",
"ki chal reha":"Bas vadhiya ji. Tusi dasso?",
"ki kr rhe ho":"Main tuhade naal gall kar reha haan 😊",
"ki kar rahe ho":"Main tuhade questions de answer de reha haan.",
"ki karde ho":"Main chatbot haan. Main help karda haan.",
"tusi dsso":"Main vadhiya haan ji 😊",
"tusi dasso":"Main theek haan. Tusi hor pucho.",
"tusi kive ho":"Main bilkul theek haan 😊",
"main vadhiya haan":"Eh sun ke khushi hoi 😊",
"main theek haan":"Bahut vadhiya 😊",
"main vadiya":"Great 😊",
"main bore ho reha":"Chalo gallan karde haan 😄",
"main free haan":"Vadhiya! Hor kujh pucho.",
"main busy haan":"Koi gall nahi. Jadon free hovo fir gall karange.",
"ki karna":"Jo vi help chahidi hove pucho.",
"ki hoya":"Kujh nahi ji. Sab theek aa 😊",
"tusi ki karde ho":"Main chatbot haan. Questions de answer denda haan.",
"ki khabar":"Sab changa ji 😊",
"ajj ki haal":"Ajj vi sab vadhiya.",
"ki scene aa":"Sab set aa 😎",
"scene ki aa":"Kujh khas nahi. Tusi dasso.",
"changa":"Theek aa ji 😊",
"theek aa":"Vadhiya 😊",
"acha":"Haan ji 😊",
"achha":"Ji 😊",
"wah":"Shukriya 😊",
"vadiya":"Thank you 😊",
"sira":"Haha 😄 Shukriya!",
"att":"Thank you ji 😄",
"love you":"Love you too as a friend 😊",
"miss you":"Main hamesha ithe haan jadon tusi chat karna chaunde ho.",
"main udaas haan":"Udaas na hovo. Sab theek ho jauega ❤️",
"main khush haan":"Eh sun ke bahut khushi hoi 😊",
"mera naam guri aa":"Nice to meet you Guri! 😊",
"mera naam":"Nice to meet you 😊",
"tu kon aa":"Main Guri's Chatbot haan.",
"tusi kon ho":"Main Guri's Chatbot haan.",
"thanku":"You're welcome 😊",
"shukriya":"Koi gall nahi ji 😊",
"dhannwad":"Ji Aayan Nu 😊",
"chal bye":"Bye ji! Rab Rakha 👋",
"bye bye":"Rab Rakha 😊",
"fir milange":"Jarur! Fir milange 😊"
# Coding & Programming
"what is coding":"Coding is the process of writing instructions for computers.",
"what is programming":"Programming means creating software using programming languages.",
"why learn python":"Python is easy to learn and widely used in AI and web development.",
"what is php":"PHP is a server-side scripting language for web development.",
"what is mysql":"MySQL is a database management system.",
"what is sql":"SQL is used to manage databases.",
"what is api":"API allows two applications to communicate with each other.",
"what is github":"GitHub is a platform to host and manage code.",
"what is streamlit":"Streamlit is a Python framework for building web apps.",
"what is chatbot":"A chatbot is a program that talks with users.",

# AI
"what is chatgpt":"ChatGPT is an AI chatbot developed by OpenAI.",
"can ai replace humans":"AI can assist humans but cannot replace human creativity completely.",
"what is machine learning":"Machine Learning allows computers to learn from data.",
"what is deep learning":"Deep Learning is an advanced branch of AI.",
"what is prompt":"A prompt is the instruction you give to an AI.",

# Education
"why study":"Education helps you build knowledge and skills.",
"how to score good marks":"Study regularly and practice daily.",
"how to focus":"Avoid distractions and make a study timetable.",
"best career":"Choose a career based on your interest and skills.",
"how to become successful":"Work hard, stay consistent and never give up.",

# Mathematics
"2+2":"2 + 2 = 4",
"5+5":"5 + 5 = 10",
"10+10":"10 + 10 = 20",
"100-50":"100 - 50 = 50",
"10*10":"10 × 10 = 100",
"20/5":"20 ÷ 5 = 4",

# Internet
"what is wifi":"Wi-Fi is a wireless network technology.",
"what is bluetooth":"Bluetooth is used to connect nearby devices wirelessly.",
"what is vpn":"VPN helps protect your privacy online.",
"what is domain":"A domain is the address of a website.",
"what is hosting":"Hosting stores website files on a server.",

# Mobile
"android":"Android is a mobile operating system.",
"iphone":"iPhone is a smartphone made by Apple.",
"play store":"Play Store is used to download Android apps.",
"app":"An app is a software application.",
"update":"Updating apps adds new features and fixes bugs.",

# Daily Conversation
"how can i improve myself":"Learn something new every day and stay consistent.",
"i am learning":"That's great! Keep going.",
"i am confused":"Take one step at a time. You'll figure it out.",
"i need advice":"Stay focused on your goals and don't give up.",
"good":"Nice 😊",
"very good":"Awesome 😊",
"excellent":"Excellent! Keep it up.",
"amazing":"That's amazing!",
"wow":"😊 Glad you liked it.",
"cool":"Cool! 😎",
"haha":"😂",
"lol":"😂 That's funny.",
"are you intelligent":"I try my best to answer correctly.",
"can you think":"I generate responses based on what I have learned.",
"who made you":"Guri created this chatbot using Streamlit.",
"what is your purpose":"My purpose is to help and chat with you.",
"can you solve problems":"Yes, I'll try my best.",
"do you know coding":"Yes! I can help with coding questions.",
"can you teach python":"Yes! I can help you learn Python.",
"thank you so much":"You're most welcome 😊",
"bye":"Goodbye! Have a wonderful day. 👋",

# Punjabi
"tusi vadhiya ho":"Shukriya ji 😊",
"main coding kar reha haan":"Bahut vadhiya! Practice karde raho.",
"main python sikh reha haan":"Excellent! Python ik bahut powerful language hai.",
"main website bana reha haan":"Awesome! Best of luck with your project.",
"ki tusi meri madad kar sakde ho":"Haan ji! Zaroor. Apna question pucho.",
"fir milange":"Rab Rakha Ji. Fir milange 😊",
"chalo bye":"Bye ji! Take care.",
"sat sri akal ji":"Sat Sri Akal Ji 🙏",
"dhannwad":"Ji Aayan Nu 😊",
"rab rakha":"Rab Rakha Ji 🙏"
# HTML
"html":"HTML stands for HyperText Markup Language.",
"what is html":"HTML is used to create web pages.",
"who invented html":"HTML was invented by Tim Berners-Lee.",
"html full form":"HyperText Markup Language.",
"html tags":"HTML uses tags to structure web pages.",
"html uses":"HTML is used for creating websites.",

# CSS
"css":"CSS stands for Cascading Style Sheets.",
"what is css":"CSS is used to design web pages.",
"css full form":"Cascading Style Sheets.",
"why use css":"CSS makes websites beautiful and responsive.",
"css selectors":"Selectors are used to target HTML elements.",
"responsive design":"Responsive design makes websites work on all devices.",

# JavaScript
"javascript":"JavaScript is a scripting language.",
"what is javascript":"JavaScript makes websites interactive.",
"js full form":"JavaScript has no official full form. JS is its short name.",
"what can javascript do":"JavaScript can create dynamic web pages.",
"alert":"alert() displays a popup message.",
"console log":"console.log() prints messages in the browser console.",

# Python
"python":"Python is a popular programming language.",
"python full form":"Python has no full form.",
"who created python":"Python was created by Guido van Rossum.",
"python uses":"Python is used for AI, web development, automation and data science.",
"is python easy":"Yes, Python is beginner friendly.",
"python vs c":"Python is easier, C is faster.",

# C Language
"what is c":"C is a powerful programming language.",
"c language":"C is one of the oldest programming languages.",
"who invented c":"Dennis Ritchie invented C.",
"c uses":"C is used for system programming.",
"c full form":"C has no full form.",

# C++
"what is c++":"C++ is an object-oriented programming language.",
"who invented c++":"Bjarne Stroustrup invented C++.",
"c++ uses":"C++ is used in games and software development.",
"c++ full form":"C++ has no full form.",

# Java
"what is java":"Java is an object-oriented programming language.",
"java full form":"Java has no full form.",
"who invented java":"James Gosling created Java.",
"java uses":"Java is used for Android apps and enterprise software.",

# PHP
"what is php":"PHP is a server-side scripting language.",
"php full form":"PHP: Hypertext Preprocessor.",
"php uses":"PHP is mainly used for web development.",
"laravel":"Laravel is a PHP framework.",

# AI
"what is ai":"AI means Artificial Intelligence.",
"artificial intelligence":"AI enables machines to think and learn.",
"chatgpt":"ChatGPT is an AI chatbot.",
"machine learning":"Machine Learning is a branch of AI.",
"deep learning":"Deep Learning uses neural networks.",

# Education
"why should i learn coding":"Coding helps build apps, websites and software.",
"best programming language":"Python is a great choice for beginners.",
"how to become programmer":"Practice coding daily and build projects.",
"how to learn coding":"Start with HTML, CSS and Python.",
"what is web development":"Web development means creating websites.",

# Daily Conversation
"what are you doing":"I am waiting for your next question.",
"i love coding":"That's awesome! Keep learning.",
"i am learning python":"Excellent! Practice every day.",
"i am beginner":"No problem. Everyone starts as a beginner.",
"good bye":"Goodbye! Take care.",
"see you":"See you again! Have a nice day.",
"have a nice day":"Thank you! You too.",
"good luck":"Thank you 😊",
"who is guri":"Guri is my creator.",
"do you know punjabi":"Yes! I can understand Punjabi written in English.",
"do you know english":"Yes! I understand English very well.",
"i need help":"Sure! Tell me your question.",
"help":"I'm here to help you.",
"what is your hobby":"I like chatting with people.",
"are you smart":"I try my best to answer correctly.",
"who is your friend":"Everyone who chats with me is my friend.",
"can we be friends":"Of course! 😊",
"i am tired":"Take some rest and drink water.",
"i am busy":"No worries. Come back anytime.",
"love you":"Thank you! 😊"

# English Conversation
"how are you":"I am fine. Thank you! How are you?",
"what is your name":"My name is Guri's Chatbot.",
"who are you":"I am Guri's Chatbot. I am here to help you.",
"good morning":"Good Morning! Have a wonderful day.",
"good afternoon":"Good Afternoon!",
"good evening":"Good Evening!",
"good night":"Good Night! Sweet dreams.",
"bye":"Goodbye! Have a nice day.",
"thanks":"You're welcome 😊",
"thank you":"You're welcome 😊",

# Punjabi Conversation
"kive ho":"Main vadhiya haan. Tusi sunao?",
"ki haal aa":"Main theek haan. Tuhada ki haal aa?",
"theek ho":"Haan ji, main theek haan.",
"tusi kon ho":"Main Guri's Chatbot haan.",
"ki kar rahe ho":"Main tuhade questions de answer de reha haan.",
"sat sri akal":"Sat Sri Akal Ji 🙏",
"shukriya":"Koi gall nahi 😊",
"rab rakha":"Rab Rakha Ji 🙏",
# English Conversation
"how old are you":"I don't have an age. I am a chatbot.",
"where are you from":"I live on the internet.",
"can you help me":"Yes! I will try my best to help you.",
"what can you do":"I can answer your questions and chat with you.",
"are you a robot":"Yes, I am a virtual chatbot.",
"do you like coding":"Yes! Coding is amazing.",
"what is your favourite language":"I like Python because it is easy.",
"are you real":"No, I am a virtual assistant.",
"who created you":"I was created by Guri.",
"nice":"Thank you 😊",
"awesome":"Glad you liked it!",
"good":"That's great!",
"ok":"Okay 👍",
"okay":"Okay 😊",
"yes":"Great!",
"no":"No problem.",
"tell me a joke":"Why do programmers prefer dark mode? Because light attracts bugs. 😂",
"i am happy":"That's wonderful! 😊",
"i am sad":"Don't worry. Better days are coming.",
"good job":"Thank you so much!",

# Punjabi Conversation
"tuhada naam ki aa":"Mera naam Guri's Chatbot hai.",
"tusi ki karde ho":"Main tuhade questions de jawab denda haan.",
"main theek haan":"Eh sun ke khushi hoi 😊",
"mera naam guri aa":"Nice to meet you Guri!",
"tuhada favourite colour":"Mainu saare colours pasand ne.",
"ki tusi punjabi samajhde ho":"Haan ji, main Punjabi samajhda haan.",
"ki tusi english samajhde ho":"Yes, I understand English.",
"ki tusi hindi samajhde ho":"Haan ji, thodi bahut Hindi vi samajhda haan.",
"tusi kithe rehnde ho":"Main internet te rehnda haan.",
"main bore ho reha haan":"Chalo gallan karde haan 😊",
"ki chal reha":"Sab vadhiya! Tusi dasso.",
"ki karna chahida":"Apna goal choose karo te mehnat karo.",
"vadiya":"Bahut vadiya 😊",
"changa":"Shukriya!",
"fir milange":"Jarur! Rab Rakha.",
"main student haan":"Best of luck for your studies.",
"main coding sikhna chaunda haan":"Great! Start with HTML, CSS and Python.",
"main python sikhna chaunda haan":"Python beginners lai bahut easy hai.",
"main web development sikhna chaunda haan":"HTML, CSS, JavaScript te PHP ton start karo.",
"main ai sikhna chaunda haan":"Python + Machine Learning + AI best combination hai.",

# Computer Questions
"what is cpu":"CPU is the brain of a computer.",
"what is ram":"RAM is temporary memory used while programs are running.",
"what is rom":"ROM stores permanent data.",
"what is keyboard":"A keyboard is an input device.",
"what is mouse":"A mouse is a pointing device.",
"what is monitor":"A monitor displays output from the computer.",
"what is printer":"A printer prints documents on paper.",
"what is internet":"The Internet is a global network connecting computers.",
"what is website":"A website is a collection of web pages.",
"what is browser":"A browser is software used to open websites.",
"what is google":"Google is a search engine.",
"what is youtube":"YouTube is a video sharing platform.",
"what is email":"Email is an electronic mail service.",
"what is wifi":"Wi-Fi is wireless internet technology.",
"what is software":"Software is a set of programs.",
"what is hardware":"Hardware means the physical parts of a computer.",
"what is operating system":"An operating system manages computer hardware and software.",
"what is windows":"Windows is an operating system developed by Microsoft.",
"what is android":"Android is a mobile operating system.",
"what is iphone":"iPhone is a smartphone developed by Apple."

# Computer
"what is computer":"A computer is an electronic machine that processes data.",
"computer ki hunda":"Computer ik electronic machine hai jo data process kardi hai.",
"what is python":"Python is an easy and powerful programming language.",
"python ki hunda":"Python ik programming language hai jo beginners lai easy hai.",
"what is html":"HTML is used to create web pages.",
"what is css":"CSS is used to design web pages.",
"what is javascript":"JavaScript adds interactivity to websites.",
"what is ai":"AI means Artificial Intelligence.",
}

question = st.text_input("Ask your question")

if st.button("Send"):
    msg = question.strip().lower()

    if msg in qa:
        st.success(qa[msg])
    else:
        st.warning("Sorry! I don't know the answer yet.")
