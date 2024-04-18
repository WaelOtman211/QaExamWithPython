
# Production QA Exam - Loan Offer Processing System

##  Part1 :Python Programming Tasks

Welcome to the repository for Python scripts designed to manipulate words in various ways.

## Prerequisites

Ensure that Python 3.x is installed on your local system.

## Getting Started

1. Clone this repository to your local machine:

    
    git clone https://github.com/WaelOtman211/QaExamWithPython.git
    

2. Navigate to the cloned directory:

    
    cd QaExamWithPython
    

## Usage

Run the script using Python:

    
    python EX1_EX2.py
    
Feel free to modify the input strings or parameters directly within the script file.

## Description

- EX1_EX2.py: This script contains two examples:
    - *Example 1*: Retrieves words longer than a specified length from a string.
    - *Example 2*: Checks for palindromes in a list of strings.



## Part 2: Loan Offer Processing System Overview
Answers to the question are provided in the attached PDF file named Production QA 

### Application

An application is the initial step, where details about the applicant are gathered. This includes fetching CreditFeatures from a credit bureau API and specifying the requested amount.

### Offer Generation

Upon receiving an application, the system generates three initial offers based on the requested amount. 

### Models

The system employs two main models: the Rate_model and the Risk_model. The Rate_model calculates a rate model score based on the applicant's credit features and offer attributes, while the Risk_model assesses the risk associated with the applicant.

### Risk Modification

Risk modification adjusts interest rates based on the risk model score, ensuring that appropriate risk assessment is factored into the final rates.

### Pricing Table and Final Decision

A pricing table determines the final rate offered to applicants based on score buckets. Offers meeting both the rate and loan restriction criteria are approved, while others are declined.

