let burgerMenu = document.querySelector('.burger-menu') 
let headerNav = document.querySelector("header nav") 
burgerMenu.addEventListener('click', () => { 
    headerNav.classList.toggle('show') 
})


function check_empty(input) {
    if (input.value == "" ) {
        input.classList.add('error') 
        return true; 
    } else {
        input.classList.remove('error') 
        return false; 
    }
}