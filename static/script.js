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

// navbar import
// async function loadTemplates() {
//     document.getElementById("navbar").innerHTML = await fetch('navbar.html').then(res => res.text());
// }
// loadTemplates();

$(document).ready(function () {

    // js for navbar
    var trigger = $('.hamburger'),
        overlay = $('.overlay'),
        isClosed = false;

    trigger.click(function () {
        hamburger_cross();
    });

    function hamburger_cross() {

        if (isClosed == true) {
            console.log(isClosed)
            // overlay.hide();
            trigger.removeClass('is-open');
            trigger.addClass('is-closed');
            isClosed = false;
        } else {
            console.log(isClosed)
            // overlay.show();
            trigger.removeClass('is-closed');
            trigger.addClass('is-open');
            isClosed = true;
        }
    }

    // close navbar when clicking outside of it
    overlay.click(function () {
        if (!overlay.hasClass('index')) {
            hamburger_cross();
            $('#wrapper').toggleClass('toggled');
        }
    });

    // adds the class "toggled" if it's not present, and removes it if it is already present
    $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
    });

    // Get the button that opens the popup
    var btn = document.getElementById("infoBtn");

    if (btn) {

        // Get the element that represents the popup
        var popup = document.getElementById("popup");

        // Get the <span> element that closes the popup
        var closeBtn = document.querySelector(".close-btn");

        // When the user clicks on the button, open the popup
        btn.onclick = function () {
            popup.style.display = "flex";
        }

        // When the user clicks on <span> (x), close the popup
        closeBtn.onclick = function () {
            popup.style.display = "none";
        }

        // Also close the popup if the user clicks outside of the popup content
        window.onclick = function (event) {
            if (event.target == popup) {
                popup.style.display = "none";
            }
        }
    }

    // Close the popup when the user presses the Esc key
    document.addEventListener('keydown', function (event) {
        if (event.key === "Escape") { // Check if the key is the "Escape" key
            if (popup.style.display === "flex") { // Check if the popup is currently displayed
                popup.style.display = "none";
            }
        }
    });

    // nested dropdowns
    $(document).ready(function () {
        // Enable dropdown and sub-dropdown toggle
        $('.dropdown-toggle').on('click', function (e) {
            e.stopPropagation();
            e.preventDefault();
            const $el = $(this).next('.dropdown-menu');
            const $parent = $(this).closest('.dropdown');

            // Close any other open sub-dropdowns
            $parent.siblings('.dropdown').find('.dropdown-menu').removeClass('show');

            // Toggle the dropdown or sub-dropdown
            $el.toggleClass('show');
        });

        // Close dropdowns when clicking outside
        $(document).on('click', function (e) {
            $('.dropdown-menu').removeClass('show');
        });
    });

});
