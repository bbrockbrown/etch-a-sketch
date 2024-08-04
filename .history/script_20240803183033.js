const grid_container = document.querySelector("#grid_container");


function genSquares(numSquares) {
    for (let i = 0; i < numSquares; i++) {
        for (let j = 0; j < numSquares; j++) {
            let square = document.createElement("div");
            square.textContent = 'hi';
            grid_container.appendChild(square);
        }
    }
}

genSquares(16);