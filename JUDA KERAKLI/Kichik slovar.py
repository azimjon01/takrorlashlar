#################Kutubxonalar import qilingan o'chirilmasin##########################
from random import choice
import sys,subprocess
import pyttsx3
gap=pyttsx3.init()
voices=gap.getProperty('voices')
gap.setProperty('voice',voices[0].id)
import speech_recognition as sr
r = sr.Recognizer()


lugat=[



#########tugash#########*****600-700******###############


                                    # "poet - shoir",
                                    # "scene - sahna",
                                    # "sheet - varoq",
                                    # "silly - ahmoqona",
                                    # "store - omborga saqlamoq",


                                    # "suffer - azoblanmoq",
                                    # "chimney - mo'ri",
                                    # "breathe - nafas olmoq",
                                    # "characteristic - xarakterli",
                                    # "consume - iste'mol qilmoq",


                                    # "tube - truba",
                                    # "extreme - keskin",
                                    # "fear - qo'rqmoq",
                                    # "fortunate - baxtli",
                                    # "singlet - mayka",


                                    # "observe - kuzatmoq",
                                    # "opportune - qulay",
                                    # "race - poyga",
                                    # "tourniquet - turnik",
                                    # "respond - javob bermoq",


                                    # "risk - tavakkal",
                                    # "contemplate - o'ylamoq",
                                    # "wind - shamol",
                                    # "ancient - qadimiy",
                                    # "century - asr",


                                    # "clue - mantiq",
                                    # "county - graflik",
                                    # "exist - mavjud",
                                    # "flat - tekis",
                                    # "hidden - yashirin",


                                    # "maybe - balki",
                                    # "pound - tuymoq",
                                    # "process - jarayon",
                                    # "publish - nashr qilmoq",
                                    # "wealth - boylik",


                                    # "appreciate - qadrlamoq",
                                    # "available - mavjud",
                                    # "beat - yengmoq",
                                    # "bright - yorug'",
                                    # "celebrate - nishonlamoq",


                                    # "determine - aniqlamoq",
                                    # "disappear - yo'qolmoq",
                                    # "else - boshqa",
                                    # "fair - adolatli",
                                    # "flow - oqmoq",


                                    # "hill - tepalik",
                                    # "recede - ketmoq",
                                    # "round - yumaloq",
                                    # "nird - parranda",
                                    # "prise - ko'tarmoq",


                                    # "ballon - shar",
                                    # "barrel - bochka",
                                    # "bat - ko'rshapalak",
                                    # "bathtub - vanna",
                                    # "belt - kamar",


                                    # "bench - skameyka",
                                    # "biscuit - pecheniy",
                                    # "bolt - bolt",
                                    # "bone - suyak",
                                    # "boots - etik",


                                    # "bottle - butilka",
                                    # "brick - g'isht",
                                    # "bride - kelin",
                                    # "bridge - ko'prik",
                                    # "broom - supirgi",


                                    # "brush - cho'tka",
                                    # "bulb - lampochka",
                                    # "butcher - qassob",
                                    # "butter - saryog'",
                                    # "cabbage - karam",


                                    # "cage - qafas",
                                    # "cake - tort",
                                    # "chain - zanjir",
                                    # "clothespin - qisqich",
                                    # "coat - palto",


                                    # "cocoon - pilla",
                                    # "colt - toychoq",
                                    # "comb - taroq",
                                    # "corn - makkajo'xori",
                                    # "cotton - paxta",


                                    # "cradle - beshik",
                                    # "crayon - rangli qalam",
                                    # "crown - toj",
                                    # "curtain - parda",
                                    # "dagger - xanjar",


                                    # "dill - shivit",
                                    # "dove - kabutar",
                                    # "draughts - shashka",
                                    # "dressing gown - xalat",
                                    # "drum - do'mbira",


                                    # "dumb bell - gantel",
                                    # "eagle - burgut",
                                    # "eggplant - baqlajon",
                                    # "envelope - konvert",
                                    # "feather - pat",


                                    # "dignity - qadr qimmat",
                                    # "worth - qiymat",
                                    # "distress - qayg'u",
                                    # "brisk - chaqqon",
                                    # "debase - tushirmoq",


# ##############******1400-1500*****##################



                                    "budget-budjet",
                                    "airline-havo yo'li",
                                    "battle-jang",
                                    "ground-yer",
                                    "reference-ma'lumotnoma",


                                    "called - deyiladi",
                                    "should - kerak",
                                    "could you - qila olasizmi",
                                    "use - ishlatmoq",
                                    "do - qilmoq",


                                    "bother-bezovta",
                                    "curve-egri chiziq",
                                    "designer-dizayner",
                                    "dimension-o'lcham",
                                    "dress-kiyim",


                                    "ease-yengillik",
                                    "evening-kechqurun",
                                    "extension-kengaytirish",
                                    "farm-ferma ",
                                    "fight-jang",


                                    "tessera-kubik",
                                    "pipeline-quvur",
                                    "emergency-favqulodda vaziyat",
                                    "loan-qarz",
                                    "occasion-qulay fursat",


                                    # "package-paket",
                                    # "patient-bemor",
                                    # "proof-isbot ",
                                    # "race-poyga",
                                    # "sand-qum",


                                    # "sentence-gap ",
                                    # "stomach-oshqozon",
                                    # "shoulder-yelka",
                                    # "towel-sochiq",
                                    # "vacation-dam olish",


                                    # "wheel-g'ildirak",
                                    # "aside-chetga ",
                                    # "associate-asatsatsiya",
                                    # "horse-ot",
                                    # "blow-zarba",


                                    # "",
                                    # "branch-filial",
                                    # "bunch-to'plam",
                                    # "onion-piyoz",
                                    # "draft-qoralama",


                                    # "floor-qavat",
                                    # "",
                                    # "",
                                    # "league-liga",
                                    # "mail-xat",


                                    # "native-maxalliy",
                                    # "parent-ota ona",
                                    # "",
                                    # "pool-hovuz",
                                    # "request-so'rov",


                                    # "",
                                    # "shame-sharmandalik",
                                    # "shelter-boshpana",
                                    # "shoe-oyoq kiyimi",
                                    # "silver-kumush",


                                    # "tackle-kurash",
                                    # "tank-tank",
                                    # "",
                                    # "bake-pishirmoq",
                                    # "bar-bar",


                                    # "bell-qo'ngiroq",
                                    # "blame-aybdor",
                                    # "",
                                    # "closet-shkaf",
                                    # "collar-yoqa",


                                    # "comment-sharx",
                                    # "conference-kanferensiya",
                                    # "devil-iblis ",
                                    # "diet-dieta",
                                    # "fuel-yoqilg'i",


                                    # "glove-qo'lqop",
                                    # "lunch-tushlik",
                                    # "nurse-xamshira",
                                    # "panic-vahima",
                                    # "peak-cho'qqi",


                                    # "plane-samalyot ",
                                    # "eward-mukofot",
                                    # "sandwich-sendvich",
                                    # "shock-shok",
                                    # "lamp-lampa",


                                    # "surprise-ajablanish",
                                    # "till-gacha",
                                    # "transition-o'tish",
                                    # "weekend-xafta oxri ",
                                    # "snake-ilon",


                                    # "bicycle-velosiped",
                                    # "blind-ko'r",
                                    # "cable-kabel",
                                    # "candle-sham",
                                    # "clerk-kotib",


                                    # "alarm-signal",
                                    # "grandfather-bobo",
                                    # "knee-tizza",
                                    # "lawyer-advokat",
                                    # "leather-charm",












]       ##########################kodli blok#############################ochirilmasin!


#####################################ovozsiz#############################################
while True:
    sorash=input("Ovozli bo'lsinmi yoki ovozsiz(tez/aralash/tugaguncha/ovozli/ovozsiz/internetli):")
    if sorash.strip().lower()=="ovozsiz":
        print("O'zbekchaga tarjima qiling?⏳")
        notogrijavoblar=[]
        togri=0
        notogri=0
        while True:
            a=choice(lugat)
            b=a.split('-')
            print(b[0].strip())
            javob=input("Javob⏳(❎ break):  ")
            if javob.strip().lower()==b[1].strip().lower():
                togri+=1
                subprocess.run('cls',shell=True)
                print(togri+notogri,"✅👍👍👍👍👍👍👍👍👍")
                print("Javobingiz to'g'ri!")
                print(a.strip())
                print("Keyingi savol❓❔❕❗↩️")
            elif javob=="break":
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar)
                print(togri+notogri," tadan ",togri," ta tog'ri va ",notogri," ta notog'ri.")
                print("Endi inglizchaga tarjima qiling?⏳")
                break
            else:
                notogri+=1
                notogrijavoblar.append(a.strip())
                print(togri+notogri,"❎👎👎👎👎👎👎👎👎")
                print("Javobingiz noto'g'ri!")
                print(a.strip())
                print("Keyingi savol❓❔❕❗↩️")
        notogrijavoblar1=[]
        togri1=0
        notogri1=0
        while True:
            p=choice(lugat)
            i=p.split('-')
            print(i[1].strip())
            jav=input("Javob⏳(❎ break):  ")
            if jav.strip().lower()==i[0].strip().lower():
                togri1+=1
                subprocess.run('cls',shell=True)
                print(togri1+notogri1,"✅👍👍👍👍👍👍👍👍👍")
                print("Javobingiz to'g'ri!")
                print(p.strip())
                print("Keyingi savol❓❔❕❗↩️")
            elif jav=="break":
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar1)
                print(togri1+notogri1," tadan ",togri1," ta tog'ri va ",notogri1," ta notog'ri.")
                print("Davom etamiz!👍👍👍😁😁😁")
                break
            else:
                notogri1+=1
                notogrijavoblar1.append(p.strip())
                print(togri1+notogri1,"❎👎👎👎👎👎👎👎👎")
                print("Javobingiz noto'g'ri!")
                print(p.strip())
                print("Keyingi savol!")





        notogrijavoblar2=[]
        notogrijavoblar3=[]
        togri2=0
        notogri2=0
        togri3=0
        notogri3=0
        while True:
            engoxirgijavob=input("Hamma lug'atlarni ko'rishni xoxlaysizmi(ha/yo'q):")
            if engoxirgijavob=="ha":
                print("O'zbekchaga tarjima qiling?⏳")
                for oxirgi in lugat:
                    oxirgisiniki=oxirgi.split('-')
                    print(oxirgisiniki[0].strip())
                    javobimiz=input("Javob⏳(❎ break):  ")
                    if javobimiz.strip().lower()==oxirgisiniki[1].strip().lower():
                        togri2+=1
                        subprocess.run('cls',shell=True)
                        print(togri2+notogri2,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        print(oxirgi.strip())
                        print("Keyingi savol❓❔❕❗↩️")
                    elif javobimiz=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar2)
                        print(togri2+notogri2," tadan ",togri2," ta tog'ri va ",notogri2," ta notog'ri.")
                        print("Endi inglizchaga tarjima qiling?⏳")
                        break
                    else:
                        notogri2+=1
                        notogrijavoblar2.append(oxirgi.strip())
                        print(togri2+notogri2,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        print(oxirgi.strip())
                        print("Keyingi savol❓❔❕❗↩️")
                for yanoxir in lugat:
                    yanoxirgisi=yanoxir.split('-')
                    print(yanoxirgisi[1].strip())
                    javoxir=input("Javob⏳(❎ break):  ")
                    if javoxir.strip().lower()==yanoxirgisi[0].strip().lower():
                        togri3+=1
                        subprocess.run('cls',shell=True)
                        print(togri3+notogri3,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        print(yanoxir.strip())
                        print("Keyingi savol❓❔❕❗↩️")
                    elif javoxir=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar3)
                        print(togri3+notogri3," tadan ",togri3," ta tog'ri va ",notogri3," ta notog'ri.")
                        print("Davom etamiz!👍👍👍😁😁😁")
                        break
                    else:
                        notogri3+=1
                        notogrijavoblar3.append(yanoxir.strip())
                        print(togri3+notogri3,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        print(yanoxir.strip())
                        print("Keyingi savol!")
            elif engoxirgijavob=="yo'q":
                print("Sizning barcha xato javoblaringgiz: ",notogrijavoblar+notogrijavoblar1+notogrijavoblar2+notogrijavoblar3)
                print("Siz ",togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3," tadan ",togri+togri1+togri2+togri3," ta tog'ri va ",notogri+notogri1+notogri2+notogri3," ta notog'ri javob berdingiz!👍.")
                print("Ishtirok etganingiz uchun katta raxmat!👍👍👍👍👍😁😁😁😁😁😁")
                break
            else:
                print("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting!!!")


######################################ovozli#############################################

    elif sorash.strip().lower()=="ovozli":
        print("O'zbekchaga tarjima qiling?⏳")
        gap.say("O'zbekchaga tarjima qiling")
        gap.runAndWait()
        notogrijavoblar=[]
        togri=0
        notogri=0
        while True:
            a=choice(lugat)
            b=a.split('-')
            print(b[0].strip())
            gap.say(b[0])
            gap.runAndWait()
            javob=input("Javob⏳(❎ break):  ")
            if javob.strip().lower()==b[1].strip().lower():
                togri+=1
                subprocess.run('cls',shell=True)
                print(togri+notogri,"✅👍👍👍👍👍👍👍👍👍")
                print("Javobingiz to'g'ri!")
                gap.say("correct")
                gap.runAndWait()
                print(a.strip())
                gap.say(a)
                gap.runAndWait()
                print("Keyingi savol❓❔❕❗↩️")
                gap.say("next")
                gap.runAndWait()
            elif javob=="break":
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar)
                print(togri+notogri," tadan ",togri," ta tog'ri va ",notogri," ta notog'ri.")
                jamida=str(togri+notogri)
                tg=str(togri)
                ntg=str(notogri)
                gap.say(jamida+" " +"tadan "+tg+" ta tog'ri va "+ntg+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Endi inglizchaga tarjima qiling?⏳")
                gap.say("Endi inglizchaga tarjima qiling")
                gap.runAndWait()
                break
            else:
                notogri+=1
                notogrijavoblar.append(a.strip())
                print(togri+notogri,"❎👎👎👎👎👎👎👎👎")
                print("Javobingiz noto'g'ri!")
                gap.say("fail")
                gap.runAndWait()
                print(a.strip())
                gap.say(a)
                gap.runAndWait()
                print("Keyingi savol❓❔❕❗↩️")
                gap.say("next")
                gap.runAndWait()
        notogrijavoblar1=[]
        togri1=0
        notogri1=0
        while True:
            p=choice(lugat)
            i=p.split('-')
            print(i[1].strip())
            gap.say(i[1])
            gap.runAndWait()
            jav=input("Javob⏳(❎ break):  ")
            if jav.strip().lower()==i[0].strip().lower():
                togri1+=1
                subprocess.run('cls',shell=True)
                print(togri1+notogri1,"✅👍👍👍👍👍👍👍👍👍")
                print("Javobingiz to'g'ri!")
                gap.say("correct")
                gap.runAndWait()
                print(p.strip())
                gap.say(p)
                gap.runAndWait()
                print("Keyingi savol❓❔❕❗↩️")
                gap.say("next")
                gap.runAndWait()
            elif jav=="break":
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar1)
                print(togri1+notogri1," tadan ",togri1," ta tog'ri va ",notogri1," ta notog'ri.")
                togi=str(togri1+notogri1)
                togi2=str(togri1)
                togi3=str(notogri1)
                gap.say(togi+" tadan "+togi2+" ta tog'ri va "+togi3+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Davom etamiz!👍👍👍😁😁😁")
                gap.say("Davom etamiz")
                gap.runAndWait()
                break
            else:
                notogri1+=1
                notogrijavoblar1.append(p.strip())
                print(togri1+notogri1,"❎👎👎👎👎👎👎👎👎")
                print("Javobingiz noto'g'ri!")
                gap.say("fail")
                gap.runAndWait()
                print(p.strip())
                gap.say(p)
                gap.runAndWait()
                print("Keyingi savol!")
                gap.say("next")
                gap.runAndWait()





        notogrijavoblar2=[]
        notogrijavoblar3=[]
        togri2=0
        notogri2=0
        togri3=0
        notogri3=0
        while True:
            engoxirgijavob=input("Hamma lug'atlarni ko'rishni xoxlaysizmi(ha/yo'q):")
            gap.say("Hamma lug'atlarni ko'rishni xoxlaysizmi")
            gap.runAndWait()
            if engoxirgijavob=="ha":
                print("O'zbekchaga tarjima qiling?⏳")
                gap.say("O'zbekchaga tarjima qiling")
                gap.runAndWait()
                for oxirgi in lugat:
                    oxirgisiniki=oxirgi.split('-')
                    print(oxirgisiniki[0].strip())
                    gap.say(oxirgisiniki[0])
                    gap.runAndWait()
                    javobimiz=input("Javob⏳(❎ break):  ")
                    if javobimiz.strip().lower()==oxirgisiniki[1].strip().lower():
                        togri2+=1
                        subprocess.run('cls',shell=True)
                        print(togri2+notogri2,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        gap.say("correct")
                        gap.runAndWait()
                        print(oxirgi.strip())
                        gap.say(oxirgi)
                        gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        gap.say("next")
                        gap.runAndWait()
                    elif javobimiz=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar2)
                        print(togri2+notogri2," tadan ",togri2," ta tog'ri va ",notogri2," ta notog'ri.")
                        togsi=str(togri2+notogri2)
                        togsi2=str(togri2)
                        togsi3=str(notogri2)
                        gap.say(togsi+" tadan "+togsi2+" ta tog'ri va "+togsi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Endi inglizchaga tarjima qiling?⏳")
                        gap.say("Endi inglizchaga tarjima qiling")
                        gap.runAndWait()
                        break
                    else:
                        notogri2+=1
                        notogrijavoblar2.append(oxirgi.strip())
                        print(togri2+notogri2,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        gap.say("fail")
                        gap.runAndWait()
                        print(oxirgi.strip())
                        gap.say(oxirgi)
                        gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        gap.say("next")
                        gap.runAndWait()
                for yanoxir in lugat:
                    yanoxirgisi=yanoxir.split('-')
                    print(yanoxirgisi[1].strip())
                    gap.say(yanoxirgisi[1])
                    gap.runAndWait()
                    javoxir=input("Javob⏳(❎ break):  ")
                    if javoxir.strip().lower()==yanoxirgisi[0].strip().lower():
                        togri3+=1
                        subprocess.run('cls',shell=True)
                        print(togri3+notogri3,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        gap.say("correct")
                        gap.runAndWait()
                        print(yanoxir.strip())
                        gap.say(yanoxir)
                        gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        gap.say("next")
                        gap.runAndWait()
                    elif javoxir=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar3)
                        print(togri3+notogri3," tadan ",togri3," ta tog'ri va ",notogri3," ta notog'ri.")
                        toghi=str(togri3+notogri3)
                        toghi2=str(togri3)
                        toghi3=str(notogri3)
                        gap.say(toghi+" tadan "+toghi2+" ta tog'ri va "+toghi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Davom etamiz!👍👍👍😁😁😁")
                        gap.say("Davom etamiz")
                        gap.runAndWait()
                        break
                    else:
                        notogri3+=1
                        notogrijavoblar3.append(yanoxir.strip())
                        print(togri3+notogri3,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        gap.say("fail")
                        gap.runAndWait()
                        print(yanoxir.strip())
                        gap.say(yanoxir)
                        gap.runAndWait()
                        print("Keyingi savol!")
                        gap.say("next")
                        gap.runAndWait()
            elif engoxirgijavob=="yo'q":
                print("Sizning barcha xato javoblaringgiz: ",notogrijavoblar+notogrijavoblar1+notogrijavoblar2+notogrijavoblar3)
                print("Siz ",togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3," tadan ",togri+togri1+togri2+togri3," ta tog'ri va ",notogri+notogri1+notogri2+notogri3," ta notog'ri javob berdingiz!👍.")
                togli=str(togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3)
                togli2=str(togri+togri1+togri2+togri3)
                togli3=str(notogri+notogri1+notogri2+notogri3)
                gap.say("Siz "+togli+" tadan "+togli2+" ta tog'ri va "+togli3+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Ishtirok etganingiz uchun katta raxmat!👍👍👍👍👍😁😁😁😁😁😁")
                gap.say("Ishtirok etganingiz uchun katta raxmat")
                gap.runAndWait()
                break
            else:
                print("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting!!!")
                gap.say("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting")
                gap.runAndWait()



######################################tez#############################################

    elif sorash.strip().lower()=="tez":
        print("O'zbekchaga tarjima qiling?⏳")
        gap.say("O'zbekchaga tarjima qiling")
        gap.runAndWait()
        notogrijavoblar=[]
        togri=0
        notogri=0
        while True:
            a=choice(lugat)
            b=a.split('-')
            print(b[0].strip())
            gap.say(b[0])
            gap.runAndWait()
            javob=input("Javob⏳(❎ break):  ")
            if javob.strip().lower()==b[1].strip().lower():
                togri+=1
                subprocess.run('cls',shell=True)
                print(togri+notogri,"✅👍👍👍👍👍👍👍👍👍")
                print("Javobingiz to'g'ri!")
                # gap.say("correct")
                # gap.runAndWait()
                print(a.strip())
                # gap.say(a)
                # gap.runAndWait()
                print("Keyingi savol❓❔❕❗↩️")
                # gap.say("next")
                # gap.runAndWait()
            elif javob=="break":
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar)
                print(togri+notogri," tadan ",togri," ta tog'ri va ",notogri," ta notog'ri.")
                jamida=str(togri+notogri)
                tg=str(togri)
                ntg=str(notogri)
                gap.say(jamida+" " +"tadan "+tg+" ta tog'ri va "+ntg+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Endi inglizchaga tarjima qiling?⏳")
                gap.say("Endi inglizchaga tarjima qiling")
                gap.runAndWait()
                break
            else:
                notogri+=1
                notogrijavoblar.append(a.strip())
                print(togri+notogri,"❎👎👎👎👎👎👎👎👎")
                print("Javobingiz noto'g'ri!")
                # gap.say("fail")
                # gap.runAndWait()
                print(a.strip())
                # gap.say(a)
                # gap.runAndWait()
                print("Keyingi savol❓❔❕❗↩️")
                # gap.say("next")
                # gap.runAndWait()
        notogrijavoblar1=[]
        togri1=0
        notogri1=0
        while True:
            p=choice(lugat)
            i=p.split('-')
            print(i[1].strip())
            gap.say(i[1])
            gap.runAndWait()
            jav=input("Javob⏳(❎ break):  ")
            if jav.strip().lower()==i[0].strip().lower():
                togri1+=1
                subprocess.run('cls',shell=True)
                print(togri1+notogri1,"✅👍👍👍👍👍👍👍👍👍")
                print("Javobingiz to'g'ri!")
                # gap.say("correct")
                # gap.runAndWait()
                print(p.strip())
                gap.say(i[0])
                gap.runAndWait()
                # gap.say(p)
                # gap.runAndWait()
                print("Keyingi savol❓❔❕❗↩️")
                # gap.say("next")
                # gap.runAndWait()
            elif jav=="break":
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar1)
                print(togri1+notogri1," tadan ",togri1," ta tog'ri va ",notogri1," ta notog'ri.")
                togi=str(togri1+notogri1)
                togi2=str(togri1)
                togi3=str(notogri1)
                gap.say(togi+" tadan "+togi2+" ta tog'ri va "+togi3+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Davom etamiz!👍👍👍😁😁😁")
                # gap.say("Davom etamiz")
                # gap.runAndWait()
                break
            else:
                notogri1+=1
                notogrijavoblar1.append(p.strip())
                print(togri1+notogri1,"❎👎👎👎👎👎👎👎👎")
                print("Javobingiz noto'g'ri!")
                # gap.say("fail")
                # gap.runAndWait()
                print(p.strip())
                gap.say(i[0])
                gap.runAndWait()
                # gap.say(p)
                # gap.runAndWait()
                print("Keyingi savol!")
                # gap.say("next")
                # gap.runAndWait()





        notogrijavoblar2=[]
        notogrijavoblar3=[]
        togri2=0
        notogri2=0
        togri3=0
        notogri3=0
        while True:
            engoxirgijavob=input("Hamma lug'atlarni ko'rishni xoxlaysizmi(ha/yo'q):")
            # gap.say("Hamma lug'atlarni ko'rishni xoxlaysizmi")
            # gap.runAndWait()
            if engoxirgijavob=="ha":
                print("O'zbekchaga tarjima qiling?⏳")
                gap.say("O'zbekchaga tarjima qiling")
                gap.runAndWait()
                for oxirgi in lugat:
                    oxirgisiniki=oxirgi.split('-')
                    print(oxirgisiniki[0].strip())
                    gap.say(oxirgisiniki[0])
                    gap.runAndWait()
                    javobimiz=input("Javob⏳(❎ break):  ")
                    if javobimiz.strip().lower()==oxirgisiniki[1].strip().lower():
                        togri2+=1
                        subprocess.run('cls',shell=True)
                        print(togri2+notogri2,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        # gap.say("correct")
                        # gap.runAndWait()
                        print(oxirgi.strip())
                        # gap.say(oxirgi)
                        # gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        # gap.say("next")
                        # gap.runAndWait()
                    elif javobimiz=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar2)
                        print(togri2+notogri2," tadan ",togri2," ta tog'ri va ",notogri2," ta notog'ri.")
                        togsi=str(togri2+notogri2)
                        togsi2=str(togri2)
                        togsi3=str(notogri2)
                        gap.say(togsi+" tadan "+togsi2+" ta tog'ri va "+togsi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Endi inglizchaga tarjima qiling?⏳")
                        gap.say("Endi inglizchaga tarjima qiling")
                        gap.runAndWait()
                        break
                    else:
                        notogri2+=1
                        notogrijavoblar2.append(oxirgi.strip())
                        print(togri2+notogri2,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        # gap.say("fail")
                        # gap.runAndWait()
                        print(oxirgi.strip())
                        # gap.say(oxirgi)
                        # gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        # gap.say("next")
                        # gap.runAndWait()
                for yanoxir in lugat:
                    yanoxirgisi=yanoxir.split('-')
                    print(yanoxirgisi[1].strip())
                    gap.say(yanoxirgisi[1])
                    gap.runAndWait()
                    javoxir=input("Javob⏳(❎ break):  ")
                    if javoxir.strip().lower()==yanoxirgisi[0].strip().lower():
                        togri3+=1
                        subprocess.run('cls',shell=True)
                        print(togri3+notogri3,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        # gap.say("correct")
                        # gap.runAndWait()
                        print(yanoxir.strip())
                        # gap.say(yanoxir)
                        # gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        # gap.say("next")
                        # gap.runAndWait()
                    elif javoxir=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar3)
                        print(togri3+notogri3," tadan ",togri3," ta tog'ri va ",notogri3," ta notog'ri.")
                        toghi=str(togri3+notogri3)
                        toghi2=str(togri3)
                        toghi3=str(notogri3)
                        gap.say(toghi+" tadan "+toghi2+" ta tog'ri va "+toghi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Davom etamiz!👍👍👍😁😁😁")
                        # gap.say("Davom etamiz")
                        # gap.runAndWait()
                        break
                    else:
                        notogri3+=1
                        notogrijavoblar3.append(yanoxir.strip())
                        print(togri3+notogri3,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        # gap.say("fail")
                        # gap.runAndWait()
                        print(yanoxir.strip())
                        # gap.say(yanoxir)
                        # gap.runAndWait()
                        print("Keyingi savol!")
                        # gap.say("next")
                        # gap.runAndWait()
            elif engoxirgijavob=="yo'q":
                print("Sizning barcha xato javoblaringgiz: ",notogrijavoblar+notogrijavoblar1+notogrijavoblar2+notogrijavoblar3)
                print("Siz ",togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3," tadan ",togri+togri1+togri2+togri3," ta tog'ri va ",notogri+notogri1+notogri2+notogri3," ta notog'ri javob berdingiz!👍.")
                togli=str(togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3)
                togli2=str(togri+togri1+togri2+togri3)
                togli3=str(notogri+notogri1+notogri2+notogri3)
                gap.say("Siz "+togli+" tadan "+togli2+" ta tog'ri va "+togli3+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Ishtirok etganingiz uchun katta raxmat!👍👍👍👍👍😁😁😁😁😁😁")
                gap.say("Ishtirok etganingiz uchun katta raxmat")
                gap.runAndWait()
                break
            else:
                print("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting!!!")
                # gap.say("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting")
                # gap.runAndWait()



######################################aralash#############################################

    elif sorash.strip().lower()=="aralash":
        print("O'zbekchaga tarjima qiling?⏳")
        gap.say("O'zbekchaga tarjima qiling")
        gap.runAndWait()
        notogrijavoblar=[]
        togri=0
        notogri=0
        lugat_aralash=lugat[:]
        while True:
            if lugat_aralash == []:
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar)
                print(togri+notogri," tadan ",togri," ta tog'ri va ",notogri," ta notog'ri.")
                jamida=str(togri+notogri)
                tg=str(togri)
                ntg=str(notogri)
                gap.say(jamida+" " +"tadan "+tg+" ta tog'ri va "+ntg+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Endi inglizchaga tarjima qiling?⏳")
                gap.say("Endi inglizchaga tarjima qiling")
                gap.runAndWait()
                break
            else:
                a=choice(lugat_aralash)
                b=a.split('-')
                print(b[0].strip())
                gap.say(b[0])
                gap.runAndWait()
                javob=input("Javob⏳(❎ break):  ")
                if javob.strip().lower()==b[1].strip().lower():
                    togri+=1
                    subprocess.run('cls',shell=True)
                    print(togri+notogri,"✅👍👍👍👍👍👍👍👍👍")
                    print("Javobingiz to'g'ri!")
                    # gap.say("correct")
                    # gap.runAndWait()
                    print(a.strip())
                    # gap.say(a)
                    # gap.runAndWait()
                    print("Keyingi savol❓❔❕❗↩️")
                    # gap.say("next")
                    # gap.runAndWait()
                elif javob=="break":
                    subprocess.run('cls',shell=True)
                    print("Bular noto'g'ri javoblar:",notogrijavoblar)
                    print(togri+notogri," tadan ",togri," ta tog'ri va ",notogri," ta notog'ri.")
                    jamida=str(togri+notogri)
                    tg=str(togri)
                    ntg=str(notogri)
                    gap.say(jamida+" " +"tadan "+tg+" ta tog'ri va "+ntg+" ta notog'ri javob berdingiz")
                    gap.runAndWait()
                    print("Endi inglizchaga tarjima qiling?⏳")
                    gap.say("Endi inglizchaga tarjima qiling")
                    gap.runAndWait()
                    break
                else:
                    notogri+=1
                    notogrijavoblar.append(a.strip())
                    print(togri+notogri,"❎👎👎👎👎👎👎👎👎")
                    print("Javobingiz noto'g'ri!")
                    # gap.say("fail")
                    # gap.runAndWait()
                    print(a.strip())
                    # gap.say(a)
                    # gap.runAndWait()
                    print("Keyingi savol❓❔❕❗↩️")
                    # gap.say("next")
                    # gap.runAndWait()
                lugat_aralash.remove(a)
        notogrijavoblar1=[]
        togri1=0
        notogri1=0
        lugat_aralash1=lugat[:]
        while True:
            if lugat_aralash1 == []:
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar1)
                print(togri1+notogri1," tadan ",togri1," ta tog'ri va ",notogri1," ta notog'ri.")
                togi=str(togri1+notogri1)
                togi2=str(togri1)
                togi3=str(notogri1)
                gap.say(togi+" tadan "+togi2+" ta tog'ri va "+togi3+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Davom etamiz!👍👍👍😁😁😁")
                # gap.say("Davom etamiz")
                # gap.runAndWait()
                break
            else:
                p=choice(lugat_aralash1)
                i=p.split('-')
                print(i[1].strip())
                gap.say(i[1])
                gap.runAndWait()
                jav=input("Javob⏳(❎ break):  ")
                if jav.strip().lower()==i[0].strip().lower():
                    togri1+=1
                    subprocess.run('cls',shell=True)
                    print(togri1+notogri1,"✅👍👍👍👍👍👍👍👍👍")
                    print("Javobingiz to'g'ri!")
                    # gap.say("correct")
                    # gap.runAndWait()
                    print(p.strip())
                    # gap.say(p)
                    # gap.runAndWait()
                    gap.say(i[0])
                    gap.runAndWait()
                    print("Keyingi savol❓❔❕❗↩️")
                    # gap.say("next")
                    # gap.runAndWait()
                elif jav=="break":
                    subprocess.run('cls',shell=True)
                    print("Bular noto'g'ri javoblar:",notogrijavoblar1)
                    print(togri1+notogri1," tadan ",togri1," ta tog'ri va ",notogri1," ta notog'ri.")
                    togi=str(togri1+notogri1)
                    togi2=str(togri1)
                    togi3=str(notogri1)
                    gap.say(togi+" tadan "+togi2+" ta tog'ri va "+togi3+" ta notog'ri javob berdingiz")
                    gap.runAndWait()
                    print("Davom etamiz!👍👍👍😁😁😁")
                    # gap.say("Davom etamiz")
                    # gap.runAndWait()
                    break
                else:
                    notogri1+=1
                    notogrijavoblar1.append(p.strip())
                    print(togri1+notogri1,"❎👎👎👎👎👎👎👎👎")
                    print("Javobingiz noto'g'ri!")
                    # gap.say("fail")
                    # gap.runAndWait()
                    print(p.strip())
                    # gap.say(p)
                    # gap.runAndWait()
                    gap.say(i[0])
                    gap.runAndWait()
                    print("Keyingi savol!")
                    # gap.say("next")
                    # gap.runAndWait()
                lugat_aralash1.remove(p)




        notogrijavoblar2=[]
        notogrijavoblar3=[]
        togri2=0
        notogri2=0
        togri3=0
        notogri3=0
        while True:
            engoxirgijavob=input("Hamma lug'atlarni ko'rishni xoxlaysizmi(ha/yo'q):")
            # gap.say("Hamma lug'atlarni ko'rishni xoxlaysizmi")
            # gap.runAndWait()
            if engoxirgijavob=="ha":
                print("O'zbekchaga tarjima qiling?⏳")
                gap.say("O'zbekchaga tarjima qiling")
                gap.runAndWait()
                for oxirgi in lugat:
                    oxirgisiniki=oxirgi.split('-')
                    print(oxirgisiniki[0].strip())
                    gap.say(oxirgisiniki[0])
                    gap.runAndWait()
                    javobimiz=input("Javob⏳(❎ break):  ")
                    if javobimiz.strip().lower()==oxirgisiniki[1].strip().lower():
                        togri2+=1
                        subprocess.run('cls',shell=True)
                        print(togri2+notogri2,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        # gap.say("correct")
                        # gap.runAndWait()
                        print(oxirgi.strip())
                        # gap.say(oxirgi)
                        # gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        # gap.say("next")
                        # gap.runAndWait()
                    elif javobimiz=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar2)
                        print(togri2+notogri2," tadan ",togri2," ta tog'ri va ",notogri2," ta notog'ri.")
                        togsi=str(togri2+notogri2)
                        togsi2=str(togri2)
                        togsi3=str(notogri2)
                        gap.say(togsi+" tadan "+togsi2+" ta tog'ri va "+togsi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Endi inglizchaga tarjima qiling?⏳")
                        gap.say("Endi inglizchaga tarjima qiling")
                        gap.runAndWait()
                        break
                    else:
                        notogri2+=1
                        notogrijavoblar2.append(oxirgi.strip())
                        print(togri2+notogri2,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        # gap.say("fail")
                        # gap.runAndWait()
                        print(oxirgi.strip())
                        # gap.say(oxirgi)
                        # gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        # gap.say("next")
                        # gap.runAndWait()
                for yanoxir in lugat:
                    yanoxirgisi=yanoxir.split('-')
                    print(yanoxirgisi[1].strip())
                    gap.say(yanoxirgisi[1])
                    gap.runAndWait()
                    javoxir=input("Javob⏳(❎ break):  ")
                    if javoxir.strip().lower()==yanoxirgisi[0].strip().lower():
                        togri3+=1
                        subprocess.run('cls',shell=True)
                        print(togri3+notogri3,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        # gap.say("correct")
                        # gap.runAndWait()
                        print(yanoxir.strip())
                        # gap.say(yanoxir)
                        # gap.runAndWait()
                        gap.say(yanoxirgisi[0])
                        gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        # gap.say("next")
                        # gap.runAndWait()
                    elif javoxir=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar3)
                        print(togri3+notogri3," tadan ",togri3," ta tog'ri va ",notogri3," ta notog'ri.")
                        toghi=str(togri3+notogri3)
                        toghi2=str(togri3)
                        toghi3=str(notogri3)
                        gap.say(toghi+" tadan "+toghi2+" ta tog'ri va "+toghi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Davom etamiz!👍👍👍😁😁😁")
                        # gap.say("Davom etamiz")
                        # gap.runAndWait()
                        break
                    else:
                        notogri3+=1
                        notogrijavoblar3.append(yanoxir.strip())
                        print(togri3+notogri3,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        # gap.say("fail")
                        # gap.runAndWait()
                        print(yanoxir.strip())
                        # gap.say(yanoxir)
                        # gap.runAndWait()
                        gap.say(yanoxirgisi[0])
                        gap.runAndWait()
                        print("Keyingi savol!")
                        # gap.say("next")
                        # gap.runAndWait()
            elif engoxirgijavob=="yo'q":
                print("Sizning barcha xato javoblaringgiz: ",notogrijavoblar+notogrijavoblar1+notogrijavoblar2+notogrijavoblar3)
                print("Siz ",togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3," tadan ",togri+togri1+togri2+togri3," ta tog'ri va ",notogri+notogri1+notogri2+notogri3," ta notog'ri javob berdingiz!👍.")
                togli=str(togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3)
                togli2=str(togri+togri1+togri2+togri3)
                togli3=str(notogri+notogri1+notogri2+notogri3)
                gap.say("Siz "+togli+" tadan "+togli2+" ta tog'ri va "+togli3+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Ishtirok etganingiz uchun katta raxmat!👍👍👍👍👍😁😁😁😁😁😁")
                gap.say("Ishtirok etganingiz uchun katta raxmat")
                gap.runAndWait()
                break
            else:
                print("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting!!!")
                # gap.say("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting")
                # gap.runAndWait()



######################################tugaguncha#############################################

    elif sorash.strip().lower()=="tugaguncha":
        print("O'zbekchaga tarjima qiling?⏳")
        gap.say("O'zbekchaga tarjima qiling")
        gap.runAndWait()
        notogrijavoblar=[]
        togri=0
        notogri=0
        lugat_aralash=lugat[:]
        while True:
            if lugat_aralash == []:
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar)
                print(togri+notogri," tadan ",togri," ta tog'ri va ",notogri," ta notog'ri.")
                jamida=str(togri+notogri)
                tg=str(togri)
                ntg=str(notogri)
                gap.say(jamida+" " +"tadan "+tg+" ta tog'ri va "+ntg+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Endi inglizchaga tarjima qiling?⏳")
                gap.say("Endi inglizchaga tarjima qiling")
                gap.runAndWait()
                break
            else:
                a=choice(lugat_aralash)
                b=a.split('-')
                print(b[0].strip())
                gap.say(b[0])
                gap.runAndWait()
                javob=input("Javob⏳(❎ break):  ")
                if javob.strip().lower()==b[1].strip().lower():
                    togri+=1
                    subprocess.run('cls',shell=True)
                    print(togri+notogri,"✅👍👍👍👍👍👍👍👍👍")
                    print("Javobingiz to'g'ri!")
                    # gap.say("correct")
                    # gap.runAndWait()
                    print(a.strip())
                    # gap.say(a)
                    # gap.runAndWait()
                    print("Keyingi savol❓❔❕❗↩️")
                    # gap.say("next")
                    # gap.runAndWait()
                elif javob=="break":
                    subprocess.run('cls',shell=True)
                    print("Bular noto'g'ri javoblar:",notogrijavoblar)
                    print(togri+notogri," tadan ",togri," ta tog'ri va ",notogri," ta notog'ri.")
                    jamida=str(togri+notogri)
                    tg=str(togri)
                    ntg=str(notogri)
                    gap.say(jamida+" " +"tadan "+tg+" ta tog'ri va "+ntg+" ta notog'ri javob berdingiz")
                    gap.runAndWait()
                    print("Endi inglizchaga tarjima qiling?⏳")
                    gap.say("Endi inglizchaga tarjima qiling")
                    gap.runAndWait()
                    break
                else:
                    notogri+=1
                    notogrijavoblar.append(a.strip())
                    print(togri+notogri,"❎👎👎👎👎👎👎👎👎")
                    print("Javobingiz noto'g'ri!")
                    # gap.say("fail")
                    # gap.runAndWait()
                    print(a.strip())
                    # gap.say(a)
                    # gap.runAndWait()
                    print("Keyingi savol❓❔❕❗↩️")
                    # gap.say("next")
                    # gap.runAndWait()
                lugat_aralash.remove(a)
        notogrijavoblar1=[]
        togri1=0
        notogri1=0
        lugat_aralash1=lugat[:]
        while True:
            if lugat_aralash1 == []:
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar1)
                print(togri1+notogri1," tadan ",togri1," ta tog'ri va ",notogri1," ta notog'ri.")
                togi=str(togri1+notogri1)
                togi2=str(togri1)
                togi3=str(notogri1)
                gap.say(togi+" tadan "+togi2+" ta tog'ri va "+togi3+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Davom etamiz!👍👍👍😁😁😁")
                # gap.say("Davom etamiz")
                # gap.runAndWait()
                break
            else:
                p=choice(lugat_aralash1)
                i=p.split('-')
                print(i[1].strip())
                gap.say(i[1])
                gap.runAndWait()
                jav=input("Javob⏳(❎ break):  ")
                if jav.strip().lower()==i[0].strip().lower():
                    togri1+=1
                    subprocess.run('cls',shell=True)
                    print(togri1+notogri1,"✅👍👍👍👍👍👍👍👍👍")
                    print("Javobingiz to'g'ri!")
                    # gap.say("correct")
                    # gap.runAndWait()
                    print(p.strip())
                    # gap.say(p)
                    # gap.runAndWait()
                    gap.say(i[0])
                    gap.runAndWait()
                    print("Keyingi savol❓❔❕❗↩️")
                    # gap.say("next")
                    # gap.runAndWait()
                elif jav=="break":
                    subprocess.run('cls',shell=True)
                    print("Bular noto'g'ri javoblar:",notogrijavoblar1)
                    print(togri1+notogri1," tadan ",togri1," ta tog'ri va ",notogri1," ta notog'ri.")
                    togi=str(togri1+notogri1)
                    togi2=str(togri1)
                    togi3=str(notogri1)
                    gap.say(togi+" tadan "+togi2+" ta tog'ri va "+togi3+" ta notog'ri javob berdingiz")
                    gap.runAndWait()
                    print("Davom etamiz!👍👍👍😁😁😁")
                    # gap.say("Davom etamiz")
                    # gap.runAndWait()
                    break
                else:
                    notogri1+=1
                    notogrijavoblar1.append(p.strip())
                    print(togri1+notogri1,"❎👎👎👎👎👎👎👎👎")
                    print("Javobingiz noto'g'ri!")
                    # gap.say("fail")
                    # gap.runAndWait()
                    print(p.strip())
                    # gap.say(p)
                    # gap.runAndWait()
                    gap.say(i[0])
                    gap.runAndWait()
                    print("Keyingi savol!")
                    # gap.say("next")
                    # gap.runAndWait()
                lugat_aralash1.remove(p)




        notogrijavoblar2=[]
        notogrijavoblar3=[]
        togri2=0
        notogri2=0
        togri3=0
        notogri3=0
        Hamma="Hamma"
        while True:
            engoxirgijavob=input(f"{Hamma} lug'atlarni ko'rishni xoxlaysizmi(ha/yo'q):")
            # gap.say("Hamma lug'atlarni ko'rishni xoxlaysizmi")
            # gap.runAndWait()
            if engoxirgijavob=="ha":
                Hamma="Yana hamma"
                print("O'zbekchaga tarjima qiling?⏳")
                gap.say("O'zbekchaga tarjima qiling")
                gap.runAndWait()
                for oxirgi in lugat:
                    oxirgisiniki=oxirgi.split('-')
                    print(oxirgisiniki[0].strip())
                    gap.say(oxirgisiniki[0])
                    gap.runAndWait()
                    javobimiz=input("Javob⏳(❎ break):  ")
                    if javobimiz.strip().lower()==oxirgisiniki[1].strip().lower():
                        togri2+=1
                        subprocess.run('cls',shell=True)
                        print(togri2+notogri2,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        # gap.say("correct")
                        # gap.runAndWait()
                        print(oxirgi.strip())
                        # gap.say(oxirgi)
                        # gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        # gap.say("next")
                        # gap.runAndWait()
                    elif javobimiz=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar2)
                        print(togri2+notogri2," tadan ",togri2," ta tog'ri va ",notogri2," ta notog'ri.")
                        togsi=str(togri2+notogri2)
                        togsi2=str(togri2)
                        togsi3=str(notogri2)
                        gap.say(togsi+" tadan "+togsi2+" ta tog'ri va "+togsi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Endi inglizchaga tarjima qiling?⏳")
                        gap.say("Endi inglizchaga tarjima qiling")
                        gap.runAndWait()
                        break
                    else:
                        notogri2+=1
                        notogrijavoblar2.append(oxirgi.strip())
                        print(togri2+notogri2,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        # gap.say("fail")
                        # gap.runAndWait()
                        print(oxirgi.strip())
                        # gap.say(oxirgi)
                        # gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        # gap.say("next")
                        # gap.runAndWait()
                for yanoxir in lugat:
                    yanoxirgisi=yanoxir.split('-')
                    print(yanoxirgisi[1].strip())
                    gap.say(yanoxirgisi[1])
                    gap.runAndWait()
                    javoxir=input("Javob⏳(❎ break):  ")
                    if javoxir.strip().lower()==yanoxirgisi[0].strip().lower():
                        togri3+=1
                        subprocess.run('cls',shell=True)
                        print(togri3+notogri3,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        # gap.say("correct")
                        # gap.runAndWait()
                        print(yanoxir.strip())
                        # gap.say(yanoxir)
                        # gap.runAndWait()
                        gap.say(yanoxirgisi[0])
                        gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        # gap.say("next")
                        # gap.runAndWait()
                    elif javoxir=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar3)
                        print(togri3+notogri3," tadan ",togri3," ta tog'ri va ",notogri3," ta notog'ri.")
                        toghi=str(togri3+notogri3)
                        toghi2=str(togri3)
                        toghi3=str(notogri3)
                        gap.say(toghi+" tadan "+toghi2+" ta tog'ri va "+toghi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Davom etamiz!👍👍👍😁😁😁")
                        # gap.say("Davom etamiz")
                        # gap.runAndWait()
                        break
                    else:
                        notogri3+=1
                        notogrijavoblar3.append(yanoxir.strip())
                        print(togri3+notogri3,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        # gap.say("fail")
                        # gap.runAndWait()
                        print(yanoxir.strip())
                        # gap.say(yanoxir)
                        # gap.runAndWait()
                        gap.say(yanoxirgisi[0])
                        gap.runAndWait()
                        print("Keyingi savol!")
                        # gap.say("next")
                        # gap.runAndWait()
            elif engoxirgijavob=="yo'q":
                print("Sizning barcha xato javoblaringgiz: ",notogrijavoblar+notogrijavoblar1+notogrijavoblar2+notogrijavoblar3)
                print("Siz ",togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3," tadan ",togri+togri1+togri2+togri3," ta tog'ri va ",notogri+notogri1+notogri2+notogri3," ta notog'ri javob berdingiz!👍.")
                togli=str(togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3)
                togli2=str(togri+togri1+togri2+togri3)
                togli3=str(notogri+notogri1+notogri2+notogri3)
                gap.say("Siz "+togli+" tadan "+togli2+" ta tog'ri va "+togli3+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Davom etamiz!👍👍👍😁😁😁")

                # ####notog'ri javoblarni qaytadan ko'rishni boshlanishi.
                notogri_javoblarni_hammasi=list(dict.fromkeys(notogrijavoblar+notogrijavoblar1+notogrijavoblar2+notogrijavoblar3))
                # notogrijavoblar_t=[]
                Notogri="Noto'g'ri"
                while True:
                    lugat_aralash=notogri_javoblarni_hammasi[:]
                    lugat_aralash1=notogri_javoblarni_hammasi[:]
                    notogri_javob_t=input(f"{Notogri} javoblarni ko'rishni hohlaysizmi?(ha/yo'q):")
                    if(notogri_javob_t=="ha"):
                        Notogri="Yana noto'g'ri"
                        print("O'zbekchaga tarjima qiling?⏳")
                        gap.say("O'zbekchaga tarjima qiling")
                        gap.runAndWait()
                        notogrijavoblar_t=[]
                        togri=0
                        notogri=0

                        while True:
                            if lugat_aralash == []:
                                subprocess.run('cls',shell=True)
                                print("Bular noto'g'ri javoblar:",notogrijavoblar_t)
                                print(togri+notogri," tadan ",togri," ta tog'ri va ",notogri," ta notog'ri.")
                                jamida=str(togri+notogri)
                                tg=str(togri)
                                ntg=str(notogri)
                                gap.say(jamida+" " +"tadan "+tg+" ta tog'ri va "+ntg+" ta notog'ri javob berdingiz")
                                gap.runAndWait()
                                # notogri_javoblarni_hammasi=notogrijavoblar_t
                                break
                            else:
                                a=choice(lugat_aralash)
                                b=a.split('-')
                                print(b[0].strip())
                                gap.say(b[0])
                                gap.runAndWait()
                                javob=input("Javob⏳(❎ break):  ")
                                if javob.strip().lower()==b[1].strip().lower():
                                    togri+=1
                                    subprocess.run('cls',shell=True)
                                    print(togri+notogri,"✅👍👍👍👍👍👍👍👍👍")
                                    print("Javobingiz to'g'ri!")
                                    # gap.say("correct")
                                    # gap.runAndWait()
                                    print(a.strip())
                                    # gap.say(a)
                                    # gap.runAndWait()
                                    print("Keyingi savol❓❔❕❗↩️")
                                    # gap.say("next")
                                    # gap.runAndWait()
                                    # lugat_aralash.remove(a)###
                                elif javob=="break":
                                    subprocess.run('cls',shell=True)
                                    print("Bular noto'g'ri javoblar:",notogrijavoblar_t)
                                    print(togri+notogri," tadan ",togri," ta tog'ri va ",notogri," ta notog'ri.")
                                    jamida=str(togri+notogri)
                                    tg=str(togri)
                                    ntg=str(notogri)
                                    gap.say(jamida+" " +"tadan "+tg+" ta tog'ri va "+ntg+" ta notog'ri javob berdingiz")
                                    gap.runAndWait()
                                    print("Endi inglizchaga tarjima qiling?⏳")
                                    gap.say("Endi inglizchaga tarjima qiling")
                                    gap.runAndWait()
                                    # notogri_javoblarni_hammasi=notogrijavoblar_t
                                    break
                                else:
                                    notogri+=1
                                    notogrijavoblar_t.append(a.strip())
                                    print(togri+notogri,"❎👎👎👎👎👎👎👎👎")
                                    print("Javobingiz noto'g'ri!")
                                    # gap.say("fail")
                                    # gap.runAndWait()
                                    print(a.strip())
                                    # gap.say(a)
                                    # gap.runAndWait()
                                    print("Keyingi savol❓❔❕❗↩️")
                                    # gap.say("next")
                                    # gap.runAndWait()
                                lugat_aralash.remove(a)
                        notogrijavoblar1=[]
                        togri1=0
                        notogri1=0
                        # lugat_aralash1=notogri_javoblarni_hammasi[:]
                        while True:
                            if lugat_aralash1 == []:
                                subprocess.run('cls',shell=True)
                                print("Bular noto'g'ri javoblar:",notogrijavoblar1)
                                print(togri1+notogri1," tadan ",togri1," ta tog'ri va ",notogri1," ta notog'ri.")
                                togi=str(togri1+notogri1)
                                togi2=str(togri1)
                                togi3=str(notogri1)
                                gap.say(togi+" tadan "+togi2+" ta tog'ri va "+togi3+" ta notog'ri javob berdingiz")
                                gap.runAndWait()
                                print("Davom etamiz!👍👍👍😁😁😁")
                                # notogri_javoblarni_hammasi=list(dict.fromkeys(notogrijavoblar1+notogrijavoblar_t))
                                break
                            else:
                                p=choice(lugat_aralash1)
                                i=p.split('-')
                                print(i[1].strip())
                                gap.say(i[1])
                                gap.runAndWait()
                                jav=input("Javob⏳(❎ break):  ")
                                if jav.strip().lower()==i[0].strip().lower():
                                    togri1+=1
                                    subprocess.run('cls',shell=True)
                                    print(togri1+notogri1,"✅👍👍👍👍👍👍👍👍👍")
                                    print("Javobingiz to'g'ri!")
                                    # gap.say("correct")
                                    # gap.runAndWait()
                                    print(p.strip())
                                    # gap.say(p)
                                    # gap.runAndWait()
                                    gap.say(i[0])
                                    gap.runAndWait()
                                    print("Keyingi savol❓❔❕❗↩️")
                                    # gap.say("next")
                                    # gap.runAndWait()
                                    # lugat_aralash1.remove(p)
                                elif jav=="break":
                                    subprocess.run('cls',shell=True)
                                    print("Bular noto'g'ri javoblar:",notogrijavoblar1)
                                    print(togri1+notogri1," tadan ",togri1," ta tog'ri va ",notogri1," ta notog'ri.")
                                    togi=str(togri1+notogri1)
                                    togi2=str(togri1)
                                    togi3=str(notogri1)
                                    gap.say(togi+" tadan "+togi2+" ta tog'ri va "+togi3+" ta notog'ri javob berdingiz")
                                    gap.runAndWait()
                                    print("Davom etamiz!👍👍👍😁😁😁")
                                    # gap.say("Davom etamiz")
                                    # gap.runAndWait()
                                    # notogri_javoblarni_hammasi=list(dict.fromkeys(notogrijavoblar1+notogrijavoblar_t))
                                    break
                                else:
                                    notogri1+=1
                                    notogrijavoblar1.append(p.strip())
                                    print(togri1+notogri1,"❎👎👎👎👎👎👎👎👎")
                                    print("Javobingiz noto'g'ri!")
                                    # gap.say("fail")
                                    # gap.runAndWait()
                                    print(p.strip())
                                    # gap.say(p)
                                    # gap.runAndWait()
                                    gap.say(i[0])
                                    gap.runAndWait()
                                    print("Keyingi savol!")
                                    # gap.say("next")
                                    # gap.runAndWait()
                                lugat_aralash1.remove(p)
                            notogri_javoblarni_hammasi=list(dict.fromkeys(notogrijavoblar1+notogrijavoblar_t))
                    elif(notogri_javob_t=="yo'q"):
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogri_javoblarni_hammasi)
                        print(togri1+notogri1+togri+notogri," tadan ",togri1+togri," ta tog'ri va ",notogri1+notogri," ta notog'ri.")
                        togi=str(togri1+notogri1+togri+notogri)
                        togi2=str(togri1+togri)
                        togi3=str(notogri1+notogri)
                        gap.say(togi+" tadan "+togi2+" ta tog'ri va "+togi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Davom etamiz!👍👍👍😁😁😁")
                        # gap.say("Davom etamiz")
                        # gap.runAndWait()
                        print("Ishtirok etganingiz uchun katta raxmat!👍👍👍👍👍😁😁😁😁😁😁")
                        gap.say("Ishtirok etganingiz uchun katta raxmat")
                        gap.runAndWait()
                        break
                else:
                    print("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting!!!")
                break ###tursinchi
            else:
                print("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting!!!")
                # gap.say("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting")
                # gap.runAndWait()



######################################internetli#############################################

    elif sorash.strip().lower()=="internetli":
        print("O'zbekchaga tarjima qiling?⏳")
        gap.say("O'zbekchaga tarjima qiling")
        gap.runAndWait()
        notogrijavoblar=[]
        togri=0
        notogri=0
        while True:
            a=choice(lugat)
            b=a.split('-')
            print(b[0].strip())
            gap.say(b[0])
            gap.runAndWait()
            while True:
                r = sr.Recognizer()
                with sr.Microphone(device_index=1) as source:
                    audio=r.listen(source)
                javob=r.recognize_google(audio, language="uz-Uz")
                gap.say("Siz "+javob+" dedingizmi")
                with sr.Microphone(device_index=1) as source:
                    audio1=r.listen(source)
                tastiqjavob=r.recognize_google(audio1, language="uz-Uz")
                if tastiqjavob.lower()=="ha":
                    break
                elif tastiqjavob.lower()=="yo'q":
                    gap.say("qaytadan ayting")
                    continue
                else:
                    gap.say("qaytadan ayting")
                    continue
            if javob.strip().lower()==b[1].strip().lower():
                togri+=1
                subprocess.run('cls',shell=True)
                print(togri+notogri,"✅👍👍👍👍👍👍👍👍👍")
                print("Javobingiz to'g'ri!")
                gap.say("Javobingiz to'g'ri")
                gap.runAndWait()
                print(a.strip())
                gap.say(a)
                gap.runAndWait()
                print("Keyingi savol❓❔❕❗↩️")
                gap.say("Keyingi savol")
                gap.runAndWait()
            elif javob=="break":
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar)
                print(togri+notogri," tadan ",togri," ta tog'ri va ",notogri," ta notog'ri.")
                jamida=str(togri+notogri)
                tg=str(togri)
                ntg=str(notogri)
                gap.say(jamida+" " +"tadan "+tg+" ta tog'ri va "+ntg+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Endi inglizchaga tarjima qiling?⏳")
                gap.say("Endi inglizchaga tarjima qiling")
                gap.runAndWait()
                break
            else:
                notogri+=1
                notogrijavoblar.append(a.strip())
                print(togri+notogri,"❎👎👎👎👎👎👎👎👎")
                print("Javobingiz noto'g'ri!")
                gap.say("Javobingiz noto'g'ri")
                gap.runAndWait()
                print(a.strip())
                gap.say(a)
                gap.runAndWait()
                print("Keyingi savol❓❔❕❗↩️")
                gap.say("Keyingi savol")
                gap.runAndWait()
        notogrijavoblar1=[]
        togri1=0
        notogri1=0
        while True:
            p=choice(lugat)
            i=p.split('-')
            print(i[1].strip())
            gap.say(i[1])
            gap.runAndWait()
            while True:
                with sr.Microphone(device_index=1) as source: # r = sr.Recognizer()
                    audio2=r.listen(source)
                jav=r.recognize_google(audio2, language="eng-Eng")
                gap.say("Siz "+jav+" dedingizmi")
                with sr.Microphone(device_index=1) as source:
                    audio3=r.listen(source)
                tastiqjavob2=r.recognize_google(audio3, language="uz-Uz")
                if tastiqjavob2.lower()=="ha":
                    break
                elif tastiqjavob2.lower()=="yo'q":
                    gap.say("qaytadan ayting")
                    continue
                else:
                    gap.say("qaytadan ayting")
                    continue
            jav=input("Javob⏳(❎ break):  ")
            if jav.strip().lower()==i[0].strip().lower():
                togri1+=1
                subprocess.run('cls',shell=True)
                print(togri1+notogri1,"✅👍👍👍👍👍👍👍👍👍")
                print("Javobingiz to'g'ri!")
                gap.say("Javobingiz to'g'ri")
                gap.runAndWait()
                print(p.strip())
                gap.say(p)
                gap.runAndWait()
                print("Keyingi savol❓❔❕❗↩️")
                gap.say("Keyingi savol")
                gap.runAndWait()
            elif jav=="break":
                subprocess.run('cls',shell=True)
                print("Bular noto'g'ri javoblar:",notogrijavoblar1)
                print(togri1+notogri1," tadan ",togri1," ta tog'ri va ",notogri1," ta notog'ri.")
                togi=str(togri1+notogri1)
                togi2=str(togri1)
                togi3=str(notogri1)
                gap.say(togi+" tadan "+togi2+" ta tog'ri va "+togi3+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Davom etamiz!👍👍👍😁😁😁")
                gap.say("Davom etamiz")
                gap.runAndWait()
                break
            else:
                notogri1+=1
                notogrijavoblar1.append(p.strip())
                print(togri1+notogri1,"❎👎👎👎👎👎👎👎👎")
                print("Javobingiz noto'g'ri!")
                gap.say("Javobingiz noto'g'ri")
                gap.runAndWait()
                print(p.strip())
                gap.say(p)
                gap.runAndWait()
                print("Keyingi savol!")
                gap.say("Keyingi savol")
                gap.runAndWait()





        notogrijavoblar2=[]
        notogrijavoblar3=[]
        togri2=0
        notogri2=0
        togri3=0
        notogri3=0
        while True:
            engoxirgijavob=input("Hamma lug'atlarni ko'rishni xoxlaysizmi(ha/yo'q):")
            gap.say("Hamma lug'atlarni ko'rishni xoxlaysizmi")
            gap.runAndWait()
            if engoxirgijavob=="ha":
                print("O'zbekchaga tarjima qiling?⏳")
                gap.say("O'zbekchaga tarjima qiling")
                gap.runAndWait()
                for oxirgi in lugat:
                    oxirgisiniki=oxirgi.split('-')
                    print(oxirgisiniki[0].strip())
                    gap.say(oxirgisiniki[0])
                    gap.runAndWait()
                    while True:
                        with sr.Microphone(device_index=1) as source: # r = sr.Recognizer()
                            audio4=r.listen(source)
                        javobimiz=r.recognize_google(audio4, language="uz-Uz")
                        gap.say("Siz "+javobimiz+" dedingizmi")
                        with sr.Microphone(device_index=1) as source:
                            audio5=r.listen(source)
                        tastiqjavob3=r.recognize_google(audio5, language="uz-Uz")
                        if tastiqjavob3.lower()=="ha":
                            break
                        elif tastiqjavob3.lower()=="yo'q":
                            gap.say("qaytadan ayting")
                            continue
                        else:
                            gap.say("qaytadan ayting")
                            continue
                    if javobimiz.strip().lower()==oxirgisiniki[1].strip().lower():
                        togri2+=1
                        subprocess.run('cls',shell=True)
                        print(togri2+notogri2,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        gap.say("Javobingiz to'g'ri")
                        gap.runAndWait()
                        print(oxirgi.strip())
                        gap.say(oxirgi)
                        gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        gap.say("Keyingi savol")
                        gap.runAndWait()
                    elif javobimiz=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar2)
                        print(togri2+notogri2," tadan ",togri2," ta tog'ri va ",notogri2," ta notog'ri.")
                        togsi=str(togri2+notogri2)
                        togsi2=str(togri2)
                        togsi3=str(notogri2)
                        gap.say(togsi+" tadan "+togsi2+" ta tog'ri va "+togsi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Endi inglizchaga tarjima qiling?⏳")
                        gap.say("Endi inglizchaga tarjima qiling")
                        gap.runAndWait()
                        break
                    else:
                        notogri2+=1
                        notogrijavoblar2.append(oxirgi.strip())
                        print(togri2+notogri2,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        gap.say("Javobingiz noto'g'ri")
                        gap.runAndWait()
                        print(oxirgi.strip())
                        gap.say(oxirgi)
                        gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        gap.say("Keyingi savol")
                        gap.runAndWait()
                for yanoxir in lugat:
                    yanoxirgisi=yanoxir.split('-')
                    print(yanoxirgisi[1].strip())
                    gap.say(yanoxirgisi[1])
                    gap.runAndWait()
                    while True:
                        with sr.Microphone(device_index=1) as source: # r = sr.Recognizer()
                            audio6=r.listen(source)
                        javoxir=r.recognize_google(audio6, language="eng-Eng")
                        gap.say("Siz "+javoxir+" dedingizmi")
                        with sr.Microphone(device_index=1) as source:
                            audio7=r.listen(source)
                        tastiqjavob4=r.recognize_google(audio7, language="uz-Uz")
                        if tastiqjavob4.lower()=="ha":
                            break
                        elif tastiqjavob4.lower()=="yo'q":
                            gap.say("qaytadan ayting")
                            continue
                        else:
                            gap.say("qaytadan ayting")
                            continue
                    if javoxir.strip().lower()==yanoxirgisi[0].strip().lower():
                        togri3+=1
                        subprocess.run('cls',shell=True)
                        print(togri3+notogri3,"✅👍👍👍👍👍👍👍👍👍")
                        print("Javobingiz to'g'ri!")
                        gap.say("Javobingiz to'g'ri")
                        gap.runAndWait()
                        print(yanoxir.strip())
                        gap.say(yanoxir)
                        gap.runAndWait()
                        print("Keyingi savol❓❔❕❗↩️")
                        gap.say("Keyingi savol")
                        gap.runAndWait()
                    elif javoxir=="break":
                        subprocess.run('cls',shell=True)
                        print("Bular noto'g'ri javoblar:",notogrijavoblar3)
                        print(togri3+notogri3," tadan ",togri3," ta tog'ri va ",notogri3," ta notog'ri.")
                        toghi=str(togri3+notogri3)
                        toghi2=str(togri3)
                        toghi3=str(notogri3)
                        gap.say(toghi+" tadan "+toghi2+" ta tog'ri va "+toghi3+" ta notog'ri javob berdingiz")
                        gap.runAndWait()
                        print("Davom etamiz!👍👍👍😁😁😁")
                        gap.say("Davom etamiz")
                        gap.runAndWait()
                        break
                    else:
                        notogri3+=1
                        notogrijavoblar3.append(yanoxir.strip())
                        print(togri3+notogri3,"❎👎👎👎👎👎👎👎👎")
                        print("Javobingiz noto'g'ri!")
                        gap.say("Javobingiz noto'g'ri")
                        gap.runAndWait()
                        print(yanoxir.strip())
                        gap.say(yanoxir)
                        gap.runAndWait()
                        print("Keyingi savol!")
                        gap.say("Keyingi savol")
                        gap.runAndWait()
            elif engoxirgijavob=="yo'q":
                print("Sizning barcha xato javoblaringgiz: ",notogrijavoblar+notogrijavoblar1+notogrijavoblar2+notogrijavoblar3)
                print("Siz ",togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3," tadan ",togri+togri1+togri2+togri3," ta tog'ri va ",notogri+notogri1+notogri2+notogri3," ta notog'ri javob berdingiz!👍.")
                togli=str(togri+togri1+togri2+togri3+notogri+notogri1+notogri2+notogri3)
                togli2=str(togri+togri1+togri2+togri3)
                togli3=str(notogri+notogri1+notogri2+notogri3)
                gap.say("Siz "+togli+" tadan "+togli2+" ta tog'ri va "+togli3+" ta notog'ri javob berdingiz")
                gap.runAndWait()
                print("Ishtirok etganingiz uchun katta raxmat!👍👍👍👍👍😁😁😁😁😁😁")
                gap.say("Ishtirok etganingiz uchun katta raxmat")
                gap.runAndWait()
                break
            else:
                print("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting!!!")
                gap.say("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting")
                gap.runAndWait()
    else:
        print("Siz xato ma'lumot kiritdingiz, iltimos qaytadan kiriting!!!")
    break



##############kodni oxiri################
gap.runAndWait()