document.querySelector(".helpbtn").addEventListener('click', function () {
    window.location.href = "/help";
})

document.querySelector(".aboutbtn").addEventListener('click', function () {
    window.location.href = "/about";
})

document.querySelector(".homebtn").addEventListener('click', function () {
    window.location.href = "/ayush";
})

const prevButton = document.getElementById("gunb");
const nextButton = document.getElementById("gunf");
const image = document.querySelector(".content img");

let currentImageIndex = 0;
const images = ["/static/images/slides1.png", "/static/images/slides2.png", "/static/images/slides3.png", "/static/images/slides4.png"];

prevButton.addEventListener("click", () => {
    var audio = new Audio("/static/audio/boom.mp3");
    audio.volume=0.3
    audio.play();
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    updateImage();
});

nextButton.addEventListener("click", () => {
    var audio = new Audio("/static/audio/boom.mp3");
    audio.volume=0.3
    audio.play();
    currentImageIndex = (currentImageIndex + 1) % images.length;
    updateImage();
});

function updateImage() {
    image.src = images[currentImageIndex];
}
function recoilGun() {
    const gun = document.querySelector('.gun');
    gun.classList.add('recoil');
    setTimeout(() => {
        gun.classList.remove('recoil');
    }, 400); // Adjust the delay for a slower animation
}
function recoilGun2() {
    const gun2 = document.querySelector('.gun2');
    gun2.classList.add('recoil2');
    setTimeout(() => {
        gun2.classList.remove('recoil2');
    }, 400); // Adjust the delay for a slower animation
}