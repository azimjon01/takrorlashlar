const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");
const btn1 = document.getElementById("btn1");
const btn2 = document.getElementById("btn2");
const informationContainer = document.querySelector(".container__information");
const dateId = document.getElementById("dateId");
const monthId = document.getElementById("monthId");

btn1.addEventListener('click',()=>{
    if(inputBox.value === ""){
        alert("Siz ma'lumot kiritmadingiz!");
    }else{
        informationContainer.style.zIndex = 100;
    }
})

btn2.addEventListener('click',()=>{
    if((dateId.value === "") || (monthId.value === "")){
        alert("Izoh va vaqtni belgilang!");
    }else{
        let li = document.createElement("li");
        li.innerHTML = inputBox.value + " " + dateId.value + " " +monthId.value;
        listContainer.appendChild(li);
        let span = document.createElement("span");
        span.innerHTML = "\u00d7";
        li.appendChild(span);
    }
    inputBox.value = "";
    dateId.value = "";
    monthId.value = "";
    informationContainer.style.zIndex = 1;
    saveData();
})

listContainer.addEventListener('click',function(e){
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked");
        saveData();
    }else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData()
    }
},false);

function saveData(){
    localStorage.setItem("data",listContainer.innerHTML);
}

function showTask(){
    listContainer.innerHTML = localStorage.getItem("data");
}

showTask()





// function addTask(){
//     if(inputBox.value === ''){
//         alert("You most write something!");
//     }else{
//         let li = document.createElement("li");
//         li.innerHTML = inputBox.value;
//         listContainer.appendChild(li);
//         let span = document.createElement("span")
//         span.innerHTML = "\u00d7";
//         li.appendChild(span);
//     }
//     inputBox.value = "";
//     saveData();
// }

// listContainer.addEventListener('click',function(e){
//     if(e.target.tagName === "LI"){
//         e.target.classList.toggle("checked");
//         saveData();
//     }else if(e.target.tagName === "SPAN"){
//         e.target.parentElement.remove();
//         saveData();
//     }
// },false);

// function saveData(){
//     localStorage.setItem("data", listContainer.innerHTML);
// }

// function showTask(){
//     listContainer.innerHTML = localStorage.getItem("data");
// }

// showTask();