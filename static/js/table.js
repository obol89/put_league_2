var selectedRow = null

function onFormSubmit() {
        var formData = readFormData();
        if (selectedRow == null)
            insertNewRecord(formData);
        else
            updateRecord(formData);
        resetForm();
    }


function readFormData() {
    var formData = {};
    formData["teamName"] = document.getElementById("teamName").value;
    return formData;
}

function insertNewRecord(data) {
    var table = document.getElementById("allTeams").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.teamName;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = `<a onClick="onEdit(this)">Edit</a>
                       <a onClick="onDelete(this)">Delete</a>`;
}

function resetForm() {
    document.getElementById("teamName").value = "";
    selectedRow = null;
}

function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("teamName").value = selectedRow.cells[0].innerHTML;
}
function updateRecord(formData) {
    selectedRow.cells[0].innerHTML = formData.teamName;
}

function onDelete(td) {
    if (confirm('Are you sure to delete this record ?')) {
        row = td.parentElement.parentElement;
        document.getElementById("allTeams").deleteRow(row.rowIndex);
        resetForm();
    }
}
/*
function validate() {
    isValid = true;
    if (document.getElementById("teamName").value == "") {
        isValid = false;
        document.getElementById("fullNameValidationError").classList.remove("hide");
    } else {
        isValid = true;
        if (!document.getElementById("fullNameValidationError").classList.contains("hide"))
            document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;
}
*/
$.post( "/postmethod", {
  canvas_data: JSON.stringify(formData)
}, function(err, req, resp){
  window.location.href = "/results/"+resp["responseJSON"]["uuid"];
});
}
