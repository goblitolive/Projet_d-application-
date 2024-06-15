function chiffrerTexte() {
    var texteOriginal = document.getElementById("texteOriginal").value;
    var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .";  // Exemple d'alphabet
    var substitution = {};  // Dictionnaire pour les substitutions
    var texteChiffre = "";

    for (var i = 0; i < texteOriginal.length; i++) {
        var char = texteOriginal.charAt(i);

        if (substitution[char] === undefined) {
            var randIndex = Math.floor(Math.random() * alphabet.length);
            var randChar = alphabet.charAt(randIndex);

            while (randChar === char || Object.values(substitution).includes(randChar)) {
                randIndex = Math.floor(Math.random() * alphabet.length);
                randChar = alphabet.charAt(randIndex);
            }

            substitution[char] = randChar;
        }

        texteChiffre += substitution[char];
    }

    var resultatChiffre = document.getElementById("resultatChiffre");
    resultatChiffre.textContent = "Texte chiffré : " + texteChiffre;
}
