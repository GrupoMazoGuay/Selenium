
(function ($) {

    $( "#execute" ).click(function() {
        var auxP=document.getElementById("p1")
        var auxP2=document.getElementById("p2")

        if($('[name="text"]').val() != "") {
            texto = $('[name="text"]').val()

            numOfWords = texto.split(' ').length;
            listOfWords = texto.split(' ');

            dictOfWords = {}

            listOfWords.forEach(function(element){
                if (dictOfWords[element] == undefined) {
                    dictOfWords[element] = 1;
                } else {
                    dictOfWords[element] += 1;
                }
            });


            var arrayOrdered = Object.keys(dictOfWords).map(function(key) {
                return [key, dictOfWords[key]];
            });

            arrayOrdered.sort(function(first, second) {
                return second[1] - first[1];
            });
            
            console.log(arrayOrdered.length);
            
            arrayOrderedString = "";

            for(i = 0; i < arrayOrdered.length; i++) {
                if(arrayOrderedString.length > 0) arrayOrderedString += ", ";
                arrayOrderedString += "{"+arrayOrdered[i][0]+":"+arrayOrdered[i][1]+"}";
            }

            console.log(arrayOrderedString)

            
            auxP.innerHTML=arrayOrderedString
            auxP2.innerHTML=arrayOrdered.length


        }
    });
    

    $( "#reset" ).click(function() {
        $('[name="text"]').val('');

        var auxP=document.getElementById("p1")
        var auxP2=document.getElementById("p2")
        auxP.innerHTML=""
        auxP2.innerHTML=""
    });

    
})(jQuery);


