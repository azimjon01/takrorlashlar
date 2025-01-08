const tab = document.querySelector('.tabs'),
    badges = tab.querySelectorAll('.tab'),
    icons = document.querySelectorAll('.icon span'),
    {clientWidth, scrollWidth}=tab;


badges.forEach(badge => {
    badge.addEventListener('click',()=>{
        tab.querySelector('.active').classList.remove('active');
        badge.classList.add('active');

        badge.scrollIntoView({
            inline:'center'
        })
    })
});

icons.forEach(icon =>{
    icon.addEventListener('click',()=>{
        tab.style = "";
        tab.scrollLeft += icon.classList.contains('right-arrow') ? 300 : -300;
    })
})

tab.addEventListener('scroll', (e)=>{
    updateIcons(e.target.scrollLeft);
});

tab.addEventListener('wheel', (e)=>{
    tab.style.scrollBehavior = "auto";
    tab.scrollLeft += e.deltaY;
});

function updateIcons(scrolled_width){
    icons[0].parentElement.classList.toggle('hide', scrolled_width <=1)
    icons[1].parentElement.classList.toggle('hide',scrollWidth - (clientWidth+scrolled_width) <=1)
}