function check_empty(input) {
    if (input.value == "" ) {
        input.classList.add('error') 
        return true; 
    } else {
        input.classList.remove('error') 
        return false; 
    }
}



let fieldsTypes = document.querySelector('.fields__types' ) 
let fieldsTypesInputs = document.querySelector('.fields__types' ).querySelectorAll('input') 
fieldsTypesInputs.forEach((input) => {
    input.parentElement.querySelector('label').addEventListener('click', () => {
        fieldsTypesInputs.forEach((radio_input) => {
            radio_input.checked = false; 
        })

        // complete the code here 
        input.checked = true;
    }) 

})

document.querySelector("#add-field-form").addEventListener('submit', (e) => {
    e.preventDefault(); 
})

let btnAddNewField = document.querySelector(".btn-add-new-field"); 
btnAddNewField.addEventListener('click', () => {

    // now, I'm sending it of field type to get it in the views 
    // and then, I'm getting table id 
    /*
    the views logic: after getting id of table, field_type 
    get table obj 
    get field_type_obj 
    get name  
    get description 
    
    start create field type 

    finally, ajax update fields 
     */


    // field name 
    let fieldNameInput = document.querySelector('#field__name'), 
        isFieldNameInput_empty = check_empty(fieldNameInput); 


    // field description 
    let fieldDescriptionInput = document.querySelector('#field__description'), 
        isFieldDescriptionInput_empty = check_empty(fieldDescriptionInput); 



    // table id 
    let tableIdInput = document.querySelector('[name=table_id]')


    // field type id 
    let fieldTypeId = ''


    // First, get the checked radio input 
    let radioHasChecked = false; 
    fieldsTypesInputs.forEach((input) => {
        if (input.checked) {
            radioHasChecked = true; 
            fieldTypeId = input.dataset.field_type_id 
        } 
    }) 

    if (radioHasChecked == false)  {
        // not ready to send 
    } else { 
        if (isFieldNameInput_empty == false & isFieldDescriptionInput_empty == false )  {
            // start ajax request 
            $.ajax({
                url: '/websites/table-details/add-field/', 
                type: 'POST', 
                data: {
                    'table-id': tableIdInput.value, 
                    'field-type-id': fieldTypeId, 
                    'field-name': fieldNameInput.value, 
                    'field-description': fieldDescriptionInput.value,
                    "csrfmiddlewaretoken": document.querySelector('[name=csrfmiddlewaretoken]').value
                }, success: function (response)  {
                    console.log('success');
                    $("#all-fields").html(response) ;
                }, error: function (xhr, status, error) {  

                }
            })
        }
    }


})