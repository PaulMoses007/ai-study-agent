# Development Journal

## Step 1 – 24.04.2026

### Planned System and Goal

The planned system is an AI-assisted study agent written in Python. The goal of the system is to help a student answer study-related questions by using external tools during execution.

The system receives user input, analyses the request, chooses a suitable tool, uses the tool, and returns a meaningful answer.

### AI or Agent-Based Approach

The system uses a single-agent workflow. The agent receives a question from the user and decides what action should be performed.

The workflow is:

1. Receive user input.
2. Validate the input.
3. Decide whether the user needs calculation or information search.
4. Use the selected tool.
5. Return the result to the user.

### Tools Planned for the System

The system will use these tools:

- Calculator tool for mathematical expressions.
- File reader tool for reading local study notes.
- Keyword search tool for finding relevant information inside notes.
- Input validation logic for checking empty input.

### Preliminary Programming Concepts Required

The project will require:

- Python functions
- Python classes
- Modules
- File handling
- String processing
- Lists
- Conditional statements
- Error handling
- User input and output
- Unit testing
- Git version control
- GitHub repository management

### Current Progress

The project idea has been selected. The initial folder structure has been created. Basic tools and a simple agent workflow have been planned and partially implemented. The next step is to improve the agent logic and add automated tests.
