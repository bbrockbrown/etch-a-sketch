const grid_container = document.querySelector("#grid_container");
const grid_slider = document.querySelector("#grid_slider");
const grid_size_display = document.querySelector("#grid_size");
grid_size_display.innerHTML = `${grid_slider.value} x ${grid_slider.value}`;
const color_input = document.querySelector("#clr_input");
const rand_color = document.querySelector("#rand_clr");

let is_rand = false;
let mouseDown = false;

// Event listeners to track mouse button state
document.body.addEventListener('mousedown', () => (mouseDown = true));
document.body.addEventListener('mouseup', () => (mouseDown = false));


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

            // if user clicks on square --> change color
            square.addEventListener("mousedown", () => {
                changeColor(square, false);
            });

            // if user is over a square and is clicking down --> change color
            // aka gives 'sketch' effect
            square.addEventListener("mouseover", () => {
                if (mouseDown) {
                    changeColor(square, false);
                }
            });
        }
    }

    
}

grid_slider.oninput = function() {
    grid_size_display.innerHTML = `${grid_slider.value} x ${grid_slider.value}`;
    genSquares(grid_slider.value);
}

function changeColor(square, is_random) {
    if (is_random) {
        const color = randomColor();
        square.style.backgroundColor = color;
    }
    else {
        const color = color_input.value;
        square.style.backgroundColor = color;
    }
}

function randomColor () {
    const randomColor = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;
    return randomColor
}

rand_color.addEventListener("click", () => {
    is_rand = true;
});

genSquares(16);