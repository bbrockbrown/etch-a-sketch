const grid_container = document.querySelector("#grid_container");


function genSquares(numSquares) {
    let sqHeight = 960 / numSquares;
    let sqWidth = 960 / numSquares;

    for (let i = 0; i < numSquares; i++) {
        for (let j = 0; j < numSquares; j++) {
            let square = document.createElement("div");
            square.classList.add("square");
            square.textContent = 'hi';
            grid_container.appendChild(square);
        }
    }
}

genSquares(16);