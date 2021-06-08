from pymongo import MongoClient
from hashlib import sha256
from Persistence.job import JobObject

dbs = MongoClient("mongodb+srv://Mblanca4:Team2SpringQuarter@team2.14wgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority").myFirstDatabase
candidates = dbs.Candidate
companies = dbs.Company
jobs = dbs.Job

def hash_text(password):
    hashed_text = sha256(password.encode('utf-8')).hexdigest()
    return hashed_text

def add_candidates():
    candidates.insert_many([
        {"password": hash_text("123Puyo!"), "userName": "arleNadja".lower(), "email": "anadja@bayoen.com",
         "phoneNum": "6076226091", "references": "Ringo", "tech_skills": ["c", "HTML", "Cobol", "python"],
         "business_skills": ["problem-solving", "critical-thinking"],
         "attitude": ["enthusiastic", "economics", "cheerful", "innovative", "adaptable"], "bestMatch": [],
         "name": "Arle Nadja"},
         {"password": hash_text("321Tetris!"), "userName": "teeSpin".lower(), "email": "tspin@email.com",
          "phoneNum": "6376224432", "references": "Lemres", "tech_skills": ["Java", "C++", "Lua", "PL/SQL"],
          "business_skills": ["Quickbooks", "customer-service"],
          "attitude": ["determined", "responsible", "innovative"], "bestMatch": [], "name": "Tee Tetrimino"},
          {"password": hash_text("F04nSw!tch"), "userName": "dougFalcon".lower(), "email": "bluefalcon07@email.com",
           "phoneNum": "0762244323", "references": "Aaron", "tech_skills": ["HTML", "R", "CSS", "Lua"],
           "business_skills": ["management", "problem-solving", "multitasking"], "attitude": ["respectful", "creative"],
           "bestMatch": [], "name": "Doug Falcon"},
        {"password": hash_text("C4lamityT!me"), "userName": "zeldaB".lower(), "email": "nayruLovesMe@email.com",
         "phoneNum": "8046912345", "references": "Nayru", "tech_skills": ["Java", "Scala"],
         "business_skills": ["mathematics", "customer-service", "research", "critical-thinking"],
         "attitude": ["helpfulness", "dependable"], "bestMatch": [], "name": "Zelda Faore"},
        {"password": hash_text("Fl1ghtless#"), "userName": "fLombardi".lower(), "email": "icantfly@email.com",
         "phoneNum": "4046912340", "references": "Aaron", "tech_skills": ["HTML"],
         "business_skills": ["problem-solving", "food-services", "graphic-design", "Software-development"],
         "attitude": ["enthusiastic", "motivated"], "bestMatch": [], "name": "Falcon Lombardi"},
        {"password": hash_text("sTh*12awQ"), "userName": "samAran".lower(), "email": "metroid@email.com",
         "phoneNum": "4046876340", "references": "Aaron", "tech_skills": ["CSS", "Java"],
         "business_skills": ["marketing/sales", "Organization"],
         "attitude": ["engineering", "innovative", "helpfulness"], "bestMatch": [], "name": "Samus Aran"},
        {"password": hash_text("Gr8gonzo!o"), "userName": "mariom".lower(), "email": "plumber1@email.com",
         "phoneNum": "4046937251", "references": "Luigi M", "tech_skills": ["Assembly", "C++", "python", "c", "PL/SQL"],
         "business_skills": ["journalism", "customer-service", "Finance", "communication"],
         "attitude": ["cheerful", "adaptable"], "bestMatch": [], "name": "Mario Mario"},
        {"password": hash_text("R3ntDu#e"), "userName": "isaBelle".lower(), "email": "bubblegum@email.com",
         "phoneNum": "3046937209", "references": "Tom", "tech_skills": ["HTML", "Erlang", "CSS"],
         "business_skills": ["Time-management", "digital-media", "public-speaking"],
         "attitude": ["professional", "determined", "responsible"], "bestMatch": [], "name": "Isabelle Shizue"},

        {"password": hash_text("Cr@yo0a."), "userName": "euLawrence".lower(), "email": "cryoQueen@email.com",
         "phoneNum": "3056937276", "references": "Adrian", "tech_skills": ["HTML"],
         "business_skills": ["information-technology", "Time-management"], "attitude": ["helpfulness"], "bestMatch": [],
         "name": "Eula Lawrence"},
        {"password": hash_text("Rewrite123%"), "userName": "lucinaFate".lower(), "email": "notWritten@emblem.com",
         "phoneNum": "6076226092", "references": "Marth", "tech_skills": ["C++"],
         "business_skills": ["management", "multilingual", "Insurance"], "attitude": ["motivated", "cheerful"],
         "bestMatch": [], "name": "Lucina Fate"},
        {"password": hash_text("Pui.pui6*"), "userName": "ambMolcar".lower(), "email": "PUIPUI@email.com",
         "phoneNum": "3056938877", "references": "Rifujin", "tech_skills": ["c", "Java", "Swift", "Cobol"],
         "business_skills": ["public-speaking", "Quickbooks", "Software-development"],
         "attitude": ["dependable", "positive"], "bestMatch": [], "name": "Ambulance Molcar"},
        {"password": hash_text("h1llyChurl$"), "userName": "huTao".lower(), "email": "noStamina@email.com",
         "phoneNum": "5056933214", "references": "Ghosts", "tech_skills": ["CSS"],
         "business_skills": ["communication", "mathematics", "customer-service", "public-relations"],
         "attitude": ["responsible"], "bestMatch": [], "name": "Hu Tao"},
        {"password": hash_text("e8@Ys05Qe"), "userName": "shieldNaofumi".lower(), "email": "shieldHero@email.com",
         "phoneNum": "6376223468", "references": "Filo", "tech_skills": ["HTML", "Rust"],
         "business_skills": ["customer-service", "food-services", "graphic-design", "engineering"],
         "attitude": ["respectful"], "bestMatch": [], "name": "Naofumi Iwatani"},
        {"password": hash_text("Password901%"), "userName": "yuriLowell".lower(), "email": "yLowell@email.com",
         "phoneNum": "9156933215", "references": "Repede", "tech_skills": ["C++", "Lisp"],
         "business_skills": ["public-relations", "information-technology", "cloud-computing"],
         "attitude": ["helpfulness", "problem-solving", "adaptable"], "bestMatch": [], "name": "Yuri Lowell"},
        {"password": hash_text("sa2Efl*djk"), "userName": "swordRaphtalia".lower(), "email": "swordRacoon@email.com",
         "phoneNum": "7076224433", "references": "Filo", "tech_skills": ["Java"],
         "business_skills": ["multilingual", "journalism", "problem-solving"], "attitude": ["enthusiastic"],
         "bestMatch": [], "name": "Raphtalia Tanuki"},
        {"password": hash_text("Samson456!"), "userName": "filiaMedici".lower(), "email": "badHairDay@skullheart.com",
         "phoneNum": "9382161465", "references": "Carol", "tech_skills": ["C#", "python", "Lua"],
         "business_skills": ["communication", "public-speaking"],
         "attitude": ["responsible", "motivated", "dependable"], "bestMatch": [], "name": "Filia Medici"},
        {"password": hash_text("o$pw3erEqiu"), "userName": "jStingray".lower(), "email": "shadowmaster@email.com",
         "phoneNum": "8782161465", "references": "Dana", "tech_skills": ["HTML", "CSS", "Rust", "Kotlin"],
         "business_skills": ["digital-media", "economics", "multitasking"], "attitude": ["innovative"], "bestMatch": [],
         "name": "Jill Stingray"},
        {"password": hash_text("x1zncmB.n"), "userName": "rShiba".lower(), "email": "coolDog@email.com",
         "phoneNum": "8102937856", "references": "Dana", "tech_skills": ["JavaScript"],
         "business_skills": ["customer-service", "human-resources"],
         "attitude": ["helpfulness", "creative", "cheerful"], "bestMatch": [], "name": "Rad Shiba"},

        {"password": hash_text("uiQweroR4@"), "userName": "aArmas".lower(), "email": "mechArms@email.com",
         "phoneNum": "3126907858", "references": "Gil", "tech_skills": ["R", "JavaScript", "Erlang", "c"],
         "business_skills": ["Organization", "customer-service", "Software-engineering"],
         "attitude": ["respectful", "determined"], "bestMatch": [], "name": "Alma Armas"},
        {"password": hash_text("fgdAjert#1"), "userName": "dHaze".lower(), "email": "willowg@email.com",
         "phoneNum": "7665439987", "references": "Anna", "tech_skills": ["Swift", "JavaScript", "Assembly"],
         "business_skills": ["marketing/sales", "digital-media", "Software-development"],
         "attitude": ["innovative", "adaptable"], "bestMatch": [], "name": "Dorothy Haze"},
        {"password": hash_text("xcz$ioEsd0"), "userName": "kirby".lower(), "email": "poyo@email.com", "phoneNum": "6076226093",
         "references": "Karina", "tech_skills": ["Java", "C#", "MATLAB"],
         "business_skills": ["problem-solving", "multitasking"], "attitude": ["professional", "helpfulness"],
         "bestMatch": [], "name": "Kirby Keeby"},
        {"password": hash_text("SaintTi3r$"), "userName": "rMigurdia".lower(), "email": "migurdia@tensei.com",
         "phoneNum": "6376287658", "references": "Ruijerd", "tech_skills": ["c", "Lisp"],
         "business_skills": ["communication", "writing", "research"], "attitude": ["respectful", "enthusiastic"],
         "bestMatch": [], "name": "Roxy Migurdia"},
        {"password": hash_text("wEq1rWm$n"), "userName": "cGrimoire".lower(), "email": "cliffbar@email.com",
         "phoneNum": "3334445555", "references": "Elinalise", "tech_skills": ["C++"],
         "business_skills": ["Accounting", "Quickbooks", "problem-solving"], "attitude": ["respectful", "dependable"],
         "bestMatch": [], "name": "Cliff Grimoire"},
        {"password": hash_text("eqw1Khjz%x"), "userName": "sSaturn".lower(), "email": "tomoeH@email.com",
         "phoneNum": "1112223333", "references": "Chibiusa", "tech_skills": ["HTML", "CSS", "Rust"],
         "business_skills": ["human-resources", "customer-service"], "attitude": ["cheerful"], "bestMatch": [],
         "name": "Hotaru Tomoe"},
        {"password": hash_text("jklfgd40as"), "userName": "sAsagiri".lower(), "email": "whiteKnight@email.com",
         "phoneNum": "7076226543", "references": "Jill", "tech_skills": ["C#", "python", "c"],
         "business_skills": ["public-speaking", "management", "graphic-design"], "attitude": ["positive", "determined"],
         "bestMatch": [], "name": "Sei Asagiri"},
        {"password": hash_text("7Screaming12%"), "userName": "nonJakuzure".lower(), "email": "symphony@email.com",
         "phoneNum": "2223334444", "references": "Satsuki", "tech_skills": ["Kotlin", "JavaScript"],
         "business_skills": ["mathematics", "journalism", "digital-media"], "attitude": ["helpfulness", "motivated"],
         "bestMatch": [], "name": "Nonon Jakuzure"},
        {"password": hash_text("qklwjnfe7Rq"), "userName": "stell4".lower(), "email": "ellaHoshii@email.com",
         "phoneNum": "5439876543", "references": "Jill", "tech_skills": ["Java", "Cobol", "Ruby"],
         "business_skills": ["Organization", "economics", "problem-solving"], "attitude": ["enthusiastic"],
         "bestMatch": [], "name": "Stella Hoshii"},
        {"password": hash_text("uwifbe@tqs"), "userName": "mikira".lower(), "email": "kiraKira@email.com",
         "phoneNum": "9026907858", "references": "Jill", "tech_skills": ["Java"],
         "business_skills": ["multilingual", "food-services", "customer-service"], "attitude": ["cheerful", "creative"],
         "bestMatch": [], "name": "Kira Miki"},
        {"password": hash_text("Pass465word#"), "userName": "Tarako".lower(), "email": "groundBeef@email.com",
         "phoneNum": "9076907858", "references": "Samekichi", "tech_skills": ["C#", "Java", "python"],
         "business_skills": ["marketing/sales", "multilingual", "public-speaking", "management"],
         "attitude": ["cheerful", "helpfulness"], "bestMatch": [], "name": "Tarako Calamari"},
         {"password": hash_text("67gdeEr0!)"), "userName": "claudeRiegan".lower(), "email": "goldenDeer@emblem.com",
         "phoneNum": "8026907895", "references": "Judith", "tech_skills": ["C++"],
         "business_skills": ["communication", "Organization", "human-resources"],
         "attitude": ["adaptable", "responsible", "dependable"], "bestMatch": [], "name": "Claude Riegan"},

        {"password": hash_text("q5fweij%A"), "userName": "cardSakura".lower(), "email": "clowCard@email.com",
         "phoneNum": "7076226065", "references": "Tomoyo", "tech_skills": ["Ruby", "Java", "MATLAB"],
         "business_skills": ["critical-thinking", "multilingual", "management"], "attitude": ["determined"],
         "bestMatch": [], "name": "Sakura Kinomoto"},
        {"password": hash_text("oi$evWrth0"), "userName": "syaoLi".lower(), "email": "clearCard@email.com",
         "phoneNum": "5678123098", "references": "Kero", "tech_skills": ["HTML"],
         "business_skills": ["journalism", "public-speaking", "information-technology", "cloud-computing"],
         "attitude": ["cheerful"], "bestMatch": [], "name": "Syaoran Li"},
         {"password": hash_text("fiuhj3Es%"), "userName": "lunaP".lower(), "email": "chibiLuna@email.com",
          "phoneNum": "1230985678", "references": "Chibiusa", "tech_skills": ["C#", "Lua", "HTML", "Erlang"],
          "business_skills": ["marketing/sales", "research", "data analysis"], "attitude": ["respectful", "motivated"],
          "bestMatch": [], "name": "Luna P"},
        {"password": hash_text("wsXijmkW@a3"), "userName": "yuChan".lower(), "email": "yuuri@email.com",
         "phoneNum": "8865439987", "references": "Statue", "tech_skills": ["c", "python", "C#"],
         "business_skills": ["management", "public-relations", "customer-service"], "attitude": ["innovative"],
         "bestMatch": [], "name": "Yuuri To"},
        {"password": hash_text("saofTwe6@1"), "userName": "chiChan".lower(), "email": "chito@email.com",
         "phoneNum": "6376907858", "references": "Statue", "tech_skills": ["C++", "Cobol", "Assembly"],
         "business_skills": ["customer-service", "Software-development", "multilingual", "digital-media"],
         "attitude": ["determined", "dependable"], "bestMatch": [], "name": "Chito Yu"},
        {"password": hash_text("qwefxhT54!"), "userName": "tInumaki".lower(), "email": "toge@email.com",
         "phoneNum": "2306789856", "references": "Salmon", "tech_skills": ["Java", "Swift"],
         "business_skills": ["Accounting", "marketing/sales", "Finance"], "attitude": ["helpfulness"], "bestMatch": [],
         "name": "Toge Inumaki"},
        {"password": hash_text("zx0fghJk%"), "userName": "mZenin".lower(), "email": "maki@email.com", "phoneNum": "6076226094",
         "references": "Mai", "tech_skills": ["Java"],
         "business_skills": ["multitasking", "communication", "Time-management"],
         "attitude": ["respectful", "cheerful"], "bestMatch": [], "name": "Maki Zenin"},
         {"password": hash_text("aueo5rw#Q"), "userName": "kaoriM".lower(), "email": "violin@email.com",
          "phoneNum": "8102654436", "references": "Watari", "tech_skills": ["CSS", "JavaScript", "HTML"],
          "business_skills": ["Organization", "communication", "human-resources"],
          "attitude": ["responsible", "professional"], "bestMatch": [], "name": "Kaori Miyazono"},
          {"password": hash_text("esyrtYb@56"), "userName": "kArima".lower(), "email": "piano@email.com",
           "phoneNum": "4736281762", "references": "Tsubaki", "tech_skills": ["c", "Java", "Rust"],
           "business_skills": ["customer-service", "multilingual", "digital-media"], "attitude": ["enthusiastic"],
           "bestMatch": [], "name": "Kosei Arima"},
        {"password": hash_text("hjklfAs!d5"), "userName": "dHaku".lower(), "email": "river@email.com", "phoneNum": "2817624736",
         "references": "Kaonashi", "tech_skills": ["JavaScript"],
         "business_skills": ["critical-thinking", "Quickbooks"], "attitude": ["responsible"], "bestMatch": [],
         "name": "Dragon Haku"},

        {"password": hash_text("xvcnBsf2$"), "userName": "chihiroO".lower(), "email": "spirited@email.com",
         "phoneNum": "1762284736", "references": "Kaonashi", "tech_skills": ["JavaScript", "Erlang", "Java", "python"],
         "business_skills": ["customer-service", "food-services", "management"], "attitude": ["dependable", "positive"],
         "bestMatch": [], "name": "Chihiro Spirit"},
        {"password": hash_text("Password12!"), "userName": "keqing".lower(), "email": "electro@email.com",
         "phoneNum": "9026907891", "references": "Decimo", "tech_skills": ["C++", "Kotlin", "HTML"],
         "business_skills": ["writing", "journalism", "problem-solving", "research"],
         "attitude": ["innovative", "adaptable"], "bestMatch": [], "name": "Keqing Qi"},
        {"password": hash_text("Password12@"), "userName": "cryoDiona".lower(), "email": "catstail@email.com",
         "phoneNum": "8473617622", "references": "Draff", "tech_skills": ["Scala", "JavaScript"],
         "business_skills": ["information-technology", "multilingual", "Organization"],
         "attitude": ["professional", "responsible"], "bestMatch": [], "name": "Diona Cryo"},
        {"password": hash_text("Bfgd4qw1K#"), "userName": "ganyuRain".lower(), "email": "sweetRain@email.com",
         "phoneNum": "6096607622", "references": "Decimo", "tech_skills": ["CSS"],
         "business_skills": ["Software-development", "management", "critical-thinking", "graphic-design",
                             "engineering"], "attitude": ["respectful", "creative"], "bestMatch": [],
         "name": "Ganyu Rain"},
        {"password": hash_text("Password12$"), "userName": "qiqi7".lower(), "email": "seven@email.com",
         "phoneNum": "7622609660", "references": "Baizhu", "tech_skills": ["Swift", "HTML", "python"],
         "business_skills": ["Insurance", "information-technology", "public-speaking", "Software-engineering"],
         "attitude": ["helpfulness", "professional", "motivated"], "bestMatch": [], "name": "QiQi Seven"},
        {"password": hash_text("Password12%"), "userName": "alatus".lower(), "email": "xiao@email.com",
         "phoneNum": "6076226099", "references": "Morax", "tech_skills": ["Java"],
         "business_skills": ["problem-solving", "mathematics", "economics", "cloud-computing"],
         "attitude": ["responsible"], "bestMatch": [], "name": "Xiao Alatus"},
        {"password": hash_text("Password12."), "userName": "venti".lower(), "email": "barbatos@email.com",
         "phoneNum": "3622601664", "references": "Carmen", "tech_skills": ["C#", "python", "Cobol"],
         "business_skills": ["marketing/sales", "human-resources", "Time-management"], "attitude": ["determined"],
         "bestMatch": [], "name": "Venti Wind"},
        {"password": hash_text("vcnBfgd40@"), "userName": "yanfei".lower(), "email": "scarlet@email.com",
         "phoneNum": "2847361762", "references": "Pyro", "tech_skills": ["c", "Scala"],
         "business_skills": ["research", "customer-service", "data analysis"],
         "attitude": ["adaptable", "cheerful", "dependable", "innovative"], "bestMatch": [], "name": "Yanfei Scarlet"},
        {"password": hash_text("Password12#"), "userName": "doremy".lower(), "email": "doreime@email.com",
         "phoneNum": "8865439999", "references": "Rei", "tech_skills": ["HTML", "Rust", "python", "MATLAB"],
         "business_skills": ["multitasking", "management", "communication"], "attitude": ["enthusiastic"],
         "bestMatch": [], "name": "Doremy Rei"},
        {"password": hash_text("vcnBxsf2$"), "userName": "wumbo".lower(), "email": "fourwide@email.com",
         "phoneNum": "6512654409", "references": "Schezo", "tech_skills": ["C++", "PL/SQL", "Erlang", "R"],
         "business_skills": ["problem-solving", "communication", "customer-service", "engineering"],
         "attitude": ["innovative"], "bestMatch": [], "name": "Wumbo Schezo"}
    ])

def del_candidates():
    candidates.remove( {} )

def add_companies():
    companies.insert_many([
        {"companyName": "Segwa", "email": "dreamcast@segwa.com", "phoneNum": "1237650912", "password":  hash_text("Sonic12#"), "job_list": [], "userName":"segwa123"},
        {"companyName": "Notendo", "email": "lawsuit@notendo.com", "phoneNum": "3872503862", "password":  hash_text("Password#2"), "job_list": [], "userName":"notendo123"},
        {"companyName": "Moonbucks", "email": "corporation@moonbucks.com", "phoneNum": "1234567890", "password":  hash_text("Hell0There!"), "job_list": [], "userName":"moonbucks123"},
        {"companyName": "WcDonalds", "email": "allNatural@wcdonalds.com", "phoneNum": "4567890123", "password":  hash_text("H3yListen!"), "job_list": [], "userName":"wcdonalds123"},
        {"companyName": "EyeBeeMmm", "email": "techtech@ebm.com", "phoneNum": "5254562350", "password":  hash_text("Fo0tnote#"), "job_list": [], "userName":"eyebeemmm123"},
        {"companyName": "Orange", "email": "income@orange.com", "phoneNum": "5678901234", "password":  hash_text("Over1t*"), "job_list": [], "userName":"orange123"},
        {"companyName": "Macrosoft", "email": "preloaded@macrosoft.com", "phoneNum": "2348761287", "password":  hash_text("PoyoPoy0%"), "job_list": [], "userName":"macrosoft123"},
        {"companyName": "Marusan", "email": "nomsg@marusan.com", "phoneNum": "2291636700", "password":  hash_text("Calpico2@"), "job_list": [], "userName":"marusan123"},
        {"companyName": "Qooqle", "email": "hresources@qooqle.com", "phoneNum": "2996187812", "password":  hash_text("AkjE3qPoL6 @ "), "job_list":[], "userName": "qoogle123"},
        {"companyName": "Cube Enix", "email": "trianglestrategy@cubeenix.com", "phoneNum": "1267893547","password":  hash_text("Notepad3#"), "job_list": [], "userName":"cubeenix123"},
        {"companyName": "Ise-cafe", "email": "isekai@isecafe.com", "phoneNum": "5738920374", "password":  hash_text("Spotify%5"), "job_list": [], "userName":"isecafe123"},
        {"companyName": "The Binary Job Search", "email": "searching@bjs.com", "phoneNum": "8234562359","password":  hash_text("Traveler#1"), "job_list": [], "userName":"tbjs123"},
        {"companyName": "Office Outlet", "email": "eightby11@officeoutlet.com", "phoneNum": "5254562350", "password":  hash_text("St8tion$"), "job_list": [], "userName":"st8tion123"},
        {"companyName": "Dead End", "email": "volume3@deadend.com", "phoneNum": "2758920370", "password":  hash_text("Card$card1"), "job_list": [], "userName":"de123"},
        {"companyName": "PetsCo", "email": "itHasAnS@petsco.com", "phoneNum": "1234562357", "password":  hash_text("HmLet*sSe3"), "job_list": [], "userName":"petsco123"}
    ])
def del_companies():
    companies.remove( {} )

def add_jobs():
    job = JobObject(1, "accountant", "accountant", "Looking for a skilled accountant willing to put in the time.",
                    ["python", "MATLAB"], ["Quickbooks", "Accounting", "Finance", "mathematics"],
                    ["committed", "professional", "responsible"], list()).create()
    job = JobObject(2, "programmer", "programming", "need experienced programmers", ["C", "C#", "C++", "Assembly"],
                    ["communication", "problem solving", "critical thinking"],
                    ["committed", "dependable", "professional"], list()).create()
    job = JobObject(3, "software developer", "software developer", "need beginner software developers",
                    ["Java", "python", "PL/SQL"], ["communication", "problem solving", "critical thinking"],
                    ["committed", "dependable", "professional"], list()).create()
    job = JobObject(4, "research assistant", "assist lead researcher", "help with research", ["PL/SQL"],
                    ["communication", "Organization", "research"], ["respectful", "helpfulness", "responsible"],
                    list()).create()
    job = JobObject(5, "IT", "information technology", "IT role", ["HTML", "CSS", "JavaScript", "Java"],
                    ["information technology"], ["helpfulness", "adaptable"], list()).create()

    job = JobObject(6, "digital media specialist", "social media manager", "Looking to grow our social media presence.",
                    list(), ["marketing/sales", "digital media", "writing", "graphic design"],
                    ["enthusiastic", "adaptable", "creative"], list()).create()
    job = JobObject(7, "marketing associate", "marketing associate",
                    "need marketing associate to help relay our company message.", list(),
                    ["digital media", "marketing/sales"], ["enthusiastic", "adaptable"], list()).create()
    job = JobObject(8, "grocery manager", "grocery manager", "need grocery manager to handle shift leading", list(),
                    ["customer service", "food services"], ["dependable"], list()).create()
    job = JobObject(9, "insurance consultant", "insurance consultant", "in need of insurance consultant",
                    ["MATLAB", "R"], ["Finance", "Insurance"], ["professional"], list()).create()
    job = JobObject(10, "restaurant management", "restaurant management", "looking for a restaurant manager", list(),
                    ["customer service", "food services", "multitasking"], ["dependable", "responsible"],
                    list()).create()

    job = JobObject(11, "newsletter columnist", "newsletter columnist", "looking for new columnist", list(),
                    ["multilingual", "writing", "research"], ["committed", "professional"], list()).create()
    job = JobObject(12, "economist", "economist", "economic advisor", ["R"], ["Finance", "Accounting"],
                    ["dependable", "responsible", "professional"], list()).create()
    job = JobObject(13, "head of human resources", "head of human resources", list(), list(), list(), list(),
                    list()).create()
    job = JobObject(14, "cloud engineer", "cloud engineer", "not looking for meteorologists", ["C++", "Swift"],
                    ["critical thinking", "cloud computing"], ["innovative"], list()).create()
    job = JobObject(15, "research analyst", "researcher", "analyzing research", ["PL/SQL", "R"], ["research"],
                    ["committed", "professional"], list()).create()

    job = JobObject(16, "tetris downstacker", "demolition", "it's tetris yo", list(), ["critical thinking"],
                    ["enthusiastic", "cheerful", "innovative", "adaptable"], list()).create()
    job = JobObject(17, "puyo exterminator", "exterminator", "time for puyo puyo", list(), ["critical thinking"],
                    ["cheerful", "helpful", "adaptable"], list()).create()
    job = JobObject(18, "architect", "opposite of demolition", "what should the buildings look like though", list(),
                    ["Organization", "engineering"], ["innovative", "creative"], list()).create()
    job = JobObject(19, "engineer", "how", "enginering...", ["MATLAB"], ["engineering"],
                    ["innovative", "adaptable", "creative"], list()).create()
    job = JobObject(20, "graphic design", "graphic designer", "whoah did you make this!", ["CSS"], ["graphic design"],
                    ["creative"], list()).create()

def del_jobs():
    jobs.remove( {} )

def test():
    company = list(companies.find())
    print(company)

