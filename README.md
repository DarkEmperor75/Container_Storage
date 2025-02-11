# Optimizing Container Storage Simulation

This repository contains simulation and analysis code for optimizing container storage at rail-truck transshipment terminals. The simulation models container arrival, storage allocation, and the loading process for double-stack container trains, and is designed to validate and analyze the efficiency of the proposed procedure.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation and Dependencies](#installation-and-dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

This project focuses on a simulation-based approach to improve container terminal operations by:
- **Simulating Container Arrival:** Modeling unpredictable container arrival sequences.
- **Storage Allocation:** Arranging containers for efficient retrieval based on weight and arrival sequence.
- **Efficient Loading:** Implementing a procedure that satisfies all safety and operational constraints for loading double-stack container trains.

The simulation code is written in Python and is designed to be lightweight and easy to modify for further research or operational testing.

---

## Project Structure

```plaintext
src/
└── simulation.py      # Main simulation and analysis code

Installation and Dependencies
Requirements
Python 3.x
Python Libraries
Install the following libraries using pip:
pip install numpy matplotlib
Usage
Clone the Repository:

bash
Copy
git clone <repository_url>
cd <repository_directory>
Run the Simulation:

Navigate to the src directory and run the simulation:

bash
Copy
cd src
python simulation.py
The script will execute the simulation for container storage and loading procedures, and display or output the analysis results.

Contributing
Contributions are welcome! If you'd like to suggest improvements or add new features:

Fork the repository.
Create a feature branch.
Commit your changes and open a pull request.
