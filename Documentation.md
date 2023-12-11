# CS-440 FINAL PROJECT

- This project attempts to reimplement reframe's API and extend it to include more relational algebra operations using Python. Operations include:
  - This package only accept in read `.csv` file type
  - Single-table operations:

    - **Project**:
      - Parameters: cols → List of strings representing the columns to be included in the projection.
      - Purpose: Create a new relation by selecting specific columns from the existing relation.
      - Output: A new relation with specific columns
    - **Rename**:
      - Parameters: old, new → Representation of the old column name and new column name that will be used to rename the old column name.
      - Purpose: Rename a column in the relation to have a better meaningful column representation.
      - Output: The relation with the new name specified for the column to be renamed.
    - **Extend**:
      - Parameters: name(new head col), operand0=None(data: List), operand1=None(data: List), operator=None("+", "-", "/", "\*")
      - Purpose: Extend a column in the relation to have better meaningful column representation
      - Output: The relation with the new column with data or empty depend on input parameters
    - **Select**:
      - Parameters: operand1, operator, operand2
      - Purpose: to somewhat imitate relational algebra’s “query” operations. It attempts to filter out unwanted results from a table
      - Output: a filtered relation
    - **Sort**:
      - Parameters: cols: List (column name), order (ascending or not)
      - Purpose: Sort by given columns in the relation by request order.
      - Output: The relation with sorted data by request.
    - **Groupby**:
      - Parameters: cols, operator (default is None)
      - Purpose: attempts to group the table by the column cols, followed by an optional operation (like sum or count).
      - Output: a new relation, with data grouped by the column cols and the result of the additional operation (if any).

  - Multi-table operations:
  
    - **Product**:
      - Parameters: other relations/ other table.
      - Purpose: (Table1 ✕ Table2) data1 multiply data 2A ✕ S
      - Output: combine data of table 1 and table 2
    - **Semijoin**:
      - Parameter: other(Relation(csvTable)), condition(two of similar column head (table 1 and table 2))
      - Purpose: retrieves those tuples in R that join with some tuple in S
      - Output: Relation of semijoin result
    - **Join**:
      - Parameters: other → other relation, condition → tuple specifying the columns to be joined
      - Purpose: Join between two relation based on a specific condition
      - Output: a new relation with combined rows from both relations.
    - **Union**:
      - Parameters: other → other relation
      - Purpose: Combines by the rows, both relations are required to have the same set of columns
      - Output: a new relation with combined rows from both relations into a single realtion.
    - **Outerjoin**:
      - Parameters: other, condition
      - Purpose: Performs outerjoin on two relations (self and other), on the given condition
      - Output: a new relation, resulting from the outerjoin operation.
    - **Antijoin**:
      - Parameters: other, condition
      - Purpose: Performs antijoin on two relations (self and other), on the given condition
      - Output: a new relation, resulting from the outerjoin operation

## Installation

1.  Clone the repository:

    `git clone git@github.com:sturekev/Final-Project-440.git`

2. Create and Activate(win/ubuntu) an Environment for Python
    ` python3 -m venv venv`
    
    Win:
    `.\venv\Scripts\activate`
    Ubuntu:
    `source .\venv\bin\activate`

3.  Install the required dependencies

    ` pip install -r requirements.txt`

4.  Run the application or use aplication:

    Run: `python3 tinycollege.py`
    Use as package: `from reframe import Relation`


## Contributor:

- Truong Phat(Kevin) Tu - Luther College
- Bach Hy (Bill) Dang - Luther College
- Mateus Rohden - Luther College
