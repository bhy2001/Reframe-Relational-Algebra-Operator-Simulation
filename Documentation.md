# CS-440 FINAL PROJECT

- This project attempts to reimplement reframe's API and extend it to include more relational algebra operations using Python. Operations include:
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
