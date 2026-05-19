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


## Step 2 – 08.05.2026

### Updated System Description

The AI Study Agent has been improved into a more structured Python application with integrated testing and validation support.

The system now includes:

- agent-based decision logic,
- multiple integrated tools,
- automated testing,
- modular project structure,
- improved input validation.

The system can process user requests, perform calculations, search study notes, and return structured responses.

### Programming Concepts Used

The following programming concepts are currently used:

- Python classes and objects
- Functions
- Modules and packages
- File handling
- Conditional statements
- String processing
- Lists
- Error handling
- Automated testing using pytest
- Input validation
- Git version control

### Application of Programming Concepts

Classes are used to implement the StudyAgent component.

Functions are used to implement tools such as the calculator and keyword search functionality.

Modules separate the project into reusable components including tools, utilities, agent logic, and tests.

File handling is used to load local study notes from text files.

Conditional logic allows the agent to decide which tool should be used depending on the user request.

Error handling prevents system crashes during invalid calculations.

Automated testing verifies the correctness of both tools and agent workflows.

### Tool Integration

The system integrates several tools into the agent workflow.

The calculator tool is used for mathematical operations.

The file reader tool loads information from local files.

The keyword search tool searches relevant information from study notes.

The validation utility checks whether user input is valid before processing.

The agent coordinates all tools and determines which operation should be executed.

### Current Progress

The project now includes functional implementation, modular structure, automated tests, and validation support. The next phase will focus on deployment preparation and additional testing scenarios.
