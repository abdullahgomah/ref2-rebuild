let pageNameInput = document.querySelector('[name=page-name-input]'); 
let btnAddPage = document.querySelector('.btn-add-page'); 
let websiteIdInput = document.querySelector('[name=website-id]'); 

function check_empty(input) {
    if (input.value == "" ) {
        input.classList.add('error') 
        return true; 
    } else {
        input.classList.remove('error') 
        return false; 
    }
}

btnAddPage.addEventListener('click', ()=> {
    pageNameInputIsEmpty = check_empty(pageNameInput) 
    if (pageNameInputIsEmpty == false) { 
        $.ajax({
            url: "/websites/add-page/", 
            type: "POST", 
            data: {
                "website_id": websiteIdInput.value, 
                "pageName": pageNameInput.value, 
                "csrfmiddlewaretoken": document.querySelector('[name=csrfmiddlewaretoken]').value
            }, 
            success: function (response) {
                $(".all-pages-grid").html(response)
            }, 
            error: function (xhr, status, error) { 

            }
        })
    }
})