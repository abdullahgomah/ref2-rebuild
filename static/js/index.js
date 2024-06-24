let btnAddWebsite = document.querySelector('#btn-add-website');
let websiteNameInput = document.querySelector('[name=website-name-input]')
let websiteDescriptionInput = document.querySelector('[name=website-description-input]')
let websiteToolInput = document.querySelector("[name=website-tool-input]")

function check_empty(input) {
    if (input.value == "" ) {
        input.classList.add('error') 
        return true; 
    } else {
        input.classList.remove('error') 
        return false; 
    }
}

// Validate Add new website form 
btnAddWebsite.addEventListener('click', () => {
    let isWebsiteNameInputEmpty = check_empty(websiteNameInput),
        isWebsiteDescriptionInputEmpty = check_empty(websiteDescriptionInput), 
        isWebsiteToolInputEmpty = check_empty(websiteToolInput); 


    if (isWebsiteNameInputEmpty == false & isWebsiteToolInputEmpty == false & isWebsiteDescriptionInputEmpty == false) {
        // start ajaax request 
        $.ajax({
            url: '/websites/create/',  // Adjust URL if your project has a different structure
            type: 'POST',
            data: {
                'websiteName': websiteNameInput.value,
                'websiteDescription': websiteDescriptionInput.value, 
                'websiteTool': websiteToolInput.value ,
                'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value 
            },
            success: function(response) {
                $('#section__all_websites').html(response);
            },
            error: function(xhr, status, error) {
            }
        });

    }
})

window.onload = () => {
    $.ajax({
        url: "/websites/ajax-all-websites/", 
        type: "GET", 
        data: {
            // here I will pass user id 
        },
        success: function (response) { 
            $('#section__all_websites').html(response);
        }, error: function (xhr, status, error) { 
            console.log(error)
        }
    })
} 