const grid_container = document.querySelector("#grid_container");
const grid_slider = document.querySelector("#grid_slider");
const grid_size_display = document.querySelector("#grid_size");
grid_size_display.innerHTML = `${grid_slider.value} x ${grid_slider.value}`;
const color_input = document.querySelector("#clr_input");

function genSquares(numSquares) {
    // reset grid to be empty
    grid_container.innerHTML = "";

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

            square.addEventListener("mouseover", () => {
                changeColor(square);
            })
        }
    }

    
}

grid_slider.oninput = function() {
    grid_size_display.innerHTML = `${grid_slider.value} x ${grid_slider.value}`;
    genSquares(grid_slider.value);
}


function changeColor(input) {
    const color = color_input.value;
    square.style.backgroundColor = color;
}

genSquares(16);