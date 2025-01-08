const canvas = document.getElementById('cover'),
    ctx = canvas.getContext('2d');

//Setting width & height of canvas
canvas.height = canvas.offsetHeight;
canvas.width = canvas.offsetWidth;

let x=null,
    y=null,
    radius=14;

function getPos(e){
    const {left, top} = canvas.getBoundingClientRect();
    x=e.pageX - left;
    y=e.pageY - top;
}

function scratch(x,y){
    ctx.globalCompositeOperation = "destination-out";
    ctx.beginPath();
    ctx.fillStyle = 'gold';
    ctx.arc(x,y,radius,0,2*Math.PI);
    ctx.fill();
}

//creating leniar gradient background color
const gradient = ctx.createLinearGradient(0,0,canvas.width, canvas.height);
gradient.addColorStop(0.7,'magenta');

ctx.fillStyle=gradient;
ctx.fillRect(0,0,canvas.width,canvas.height);

//Detecting exact position of Mouse
canvas.assEventListener('mousemove', (e)=>{
    getPos(e)
    scratch(x,y);
})