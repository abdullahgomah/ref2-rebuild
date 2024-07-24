let tableNameInput =document.querySelector('[name=table-name-input]'), 
    btnAddTable = document.querySelector('.btn-add-table'); 

let db_id = document.querySelector('[name=db_id_input]').value; 
let btnsDelTable = document.querySelectorAll('.btn-del-table'); 



function check_empty(input) {
    if (input.value == "" ) {
        input.classList.add('error') 
        return true; 
    } else {
        input.classList.remove('error') 
        return false; 
    }
}



btnAddTable.addEventListener("click", () => {
    let is_tableNameInput_empty = check_empty(tableNameInput); 
    

    if (is_tableNameInput_empty == false) { 
        $.ajax({
            url: "/websites/add-table/", 
            type: "POST", 
            data: {
                "db_id": db_id, 
                "table_name": tableNameInput.value, 
                "csrfmiddlewaretoken": document.querySelector('[name=csrfmiddlewaretoken]').value, 
            }, success: function(response) { 
                $(".db-tables").html(response)
                tableNameInput.value = ""; 
            }, error: function (xhr, status, error) { 
    
            }
        })
    }
})


btnsDelTable.forEach((btn) => { 
    btn.addEventListener('click', () => {
        let tableId = btn.parentElement.parentElement.querySelector('[name=table_id_input]'); 
        console.log(tableId); 
        $.ajax({
            url: "/websites/del-table/"+tableId.value+'/',
            method: "POST", 
            data: {
                "csrfmiddlewaretoken": document.querySelector('[name=csrfmiddlewaretoken]').value, 
            }, 
            success: (response) => {
                $('.db-tables').html(response) 
            },
            error: function (xhr, status, error) { 
            }
        })
    })
})