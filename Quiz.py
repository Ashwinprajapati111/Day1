# Simple Quiz Game

# List of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Mark Twain", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "Which element has the atomic number 1?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Hydrogen", "D. Helium"],
        "answer": "C"
    }
]

# Function to run the quiz
def run_quiz(questions):
    score = 0  # Initialize score
    
    # Loop through each question in the quiz
    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question['question']}")
        for option in question["options"]:
            print(option)
        
        # Get user's answer
        answer = input("Your answer (A/B/C/D): ").upper()
        
        # Check if the answer is correct
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1  # Increment score for a correct answer
        else:
            print(f"Incorrect! The correct answer was {question['answer']}.\n")
    
    # Display final score
    print(f"Quiz completed! Your final score is {score}/{len(questions)}")

# Run the quiz
run_quiz(questions)
