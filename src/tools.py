def calculator(expression: str) -> str:
    try:
        allowed_chars = "0123456789+-*/(). "
        if not all(char in allowed_chars for char in expression):
            return "Invalid calculation input."
        return str(eval(expression))
    except Exception:
        return "Calculation error."


def read_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."


def keyword_search(text: str, keyword: str) -> list[str]:
    results = []
    for line in text.splitlines():
        if keyword.lower() in line.lower():
            results.append(line)
    return results
