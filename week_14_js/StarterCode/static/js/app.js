var tableData = data;
var tbody = d3.select('tbody');
// YOUR CODE HERE!
//console.log(tableData[0].datetime)

// id='datetime'  BUTTON CLICK id='filter-btn'
var filterData = function() {
    var dateTimeCheck = document.getElementById('datetime').value;
    var i, allDates
    allDates = [];
    for (i=0;i<data.length;i++) {
        if (dateTimeCheck == data[i].datetime) {
            allDates.push(data[i])
         }};
    allDates.forEach((filteredDataPrint) => {
        var row = tbody.append('tr');
        Object.entries(filteredDataPrint).forEach(([key, value]) => {
            var cell = row.append('td');
            cell.text(value);
        });
    });
    if (date.length > 0) {
        alert('Data was found on the date you are searching!');
    } else {
        alert("No data was found on the specified date. Please try again.");
    }
}