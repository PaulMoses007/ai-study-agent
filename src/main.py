from agent import StudyAgent


def main():
    agent = StudyAgent()

    print("AI Study Agent")
    print("Type a keyword or use calculate: 2 + 2")
    print("Type exit to quit.")

    while True:
        user_input = input("\nEnter your question: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = agent.answer(user_input)
        print(response)


if __name__ == "__main__":
    main()
