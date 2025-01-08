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




#################******1-100*******###############


                                    # "Afraid - qo'rqqan" ,
                                    # "Agree - rozi bo'lmoq" ,
                                    # "Angry - jahli chiqqan" ,
                                    # "Arrive - yetib kelmoq" ,
                                    # "Attack - hujum qilmoq" ,


                                    # "Bottom - pastki qism" ,
                                    # "Clever - aqilli" ,
                                    # "Cruel - berahm" ,
                                    # "Finally - vanihoyat",
                                    # "Hide - berkinmoq" ,


                                    # "Hunt - ov qilmoq" ,
                                    # "Lot - juda ko'p",
                                    # "Middle - o'rta" ,
                                    # "Moment - sekund" ,
                                    # "Pleased - mamnun" ,


                                    # "Promise - va'da bermoq",
                                    # "Reply - javob bermoq" ,
                                    # "Safe - xavfsiz" ,
                                    # "Trick - xiyla",
                                    # "Well - yaxshi" ,


                                    # "Let's go - qani ketdik",
                                    # "Me too - men ham",
                                    # "My name is - mening ismim",
                                    # "Never mind - hechqisi yo'q",
                                    # "Next time - keyingi safar",


                                    # "Nice to meet you - tanishganimdan hursandman",
                                    # "No problem - muammo yo'q",
                                    # "No, thank you - yo'q, rahmat",
                                    # "No way - bo'lishi mumkin emas",
                                    # "Not yet - hali emas",


                                    # "Nothing else - boshqa hech narsa",
                                    # "On the left - chapga",
                                    # "On the right - o'ngga",
                                    # "Over here - bu yerda",
                                    # "Over there - ana u yerda",



                                    # "Rise and shine - ko'tariling va porlang",
                                    # "See you later - Ko'rishguncha",
                                    # "See you soon - tez orada ko'rishguncha",
                                    # "because - chunki",
                                    # "as a result - Natijada",



                                    # "See you tomorrow - Ertaga ko'rishguncha",
                                    # "Shut up - Ovozingni o'chir",
                                    # "Sit down please - O'tiring marhamat",
                                    # "Stand back - Orqaga turing",
                                    # "Start the car - mashinani ishga tushuring",


                                    # "Step aside - Bir chetga o'ting",
                                    # "Take care - o'zingizni ehtiyot qiling",
                                    # "For example - Misol uchun",
                                    # "Therefore - shuning uchun",
                                    # "For this reason - shu sababli",


                                    # "tree - daraxt",
                                    # "rock - qoya",
                                    # "cloud - bulut",
                                    # "rainbow - kamalak",
                                    # "flower - gul",


                                    # "sun - quyosh",
                                    # "leaf - barg",
                                    # "beehive - asalari qutisi",
                                    # "grass - o't, maysa",
                                    # "moon - oy",

                                    # "river - daryo",
                                    # "star - yulduz",
                                    # "nest - uya, in",
                                    # "pinecone - qarag'ay g'uddasi",
                                    # "mountain - tog'",


                                    # "Channel - Kanal",
                                    # "Group - Guruh",
                                    # "Forward - Oldinga",
                                    # "Type - yozmoq, turi",
                                    # "Online - Internetga ulangan",


                                    # "Record voice - ovoz yozmoq",
                                    # "Send file - faylni yubormoq",
                                    # "Search - qidirmoq",
                                    # "Last seen at - da oxiri ko'rilgan",
                                    # "Last seen recently - yaqinda ko'rilgan",


                                    # "sky - osmon",
                                    # "Deleted account - o'chirilgan hisob ",
                                    # "Block - to'smoq",
                                    # "Join - qo'shilmoq",
                                    # "Leave - tark etmoq",


                                    # "Add - qo'shmoq",
                                    # "Members - a'zolar",
                                    # "Character - Xarakter",
                                    # "Arrogant - Kekkaygan, gerdaygan",
                                    # "Stubborn - O'jar, qaysar",


                                    # "Frank - Samimiy",
                                    # "Brusque - Qo'pol",
                                    # "Genius - Daho",
                                    # "Patient - Sabrli",
                                    # "Rude - yoqimsiz",


                                    # "Nice - yoqimli",
                                    # "Stupid - Ahmoq, tentak",
                                    # "Generous - Saxiy, saxovatli",
                                    # "Mad - Aqldan ozgan, jinni",
                                    # "Kind - Xushfe'l",


                                    # "achieve - erishmoq",
                                    # "brain - miya",
                                    # "concentrate - fikrni jamlamoq",
                                    # "consider - deb hisoblamoq",
                                    # "course - kurs",



###############*****100-200******##################


                                    # "degree - daraja",
                                    # "experience - tajriba",
                                    # "expert - o'z ishini ustasi",
                                    # "fail - muvaffaqiyatsizlikka uchramoq",
                                    # "guess - tahmin qilmoq",


                                    # "hesitate - ikkilanmoq",
                                    # "instruction - qo'llanma",
                                    # "make progress - yuksalmoq",
                                    # "make sure - ishonch hosil qilmoq",
                                    # "mark - baholamoq",


                                    # "mental - aqliy",
                                    # "pass - imtihondan o'tmoq",
                                    # "qualification - malaka",
                                    # "remind  - eslatmoq",
                                    # "report - hisob bermoq",


                                    # "revise - qaytadan ko'rib chiqmoq",
                                    # "search - qidirmoq",
                                    # "skill - mahorat",
                                    # "smart - aqilli",
                                    # "subject - fan",


                                    # "take an exam - imtihon topshirmoq",
                                    # "talented - talantli",
                                    # "term - termin",
                                    # "wonder - hayratlanmoq",
                                    # "pleasure - mamnun bo'lish",


                                    # "measure - o'lchamoq",
                                    # "happiness - baxt",
                                    # "simultaneous - bir vaqtda bo'lgan",
                                    # "destination - belgilangan joy",
                                    # "insatiable - ta'riflab bo'lmaydigan",


                                    # "rarely - kamdan kam",
                                    # "sure - albatta",
                                    # "would - bo'lardi",
                                    # "useful - foydali",
                                    # "order - buyurtma bermoq",


                                    # "paying - to'lash",
                                    # "exspressions - ifodalar",
                                    # "piece - bo'lak",
                                    # "glass - stakan",
                                    # "barbel - shtanga",


                                    # "slice - tilim, burda",
                                    # "adverb - ravish",
                                    # "frequency - tez tez takrorlanish",
                                    # "breakfast - nonushta",
                                    # "never - hech qachon",


                                    # "bracket - qavs",
                                    # "vocabulary - lug'at",
                                    # "vegetable - sabzavot",
                                    # "have - bor",
                                    # "certainly - shubhasiz",


                                    # "half - yarmi",
                                    # "past - o'tgan",
                                    # "quarter - chorak",
                                    # "pronunciation - talaffuz",
                                    # "marked - belgilangan",


                                    # "afternoon - tushdan keyin",
                                    # "boring - zerikarli",
                                    # "contraction - qisqarish",
                                    # "full - to'la",
                                    # "really - haqiqatdan ham",


                                    # "meal - ovqat",
                                    # "tense - zamon",
                                    # "present - hozir",
                                    # "simple - oddiy",
                                    # "positive - ijobiy",


                                    # "consonant - undosh",
                                    # "carry - olib yurish",
                                    # "cry - yig'lamoq",
                                    # "change - o'zgartirish",
                                    # "after - keyin",


                                    # "appendix - ilova",
                                    # "rule - qoida",
                                    # "give - berish",
                                    # "general - umumiy",
                                    # "description - tavsifi",


                                    # "activity - faollik",
                                    # "happen - sodir bo'lmoq",
                                    # "not - emas",
                                    # "know - bilish",
                                    # "want - istayman",


                                    # "accasionally - vaqti vaqti bilan",
                                    # "forget - unutmoq",
                                    # "diary - kundalik",
                                    # "south - janub",
                                    # "north - shimol",


                                    # "east - sharq",
                                    # "west - g'arb",
                                    # "most - eng",
                                    # "pepper - qalampir",
                                    # "tip - maslahat",


                                    # "them - ular",
                                    # "fridge - muzlatgich",
                                    # "freezer - muzlatgich",
                                    # "bin - quti",
                                    # "tap - jo'mrak",


                                    # "sink - rakovina",
                                    # "washing machine - kir yuvish mashinasi",
                                    # "microwave - mikroto'lqinli pech",
                                    # "cupboard - javon",
                                    # "shelf - tokcha",



###############*****200-300******##################


                                    # "worktop - ish stoli",
                                    # "dishwasher - idish yuvish mashinasi",
                                    # "frying pan - tova",
                                    # "cloth - mato",
                                    # "teapot - choynak",


                                    # "coffee maker - kofe qaynatgich",
                                    # "kitchen roll - oshxona ruloni",
                                    # "bowl - kosa",
                                    # "fork - sanchqi",
                                    # "knife - pichoq",


                                    # "chopsticks - tayoqchalar",
                                    # "spoon - qoshiq",
                                    # "mug - krujka",
                                    # "plate - likopcha",
                                    # "dry - quruq",


                                    # "stage - bosqich",
                                    # "thing - narsa",
                                    # "button - tugma",
                                    # "earphone - quloqchin",
                                    # "cover - qopqoq",


                                    # "low - past",
                                    # "make - qilmoq",
                                    # "male - erkak",
                                    # "natural - tabiy",
                                    # "new - yangi",


                                    # "old - eski",
                                    # "ordinary - oddiy",
                                    # "patterned - naqshli",
                                    # "plain - aniq",
                                    # "purple - siyohrang",


                                    # "scarf - sharf",
                                    # "sew - tikmoq",
                                    # "sewing machine - tikuv mashinasi",
                                    # "shirt - ko'ylak",
                                    # "similar - o'xshash",


                                    # "skirt - yubka",
                                    # "sock - paypoq",
                                    # "special - maxsus",
                                    # "terrible - dahshatli",
                                    # "tie - galstuk",


                                    # "tight - mustahkam",
                                    # "track suit - mashq qilish kiyimi",
                                    # "unhappy - baxtsiz",
                                    # "unkind - qo'pol",
                                    # "unnecessary - keraksiz",


                                    # "necessary - kerakli",
                                    # "untidy - tartibsiz",
                                    # "tidy - tartibli",
                                    # "violet - binafsha",
                                    # "wallet - hamyon",


                                    # "wrong - noto'g'ri",
                                    # "mistake - xato",
                                    # "beef - mol go'shti",
                                    # "chicken - tovuq",
                                    # "customer - xaridor, mijoz",


                                    # "fresh - toza",
                                    # "olive - zaytun",
                                    # "peas - no'xat",
                                    # "peasant - dehqon",
                                    # "prawn - krevetka",


                                    # "rubbish - chiqindi",
                                    # "rubbish bin - chiqindi qutisi",
                                    # "sausage - kolbasa",
                                    # "throw - otmoq",
                                    # "tray - patnis",


                                    # "waiter - ofitsiant",
                                    # "attractive - maftunkor",
                                    # "behind - orqasida",
                                    # "better - yaxshiroq",
                                    # "between - orasida, o'rtasida",


                                    # "busy - band",
                                    # "church - cherkov",
                                    # "cinema - kinoteatr",
                                    # "coach - murabbiy",
                                    # "crossroads - chorraha",


                                    # "crowd - olomon",
                                    # "dirty - kir",
                                    # "exciting - hayajonlantiruvchi",
                                    # "far - uzoq",
                                    # "field - dala, ekinzor",


                                    # "fire station - o't o'chiruvchilar stansiyasi",
                                    # "inside - ichida",
                                    # "front - oldingi qism",
                                    # "lake - ko'l",
                                    # "library - kutubxona",



                                    # "more - ko'proq",
                                    # "next - keyingi",
                                    # "noisy - shovqinli",
                                    # "opposite - ro'parada, qarshisida",
                                    # "outside - tashqarida",


                                    # "plane - tekislik",
                                    # "post office - pochta idorasi",
                                    # "post - ustun, tirgak",
                                    # "quiet - jimjit, tinch",
                                    # "traffic - yo'l transport harakati",


                                    # "ugly - xunuk, badbashara",
                                    # "under - tagiga, tagida",
                                    # "wood - yog'och, o'tin",
                                    # "across - ko'ndalangiga, eniga",
                                    # "along - yoqalab",



###############*****300-400******##################



                                    # "irregular - noto'g'ri, betartib",
                                    # "personal - shaxsiy",
                                    # "affirmative - bo'lishli",
                                    # "interrogative - so'roq",
                                    # "handle - tutqich",


                                    # "firefighter - o't o'chiruvchi",
                                    # "fill - to'ldirish",
                                    # "gap - oraliq",
                                    # "garden - bog'",
                                    # "clown - masxaraboz",


                                    # "cool - salqin, sovuq",
                                    # "lorry - yuk tashuvchi mashina",
                                    # "act - ish, harakat",
                                    # "then - so'ng, keyin",
                                    # "describe - tasvirlamoq",


                                    # "possessive - egalik",
                                    # "our - bizning",
                                    # "mine - meniki",
                                    # "case - hodisa, voqea",
                                    # "shampoo - shampun",


                                    # "tail - dum",
                                    # "whose - kimning",
                                    # "quilt - ko'rpa",
                                    # "pick - termoq",
                                    # "item - buyum",



                                    # "borrow - qarz olmoq",
                                    # "kill - o'ldirish",
                                    # "ride - haydamoq",
                                    # "walk - yurmoq",
                                    # "climb - yuqoriga chiqmoq, tirmashmoq",


                                    # "seek - izlamoq, qidirmoq",
                                    # "nail - mix, tirnoq",
                                    # "cycle - sykl, davr",
                                    # "scissors - qaychi",
                                    # "into - ichiga",


                                    # "crow - qarg'a",
                                    # "lone - yakka, yolg'iz",
                                    # "easier - sekinroq",
                                    # "fix - tuzatmoq",
                                    # "essential - muhim, ahamiyatli",


                                    # "pub - mayxona",
                                    # "nation - millat",
                                    # "anxious - xavotirlangan",
                                    # "awful - juda yomon",
                                    # "consist - iborat bo'lmoq",


                                    # "desire - xoxlamoq",
                                    # "eager - chanqoq, sabrsiz",
                                    # "household - oila a'zolar",
                                    # "intent - niyat, maqsad",
                                    # "landscape - landshaft, manzara",


                                    # "lift - ko'tarmoq",
                                    # "load - yuklamoq",
                                    # "lung - o'pka",
                                    # "motion - ishora, harakat",
                                    # "pace - temp, sur'at",


                                    # "polite - odobli, aql xushli",
                                    # "possess - egalik qilmoq",
                                    # "rapidly - juda tez",
                                    # "remark - ta'kidlamoq",
                                    # "trail - iz",


                                    # "shine - nur taratmoq",
                                    # "spill - to'kmoq",
                                    # "bring - olib kelmoq",
                                    # "castle - qasr, saroy",
                                    # "command - buyruq bermoq",


                                    # "counsel - maslahat bermoq",
                                    # "ensure - ta'minlamoq",
                                    # "explosion - portlash",
                                    # "jewelry - taqinchoq",
                                    # "land - qo'nmoq",


                                    # "meteor - meteorit",
                                    # "monster - mahluq",
                                    # "northern - shimoliy",
                                    # "remote - olis, uzoq",
                                    # "southern - janubiy",


                                    # "statue - haykal",
                                    # "steam - par, bug'",
                                    # "submit - bo'ysunmoq",
                                    # "temple - ibodatxona",
                                    # "upper - yuqori, ustki",


                                    # "weed - begona o't",
                                    # "wing - qanot",
                                    # "arrow - o'q, yoy",
                                    # "battle - urush",
                                    # "bow - kamon",


                                    # "brave - mard, jasur",
                                    # "chief - boshliq, sardor",
                                    # "disadvantage - kamchilik, nuqson",
                                    # "enemy - dushman",
                                    # "entrance - kirish yo'li",


                                    # "hardly - arang",
                                    # "intend - niyat qilmoq",
                                    # "laughter - kulgi",
                                    # "log - g'ola",
                                    # "military - armiya",


                                    # "obey - bo'ysunmoq",
                                    # "secure - xotirjam",
                                    # "steady - turg'un",
                                    # "trust - ishonch",
                                    # "twist - qayrilmoq",



################*****400-500******#################



                                    # "unless - magan taqdirda",
                                    # "weapon - qurol",
                                    # "pillow - yostiq",
                                    # "ceiling - shift",
                                    # "needle - igna",


                                    # "adventure - sarguzasht",
                                    # "approach - yaqinlashmoq",
                                    # "carefully - e'tibor bilan",
                                    # "chemical - kimyoviy",
                                    # "create - yasamoq",


                                    # "evil - yomon, yovuz",
                                    # "copper - qozon",
                                    # "loud - shovqinli, baland",
                                    # "nervous - xavotirlangan",
                                    # "noise - shovqin",


                                    # "scare - qo'rqitmoq",
                                    # "secret - sir",
                                    # "shout - baqirmoq",
                                    # "smell - hidlamoq",
                                    # "bucket - paqir",


                                    # "worse - yomonroq",
                                    # "alien - o'zga sayyoralik",
                                    # "among - orasida, ichida",
                                    # "chart - diagramma",
                                    # "comprehend - tushunmoq",


                                    # "ever - qachondir",
                                    # "grade - baho",
                                    # "instead - o'rniga",
                                    # "several - bir nechta",
                                    # "solve - javob topmoq",


                                    # "suddenly - to'sattan, birdaniga",
                                    # "suppose - mo'ljallamoq",
                                    # "universe - koinot",
                                    # "view - ko'rinish",
                                    # "appropriate - mos, muvofiq",


                                    # "avoid - yaqinlashmaslik",
                                    # "behave - odob saqlamoq",
                                    # "calm - xotirjam",
                                    # "concern - tashvish, g'am",
                                    # "content - xursand, shod",


                                    # "expect - kutmoq",
                                    # "habit - odat",
                                    # "jar - bonka",
                                    # "issue - muammo",
                                    # "none - hech qaysi",


                                    # "punish - jazolamoq",
                                    # "represent - vakil bo'lmoq",
                                    # "shake - silkitmoq",
                                    # "spread - tarqatmoq",
                                    # "stroll - sayr qilmoq",


                                    # "village - qishloq",
                                    # "aware - habardor, ogoh",
                                    # "belong - tegishli bo'lmoq",
                                    # "hurt - zarar yetkazmoq",
                                    # "judgment - qaror qabul qilmoq",



                                    # "likely - ehtimol, balki",
                                    # "relax - dam olmoq",
                                    # "request - so'ramoq",
                                    # "reside - istiqomat qilmoq",
                                    # "roll - yumalatmoq",


                                    # "since - dan beri",
                                    # "visible - ko'rinib turgan",
                                    # "wild - yovvoyi",
                                    # "advantage - ustunlik, afzallik",
                                    # "cause - sabab, asos",


                                    # "choice - tanlash imkoniyati",
                                    # "community - jamiyat, jamoa",
                                    # "dead - o'lgan, o'lik",
                                    # "distance - masofa",
                                    # "escape - qochib qutulmoq",


                                    # "face - yuzlanmoq",
                                    # "follow - ortidan bormoq",
                                    # "fright - qo'rquv, vahima",
                                    # "ghost - rux, arvox",
                                    # "individual - shaxs",


                                    # "pet - uy hayvoni",
                                    # "reach - yetib bormoq, erishmoq",
                                    # "return - qaytib kelmoq",
                                    # "survive - tirik qolmoq, omon qolmoq",
                                    # "upset - xafa, tushkun",


                                    # "wise - dono",
                                    # "allow - ruxsat bermoq",
                                    # "announce - e'lon qilmoq",
                                    # "beside - yonma yon",
                                    # "challenge - qiyinchilik",


                                    # "claim - tasdiqlamoq, talab qilmoq",
                                    # "condition - holat",
                                    # "contribute - xissa qo'shmoq",
                                    # "difference - farq",
                                    # "divide - taqsimlamoq",


                                    # "force - kuch, qudrat",
                                    # "harm - ziyon",
                                    # "lay - qo'ymoq",
                                    # "peace - tinchlik",
                                    # "prince - shahzoda",


                                    # "protect - himoya qilmoq",
                                    # "sense - sezmoq",
                                    # "wire - sim",
                                    # "accept - qabul qilmoq",
                                    # "arrange - tartibga solmoq",



############*****500-600******#####################


                                    # "attend - bormoq",
                                    # "balance - muvozanat saqlamoq",
                                    # "contrast - katta farq",
                                    # "encourage - ruhlantirmoq",
                                    # "familiar - tanish, qadirdon",


                                    # "grab - tortib olmoq",
                                    # "hang - osmoq",
                                    # "huge - ulkan",
                                    # "dough - xamir",
                                    # "propose - taklif qilmoq",


                                    # "purpose - maqsad",
                                    # "release - ozod qilmoq",
                                    # "require - talab qilmoq",
                                    # "single - bir dona",
                                    # "succes - muvaffaqiyat",


                                    # "tear - yirtmoq",
                                    # "theory - nazariya",
                                    # "against - qarama qarshi",
                                    # "damage - shikastlamoq",
                                    # "discover - kashf qilmoq",


                                    # "emotion - hissiyot",
                                    # "lock - qulf",
                                    # "identify - tanimoq",
                                    # "perhaps - ehtimol",
                                    # "pleasant - yoqimtoy",



                                    # "prevent - to'sqinlik qilmoq",
                                    # "save - saqlamoq",
                                    # "step - qadam tashlamoq",
                                    # "still - hali ham",
                                    # "taste - ta'm",


                                    # "chandelier - qandil",
                                    # "wave - to'lqin",
                                    # "benefit - foyda qilmoq",
                                    # "bud - kurtak",
                                    # "chance - imkoniyat",


                                    # "effect - amalga oshirmoq",
                                    # "iron - temir",
                                    # "focus - e'tibor markazi",
                                    # "guard - qo'riqlamoq",
                                    # "immediate - shoshilinch",


                                    # "primary - birinchi darajali",
                                    # "proud - mag'rur",
                                    # "remain - qolmoq",
                                    # "rest - dam olmoq",
                                    # "separate - alohida",


                                    # "site - joy",
                                    # "trouble - bezovta qilmoq",
                                    # "anymore - bundan keyin",
                                    # "berry - mayda meva",
                                    # "collect - to'plamoq",


                                    # "compete - musobaqalashmoq",
                                    # "creature - tirik mavjudot",
                                    # "decision - qaror",
                                    # "either - ikkisidan biri",
                                    # "introduce - tanishtirmoq",


                                    # "marry - turmush qurmoq",
                                    # "prepare - tayyorlamoq",
                                    # "sail - kemada suzmoq",
                                    # "serious - jiddiy",
                                    # "spend - sarflamoq",


                                    # "strange - g'alati",
                                    # "truth - haqiqat",
                                    # "wake - uyg'onmoq",
                                    # "bough - shox",
                                    # "article - maqola",


                                    # "attitude - munosabat",
                                    # "compare - solishtirmoq",
                                    # "judge - hakamlik qilmoq",
                                    # "profit - foyda",
                                    # "quality - sifat",


                                    # "shape - shakl",
                                    # "space - bo'sh joy",
                                    # "stair - zina",
                                    # "symbol - belgi",
                                    # "thin - ozg'in",


                                    # "blood - qon",
                                    # "burn - yondirmoq",
                                    # "cell - qamoq xonasi",
                                    # "contain - o'z ichiga olmoq",
                                    # "crop - hosil",


                                    # "demand - talab qilmoq",
                                    # "equal - teng",
                                    # "feed - ovqatlantirmoq",
                                    # "hole - teshik",
                                    # "increase - o'stirmoq",


                                    # "owe - qarzdor",
                                    # "raise - oshirish",
                                    # "responsible - mas'ul",
                                    # "sight - manzara",
                                    # "spot - dog'",


                                    # "structure - tuzulish",
                                    # "whole - to'la",
                                    # "floorboard - pol taxtasi",
                                    # "direct - to'g'ri",
                                    # "limit - meyor",


                                    # "local - mahalliy",
                                    # "magical - sehrli",
                                    # "mail - pochta",
                                    # "novel - roman",
                                    # "outline - reja",



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



##############******700-800*****###########***##########Ingliz tilida 1000 ta ot#############



                                    # "flashlight - fonar",
                                    # "history-tarix",
                                    # "way-yo'l",
                                    # "art-san'at",
                                    # "world-dunyo",


                                    # "information-ma'lumot",
                                    # "map-xarita",
                                    # "family-oila",
                                    # "government-hukumat",
                                    # "health-sog'lik",


                                    # "system-tizim",
                                    # "computer-kompyuter",
                                    # "meat-go'sht",
                                    # "year-yil",
                                    # "thanks-rahmat",


                                    # "music-musiqa",
                                    # "person-inson",
                                    # "read-o'qimoq",
                                    # "method-uslub",
                                    # "data-ma'lumot",


                                    # "food-ovqat",
                                    # "dream - orzu",
                                    # "target - maqsad",
                                    # "law-xuquq",
                                    # "bird-qush",


                                    # "literature-adabiyot",
                                    # "librarian - kutubxonachi",
                                    # "soft-yumshoq",
                                    # "control-nazorat",
                                    # "knowledge-bilim",


                                    # "power-kuch",
                                    # "ability-qobiliyat",
                                    # "economics-iqtisod",
                                    # "lie - yolg'on",
                                    # "deception - aldash",


                                    # "before - oldin",
                                    # "thread - ip",
                                    # "yarn - yigirilgan ip",
                                    # "nature-tabiat",
                                    # "fact-dalil",


                                    # "product-mahsulot",
                                    # "idea-g'oya",
                                    # "temperature-xarorat",
                                    # "invest-investitsiya",
                                    # "area-maydon",


                                    # "society-jamiyat",
                                    # "tow - tortmoq",
                                    # "however - ammo",
                                    # "industry-sanoat",
                                    # "media-axborot vositalari",


                                    # "dolour - g'am",
                                    # "diamond - olmos",
                                    # "luxury - hashamatli",
                                    # "definition-ta'rif",
                                    # "safety-xavfsizlik",


                                    # "insect - hashorot",
                                    # "development-rivojlanish",
                                    # "lately - oxirgi paytlarda",
                                    # "management-boshqaruv",
                                    # "always - har doim",


                                    # "phone-telefon",
                                    # "video-video",
                                    # "week-xafta",
                                    # "security-xavfsizlik",
                                    # "country-mamlakat",


                                    # "exam-imtixon",
                                    # "movie-film",
                                    # "organization-tashkilot",
                                    # "equipment-jixoz",
                                    # "physics-fizika",


                                    # "analysis-tahlil",
                                    # "policy-siyosat",
                                    # "series-qator",
                                    # "wall-devor",
                                    # "bee-asalari",


                                    # "boyfriend-sevgan yigit",
                                    # "direction-yo'nalish",
                                    # "strategy-usul",
                                    # "technology-texnalogiya",
                                    # "army-armiya",


                                    # "camera-kamera",
                                    # "freedom-ozodlik",
                                    # "paper-qog'oz",
                                    # "environment-atrof muhit",
                                    # "child-bola",


                                    # "instance-namuna",
                                    # "month-oy",
                                    # "truth-xaqiqat",
                                    # "marketing-savdo",
                                    # "university-universitet",


                                    # "writing-yozish",
                                    # "sentence - gap",
                                    # "doll-qo'g'irchoq",
                                    # "cement - sement",
                                    # "goal-maqsad",


                                    # "news-yangilik",
                                    # "audience-tinglovchi",
                                    # "fishing-baliq ovlash",
                                    # "growth-o'sish",
                                    # "income-daromad",



#############*****800-900******####################



                                    # "marriage-nikoh",
                                    # "user-foydalanuvchi",
                                    # "combination-kombinatsiya",
                                    # "failure-muvaffaqiyatsizlik",
                                    # "meaning-ma'no",


                                    # "medicine-tibbiyot",
                                    # "philosophy-falsafa",
                                    # "loser - mag'lub",
                                    # "communication-aloqa",
                                    # "night-tun",


                                    # "chemistry-kimyo",
                                    # "disease-kasallik ",
                                    # "gear - mexanizm",
                                    # "energy-quvvat",
                                    # "nation-millat",


                                    # "road-yo'l",
                                    # "role-rol",
                                    # "soup-sovun",
                                    # "advertising-reklama",
                                    # "location-manzil",


                                    # "success-muvaffaqiyat",
                                    # "addition-qo'shish",
                                    # "apartment-turar joy",
                                    # "education-ta'lim",
                                    # "math-matematika",


                                    # "acridity - qo'pol",
                                    # "painting-rasm",
                                    # "politics-siyosat",
                                    # "attention-diqqat",
                                    # "event-hodisa",


                                    # "property-mulk",
                                    # "shopping-xarid",
                                    # "mesh - setka",
                                    # "net - to'r",
                                    # "competition-musobaqa",


                                    # "distribution-taqsimlash",
                                    # "entertainment-ko'ngilochar",
                                    # "office-idora",
                                    # "population-aholi",
                                    # "president-prezident",


                                    # "unit-qism",
                                    # "category-toifa",
                                    # "cigarette-sigareta",
                                    # "context-vaziyat",
                                    # "pray - ibodat qilmoq",


                                    # "opportunity-imkoniyat",
                                    # "performance-bajarish",
                                    # "flight-jang",
                                    # "length-uzunlik",
                                    # "magazine-jurnal",


                                    # "newspaper-gazeta",
                                    # "relationship-qarindoshchilik",
                                    # "teaching-o'qitish",
                                    # "cell-hujayra",
                                    # "dealer-olibsotar",


                                    # "sandal - shippak",
                                    # "appearance-qiyofa",
                                    # "association-birlashma",
                                    # "concept-tushuncha",
                                    # "bailer - cho'mich",


                                    # "death-o'lim",
                                    # "discussion-muhokama",
                                    # "tureen - tovoq",
                                    # "inflation-inflyatsiya",
                                    # "insurance-sug'urta",


                                    # "mood-kayfiyat",
                                    # "woman-ayol",
                                    # "advice-maslahat",
                                    # "lead - qo'rg'oshin",
                                    # "effort-harakat qilish",


                                    # "expression-ifoda",
                                    # "importance-muhimlik",
                                    # "opinion-fikr",
                                    # "payment-to'lov",
                                    # "reality-haqiqat",


                                    # "responsibility-mas'uliyat",
                                    # "situation-vaziyat",
                                    # "husk - qobiq",
                                    # "statement-bayonot",
                                    # "contradictory - qarama qarshi",


                                    # "application-ariza",
                                    # "city-shahar",
                                    # "chew - chaynamoq",
                                    # "depth-chuqur",
                                    # "estate-mulk",


                                    # "foundation-poydevor",
                                    # "grandmother-buvi",
                                    # "heart-yurak",
                                    # "perspective-istiqbol",
                                    # "photo-surat",


                                    # "recipe-retsept ",
                                    # "studio-studiya",
                                    # "topic - mavzu",
                                    # "lection-leksiya",
                                    # "depression-depressiya",


                                    # "mutton - qo'y go'shti",
                                    # "bare - yalang'och",
                                    # "seed - urug'",
                                    # "sort - tur",
                                    # "pot - qozon",



##############******900-1000*****##################


                                    # "imagination-tasavvur",
                                    # "passion-ehtiros",
                                    # "percentage-foiz",
                                    # "resource-manba",
                                    # "setting-sozlama ",


                                    # "advertisement-reklama",
                                    # "agency-agentlik",
                                    # "college-kollej",
                                    # "connection-aloqa",
                                    # "criticism-tanqid",


                                    # "debt-qarz",
                                    # "thorn - tikan",
                                    # "memory-xotira",
                                    # "patience-sabr",
                                    # "secretary-kotib",


                                    # "solution-yechim",
                                    # "administration-ma'muriyat",
                                    # "aspect-ko'rinish",
                                    # "dust - chang",
                                    # "clay -  loy",


                                    # "personality-shaxs",
                                    # "psychology-psixologiya",
                                    # "recommendation-tavsiya",
                                    # "response-javob",
                                    # "selection-tanlash",


                                    # "storage-saqlash",
                                    # "version-variant",
                                    # "alcohol-alkogol",
                                    # "argument-bahs",
                                    # "complaint-shikoyat",


                                    # "contract-shartnoma",
                                    # "emphasis-urg'u",
                                    # "highway-katta yo'l",
                                    # "loss-yo'qotish",
                                    # "membership-a'zolik",


                                    # "preparation-tayyorgarlik",
                                    # "steak-steyk",
                                    # "union-birlashma",
                                    # "agreement-bitim",
                                    # "cancer-saraton",


                                    # "currency-valyuta",
                                    # "employment-xizmat",
                                    # "engineering-muhandislik",
                                    # "entry-kirish",
                                    # "interaction-o'zaro ta'sir",


                                    # "mixture-aralashma",
                                    # "preference-afzal",
                                    # "region-hudud",
                                    # "respublic-respublika",
                                    # "tradition-an'ana",


                                    # "virus-virus",
                                    # "actor-aktyor",
                                    # "classroom-sinfxona",
                                    # "delivery-yetkazib berish",
                                    # "device-qurilma",


                                    # "difficulty-qiyinchilik",
                                    # "drama-drama",
                                    # "election-saylov",
                                    # "engine-dvigatel",
                                    # "vein - tomir",


                                    # "guidance-hidoyat",
                                    # "hotel-mehmonxona",
                                    # "owner-egasi",
                                    # "priority-ustuvorlik",
                                    # "protection-himoya",


                                    # "suggestion-taklif",
                                    # "tension-kuchlanish",
                                    # "variation-o'zgarish",
                                    # "anxiety-bezovtalik",
                                    # "atmosphere-atmosfera",


                                    # "awareness-habardorlik",
                                    # "bath-hammom",
                                    # "bread-non",
                                    # "candidate-nomzod",
                                    # "climate-iqlim",


                                    # "comparison-qiyoslash",
                                    # "confusion-tartibsizlik",
                                    # "construction-qurilish",
                                    # "elevator-lift",
                                    # "soil - tuproq",


                                    # "employee-xodim",
                                    # "employer-ish beruvchi",
                                    # "guest-mehmon",
                                    # "height-balandlik",
                                    # "leadership-rahbarlik",


                                    # "poplar - terak",
                                    # "manager-rahbar",
                                    # "operation-operatsiya",
                                    # "recording-yozuv",
                                    # "sample-namuna",


                                    # "transportation-tashish",
                                    # "charity-xayriya",
                                    # "cousin-bo'la",
                                    # "disaster-musibat",
                                    # "editor-muharrir",


                                    # "efficiency-samaradorlik",
                                    # "excitement-hayajonlanish",
                                    # "extent-daraja",
                                    # "feedback-fikr",
                                    # "guitar-gitara",



############*****1000-1100******##################



                                    # "homework-uy vazifasi",
                                    # "leader-yetakchi ",
                                    # "mom-ona",
                                    # "outcome-natija",
                                    # "permission-ruxsat",


                                    # "presentation-taqdimot",
                                    # "promotion-rag'batlantirish",
                                    # "prayer - ibodat qiluvchi",
                                    # "refrigerator-muzlatgich",
                                    # "navel - kindik",


                                    # "revenue-daromad",
                                    # "session-sessiya",
                                    # "singer-qo'shiqchi",
                                    # "tennis-tennis ",
                                    # "basket-savat",


                                    # "bonus-mukofot",
                                    # "cabinet-kabinet",
                                    # "childhood-bolalik",
                                    # "tile - kafel",
                                    # "skimmer - kapgir",


                                    # "skin - teri",
                                    # "dinner-kechki ovqat",
                                    # "drawing-chizma",
                                    # "hair-soch",
                                    # "hearing-eshitish",


                                    # "initiative-tashabbus",
                                    # "propeller - parrak",
                                    # "lid - qopqoq",
                                    # "dabby - ho'l",
                                    # "mode-tur",


                                    # "mud-loy",
                                    # "orange-apelsin",
                                    # "poetry-she'riyat ",
                                    # "police-politsiya",
                                    # "possibility-ehtimol",


                                    # "procedure-tartib",
                                    # "queen-malika",
                                    # "ratio-nisbat",
                                    # "relation-munosabat",
                                    # "dear-qadrdon",


                                    # "satisfaction-qoniqish",
                                    # "female-ayol",
                                    # "signature-imzo",
                                    # "significance-ahamiyat",
                                    # "song-qo'shiq",


                                    # "tooth-tish",
                                    # "town-shaxar",
                                    # "vehicle-transport vositasi",
                                    # "volume-ovoz",
                                    # "wife-xotin",


                                    # "hurry-shoshilish",
                                    # "appointment-tayinlash",
                                    # "leotard - triko",
                                    # "assumption-faraz ",
                                    # "content - tarkib",


                                    # "chapter-bob",
                                    # "committee-qo'mita",
                                    # "conversation-suhbat",
                                    # "database-ma'lumotlar bazasi",
                                    # "enthusiasm-ishtiyoq",


                                    # "error-xato",
                                    # "explanation-tushuntirish",
                                    # "word-so'z",
                                    # "gate-darvoza",
                                    # "girl-qiz",


                                    # "hall-zal",
                                    # "murder - qotillik",
                                    # "hospital-kasalxona",
                                    # "injury-jarohat",
                                    # "hammer - bolg'a",


                                    # "punch-musht",
                                    # "saw - arra",
                                    # "almond - bodom",
                                    # "perception-idrok",
                                    # "pie-pirog",


                                    # "poem - she'r",
                                    # "tear - ko'z yoshi",
                                    # "peach - shaftoli",
                                    # "reception - qabul",
                                    # "charge - zaryad",


                                    # "revolution-inqilob",
                                    # "fauces - halqum",
                                    # "son-o'g'il",
                                    # "speech-nutq",
                                    # "salt cellar - tuzdon",


                                    # "above - tepasida",
                                    # "warning-ogohlantirish",
                                    # "winner-g'olib",
                                    # "absent - kelmagan",
                                    # "absorb - so'rmoq",


                                    # "assistance-yordamchi",
                                    # "accompany - hamroh",
                                    # "buyer-xaridor ",
                                    # "chest-ko'krak",
                                    # "according - ga ko'ra",


                                    # "conclusion-xulosa",
                                    # "accuracy - aniqlik",
                                    # "courage-jasurlik",
                                    # "achievment - yutuq",
                                    # "desk- parta",



############*****1100-1200******##################


                                    # "drawer-tortma",
                                    # "establishment-muassasa",
                                    # "action - harakat",
                                    # "garbage-axlat",
                                    # "honey-asal",


                                    # "impression-taassurot",
                                    # "improvement-takomillashtirish",
                                    # "insect-hashorat",
                                    # "inspection-tekshirish",
                                    # "king-qirol",


                                    # "ladder-narvon",
                                    # "profession-kasb",
                                    # "quantity-miqdor",
                                    # "reaction-reaksiya",
                                    # "requirement-talab",


                                    # "tongue-til",
                                    # "weakness-zaiflik",
                                    # "wedding-to'y",
                                    # "affair-ish",
                                    # "ambition-shuhratparastlik",


                                    # "assignment-topshiriq",
                                    # "independence-mustaqillik",
                                    # "celebration-nishonlash",
                                    # "curtain-parda",
                                    # "diamond-olmos",


                                    # "dirt-kir",
                                    # "ear-quloq",
                                    # "fortune-omad",
                                    # "friendship-do'stlik",
                                    # "hat-shlyapa",


                                    # "gene-gen",
                                    # "girlfriend-sevgan qiz",
                                    # "indication-ko'rsatma",
                                    # "intention-niyat",
                                    # "lady-xonim",


                                    # "negotiation-muzokara",
                                    # "obligation-majburiyat",
                                    # "passenger-yo'lovchi",
                                    # "pizza-pitsa",
                                    # "platform-platforma",


                                    # "pollution-ifloslanish",
                                    # "recognition-tan olish",
                                    # "reputation-obro'",
                                    # "shirt-ko'ylak",
                                    # "speaker-notiq",


                                    # "stranger-begona",
                                    # "surgery-jarrohlik",
                                    # "sympathy-hamdardlik",
                                    # "rat-kalamush ",
                                    # "trainer-murabbiy",


                                    # "uncle-tog'a",
                                    # "youth-yoshlar",
                                    # "time-vaqt",
                                    # "tale-ertak",
                                    # "water-suv",


                                    # "money-pul",
                                    # "example-misol",
                                    # "while-paytda",
                                    # "game-o'yin",
                                    # "life-hayot",


                                    # "form-shakl",
                                    # "air-xavo ",
                                    # "day-kun",
                                    # "place-joy",
                                    # "part-qism",


                                    # "partake - tanovul",
                                    # "headdress-bosh kiyimi",
                                    # "back-orqa",
                                    # "process - jarayon",
                                    # "heat-issiqlik",


                                    # "headiness-qattiqligicha",
                                    # "headlines -sarlavhalari",
                                    # "endeavour -urinmoq",
                                    # "catharsis-yengillashish ",
                                    # "end-oxir",


                                    # "fabricating - soxtalashtirish",
                                    # "fabricator -uydirma",
                                    # "dactylogram -barmoq izi",
                                    # "economy-iqtisod",
                                    # "face card-suratli qarta",


                                    # "body -tana",
                                    # "market-bozor",
                                    # "guide-git",
                                    # "interest-qiziqish",
                                    # "state-davlat ",


                                    # "facer - zarba",
                                    # "company-kompaniya",
                                    # "price-narx",
                                    # "mind-aql",
                                    # "trade-savdo",


                                    # "care-g'amxo'rlik",
                                    # "group-guruh",
                                    # "top-baland",
                                    # "amount-summa",
                                    # "level-daraja",


                                    # "gears - tishli ",
                                    # "practice-mashq",
                                    # "research-tadqiqot",
                                    # "sense-xis",
                                    # "service-xizmat",



##############******1200-1300*****##################



                                    # "boss-boss",
                                    # "fun-qiziqarli",
                                    # "page-bet",
                                    # "term-muddat",
                                    # "sound-tovush",


                                    # "matter-masala",
                                    # "kind-tur",
                                    # "board-taxta",
                                    # "oil-yog'",
                                    # "access-kirish",


                                    # "rope-arqon",
                                    # "rate-tarif",
                                    # "reason-sabab ",
                                    # "future-kelajak",
                                    # "site-sayt",


                                    # "gracious-xushfe'l",
                                    # "image-rasm",
                                    # "coast-qirg'oq",
                                    # "section-bo'lim",
                                    # "building-bino",


                                    # "cash-naqt pul",
                                    # "nothing-xech narsa",
                                    # "period-davr",
                                    # "plan-reja",
                                    # "side-tomon ",


                                    # "stock-aksiya",
                                    # "weather-ob xavo",
                                    # "figure-figura",
                                    # "model-model",
                                    # "source-manba",


                                    # "earth-yer",
                                    # "beginning-boshlanish",
                                    # "chicken-jo'ja",
                                    # "feature-xususiyat",
                                    # "material-material",


                                    # "question-savol",
                                    # "daedalian - qo'shma",
                                    # "object-obekt",
                                    # "scale -masshtab",
                                    # "style -uslub",


                                    # "war-urush",
                                    # "outside-tashqarida",
                                    # "standard-standart",
                                    # "exchange-almashish",
                                    # "fire-olov",


                                    # "pressure-bosim",
                                    # "frame-ramka",
                                    # "cycle-aylana ",
                                    # "paint-bo'yoq",
                                    # "review-ko'rib chiqish",


                                    # "screen-ekran",
                                    # "structure-tuzilma",
                                    # "ball-to'p",
                                    # "discipline-intizom",
                                    # "medium-o'rtacha",


                                    # "share-baxam ko'rish",
                                    # "gift-sovg'a",
                                    # "impact-zarba ",
                                    # "tool-asbob",
                                    # "wind-shamol",


                                    # "average-o'rtacha",
                                    # "career-martaba ",
                                    # "culture-madaniyat",
                                    # "signtable-imzolanishi",
                                    # "task-topshiriq",


                                    # "hope-umid",
                                    # "network-tarmoq",
                                    # "square-kvadrat",
                                    # "attempt-urinish",
                                    # "effect-amalga oshirmoq",


                                    # "link-aloqa",
                                    # "TV-televizor",
                                    # "capital-poytaxt",
                                    # "keyboard-klaviatura",
                                    # "shot-otish",


                                    # "brush-cho'tka",
                                    # "couple-juftlik",
                                    # "debate-munozara",
                                    # "chargers-zaryadlovchi",
                                    # "function-funksiya",


                                    # "lack-yetishmovchilik",
                                    # "plant-o'simlik ",
                                    # "summer-yoz",
                                    # "theme-mavzu",
                                    # "truck-yuk mashinasi",


                                    # "click-qarsillatmoq",
                                    # "transparent-shaffof",
                                    # "foot-oyoq",
                                    # "influence-tasir",
                                    # "notice-bildirishnoma",


                                    # "rain-yomg'ir",
                                    # "base-asos",
                                    # "feeling-sezgir",
                                    # "pair-juft",
                                    # "saving-tejash",


                                    # "staff-xodim",
                                    # "sugar-shakar",
                                    # "target-maqsad",
                                    # "animal-hayvon",
                                    # "author-muallif",


# ##############******1300-1400*****##################

                                    # "lecture-leksiya",
                                    # "partner-sherik",
                                    # "respect-xurmat",
                                    # "rice-guruch",
                                    # "routine-muntazam",


                                    # "register-ro'yxat qilmoq",
                                    # "sky-osmon",
                                    # "stick-tayoq",
                                    # "title-sarlavha",
                                    # "torch - mash'al",


                                    # "bridge - ko'prik",
                                    # "tyre - balon",
                                    # "character-xarakter",
                                    # "evidence-dalil",
                                    # "fan-fanat",


                                    # "brook - ariqcha",
                                    # "maximum-maksimum",
                                    # "option-variant",
                                    # "pack-paket",
                                    # "gutter-tarnov",


                                    # "background-fon ",
                                    # "dish-idish",
                                    # "factor-omil",
                                    # "joint-qo'shma",
                                    # "master-usta",


                                    # "muscle-mushak",
                                    # "strength-kuch",
                                    # "gnat - chivin",
                                    # "trip-sayoxat",
                                    # "appeal-murojat",


                                    # "land-yer",
                                    # "party-bazm",
                                    # "principle-tamoyil",
                                    # "relative-qarindosh",
                                    # "salary-maosh",


                                    # "season-mavsum",
                                    # "signal-signal ",
                                    # "spirit-ruhlantirmoq",
                                    # "street-ko'cha",
                                    # "Workshop-ustaxona ",


                                    # "drop-tomchi",
                                    # "minimum-minimal",
                                    # "path-yo'l",
                                    # "project-loyiha",
                                    # "sea-dengiz",


                                    # "commission-komissiya",
                                    # "status-xolat",
                                    # "conversion - aylantirish",
                                    # "ticket-bilet",
                                    # "tour-sayoxat",


                                    # "angel-farishta",
                                    # "daughter-qiz",
                                    # "dot-nuqta",
                                    # "duty-burch",
                                    # "father-ota",


                                    # "fee-choy puli",
                                    # "finance-moliya",
                                    # "hour-soat",
                                    # "drug - dori",
                                    # "within - ichida",


                                    # "luck-omad",
                                    # "confidence-ishonch",
                                    # "mouth-og'iz",
                                    # "pipe-quvur",
                                    # "seat-o'rindiq",


                                    # "stable-barqaror",
                                    # "storm-bo'ron",
                                    # "substance-modda",
                                    # "team-jamoa",
                                    # "napkin - salfetka",


                                    # "beach-plyaj ",
                                    # "blank-bo'sh",
                                    # "catch-tutmoq ",
                                    # "scroll - aylantirish",
                                    # "interview-intervyu",


                                    # "brake - tormoz",
                                    # "match-moslik",
                                    # "mission-missiya",
                                    # "pain-og'riq",
                                    # "rosary - tasbeh",


                                    # "score-hisob",
                                    # "chair-kursi",
                                    # "contest-tanlov",
                                    # "shower-dush",
                                    # "suit-kostyum",


                                    # "paltry-arzimas",
                                    # "perfect-mukammal",
                                    # "tacit-sokin",
                                    # "mere-oddiy",
                                    # "decorous-bezakli",


                                    # "corner-burchak",
                                    # "court-sud",
                                    # "district-tuman",
                                    # "discount-chegirma",
                                    # "finger-barmoq",


                                    # "guarantee-kafolat",
                                    # "mosque-masjid",
                                    # "hook-ilgak",
                                    # "implement-amalga oshirish",
                                    # "layer-qatlam",


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



##############******1500-1600*****##################



                                    # "",
                                    # "",
                                    # "neck-bo'yin",
                                    # "pension-pensiya",
                                    # "",


                                    # "ship-kema",
                                    # "",
                                    # "snow-qor",
                                    # "specialist-mutaxasis",
                                    # "stroke-zarba",


                                    # "trash-axlat ",
                                    # "fox-tulki",
                                    # "zone-hudud",
                                    # "anger-g'azab",
                                    # "award-mukofot ",


                                    # "",
                                    # "bitter-achchiq",
                                    # "",
                                    # "camp-oromgox",
                                    # "candy-konfet",


                                    # "",
                                    # "",
                                    # "clock-soat",
                                    # "comfort-qulay",
                                    # "",


                                    # "crack-yoriq",
                                    # "engineer-muhaddis",
                                    # "",
                                    # "fault-xato",
                                    # "",


                                    # "highlight-takidlash",
                                    # "incident-voqea",
                                    # "island-orol",
                                    # "joke-hazil",
                                    # "jury-hakam",


                                    # "",
                                    # "lip-lab",
                                    # "mate-do'st",
                                    # "motor-motor",
                                    # "nerve-asab",


                                    # "passage-o'tish",
                                    # "pride-g'urur",
                                    # "priest-ruhoniy ",
                                    # "prize-mukofot",
                                    # "resident-rezident ",


                                    # "ring-sirg'a",
                                    # "resort-kurort",
                                    # "",
                                    # "sail-yelkan",
                                    # "scheme-sxema",


                                    # "",
                                    # "station-bekat ",
                                    # "tower-minora",
                                    # "",
                                    # "witness-guvox",


                                    # "nature-tabiat",
                                    # "good-maxsulot",
                                    # "human-inson",
                                    # "tonight-kecha",
                                    # "",


                                    # "unequaled-tengsiz",
                                    # "inconclusive-noaniq",
                                    # "yielding-xosil beruvchi",
                                    # "slippery-sirg'anchiq",
                                    # "agitated-xayajonlangan",


                                    # "debonair-yomon",
                                    # "icy-muzli",
                                    # "madly-aqldan ozgan",
                                    # "scarce-kam",
                                    # "magenta-mjenta",


                                    # "abortive-muvaffaquyatsiz",
                                    # "absorbing-singdiruvchi",
                                    # "sweet-shirin",
                                    # "longing-sog'inish",
                                    # "able-qodir",


                                    # "rambunctious-shovshuvli",
                                    # "macabre-daxshatli",
                                    # "natural-tabiy",
                                    # "ready-tayyor",
                                    # "acoustic-tovush qay-gan",


                                    # "mighty-qudratli",
                                    # "disgusted-jirkanch",
                                    # "bulky-katta",
                                    # "bumpy-g'alati",
                                    # "mean-ma'no bildirmoq",


                                    # "young-yosh",
                                    # "narrow-tor",
                                    # "painstaking-mashaqqatli",
                                    # "shaky-titroqli",
                                    # "sour-nordon",


                                    # "ceaseless-tinimsiz",
                                    # "nauseating-ko'ngil aynitadigan",
                                    # "frantic-g'azablangan",
                                    # "pale-rangbarang",
                                    # "appalling-daxshatli",


                                    # "delicious-mazali",
                                    # "smoggy-tutunli",
                                    # "regular-muntazam",
                                    # "living-jonli",
                                    # "adventurous-Sarguzashtli",



############Ingliz tilida 1000 ta sifat################
##############******1600-1700*****##################



                                    # "witty-aqilli",
                                    # "majestic-ulug'vor",
                                    # "tart-buzuq",
                                    # "deranged-aqildan ozdiradigan",
                                    # "warlike-jangovar",


                                    # "far-flung-uzoq",
                                    # "noxious-zararli",
                                    # "malicious-zararli",
                                    # "heady-boshli",
                                    # "lonely-yolg'iz",


                                    # "murky-xira",
                                    # "whole-butun",
                                    # "naughty-yaramas",
                                    # "past-o'tgan",
                                    # "organic-organik",


                                    # "internal-ichki",
                                    # "few-oz",
                                    # "concerned-tashvishli",
                                    # "complete-to'liq",
                                    # "grotesque-krotesk",


                                    # "illegal-noqonuniy",
                                    # "bad-yomon",
                                    # "bawdy-beadab",
                                    # "distinct-aloxida",
                                    # "gritty-jasur",


                                    # "cumbersome-og'ir",
                                    # "unnatural-notabiy",
                                    # "tricky-ayyor",
                                    # "likeable-yoqimli",
                                    # "dizzy-bosh aylanish",


                                    # "vigorous-kuchli",
                                    # "bent-egilgan",
                                    # "observant-kuzatuvchan",
                                    # "best-eng yaxshi",
                                    # "hypnotic-gipnoz",


                                    # "messy-tartibsiz",
                                    # "exhilarated-xayajonli",
                                    # "depraved-buzuq",
                                    # "noisy-shovqinli",
                                    # "dull-zerikarli",


                                    # "whopping-ajoyib",
                                    # "second-ikkinchi",
                                    # "efficient-samarali",
                                    # "testy-mazali",
                                    # "vulgar-qo'pol",
                                    # "well-off-taniqli",
                                    # "pastoral-chorvachilik",
                                    # "irritable-asabit",
                                    # "worried-xavotirli",
                                    # "black-qora",
                                    # "fierce up-shiddatli",
                                    # "wandering-sarson",
                                    # "pathetic-achinarli",
                                    # "hesitant-ikkilangan",
                                    # "neighborly-qo'shnichilik",
                                    # "festive-bayramona",
                                    # "glossy-silliq",
                                    # "shiny-yaltiroq",
                                    # "dangerous-xafli",
                                    # "lively-jonli",
                                    # "maddening-asabga tegadig",
                                    # "quickest-eng tez",
                                    # "merciful-mehribon",
                                    # "many-ko'p",
                                    # "jaded-charchagan",
                                    # "closed-yopiq",
                                    # "military-xarbiy",
                                    # "fertile-unumdor",
                                    # "maniacal-manyak",
                                    # "smiling-tabassum",
                                    # "female-ayol",
                                    # "vengeful-qasoskor ",
                                    # "certain-aniq",
                                    # "knotty-tugunli",
                                    # "attractive-jozibali",
                                    # "cooing-pishirilgan",
                                    # "fierce-shiddatli",
                                    # "gorgeous-chiroyli",
                                    # "apprehensive-xavotirli",
                                    # "magnificent-ajoyib",
                                    # "learned-o'rgangan",
                                    # "feeble-zayif",
                                    # "solid-mustaxkam",
                                    # "ordinary-alixida",
                                    # "chief-shef",
                                    # "woebegone-voybon",
                                    # "talented-qobilyatli",
                                    # "livid-jonli",
                                    # "chemical-ximyoviy successful-omadli",
                                    # "distressed-g'amgin",
                                    # "bouncy-chaqqon damaging-zararli",
                                    # "absent-yo'q",
                                    # "abashed-xijolatli",
                                    # "real-xaqiqiy ",
                                    # "telling-aytib",
                                    # "unsightly-yoqimsiz",
                                    # "handsomely-chiroyli",
                                    # "rabid-quturgan",
                                    # "feigned-mug'ombir",
                                    # "outgoing-chiquvchi mature-pishgan",
                                    # "cloudy-bulutli",
                                    # "soggy-xo'l",
                                    # "well-made-yaxshi yasalgan",
                                    # "nutty-yong'oq",
                                    # "ludicrous-kulgili",
                                    # "odd-g'alati",
                                    # "fearless-qo'rqmas",
                                    # "distraught-bezovta",
                                    # "intrigued-g'ayritabiy",
                                    # "abnormal-g'ayritabiy",
                                    # "handsome-kelishgan",
                                    # "fearful-qo'rqoq",
                                    # "deadpan-o'lik",
                                    # "halting-to'xtagan",
                                    # "general-umumiy",
                                    # "smug-chiroyli",
                                    # "brash-jasur",
                                    # "womanly-ayollik",
                                    # "utter-butkul",
                                    # "unsuitable-yaroqsiz",
                                    # "rainy-yomg'irli",
                                    # "comfortable-qulay",
                                    # "hallowed-muqaddas",
                                    # "caring-g'amxo'r",
                                    # "wild-yovvoyi",
                                    # "kindly-mexribon",
                                    # "wonderful-ajoyib",
                                    # "fluttering-ajoyib",
                                    # "gaping-bo'sh ",
                                    # "faulty-noto'g'ri",
                                    # "accessible-yaroqli",
                                    # "unknown-nomalum",
                                    # "windy-shamolli",
                                    # "kaput-nomalum",
                                    # "cynical-beadap",
                                    # "permissible-nomukammal",
                                    # "imperfect-barqaror",
                                    # "acidic-uy",
                                    # "acid-o'tkir tamli",
                                    # "steady-uyg'oq",
                                    # "flat-tekis",
                                    # "jagged-qirrali",
                                    # "wrong-xato",
                                    # "unbiased-xolis",
                                    # "abiding-bardoshli",
                                    # "wistful-g'amgin",
                                    # "hurt-siqilgan",
                                    # "quick-tez",
                                    # "petite-erka",
                                    # "damaged-zararli",
                                    # "curious-qiziquvchan",
                                    # "milky-sutli",
                                    # "infamous-nomalum",
                                    # "stormy-bo'ronli",
                                    # "convincing-ishinarli",
                                    # "yummy-mazali",
                                    # "long-term-uzoq muddatli",
                                    # "aboriginal-tub joyli",
                                    # "confused-chalkash thoughtless-o'ylamasdan",
                                    # "ultra-juda",
                                    # "parsimonious-xasis",
                                    # "defiant-bo'ysinmaydigan",
                                    # "perpetual-abadiy",
                                    # "exasperated-g'azablangan",
                                    # "victorious-g'olib",
                                    # "habitual-odatiy",
                                    # "clumsy-beadap",
                                    # "nosy-shovqinli",
                                    # "fancy-g'alati",
                                    # "old-fashioned-eski urfli",
                                    # "grumpy-g'amgin",
                                    # "incandescent-chog'lanma",
                                    # "half-yarim",
                                    # "dashing-sho'x",
                                    # "unhealthy-nosog'lom",
                                    # "sarcastic-kinoyali",
                                    # "innate-tug'ma",
                                    # "decisive-hal qiluvchi",
                                    # "receptive-qabul qiluvchi",
                                    # "bizarre-g'alati",
                                    # "periodic-davriy",
                                    # "anxious-xursand",
                                    # "elated-shod",
                                    # "used-ishlatilgan",
                                    # "sparkling-uchqunli",
                                    # "long-uzun",
                                    # "happy-xursand",
                                    # "adamant-qatiy ",
                                    # "grubby-kir",
                                    # "delicate-nozik",
                                    # "aback-cayratda qoldirad",
                                    # "miscreant-buzg'unchi",
                                    # "uptight-maxkam",
                                    # "fascinate-o'ziga tortgan",
                                    # "fascinated-jalb qilgan",
                                    # "quiet-sokin",
                                    # "ugliest-eng xunuk",
                                    # "detailed-batafsil",
                                    # "vexed-g'azablangan",
                                    # "normal-o'rtacha",
                                    # "glib-so'zamon",
                                    # "best-eng yaxshi",
                                    # "wary-ehtiyotkor",
                                    # "literate-savodli",
                                    # "nebulous-noaniq",
                                    # "actually-asil",
                                    # "brief-qisqacha",
                                    # "parallel-paralel",
                                    # "meaty-go'shtli",
                                    # "wiry-pishiq",
                                    # "nice-yaxshi ",
                                    # "clear-tozza",
                                    # "boiling-qaynagan",
                                    # "nasty-yomon",
                                    # "violent-zo'ravonlik",
                                    # "various-turlixil",
                                    # "watery-suvli ",
                                    # "obnoxious-noxush",
                                    # "abrupt-keskin",
                                    # "blue-ko'k",
                                    # "wacky-g'alati",
                                    # "good-yaxshi",
                                    # "instinctive-instinktli",
                                    # "marvelous-ajoyib",
                                    # "thankful-o'ylovli",
                                    # "acrid-zaxarli ",
                                    # "naive-sodda",
                                    # "boring-zerikarli",
                                    # "appetizing-ishtaxa ochuvch",
                                    # "scary-qo'rqinchli",
                                    # "incredible-aqlga sig'mas",
                                    # "outstanding-aloxida",
                                    # "cautious-ehtiyotkor",
                                    # "violet-binafsha",
                                    # "needless-keraksiz",
                                    # "gifted-sovg'ali",
                                    # "undesirable-ehtirossiz",
                                    # "better-yaxshiroq",
                                    # "hanging-osilgan",
                                    # "aloof-vazmin",
                                    # "jealous-rashkchi",
                                    # "rampant-keng tarqalgan black-and-white-oq qora",
                                    # "harsh-qo'pol",
                                    # "diminutive-jajji",
                                    # "hungry-och",
                                    # "thoughtful-chuqur o'ylanga outrageous-qaxrni keltirad",
                                    # "low-past",
                                    # "annoyed-asabiylashgan",
                                    # "satisfying-qoniqtiradigan",
                                    # "familiar-tanish",
                                    # "elastic-elastik",
                                    # "careful-ehtiyotkor",
                                    # "unadvised-maslaxatsiz",
                                    # " lumpy-dona",
                                    # "juvenile-voyaga yetma",
                                    # "optimal-optimal",
                                    # "peaceful-tinch",
                                    # "succulent-shirali",
                                    # "sticky-yopishqoq",
                                    # "quizzical-savol nazbilqar",
                                    # "lazy-dangasa",
                                    # "ragged-yirtilgan",
                                    # "industrious-mehnatsevar",
                                    # "hurried-shoshilinch",
                                    # "bitter-achchiq",
                                    # "melancholy-melanxoliya",
                                    # "moldy-chiriyotgan",
                                    # "itchy-qichishish",
                                    # "wiggly-to'lqinsimon",
                                    # "imminent-yaqingi",
                                    # "curvy-egri",
                                    # "unable-qodir emas",
                                    # "scintillating-sho'x",
                                    # "tight-qattiq",
                                    # "vivacious-jonli ",
                                    # "educated-bilimli",
                                    # "belligerent-urushqoq",
                                    # "muddy-loyiq",
                                    # "wet-ho'l",
                                    # "conscious-ongli",
                                    # "vivid-jonli",
                                    # "tearful-ko'zga yosh kel",
                                    # "moral-axloqiy",
                                    # "icky-jirkanch",
                                    # "famous-mashxur",
                                    # "lethal-o'limga olib kel",
                                    # "unkempt-beg'ubor",
                                    # "massive-massiv",
                                    # "harmonious-uyg'un",
                                    # "wasteful-isrofgar",
                                    # "erect-tik",
                                    # "ugly-xunuk",
                                    # "mundane-dunyo",
                                    # "judicious-adolatli",
                                    # "lyrical-lirik",
                                    # "mammoth-juda katta",
                                    # "elderly-keksa",
                                    # "youthful-yosh",
                                    # "lazy-dangasa",
                                    # "abstracted-mavxum",
                                    # "kind-tur",
                                    # "tasteless-tamsiz",
                                    # "innocent-aybsiz",
                                    # "defeated-mag'lubiyatga uch",
                                    # "weary-charchagan muddled-tushinarsiz",
                                    # "near-yaqin",
                                    # "rough-qo'pol",
                                    # "aggressive-agressiv",
                                    # "fantastic-fantastik",
                                    # "hellish-jahannam",
                                    # "garbled-tushinarsiz",
                                    # "precious-qimmatli",
                                    # "minor-kichik",
                                    # "parched-qurigan",
                                    # "absurd-absurd",
                                    # "illustrious-mashxur",
                                    # "vague-noaniq",
                                    # "opposite-qarama qarshi",
                                    # "miniature-minyaturali",
                                    # "coherent-izchil",
                                    # "breezy-shamolli",
                                    # "jittery-asaby",
                                    # "fair-adolatli",
                                    # "quirky-g'alati",
                                    # "faint-zaif",
                                    # "redundant-ortiqcha",
                                    # "combative-jangovar",
                                    # "panoramic-panoramali",
                                    # "courageous-jasoratli",
                                    # "bored-zerikkan",
                                    # "sore-og'riq",
                                    # "whispering-shivirlaydigan",
                                    # "hilarious-quvnoq",
                                    # "acceptable-qabul qilinadig excited-xayajonlangan",
                                    # "superior-ustun",
                                    # "unruly-itoatsiz",
                                    # "musty-dimiqqan",
                                    # "robust-mustaxkam",
                                    # "neat-tozza",
                                    # "melted-eritilgan",
                                    # "nostalgic-nostaljik",
                                    # "loose-bo'sh",
                                    # "wealthy-boy",
                                    # "mindless-aqilsiz",
                                    # "absently-parishonxotir",
                                    # "lean-ozg'in",
                                    # "workable-ishlashga yaroqli",
                                    # "heartbreaking-yurakni ezuv",
                                    # "strange-g'alati",
                                    # "round-aylana",
                                    # "untidy-tartibsiz",
                                    # "limping-oqsoqlanadigan",
                                    # "broad-keng",
                                    # "mistaken-xato ",
                                    # "faded-o'chgan",
                                    # "unbecoming-nomaqbul",
                                    # "fabulous-ajoyib ",
                                    # "abounding-ko'p",
                                    # "bright-yorqin",
                                    # "accidental-tasodifiy",
                                    # "short-qisqa",
                                    # "great-buyuk",
                                    # "creepy-daxshatli changeable-o'rganuvchan",
                                    # "brilliant-juda zo'r",
                                    # "legal-qonuniy",
                                    # "juicy-suvli",
                                    # "pungent-o'tkir ",
                                    # "moaning-nola",
                                    # "tall-uzun",
                                    # "noiseless-shovqinsiz",
                                    # "unarmed-qurolsiz",
                                    # "lamentable-achinarli",
                                    # "brown-jigarrang",
                                    # "little-ozgina",
                                    # "deep-chuqur",
                                    # "aboard-chuqur",
                                    # "blue-eyed-ko'k ko'zli",
                                    # "omniscient-biluvchan",
                                    # "ill-informed-bilimsiz",
                                    # "short-kalta",
                                    # "long-uzun",
                                    # "jumbled-chalkash laughable-kulggili",
                                    # "screeching-qichqiriq",
                                    # "relieved-yengillashtirilgan",
                                    # "offbeat-g'ayrioddiy",
                                    # "emaciated-ozib ketgan",
                                    # "elite-elita",
                                    # "modern-zamonaviy",
                                    # "enthusiastic-g'ayratli",
                                    # "recondite-qayta ishlangan",
                                    # "obsolete-eskirgan ",
                                    # "virtuous-fazilatli",
                                    # "married-uylangan",
                                    # "entertaining-ko'ngilochar",
                                    # "old-eski",
                                    # "imaginary-xayoliy",
                                    # "average-o'rtacha",
                                    # "penitent-sabirli",
                                    # "necessary-kerakli",
                                    # "tense-zamon",
                                    # "dilapidated-eskirgan",
                                    # "fat-semiz",
                                    # "tasty-mazali",
                                    # "troubled-muammoli",
                                    # "near-yaqin",
                                    # "quaint-qiziq",
                                    # "good-yaxshi",
                                    # "wide-eyed-ko'zli",
                                    # "new-yangi",
                                    # "horrible-taxshatli",
                                    # "fast-tez",
                                    # "grey-kulrang",
                                    # "helpless-yordamsiz",
                                    # "melodic-melodik",
                                    # "stunning-ajoyib",
                                    # "marked-belgilangan",
                                    # "lovely-sevimli",
                                    # "clever-aqilli",
                                    # "uttermost-eng",
                                    # "enormous-ulkan",
                                    # "lucky-omadli ",
                                    # "grateful-raxmat",
                                    # "hard-qattiq",
                                    # "gratis-bepul",
                                    # "volatile-uchuvchan",
                                    # "unequal-tengsiz",
                                    # "bright-yorqin",
                                    # "brawny-qo'pol",
                                    # "whimsical-injiq",
                                    # "nice-yaxshi",
                                    # "lacking-eshitmayotgan",
                                    # "questionable-shubxali",
                                    # "makeshift-vaqtinchalik",
                                    # "beneficial-foydali",
                                    # "huge-ulkan",
                                    # "energetic-baquvvat",
                                    # "crooked-qiyshiq",
                                    # "endurable-bardoshli",
                                    # "encouraging-rag'batlantiru",
                                    # "earthy-tuproqli",
                                    # "unusual-g'ayrioddiy",
                                    # "deserted-cho'l ",
                                    # "colorful-rangli",
                                    # "cool-salqin",
                                    # "open-ochiq",
                                    # "labored-mehnat qilgan",
                                    # "hot-issiq",
                                    # "known-malum ",
                                    # "knowing-bilish ",
                                    # "colossal-ulkan",
                                    # "rotten-chirigan ",
                                    # "proud-gurur",
                                    # "electric-elektir",
                                    # "scared-qo'rqgan",
                                    # "nutritious-to'yimli",
                                    # "condescending-pastlovchi",
                                    # "far-uzoq",
                                    # "capricious-injiq",
                                    # "fresh-sof",
                                    # "weak-zaif",
                                    # "wet-nam",
                                    # "irritating-bezovta qiluvchi",
                                    # "brave-jasur",
                                    # "jumpy-sakrovchi",
                                    # "measly-qizilcha",
                                    # "momentous-muhim",
                                    # "invincible-yengilmas",
                                    # "wicked-yovuz",
                                    # "tangible-moddiy",
                                    # "ill-kasal",
                                    # "mellow-yumshoq",
                                    # "impolite-shafqatsiz",
                                    # "kindly-mexribon",
                                    # "red-qizil",
                                    # "wide-keng",
                                    # "childlike-bolalardek",
                                    # "painful-og'riqli",
                                    # "superficial-yuzaki",
                                    # "large-katta",
                                    # "calm-bosiq",
                                    # "empty-bo'sh ",
                                    # "fearful-qo'rqoq",
                                    # "waiting-kutish",
                                    # "top-baland",
                                    # "bloody-qonli",
                                    # "hard-qattiq",
                                    # "fury-qaxrli",
                                    # "alive-tirik",
                                    # "impressionable-tasirchan",
                                    # "dazzling-ko'zni qamashtiru",
                                    # "sharp-o'tkir",
                                    # "healthy-sog'lom",
                                    # "eatable-yeyiladigan",
                                    # "boring-zerikarli",
                                    # "determined-aniqlangan",
                                    # "kindhearted-mehribon",
                                    # "spicy-achchiq",
                                    # "ancient-qadimgi",
                                    # "deeply-chuqur",
                                    # "filthy-iflos",
                                    # "final-oxirgi",
                                    # "versed-bilimli",
                                    # "unwritten-yozilmagan",
                                    # "joyous-quvonchli",
                                    # "broken-buzilgan",
                                    # "defective-nuqsonli",
                                    # "mental-aqliy",
                                    # "reflective-aks ettiruvchi",
                                    # "loutish-g'alati",
                                    # "bustling-shovqin",
                                    # "wrathful-g'azabli ",
                                    # "salty-sho'r",
                                    # "hateful-nafratli",
                                    # "average-o'rtacha",
                                    # "onerous-og'ir",
                                    # "breakable-buzilishi mumkin",
                                    # "flat-tekis",
                                    # "deafening-kar qiladigan",
                                    # "interesting-qiziq",
                                    # "major-muxim",
                                    # "impossible-mumkin emas",
                                    # "reassured-ishontiradigan",
                                    # "late-kech",
                                    # "handy-qulay",
                                    # "voracious-ochko'z",
                                    # "uneven-notekis",
                                    # "lavish-dabdabali",
                                    # "amused-quvnoq",
                                    # "biting-tishlash ",
                                    # "stale-eskirgan",
                                    # "deceitful-firibgar",
                                    # "basic-asosiy",
                                    # "easy-oson",
                                    # "descriptive-tavsiflovchi",
                                    # "barbarous-vaxshiy abhorrent-jirkanch",
                                    # "gray-kulrang",
                                    # "capable-qodir",
                                    # "certain-shubxasiz",
                                    # "homely-uyli",
                                    # "smooth-silliq ",
                                    # "valuable-qimmatli",
                                    # " costly-qimmat ",
                                    # " frank-samimiy",
                                    # "ignorant-nodon",
                                    # "imported-import qilingan",
                                    # "equal-teng",
                                    # "far-uzoq",
                                    # "empty-bo'sh",
                                    # "upset-xafa",
                                    # "594    white-oq",
                                    # "595    venomous-zaharli",
                                    # "596    well-groomed-yaxshi ishla",
                                    # "silky-ipak",
                                    # "honorable-hurmatli",
                                    # "inquisitive-qiziquvchan",
                                    # "scandalous-janjal important-muhim",
                                    # "glistening-yaltiroq",
                                    # "complex-kompleks",
                                    # "erratic-tartibsiz",
                                    # "clever-aqilli",
                                    # "green-yashil",
                                    # "impartial-xolis",
                                    # "zippy-zamokli",
                                    # "steep-tik",
                                    # "cut-kesilgan",
                                    # "useless-foydasiz",
                                    # "common-umumiy",
                                    # "bashful-sharmandali",
                                    # "worthless-qiymatsiz astonishing-xayratlanarli",
                                    # "vast-keng",
                                    # "light-yorug'",
                                    # "historical-tarixiy",
                                    # "next-keyingi",
                                    # "wretched-bechora",
                                    # "obsequious-itoatkor",
                                    # "useful-foydali",
                                    # "careless-beparvolik",
                                    # "numberless-sonsiz",
                                    # "yellow-sariq",
                                    # "unique-noyob",
                                    # "nonsensical-bemani",
                                    # "high-yuqori",
                                    # "gleaming-porlash",
                                    # "white-oq",
                                    # "bewildered-hayron",
                                    # "complex-murakkab",
                                    # "nervous-asabiy",
                                    # "gainful-foydali",
                                    # "skinny-og'riq",
                                    # "accurate-tog'li",
                                    # "ill-fated-baxtsiz",
                                    # "last-oxirgi",
                                    # "obscene-odobsiz",
                                    # "hushed-jim",
                                    # "motionless-harakatsiz",
                                    # "delightful-zavqli",
                                    # "condemned-hukm qilingan",
                                    # "giddy-jiddiy",
                                    # "silly-ahmoq",
                                    # "obese-semiz",
                                    # "public-jamoat",
                                    # "abusive-xaqoratmuz",
                                    # "wide-keng",
                                    # "final-oxirgi",
                                    # "further-uzoq",
                                    # "bland-muloyim",
                                    # "rebel-isyonchi",
                                    # "nimble-chaqqon",
                                    # "old-eski",
                                    # "damp-nam",
                                    # "situated-joylashgan",
                                    # "false-noto'g'ri",
                                    # "boring-zerikarli",
                                    # "absorbed-yutilgan",
                                    # "loud-baland ovozli",
                                    # "bad-yomon",
                                    # "tasteful-mazali",
                                    # "cool-salqin",
                                    # "ablaze-olov",
                                    # "lying-yolg'on",
                                    # "needy-muhtoj",
                                    # "racial-irqiy",
                                    # "homeless-uysiz",
                                    # "scientific-ilmiy",
                                    # "dark-qorong'u",
                                    # "unaccountable-jabgarsiz",
                                    # "inexpensive-arzon spotless-beg'ubor ",
                                    # "foolish-axmoq",
                                    # "abandoned-tashlab ketilgan",
                                    # "tedious-zerikarli",
                                    # "major-muxim",
                                    # "abundant-ko'p",
                                    # "wobbly-tebranish",
                                    # "mean-xasis",
                                    # "common-odatiy",
                                    # "shallow-sayoz",
                                    # "cultured-madaniy",
                                    # "nondescript-noaniq",
                                    # "calculating-hisobli",
                                    # "obtainable-olish mumkin",
                                    # "uninterested-qiziqmas",
                                    # "depressed-tushkun",
                                    # "ashamed-uyalgan",
                                    # "unused-foydalanilmagan",
                                    # "different-farqli",
                                    # "level-daraja",
                                    # "fanatical-fanatik",
                                    # "proper-xaqiqiy",
                                    # "greasy-yog'li",
                                    # "savory-mazali",
                                    # "terrible-daxshatli",
                                    # "mountainous--yog'li",
                                    # "macho-macho",
                                    # "mute-ovozsiz",
                                    # "high-pitched-baland ovozli",
                                    # "false-yolg'on",
                                    # "curly-jingalak ",
                                    # "keen-fanat",
                                    # "fat-semiz",
                                    # "economic-iqtisodiy",
                                    # "harm-zararli",
                                    # "arrogant-takabbur",
                                    # "dear-aziz",
                                    # "teeny-tiny-kichik tor",
                                    # "fallacious-yolg'on",
                                    # "slimy-shilimshiq",
                                    # "blushing-qizargan",
                                    # "equable-teng",
                                    # "cold-sovuq",
                                    # "daffy-sodda",
                                    # "faithful-sodiq",
                                    # "dependent-qaram",
                                    # "yellow-sariq",
                                    # "scant-kam",
                                    # "purple-binafsha rang",
                                    # "insidious-makkor",
                                    # "panicky-vahima",
                                    # "lovely-ajoyib",
                                    # "pink-pushti",
                                    # "voiceless-ovozsiz",
                                    # "cowardly-qo'rqoq",
                                    # "moody-kayfiyat",
                                    # "extensive-keng qamrovli",
                                    # "black-qora",
                                    # "elegant-oqlangan",
                                    # "covered-qoplangan",
                                    # "second-hand-ikkinchi qo'l left-chap",
                                    # "quick-tez",
                                    # "glamorous",
                                    # "gentle-muloyim ",
                                    # "hapless-baxtsiz",
                                    # "exuberant-quvnoq",
                                    # "warm-issiq",
                                    # "beautiful-chiroyli",
                                    # "hideous-daxshatli",
                                    # "tall-uzun",
                                    # "cool-salqin",
                                    # "bite-sized-katta o'lchamli",
                                    # "big-katta",
                                    # "immense-ulkan",
                                    # "quarrelsome-janjal",
                                    # "minute-daqiqa",
                                    # "loving-sevuvchi mysterious-sirli",
                                    # "cheerful-quvnoq",
                                    # "white-oq",
                                    # "clear-tozza",
                                    # "red-qizil",
                                    # "grieving-qayg'u",
                                    # "small-kichik",
                                    # "grey-kul rang",
                                    # "substantial-muhim",
                                    # "clueless-tushunarsiz",
                                    # "cluttered-chigallashgan hard-to-find-topish qiyin",
                                    # "gigantic-gigant ",
                                    # "brainy-aqilli",
                                    # "busy-band",
                                    # "brown-jigar rang",
                                    # "sweet-mazali",
                                    # "ripe-pishgan",
                                    # "nice-yaxshi",
                                    # "cruel-qaxirli",
                                    # "efficacious-smarali",
                                    # "early-erta",
                                    # "dead-o'lgan",
                                    # "safe-xavsiz",
                                    # "repulsive-jirkanch",
                                    # "graceful-nafis",
                                    # "sad-g'amgin",
                                    # "nonchalant-befarq",
                                    # "clammy-loyqa",
                                    # "contemplative-tafakkur",
                                    # "cloistered-yopilgan",
                                    # "near-yaqin",
                                    # "warm-iliq",
                                    # "ugly-xunuk",
                                    # "delicious-mazali",
                                    # "irate-g'azablangan",
                                    # "jobless-ishsiz",
                                    # "coordinated-muvofiqlashtiri",
                                    # "best-eng yaxshi",
                                    # "hot-issiq",
                                    # "envious-xasadgo'y",
                                    # "responsive-javob beruvchi",
                                    # "thick-qalin ",
                                    # "straight-tog'li",
                                    # "hospitable-mexmondo'st",
                                    # "wide-keng",
                                    # "full-to'la",
                                    # "idiotic-axmoq",
                                    # "ghastly-daxshatli",
                                    # "fuzzy-loyqa",
                                    # "unwield-qo'zg'almas",
                                    # "foggy-tumanli",
                                    # "cloudy-bulutli",
                                    # "orange-sabzi rang",
                                    # "funny-kulgili",
                                    # "horrific-daxshatli",
                                    # "strong-kuchli",
                                    # "frustrating-umidsizlik",
                                    # "frothy-ko'pikli",
                                    # "willing-hohlovchi scattered-tarqoq",
                                    # "lowly-past",
                                    # "cool-salqin",
                                    # "crazy-jinni",
                                    # "radical-qatiy",
                                    # "timely-o'z vaqtida obedient-itoatkor",
                                    # "hostile-g'arazli",
                                    # "cheap-arzon",
                                    # "wide-keng",
                                    # "upbeat-tezkor",
                                    # "rapid-quvnoq",
                                    # "understood-tushinilgan lopsided-egilgan",
                                    # "well-to-do-baxtli",
                                    # "rare-kamdan kam",
                                    # "edible-yesa bo'ladigan",
                                    # "big-katta",
                                    # "dense-qalin",
                                    # "heavenly-samoviy",
                                    # "curved-egri",
                                    # "lame-cho'loq",
                                    # "boundless-cheksiz",
                                    # "friendly-do'stona",
                                    # "nonstop-to'xtovsiz",
                                    # "barren-mevasiz",
                                    # "luxuriant-dabdabali",
                                    # "tall-uzun",
                                    # "historical-tarixiy",
                                    # "hot-issiq",
                                    # "same-o'xshash",
                                    # "selfish-xudbin",
                                    # "handsome-kelishgan",
                                    # "beautiful-chiroyli ",
                                    # "medical-tibbiy",
                                    # "hollow-ichi bo'sh",
                                    # "decayed-chirigan",
                                    # "giant-gigant",
                                    # "prickly-tikanli",
                                    # "humorous-hazil",
                                    # "holistic-yaxlit",
                                    # "much-ko'p",
                                    # "clean-tozza ",
                                    # "misty-tuman",
                                    # "many-ko'p",
                                    # "numerous-ko'",
                                    # "charming-go'zal ",
                                    # "wise-aqilli",
                                    # "vacuous-vakum",
                                    # "classy-sinf",
                                    # "heavy-og'g'ir",
                                    # "heavy-og'ir",
                                    # "bloody-qonli",
                                    # "amiable-mehribon ",
                                    # "luky-omadli",
                                    # "disturbed-bezovta",
                                    # "stupit-axmoq",
                                    # "despicable-razil",
                                    # "zealous-g'ayratli",
                                    # "smart-aqilli ",
                                    # "silly-axmoq",
                                    # "enchanting-sehrli",
                                    # "teeny-yosh",
                                    # "enchanted-sehrlangan",
                                    # "helpful-foydali",
                                    # "eager-g'ayratli",
                                    # "cooperative-koperativ",
                                    # "ideal-ideal",
                                    # "intelligent-aqilli",
                                    # "frightened-qo'rqib ketgan",
                                    # "male-erkak",
                                    # "fascinated-maftun",
                                    # "quiet-sokin ",
                                    # "ugliest-eng xunuk",
                                    # "detailed-batafsil",
                                    # "vexed-g'azablangan",
                                    # "normal-normal",
                                    # "great-buyuk",
                                    # "soft-yumshoq",
                                    # "wary-ehtiyotkor",
                                    # "literate-savodli",
                                    # "nebulous-noaniq",
                                    # "actually-aslida ",
                                    # "brief-qisqacha",
                                    # "parallel-paralel",
                                    # "meaty-go'shtli",
                                    # "old-eski",
                                    # "cheap-arzon",
                                    # "clear-aniq",
                                    # "boiling-qaynagan",
                                    # "nasty-yomon",
                                    # "cold-sovuq",
                                    # "various-turli",
                                    # "watery-suvli",
                                    # "wet-nam",
                                    # "abrupt-keskin",
                                    # "blue-ko'k",
                                    # "fearful-qo'rqinchli",
                                    # "good-yaxshi",
                                    # "hard-qattiq",
                                    # "green-yaxshil",
                                    # "thankful-minnatdor",
                                    # "nature-tabiy ",
                                    # "naive-sodda",
                                    # "boring-zerikarli",
                                    # "delicious-mazali",
                                    # "scary-qo'rqoq",
                                    # "incredible-aqlga sig'mas",
                                    # "outstanding-boshqacha",
                                    # "small-kichkina",
                                    # "near-yaqin",
                                    # "needless-kerakli",
                                    # "gifted-sovg'a",
                                    # "nice-yaxshi",
                                    # "better-yaxshiroq",
                                    # "far-uzoq",
                                    # "aloof-uzoqda",
                                    # "jealous-hasad",
                                    # "rampant-keng tarqalgan black-and-white-oq qora",
                                    # "harsh-qattiq",
                                    # "diminutive",
                                    # "hungry-och",
                                    # "thoughtful-o'ylovli",
                                    # "outrageous-g'alati",
                                    # "low-past",
                                    # "annoyed-bezovta",
                                    # "satisfying-qoniqarli",
                                    # "familiar-o'xshash",
                                    # "elastic-elastik",
                                    # "careful-extiyotkor",
                                    # "unadvised-maslaxatsiz",
                                    # "lumpy-bo'lak ",
                                    # "juvenile-voyaga yetmagan",
                                    # "optimal-optimal",
                                    # "peaceful-tinch",
                                    # "succulent",
                                    # "sticky-yopishqoq",
                                    # "quizzical",
                                    # "good-yaxshi",
                                    # "old-eski",
                                    # "new-yangi",
                                    # "tall-uzun",
                                    # "short-kalta",
                                    # "thin-ozg'in",
                                    # "fat-semiz",
                                    # "charming-go'zal",
                                    # "fast-tez",
                                    # "slow-sekin",
                                    # "beautiful-chiroyli",
                                    # "anxious - xavotirlangan",
                                    # "awful - juda yomon",
                                    # "polite - odobli,aqlli-xushli",
                                    # "rapidly - juda tez",
                                    # "common-odatiy",
                                    # "independent-mustaqil",
                                    # "cool-salqin,jindak sovuq",
                                    # "major-muhim",
                                    # "mean-baxil,ziqna ",
                                    # "rich-boy,badavlat",
                                    # "effective - samarali",
                                    # "false - xato",
                                    # "quite - juda ",
                                    # "specific - aniq",
                                    # "basic - oddiy, sodda",
                                    # "real - haqiqiy, real",
                                    # "worth - arziydigan",
                                    # "excellent - juda yaxshi",
                                    # "actual - haqiqiy",
                                    # "mystery - sir , jumboq",
                                    # "opposite - teskari",
                                    # "mental - aqliy",
                                    # "pole - ustun",
                                    # "safe - xavfsiz",
                                    # "complex - murakkab",
                                    # "ancient - qadimiy",
                                    # "hidden - yashirin ",
                                    # "original - asl nusxadagi ",
                                    # "empty - bo'sh",
                                    # "exact - aniq",
                                    # "brilliant-brliant",



############Ingliz tilida 1000 ta fel#################



                                    # "learn-o'rganmoq",
                                    # "become-aylanib qolmoq ",
                                    # "come-kelmoq",
                                    # "include-o'z ichiga olmoq",
                                    # "thank-raxmat aytmoq",
                                    # "thank-raxmat aytmoq",
                                    # "create-yaratmoq",
                                    # "add-qo'shmoq",
                                    # "understand-tushunmoq",
                                    # "consider-xisobga olmoq",
                                    # "choose-tanlamoq",
                                    # "develop-rivojlanmoq",
                                    # "remember-eslamoq",
                                    # "determine-aniqlamoq",
                                    # "grow-ulg'aymoq",
                                    # "allow-ruxsat bermoq",
                                    # "supply-taminlamoq",
                                    # "bring-olib kelmoq",
                                    # "improve-rivojlanmoq",
                                    # "maintain-saqlab qolmoq",
                                    # "begin-boshlamoq",
                                    # "exist-mavjud bo'lmoq",
                                    # "tend-moyil bo'lmoq",
                                    # "enjoy-roxatlanmoq",
                                    # "perform-bajarmoq",
                                    # "decide-qaror qilmoq",
                                    # "identify-aniqlamoq",
                                    # "continue-davom etmoq",
                                    # "protect-ximoya qilmoq",
                                    # "require-talab qilmoq",
                                    # "occur-yuzala kelmoq",
                                    # "write-yozmoq",
                                    # "approach-tatqiq qimoq",
                                    # "avoid-qochmoq",
                                    # "prepare-tayyorlamoq",
                                    # "build-qurmoq",
                                    # "achieve-erishmoq",
                                    # "believe-ishonmoq",
                                    # "receive-qabul qilmoq",
                                    # "seem-tuyilmoq",
                                    # "discuss-muxokama qilmoq",
                                    # "discuss-muxokama qilmoq",
                                    # "realize-anglamoq",
                                    # "contain-o'z ichida olmoq",
                                    # "follow-ergashmoq",
                                    # "refer-murojat qilmoq",
                                    # "solve-yechim topmoq",
                                    # "solve-yechim topmoq",
                                    # "describe-tasvirlamoq",
                                    # "prefer-afzal ko'rmoq",
                                    # "prevent-oldini olmoq",
                                    # "discover-kashf qilmoq",
                                    # "ensure-taminlamoq",
                                    # "expect-kutmoq",
                                    # "invest-sarmoya kiritmoq",
                                    # "reduce-kamaytirmoq",
                                    # "speak-gapirmoq",
                                    # "appear-ko'rinmoq",
                                    # "explain-tushuntirmoq",
                                    # "explore-kashf qilmoq",
                                    # "involve-jalb qilish",
                                    # "lose-yo'qoltmoq",
                                    # "afford-qurbi yetmoq",
                                    # "agree-rozi bo'lmoq",
                                    # "hear-eshitmoq",
                                    # "remain-qonmoq",
                                    # "represent-ifodalamoq",
                                    # "apply-xujjat topshirmoq",
                                    # "forget-unutmoq",
                                    # "recommend-tafsiya etmoq",
                                    # "rely-tayanmoq",
                                    # "vary-farxlamoq",
                                    # "generate-issiqlik chiqarmoq",
                                    # "obtain-olmoq",
                                    # "accept-qabul qilmoq",
                                    # "communicate-aloqa qilmoq",
                                    # "complain-shikoyat qilmoq",
                                    # "depend-big'liq bo'lmoq",
                                    # "enter-kirmoq",
                                    # "happen-sodir bo'lmoq",
                                    # "indicate-ko'rsatmoq",
                                    # "suggest-taklif qilmoq",
                                    # "survive-omon qolmoq",
                                    # "appreciate-qadrlamoq",
                                    # "compare-taqqoslamoq",
                                    # "imagine-tasavvur qilmoq",
                                    # "manage-boshqarmoq",
                                    # "differ-farq qilmoq",
                                    # "encourage-undamoq",
                                    # "expand-kengaytirmoq",
                                    # "prove-isbotlamoq",
                                    # "react-reaksiya bermoq",
                                    # "recognize-tanib olmoq",
                                    # "relax-dam olmoq",
                                    # "replace-almashtirmoq",
                                    # "relax-rozatlanmoq",
                                    # "replace-almashtirmoq",
                                    # "borrow-qarz olmoq",
                                    # "earn-ishlab topmoq",
                                    # "emphasize-takitlamoq",
                                    # "operate-ishlamoa",
                                    # "reflect-refleksiya bo'l",
                                    # "send-jo'natmoq",
                                    # "watch-ko'rmoq",
                                    # "open-ochmoq",
                                    # "engage-kelishmoq",
                                    # "hear-eshitmoq",
                                    # "examine-imtixon qilmoq install-o'rnatmoq",
                                    # "participate-qatnashmoq",
                                    # "intend-niyat qilmoq",
                                    # "introduce-tanishmoq",
                                    # "relate-bog'lamoq",
                                    # "settle-ishontirmoq",
                                    # "assure-kafolatlamoq",
                                    # "attract-jalb qilmoq distribute-bezovta qilmoq",
                                    # "overcome-yengmoq",
                                    # "owe-qarz bo'lmoq",
                                    # "succeed-muvaffaqiyatga er",
                                    # "suffer-aziyat chekmoq",
                                    # "throw-otmoq",
                                    # "acquire-ega bo'lmoq",
                                    # "adapt-moslashish",
                                    # "adjust-almashtirmoq",
                                    # "argue-baxslashmoq",
                                    # "arise-o'smoq",
                                    # "confirm-tastiqlamoq",
                                    # "encouraging-rag'batlantir",
                                    # "incorporate-qo'shib olmoq",
                                    # "justify-oqlamoq",
                                    # "organize-tashkil qilmoq",
                                    # "ought-kerak bo'lmoq",
                                    # "possess-egalik qilish",
                                    # "relieve-yengillatmoq",
                                    # "retain-saqlab qolmoq",
                                    # "shut-ràqobat qil",
                                    # "calculate-maslaxatlashm",
                                    # "compete-yetkazib berm",
                                    # "consult-maslaxat bermoq",
                                    # "deliver-kechikmoq",
                                    # "extend-uzytirmoq",
                                    # "investigate-tekshirmoq",
                                    # "negotiate-muzokara qilm qualify-saralamoq",
                                    # " retired-nafaqaga chiqmoq",
                                    # "weigh-tortmoq taroziga",
                                    # "arrive-yetib kelmoq",
                                    # "attach-biriktirmoq",
                                    # "behave-o'zini tutmoq",
                                    # "celebrate-nishonlamoq",
                                    # "convince-ishontirmoq",
                                    # "disagree-norozi bo'lmoq",
                                    # "establish-o'rnatish",
                                    # "ignore-inkor qilmoq",
                                    # "imply-nazarda tutmoq",
                                    # "insist-turib olmoq",
                                    # "pursue-taqib qilmoq",
                                    # "remaining-qolgan",
                                    # "specify-belgilamoq",
                                    # "warn-ogoxlantirmoq",
                                    # "accuse-ayblamoq",
                                    # "admire-qoyil qolmoq",
                                    # "admit-bo'yniga olmoq",
                                    # "adopt-moslashmoq",
                                    # "announce-elon qilmoq",
                                    # "apologize-uzir so'ramoq",
                                    # "approve-xursand bo'lmoq",
                                    # "attend-qatnashmoq",
                                    # "arise-o'smoq",
                                    # "attend-qatnashmoq",
                                    # "belong-tegishli bo'lmoq",
                                    # "commit-fikr bermoq",
                                    # "call-chaqirmoq ",
                                    # "deserve-yo'q qilish",
                                    # "destroy-buzmoq",
                                    # "hesitate-ikkilanmoq",
                                    # "illustrate-tasvirlamoq inform-xabar bermoq",
                                    # "manufacturing",
                                    # "persuade-taklif qilmoq",
                                    # "share-bo'lishmoq",
                                    # "aim-maqsad qilmoq",
                                    # "remind-eslamoq",
                                    # "eat-yemoq",
                                    # "submit-topshirmoq",
                                    # "suppose",
                                    # "translate-tarjima qilmoq",
                                    # "be-bo'lmoq",
                                    # "have-bor bo'lmoq",
                                    # "use-foydalanmoq",
                                    # "make-yasamoq",
                                    # "look - qaramoq",
                                    # "help-yordam",
                                    # "go-bormoq",
                                    # "being-bo'lmoq",
                                    # "think-o'ylamoq",
                                    # "read-o'qimoq",
                                    # "keep-saqlamoq",
                                    # "start-boshlamoq",
                                    # "give-bermoq",
                                    # "play-o'ynamqo",
                                    # "feel-his qilmoq",
                                    # "put-qo'ymoq ",
                                    # "set-o'rnatmoq",
                                    # "change-o'zgartirmoq",
                                    # "play-o'ynamoq",
                                    # "feel-his qilmoq",
                                    # "put-qo'ymoq",
                                    # "set-o'tirmoq",
                                    # "change-o'zgartirmoq",
                                    # "call-qo'ngiroq qilmoq",
                                    # "move-siljimoq",
                                    # "pay-to'lamoq",
                                    # "let-ruxsat bermoq",
                                    # "increase-o'smqo",
                                    # "turn-burmoq",
                                    # "ask-so'ramoq ",
                                    # "buy-so'ramoq",
                                    # " guard-qo'riqlamoq ",
                                    # "hold-ushlamoq",
                                    # "offer-taklif qilmoq",
                                    # "travel-sayoxat qilm",
                                    # "cook-pishirmoq",
                                    # "dance-raqsga tushmqo",
                                    # "excuse-kechirmqo",
                                    # "live-yashamqo",
                                    # "purchase-maqsad qilmqo",
                                    # "drink-ichmoq",
                                    # "mean-mano anglatmoq",
                                    # "fall-yiqilmoq",
                                    # "produce-ishlab chiqmoq",
                                    # "search-qidirmoq",
                                    # "spend-sarflamoq ",
                                    # "talk-suxbatlashmoq",
                                    # "upset-o'rnatmoq",
                                    # "tell-aytmqo",
                                    # "cost-narxlamoq",
                                    # "drive-xaydamqo",
                                    # " support-qo'llamqo",
                                    # "move-siljimoq",
                                    # "return-qaytmoq",
                                    # "run-yugurmqo",
                                    # "appropriate",
                                    # "serve-xizmat qilmoq",
                                    # "leave-jo'namoq",
                                    # "rest-dam olmoq",
                                    # "serve-xizmat ko'rstm",
                                    # "watch-ko'rmoq",
                                    # "reach-erishmoq",
                                    # "serve-xizmat ko'rsatmoq",
                                    # "watch-ko'rmoq",
                                    # "charge-zaryadlamoq",
                                    # "break-sindirmoq",
                                    # "stay-qolmoq",
                                    # "visit-tashrif buyurmoq",
                                    # "affect-tasir qilmoq",
                                    # "cover-qoplamqo",
                                    # "report-xabar bermqo",
                                    # "rise-ko'tarilmoq",
                                    # "walk-yurmoq",
                                    # "pick-yermoq",
                                    # "lift-ko'tarmoq",
                                    # "mix-aralashtirmoq ",
                                    # "stop-to'xtamoq ",
                                    # "teach-o'qitmoq",
                                    # "concern-aloqada bo'lmoq",
                                    # "fly-uchmoq",
                                    # "born-tug'ulmoq",
                                    # "gain-foyda qilmoq",
                                    # "save-saqlamoq",
                                    # "stand-turmoq",
                                    # "fail-yiqilmoq",
                                    # "lead-olib bormiq ",
                                    # "listen-tinglamoq",
                                    # "worry-xavotirlanmoq",
                                    # "express-ifodalamoq",
                                    # "handle-qo'lda tutmoq",
                                    # "meet-uchrashmoq",
                                    # "contribute-sadaqa qilmoq",
                                    # "consist-iborat bo'lmoq",
                                    # "release-ozod qilmoq",
                                    # "sell-sotmoq",
                                    # "finish-tugatmoq",
                                    # "press-nashr qilmoq",
                                    # "ride-minmoq",
                                    # "spread-sochmoq",
                                    # "spring-sapchimoq",
                                    # "wait-kutmoq",
                                    # "display-namoish qilm",
                                    # "flow-ergashmoq",
                                    # "hit-tepmoq",
                                    # "shoot-otmoq",
                                    # "touch-ushlamoq ",
                                    # "cancel-bekor qilmoq",
                                    # "cry-yig'lamoq ",
                                    # "dump-uymoq ",
                                    # "push-itarmoq",
                                    # "select-tanlamoq",
                                    # "conflict-zid kelmoq",
                                    # "die-o'lmoq",
                                    # "eat-yemoq",
                                    # "fill-to'ldirmoq",
                                    # "jump-sakramoq",
                                    # "kick-yepmoq",
                                    # "pass-uzatmoq",
                                    # "pitch-palatka tikmoq",
                                    # "treat-davolamoq",
                                    # "abuse-suistemoq qil",
                                    # "beat-urmoq",
                                    # "burn-kuymoq",
                                    # "deposit-bankka pul qo'ym",
                                    # "print-nashr qilmoq",
                                    # "raise-ko'tarmoq",
                                    # "sleep-uxlamoq",
                                    # "advance-odinga yurmow",
                                    # "connect--ulanmoq",
                                    # "join-qatnaahmoq",
                                    # "kill-o'ldirmoq",
                                    # "sit-o'tirmoq",
                                    # "tap-teginmoq",
                                    # "win-yutmoq",
                                    # "attack-xujum qilmoq",
                                    # "claim-davo qilm drop-tomchilamoq",
                                    # "drink-ichmoq",
                                    # "guess-taxmin qilmoq",
                                    # "pull-tortmoq",
                                    # "wear-kiymoq",
                                    # "wonder-xayron qolm",
                                    # "count-xisoblamoq",
                                    # "doubt-shubxa qilm",
                                    # "feed-boqmoq",
                                    # "impress-tassurot qold",
                                    # "repeat-takrorlamoq",
                                    # "seek-qizdirmoq",
                                    # "sing-kuylamoq",
                                    # "slide-bo'lmoq ",
                                    # "strip-shilmoq",
                                    # "wish-orzu qilmoq ",
                                    # "collect-to'plamoq",
                                    # "combine-birlashtirmoq",
                                    # "command-buyruq bermoq",
                                    # "dig-qozmoq",
                                    # "divide-bo'lmoq",
                                    # "hang-osmoq",
                                    # "hunt-ov qilmoq",
                                    # "march-norozilik yur qilm",
                                    # "mention-eslatib o'tmoq",
                                    # "smell-xidlamoq",
                                    # "survey-ko'z tashlamoq",
                                    # "tie-bog'lamoq",
                                    # "escape-qochmoq",
                                    # "expose-fosh qilmoq ",
                                    # "gather-yig'moq",
                                    # "hate-nagratlamoq ",
                                    # "repair-tamirlamoq",
                                    # "scratch-tirnamoq",
                                    # "strike-xujim qilmow",
                                    # "visit-tashrif buyurmoq",
                                    # "employ-ish bermoq ",
                                    # "hurt-jaroxatlanmoq",
                                    # "laugh-kulmoq",
                                    # "lay-yotqizmoq",
                                    # "respond-javob bermqo",
                                    # "split-tilamoq",
                                    # "strain-kuchlanmoq",
                                    # "struggle-kurashmoq",
                                    # "swim-suzmiq",
                                    # "train-tarbiyalamoq",
                                    # "wash-yuvmoq",
                                    # "waste-isrof qilmoq",
                                    # "convert-aylantirmoq",
                                    # "crash-halokatga uchr",
                                    # "fold-taxlamoq",
                                    # "grab-yulib olmoq",
                                    # "hide-yashinmoq ",
                                    # "miss-sog'inmoq",
                                    # "permit-ruxsat bermoq",
                                    # "quote-dalil keltirmoq",
                                    # "recover-tiklamoq",
                                    # "resolve-hal qilmoq",
                                    # "roll-dumalamoq",
                                    # "sink-cho'kmoq ",
                                    # "slip-toymoq",
                                    # "suspect-gumon qilinmoq",
                                    # "swing-belamoq ",
                                    # "twist-qayrilmoq",
                                    # "concentrate-fikrini jamlam",
                                    # "estimate-baxolamoq",
                                    # "prompt-undamoq",
                                    # "refuse-rad etmoq",
                                    # "regret-afsuslanmoq",
                                    # "reveal-oshkor qilmoq",
                                    # "rush-shoshilmoq",
                                    # "shake-silkitmoq",
                                    # "shift-surmoq",
                                    # "shine-charaqlamoq",
                                    # "steal-o'g'irlamoq",
                                    # "surround-o'rab olmoq",
                                    # "bear-suyab turmoq",
                                    # "dare-davat qilmoq",
                                    # "delay-kechiktirmoq",
                                    # "hurry-shoshilmoq",
                                    # "invite-taklif qilmoq",
                                    # "kiss-o'pmoq",
                                    # "marry-uylanmoq",
                                    # "pop-qo'ymoq",
                                    # "pray-ibodat qilmoq",
                                    # "pretend-mug'ambirlik qil",
                                    # "punch-mushlashmoq",
                                    # "quit-to'xtatmoq",
                                    # "reply-javob bermoq",
                                    # "resist-qarshilik ko'rsatmoq rip-yirtmoq",
                                    # "rub-surtmoq",
                                    # "smile-jilmaymoq",
                                    # "spell-xarflamoq",
                                    # "stretch-cho'zilmoq",
                                    # "tear-yirtmoq",
                                    # "wake -uyg'onmoq",
                                    # "wrap-o'ramoq",
                                    # "like-yoqrirmoq",
                                    # "even-xatokki",
                                    # "film-kinoga tushmoq",
                                    # "water-sug'ormoq",
                                    # "been-bo'lmoq",
                                    # "well-qalqlib chiqmoq",
                                    # "were-bo'lgan edi",
                                    # "example-misol keltirmoq",
                                    # "own-ega bo'lmoq",
                                    # "study-taxsil olmoq",
                                    # "must-kerak bo'lmoq",
                                    # "form-tuzmoq ",
                                    # "air-qurutmoq",
                                    # "place-joylashtirmoq",
                                    # "number-raqamlamoq",
                                    # "part-ajratmoq",
                                    # "field-maydonga tushmoq",
                                    # "fish-baliq ovlamoq",
                                    # "give-bermoq ",
                                    # "heat-isitmoq",
                                    # "hand-uzatmoq",
                                    # "experience-tajriba qilmoq dry-qurumoq",
                                    # "book-band qilmoq",
                                    # "end-tugatmoq",
                                    # "point-ko'rsatmoq",
                                    # "type-yozmoq",
                                    # "value-qiymat bermoq",
                                    # "clean-tozalamoq",
                                    # "market-sotmoq",
                                    # "guide-yo'l ko'rsatmoq",
                                    # "interest-qiziqmoq",
                                    # "state-bildirmoq",
                                    # "take-olmoq",
                                    # "speak-gapirmoq ",
                                    # "break-sindirmoq",
                                    # "price-baxolamoq",
                                    # "size-tasavvur qilmoq",
                                    # "eat-yemoq",
                                    # "list-ro'yxatga kiritmoq",
                                    # "mind-fikirlamoq",
                                    # "trade-savdo qilmoq",
                                    # "line-ichini qoplamoq",
                                    # "care-g'amxorlik qilmoq",
                                    # "group-guruxlamoq",
                                    # "risk-tavakkal qilmoq",
                                    # "-open-ochmoq",
                                    # "force-majburlamoq ",
                                    # "light-yorishmoq",
                                    # "name-ism qo'ymoq",
                                    # "break-sindirmoq",
                                    # "amount-xosil bo'lmoq order-buyurmoq",
                                    # "practice-mashq qilmoq",
                                    # "research-izlanish qilmoq",
                                    # "sense-tuymoq",
                                    # "service-xizmat qilmoq",
                                    # "choose-tanlamoq",
                                    # "enter-kirmoq",
                                    # "boss-xo'jayinlik qilmoq",
                                    # "win-yutmoq",
                                    # "page-chaqirmoq",
                                    # "term-atamoq",
                                    # "test-test qilmoq",
                                    # "answer-javob bermoq",
                                    # "sound-eshtilmoq",
                                    # "focus-etibor qilmoq",
                                    # "matter-muxim bo'lmoq",
                                    # "soil-kir qilmoq",
                                    # "board-aftobusga chiqmoq",
                                    # "oil-yog'lamoq",
                                    # "picture-tasavvur qilmoq",
                                    # "access-kirmoq",
                                    # "garden-bog'da ishlam",
                                    # "open-ochmoq",
                                    # "range-miqdor bermoq",
                                    # "rate-jalb qilmoq",
                                    # "reason-sabab ",
                                    # "accord-ko'rsatmoq",
                                    # "site-joylashtirmoq",
                                    # "demand-talab qilmoq",
                                    # "exercise-mashq qilmoq image-tasvirlamoq",
                                    # "case-ssabab qilmoq ",
                                    # "cause-sabab qilmoq",
                                    # "agree-rozi bo'lmoq",
                                    # "arrive-yetib kelmoq",
                                    # "attack-xujum qilmoq",
                                    # "result-natija ko'rsatmoq",
                                    # "hide-yashirmoq",
                                    # "build-qurmoq",
                                    # "hunt-ov qilmoq",
                                    # "cash-naxt to'lamoq",
                                    # "class-sinflamoq ",
                                    # "dry-qurutmoq",
                                    # "plan-reja qilmoq",
                                    # "promise-vada bermoq",
                                    # "tax-soliq solmoq",
                                    # "involved-jalb qilmoq",
                                    # "side-tomonlamoq",
                                    # "reply-qayta o'tkazmoq",
                                    # "approach-yaqinlashmoq",
                                    # "creat-yaratmoq",
                                    # "kill-o'ldirmoq",
                                    # "scare-qo'rqmoq",
                                    # "shout-baqirmoq",
                                    # " smell-xidlamoq",
                                    # "describe-tasvirlamoq",
                                    # "fail-yiqilmoq",
                                    # "design-qaror qilmoq",
                                    # "solve-yechim topmoq",
                                    # "purpose-maqsad qilmoq suppose-taxmon qilmoq",
                                    # "view-ko'rib chiqmoq",
                                    # "act-xarakat qilmoq",
                                    # "birth-tug'ilmoq",
                                    # "avoid-qochmoq",
                                    # "behave-o'zini tutmoq",
                                    # "expect-kutmoq",
                                    # "punish-jazolamoq",
                                    # "fit - mos kelmoq ",
                                    # "note-belgilamoq",
                                    # "profit-foyda keltirmoq",
                                    # "related-bog'lamoq",
                                    # "rent-ijaraga bermoq",
                                    # "speed-tezlikni oshirmoq",
                                    # "shake-silkimoq",
                                    # "war-urushmoq",
                                    # "spread-surtmoq",
                                    # "stroll-sayr qilmoq",
                                    # "belong-tegishli bo'lmoq",
                                    # "continue-davom ettirmoq",
                                    # "hurt-lat yemoq",
                                    # "relax-dam olmoq",
                                    # "fire-yoqmoq",
                                    # "request-iltimos qilmoq",
                                    # "reside-istiqomat qilmoq",
                                    # "roll-o'ramoq",
                                    # "cause-sabab bo'lmoq",
                                    # "benefit-foyda qilmoq",
                                    # "escape-qochmoq",
                                    # "complete-tugatmoq ",
                                    # "follow-ergashmoq",
                                    # "reach-erishmoq",
                                    # "limited-cheklamoq",
                                    # "step-qadam qo'ymoq",
                                    # "return-qaytib kelmoq",
                                    # "allow-ijozat bermoq",
                                    # "interested in - ga qiziqmoq",
                                    # "announce-xabar qilmoq",
                                    # "paint-bo'yamoq",
                                    # "review-ko'rib chiqmoq",
                                    # "claim-davo qilmoq",
                                    # "contribute-inom qilmoq",
                                    # "divide-bo'lmoq,ajratmoq",
                                    # "lay-qo'ymoq",
                                    # "account-xisoblamoq",
                                    # "protect-ximoya qilmoq",
                                    # "concerne-tashvishlanmoq",
                                    # "discipline-tayuorlanmoq",
                                    # "ready-tayyorlanmoq",
                                    # "share-bo'lishmoq ",
                                    # "sense-xis qilmoq",
                                    # "accept-qabul qilmoq",
                                    # "arrange-tartibga solmoq",
                                    # "encourage-ruxlantirmoq",
                                    # "gift-sovg'a bermoq",
                                    # "impact-tasir o'tkazmoq",
                                    # "grab-tortib olmoq",
                                    # "propose-taklif qilmoq",
                                    # "release-ozod qilmoq ",
                                    # "wind-shamol esmoq require-extiyoj sezmoq",
                                    # "tear-yirtmoq",
                                    # "damage-zarar yetkazmoq",
                                    # "discover-keshf etmoq",
                                    # "sign-imzo qo'ymoq",
                                    # "fix-o'rnatmoq",
                                    # "task-vazifa bermoq",
                                    # "condition-sharoit qilmoq",
                                    # "contact-aloqa qilmoq",
                                    # "prevent-oldini olmoq",
                                    # "save-saqlamoq",
                                    # "hope-umid qilmoq",
                                    # "ice-muzlamoq",
                                    # "praise-maqtamoq",
                                    # "separate-ajratmoq",
                                    # "attempt-urinmoq",
                                    # "scream-qichqirmoq",
                                    # "effect-tasir qilmoq",
                                    # "impress-hayron qoldirmoq",
                                    # "perfect-afzal ko'rmoq",
                                    # "post-port qoldirmoq",
                                    # "start-boshlqmoq",
                                    # "voice-ovoz bermoq",
                                    # "challenge-chqirmoq",
                                    # "disturb-bezovta qilmoq",
                                    # "warm-ilimoq",
                                    # "brush-cho'tkalamoq",
                                    # "twist-qayirmoq",
                                    # "trust-ishonmoq",
                                    # "obey-bo'ysunmoq ",
                                    # "intend-niyat qilmoq",
                                    # "submit-taqdim qilmoq",
                                    # "ensure-taminlamoq",
                                    # "plant-ekmoq",
                                    # "counsel-maslaxat bermoq",
                                    # "command-buyurmoq",
                                    # "taste-tatib ko'rmoq",
                                    # "bring-olib kelmoq",
                                    # "spill-to'kmoq",
                                    # "shine-charaqlamoq",
                                    # "seek-izlamoq",
                                    # "remark-ko'rsatib bermoq",
                                    # "possess-egalik qilmoq",
                                    # "correct-tog'urlamoq",
                                    # "desire-xoxlamaoq",
                                    # "mix-aralashtirmoq",
                                    # "load-ko'tarmoq",
                                    # "lift-ko'tarilmoq",
                                    # "influence-tasir qilmoq",
                                    # "eager-intilmoq",
                                    # "rain-yomg'ir yog'moq",
                                    # "desire-xoxlamoq",
                                    # "base-asosiy qilib belg",
                                    # "damage-zarar keltirmoq",
                                    # "distance-masofa saqlamoq",
                                    # "pair-argue-sabab ko'rsatm",
                                    # "waste-isrof qilmoq",
                                    # "flow-oqmoq",
                                    # "target-nishonga olmoq",
                                    # "text-yozmoq ",
                                    # "disappear-belgilamoq",
                                    # "complicated-murakkab celebrate-nishonlamoq",
                                    # "beat-urmoq",
                                    # "publish-nashr qilmoq",
                                    # "pound-maydalamoq",
                                    # "offer-taklif qilmoq",
                                    # "exist-mavjud bo'lmoq",
                                    # "risk-tavakkal qilmoq",
                                    # "register-ro'yxatdan o'tmoq",
                                    # "secure-xavsizlikni tamin",
                                    # "happen-sodir bo'lmoq",
                                    # "excite-jo'shqinlantirmoq",
                                    # "consume-istemol qilmoq",
                                    # "title-sarlovxa qo'ymoq",
                                    # "trouble-muammoga uchra",
                                    # "breathe-nafas olmoq",
                                    # "suffer-aziyat chekmoq",
                                    # "print-nashr qilmoq",
                                    # "control-nazorat qilmoq",
                                    # "raise-ulg'aymoq",
                                    # "owe-tegishli bo'lmoq",
                                    # "evidence-dalil keltirmoq",
                                    # "fan-fanat bo'lmoq",
                                    # "increase-o'smoq",
                                    # "feed-ovqatlantirmoq",
                                    # "demand-talab qilmoq",
                                    # "organized-tashkil qilmoq",
                                    # "pack-paketlamoq",
                                    # "park-park qilmoq ",
                                    # "contain-o'z ichiga olmoq",
                                    # "burn-kuymoq",
                                    # "profit-foyda qilmoq",
                                    # "weight-tortmoq",
                                    # "baby-farzandli bo'lmoq carry-tashimoq",
                                    # "compare-taqqoslamoq exact-wake-uyg'onmoq",
                                    # "spend-sarflamoq",
                                    # "sail-suzmoq",
                                    # "rest-dam olmoq",
                                    # "marry-oipa qurmoq",
                                    # "prepare-tayyorlamoq",
                                    # "introduce-tanishtirmoq",
                                    # "collect-to'plamoq",
                                    # "rest-dam olmoq",
                                    # "land-remaind-qolmoq",
                                    # "guard-himoya qilmoq",
                                    # "focus-diqqatni jamlamoq",
                                    # "throw-otmoq",
                                    # "step-qadam qo'ymoq",
                                    # "spirit-ruxlantirmoq ",
                                    # "dissolve-erimoq",
                                    # "wave-qo'l siltamoq",
                                    # "explode-portlatmoq",
                                    # "breake-sindirmoq",
                                    # "close-yopmoq",
                                    # "come-kelmoq",
                                    # "copy-nusxa qilmqo",
                                    # "drop-tushmoq ",
                                    # "scatter-qochmoq",
                                    # "fear-qo'rqmoq",
                                    # "toss-uloqtirmoq",
                                    # "drift-olib ketmoq",
                                    # "inhabit-yashamoq",
                                    # "worship-ibodat qilmqo",
                                    # "tour-sayoxat qilmoq",
                                    # "assure-kafil bo'lmoq",
                                    # "kneel-tiz cho'kmoq",
                                    # "breakfast-nonushta qilmoq",
                                    # "scold-urishmoq",
                                    # "exploit-zulm o'tkazmoq",
                                    # "dream-orzu qilmoq",
                                    # "roast-qovurmoq",
                                    # "hinder-xalaqit bermoq",
                                    # "presume-tazyiq o'tkazmoq",
                                    # "dismiss-ishdan bo'shatmoq",
                                    # "drink-ichmoq",
                                    # "eat-yemoq",
                                    # "drive-xaydamoq",
                                    # "mean-mano anglatmoq",
                                    # "mix-aralashtirmoq",
                                    # "span-uzoq vaqt bo'lmoq",
                                    # "wander-aylanib yurmoq",
                                    # "please-iltimos qilmoq",
                                    # "sit-o'tirmoq",
                                    # "stand-turmoq",
                                    # "speak-gapirmoq",
                                    # "tear-yirtmoq",
                                    # "amazing-xayratlanmoq ",
                                    # "call-chaqirmoq ",
                                    # "beat-urmoq",
                                    # "watch-ko'rmoq",
                                    # "busy-band qilmoq",
                                    # "catch-ushlmoq",
                                    # "open-ochmoq",
                                    # "shoot-otmoq ",
                                    # "wear-kiymoq",
                                    # "good-band qilmoq",
                                    # "delete-o'chirmoq",
                                    # "interview-intervyu olmoq",
                                    # "kind-mexribon bo'lmoq",
                                    # "mark-belgilamoq",
                                    # "play-o'ynamoq",
                                    # "pain-og'rimoq",
                                    # "pleasure-zavqlanmoq",
                                    # "score-xisobni ochmoq",
                                    # "show-ko'rsatmoq ",
                                    # "share-bo'lishmoq",
                                    # "compel-majbur qilmoq",
                                    # "shower-dush qilmoq",
                                    # "suit-mos kelmoq",
                                    # "open-ochmoq",
                                    # "wear-kiymoq",
                                    # "irrigate-sug'ormoq",
                                    # "finance-mablag' ajratmoq",
                                    # "impose-jarima solmoq",
                                    # "oppress-zulm qilmoq",
                                    # "clean-tozalamoq",
                                    # "deter-aynitmoq ",
                                    # "digest-xazm qilmoq",
                                    # "tolerate-chidamoq",
                                    # "asses-baxolamoq",
                                    # "confer-maslaxatlashmoq",
                                    # "situate-joylashmoq",
                                    # "escort-qo'riqlab bormoq apecify-aniq belgilamoq",
                                    # "infer-xulosa qilmoq",
                                    # "hole-teshmoq",
                                    # "cite-misol keltirmoq",
                                    # "restrict-chegaralamoq",
                                    # "knit-to'qimoq",
                                    # "refine-takomillashtirmoq",
                                    # "lie-yotmoq",
                                    # "married-uylanmoq ",
                                    # "narrow-tor kelmoq",
                                    # "appal-qo'rqitmoq",
                                    # "examine-imtixon qilmoq",
                                    # "imagine-tasavvur qilmoq",
                                    # "respect-xurmat qilmoq",
                                    # "cancel-bekor qilmoq",
                                    # "norice-payqamoq",
                                    # "telephone-telefon qilmoq",
                                    # "own-ega bo'lmoq",
                                    # "rush-yuguslrmow",
                                    # "share-bo'lishmoq",
                                    # "advertise-reklama qilmoq",
                                    # "gain-erishmoq",
                                    # "prefer-afzal ko'rmoq",
                                    # "vote-ovoz bermoq ",
                                    # "cost-narxlamoq",
                                    # "scan-o'rganib chiqmoq",
                                    # "concude-yakunlamoq",
                                    # "cheat-g'irromlik qilmoq",
                                    # "persuade-ruxsat bermoq fight-jang qilmoq",
                                    # "depress-ruxni tushirmoq",
                                    # "debate-debat qilmoq",
                                    # "permit-ruxsat bermoq",
                                    # "exchange-almashtirmoq",
                                    # "chase-ov qilmoq",
                                    # "anger-jaxli chiqmoq",
                                    # "wrap-o'ramow",
                                    # "mistake-xato qilmoq",
                                    # "sink-cho'kmoq",
                                    # "noise-shovqin qilmoq",
                                    # "rectify-xatoni tuzatmoq",
                                    # "package-joylamoq",
                                    # "pause-to'xtamoq",
                                    # "opt-tanlamoq",
                                    # "elapse-tezda o'tib ketmoq",
                                    # "appal-qo'rqitmoq",
                                    # "allot-taqsimlamoq",
                                    # "exist-mavjud bo'lmoq",
                                    # "smoke-chekmow",
                                    # "publish-nashr wilmoq",
                                    # "appreciate-xurmat qilmoq",
                                    # "surprised-xayron qolmoq",
                                    # "flow-oqmoq",
                                    # "waste-isrof qilmoq ",
                                    # "argue-baxslashmoq",
                                    # "depend-tegishli bo'lmoq",
                                    # "associate-asos solmoq",
                                    # "indicate-ko'rsatmoq",
                                    # "blow-puflamoq",
                                    # "offer-taklif qilmoq",
                                    # "select-tanlamoq",
                                    # "treat-munosabatda bo'lmoq",
                                    # "bother-bezor qilmoq",
                                    # "explore-tatqiqot qilmoq",
                                    # "mention-aytib o'tmoq",
                                    # "appear-ko'rinmoq",
                                    # "cross-kesib o'tmoq",
                                    # "enter-kirmoq",
                                    # "locate-o'rnini aniqlamoq",
                                    # "dust-chang artmoq",
                                    # "refuse-inkor qilmqo",
                                    # "hurry-shoshilmoq",
                                    # "habit-odat bo'lmoq",
                                    # "iron-dazmollamoq",
                                    # "amaze-ajablanmoq",
                                    # "comfort-qulay bo'lmoq",
                                    # "deliver-tashimoq",
                                    # "earn-pul ishla topmoq",
                                    # "include-ichiga olmoq",
                                    # "manage-boshwarmoq",
                                    # "occur-sodir bo'lmoq",
                                    # "receive-qabul qilmoq",
                                    # "set-joylashtirmoq",
                                    # "steal-o'g'irlamoq ",
                                    # "advance-oldinga yurmoq",
                                    # "request-talab qilmoq",
                                    # "lower-pastga tushmoq",
                                    # "shame-uyalmoq",
                                    # "remove-olib tashlamoq",
                                    # "shoot-otmoq",
                                    # "swim-suzmoq",
                                    # "cheer-qichqirmoq",
                                    # "trust-ishonmoq",
                                    # "assist-yirdam bermoq",
                                    # "bake-non yopmoq",
                                    # "perform-bajarmoq",
                                    # "bell-jiringlamoq",
                                    # "bike-velasapet xaydamoq",
                                    # "blame-ayblamow",
                                    # "support-taminlamoq",
                                    # "unite-birlashtirmoq",
                                    # "involve-taqazo etmoq",
                                    # "organize-tashkillashtirmoq",
                                    # "cmproduce-ishlab chiqmoq",
                                    # "comment-fikr bermoq",
                                    # "recognize-tanimoq",
                                    # "attack-xujum qilmoq",
                                    # "diet-dieta qilmoq",
                                    # "fear-qo'rqmoq",
                                    # "drop-tomchilamoq",
                                    # "imply-nazarda tutmoq",
                                    # "maintain-davom ettirmoq",
                                    # "lunch-tushlik qilmoq",
                                    # "ride-minmoq ",
                                    # "suggest-taklif qilmoq",
                                    # "examine-imtixon qilmoq",
                                    # "recite-yoddan aytmoq",
                                    # "vanish-g'oyib bo'lmoq",
                                    # "pad-qarsak chalmoq",
                                    # "provide-taminlamoq",
                                    # "kidnap-o'g'irlamoq",
                                    # "creep-sudramoq",
                                    # "see-ko'rmlq",
                                    # "shock-shokka tushmoq",
                                    # "restore-egasiga qaytarmoq",
                                    # "spray-sepmoq",
                                    # "surprise-xayron qolmoq",
                                    # "tear-yirtmoq",
                                    # "translation-tarjima qilmqo",
                                    # " bark-darax po'slog' yulmoq",
                                    # "abandon-bosh tortmoq",
                                    # "stir-aralashtirmoq",
                                    # "endure-chidamoq",
                                    # "be-bo'lmoq",
                                    # "bite-tishlamoq",
                                    # "chop-kesmoq ",
                                    # "spoll-buzmoq",
                                    # "curse-so'kmoq",
                                    # "sneeze-aksirmoq",
                                    # "dip-suvga botirib olmoq",
                                    # "decay-chirimoq",
                                    # "bloom-gullamoq",
                                    # "count-xisoblamoq",
                                    # "dirty-kir bo'lmoq ",
                                    # "tease-masxara qilmoq",
                                    # "offend-xafa qilmoq",
                                    # "kid-axmoq qilmoq",
                                    # "irritate-g'azablantirmoq",
                                    # "venture-tavakkal qilmoq",
                                    # "overlook-yuqoridan qara",
                                    # "loose-yo'qotmoq",
                                    # "deceive-aldamoq",
                                    # "sustain-ko'tarib turmoq",
                                    # "occupy-egallamoq",
                                    # "exceed-oshib ketmoq",
                                    # "pleased-xursand bo'lmoq",
                                    # "arise-yuzaga kelmoq",
                                    # "run-yugurmoq",
                                    # "combine-birlashtirmoq",
                                    # "vary-farq qilmoq",
                                    # "slicebo'lmoq",
                                    # "snow-qor yog'moq",
                                    # "stroke-zarba bermoq",
                                    # "switch-o'chirmoq",
                                    # "tired-charchamoq",
                                    # "wreck-xaroba bo'lmoq",
                                    # "echo-aks sado bermoq",
                                    # "worried-xavotirlanmoq",
                                    # "torment-azob bermoq",
                                    # "anger-jaxli chiqmoq",
                                    # "moan-ingramoq",
                                    # "perish-vafot etmoq",
                                    # "soar-uchmoq",
                                    # "weep-ko'z yosh to'kmoq faint-xushidan ketmoq",
                                    # "operate-boshqarmoq",
                                    # "melt-erimoq",
                                    # "cut-kesmoq",
                                    # "soak-namlamoq",
                                    # "conceal-yashirmoq",
                                    # "volunteer-ko'ngilli bo'lmoq",
                                    # "grio-maxkam tutmoq",
                                    # "replace-joyiga qo'ymoq",
                                    # "tend-odatlanib qolmoq",
                                    # "disappointed-g'oyib bo'l",
                                    # "empty-bo'shatmoq",
                                    # "display-ko'rsatmoq",
                                    # "entr-kirmoq",
                                    # "forgive-kechirmoq",
                                    # "slap-shapaloqlamoq",
                                    # "smash-gumburlamoq",
                                    # "classify'sinflarga bo'lmoq",
                                    # "construct-tuzmoq",
                                    # "joke-xazillashmoq",
                                    # "surrender-taslim bo'lmoq",
                                    # "lure-qiziqtirmoq",
                                    # "sort-saralamoq",
                                    # "supply-taminlamoq",
                                    # "blow-esmoq",
                                    # "lean-egilmoq",
                                    # "rescue-qutqarmoq",
                                    # "pride-g'ururlanmoq",
                                    # "affect-tasir qilmoq",
                                    # "promise-vada bermoq ",
                                    # "lag-orqada qolmoq",
                                    # "ring-jiringlamoq",
                                    # "zoom-parvoz qilmoq",
                                    # "utter-ifodalamoq",
                                    # "sail-suzmoq kemada",
                                    # "sparkle-porlamoq",
                                    # "sift-elamoq",
                                    # "ruin-buzmoq",
                                    # "injure-jaroxatlanmoq ",
                                    # "flush-qizlarmoq",
                                    # "express-ifodalamow",
                                    # "crumble-uvalmoq",



############Ingliz tilida 500 ta kerakli so'zlar #######



                                    # "Bog'lovchilar",
                                    # "and-va",
                                    # "because-chunki",
                                    # "so-shuning uchun",
                                    # "or-yoki",
                                    # "If-agar",
                                    # "but-lekin",
                                    # "after-keyin",
                                    # "as-dek",
                                    # "since-dan beri",
                                    # "untill-gacha",
                                    # "while-paytda",
                                    # "for-uchun",
                                    # "unless-agar",
                                    # "as well as-shuningdek",
                                    # "eitheror- yokiyo",
                                    # "as long as-qadar",
                                    # "as if-xuddi",
                                    # "asas-dek kabı",
                                    # "that-ga qaraganda",
                                    # "so that-uchun",
                                    # "Maxsus so'roq gaplari Va Modal fellar",
                                    # "what-nima",
                                    # "when-qachon",
                                    # "who-kim",
                                    # "where-qayer",
                                    # "which-qaysi",
                                    # "how-qanday",
                                    # "how many-nechta",
                                    # "how much-qancha",
                                    # "should-kerak",
                                    # "must-kerak",
                                    # "have to - kerak",
                                    # "can-qila olmoq",
                                    # "could-qila olmoq",
                                    # "may-mumkin",
                                    # "might-mumkin",
                                    # "ought to-kerak",
                                    # "Hissiyotni idrk Va aqliy holatni ifodalovchi so'zlar",
                                    # "love-sevmoq",
                                    # "believe-ishonmoq",
                                    # "be-bo'lmoq",
                                    # "know-bilmoq",
                                    # "possess-egalik wilmoq",
                                    # "forget-unutmoq",
                                    # "remember-eslamoq",
                                    # "understand-tushunmoq",
                                    # "notice-payqamoq",
                                    # "feel-xis qilmoq",
                                    # "hear-eshitmoq",
                                    # "see-ko'rmoq",
                                    # "wishh-xohlamoa",
                                    # "want-istamoq",
                                    # "like-yoqtirmoq",
                                    # "hate-nafratlanmoq",
                                    # "seem-tuyilmoq",
                                    # "Predloglar",
                                    # "about-haqida",
                                    # "about-taxminan",
                                    # "about-atrofida",
                                    # "above-ustida",
                                    # "across-ko'ndalangiga",
                                    # "after-keyin",
                                    # "against-qarshi",
                                    # "along-bo'ylab",
                                    # "among-orasida",
                                    # "at-yonida,da",
                                    # "before-avval",
                                    # "behind-orqasida",
                                    # "below-ostida",
                                    # "beside-yonida",
                                    # "besides-dan tashqari",
                                    # "by-tomonidanvoditasida",
                                    # "between-o'rtasida",
                                    # "beyond-orqasida ",
                                    # "down-patga",
                                    # "during-davomida",
                                    # "exept-dan tashqari",
                                    # "for-uchun",
                                    # "from-uchun",
                                    # "in-da, ichida",
                                    # "inside-ichiga",
                                    # "with-bilan",
                                    # "witout-siz",
                                    # "within-ichida",
                                    # "up-yuqoriga",
                                    # "under-tagida",
                                    # "towards-ga qarab",
                                    # "to-ga",
                                    # "till-gacha",
                                    # "untill-gacha",
                                    # "round-atrofida",
                                    # "around-atrofida",
                                    # "past-yonidan",
                                    # "over-ustidan",
                                    # "out-tashqari",
                                    # "outside-tashqarida",
                                    # "on-da,ustida",
                                    # "of-ning",
                                    # "off-ustidan",
                                    # "inside-ichkarida",
                                    # "into-ochiga",
                                    # "out of dan tashqari ",
                                    # "since-dan buton",
                                    # "Phrasal verbs ",
                                    # "Ask after -  haqida yangilik so'ramoq",
                                    # "Bring up - voyaga yetkazmoq",
                                    # "Fall for - sevib qolmoq",
                                    # "Fall out (with)- urishib qolmoq",
                                    # "Get on (with) - (bilan) yaxshi chiqishmoq",
                                    # "Grow up - katta bo'lmoq, ulg'aymoq",
                                    # "Look down on - mensimay qaramoq",
                                    # "Look up to - hurmat qilmoq",
                                    # "Make up - yarashmoq",
                                    # "Pass away - olamdan o'tmoq",
                                    # "Pick on - kamsitavermoq",
                                    # "Put down - kamsitmoq",
                                    # "Settle down - ) jim bo'lib qolmoq; ) tinchib yashamoq",
                                    # "Stand up for - tarafini olmoq",
                                    # "Take aback - hayratlantirmoq",
                                    # "Go in - Ichkariga kirmoq",
                                    # "Walk in - Yurib kirmoq",
                                    # "Look out - tashqariga qaramoq / ehtiyot bo'l",
                                    # "Get out - transportdan tushmoq",
                                    # "Get on - transportga chiqmoq",
                                    # "Come on - Bo'laqol",
                                    # "Hold on - kutmoq",
                                    # "Carry on - davom etmoq",
                                    # "Go / walk / drive on - yo'lda davom etmoq",
                                    # "Fall off - tushib ketmoq",
                                    # "Take off - ko'tarilmoq",
                                    # "Stand up - turmoq",
                                    # "Go up - balandlamoq",
                                    # "Look up - qaramoq",
                                    # "Wake up - uyg'onmoq",
                                    # "Get up - o'rindan turmoq",
                                    # "Grow up - ulg'aymoq",
                                    # "Speak up - balandroq gapirmoq",
                                    # "Wash up - yuvmoq",
                                    # "Hurry up - shoshilmoq",
                                    # "Give up - harakatdan to'xtamoq",
                                    # "Sit down - o'tirmoq",
                                    # "Lie down - uyquga yotmoq",
                                    # "Fall down - qulamoq",
                                    # "Slow down - sekinlamoq",
                                    # "Break down - buzilmoq",
                                    # "Run away (yoki off) - yugurib ketmoq",
                                    # "Come back - qaytib kelmoq",
                                    # "Look round - burilib qaramoq",
                                    # "Fall over - yiqilmoq",
                                    # "Climb over - oshib o'tmoq",
                                    # "chance upon- tasodifan ko’rib qolmoq",
                                    # "change around - atrofni o’zgartirmoq",
                                    # "change into - holat va vaziyatni o’zgartirmoq; kiyimini almashtirmoq",
                                    # "change out of  - kiyimini almashtirmoq",
                                    # "clock up  - ma’lum bir miqdorga yetishmoq",
                                    # "club together - pul yig’moq (jamoa b-n)",
                                    # "close up- yopib tashlamoq",
                                    # "close down- ishlashdan toxtamoq (kompaniya uchun)",
                                    # "come off- muvaffaqiyatli chiqmoq",
                                    # "come on - rivojlanmoq",
                                    # "come up with- biror narsa haqida o’ylamoq",
                                    # "cut off- ta’minotni toxtatmoq",
                                    # "come on- namoish qilina boshlamoq",
                                    # "come out- chop etmoq",
                                    # "come forward- yordam yoki ma’lumot taklif etmoq",
                                    # "come down with- og’ir kasalikga chalinmoq",
                                    # "come round/to - xushiga kelmoq",
                                    # "come (a) round (to)- o’ziga kelmoq",
                                    # "come across - tasodifan duch kelmoq",
                                    # "come by- olishi qiyin bo’lgan narsani olmoq",
                                    # "167.    Go in - Ichkariga kirmoq",
                                    # "168.    Walk in - Yurib kirmoq",
                                    # "Look out - tashqariga qaramoq / ehtiyot bo'l",
                                    # "Get out - transportdan tushmoq",
                                    # "Get on - transportga chiqmoq",
                                    # "Come on - Bo'laqol",
                                    # "Hold on - kutmoq",
                                    # "Carry on - davom etmoq",
                                    # "Go / walk / drive on - yo'lda davom etmoq",
                                    # "Fall off - tushib ketmoq",
                                    # "Take off - ko'tarilmoq",
                                    # "Stand up - turmoq",
                                    # "Go up - balandlamoq",
                                    # "Look up - qaramoq",
                                    # "Wake up - uyg'onmoq",
                                    # "Get up - o'rindan turmoq",
                                    # "Grow up - ulg'aymoq",
                                    # "Speak up - balandroq gapirmoq",
                                    # "Wash up - yuvmoq ",
                                    # "Hurry up - shoshilmoq",
                                    # "Give up - harakatdan to'xtamoq",
                                    # "Sit down - o'tirmoq",
                                    # "Lie down - uyquga yotmoq",
                                    # "Fall down - qulamoq",
                                    # "Slow down - sekinlamoq",
                                    # "Break down - buzilmoq",
                                    # "Run away (yoki off) - yugurib ketmoq ",
                                    # "Come back - qaytib kelmoq",
                                    # "Look round - burilib qaramoq",
                                    # "Fall over - yiqilmoq",
                                    # "Climb over - oshib o'tmoq",
                                    # "Fed up with - joniga tegmoq",
                                    # "Famous for - mashxur",
                                    # "Frightened by -qorqmoq",
                                    # "Envious of - ichi qoralik qilmoq",
                                    # "Exhausted from - charchagan horigan",
                                    # "Dressed in - kiyinib olgan",
                                    # "Disappointed by - dan norozi bolmoq",
                                    # "Confused by - yanglishmoq",
                                    # "Capable of - ga qobilyatli bolmoq",
                                    # "Bored by - charchagan bolmoq",
                                    # "Angry with - achchiqlanmoq",
                                    # "After all - ga qaramasdan",
                                    # "All along - har doim",
                                    # "All of a sudden - tosatdan",
                                    # "All the same -bir xil",
                                    # "As a rule - odatda ",
                                    # "As far as I am concerned - mening fikrimcha",
                                    # "As for me - men oylashimcha",
                                    # "Be about to - tayyor bolmoq",
                                    # "Be back on ones feet - healthy again or better financially ",
                                    # "Be beside oneself - juda havotirlangan, achchiqlangan ",
                                    # "Be in the red - qarzga botmoq",
                                    # "Come across - tosatdan korib qolmoq",
                                    # "Catch ones eye - etiborini tortmoq",
                                    # "Have a good time - yaxshi vaqt o'tkazmoq",
                                    # "Have a rest - dam olmoq",
                                    # "Have a break - tanaffus qilmoq",
                                    # "Have a cold - shamollamoq",
                                    # "Have  meals a day - kuniga  mahal ovqatlanmoq",
                                    # "Have a headache - boshi ogrimoq",
                                    # "Have a toothache - tishi ogrimoq",
                                    # "Have a backache - beli ogrimoq ",
                                    # "Have a stomachache - oshqozoni ogrimoq ",
                                    # "Have a sore throat - tomogi ogrimoq",
                                    # "Have a flu - gripp bolmoq",
                                    # "Have a cough - yotalmoq",
                                    # "Have a sneeze - aksirmoq",
                                    # "Have one's English - Ingliz tili bilan shug'ullanmoq",
                                    # "Have a smoke - chekmoq ",
                                    # "Have a tea - choy ichmoq",
                                    # "Have a dictation - diktant yozmoq",
                                    # "Noto'g'ri Fellar ro'yxati",
                                    # "abide- abode -abode-turmoq",
                                    # "arise -arose -arisen-paydo bo'lmoq",
                                    # "awake -awoke -awoken-uyg'onmoq",
                                    # "be- was/were -been-bo'lmoq",
                                    # "bear -bore - born-tug'ilmoq",
                                    # "beat -beat -beaten-urmoq",
                                    # "become -became -become-aylanib qolmoq",
                                    # "beget -begat -begotten-paydo bo'lmoq",
                                    # "begin- began -begun-boshlamoq",
                                    # "bend -bent -bent-egilmoq",
                                    # "bet -bet -bet-tikilmoq",
                                    # "bid -bade-bidden-unutmoq",
                                    # "bite -bit -bitten-tishlamoq",
                                    # "bleed -bled- bled-qon ketmoq",
                                    # "blow- blew -blown-puflamoq,esmoq",
                                    # "break -broke -broken-sindirmoq",
                                    # "bring- brought -brought-olib kelmoq",
                                    # "broadcast -broadcast- broadcast-radio orqali uzatmoq",
                                    # "build- built -built-qurmoq",
                                    # "burn -burnt -burnt-kuymoq",
                                    # "burst- burst -burst-yorilmoq",
                                    # "buy- bought -bought-sotib olmoq can -could -could-qila olmoq",
                                    # "cast -cast -cast-rolga tayinlamoq",
                                    # "catch -caught -caught-ushlamoq",
                                    # "choose- chose- chosen-tanlamoq",
                                    # "cling -clung -clung-chirmashmoq",
                                    # "clothe- clothed - clothed-kiyintirmoq",
                                    # "come- came- come-kelmoq",
                                    # "cost -cost -cost-narxlamoq",
                                    # "creep- crept- crept-emaklamoq",
                                    # "cut- cut -cut-kesmoq",
                                    # "deal- dealt -dealt-muomila qilmoq",
                                    # "dig -dug -dug-qozmoq",
                                    # "dive -dived -dove-suvga kala tashlamoq",
                                    # "do -did -done-bajarmoq",
                                    # "draw -drew -drawn-chizmoa",
                                    # "dream -dreamt -dreamt-orzu qilmoq",
                                    # "drink -drank -drunk-ichmoq",
                                    # "drive -drove -driven-xaydamoq",
                                    # "dwell -dwelt -dwelt-yashamoq",
                                    # "eat-ate-eaten-yemoq",
                                    # "fall - fell - fallen-ko'z tushmoq",
                                    # "feed- fed -fed-boqmoq",
                                    # "feel -felt-felt-his qilmoq",
                                    # "fight- fought -fought-jang qilmoq",
                                    # "find -found- found-topmoq",
                                    # "flee- fled- fled-qochmoq",
                                    # "fling -flung -flung -irg'itmoq",
                                    # "fly -flew- flown-uchmoq",
                                    # "forbid -forbade -forbidden-man qilmoq",
                                    # "forget-forgot- forgotten-unutmoq",
                                    # "forgive-forgave -forgiven-kechirmoq",
                                    # "forsake-forsook -forsaken-umirbod talk etmoq",
                                    # "freeze-froze -frozen-muzlamoq",
                                    # "get-got -gotten-olmoq",
                                    # "give-gave -given-bermoq",
                                    # "go -went -gone-bormoq",
                                    # "grind ground ground-yanchmoq",
                                    # "grow -grew -grown-ulg'aymoq",
                                    # "hang -hung- hung-osmoq",
                                    # "have -had -had-bor bo'lmoq",
                                    # "hear- heard-eshitmoq heard-eahitmoq",
                                    # "hide- hid- hidden-yashinmoq",
                                    # "hit -hit -hit-urmoq",
                                    # "hold -held -held-ushlamoq",
                                    # "hurt- hurt- hurt-jaroxatlanmoq",
                                    # "keep kept -kept-saqlamoq",
                                    # "kneel -knelt -knelt-tiz cho'kmoq",
                                    # "know -knew -known-bilmoq",
                                    # "lay laid laid-yotqizmoq",
                                    # "lead led led-olib bormoq",
                                    # "lean -leant-leant -og'moq",
                                    # "leap- leaped -leaped",
                                    # "learn -learnt -learnt-o'rganmoq",
                                    # "leave -left -left-jo'namoq",
                                    # "lend -lent -lent-qarz olmoq",
                                    # "let- let -let-ruxsat bermoq",
                                    # "lie- lay -lain-aldamoq",
                                    # "light -lighted -lighted-yorishmoq",
                                    # "lose- lost -lost-yo'qotmoq",
                                    # "make- made -made-yasamoq",
                                    # "mean- meant- meant-mano anglatmoq",
                                    # "meet -met- met-uchrashmoq",
                                    # "mow -mowed- mown-o't o'rmoq",
                                    # "offset -offset- offset-o'rnini to'ldirmoq",
                                    # "overcome- overcame- overcome-yengmoa",
                                    # "partake -partook- partaken-ishtirok etmoq",
                                    # "pay- paid -paid-to'lamoq",
                                    # "plead-pleaded - pleaded-o'tinib so'ramoq",
                                    # "preset -preset- preset-oldindan o'rnatmoq",
                                    # "prove -proved -proven-isbotlamoq",
                                    # "put- put -put-qo'ymoq",
                                    # "quit -quit- quit-tashlab ketmoq",
                                    # "read- read -read-o'qimoq",
                                    # "relay -relaid- relaid-olib bermoq",
                                    # "rid -rid- rid-qutulmoq,",
                                    # "ring- rang- rung-jiringlamoq",
                                    # "rise- rose- risen-o'smoq",
                                    # "run- ran -run-yugurmoq",
                                    # "say -said- said-aytmoq",
                                    # "see- saw- seen-ko'rmoq",
                                    # "seek -sought -sought-izlamoq",
                                    # "sell -sold- sold-sotmoq",
                                    # "send- sent- sent-yubormoq",
                                    # "set- set -set-joylamoq",
                                    # "shake- shook-joylamoq shaken-silkitmoq",
                                    # "shed -shed -shed-to'kmoq",
                                    # "shine- shone- shone-porlamoq",
                                    # "shoe -shod -shod-taqa taqmoq",
                                    # "shoot- shot -shot-otmoq",
                                    # "show -showed- shown-kos'rsatmoq",
                                    # "shut- shut- shut-yopmoq",
                                    # "sing -sang -sung-kuylamoq",
                                    # "sit- sat -sat-o'tirmoq",
                                    # "slay -slew- slain-o'ldirmoq",
                                    # "sleep- slept- slept-uxlamoq",
                                    # "slide- slid- slid-sirpanmoq",
                                    # "slit -slit- slit-yirtmoq",
                                    # "smell -smelt -smelt-xidlamoq",
                                    # "sow -sowed- sown-sepmoq",
                                    # "speak- spoke- spoken-gapirmoq",
                                    # "speed -sped- sped-tez qilmoq",
                                    # "spell- spelt- spelt-xarflamoq",
                                    # "spend -spent -spent-sarflamoq",
                                    # "spill -spilt -spilt -to'kmoq",
                                    # "spin -spun -spun-aylantirmoq",
                                    # "spit -spat-spat-tupurmoq",
                                    # "split -split -split-tilmoq",
                                    # "spoil -spoilt- spoilt-to'kmoq",
                                    # "spread- spread -spread-taratmoq",
                                    # "spring -sprang- sprung",
                                    # "stand- stood- stood-turmoq",
                                    # "steal -stole- stolen-o'g'irlamoq",
                                    # "stick -stuck- stuck-tiqmoq",
                                    # "sting- stung- stung-nayza sanchmoq",
                                    # "stink -stank -stunk-xid chiqarmoq",
                                    # "strike- struck- stricken-urmoq",
                                    # "strive -strove -striven-intilmoq",
                                    # "swear -swore -sworn-qasam ichmoq",
                                    # "sweat -sweat- sweat-terlamoq",
                                    # "sweep -swept -swept-supurmoq",
                                    # "swell -swelled - swollen-shishmoq",
                                    # "swim -swam- swum-suzmoq",
                                    # "swing -swung- swung-tebratmoq",
                                    # "take -took- taken-olmoq",
                                    # "teach -taught- taught-o'qitmoq",
                                    # "tear -tore -torn-yirtmoq",
                                    # "tell- told- told-aytmoq",
                                    # "think -thought -thought-o'ylamoq",
                                    # "thrive -throve- thriven-o'smoq",
                                    # "throw -threw- thrown-uloqtirmoq",
                                    # "thrust -thrust- thrust-itarib yubormoq",
                                    # "undergo- underwent- undergone-boshdan kechirmoq",
                                    # "understand -understood- understood-tushunmoq",
                                    # "wake- woke- woken-uyg'onmoq",
                                    # "wear- wore -worn-kiymoq",
                                    # "weep- wept -wept-ko'z yosh to'kmoq",
                                    # "wet- wet- wet-namlamoq",
                                    # "win won won-yutmoq",
                                    # "wind wound wound-o'ramoq",
                                    # "wring wrung wrung-siqib chiqarmoq",
                                    # "write wrote written-yozmoa ✔Phrasal_verbs ",
                                    # "Carry on - davom ettirmoq ",
                                    # "Get round to - (uzoq o'ylangan rejani) boshlamoq ",
                                    # "Get up to - ) bajarmoq; ) qilmaslik kerak bo'lgan ishni qilmoq ",
                                    # "Go in for - ) musobatga kirmoq; ) yoqtirmoq ",
                                    # "Go off - yomon ko'rib qolmoq ",
                                    # "Join in - a'zo bo'lmoq ",
                                    # "Knock out - ) o'yindan chiqarib yubormoq; ) xushidan ketkizmoq",
                                    # "Look out - ehtiyot bo'lmoq ",
                                    # "Pull out - to'xtatmoq, voz kechmoq ",
                                    # "Put off - kechiktirmoq ",
                                    # "Put up with - chidamoq, bardosh bermoq ",
                                    # "Take to - odat sifatida boshlamoq ",
                                    # "Take up - ) (hobby, sport) boshlamoq; ) vaqtni olmoq ✅ Juda yaxshi deyishning turli ko'rinishlari:",
                                    # " Great",
                                    # " Fantastic",
                                    # " Wonderful",
                                    # " Splendid",
                                    # " Excellent ",
                                    # " Amazing ",
                                    # " Incredible",
                                    # " Awesome",
                                    # " The best",
                                    # " Impressive ",
                                    # " Breathtaking  ",
                                    # "Marvellous",
                                    # " Unbelievable",
                                    # " Remarkable  ",
                                    # "Astonishing",
                                    # " Extraordinary",
                                    # " Fascinating",
                                    # " Mind blowing",
                                    # " Unimaginable",
                                    # " Magnificent",
                                    # " Tremendous",
                                    # "🔎Telegramga oid so'zlar:",
                                    # "Channel - Kanal",
                                    # "Group - Guruh",
                                    # "Forward - xatni yangi adressga jo'natmoq",
                                    # "Type - yozmoq",
                                    # "Online - Internetga ulangan",
                                    # "Record voice - ovoz yozmoq",
                                    # "Send file - rasm, video yubormoq",
                                    # "Search - qidirmoq (qidiruv)",
                                    # "Last seen at -da oxiri ko'rilgan",
                                    # "Last seen recently - yaqinda ko'rilgan",
                                    # "Last seen within week (month) - oxiri hafta davomida ko'rilgan (oy davomida)",
                                    # "Deleted account - o'chirilgan akkaunt ",
                                    # "Block - to'smoq",
                                    # "Join - qo'shilmoq",
                                    # "Leave - tark etmoq",
                                    # "Add - qo'shmoq",
                                    # "🔥 Eng koʻp ishlatiladigan iboralar:",
                                    # "Catch me later - Keyinroq gaplashamiz",
                                    # "Clear the way! - Yo'lni bo'shating",
                                    # "Come back anytime - Xohlagan paytda yana tashrif buyuring",
                                    # "Come right in - Kirib o'ting",
                                    # "Could I call you later? - Keyinroq qo'ng'iroq qilsam maylimi?",
                                    # "Could I join you? - Sizga qo'shilsam bo'ladimi? Don't push (me)! - Menga bunday gapirmang! ",
                                    # "Enjoy your meal! - Yoqimli ishtaha Guess what! - Nimaligini toping!",
                                    # "I doubt that - Shubhalanayapman",
                                    # "I had a lovely time - Vaqtimni yaxshi o'tkazdim",
                                    # "I spoke too soon - O'ylamay gapirib yuboribman",
                                    # "Keep in touch - Aloqada bo'lib turing",
                                    # "Leave it to me - Buni menga qo'yib bering",
                                    # "Make it two - Menga ham qo'shib oling ( asosan kafelarda )",
                                    # "No can do - Buni qila olmayman",
                                    # "No way! - Hechamda ! ",
                                    # "Pull up a chair - Bizga qo'shiling",
                                    # "Shut up! - Og'zingni yop",
                                    # "Sit down, please - O'tiring marhamat",
                                    # "So'zlashuv uchun: Lug'at",
                                    # "⚡ Foydali  ibora",
                                    # "Right you are  - Siz haqsiz ",
                                    # " Sure  - Turgan gap ",
                                    # "That’s fine  - Juda soz bo’libdi ",
                                    # "That’s just it  - Xuddi shunday ",
                                    # "That’s right  - To’g’ri ",
                                    # "Undoubtedly  - Shubhasiz ",
                                    # "Very good  - Juda yaxshi ",
                                    # "Willingly  - Bajonidil ",
                                    # "With pleasure  - Jon deb ",
                                    # "Yes, certainly  - Ha, albatta  ",
                                    # "Rest of my life  - Butun umr, qolgan umr",
                                    # "Piss somebody  - Jonga tegmoq, g'azablanmoq",
                                    # "Beg  - Yolvormoq",
                                    # "Exact same  - Huddi shunaqa, bir xil",
                                    # "Alohida iboralar",
                                    # "What time is it?- Soat necha bo'ldi?",
                                    # "Give me this-! Buni menga bering ",
                                    # "Are you sure? -Aminmisiz?",
                                    # "Take this! - Oling!",
                                    # "It's freezing - Juda sovuq",
                                    # "It's cold -Sovuq",
                                    # "It's hot -Issiq",
                                    # "Do you like it?- Senga Yoqadimi?",
                                    # "I really like it!- Menga yoqadi!",
                                    # "I'm hungry- Qornim och",
                                    # "I'm thirsty-Chanqadim",
                                    # "He is funny- U kulguli",
                                    # "In The Morning-Ertalab",
                                    # "In the evening -Kechqurun",
                                    # "At Night -Tunda",



########Arab harflari#########



                                    # "ا - alif",
                                    # "ض - dod",
                                    # "ص - sod",
                                    # "ث - sa",
                                    # "ق - qof",


                                    # "ف - fa",
                                    # "غ - g'oyn",
                                    # "ع - ayn",
                                    # "ه - ha",
                                    # "خ - xo",


                                    # "ح - ha",
                                    # "ج - jim",
                                    # "د - dal",
                                    # "ش - shin",
                                    # "س - sin",


                                    # "ي - ya",
                                    # "ب - ba",
                                    # "ل - lam",
                                    # "ا - alif",
                                    # "ت - ta",

                                    # "ن - nun",
                                    # "م -mim",
                                    # "ك - kaf",
                                    # "ط - to",
                                    # "ر - ro",


                                    # "و -vav",
                                    # "ز - za",
                                    # "ظ - zzo",
                                    # "ذ - zal",
                                    #



###################English conversation####################



                                    # "story - hikoya, voqea",
                                    # "share - baham ko'rmoq",
                                    # "fancier - ishqivoz",
                                    # "how - qanday",
                                    # "by - yaqin",


                                    # "extra - qo'shimcha",
                                    # "horoscope - munajjimlar bashoarati",
                                    # "will - bo'ladi",
                                    # "career - martaba, tez harakat qilmoq",
                                    # "which - qaysi",


                                    # "lucky - omadli",
                                    # "written - yozma",
                                    # "where - qayerda",
                                    # "was - edi",
                                    # "done - qilingan",


                                    # "cushion - yostiq",
                                    # "wear - kiymoq",
                                    # "off - to'xtatmoq",
                                    # "take - olmoq",
                                    # "just - faqat, bor yo'g'i, hozirgina",


                                    # "must - kerak",
                                    # "anybody - hech kim",
                                    # "same - bir xil",
                                    # "heard - eshitib qolmoq",
                                    # "get - olmoq",


                                    # "keep - saqlamoq",
                                    # "anything - biror narsa",
                                    # "could - qo'lidan",
                                    # "ticket - chipta",
                                    # "got - bor",


                                    # "been - edi",
                                    # "can - qila olmoq",
                                    # "anyway - harholda",
                                    # "wait - kutmoq",
                                    # "met - uchrashdi",


                                    # "blonde - oqsariq",
                                    # "crazy - aqldan ozgan",
                                    # "ask - so'ramoq",
                                    # "said - dedi",
                                    # "maybe - balki, ehtimol",


                                    # "bit - parcha",
                                    # "those - ular",
                                    # "were - edi",
                                    # "luxury - hashamatli",
                                    # "exotic - ajoyib",


                                    # "best - eng yaxshi",
                                    # "mix - aralashtirib yubormoq",
                                    # "charity - xayriya",
                                    # "resign - ishdan bo'shamoq",
                                    # "ring - uzuk, aylana, qurshab olmoq",


                                    # "dear - aziz",
                                    # "disappear - yo'qolmoq",
                                    # "still - hali ham",
                                    # "brush - taramoq, cho'tkalamoq",
                                    # "comb - taroq",


                                    # "took - oldi",
                                    # "irresistible - qaytarib bo'lmaydigan",
                                    # "had - bor",
                                    # "darling - mahbubim",
                                    # "lost - yo'qolgan",


                                    # "fault - ayb",
                                    # "show - ko'rsatmoq",
                                    # "until - gacha",
                                    # "hope - umid",
                                    # "shall - keladir",


                                    # "sort - saralamoq",
                                    # "dustman - axlat tozalovchi",
                                    # "prepare - tayyor bo'lmoq",
                                    # "unfortunate - badbaxt",
                                    # "wrote - yozgan",


                                    # "told - aytdi",
                                    # "made - yasalgan",
                                    # "windscreen - shisha",
                                    # "mean - degani",
                                    # "while - paytda",


                                    # "called - deyiladi",
                                    # "should - kerak",
                                    # "could you - qila olasizmi",
                                    # "use - ishlatmoq",
                                    # "do - qilmoq",


                                    # "way - yo'l",
                                    # "place - joy",
                                    # "government - hukumat",
                                    # "yesterday - kecha",
                                    # "everything - hammasi",


                                    # "improve - yaxshilanmoq",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",



###############***********##################



                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",

                                ####50#####

                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


###############***********##################



                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",

                                ####50#####

                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


###############***********##################



                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",

                                ####50#####

                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


###############***********##################



                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",

                                ####50#####

                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


###############***********##################



                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",

                                ####50#####

                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


###############***********##################



                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",

                                ####50#####

                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


###############***********##################



                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",

                                ####50#####

                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",


                                    # "",
                                    # "",
                                    # "",
                                    # "",
                                    # "",



















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