let flippedCards = [];
let score = 0;

function startMemoryGame() {
    console.log("Le bouton a été cliqué!");

    const grid_size = 6;
    const container = document.getElementById('memory-game-container');
    const cards = createShuffledDeck(grid_size);

    // Remettre à zéro le tableau des cartes retournées et le score
    flippedCards = [];
    score = 0;

    // Supprimer les cartes existantes du conteneur
    container.innerHTML = '';


        // Créer et afficher la grille du jeu
    for (let i = 0; i < grid_size; i++) {
        for (let j = 0; j < grid_size; j++) {
            const card = document.createElement('div');
            card.classList.add('card');

            // Utiliser le chemin d'accès correct vers l'image
            const cardValue = cards[i * grid_size + j];
            const back = document.createElement('div');
            back.classList.add('back');
            back.style.backgroundImage = `url('/static/images/card${cardValue}.jpg')`;

            // Stocker la valeur de la carte en tant que data-value
            card.dataset.value = cardValue;

            // Ajouter une classe 'front' pour la face avant de la carte
            const front = document.createElement('div');
            front.classList.add('front');

            // Ajouter un gestionnaire d'événements pour la carte
            card.addEventListener('click', () => onCardClick(card));

            // Ajouter les éléments de carte à la carte
            card.appendChild(front);
            card.appendChild(back);

            // Ajouter la carte au conteneur
            container.appendChild(card);
        }
    }

}


// Fonction appelée lorsqu'une carte est cliquée
function onCardClick(card) {
    // Ne rien faire si la carte est déjà retournée ou si deux cartes sont déjà retournées
    if (card.classList.contains('flipped') || flippedCards.length === 2) {
        return;
    }

    // Retourner la carte
    flipCard(card);

    // Ajouter la carte retournée au tableau
    flippedCards.push(card);

    // Si deux cartes sont retournées, vérifier si elles forment une paire
    if (flippedCards.length === 2) {
        setTimeout(checkForMatch, 1000);
    }
}

    // Fonction pour retourner une carte
function flipCard(card) {
    card.classList.add('flipped');

    const front = card.querySelector('.front');
    const back = card.querySelector('.back');
    front.classList.add('flipped');
    back.classList.add('flipped');
}




// Fonction pour créer et mélanger le deck de cartes
function createShuffledDeck(size) {
    const deck = Array.from({ length: (size ** 2) / 2 }, (_, index) => index + 1).flat();
    const shuffledDeck = [...deck, ...deck].sort(() => Math.random() - 0.5);
    return shuffledDeck;
}

// Fonction pour vérifier si les deux cartes retournées forment une paire
function checkForMatch() {
    const [card1, card2] = flippedCards;
    const value1 = card1.dataset.value;
    const value2 = card2.dataset.value;

    if (value1 === value2) {
        // Les cartes forment une paire, augmenter le score
        score += 10;
        updateScore();
        // Retirer les cartes du tableau des cartes retournées
        flippedCards = [];
    } else {
        // Les cartes ne forment pas une paire, les retourner
        unflipCards(card1, card2);
    }
}

// Fonction pour retourner deux cartes
function unflipCards(card1, card2) {
    setTimeout(() => {
        card1.classList.remove('flipped');
        card2.classList.remove('flipped');
        // Réinitialiser le tableau des cartes retournées
        flippedCards = [];
    }, 1000);
}

// Fonction pour mettre à jour le score
function updateScore() {
    document.getElementById('score').textContent = `Score: ${score}`;
}
