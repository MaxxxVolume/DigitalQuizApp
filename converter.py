import json
import re

print("Starting quiz conversion...")

# building a list of question dictionaries
new_quiz_data = {"questions": []}

# helper dictionary to map letters to list indices
letter_to_index = {"A": 0, "B": 1, "C":2, "D": 3}

try: 
    # Read text File
    with open("raw_quiz.txt", "r", encoding="utf-8") as f:
        full_text = f.read()

    # splitting the file into question blocks
    question_blocks = full_text.split("### Question ")[1:]

    if not question_blocks:
        print("Error: No questions found in raw_quiz.txt. Maybe check the format.")

    # loop trhough each block and parse it
    for i, block in enumerate(question_blocks, 1):

        # finding question text
        question_text = block.split("\n\n")[1].strip()

        # finding answer options
        options = re.findall(r"^[A-D]\. (.*)", block, re.MULTILINE)

        # finding correct answer
        correct_letter = re.search(r"Correct Answer: ([A-D])", block).group(1)

        # getting correct answer text
        correct_index  = letter_to_index[correct_letter]
        correct_text = options[correct_index]

        # building JSON dictionary
        question_dict = {
            "question": question_text,
            "options": options,
            "correct_answer": correct_text
        }

        # adding question to main list
        new_quiz_data["questions"].append(question_dict)

        print(f"Successfully parsed Question {i}...")

    # write new questions.json file
    with open("questions.json", "w", encoding="utf-8") as f:
        json.dump(new_quiz_data, f, indent=2)

    print(f"\nSuccess! Wrote {len(new_quiz_data['questions'])} questions to new_questions.json")
    print("You can now run your Quiz app")

# writing the exceptions
except FileNotFoundError:   
    print("Error: .txt file was not found.")

except Exception as e:
    print(f"An error occured {e}")
    print("Please check the format of your .txt file")