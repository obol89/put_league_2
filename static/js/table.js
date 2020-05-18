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
    let teamCount = document.getElementById("allTeams").rows.length;
    let newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = teamCount;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.teamName;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = `<a onClick="onEdit(this)">Edit</a>
                       <a onClick="onDelete(this)">Delete</a>`;
}

function resetForm() {
    document.getElementById("teamName").value = "";
    selectedRow = null;
}

function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("teamName").value = selectedRow.cells[1].innerHTML;
}
function updateRecord(formData) {
    selectedRow.cells[1].innerHTML = formData.teamName;
}

function onDelete(td) {
    if (confirm('Are you sure to delete this record ?')) {
        row = td.parentElement.parentElement;
        let table = document.getElementById("allTeams").getElementsByTagName('tbody')[0];
        document.getElementById("allTeams").deleteRow(row.rowIndex);
        for (let i = 0, row; row = table.rows[i]; i++) {
            table.rows[i].cells[0].innerHTML = i+1;
           }
        resetForm();
    }
}

function validate() {
    isValid = true;
    if (document.getElementById("teamName").value == "") {
        isValid = false;
    }
    return isValid;
}


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
