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
        isClosed = false;

    var navButtonLeft = $('.nav-button-left');
    var navButtonRight = $('.nav-button-right');

    trigger.click(function () {
        hamburger_cross();
    });

    function hamburger_cross() {

        if (isClosed == true) {
            navButtonLeft.show();
            navButtonRight.show();
            trigger.removeClass('is-open');
            trigger.addClass('is-closed');
            isClosed = false;
        } else {
            navButtonLeft.hide();
            navButtonRight.hide();
            trigger.removeClass('is-closed');
            trigger.addClass('is-open');
            isClosed = true;
        }
    }

    $(document).on('click', function (e) {
        // If the click is outside of the hamburger button and the navbar
        if ($(e.target).closest('#page-content-wrapper').length === 1 && isClosed) {
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

// swiping navigation on mobile
document.addEventListener("DOMContentLoaded", function () {
    let leftNav = document.querySelector(".nav-button-left");
    let rightNav = document.querySelector(".nav-button-right");

    // only add swipe functionality if at least one nav button exists
    if (!leftNav && !rightNav) {
        return;
    }

    let touchStartX = 0;
    let touchStartY = 0;
    let touchEndX = 0;
    let touchEndY = 0;
    let touchStartTime = 0;

    function handleGesture() {
        let deltaX = touchEndX - touchStartX;
        let deltaY = Math.abs(touchEndY - touchStartY);
        let duration = Date.now() - touchStartTime;

        // check mostly horizontal swipe, enough distance, not too fast
        if (Math.abs(deltaX) > 80 && deltaY < 50 && duration > 150) {
            if (deltaX < 0 && rightNav) {
                // swiped left
                window.location.href = rightNav.href;
            } else if (deltaX > 0 && leftNav) {
                // swiped right
                window.location.href = leftNav.href;
            }
        }
    }

    document.addEventListener("touchstart", function (event) {
        touchStartX = event.changedTouches[0].screenX;
        touchStartY = event.changedTouches[0].screenY;
        touchStartTime = Date.now();
    });

    document.addEventListener("touchend", function (event) {
        touchEndX = event.changedTouches[0].screenX;
        touchEndY = event.changedTouches[0].screenY;
        handleGesture();
    });
});


// tooltip mouse pointer
document.addEventListener("DOMContentLoaded", function () {
    const tooltip = document.createElement("div");
    tooltip.className = "image-tooltip";
    document.body.appendChild(tooltip);

    document.querySelectorAll(".image-wrapper").forEach(wrapper => {
        wrapper.addEventListener("mousemove", function (event) {
            tooltip.innerText = this.getAttribute("data-tooltip");
            tooltip.style.left = event.pageX + 10 + "px";  // Offset to the right
            tooltip.style.top = event.pageY + 10 + "px";   // Offset slightly below
            tooltip.style.opacity = 1;
        });

        wrapper.addEventListener("mouseleave", function () {
            tooltip.style.opacity = 0;
        });
    });
});
