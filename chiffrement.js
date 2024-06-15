function chiffrerTexte() {
    var texteOriginal = document.getElementById("texteOriginal").value.toLowerCase(); // Convertir tout le texte en minuscules
    var alphabet = "abcdefghijklmnopqrstuvwxyz .";  // Exemple d'alphabet en minuscules
    var alphabetArray = alphabet.split('');  // Convertir l'alphabet en tableau pour manipuler les lettres
    var substitution = {};  // Dictionnaire pour les substitutions
    var texteChiffre = "";

    for (var i = 0; i < texteOriginal.length; i++) {
        var char = texteOriginal.charAt(i);

        if (substitution[char] === undefined) {
            var randIndex = Math.floor(Math.random() * alphabetArray.length);
            var randChar = alphabetArray[randIndex];

            // Assurer que le caractère aléatoire est différent du caractère original
            while (randChar === char) {
                randIndex = Math.floor(Math.random() * alphabetArray.length);
                randChar = alphabetArray[randIndex];
            }

            // Ajouter la substitution au dictionnaire
            substitution[char] = randChar;
            
            // Retirer le caractère aléatoire utilisé de alphabetArray
            alphabetArray.splice(randIndex, 1);
        }

        texteChiffre += substitution[char];
    }

    var resultatChiffre = document.getElementById("resultatChiffre");
    resultatChiffre.textContent = "Texte chiffré : " + texteChiffre;
}
