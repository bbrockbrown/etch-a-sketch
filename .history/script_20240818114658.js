const grid_container = document.querySelector("#grid_container");
const grid_slider = document.querySelector("#grid_slider");
const grid_size_display = document.querySelector("#grid_size");
grid_size_display.innerHTML = `${grid_slider.value} x ${grid_slider.value}`;
const color_input = document.querySelector("#clr_input");
const color_input_txt = document.querySelector("#color_input_txt")
const rand_color = document.querySelector("#rand_clr");
const clear_grid_btn = document.querySelector("#clear_grid");

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
                changeColor(square, is_rand);
            });

            // if user is over a square and is clicking down --> change color
            // aka gives 'sketch' effect
            square.addEventListener("mouseover", () => {
                if (mouseDown) {
                    changeColor(square, is_rand);
                }
            });
        }
    }

    
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

function clearGrid() {
    squares = document.querySelectorAll(".square");
    squares.forEach((square) => square.style.backgroundColor = "white");
    
}


grid_slider.oninput = function() {
    grid_size_display.innerHTML = `${grid_slider.value} x ${grid_slider.value}`;
    genSquares(grid_slider.value);
}

rand_color.addEventListener("click", () => {
    if (is_rand) {
        is_rand = false;
        color_input.style.display = "block";
        color_input_txt.innerHTML = "Color:";
        grid_slider.classList.remove('rainbow');
    } else {
        is_rand = true;
        color_input.style.display = "none";
        color_input_txt.innerHTML = "Color: Random!!!";

        let styleElement = document.getElementById('rainbow-thumb');
        if (!styleElement) {
            styleElement = document.createElement('style');
            styleElement.id = 'rainbow-thumb';
            document.head.appendChild(styleElement);
        }
        styleElement.innerHTML = `
        `
    }
});

color_input.addEventListener("input", () => {
    let styleElement = document.getElementById('slider-thumb-style');
        if (!styleElement) {
            styleElement = document.createElement('style');
            styleElement.id = 'slider-thumb-style';
            document.head.appendChild(styleElement);
        }
    styleElement.innerHTML = `
    #grid_slider {
        -webkit-appearance: none;
        width: 200px;
        height: 20px;
        border-radius: 10px;
        border: black 2px solid;  
        background: white;
        outline: none;
        opacity: 0.8;
        -webkit-transition: .2s;
        transition: opacity .2s;
    }

    #grid_slider:hover {
        opacity: 1; /* Fully shown on mouse-over */
    }

    #grid_slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 25px;
        height: 25px;
        border-radius: 50%; 
        background: ${color_input.value};
        cursor: pointer;
    }`;
})

clear_grid_btn.addEventListener("click", () => (clearGrid()));

genSquares(16);