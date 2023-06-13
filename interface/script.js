function add(){
    var list = document.getElementsByClassName("ligne")
    var test = list[0]
    var child = test.cloneNode(true)
    

    var removeBtn = document.createElement("button");
    removeBtn.textContent = "Remove";
    removeBtn.addEventListener("click", function() {
        child.remove();
    });
    child.appendChild(removeBtn);

    var labels = child.querySelectorAll("label");
    labels.forEach(function(label) {
        label.remove();
    });

    var E1 = document.getElementById("tanklist")
    E1.appendChild(child)
    
}
function add2(){
    var list = document.getElementsByClassName("ligne1")
    var test = list[0]
    var child = test.cloneNode(true)
    

    var removeBtn = document.createElement("button");
    removeBtn.textContent = "Remove";
    removeBtn.addEventListener("click", function() {
        child.remove();
    });
    child.appendChild(removeBtn);
    
    var labels = child.querySelectorAll("label");
    labels.forEach(function(label) {
        label.remove();
    });

    var E1 = document.getElementById("formula")
    E1.appendChild(child)
}


// but : réccupérer les valeurs misent dans les input :
//function getValue() { 
// Valuelist = []
// trouver un chemin pour arriver dans la class ligne 
// pouvoir récupérer chaque éléments séparément name , quatitymax, checkbox
//  value_name -> prend la valeur de name 
//  value_maxQuantity -> // de quantitymax
//  value_full -> // de full
//  append les valeurs dans Valuelist 
function getValue() { 
    Valuelist = []
    var list = document.getElementsByClassName("ligne");





    var value_name = document.getElementById("name").value;
    var value_maxQuantity = document.getElementById("quantitymax").value;
    var value_full = document.getElementById("full").value;
    Valuelist.extend(value_name, value_maxQuantity, value_full)
    console.log(Valuelist)
}


function validatePercentage(input) {
    var value = input.value;
    var numberValue = parseInt(value);
  
    if (isNaN(numberValue) || numberValue > 100) {
      input.value = "";
    }
  }