# AI Study Agent

## Project Description

AI Study Agent is a Python-based agent system that helps students answer study-related questions. The system receives user input, decides which tool should be used, calls the tool, and returns a structured result.

## Goal

The goal of this project is to demonstrate an AI-assisted or agent-based software solution that uses external tools during execution.

## Tools Used

- Calculator tool
- File reader tool
- Keyword search tool

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the program:

python src/main.py

Example inputs:

agent  
calculate: 2 + 2  
testing  

## Current Status

Step 1 completed: system designed, implemented, and tested.

## Testing

Run automated tests:

pytest

Run the application:

python -m src.main

## Deployment Preparation

This project is prepared as a local command-line Python application.

Deployment steps:

1. Install Python 3
2. Install dependencies using:
   pip install -r requirements.txt
3. Run the application:
   python -m src.main

## Data Handling and Conversion

The system reads study notes from a local text file.

The file reader tool converts the file contents into plain text strings.

The keyword search tool processes the text line-by-line and returns matching results while preserving data consistency.

## Deployment Strategy

The current deployment strategy is a local command-line application.

In future development, the system could also be deployed as:

- a web application,
- an API-based assistant,
- a cloud-hosted study assistant service.
