# Project 1: Singly Linked List README
## Overview
Project 1 for CSE 331 F23 is a comprehensive implementation of a Singly Linked List (SLL) and its various operations. This project provides a detailed understanding of linked list data structures and their application in a real-world scenario, specifically in creating and managing a racing game roster.

## Features
SLLNode: A class representing a node in a singly linked list.<br />
SinglyLinkedList (SLL): The main class implementing the singly linked list, with operations for appending nodes, converting to and from strings, calculating the length, summing node values, deleting nodes, and searching for data.<br />
Roster Management in Racing Game: An application scenario where the SLL is used to manage a roster of racers, specifically to help Mario by moving his ally to the front of the list.<br />
## Usage
SLL Operations:<br />
append: Add a new node to the end of the list.<br />
to_string: Convert the SLL to a string representation.<br />
length: Return the number of nodes in the list.<br />
total: Calculate the sum of values in the list.<br />
delete / delete_all: Remove nodes with a specific value.<br />
find: Check if a value exists in the list.<br />
find_sum: Count occurrences of a specific value in the list.<br />
Racing Game Roster Management (help_mario):<br />
This function adjusts the roster (SLL) to move Mario's ally to the front, ensuring the ally gets a strategic advantage.<br />

## Installation
No special installation is required beyond Python 3.7 or newer.

## Dependencies
Python 3.7+

## Author
Dallas Foley
