const grid_container = document.querySelector("#grid-container");

function genSquares(numSquares) {
    for (let i = 0; i < numSquares; i++) {
        let square = document.createElement("div");
        square.textContent = 'hi';
        grid_container.appendChild(square);
    }
}

genSquares(16);