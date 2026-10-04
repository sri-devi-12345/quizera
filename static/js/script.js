/*
=========================================================
   QUIZERA - MAIN SCRIPT
=========================================================
*/

document.addEventListener("DOMContentLoaded", function () {


    /* -----------------------------------------------------
       NAVIGATION
       ----------------------------------------------------- */

    const navLinks =
        document.querySelectorAll(".nav-links a");

    navLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            navLinks.forEach(function (item) {
                item.classList.remove("active");
            });

            this.classList.add("active");
        });

    });


    /* -----------------------------------------------------
       START QUIZ BUTTON
       ----------------------------------------------------- */

    const startButton =
        document.querySelector(".start-btn");

    if (startButton) {

        startButton.addEventListener(
            "click",
            function () {

                window.location.href = "/quiz";

            }
        );

    }


    /* -----------------------------------------------------
       SMOOTH SCROLL
       ----------------------------------------------------- */

    const scrollLinks =
        document.querySelectorAll('a[href^="#"]');

    scrollLinks.forEach(function (link) {

        link.addEventListener(
            "click",
            function (event) {

                const targetId =
                    this.getAttribute("href");


                if (
                    !targetId ||
                    targetId === "#"
                ) {
                    return;
                }


                const target =
                    document.querySelector(targetId);


                if (target) {

                    event.preventDefault();

                    target.scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });

                }

            }
        );

    });


    /* -----------------------------------------------------
       PROFILE PICTURE VALIDATION
       ----------------------------------------------------- */

    const profilePictureInput =
        document.querySelector("#profile_picture");


    if (profilePictureInput) {

        profilePictureInput.addEventListener(
            "change",
            function () {

                const file =
                    this.files[0];


                if (!file) {
                    return;
                }


                const allowedTypes = [
                    "image/jpeg",
                    "image/png",
                    "image/jpg",
                    "image/webp"
                ];


                if (!allowedTypes.includes(file.type)) {

                    alert(
                        "Please select a JPG, PNG or WEBP image."
                    );

                    this.value = "";

                    return;
                }


                const maxSize =
                    5 * 1024 * 1024;


                if (file.size > maxSize) {

                    alert(
                        "Image size must be less than 5 MB."
                    );

                    this.value = "";

                }

            }
        );

    }


    /* -----------------------------------------------------
       FORM SUBMIT LOADING EFFECT
       ----------------------------------------------------- */

    const forms =
        document.querySelectorAll("form");


    forms.forEach(function (form) {

        form.addEventListener(
            "submit",
            function () {

                const submitButton =
                    form.querySelector(
                        'button[type="submit"]'
                    );


                if (!submitButton) {
                    return;
                }


                if (
                    submitButton.dataset.loading ===
                    "true"
                ) {
                    return;
                }


                submitButton.dataset.loading =
                    "true";


                submitButton.dataset.originalText =
                    submitButton.textContent;


                submitButton.textContent =
                    "Saving...";

            }
        );

    });


    /* -----------------------------------------------------
       CARD INTERACTION
       ----------------------------------------------------- */

    const cards =
        document.querySelectorAll(
            ".quiz-category-card, " +
            ".learning-card, " +
            ".practice-card, " +
            ".category-card, " +
            ".journey-card, " +
            ".hero-card"
        );


    cards.forEach(function (card) {

        card.addEventListener(
            "mouseenter",
            function () {

                this.classList.add(
                    "is-hovered"
                );

            }
        );


        card.addEventListener(
            "mouseleave",
            function () {

                this.classList.remove(
                    "is-hovered"
                );

            }
        );

    });


    /* -----------------------------------------------------
       ESCAPE KEY - CLOSE MODALS
       ----------------------------------------------------- */

    document.addEventListener(
        "keydown",
        function (event) {

            if (event.key !== "Escape") {
                return;
            }


            const modal =
                document.querySelector(
                    ".modal-overlay"
                );


            if (
                modal &&
                modal.classList.contains("show")
            ) {

                modal.classList.remove("show");

            }

        }
    );


    /* -----------------------------------------------------
       CLOSE MODAL WHEN CLICKING OUTSIDE
       ----------------------------------------------------- */

    const modalOverlays =
        document.querySelectorAll(
            ".modal-overlay"
        );


    modalOverlays.forEach(function (modal) {

        modal.addEventListener(
            "click",
            function (event) {

                if (event.target === modal) {

                    modal.classList.remove(
                        "show"
                    );

                }

            }
        );

    });


    /* =====================================================
       QUIZERA ROBOT - PUPIL / EYE MOVEMENT
       ===================================================== */

    const robot =
        document.querySelector("#quizeraRobot");


    if (robot) {

        const robotEyes =
            robot.querySelectorAll(".robot-eye");


        robotEyes.forEach(function (eye) {

            const pupil =
                eye.querySelector("i");


            if (!pupil) {
                return;
            }


            // Keep the original position
            pupil.style.transform =
                "translate(0px, 0px)";


            eye.dataset.pupilReady = "true";

        });


        document.addEventListener(
            "mousemove",
            function (event) {

                robotEyes.forEach(function (eye) {

                    const pupil =
                        eye.querySelector("i");


                    if (!pupil) {
                        return;
                    }


                    const eyeRect =
                        eye.getBoundingClientRect();


                    const eyeCenterX =
                        eyeRect.left +
                        (eyeRect.width / 2);


                    const eyeCenterY =
                        eyeRect.top +
                        (eyeRect.height / 2);


                    const mouseX =
                        event.clientX;


                    const mouseY =
                        event.clientY;


                    const differenceX =
                        mouseX - eyeCenterX;


                    const differenceY =
                        mouseY - eyeCenterY;


                    const angle =
                        Math.atan2(
                            differenceY,
                            differenceX
                        );


                    /*
                     * Small movement so the
                     * robot stays cute and natural.
                     */
                    const pupilDistance = 4;


                    const pupilX =
                        Math.cos(angle) *
                        pupilDistance;


                    const pupilY =
                        Math.sin(angle) *
                        pupilDistance;


                    pupil.style.transform =
                        `translate(${pupilX}px, ${pupilY}px)`;

                });

            }
        );


        /*
         * Return pupils to the center when
         * the mouse leaves the browser window.
         */

        document.addEventListener(
            "mouseleave",
            function () {

                robotEyes.forEach(function (eye) {

                    const pupil =
                        eye.querySelector("i");


                    if (!pupil) {
                        return;
                    }


                    pupil.style.transform =
                        "translate(0px, 0px)";

                });

            }
        );

    }

});