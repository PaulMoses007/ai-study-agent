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


## Step 3 – 15.05.2026

### Testing Process

Testing was performed continuously during implementation.

The testing process included:

- manual functional testing,
- automated testing using pytest,
- validation testing,
- error handling verification.

The goal of testing was to verify that all tools and the agent workflow operate correctly.

### Test Scenarios

The following test scenarios were implemented:

1. Calculator tool test  
Input: "2 + 2"  
Expected Result: "4"

2. Invalid calculation test  
Input: "abc"  
Expected Result: invalid calculation message

3. Keyword search test  
Input keyword: "Python"  
Expected Result: matching text line returned

4. Empty input validation test  
Input: empty string  
Expected Result: validation warning message

5. Agent calculation workflow test  
Input: "calculate: 10 + 5"  
Expected Result: calculation result returned

6. Unknown question test  
Input: "banana"  
Expected Result: no relevant information message

### Deployment Preparation

The project was prepared as a local command-line Python application.

Deployment preparation includes:

- requirements.txt for dependencies,
- startup instructions in README,
- modular project structure,
- clear execution instructions using python -m src.main.

### Data Conversion and Porting

The system reads data from local text files.

The file reader converts file contents into text strings.

The keyword search tool processes the text line-by-line while preserving consistency and correctness.

Data is passed between components using standard Python string and list structures.

### Current Progress

The project now includes functional implementation, modular architecture, automated testing, deployment preparation, and documented workflows.

## Final Submission – 22.05.2026

### Final System Description and Goal

The final system is an AI-assisted Study Agent developed in Python. The purpose of the system is to help students obtain information from study materials and perform simple calculations through an agent-based workflow.

The system receives user input, determines the required action, selects an appropriate tool, processes the request, and returns a meaningful response. The project demonstrates how an intelligent software component can coordinate multiple tools to solve practical tasks.

### Final Programming Concepts and Their Usage

The project uses several programming concepts:

- Classes and objects: used to implement the StudyAgent component.
- Functions: used to implement reusable tool functionality.
- Modules and packages: used to separate the project into logical components.
- File handling: used to read study notes from local text files.
- Conditional statements: used for decision-making inside the agent workflow.
- String processing: used to analyse and process user requests.
- Lists: used to store and return search results.
- Error handling: used to manage invalid calculations safely.
- Input validation: used to verify user requests before processing.
- Automated testing: implemented using pytest to verify correctness.
- Git and GitHub: used for version control and project management.

### Final Tools and Their Role

The system integrates several tools:

1. Calculator Tool
   - Performs mathematical calculations.
   - Used when the user requests arithmetic operations.

2. File Reader Tool
   - Reads study notes stored in local text files.
   - Provides information for further processing.

3. Keyword Search Tool
   - Searches study notes for relevant information.
   - Returns matching content to the user.

4. Validation Utility
   - Checks whether user input is valid.
   - Prevents invalid requests from being processed.

The agent coordinates all tools and determines which tool should be used based on the user request.

### Final Testing Results and Conclusions

Testing was performed throughout development using both manual and automated methods.

Implemented test scenarios:

- Calculator operation test
- Invalid calculation test
- Keyword search test
- Empty input validation test
- Agent calculation workflow test
- Unknown question handling test

Automated testing was implemented using pytest.

Final testing results:

- Total tests executed: 6
- Tests passed: 6
- Tests failed: 0

The testing process confirmed that the system behaves correctly under both normal and invalid input conditions.

### Final Deployment Preparation Description

The project is prepared for deployment as a local command-line application.

Deployment requirements:

1. Python 3 installed.
2. Dependencies installed using:

   pip install -r requirements.txt

3. Application execution:

   python -m src.main

The repository includes:

- source code,
- automated tests,
- project documentation,
- requirements.txt,
- startup instructions.

### Deployment Strategy

The selected deployment strategy is a local command-line application.

This strategy is suitable because the system is lightweight, easy to install, and simple to test. Future versions could be deployed as:

- a web application,
- an API service,
- a cloud-hosted study assistant.

A staged deployment approach would be recommended, where testing is completed before releasing the application to end users.
