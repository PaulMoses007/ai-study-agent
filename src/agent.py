from tools import calculator, read_file, keyword_search


class StudyAgent:
    def answer(self, user_input: str) -> str:
        if not user_input.strip():
            return "Please enter a valid question."

        if user_input.startswith("calculate:"):
            expression = user_input.replace("calculate:", "").strip()
            result = calculator(expression)
            return f"Calculation result: {result}"

        notes = read_file("data/sample_notes.txt")
        results = keyword_search(notes, user_input)

        if results:
            return "Relevant information found:\n" + "\n".join(results)

        return "No relevant information was found in the study notes."
