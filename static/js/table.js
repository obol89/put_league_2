let selectedRow = null

function onFormSubmit() {
      if (validate()) {
        let formData = readFormData();
        if (selectedRow == null)
            insertNewRecord(formData);
        else
            updateRecord(formData);
        resetForm();
    }
  }


function readFormData() {
    let formData = [];
    formData["teamName"] = document.getElementById("teamName").value;
    return formData;
}

function insertNewRecord(data) {
    let table = document.getElementById("allTeams").getElementsByTagName('tbody')[0];
    let newRow = table.insertRow(table.length);
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

function validate() {
    isValid = true;
    if (document.getElementById("teamName").value == "") {
        isValid = false;
        document.getElementById("teamNameError").classList.remove("hide");
    } else {
        isValid = true;
        if (!document.getElementById("teamNameError").classList.contains("hide"))
            document.getElementById("teamNameError").classList.add("hide");
    }
    return isValid;
}
let tableInfo = Array.prototype.map.call(document.querySelectorAll('#allTeams tr'), function(tr){
  return Array.prototype.map.call(tr.querySelectorAll('td'), function(td){
    return td.innerHTML;
    });
  });

$('#button3').click( function() {
  var arr = [];
  $("#allTeams tr").each(function(){
      arr.push($(this).find("td:first").text());
  });
      var myJsonString = JSON.stringify(arr);
      $.ajax({
        type: 'POST',
        data: {'teams': myJsonString},
      });
      console.log(myJsonString)
    });

/*
$('#generate').click( function() {
            $.getJSON("/update",
                function(data) {
                    $("#teams_groups").text(data.groups)
                });
            });
*/
