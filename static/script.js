// --------------------------------------------Cardiology button-------------------------------------------------------------------------
let bnt1 = document.getElementById('butid81');

bnt1.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/Cardiology")
});
// --------------------------------------------Orthopedics button-------------------------------------------------------------------------
let bnt4 = document.getElementById('butid83');

bnt4.addEventListener('click', (e1) => {
    e1.target.style.backgroundColor = "yellow";
    e1.target.style.color = "black";
    window.open("/department/Orthopedics")
});

// ---------------------------------------------Neurology button-------------------------------------------------------------------------
let bntor81 = document.querySelector('#butid82');

bntor81.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/Neurology");
});

// ---------------------------------------------Pediatrics button-------------------------------------------------------------------------
let butid84 = document.querySelector('#butid84');

butid84.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/Pediatrics");
});

// ---------------------------------------------Oncology button-------------------------------------------------------------------------
let butid85 = document.querySelector('#butid85');

butid85.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/Oncology");
});

// ---------------------------------------------Gynecology & Obstetrics button-------------------------------------------------------------------------
let butid86 = document.querySelector('#butid86');

butid86.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/Gynecology & Obstetrics ");
});

// ---------------------------------------------Dermatology button-------------------------------------------------------------------------
let butid87 = document.querySelector('#butid87');

butid87.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/Dermatology");
});

// ---------------------------------------------ENT (Ear, Nose, Throat) button-------------------------------------------------------------------------
let butid88 = document.querySelector('#butid88');

butid88.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/ENT (Ear, Nose, Throat)");
});

// ---------------------------------------------General Medicine button-------------------------------------------------------------------------
let butid89 = document.querySelector('#butid89');

butid89.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/General Medicine");
});

// ---------------------------------------------Emergency & Trauma button-------------------------------------------------------------------------
let butid810 = document.querySelector('#butid810');

butid810.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/Emergency & Trauma");
});

// ---------------------------------------------Urology button-------------------------------------------------------------------------
let butid811 = document.querySelector('#butid811');

butid811.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/Urology");
});

// ---------------------------------------------Pulmonology button-------------------------------------------------------------------------
let butid813 = document.querySelector('#butid813');

butid813.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/Pulmonology");
});

let butid812 = document.querySelector('#butid812');

butid812.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    window.open("/department/Gastroenterology");
});

let but_color = document.querySelector('#but_color')

but_color.addEventListener('click',(a) => {
    let body1=document.querySelector('#body1');
    if (body1.style.color==="white" && body1.style.backgroundColor==="black"){
        a.target.innerText="dark-mode";
        body1.style.backgroundColor="white"
        body1.style.color="black"
        document.querySelector("#h4_main").style="color:black;"
        document.querySelector("#h1_main").style="color:#4b0082;text-align: center;";
        
    }
    else{
        a.target.innerText="light-mode";
        body1.style.backgroundColor="black"
        body1.style.color="white"
        document.querySelector("#h4_main").style="color:white;"
        document.querySelector("#h1_main").style="color:#C5B4E3;text-align: center;";
    }
});

// let but_main=document.querySelector("#main_but")
// but_main.window.print()
// console.log("hd");
let but_search = document.querySelector("#search_butt")
      but_search.addEventListener('click',() => {
        let value=document.querySelector("#search_Input").value
        if(value==""){
            mess="kindly enter the department name"
            let post = document.createElement("p")
            post.innerText=mess
            post.style.marginLeft="-20px";
            document.querySelector("#serach_div").appendChild(post)
        }
        localStorage.setItem("dept_name", value)
      });