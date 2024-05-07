import json
from difflib import get_close_matches



# load data => contains responses
def load_data(file_path: str) -> dict:

    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data



def save_data(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)




def find_best_match(user_query: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_query, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None




def get_answer_for_question(query: str, data: dict) -> str :
    for q in data["questions"]:
        if q["question"] == query:
            return q["answer"]




def chat_bot():

    db: dict = load_data("data.json")

    while True:

        user_query: str = input("You: ")

        if user_query.lower() == "quit":
            break

        best_match: str = find_best_match(user_query, [q["question"] for q in db["questions"]])
        if best_match:
            answer: str = get_answer_for_question(best_match, db)
            print(f"Bot: {answer}")
        else:

            print("Bot: I don't know the answer. Can you teach me?")

            new_answer: str = input("Type the answer or 'skip' to skip: ")


            if new_answer.lower() != "skip":

                db["questions"].append({"question": user_query, "answer": new_answer})

                save_data("data.json", db)

                print("Bot: Thank you, I learned a new response")




if __name__ == "__main__":

    chat_bot()