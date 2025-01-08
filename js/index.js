console.clear(); // Shu qatordan oldingi loglarni tozalash
// Keyingi kodni yozishni davom ettiring!
// console.log("Hello world ");
// let salom = "salom";
// console.log("salom");
// sal sdf j="kdsajdf";
// console.log(sal sdf j);
// let salom;
// let salom=null;
// let salom=Symbol('salom');
// const salom=BigInt(478932);
// console.log(typeof(salom));
// let yosh =23;
// console.log(yosh);
// yosh=24;
// console.log(yosh);
// const id=22;
// console.log(id);
// id=33;
// "use strict";
// salom="salom";
// console.log(salom);
// const array1=[1,2,3]
// const array2=[4,5,6]
// const array3=array1.concat(array2);
// console.log(array3);
// const dasturchi = {
//     ism:"Ulug'bek",
//     yosh:23,
// }
// console.log(typeof dasturchi);
// console.log(dasturchi.ism);
// console.log(dasturchi.yosh);
// console.log(dasturchi["ism"]);
// console.log(dasturchi['yosh']);
// const dasturchi={
//     ism:"Ulug'bek",
//     yosh:23,
//     manzil:{
//         davlat:"O'zbekiston",
//         shaxar:"Toshkent",
//         uy:7
//     }
// }
// console.log(dasturchi['manzil']);
// console.log(dasturchi);
// console.log(dasturchi.manzil.davlat);
// const dasturchi={
//     ism:"Ulug'bek",
//     yosh:23,
//     salomlashish: function(){
//         console.log('salomlashish');
//     }
// }
// console.log(dasturchi.salomlashish)
// console.log(dasturchi.salomlashish())
// const dasturchi={
//     ism:"Ulug'bek",
//     yosh:23,
//     salom:function(){
//             console.log("salom " + this.ism);
//     }
// }
// // dasturchi.salom();
// const dasturchi={
//     ism:"Ulug'bek",
//     yosh:23
// }
// console.log(Object.keys(dasturchi));
// console.log(Object.values(dasturchi));
// console.log(Object.entries(dasturchi));
// const number=-2;
// if(number>0){
//     console.log("berilgan son musbat");
// }
// console.log("if dan keyingi qator");
// const number =-2;
// if(number>0){
//     console.log("Berilgan son musbat");
// }else{
//     console.log("Berilgan son manfiy");
// }
// console.log("else blocki if blockidan keyin yoziladi.")
// const number=0;
// if(number>0){
//     console.log("Berilgan son 0 dan katta");
// }else if(number===0){
//     console.log("Berilgan son 0 ga teng");
// }else{
//     console.log("Berilgan son manfiy");
// }
// console.log("if ese dan keyingi kod");
// const number=3;
// let output;

// switch (number){
//     case 1:
//         output="bir";
//         break;
//     case 2:
//         output="ikki";
//         break;
//     case 3:
//         output="uch";
//         break;
//     default:
//         output="Qiymat topilmadi.";
//         break;
// }
// console.log(output);
// const salom="Assalomu aleykum";
// let output;
// switch (salom){
//     case "salom":
//         output="Assalomu aleykum";
//         break
//     case "Assalomu aleykum":
//         output="Va aleykum assalom";
//         break
//     default:
//         output="qalay";
//         break
// }
// console.log(output)
// for(let i=0;i<10;i++){
//     console.log(i);
// }
// let sum=0;
// for(let i=0;i<=10;i++){
//     sum+=i;
// }
// console.log(sum);
// for(let i=0; i<10;i++){
//     console.log(i+1,"salom");
// }
// let sum=0;
// for(let i=1;i<=10;i++){
//     sum+=i;
// }
// console.log(sum);
// for(let i=1; i<=10; i++){
//     if(i===4){
//         break
//     }
//     console.log(i);
// }
// for(let i=0;i<=10;i++){
//     if(i===3){
//         console.log(i+" bo'lganda o'tkazib yubordim");
//     }
//     console.log(i)
// }
// let i=1;
// while(i<=10){
//     console.log(i+'salom');
//     i++;
// }
// let i=1;
// let sum=0;
// while(i<=10){
//     console.log("salom dunyo!");
//     i++;
// }
// let i=0;
// let sum=0;
// while(i<=10){
//     i++;
//     console.log(i);
//     if(i===3){
//         console.log("${i} ni o'tkazib yubordi");
//         continue
//     }
//     if(i===5){
//         console.log("${i} da to'xtadik");
//         break
//     }

// }
// let i=0;
// do{
//     console.log("salom dunyo!");
//     i++
// }while(i<=10)
// do{
//     console.log("sallom dunyo!");
// }while(false);
// const inRange = (min,max,number)=>{
//     if(number>=min && number<=max){
//         console.log("berilgan son min va max qiymat orasida");
//     }else{
//         console.log("Berilgan son min va max orasida emas");
//     }
// }
// let min=10;
// let number=40;
// let max=30;
// inRange(min,max,number);
// const simpleCalculator=(son1,belgi,son2)=>{
//     switch(belgi){
//         case "qo'shuv":
//             console.log(son1+son2);
//             break;
//         case "ayiruv":
//             console.log(son1-son2);
//             break;
//         case "ko'paytiruv":
//             console.log(son1*son2);
//             break;
//         case "bo'luv":
//             console.log(son1/son2);
//             break;
//     }
// }
// let son1=3;
// let son2=4;
// let belgi="qo'shuv";
// belgi="ayiruv"
// belgi="ko'paytiruv"
// belgi="bo'luv"
// simpleCalculator(son1,belgi,son2);
// const myFunction=(array)=>{
//     tanlangan=array[0];
//     for(let i=1;i<array.length;i++){
//         if(tanlangan<array[i]){
//             tanlangan=array[i];
//         }
//         else{
//             continue
//         }
//     }
//     return tanlangan;
// }
// const array=[123,43434,43434,2434,9708909809,34,434,34,35,34,535565,75,768,67];
// let salom=myFunction(array);
// console.log(`Berilgan ${array} dan eng katta son ${salom} sonidir`);
// const salom=document.getElementById('sarlavha');
// console.log(salom);
// salom.remove();
// const inputel = document.getElementsByName('input');
// console.log(inputel);
// inputel[0].remove();
// const salom = document.getElementsByTagName('p');
// salom[0].remove();
// salom[0].remove();
// const salomlar=document.getElementById('salomlar');
// salomlar.textContent="yangi matn"
// const inputId = document.getElementById('inputId');
// inputId.value=33434;
// const pId=document.getElementById('pId');
// pId.textContent="<h1>salomlar</h1>"
// pId.innerHTML="<h2>salomalrimiz</h2>"
// const poragraph = document.createElement('p');
// console.log(poragraph);
// const text = document.createTextNode('bu yangi matn');
// const box=document.getElementById('box');
// box.appendChild(poragraph);
// console.log(box);
// console.log(box.children);
// console.log(box.parentElement);
// console.log('salom');
// console.log("salkajsdkjf");
// const myFunction=()=>{
//     const salom = document.getElementById('salom');
//     salom.textContent='Assalomu aleykum';
// }
// const changeHeading = () =>{
//     const heading = document.getElementById('salom');
//     heading.textContent="Assalomu aleykum";
// }
// const btn = document.getElementById("buttonId");
// btn.addEventListener('click',changeHeading);
// const notifyDoubleClick = () => {
//     console.log('Element ikki marta bosildi');
// }
// const btn = document.getElementById('btn');
// btn.addEventListener('dblclick',notifyDoubleClick);
// document.addEventListener('keydown', event=>{
//     console.log('key: '+event.key);
//     console.log('code: '+event.code);
// });
// console.log(1)
// console.log(2)
// console.log('Azizbek');
// let ism="Ahror";
// console.log(ism);
// let yosh = 24;
// console.log(ism,yosh);
// yosh=25;
// console.log(yosh);
// const familiya = "Soliyev";
// console.log(familiya);
// var nom="Jizzax";
// console.log(nom);
// var nom="ksdkf";
// console.log(nom);
// /* Var eski bo'lganligi uchun faqat let va const dan foydalanamiz var muammolar keltirib chiqaradi.*/
// console.log('email');
// let email = "gmail.com";
// console.log(email);
// console.log("Bu yangi log");
// let ism = "Asliddin";
// let familiya="O'mirboyev";
// console.log(birga=ism + " " + familiya);
// console.log(ism[0]);
// console.log(ism[3]);
// console.log(ism.length);
// console.log(ism.toUpperCase());
// let result = ism.toLowerCase();
// console.log(result);
// let email = "kuchukcahni@top";
// console.log(email)
// const result = email.indexOf('@');
// console.log(result);
// let email = "     akhrorweb@gmail.com      ";
// let result = email.indexOf('a');
// console.log(result);
// let result2 = email.lastIndexOf('a');
// console.log(result2);
// 0a1k2h3r4o5r6w7e8b9@10 shu tarzda oladi.
// let result = email.slice(0,1);
// console.log(result);
// let result2 = email.slice(9,10);
// console.log(result2);
// let result = email.substr(4,10);
// console.log(result.length);
// let result = email.replace("a","d");
// console.log(result);
// let result = email.charAt();
// console.log(result);
// let result = email.toUpperCase();
// console.log(result);
// let salom = email.toLowerCase();
// console.log(salom);
// console.log(email);
// let result = email.trim();
// console.log(result);
// console.log(result.length,email.length);
// let result = email.split("");
// let result2 = email.trim().split('a')
// console.log(result);
// console.log(result2);
// let radius=10;
// const pi=3.14;
// console.log(pi,radius);
// console.log(10/2);
// console.log(radius%3);
// console.log(12%5);
// let result = pi*radius**2;
// console.log(result);
// const title="Rastomojka";
// const author = "lag'mon";
// const likes=35000000;

// let result = title + " " + author + " " + likes;
// console.log(result);
// let result = `${title},${author},${likes}`;
// console.log(result);
// let result=`${<h1>salomlar</h1>},${<title>author</title>}`;
// console.log(result);
// console.log(mehmonlar);
// mehmonlar[0] = "Aziz";
// console.log(mehmonlar);
//console.log(mehmonlar[1]);
// const mehmonlar = ['Azizbek','Asliddin','Ahror'];
// let number = [3,3,4,5,6,4];
// console.log(number.length);
// let result = mehmonlar.indexOf("Azizbek");
// console.log(result)
// console.log(mehmonlar.indexOf("Asliddin"));
// let salom =mehmonlar.indexOf("Ahror")
// console.log(salom);
// let result = mehmonlar.concat(number);
// console.log(result);
// mehmonlar.push("Davlatbek");
// mehmonlar.pop();
// mehmonlar.pop();
// mehmonlar.push("Ahrorbek");
// console.log(mehmonlar);
// let age;
// console.log(age,age+3,`${age}`);
// null matematik jihatdan 0 ga teng!
// let age1=null;
// console.log(age1,age1+3,`${age1}`);
// let tree = [true, false, "true", "false"];
// console.log(tree);
// let email = "akhrorweb@gmail.com";
// let result = email.includes('@');
// console.log(result);
// let age = 25;
// console.log(age==25);
// console.log(age=="25");
// Ikkitalik tengda xar hil turdagi ma'lumotlarni bir biriga teng ekanligini aniqlashimiz mumkin ekan.
// console.log(age != 25);
// kuchli taqqoslashlar bunda turi ham qiymati ham teng bo'lishi kerak
// console.log(age===25);
// console.log(age==="25");
// console.log(age !== 25);
// console.log(age !=="25");
// let matn = '3';
// console.log(234+matn);
// console.log(323+Number(matn));
// let text = String(323);
// let raqam = Number("3244");
// console.log(typeof(text));
// console.log(typeof(raqam));
// let result = String(343);
// console.log(typeof result);
// let ism = prompt("Ismingizni kiriting:");
// console.log(`Sizning simingiz ${ism} ekan.`);
// let ism = prompt("Ismingizni kiriting:");
// console.log(ism);
// let boshHarf=ism.charAt().toUpperCase();
// let davomi = ism.slice(1).toLowerCase();
// alert(`salom ${boshHarf+davomi}`);
// let imim = prompt("Ismingizni kiriting:");
// alert(`salom ${ism.toLocaleLowerCase()}`);
// for (let a=0;a<10;a++){
//     console.log("salom");
// }
// const array1 = ['Azizbek','Asliddin','Ahror'];
// for (let i=0;i<array1.length;i++){
//     console.log(array1[i]);
// }
// let i=0;
// while(i<array1.length){
//     console.log(array1[i].toUpperCase());
//     i++
// }
// let a=5;
// do{
//     console.log("salom");
//     a++;
// }while(a<10)
// const age = 21;
// if(age>20){
//     console.log('siz 20 yoshdan kattasiz.');
// }
// const parol = 'dfdfdfdfdfdej';
// if(parol.length>12){
//     console.log('Sizning parolinggiz juda ham katta!')
// }else if(parol.length<8){
//     console.log("Sizning parolingiz yetarlicha kuchli emas!");
// }else{
//     console.log("Sizning parolingiz yetarlicha kuchli!");
// }
// const natijalar = [12,23,4,0,34,23,3,100,243,34];
// for (let i=0;i<natijalar.length;i++){
//     if(i===0){
//         console.log("Bu joyda 0 tashlab ketildi.")
//         continue;
//     }
//     if(natijalar[i]===100){
//         console.log("bu eng katta 100 natija!");
//         break
//     }else{
//         console.log("Bu natijalar: "+natijalar[i]);
//         continue;
//     }
// }
// const baho="a";
// switch (baho){
//     case "a":
//         console.log("Sizning bahoyingiz a");
//         break;
//     case "b":
//         console.log("Sizning bahoyingiz b");
//         break;
//     case "c":
//         console.log("Sizning bahoyingiz c");
//         break;
//     default:
//         console.log("Sizning bahoyingiz a");
//         break;
// };
// var age = 22
// console.log(age)
// function salom(){
//     console.log("Assalomu aleykum");
// }
// salom()
// const sallom = function(){
//     console.log("salom")
// }
// sallom()
// const salom = () =>{
//     console.log("This is arrow function!");
// }
// salom();
// salom();
// salom();

// const salom = function(ism){
//     console.log(`salom ${ism}`)
// }
// salom("Azizbek")
// const salom = function(ism, kun="dushanba"){
//     console.log(`Hayrli ${kun} ${ism}`)
// }
// salom("Aziz", "kun");
// salom("Asliddin","kech")
// const salom = function(radius){
//     return radius;
// }
// let result = salom(3)
// console.log(result);
// const salom2 = () =>{
//     console.log(result);
// }
// salom2()
// const aylana = (radius) =>{
//     return 3.14 * radius**2;
// }
// let chiq = aylana(5);
// console.log(chiq);
// const salom = (radius) => 3.14*radius**2

// const chiq = salom(3);
// console.log(chiq);
// const salom = (radius) =>{
//     return radius
// }
// const chiq = salom(5)
// console.log(chiq)
// const salom = (ism, familiya) => `Bu ${ism} ${familiya} nomli odam`
// let result = salom("Azizbek","Asliddinov");
// console.log(result)
// const salom = function(maxsulotlar,foiz){
//     let total = 0;
//     for(let i=0;i<maxsulotlar.length;i++){
//         total+=total+maxsulotlar[i]*foiz
//     }
//     return total
// }
// maxsulotlarimiz = [10,13,45]
// let result = salom(maxsulotlarimiz,0.2)
// console.log(result)

// const olmalar = {
//     "olma":100,
//     "behi":100,
//     "nok":100
// }

// const salom = (mevalar,foiz) =>{
//     let total = 0
//     let objekt = Object.values(mevalar);
//     for (let i = 0;i<objekt.length;i++){
//         total+= objekt[i]*foiz
//     }
//     return total
// }
// const result = salom(olmalar,0.2);
// console.log(result)
// const ismlar = new Array('Ahror',"Doniyor","Asliddin");
// const nom =ismlar.forEach(element => {
//     console.log(element);
// });
// ismlar.forEach(function(ism){
//     console.log(ism);
// })\
// ismlar[3]="AHROR";
// ismlar[4]='KDJFSDFJLK';
// ismlar.forEach(function(ism){
//     console.log(ism.charAt().toUpperCase()+ism.slice(1).toLowerCase()+"bek")
// })
// const user={
//     name:"Ahror",
//     age:24,
//     email:'dkjf@gamil.com',
//     location:"Farg'ona",
//     lang:["O'zbekcha","Ruscha","Inglizcha"],
//     login:function(){
//         console.log("salom")
//     },
//     logout:function(){
//         console.log("xayr");
//     },
//     speak:function(){
//         console.log(this.lang)
//     },
//     gapirish:function(){
//         console.log("I can speak:");
//         this.lang.forEach((lang)=>{
//             console.log(lang);
//         }
//     )
//     }
// }
// console.log(user);
// user.age=28;
// console.log(user.age)
// console.log(user.location);
// console.log(user["location"]);
// console.log(user.login());
// console.log(user.logout());
// console.log(user.speak());
// console.log(this)
// console.log(user.gapirish())
// const array = [
//     {nomi:"Titanik",like:32323},
//     {nomi:"Avatar",like:34234},
//     {nomi:"Jumong",like:3334}
// ]

// array.forEach(kino => {
//     let result = `${kino.nomi} kinosi ${kino.like} ta like yig'gan ekan`;
//     console.log(result);
// });
// const randomNumber = Math.trunc(Math.random()*10)+1;
// console.log(randomNumber);
// const matn = "kdjsfAdssfddfs Aa Dkls jds aaa dk jadsadAA";
// let aMatn = matn.split('');
// let counter=0;
// aMatn.forEach(yangi =>{
//     if(yangi=="a" || yangi=="A"){
//         console.log(`Bu matnda ${counter} ta a harfi qatnashgan.`);
//         counter++;
//     }
// })

// let result = []

// const MyFunction =(number)=>{
//     for (let i=1;i<=number;i++){
//         if(i%3==0 && i%15 !==0){
//             result.push("Fiz");
//         }
//         else if(i%5==0 && i%15 !==0){
//             result.push("Buz");
//         }
//         else if(i%15==0){
//             result.push("FizBuz");
//         }else{
//             result.push(i);
//         }
//     }
//     return result;
// }
// console.log(MyFunction(35));
// const ListItem = document.getElementsByTagName('li');
// console.log(ListItem.length)
// const ItemClass = document.getElementsByClassName('list-item');
// console.log(ItemClass[0]);
// const clickBtn = document.getElementById('click-btn');
// console.log(clickBtn);
// const h1 = document.querySelector('h1');
// console.log(h1);
// const allh1 = document.querySelectorAll('h1');
// console.log(allh1);
// const chiq = allh1.forEach(chiqadiganlar =>{
//     console.log(chiqadiganlar)
// })
// const Classorqali = document.querySelector(".list-item")
// console.log(Classorqali);
// const ClassOrqali = document.querySelectorAll(".list-item");
// console.log(ClassOrqali);
// const chiqadi = ClassOrqali.forEach(salom=>{
//     console.log(salom);
// })
// const idorqali = document.querySelector("#click-btn");
// console.log(idorqali);
// const h1idtitle = document.querySelector("#title");
// console.log(h1idtitle.textContent+" salomlar");
// const list = document.querySelectorAll(".list-item");
// console.log(list);
// const salom = list.forEach(item=>{
//     console.log(item.textContent+" darslari.");
// })
// const list = document.querySelector("#title")
// const list1 = document.querySelector("#title1")
// list.innerHTML="<i>Salom Dunyo</i>"
// list1.textContent="<i>Salom Dunyo</i>"
// const list = ["Ahror","Sardor","Doniyor"]
// const ol = document.querySelector("ol");
// list.forEach(item =>{
//     ol.innerHTML += `<li>${item}</li>`;
// })
// console.log(ol);
// const link = document.querySelector('a');
// console.log(link.getAttribute("href"));
// link.setAttribute("href","https://yandex.ru");
// console.log(link.getAttribute("href"));
// console.log(link.textContent);
// link.textContent = "Endi bu yandexning linki bo'ldida";
// console.log(link.textContent);
// const ptagi = document.querySelector("p");
// console.log(ptagi.getAttribute("class"));
// ptagi.setAttribute("class","ptagiclasi");
// console.log(ptagi.getAttribute("class"));
// const heading = document.querySelector('h1');
// console.log(heading);
// heading.setAttribute("style","margint:50px; color:red");
// heading.style.color = "crimson";
// heading.style.color = 'pink';
// heading.style.color = 'yellow';
// heading.style.margin = "88px";
// heading.style.textAlign = "center";
// heading.style.textAlign = "top";
// heading.style.margin = "0px";
// heading.style.marginLeft = "0px";
// heading.style.color = "greenyellow";
// heading.style.fontSize = '50px'
// heading.style.fontFamily = "Times New Roman";
// heading.style.margin = "33px";
// heading.style.margin = '';
// const kerak = document.querySelector("p");
// console.log(kerak.classList);
// kerak.classList.add("pushti");
// console.log(kerak.classList);
// kerak.classList.remove("oq");
// console.log(kerak.classList);
// const plar = document.querySelectorAll("p");
// console.log(plar);
// plar.forEach(text =>{
//     console.log(text.textContent.includes('success'));
// })
// plar.forEach(text2 =>{
//     console.log(text2.textContent.includes("error"));
// })
// const plar = document.querySelectorAll("p");
// console.log(plar)
// plar.forEach(matn =>{
//     if(matn.textContent.includes('success')){
//         matn.classList.add("success");
//         console.log(matn)
//     }
//     if(matn.textContent.includes('error')){
//         matn.classList.add("error")
//         console.log(matn)
//     }
// })
// const article = document.querySelector('article')
// console.log(article.children);
// console.log(Array.from(article.children));
// Array.from(article.children).forEach(salom => {
//     salom.classList.add("article-class");
// })
// console.log(article.children)
// const sarlavha = document.querySelector('h2');
// console.log(sarlavha);
// console.log(sarlavha.parentElement);
// console.log(sarlavha.parentElement.parentElement);
// console.log(sarlavha.parentElement.parentElement.parentElement);
// console.log(sarlavha.nextElementSibling);
// console.log(sarlavha.nextElementSibling.nextElementSibling);
// console.log(sarlavha.previousElementSibling);
// console.log(sarlavha.previousElementSibling.previousElementSibling);
// console.log((document.querySelector("h2")).nextElementSibling.nextElementSibling.previousElementSibling.parentElement.children);
// const natija = document.querySelector("button");
// natija.addEventListener('click', ()=>{
//     console.log("You are clicked me.");
// });
// const ish = document.querySelector('button');
// ish.addEventListener('mouseover', ()=>{
//     console.log("E qondoyey.");
// });
// const ish =  document.querySelectorAll('li');
// console.log(ish)
// ish.forEach(item =>{
//     item.addEventListener('click',(e)=>{
//         // console.log("salomlar item clicked");
//         // console.log(e.target);
//         console.log(item);
//         console.log("Buning ustiga chiziq chizilib qoladigan qilamiz");
//         e.target.style.textDecoration = 'line-through';
//         e.target.style.opacity = 0.5;
//     })
// })
// const ul = document.querySelector('ul');
// ul.remove();
// const ul = document.querySelector("ul");
// const button = document.querySelector("button");
// button.addEventListener("click",()=>{
//     ul.innerHTML+="<li>Assalomu aleykum</li>";
// });
// const ul = document.querySelector("ul");
// const button = document.querySelector("button");
// button.addEventListener('click',() =>{

// });
// const sarlavha = document.querySelector("h1");
// sarlavha.addEventListener("click",()=>{
//     sarlavha.textContent="Bu sarlavhaku tentak nimaga buni bosasan. \n Qara ikkita tugma pastga tushib ketdi."
// })
// const li = document.querySelectorAll("li");
// li.forEach(item => {
//     item.addEventListener("click",(e)=>{
//         e.target.remove();
//     });
// });
// const ul = document.querySelector("ul");
// const button1 = document.querySelector("button");
// const yangiLi = document.createElement("li");
// yangiLi.textContent="<li>Assalomu aleykum</li>";
// button1.addEventListener('click',(e)=>{
//     ul.appendChild(yangiLi);
// });
// const bastBnt = document.querySelector('.btn');
// bastBnt.addEventListener("click",(e)=>{
//     ul.prepend(yangiLi);
// });
// const ul = document.querySelector('ul');
// const li = document.querySelector('li');
// ul.addEventListener('click',(e)=>{
//     console.log("Assalomu aleykum");
//     e.stopPropagation();
// });
// li.addEventListener('click',(e)=>{
//     console.log("Va aleykum Assalom");
//     e.stopPropagation();
// });
// const li = document.querySelectorAll('li');
// li.forEach(item =>{
//     item.addEventListener("click",(e)=>{
//         console.log(e.target.nodeName);
//     })
// })
// const ul = document.querySelector("ul");
// ul.addEventListener("click",(e)=>{
//     if(e.target.nodeName == "LI"){
//         e.target.remove();
//     }else{
//         console.log(e.target.nodeName+" qo'ysangchi.");
//     }
// })
// document.addEventListener("keydown",(e)=>{
    // console.log("hello");
    // console.log(e)
    // console.log(e.key);
    // console.log(e.code);
    // console.log(e.keyCode);
//     if(e.key == "m" && e.ctrlKey){
//         console.log("Siz ctrl + m ni bosdingiz.");
//     }
// })
// document.addEventListener("keyup", (e)=>{
    // console.log('Assalomu aleykum');
    // console.log(e);
    // console.log(e.key);
    // console.log(e.code);
    // console.log(e.keyCode);
//     if(e.key == "m" && e.ctrlKey){
//         console.log("GOOOL!!!");
//     }
// })
// const insert = document.getElementById("insert");
// window.addEventListener('keydown',(e)=>{
//     insert.innerHTML=`
//     <div class="key">
//         ${e.key==' ' ? "Space" : e.key}
//         <small>event.key</small>
//     </div>
//     <div class="key">
//         ${e.keyCode}
//         <small>event.keyCode</small>
//     </div>
//     <div class="key">
//         ${e.code}
//         <small>event.code</small>
//     </div>

    // `


    // console.log("event.Key", e.key);
    // console.log('event.KeyCode', e.keyCode);
    // console.log("event.Code", e.code);
    // console.log(e)

// })
// ------------------kod qismi-----------------
// const body = document.querySelector("body");
// const container = document.querySelector(".container")
// const colorText = document.querySelector(".color-text")
// const values = [
//     '0',
//     '1',
//     '2',
//     '3',
//     '4',
//     '5',
//     '6',
//     '7',
//     '8',
//     '9',
//     'a',
//     'b',
//     'c',
//     'd',
//     'e',
//     'f',
// ]

// // rendom color function

// function getGradient(){
//     let color='#'
//     for(let i=0;i<6;i++){
//         const randomNumber = Math.trunc(Math.random()*values.length);
//         color+=values[randomNumber];
//     }
//     return color;
// }

// // set color to body

// function setGradient(){
//     const color1 = getGradient();
//     const color2 = getGradient();
//     const randomDeg = Math.trunc(Math.random()*360);
//     const bgColor = `linear-gradient(
//     ${randomDeg}deg,
//     ${color1},
//     ${color2}
//     )`
//     body.style.background = bgColor;
//     colorText.textContent = bgColor;
// }

// setGradient();

// container.addEventListener('click',setGradient);

// ------------------kod qismi-----------------

// const movies = [
//     {name:'Avatar 3D', year:2008, rating:9},
//     {name:'Titanik 4D', year:1997,rating:7},
//     {name:'Avengars 3D', year:2012,rating:6},
// ];
// for(nom in movies){
//     if(movies[nom].year>2010){
//         console.log(movies[nom].name + " bu kino 2010-yildan keyin ishlab chiqilgan.");
//     }else{
//         console.log(movies[nom].name + " bu kino 2010-yildan oldinroq ishlab chiqilgan.");
//     }
// }

// movies.forEach(item =>{
//     if(item.year>2010){
//         console.log(item.name + " bu kino 2010 - yildan keyin ishlab chiqilgan");
//     }else{
//         console.log(item.name + " bu kino 2010 - yildan oldinroq ishlab chiqilgan.");
//     }
// })

// const filterMovies = movies.filter(movie =>{
//     return movie.year>2010;
// })
// console.log(filterMovies);

// ------------------kod qismi-----------------
// const numbersDegree = [];
// const numbers = [2,3,4,5];
// numbers.forEach(number=>{
//     numbersDegree.push(number**2);
// })
// console.log(numbersDegree);
// const newMapNumbers = numbers.map(number=>{
//     return number**2;
// })
// const newMapNumbers = numbers.map(number => number**2);
// console.log(newMapNumbers);

// ------------------kod qismi-----------------

// const names = ['bobur','doniyor','ahror','sardor']
// const sorted = names.sort();
// console.log(sorted)
// const raqamlar = [3,2,53,23,23]
// const sortNumber = raqamlar.sort()
// console.log(sortNumber);
// const Numbersort = raqamlar.sort((a,b)=>{
//     return a-b
// })
// console.log(Numbersort)
// const reverseNumbers = raqamlar.sort((a,b)=>{
//     return b-a;
// })
// console.log(reverseNumbers);
// const movies = [
//     {name:"Aslliddin",yil:2001,yosh:23,rating:3},
//     {name:"Azizbek",yil:2001,yosh:23,rating:3},
//     {naem:"Ahror",yil:2001,yosh:23,rating:3},
// ]
// const ozgar = movies.sort((a,b)=>{
//     return a.name-b.name;
// })
// const kamay  = movies.sort((a,b)=>{
//     return b.rating - a.rating;
// })
// console.log(ozgar);
// console.log(kamay);

// ------------------kod qismi-----------------

// const yosh = prompt("Yoshingizni kiriting:",18);
// if (yosh<18){
//     alert("Siz 18 yoshdan kichkinasiz.");
// }else{
//     alert("Siz 18 yoshdan kattasiz.");
// }
// yosh<18 ? alert("Siz 18 dan kichkinasiz") : alert("Siz 18 dan kattasiz");
// armiyaga borish bormasligi haqida
// yosh<18 ? alert(`Siz armiya yoshidan ${18-yosh} kichkina bo'lsangiz kerak, anig'ini bilmaymanda`) : yosh<28 ? alert("Siz armiyaga bora olasiz") : alert(`Siz armiya yoshidan ${yosh-28} yosh kichkina bo'lsangiz kerak, anig'ini bilmaymanda`);
// yosh<18 && yosh>28 ? alert("siz armiyaga bora olmasangiz kerak") : alert("siz armiyaga bora olsangiz kerak");
// true && console.log("asla");
// false && console.log("o'tkazma");
// ------------------kod qismi-----------------
// localStorage.setItem("name","Ahror");
// const name= "Ahror"
// let age = 24;
// localStorage.setItem("name",name);
// localStorage.setItem("age",age);
// const getAge = localStorage.getItem('age');
// console.log(getAge);
// localStorage.clear();
// const ismlar = ["Olim","Abduvali","Elbek","Tohir"]
// localStorage.setItem('names',ismlar);
// localStorage.setItem('ismlar',JSON.stringify(ismlar));
// const qiymat = localStorage.getItem("ismlar");
// console.log(typeof qiymat);
// const arrayQiymat = JSON.parse(localStorage.getItem("ismlar"))
// console.log(arrayQiymat);
// const ismlar = [];
//     if(ismlar.length>0){
//         console.log(ism);
//     }else{
//         console.log("Hech qanday ism yo'q");
//     }




// ------------------kod qismi-----------------
// ------------------kod qismi-----------------
// ------------------kod qismi-----------------
// ------------------kod qismi-----------------
// ------------------kod qismi-----------------
// ------------------kod qismi-----------------
// ------------------kod qismi-----------------
// ------------------kod qismi-----------------
// ------------------kod qismi-----------------
// ------------------kod qismi-----------------