document.addEventListener("DOMContentLoaded", function () {

    // =====================================================
    // GET QUESTIONS
    // =====================================================

    const quizData = document.getElementById("quiz-data");

    if (!quizData) {
        console.error("Quiz data not found.");
        return;
    }

    let questions = [];

    try {
        questions = JSON.parse(quizData.textContent);
    } catch (error) {
        console.error("Failed to read quiz data:", error);
        return;
    }

    if (!questions || questions.length === 0) {
        console.error("No questions available.");

        const questionElement =
            document.getElementById("question");

        if (questionElement) {
            questionElement.textContent =
                "No questions available.";
        }

        return;
    }

    console.log("Quiz questions loaded:", questions);


    // =====================================================
    // ELEMENTS
    // =====================================================

    const questionElement =
        document.getElementById("question");

    const answersElement =
        document.getElementById("answers");

    const questionCount =
        document.getElementById("question-count");

    const progressPercent =
        document.getElementById("progress-percent");

    const progressFill =
        document.getElementById("quiz-progress-fill");

    const nextButton =
        document.getElementById("next-btn");

    const hintButton =
        document.getElementById("hint-btn");

    const hintText =
        document.getElementById("hint-text");

    const timerElement =
        document.getElementById("quiz-timer");

    const categoryElement =
        document.getElementById("question-category");

    const nameModal =
        document.getElementById("name-modal");

    const playerName =
        document.getElementById("player-name");

    const saveNameButton =
        document.getElementById("save-name-btn");

    const closeModal =
        document.getElementById("modal-close");


    // =====================================================
    // VARIABLES
    // =====================================================

    let currentQuestion = 0;

    let score = 0;

    let selectedAnswer = false;

    // 2 MINUTES = 120 SECONDS
    const QUIZ_TIME = 120;

    let timeLeft = QUIZ_TIME;

    let timer = null;

    let finished = false;


    // =====================================================
    // GET CATEGORY
    // =====================================================

    function getCategory() {

        const category =
            document.getElementById("quiz-category");

        if (
            category &&
            category.dataset.category
        ) {
            return category.dataset.category;
        }

        if (
            questions[0] &&
            questions[0].category
        ) {
            return questions[0].category;
        }

        return "General";
    }


    // =====================================================
    // SHOW QUESTION
    // =====================================================

    function showQuestion() {

        const question =
            questions[currentQuestion];

        if (!question) {
            finishQuiz();
            return;
        }

        selectedAnswer = false;


        // QUESTION
        questionElement.textContent =
            question.question;


        // CATEGORY
        categoryElement.textContent =
            question.category || getCategory();


        // QUESTION COUNT
        questionCount.textContent =
            `Question ${currentQuestion + 1} / ${questions.length}`;


        // PROGRESS
        const percent =
            Math.round(
                (currentQuestion / questions.length) * 100
            );

        progressPercent.textContent =
            `${percent}%`;

        progressFill.style.width =
            `${percent}%`;


        // CLEAR OLD ANSWERS
        answersElement.innerHTML = "";


        // ANSWERS
        const options = [

            {
                letter: "A",
                text: question.option1
            },

            {
                letter: "B",
                text: question.option2
            },

            {
                letter: "C",
                text: question.option3
            },

            {
                letter: "D",
                text: question.option4
            }

        ];


        options.forEach(function (option, index) {

            const button =
                document.createElement("button");

            button.type = "button";

            button.className =
                "answer-option";

            button.dataset.index =
                index;


            // LETTER
            const letter =
                document.createElement("span");

            letter.className =
                "answer-letter";

            letter.textContent =
                option.letter;


            // TEXT
            const text =
                document.createElement("span");

            text.className =
                "answer-text";

            text.textContent =
                option.text;


            button.appendChild(letter);

            button.appendChild(text);


            // CLICK
            button.addEventListener(
                "click",
                function () {

                    selectAnswer(
                        button,
                        index
                    );

                }
            );


            answersElement.appendChild(button);

        });


        // HINT
        hintText.textContent = "";

        hintText.style.display = "none";

        if (question.hint) {

            hintButton.style.display =
                "inline-flex";

            hintButton.textContent =
                "💡 Show Hint";

        } else {

            hintButton.style.display =
                "none";

        }


        // NEXT BUTTON
        nextButton.disabled = true;

        if (
            currentQuestion ===
            questions.length - 1
        ) {

            nextButton.textContent =
                "Finish Quiz →";

        } else {

            nextButton.textContent =
                "Next Question →";

        }

    }


    // =====================================================
    // SELECT ANSWER
    // =====================================================

    function selectAnswer(button, index) {

        if (selectedAnswer) {
            return;
        }

        selectedAnswer = true;

        const question =
            questions[currentQuestion];


        const allButtons =
            document.querySelectorAll(
                ".answer-option"
            );


        // DISABLE ALL ANSWERS
        allButtons.forEach(function (item) {

            item.disabled = true;

        });


        // FIND CORRECT ANSWER
        const correctIndex =
            getCorrectIndex(
                question.correct_answer,
                question
            );


        // CORRECT ANSWER
        if (index === correctIndex) {

            button.classList.add(
                "answer-correct"
            );

            score++;

        }


        // WRONG ANSWER
        else {

            button.classList.add(
                "answer-wrong"
            );


            if (allButtons[correctIndex]) {

                allButtons[correctIndex]
                    .classList.add(
                        "answer-correct"
                    );

            }

        }


        // ENABLE NEXT
        nextButton.disabled = false;

    }


    // =====================================================
    // FIND CORRECT ANSWER
    // =====================================================

    function getCorrectIndex(
        correctAnswer,
        question
    ) {

        if (
            correctAnswer === null ||
            correctAnswer === undefined
        ) {
            return -1;
        }


        const answer =
            String(correctAnswer).trim();


        // 1 2 3 4
        if (
            ["1", "2", "3", "4"]
                .includes(answer)
        ) {

            return parseInt(answer) - 1;

        }


        // A B C D
        const upper =
            answer.toUpperCase();


        if (upper === "A") return 0;

        if (upper === "B") return 1;

        if (upper === "C") return 2;

        if (upper === "D") return 3;


        // EXACT TEXT
        const options = [

            question.option1,

            question.option2,

            question.option3,

            question.option4

        ];


        return options.findIndex(
            function (option) {

                return String(option).trim() === answer;

            }
        );

    }


    // =====================================================
    // NEXT QUESTION
    // =====================================================

    nextButton.addEventListener(
        "click",
        function () {

            if (!selectedAnswer) {
                return;
            }


            // LAST QUESTION
            if (
                currentQuestion >=
                questions.length - 1
            ) {

                finishQuiz();

                return;

            }


            // NEXT
            currentQuestion++;

            showQuestion();

        }
    );


    // =====================================================
    // HINT
    // =====================================================

    hintButton.addEventListener(
        "click",
        function () {

            const question =
                questions[currentQuestion];


            if (!question.hint) {
                return;
            }


            if (
                hintText.style.display ===
                "none"
            ) {

                hintText.textContent =
                    question.hint;

                hintText.style.display =
                    "block";

                hintButton.textContent =
                    "💡 Hide Hint";

            } else {

                hintText.style.display =
                    "none";

                hintButton.textContent =
                    "💡 Show Hint";

            }

        }
    );


    // =====================================================
    // TIMER
    // =====================================================

    function startTimer() {

        clearInterval(timer);

        // RESET TO 2 MINUTES
        timeLeft = QUIZ_TIME;

        updateTimer();


        timer = setInterval(
            function () {

                timeLeft--;

                updateTimer();


                // TIME OVER
                if (timeLeft <= 0) {

                    clearInterval(timer);

                    finishQuiz();

                }

            },
            1000
        );

    }


    // =====================================================
    // UPDATE TIMER
    // =====================================================

    function updateTimer() {

        if (!timerElement) {
            return;
        }


        const minutes =
            Math.floor(timeLeft / 60);

        const seconds =
            timeLeft % 60;


        const formattedSeconds =
            String(seconds).padStart(2, "0");


        timerElement.textContent =
            `⏱️ ${minutes}:${formattedSeconds}`;


        // TIMER WARNING
        if (timeLeft <= 30) {

            timerElement.classList.add(
                "timer-warning"
            );

        } else {

            timerElement.classList.remove(
                "timer-warning"
            );

        }

    }


    // =====================================================
    // FINISH QUIZ
    // =====================================================

    function finishQuiz() {

        if (finished) {
            return;
        }

        finished = true;


        // STOP TIMER
        clearInterval(timer);


        // COMPLETE PROGRESS
        if (progressFill) {

            progressFill.style.width =
                "100%";

        }


        if (progressPercent) {

            progressPercent.textContent =
                "100%";

        }


        // SHOW RESULT / NAME MODAL
        if (nameModal) {

            nameModal.style.display =
                "flex";

        }

    }


    // =====================================================
    // SAVE SCORE
    // =====================================================

    saveNameButton.addEventListener(
        "click",
        async function () {

            const name =
                playerName.value.trim() ||
                "Sri Devi";


            const data = {

                player_name: name,

                score: score,

                total_questions:
                    questions.length,

                category:
                    getCategory()

            };


            saveNameButton.disabled = true;

            saveNameButton.textContent =
                "Saving...";


            try {

                const response =
                    await fetch(
                        "/save-score",
                        {

                            method: "POST",

                            headers: {

                                "Content-Type":
                                    "application/json"

                            },

                            body:
                                JSON.stringify(data)

                        }
                    );


                const result =
                    await response.json();


                if (result.success) {

                    window.location.href =
                        "/leaderboard";

                } else {

                    alert(
                        result.message ||
                        "Unable to save score."
                    );


                    saveNameButton.disabled =
                        false;

                    saveNameButton.textContent =
                        "Save My Score →";

                }

            } catch (error) {

                console.error(error);


                alert(
                    "Unable to connect to the server."
                );


                saveNameButton.disabled =
                    false;

                saveNameButton.textContent =
                    "Save My Score →";

            }

        }
    );


    // =====================================================
    // CLOSE MODAL
    // =====================================================

    closeModal.addEventListener(
        "click",
        function () {

            nameModal.style.display =
                "none";

        }
    );


    // =====================================================
    // START QUIZ
    // =====================================================

    showQuestion();

    startTimer();

});