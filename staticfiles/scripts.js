// Back to top button
document.addEventListener("DOMContentLoaded", function () {
    var button = document.getElementById("backToTopBtn");

    // Show the button when the user scrolls down 300px from the top of the page
    window.addEventListener("scroll", function () {
        if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
            button.style.display = "block";
        } else {
            button.style.display = "none";
        }
    });

    // Scroll back to the top when the button is clicked
    button.addEventListener("click", function () {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    });
});