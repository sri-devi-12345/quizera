# =========================================================
# QUIZERA - LEARNING CONTENT
# =========================================================

LEARNING_CONTENT = {

    # =====================================================
    # PYTHON PROGRAMMING
    # =====================================================

    "Python Programming": {
        "title": "Python Programming",
        "level": "Beginner",
        "icon": "🐍",
        "sections": [
            {
                "title": "What is Python?",
                "content": """
Python is a high-level, interpreted programming language
known for its simple and readable syntax.

It is widely used for:

• Web development
• Artificial Intelligence
• Machine Learning
• Data Science
• Automation
• Software development

Python is beginner-friendly because its syntax is easier
to understand compared with many other programming languages.
"""
            },
            {
                "title": "Variables and Data Types",
                "content": """
A variable is a name used to store a value.

Example:

name = "Sri Devi"
age = 20
height = 5.4

Python automatically determines the data type.

Common data types include:

• String
• Integer
• Float
• Boolean
• List
• Tuple
• Dictionary
"""
            },
            {
                "title": "Conditional Statements",
                "content": """
Conditional statements allow a program to make decisions.

The main keywords are:

• if
• elif
• else

Example:

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

The program executes different code depending on the condition.
"""
            },
            {
                "title": "Loops",
                "content": """
Loops are used to repeat a block of code.

Python mainly provides:

• for loop
• while loop

Example:

for i in range(5):
    print(i)

This prints numbers from 0 to 4.
"""
            },
            {
                "title": "Functions",
                "content": """
A function is a reusable block of code.

Python functions are created using the def keyword.

Example:

def greet():
    print("Hello!")

greet()

Functions help make programs organized, reusable and easier
to maintain.
"""
            }
        ]
    },


    # =====================================================
    # C PROGRAMMING
    # =====================================================

    "C Programming": {
        "title": "C Programming",
        "level": "Beginner",
        "icon": "©️",
        "sections": [
            {
                "title": "What is C?",
                "content": """
C is a general-purpose programming language developed by
Dennis Ritchie.

C is widely used for:

• System programming
• Operating systems
• Embedded systems
• Compilers
• Game development

C is known for its speed and low-level memory access.
"""
            },
            {
                "title": "Variables and Data Types",
                "content": """
Variables store values in a program.

Common C data types include:

• int
• float
• char
• double

Example:

int age = 20;
float mark = 85.5;
char grade = 'A';
"""
            },
            {
                "title": "Operators",
                "content": """
Operators are symbols used to perform operations.

Arithmetic operators include:

• +
• -
• *
• /
• %

Example:

int result = 10 + 5;

C also supports relational and logical operators.
"""
            },
            {
                "title": "Conditional Statements",
                "content": """
C provides conditional statements for decision making.

Common statements are:

• if
• if-else
• else-if
• switch

Example:

if (age >= 18) {
    printf("Adult");
} else {
    printf("Minor");
}
"""
            },
            {
                "title": "Loops and Functions",
                "content": """
C provides loops for repeated execution.

Common loops are:

• for
• while
• do-while

Functions are reusable blocks of code.

Example:

void greet() {
    printf("Hello");
}
"""
            }
        ]
    },


    # =====================================================
    # C++ PROGRAMMING
    # =====================================================

    "C++ Programming": {
        "title": "C++ Programming",
        "level": "Beginner",
        "icon": "⚙️",
        "sections": [
            {
                "title": "What is C++?",
                "content": """
C++ is a general-purpose programming language developed
by Bjarne Stroustrup.

It extends the C programming language with features such
as object-oriented programming.

C++ is used in:

• Game development
• System software
• Desktop applications
• High-performance applications
"""
            },
            {
                "title": "Variables and Data Types",
                "content": """
C++ supports several data types.

Examples:

int age = 20;
float price = 10.5;
char grade = 'A';
bool passed = true;

Variables store data that can be used by a program.
"""
            },
            {
                "title": "Classes and Objects",
                "content": """
C++ supports object-oriented programming.

A class is a blueprint for creating objects.

Example:

class Student {
public:
    string name;
};

An object is an instance of a class.
"""
            },
            {
                "title": "Inheritance",
                "content": """
Inheritance allows one class to acquire properties and
behaviors from another class.

It helps reduce code duplication and supports
object-oriented design.

Example:

class Child : public Parent {
};
"""
            },
            {
                "title": "STL",
                "content": """
The Standard Template Library provides useful data
structures and algorithms.

Common STL components include:

• vector
• stack
• queue
• map
• set

STL makes C++ programming more efficient.
"""
            }
        ]
    },


    # =====================================================
    # JAVA PROGRAMMING
    # =====================================================

    "Java Programming": {
        "title": "Java Programming",
        "level": "Beginner",
        "icon": "☕",
        "sections": [
            {
                "title": "What is Java?",
                "content": """
Java is a popular object-oriented programming language.

Java follows the principle:

Write Once, Run Anywhere.

Java is commonly used for:

• Web applications
• Android development
• Enterprise software
• Backend systems
"""
            },
            {
                "title": "Variables and Data Types",
                "content": """
Java is a statically typed language.

Examples:

int age = 20;
double price = 99.5;
char grade = 'A';
boolean active = true;

The variable type must normally be specified when declaring it.
"""
            },
            {
                "title": "Classes and Objects",
                "content": """
Java is strongly based on object-oriented programming.

A class defines the structure and behavior of objects.

Example:

class Student {
    String name;
}

An object can be created using new.
"""
            },
            {
                "title": "Inheritance",
                "content": """
Inheritance allows a class to inherit properties and
methods from another class.

Example:

class Dog extends Animal {
}

Java uses the extends keyword for class inheritance.
"""
            },
            {
                "title": "Exception Handling",
                "content": """
Exception handling helps programs deal with runtime errors.

Java commonly uses:

• try
• catch
• finally
• throw
• throws

Example:

try {
    // code
} catch (Exception e) {
    // handle error
}
"""
            }
        ]
    },


    # =====================================================
    # PHP PROGRAMMING
    # =====================================================

    "PHP Programming": {
        "title": "PHP Programming",
        "level": "Beginner",
        "icon": "🐘",
        "sections": [
            {
                "title": "What is PHP?",
                "content": """
PHP is a server-side scripting language commonly used
for web development.

PHP can be used to create:

• Dynamic websites
• Web applications
• APIs
• Database-driven applications

PHP code commonly runs on a web server.
"""
            },
            {
                "title": "PHP Variables",
                "content": """
PHP variables begin with the dollar symbol.

Example:

$name = "Sri Devi";
$age = 20;

PHP variables do not require an explicit type declaration
in normal usage.
"""
            },
            {
                "title": "Conditional Statements",
                "content": """
PHP supports conditional statements such as:

• if
• elseif
• else
• switch

Example:

if ($age >= 18) {
    echo "Adult";
} else {
    echo "Minor";
}
"""
            },
            {
                "title": "Arrays",
                "content": """
Arrays allow PHP programs to store multiple values.

Example:

$students = ["Anu", "Priya", "Sri"];

PHP supports indexed arrays and associative arrays.
"""
            },
            {
                "title": "PHP and Databases",
                "content": """
PHP is commonly used with databases such as MySQL.

A PHP application can:

• Insert data
• Retrieve data
• Update data
• Delete data

This allows developers to create dynamic web applications.
"""
            }
        ]
    },


    # =====================================================
    # SQL
    # =====================================================

    "SQL": {
        "title": "SQL",
        "level": "Beginner",
        "icon": "🗄️",
        "sections": [
            {
                "title": "What is SQL?",
                "content": """
SQL stands for Structured Query Language.

SQL is used to communicate with relational databases.

It can be used to:

• Retrieve data
• Insert data
• Update data
• Delete data
• Create tables
"""
            },
            {
                "title": "SELECT",
                "content": """
The SELECT statement is used to retrieve data.

Example:

SELECT * FROM students;

This retrieves all columns and rows from the students table.

Specific columns can also be selected.
"""
            },
            {
                "title": "INSERT",
                "content": """
INSERT is used to add new records to a table.

Example:

INSERT INTO students
(name, age)
VALUES
('Sri Devi', 20);

The statement creates a new record.
"""
            },
            {
                "title": "UPDATE and DELETE",
                "content": """
UPDATE changes existing records.

Example:

UPDATE students
SET age = 21
WHERE id = 1;

DELETE removes records.

Example:

DELETE FROM students
WHERE id = 1;

A WHERE condition should be used carefully.
"""
            },
            {
                "title": "Primary Keys and Relationships",
                "content": """
A primary key uniquely identifies a record.

Tables can also be connected using relationships.

Common relationships include:

• One-to-one
• One-to-many
• Many-to-many

Foreign keys are commonly used to connect related tables.
"""
            }
        ]
    },


    # =====================================================
    # JAVASCRIPT
    # =====================================================

    "JavaScript": {
        "title": "JavaScript",
        "level": "Beginner",
        "icon": "🟨",
        "sections": [
            {
                "title": "What is JavaScript?",
                "content": """
JavaScript is a programming language widely used to make
web pages interactive.

It can be used for:

• Buttons
• Forms
• Animations
• Dynamic content
• API requests
• Web applications
"""
            },
            {
                "title": "Variables",
                "content": """
JavaScript provides several ways to declare variables.

Common keywords are:

• let
• const
• var

Example:

let age = 20;
const name = "Sri Devi";

const is commonly used when a variable should not be reassigned.
"""
            },
            {
                "title": "Functions",
                "content": """
Functions are reusable blocks of JavaScript code.

Example:

function greet() {
    console.log("Hello!");
}

greet();

JavaScript also supports arrow functions.
"""
            },
            {
                "title": "DOM Manipulation",
                "content": """
The Document Object Model represents the structure of a
web page.

JavaScript can modify HTML elements.

Example:

document.getElementById("title").textContent = "Hello";
"""
            },
            {
                "title": "Events",
                "content": """
Events occur when users interact with a web page.

Examples include:

• click
• submit
• mouseover
• keydown

JavaScript can listen for events using event listeners.

Example:

button.addEventListener("click", function() {
    alert("Clicked!");
});
"""
            }
        ]
    },


    # =====================================================
    # WEB DEVELOPMENT
    # =====================================================

    "Web Development": {
        "title": "Web Development",
        "level": "Beginner",
        "icon": "🌐",
        "sections": [
            {
                "title": "What is Web Development?",
                "content": """
Web development is the process of creating websites and
web applications.

It generally involves:

• HTML
• CSS
• JavaScript
• Backend technologies
• Databases
"""
            },
            {
                "title": "Frontend Development",
                "content": """
Frontend development focuses on the part of a website
that users see and interact with.

Common frontend technologies include:

• HTML
• CSS
• JavaScript
• React
"""
            },
            {
                "title": "Backend Development",
                "content": """
Backend development handles server-side operations.

The backend can manage:

• Business logic
• Authentication
• Databases
• APIs
• Server requests

Technologies include Python, Java, PHP and Node.js.
"""
            },
            {
                "title": "APIs",
                "content": """
An API allows different software systems to communicate.

Web applications commonly use HTTP APIs.

Common HTTP methods include:

• GET
• POST
• PUT
• DELETE
"""
            },
            {
                "title": "Full Stack Development",
                "content": """
Full stack development involves working with both
frontend and backend technologies.

A full-stack application may contain:

Frontend → Backend → Database

Developers working across these layers are commonly
called full-stack developers.
"""
            }
        ]
    },


    # =====================================================
    # WEB DESIGNING
    # =====================================================

    "Web Designing": {
        "title": "Web Designing",
        "level": "Beginner",
        "icon": "🎨",
        "sections": [
            {
                "title": "What is Web Designing?",
                "content": """
Web designing focuses on the visual appearance and
user experience of websites.

It includes:

• Layout
• Colors
• Typography
• Images
• Navigation
• Responsive design
"""
            },
            {
                "title": "HTML Structure",
                "content": """
HTML provides the structure of a webpage.

Common elements include:

• Header
• Navigation
• Main
• Section
• Article
• Footer

Good structure makes websites easier to understand.
"""
            },
            {
                "title": "CSS Styling",
                "content": """
CSS controls the visual appearance of a website.

CSS can control:

• Colors
• Fonts
• Spacing
• Borders
• Shadows
• Layout
"""
            },
            {
                "title": "Responsive Design",
                "content": """
Responsive design allows websites to work across different
screen sizes.

A responsive website should work well on:

• Phones
• Tablets
• Laptops
• Desktop computers

CSS media queries are commonly used for responsive layouts.
"""
            },
            {
                "title": "Visual Hierarchy",
                "content": """
Visual hierarchy helps users understand which information
is most important.

It can be created using:

• Size
• Contrast
• Spacing
• Position
• Typography

Good hierarchy improves readability and usability.
"""
            }
        ]
    },


    # =====================================================
    # APP DEVELOPMENT
    # =====================================================

    "App Development": {
        "title": "App Development",
        "level": "Beginner",
        "icon": "📱",
        "sections": [
            {
                "title": "What is App Development?",
                "content": """
App development is the process of creating applications
for mobile devices.

Applications can be developed for platforms such as:

• Android
• iOS

Apps can provide services, entertainment, communication
and productivity features.
"""
            },
            {
                "title": "Mobile App UI",
                "content": """
The user interface is the part of an application that
users interact with.

Important UI elements include:

• Buttons
• Text fields
• Menus
• Navigation bars
• Cards
• Images
"""
            },
            {
                "title": "App Navigation",
                "content": """
Navigation allows users to move between different
screens of an application.

Good navigation should be:

• Clear
• Consistent
• Easy to understand
• Easy to access
"""
            },
            {
                "title": "APIs in Mobile Apps",
                "content": """
Mobile applications often communicate with backend
servers using APIs.

An app may use an API to:

• Retrieve data
• Send user information
• Authenticate users
• Upload files
"""
            },
            {
                "title": "Testing Applications",
                "content": """
Testing helps developers identify problems before an
application is released.

Testing can include:

• Functional testing
• UI testing
• Performance testing
• Compatibility testing

Testing improves application quality.
"""
            }
        ]
    },


    # =====================================================
    # UI/UX DESIGN
    # =====================================================

    "UI/UX Design": {
        "title": "UI/UX Design",
        "level": "Beginner",
        "icon": "✨",
        "sections": [
            {
                "title": "What is UI Design?",
                "content": """
UI stands for User Interface.

UI design focuses on the visual elements users interact
with.

Examples include:

• Buttons
• Forms
• Menus
• Icons
• Colors
• Typography
"""
            },
            {
                "title": "What is UX Design?",
                "content": """
UX stands for User Experience.

UX design focuses on how easy, useful and enjoyable a
product is to use.

A good UX considers:

• User needs
• Usability
• Accessibility
• Navigation
• Feedback
"""
            },
            {
                "title": "Wireframes",
                "content": """
A wireframe is a simple visual representation of a
website or application.

Wireframes help designers plan:

• Layout
• Navigation
• Content placement
• User flow

They are usually created before detailed visual design.
"""
            },
            {
                "title": "Typography and Color",
                "content": """
Typography involves choosing and arranging text.

Color can communicate meaning and create visual hierarchy.

Good design should maintain:

• Readability
• Contrast
• Consistency
• Visual balance
"""
            },
            {
                "title": "User-Centered Design",
                "content": """
User-centered design focuses on the needs of the people
who will use the product.

Designers may use:

• User research
• Personas
• User testing
• Feedback

The goal is to create useful and usable experiences.
"""
            }
        ]
    },


    # =====================================================
    # ARTIFICIAL INTELLIGENCE
    # =====================================================

    "Artificial Intelligence": {
        "title": "Artificial Intelligence",
        "level": "Beginner",
        "icon": "🤖",
        "sections": [
            {
                "title": "What is AI?",
                "content": """
Artificial Intelligence, or AI, is a field of computer
science focused on creating systems that can perform tasks
that normally require human intelligence.

Examples include:

• Understanding language
• Recognizing images
• Making predictions
• Solving problems
• Generating content
"""
            },
            {
                "title": "Machine Learning",
                "content": """
Machine Learning is a branch of AI where computers learn
patterns from data.

Instead of explicitly programming every rule, a model learns
from examples.
"""
            },
            {
                "title": "Training Data",
                "content": """
Training data is the data used to teach a machine learning
model.

Examples include:

• Images
• Text
• Audio
• Numbers
• Sensor data

The quality of data can strongly affect model performance.
"""
            },
            {
                "title": "Neural Networks",
                "content": """
Neural networks are machine learning models inspired by
biological neural networks.

They commonly contain:

• Input layer
• Hidden layers
• Output layer

They are widely used in image and language applications.
"""
            },
            {
                "title": "Generative AI",
                "content": """
Generative AI refers to AI systems that can create new content.

They can generate:

• Text
• Images
• Audio
• Video
• Computer code

The generated content is produced from patterns learned
during training.
"""
            }
        ]
    },


    # =====================================================
    # MACHINE LEARNING
    # =====================================================

    "Machine Learning": {
        "title": "Machine Learning",
        "level": "Intermediate",
        "icon": "🧠",
        "sections": [
            {
                "title": "What is Machine Learning?",
                "content": """
Machine Learning is a field of AI where computer systems
learn patterns from data and use those patterns to make
predictions or decisions.
"""
            },
            {
                "title": "Supervised Learning",
                "content": """
Supervised learning uses labelled training data.

The model learns the relationship between input data and
known outputs.

Common tasks include:

• Classification
• Regression
"""
            },
            {
                "title": "Unsupervised Learning",
                "content": """
Unsupervised learning works with data that does not have
labelled outputs.

The model attempts to discover patterns or structures
within the data.

Clustering is a common example.
"""
            },
            {
                "title": "Model Training",
                "content": """
During training, a machine learning model adjusts its
parameters based on training data.

The goal is to learn patterns that allow the model to
perform well on new data.
"""
            },
            {
                "title": "Testing and Evaluation",
                "content": """
A trained model should be evaluated using data that was
not used for training.

Evaluation helps determine how well a model generalizes
to new examples.

Different tasks require different evaluation measures.
"""
            }
        ]
    },


    # =====================================================
    # COMPUTER SCIENCE
    # =====================================================

    "Computer Science": {
        "title": "Computer Science",
        "level": "Beginner",
        "icon": "💻",
        "sections": [
            {
                "title": "What is Computer Science?",
                "content": """
Computer Science is the study of computation, algorithms,
software, data and computer systems.

It includes:

• Programming
• Algorithms
• Data Structures
• Databases
• Operating Systems
• Artificial Intelligence
• Computer Networks
"""
            },
            {
                "title": "Algorithms",
                "content": """
An algorithm is a step-by-step procedure used to solve
a problem or perform a task.

A good algorithm should be:

• Clear
• Finite
• Correct
• Efficient
"""
            },
            {
                "title": "Data Structures",
                "content": """
Data structures are ways of organizing and storing data.

Examples include:

• Arrays
• Lists
• Stacks
• Queues
• Trees
• Graphs
• Hash tables
"""
            },
            {
                "title": "Operating Systems",
                "content": """
An operating system manages the hardware and software
resources of a computer.

Examples include:

• Windows
• Linux
• macOS
• Android

Operating systems manage processes, memory, files and devices.
"""
            },
            {
                "title": "Computer Networks",
                "content": """
Computer networks allow devices to communicate with each
other.

Important concepts include:

• IP addresses
• Routers
• Servers
• Protocols
• Internet

Networks allow computers and other devices to exchange data.
"""
            }
        ]
    },


    # =====================================================
    # DATA STRUCTURES
    # =====================================================

    "Data Structures": {
        "title": "Data Structures",
        "level": "Intermediate",
        "icon": "🧩",
        "sections": [
            {
                "title": "Arrays",
                "content": """
An array stores multiple values in an ordered structure.

Elements can generally be accessed using an index.

Example:

numbers = [10, 20, 30, 40]

The first element is accessed using index 0.
"""
            },
            {
                "title": "Stack",
                "content": """
A stack follows the LIFO principle:

Last In, First Out.

Common operations include:

• Push
• Pop
• Peek

Stacks are useful for function calls and undo operations.
"""
            },
            {
                "title": "Queue",
                "content": """
A queue follows the FIFO principle:

First In, First Out.

Common operations include:

• Enqueue
• Dequeue

Queues are useful in scheduling and task processing systems.
"""
            },
            {
                "title": "Trees",
                "content": """
A tree is a hierarchical data structure.

Important concepts include:

• Root
• Parent
• Child
• Leaf
• Subtree

Binary trees are a common type of tree.
"""
            },
            {
                "title": "Graphs",
                "content": """
A graph consists of vertices and edges.

Graphs can represent:

• Social networks
• Road systems
• Computer networks
• Recommendation systems

Graphs may be directed or undirected.
"""
            }
        ]
    },


    # =====================================================
    # CYBER SECURITY
    # =====================================================

    "Cyber Security": {
        "title": "Cyber Security",
        "level": "Beginner",
        "icon": "🔐",
        "sections": [
            {
                "title": "What is Cyber Security?",
                "content": """
Cyber security is the practice of protecting computers,
networks, applications and data from unauthorized access
and attacks.

It helps protect:

• Confidentiality
• Integrity
• Availability
"""
            },
            {
                "title": "Passwords",
                "content": """
Strong passwords help protect user accounts.

A strong password should generally:

• Be sufficiently long
• Avoid easily guessed information
• Be unique
• Avoid common passwords

Password managers can help manage unique passwords.
"""
            },
            {
                "title": "Phishing",
                "content": """
Phishing is a type of social engineering attack.

Attackers may send fake messages designed to trick users
into revealing information or clicking malicious links.

Always verify unexpected messages before responding.
"""
            },
            {
                "title": "Encryption",
                "content": """
Encryption transforms readable information into a protected
form using cryptographic techniques.

It is commonly used to protect sensitive information during
storage and communication.
"""
            },
            {
                "title": "Authentication",
                "content": """
Authentication is the process of verifying someone's identity.

Examples include:

• Passwords
• One-time passwords
• Security keys
• Biometrics

Multi-factor authentication provides additional verification.
"""
            }
        ]
    },


    # =====================================================
    # PROMPT MAKING
    # =====================================================

    "Prompt Making": {
        "title": "Prompt Making",
        "level": "Beginner",
        "icon": "💬",
        "sections": [
            {
                "title": "What is a Prompt?",
                "content": """
A prompt is an instruction or input given to an AI system
to produce a desired response.

A prompt can contain:

• Instructions
• Context
• Questions
• Examples
• Output requirements
"""
            },
            {
                "title": "Clear Instructions",
                "content": """
Clear instructions help an AI system understand what you
want.

Instead of:

"Tell me about Python."

A more specific prompt could be:

"Explain Python variables to a beginner using three simple
examples."
"""
            },
            {
                "title": "Adding Context",
                "content": """
Context provides additional information that helps an AI
understand the task.

For example:

"I am a first-year computer science student.
Explain recursion using a simple Python example."

The context helps make the response more relevant.
"""
            },
            {
                "title": "Specifying Output Format",
                "content": """
You can tell an AI how you want the response structured.

Examples:

• Use bullet points
• Create a table
• Give step-by-step instructions
• Provide code
• Keep the answer under 200 words

Output requirements make results easier to use.
"""
            },
            {
                "title": "Improving Prompts",
                "content": """
Good prompts can be improved through iteration.

A useful process is:

1. Write the initial prompt.
2. Check the response.
3. Identify what is missing.
4. Add more context or constraints.
5. Try again.

Prompt making is an iterative skill.
"""
            }
        ]
    },


    # =====================================================
    # CONTENT CREATION
    # =====================================================

    "Content Creation": {
        "title": "Content Creation",
        "level": "Beginner",
        "icon": "🎬",
        "sections": [
            {
                "title": "What is Content Creation?",
                "content": """
Content creation is the process of producing material
for an audience.

Content can include:

• Articles
• Videos
• Images
• Social media posts
• Podcasts
• Educational content
"""
            },
            {
                "title": "Understanding Your Audience",
                "content": """
Understanding your audience helps you create useful content.

Consider:

• Age group
• Interests
• Problems
• Knowledge level
• Preferred platform

Audience research helps make content more relevant.
"""
            },
            {
                "title": "Content Planning",
                "content": """
Planning helps creators produce content consistently.

A content plan may include:

• Topic
• Format
• Target audience
• Publishing date
• Platform

A content calendar can help organize future content.
"""
            },
            {
                "title": "Storytelling",
                "content": """
Storytelling helps make content more engaging.

A simple structure can include:

• Beginning
• Problem
• Development
• Solution
• Conclusion

Stories can make information easier to remember.
"""
            },
            {
                "title": "Content Quality",
                "content": """
High-quality content should provide value to its audience.

Important factors include:

• Accuracy
• Clarity
• Originality
• Good presentation
• Consistency

Creators should also respect copyright and avoid misleading
information.
"""
            }
        ]
    }
}