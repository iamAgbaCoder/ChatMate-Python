
```markdown
# Train Your ChatBot Project

## Overview

This project is a simple yet effective chatbot designed to interact with users through text-based queries. It utilizes a JSON file to store questions and answers, allowing for dynamic learning and adaptation based on user interactions. The chatbot is capable of finding the best match for user queries among stored questions and providing answers accordingly. Additionally, it has the ability to learn new responses from users, enhancing its knowledge base over time.

## Getting Started

### Prerequisites

- Python 3.x
- A JSON file named `data.json` in the project directory with the following structure:

```json
{
  "questions": [
    {
      "question": "What is the capital of France?",
      "answer": "Paris"
    },
    {
      "question": "Who wrote Hamlet?",
      "answer": "William Shakespeare"
    }
  ]
}
```

### Installation

No installation is required. Simply clone the repository and ensure you have Python installed.

### Running the Bot

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the script using Python:

```bash
python chatbot.py
```

4. Interact with the bot by typing your queries. Use "quit" to exit the chat.

## Usage

- Type your query in the chat interface.
- The bot will attempt to find the best match for your query from the stored questions.
- If a match is found, the bot will provide the corresponding answer.
- If no match is found, the bot will ask if you can teach it a new response.
- To teach the bot a new response, type the answer or "skip" to continue without adding a new question-answer pair.

## Contributing

Contributions to this project are welcome. Please feel free to submit pull requests or report issues.

## Contact

For any questions or feedback, please reach out via email at demiladebamgboye@gmail.com.

## License

This project is licensed under the MIT License - see the LICENSE file for details.