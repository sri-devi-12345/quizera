from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
from learning_content import LEARNING_CONTENT

import sqlite3
import os


# ============================================================
# APP
# ============================================================

app = Flask(__name__)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(
    BASE_DIR,
    "database",
    "quiz.db"
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "static",
    "uploads",
    "profile_pictures"
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(
    os.path.dirname(DATABASE),
    exist_ok=True
)

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# ============================================================
# DATABASE
# ============================================================

def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


# ============================================================
# ALL QUIZ / LEARNING TOPICS
# ============================================================

QUIZ_TOPICS = [
    {
        "title": "Python Programming",
        "category": "Python",
        "description": "Learn Python syntax, variables, conditions, loops, functions and problem solving.",
        "level": "Beginner",
        "icon": "🐍"
    },
    {
        "title": "C Programming",
        "category": "C",
        "description": "Learn C programming fundamentals, functions, arrays, pointers and memory.",
        "level": "Beginner",
        "icon": "🔵"
    },
    {
        "title": "C++ Programming",
        "category": "C++",
        "description": "Learn C++ programming, object-oriented concepts, STL and problem solving.",
        "level": "Intermediate",
        "icon": "🔷"
    },
    {
        "title": "Java Programming",
        "category": "Java",
        "description": "Learn Java syntax, OOP, classes, methods, collections and exceptions.",
        "level": "Beginner",
        "icon": "☕"
    },
    {
        "title": "PHP Programming",
        "category": "PHP",
        "description": "Learn PHP fundamentals, variables, functions, forms and server-side development.",
        "level": "Beginner",
        "icon": "🐘"
    },
    {
        "title": "SQL",
        "category": "SQL",
        "description": "Learn SQL queries, tables, filtering, joins, grouping and database operations.",
        "level": "Beginner",
        "icon": "🗄️"
    },
    {
        "title": "JavaScript",
        "category": "JavaScript",
        "description": "Learn JavaScript variables, functions, DOM, events, arrays and modern syntax.",
        "level": "Beginner",
        "icon": "🟨"
    },
    {
        "title": "Web Development",
        "category": "Web Development",
        "description": "Learn how modern websites work with frontend and backend technologies.",
        "level": "Beginner",
        "icon": "🌐"
    },
    {
        "title": "Web Designing",
        "category": "Web Designing",
        "description": "Learn layouts, typography, colors, responsive design and visual web design.",
        "level": "Beginner",
        "icon": "🎨"
    },
    {
        "title": "App Development",
        "category": "App Development",
        "description": "Learn the fundamentals of designing and developing mobile applications.",
        "level": "Beginner",
        "icon": "📱"
    },
    {
        "title": "UI/UX Design",
        "category": "UI/UX Design",
        "description": "Learn user interface design, user experience, wireframes and usability.",
        "level": "Beginner",
        "icon": "🖌️"
    },
    {
        "title": "Artificial Intelligence",
        "category": "Artificial Intelligence",
        "description": "Understand AI concepts, intelligent systems, neural networks and applications.",
        "level": "Beginner",
        "icon": "🤖"
    },
    {
        "title": "Machine Learning",
        "category": "Machine Learning",
        "description": "Explore datasets, models, training, evaluation and machine learning algorithms.",
        "level": "Intermediate",
        "icon": "🧠"
    },
    {
        "title": "Computer Science",
        "category": "Computer Science",
        "description": "Build a strong foundation in algorithms, operating systems and computing concepts.",
        "level": "Beginner",
        "icon": "💻"
    },
    {
        "title": "Data Structures",
        "category": "Data Structures",
        "description": "Learn arrays, linked lists, stacks, queues, trees, graphs and algorithms.",
        "level": "Intermediate",
        "icon": "🧩"
    },
    {
        "title": "Cyber Security",
        "category": "Cyber Security",
        "description": "Learn cybersecurity fundamentals, threats, authentication and data protection.",
        "level": "Beginner",
        "icon": "🔐"
    },
    {
        "title": "Prompt Making",
        "category": "Prompt Making",
        "description": "Learn how to write clear, useful and effective prompts for AI systems.",
        "level": "Beginner",
        "icon": "✨"
    },
    {
        "title": "Content Creation",
        "category": "Content Creation",
        "description": "Learn content planning, storytelling, social media content and digital creation.",
        "level": "Beginner",
        "icon": "🎬"
    }
]


# ============================================================
# DATABASE INITIALIZATION
# ============================================================

def init_db():

    connection = get_db()
    cursor = connection.cursor()

    # --------------------------------------------------------
    # QUESTIONS
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            hint TEXT,
            category TEXT DEFAULT 'Python'
        )
    """)

    # --------------------------------------------------------
    # USERS
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT,
            mobile TEXT,
            profile_picture TEXT,
            education TEXT,
            location TEXT
        )
    """)

    # --------------------------------------------------------
    # LEADERBOARD
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            score INTEGER NOT NULL,
            total_questions INTEGER NOT NULL,
            category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # --------------------------------------------------------
    # PROGRESS
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT NOT NULL,
            score INTEGER DEFAULT 0,
            total_questions INTEGER DEFAULT 0,
            percentage REAL DEFAULT 0,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # --------------------------------------------------------
    # LEARNING TOPICS
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learning_topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            category TEXT NOT NULL,
            level TEXT DEFAULT 'Beginner',
            icon TEXT DEFAULT '📚'
        )
    """)

    # ========================================================
    # MIGRATION
    # ========================================================

    cursor.execute("PRAGMA table_info(questions)")

    question_columns = [
        row["name"]
        for row in cursor.fetchall()
    ]

    if "category" not in question_columns:

        cursor.execute("""
            ALTER TABLE questions
            ADD COLUMN category TEXT DEFAULT 'Python'
        """)

    cursor.execute("PRAGMA table_info(leaderboard)")

    leaderboard_columns = [
        row["name"]
        for row in cursor.fetchall()
    ]

    if "created_at" not in leaderboard_columns:

        cursor.execute("""
            ALTER TABLE leaderboard
            ADD COLUMN created_at TIMESTAMP
        """)

    # ========================================================
    # DEFAULT USER
    # ========================================================

    cursor.execute("""
        SELECT COUNT(*) AS count
        FROM users
    """)

    user_count = cursor.fetchone()["count"]

    if user_count == 0:

        cursor.execute("""
            INSERT INTO users
            (
                username,
                email,
                mobile,
                profile_picture,
                education,
                location
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            "Sri Devi",
            "sridevi@example.com",
            "+91 98765 43210",
            "default.png",
            "B.Sc. Computer Science",
            "Chennai, India"
        ))

    # ========================================================
    # LEARNING TOPICS
    # ========================================================

    # Make sure the new 18-topic list is available.
    # Existing old topics are cleared because their categories
    # do not match the new quiz structure.

    cursor.execute("DELETE FROM learning_topics")

    for topic in QUIZ_TOPICS:

        cursor.execute("""
            INSERT INTO learning_topics
            (
                title,
                description,
                category,
                level,
                icon
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            topic["title"],
            topic["description"],
            topic["category"],
            topic["level"],
            topic["icon"]
        ))

    connection.commit()
    connection.close()


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    db = get_db()

    categories = db.execute("""
        SELECT
            category,
            COUNT(*) AS count
        FROM questions
        GROUP BY category
        ORDER BY category
    """).fetchall()

    category_counts = {
        row["category"]: row["count"]
        for row in categories
    }

    total_questions = db.execute("""
        SELECT COUNT(*) AS count
        FROM questions
    """).fetchone()["count"]

    total_topics = db.execute("""
        SELECT COUNT(*) AS count
        FROM learning_topics
    """).fetchone()["count"]

    db.close()

    return render_template(
        "index.html",
        category_counts=category_counts,
        total_questions=total_questions,
        total_topics=total_topics
    )


# ============================================================
# QUIZZES
# ============================================================

@app.route("/quizzes")
def quizzes():

    db = get_db()

    rows = db.execute("""
        SELECT
            category,
            COUNT(*) AS count
        FROM questions
        GROUP BY category
        ORDER BY category
    """).fetchall()

    category_counts = {
        row["category"]: row["count"]
        for row in rows
    }

    db.close()

    return render_template(
        "quizzes.html",
        category_counts=category_counts,
        topics=QUIZ_TOPICS
    )


# ============================================================
# LEARN
# ============================================================

@app.route("/learn")
def learn():

    category = request.args.get("category")

    db = get_db()

    if category:

        topics = db.execute("""
            SELECT *
            FROM learning_topics
            WHERE category = ?
            ORDER BY id
        """, (category,)).fetchall()

    else:

        topics = db.execute("""
            SELECT *
            FROM learning_topics
            ORDER BY id
        """).fetchall()

    db.close()

    return render_template(
        "learn.html",
        topics=topics,
        selected_category=category
    )


# ============================================================
# LEARN TOPIC
# ============================================================

@app.route("/learn/<int:topic_id>")
def learn_topic(topic_id):

    db = get_db()

    topic = db.execute("""
        SELECT *
        FROM learning_topics
        WHERE id = ?
    """, (topic_id,)).fetchone()

    db.close()

    if topic is None:
        return render_template("404.html"), 404

    topic = dict(topic)

    content = LEARNING_CONTENT.get(
        topic["title"]
    )

    if content is None:

        content = {
            "title": topic["title"],
            "level": topic["level"],
            "icon": topic["icon"],
            "sections": []
        }

    return render_template(
        "learn_topic.html",
        topic=topic,
        content=content
    )


# ============================================================
# PRACTICE
# ============================================================

@app.route("/practice")
def practice():

    db = get_db()

    rows = db.execute("""
        SELECT
            category,
            COUNT(*) AS count
        FROM questions
        GROUP BY category
        ORDER BY category
    """).fetchall()

    category_counts = {
        row["category"]: row["count"]
        for row in rows
    }

    db.close()

    return render_template(
        "practice.html",
        category_counts=category_counts,
        categories=rows,
        topics=QUIZ_TOPICS
    )


# ============================================================
# PRACTICE CATEGORY
# ============================================================

@app.route("/practice/<path:category>")
def practice_category(category):

    db = get_db()

    questions = db.execute("""
        SELECT *
        FROM questions
        WHERE category = ?
        ORDER BY RANDOM()
        LIMIT 10
    """, (category,)).fetchall()

    db.close()

    return render_template(
        "practice_questions.html",
        questions=questions,
        category=category
    )


# ============================================================
# QUIZ
# ============================================================

@app.route("/quiz")
def quiz():

    category = request.args.get("category")

    db = get_db()

    if category:

        # Every topic has 30 questions.
        # RANDOM() changes their order each time.

        rows = db.execute("""
            SELECT *
            FROM questions
            WHERE category = ?
            ORDER BY RANDOM()
            LIMIT 30
        """, (category,)).fetchall()

    else:

        rows = db.execute("""
            SELECT *
            FROM questions
            ORDER BY RANDOM()
            LIMIT 30
        """).fetchall()

    questions = [
        dict(row)
        for row in rows
    ]

    db.close()

    return render_template(
        "quiz.html",
        questions=questions,
        selected_category=category
    )


# ============================================================
# SAVE SCORE
# ============================================================

@app.route(
    "/save-score",
    methods=["POST"]
)
def save_score():

    data = request.get_json(
        silent=True
    )

    if not data:

        return jsonify({
            "success": False,
            "message": "No score data received."
        }), 400

    try:

        score = int(
            data.get(
                "score",
                0
            )
        )

        total_questions = int(
            data.get(
                "total_questions",
                0
            )
        )

    except (
        TypeError,
        ValueError
    ):

        return jsonify({
            "success": False,
            "message": "Invalid score data."
        }), 400

    player_name = data.get(
        "player_name",
        "Sri Devi"
    )

    category = data.get(
        "category",
        "General"
    )

    percentage = 0

    if total_questions > 0:

        percentage = round(
            (
                score /
                total_questions
            ) * 100,
            2
        )

    db = get_db()

    # --------------------------------------------------------
    # USER
    # --------------------------------------------------------

    user = db.execute("""
        SELECT id
        FROM users
        ORDER BY id
        LIMIT 1
    """).fetchone()

    user_id = (
        user["id"]
        if user
        else None
    )

    # --------------------------------------------------------
    # LEADERBOARD
    # --------------------------------------------------------

    db.execute("""
        INSERT INTO leaderboard
        (
            player_name,
            score,
            total_questions,
            category
        )
        VALUES (?, ?, ?, ?)
    """, (
        player_name,
        score,
        total_questions,
        category
    ))

    # --------------------------------------------------------
    # PROGRESS
    # --------------------------------------------------------

    db.execute("""
        INSERT INTO progress
        (
            user_id,
            category,
            score,
            total_questions,
            percentage
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        user_id,
        category,
        score,
        total_questions,
        percentage
    ))

    db.commit()
    db.close()

    return jsonify({
        "success": True,
        "score": score,
        "total_questions": total_questions,
        "percentage": percentage
    })


# ============================================================
# PROGRESS
# ============================================================

@app.route("/progress")
def progress():

    db = get_db()

    records = db.execute("""
        SELECT *
        FROM progress
        ORDER BY completed_at DESC
    """).fetchall()

    stats_row = db.execute("""
        SELECT
            COUNT(*) AS quizzes_completed,
            COALESCE(
                MAX(percentage),
                0
            ) AS best_score,
            COALESCE(
                AVG(percentage),
                0
            ) AS average_score
        FROM progress
    """).fetchone()

    stats = {
        "quizzes_completed":
            stats_row["quizzes_completed"],

        "best_score":
            round(
                stats_row["best_score"],
                2
            ),

        "average_score":
            round(
                stats_row["average_score"],
                2
            )
    }

    db.close()

    return render_template(
        "progress.html",
        progress_data=records,
        progress_records=records,
        stats=stats
    )


# ============================================================
# LEADERBOARD
# ============================================================

@app.route("/leaderboard")
def leaderboard():

    db = get_db()

    rows = db.execute("""
        SELECT
            player_name,
            score,
            total_questions,
            category,
            created_at
        FROM leaderboard
        ORDER BY
            score DESC,
            total_questions DESC,
            id ASC
    """).fetchall()

    db.close()

    return render_template(
        "leaderboard.html",
        leaderboard=rows
    )


# ============================================================
# PROFILE
# ============================================================

@app.route("/profile")
def profile():

    db = get_db()

    user = db.execute("""
        SELECT *
        FROM users
        ORDER BY id
        LIMIT 1
    """).fetchone()

    stats_row = db.execute("""
        SELECT
            COUNT(*) AS quizzes_completed,
            COALESCE(
                MAX(percentage),
                0
            ) AS best_score,
            COALESCE(
                AVG(percentage),
                0
            ) AS average_score
        FROM progress
    """).fetchone()

    stats = {
        "quizzes_completed":
            stats_row["quizzes_completed"],

        "best_score":
            round(
                stats_row["best_score"],
                2
            ),

        "average_score":
            round(
                stats_row["average_score"],
                2
            )
    }

    db.close()

    return render_template(
        "profile.html",
        user=user,
        stats=stats
    )


# ============================================================
# EDIT PROFILE
# ============================================================

@app.route(
    "/profile/edit",
    methods=["GET", "POST"]
)
def edit_profile():

    db = get_db()

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        mobile = request.form.get(
            "mobile",
            ""
        ).strip()

        education = request.form.get(
            "education",
            ""
        ).strip()

        location = request.form.get(
            "location",
            ""
        ).strip()

        db.execute("""
            UPDATE users
            SET
                username = ?,
                email = ?,
                mobile = ?,
                education = ?,
                location = ?
            WHERE id = (
                SELECT id
                FROM users
                ORDER BY id
                LIMIT 1
            )
        """, (
            username,
            email,
            mobile,
            education,
            location
        ))

        db.commit()
        db.close()

        return redirect(
            url_for("profile")
        )

    user = db.execute("""
        SELECT *
        FROM users
        ORDER BY id
        LIMIT 1
    """).fetchone()

    db.close()

    return render_template(
        "edit_profile.html",
        user=user
    )


# ============================================================
# PROFILE PICTURE
# ============================================================

@app.route(
    "/upload-profile-picture",
    methods=["POST"]
)
def upload_profile_picture():

    if "profile_picture" not in request.files:

        return (
            "No file selected.",
            400
        )

    file = request.files[
        "profile_picture"
    ]

    if not file.filename:

        return (
            "No file selected.",
            400
        )

    allowed_extensions = {
        "jpg",
        "jpeg",
        "png",
        "webp"
    }

    extension = (
        file.filename
        .rsplit(".", 1)[-1]
        .lower()
        if "." in file.filename
        else ""
    )

    if extension not in allowed_extensions:

        return (
            "Invalid image format.",
            400
        )

    filename = secure_filename(
        file.filename
    )

    if not filename:

        return (
            "Invalid file name.",
            400
        )

    file.save(
        os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )
    )

    db = get_db()

    db.execute("""
        UPDATE users
        SET profile_picture = ?
        WHERE id = (
            SELECT id
            FROM users
            ORDER BY id
            LIMIT 1
        )
    """, (filename,))

    db.commit()
    db.close()

    return redirect(
        url_for("profile")
    )


# ============================================================
# API — CATEGORIES
# ============================================================

@app.route("/api/categories")
def api_categories():

    db = get_db()

    rows = db.execute("""
        SELECT
            category,
            COUNT(*) AS question_count
        FROM questions
        GROUP BY category
        ORDER BY category
    """).fetchall()

    result = [
        dict(row)
        for row in rows
    ]

    db.close()

    return jsonify(result)


# ============================================================
# API — QUESTIONS
# ============================================================

@app.route("/api/questions")
def api_questions():

    category = request.args.get(
        "category"
    )

    db = get_db()

    if category:

        rows = db.execute("""
            SELECT *
            FROM questions
            WHERE category = ?
            ORDER BY RANDOM()
            LIMIT 30
        """, (category,)).fetchall()

    else:

        rows = db.execute("""
            SELECT *
            FROM questions
            ORDER BY RANDOM()
            LIMIT 30
        """).fetchall()

    result = [
        dict(row)
        for row in rows
    ]

    db.close()

    return jsonify(result)


# ============================================================
# API — PROGRESS
# ============================================================

@app.route("/api/progress")
def api_progress():

    db = get_db()

    rows = db.execute("""
        SELECT *
        FROM progress
        ORDER BY completed_at DESC
    """).fetchall()

    result = [
        dict(row)
        for row in rows
    ]

    db.close()

    return jsonify(result)


# ============================================================
# 404
# ============================================================

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "404.html"
    ), 404


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    init_db()

    app.run(
        debug=True
    )