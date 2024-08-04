const grid_container = document.querySelector("#grid_container");


function genSquares(numSquares) {
    let sqHeight = 960 / numSquares;
    let sqWidth = 960 / numSquares;

    for (let i = 0; i < numSquares; i++) {
        for (let j = 0; j < numSquares; j++) {
            // create new square div
            let square = document.createElement("div");
            // tag new square with 'square' class for CSS + add W/H
            square.classList.add("square");
            square.style.height = `${sqHeight}px`;
            square.style.width = sqWidth;
            grid_container.appendChild(square);
        }
    }
}

genSquares(16);