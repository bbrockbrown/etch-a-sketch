const grid_container = document.querySelector("#grid_container");


function genSquares(numSquares) {
    let ratio = 100 / numSquares;

    for (let i = 0; i < numSquares; i++) {
        for (let j = 0; j < numSquares; j++) {
            // create new square div
            let square = document.createElement("div");
            // tag new square with 'square' class for CSS + add W/H
            square.classList.add("square");
            square.style.flex = `1 0 ${ratio}%`;
            square.style.height = `${ratio}%`;
            grid_container.appendChild(square);
        }
    }
}

genSquares(16);