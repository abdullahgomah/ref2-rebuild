let burgerMenu = document.querySelector('.burger-menu') 
let headerNav = document.querySelector("header nav") 
burgerMenu.addEventListener('click', () => { 
    headerNav.classList.toggle('show') 
})