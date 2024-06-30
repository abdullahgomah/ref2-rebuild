function check_empty(input) {
    if (input.value == "" ) {
        input.classList.add('error') 
        return true; 
    } else {
        input.classList.remove('error') 
        return false; 
    }
}

let dbNameInput = document.querySelector('[name=db-name-input]'), 
    dbTypeInput = document.querySelector('[name=db-type-input]'),
    btnAddDb = document.querySelector('.btn-add-db');

btnAddDb.addEventListener('click', () => {
    let is_dbNameInput_empty = check_empty(dbNameInput)
    let is_dbTypeInput_empty = check_empty(dbTypeInput) 
    
    if (is_dbNameInput_empty == false & is_dbTypeInput_empty == false) {
        $.ajax({
            url: "/websites/add-database/", 
            type: "POST", 
            data: {
                "website_id": websiteIdInput.value, 
                "dbName": dbNameInput.value, 
                "dbType":dbTypeInput.value,
                "csrfmiddlewaretoken": document.querySelector('[name=csrfmiddlewaretoken]').value
            }, 
            success: function (response) {
                $(".website-databases").html(response)
                dbNameInput.value = ""; 
            }, 
            error: function (xhr, status, error) { 

            }
        })
    }
})