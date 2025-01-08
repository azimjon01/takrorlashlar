const getRandomNumber=(min,max)=>{
    return Math.floor(Math.random()*(max-min+1))+min;
}



const generate=()=>{
    const minEl=document.getElementById('min');
    const maxEl=document.getElementById('max');
    const min=Number(minEl.value);
    const max=Number(maxEl.value);
    console.log(min,max);

    if(minEl.value===''){
        alert("Iltimos minimum qiymatni kiriting!");
        return;
    }else if(maxEl.value===''){
        alert("Iltimos maximum qiymatni kiriting!");
        return;
    }

    if(min>max){
        alert("Minimum qiymat Maximum qiymatdan kichik bo'lishi kerak!");
    }

    const placeholderEl=document.querySelector("#placeholder");
    placeholderEl.textContent=getRandomNumber(min,max);
}

const btnEl=document.getElementById('generate');
btnEl.addEventListener('click',generate);

// function handleSubmit(e){
//     e.preventDefault();
//     generate()
// }

// document.querySelector("form").addEventListener("submit", function(e) {
//     e.preventDefault(); // Prevents the form from submitting
//     generate()
//     console.log("Form submission prevented.");
//     // Your form handling logic here
//   });