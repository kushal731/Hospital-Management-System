let bntor81 = document.querySelector('#butidor81');
bntor81.addEventListener('click', (e) => {
    e.target.style.backgroundColor = "yellow";
    e.target.style.color = "black";
    // window.location.href = "/department/cardiology";
    window.print();
});