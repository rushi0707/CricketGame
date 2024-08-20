Cricket Scoring System Project Description
Project Title: Cricket Scoring System

Project Overview:
The Cricket Scoring System is a console-based application designed to manage and track the progress of a cricket match. It facilitates the input of match details, including team names, player information, runs, overs, wickets, and extras. The system provides real-time updates on the match status and calculates the total score, managing player status and scoring dynamically throughout the game.

Key Features:

Team Management:

Initialize Team: Set up team names and player information. Each team can have up to 11 players.
Player Details: Input player names and manage player-specific data such as runs, wickets, and balls faced.
Match Management:

Overs: Specify the total number of overs for the match.
Batsmen Management: Designate opening batsmen and handle player changes (e.g., due to wickets or substitutions).
Scoring:

Run Scoring: Add runs for each ball played. Handle special cases such as extras (wides, no-balls).
Wickets: Track the number of wickets fallen and update player statuses when out.
Extras: Add extra runs due to no-balls, wides, or other reasons.
Match Progress:

Overs and Balls: Track the number of overs and balls played. Update and display over and ball counts.
Score Display: Show the current score, runs per player, and the overall team score.
Innings Management: Automatically handle innings transitions, such as switching batsmen at the end of an over or when a wicket falls.
User Interaction:

Menu Options: Provide options to handle different match events (dot ball, add run, extra run, wicket, etc.).
Dynamic Updates: Continuously update the match status and display current information to the user.
Technical Details:

Programming Language: Python
Data Structures:
Arrays/lists to store player information, runs, statuses, and balls.
Dictionaries for status mapping (e.g., "not out", "bold out", etc.).
User Interface: Console-based, with user inputs for various match events and settings.
Class Design:
Team Class: Manages team data, player information, and scoring functions.
Score Class: Inherits from Team and handles match-specific logic, including overs, wickets, and player status.
Usage:
Run the application, and follow the prompts to initialize the teams, input player details, and manage the match as it progresses. The system will guide the user through scoring events and automatically update the match statistics.

Potential Enhancements:

Graphical User Interface (GUI): Develop a GUI for a more user-friendly experience.
Database Integration: Store match and player data persistently using a database.
Advanced Scoring Rules: Implement additional cricket scoring rules and features.
This project demonstrates fundamental programming skills in Python, including object-oriented design, user interaction, and data management. It provides a practical example of how to model and manage a real-world system using software.
