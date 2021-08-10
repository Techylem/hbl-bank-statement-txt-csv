class TableCSVExporter {
    constructor(table, includeHeaders = true) {
        this.table = table;
        this.rows = Array.from(table.querySelectorAll("tr"));

        if (!includeHeaders && this.rows[0].querySelectorAll("th").length) {
            this.rows.shift();
        }
    }

    convertToCSV() {
        const lines = [];
        const numCols = this._findLongestRowLength();

        for (const row of this.rows) {
            let line = "";

            for (let i = 0; i < numCols; i++) {
                if (row.children[i] !== undefined) {
                   
                    line += TableCSVExporter.parseCell(row.children[i]);
                    
                }
                line += (i !== (numCols - 1)) ? "," : "";
                
            }

            lines.push(line);
        }

        return lines.join("\n");
    }

    _findLongestRowLength() {
        return this.rows.reduce((l, row) => row.childElementCount > l ? row.childElementCount : l, 0);
    }

    static parseCell(tableCell) {
        let parsedValue = tableCell.textContent;

        // Replace all double quotes with two double quotes
        parsedValue = parsedValue.replace(/,/g, ``);
        parsedValue = parsedValue.replace(/\t/g, ``);
        parsedValue = parsedValue.replace(/\n/g, ``);
        parsedValue = parsedValue.replace(/-/g, ``);

        

        // If value contains comma, new-line or double-quote, enclose in double quotes
       // parsedValue = /[",\n]/.test(parsedValue) ? `"${parsedValue}"` : parsedValue;

        return parsedValue;
    }
}

// function checking(){
//     var table = document.createElement("table");
//     var rows = e.target.result.split("\n");
//     console.log(rows);

//     return true;
// }

function Upload() {
    var fileUpload = document.getElementById("fileUpload");
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.txt)$/;
    if (regex.test(fileUpload.value.toLowerCase())) {
        if (typeof (FileReader) != "undefined") {
            var reader = new FileReader();
            reader.onload = function (e) {
                var table = document.createElement("table");
                var rows = e.target.result.split("\n");
                for (var i = 0; i < rows.length; i++) {
                    var row = table.insertRow(-1);
                     if(rows[i].match(/Continue on next page/gi)) 
                     {
                      i=i+12;
                     }
                     if( rows[i].match(/End of statement/gi) || rows[i].match(/----/gi))
                     {
                        continue;
                     }
                    var cells = rows[i].split("|");
                    for (var j = 0; j < cells.length; j++) {
                        var cell = row.insertCell(-1);  
                        cell.innerHTML = cells[j];
                    }
                }
                var dvCSV = document.getElementById("dvCSV");
                dvCSV.innerHTML = "";
                dvCSV.appendChild(table);
            }
            reader.readAsText(fileUpload.files[0]);
        } else {
            alert("This browser does not support HTML5.");
        }
    } else {
        alert("Please upload a valid txt file.");
    }
}

function fortable(){
    var fileUpload = document.getElementById("fileUpload");
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.txt)$/;
    if (regex.test(fileUpload.value.toLowerCase())) {
        if (typeof (FileReader) != "undefined") {
            var reader = new FileReader();
            reader.onload = function (e) {
                var table = document.createElement("table");
                var rows = e.target.result.split("\n");
                for (var i = 9; i < rows.length; i++) {
                    var row = table.insertRow(-1);
                     if(rows[i].match(/Continue on next page/gi)) 
                     {
                      i=i+12;
                     }
                     if( rows[i].match(/End of statement/gi) || rows[i].match(/----/gi))
                     {
                        continue;
                     }
                    var cells = rows[i].split("|");
                    for (var j = 0; j < cells.length; j++) {
                        var cell = row.insertCell(-1);  
                        cell.innerHTML = cells[j];
                    }
                }
                var dvCSV = document.getElementById("DVCSV");
                dvCSV.innerHTML = "";
                dvCSV.appendChild(table);
            }
            reader.readAsText(fileUpload.files[0]);
        } 
    }
}

function myfunction(){
    fortable();
    Upload();
    
}