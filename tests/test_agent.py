from src.agent import StudyAgent


agent = StudyAgent()


def test_empty_input():
    assert agent.answer("") == "Please enter a valid question."


def test_calculation():
    assert "15" in agent.answer("calculate: 10 + 5")


def test_unknown_question():
    assert "No relevant information" in agent.answer("banana")
