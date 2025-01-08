// Js
const dayV =  document.getElementById('day');
const monthV = document.getElementById('month');
const yearV = document.getElementById('year');
const tugma = document.getElementById('tugma');
const yearChiqish = document.getElementById('yearChiziq');
const monthChiqish = document.getElementById('monthChiziq');
const dayChiqish = document.getElementById('dayChiziq');

const kun = document.querySelector("#titleDay");
const yil = document.querySelector('#titleYear');
const oy = document.querySelector('#titleMonth')
const xato1 = document.querySelector('#xato1')
const xato2 = document.querySelector('#xato2')
const xato3 = document.querySelector('#xato3')

const today = new Date();
const newYear = today.getFullYear();
const newMonth = today.getMonth() + 1;
const newDay = today.getDate();




tugma.addEventListener('click', (e) => {
    e.preventDefault();
    const day = parseInt(dayV.value, 10);
    const month = parseInt(monthV.value, 10);
    const year = parseInt(yearV.value, 10);
    if (!isNaN(day) && !isNaN(month) && !isNaN(year)) {
        if ((day < 1 || day > 31) && (month < 1 || month > 12) && (year < 1 || year > newYear)){
            kun.style.color = "red"
            xato1.textContent = "xato1"
            xato1.style.display = 'block'
            oy.style.color = "red"
            xato2.textContent = 'xato2'
            xato2.style.display = 'block'
            yil.style.color = "red"
            xato3.textContent = 'xato3'
            xato3.style.display = 'block'
        }if(day < 1 || day > 31){
            kun.style.color = "red"
            xato1.textContent = "xato1"
            xato1.style.display = 'block'
        }else{
            kun.style.color = ""
            xato1.textContent = ""
            xato1.style.display = 'none'
            dayChiqish.textContent="- -"
            yearChiqish.textContent="- -"
            monthChiqish.textContent="- -"
        }
       if (month < 1 || month > 12) {
            oy.style.color = "red"
            xato2.textContent = 'xato2'
            xato2.style.display = 'block'
        }else{
            oy.style.color = ""
            xato2.textContent = ''
            xato2.style.display = 'none'
            dayChiqish.textContent="- -"
            yearChiqish.textContent="- -"
            monthChiqish.textContent="- -"
        }if (year < 1 || year > newYear) {
            yil.style.color = "red"
            xato3.textContent = 'xato3'
            xato3.style.display = 'block'
        } else {
            yil.style.color = ""
            xato3.textContent = ''
            xato3.style.display = 'none'
            dayChiqish.textContent="- -"
            yearChiqish.textContent="- -"
            monthChiqish.textContent="- -"
        }
        if((day >= 1 && day < 31) && (month > 1 && month <= 12) && (year >= 1 && year <= newYear)){
        yearChiqish.textContent=2024-(year);
        monthChiqish.textContent=year !==newYear ? (newYear-(year))*12+(newMonth) : newMonth-month;
        dayChiqish.textContent=year !== newYear ? (newYear-(year))*365+((month-1)*31+day)+newMonth*31+newDay : (newMonth-month)*31+newDay-day;
        }
    }
    else {
        kun.style.color = "red"
        oy.style.color = "red"
        yil.style.color = "red"
        xato1.style.display = 'block';
        xato2.style.display = 'block';
        xato3.style.display = 'block';
    }
  });




















//   if(!isNaN(year) && !isNaN(month) &&!isNaN(day) && year.trim() !== '' && month.trim() !== '' && day.trim() !==''){
    // yearChiqish.textContent=2024-Number(year.value);
    // monthChiqish.textContent=(2024-Number(year.value))*12+Number(month.value);
    // dayChiqish.textContent=(2024-Number(year.value))*365+Number(day.value);
// }else if(year.trim() == '' && month.trim() == '' && day.trim() ==''){
    // kun.style.color = "red"
    // oy.style.color = "red"
    // yil.style.color = "red"
    // xato1.style.display = 'block';
    // xato2.style.display = 'block';
    // xato3.style.display = 'block';
// }