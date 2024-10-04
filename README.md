
# Magic Boxes Simulation

## Problem Description

Alice possesses **42 magic boxes** with infinite capacity. However, each box can only hold one type of object at any given time. Once a specific object type is added to a box, only objects of the same type can be stored. If the box is emptied, it can then store a new type of object.

### Objective

Bob provides Alice with objects, which she must store in the boxes, while Carl asks Alice for specific objects. Your task is to simulate Alice's interaction with the boxes, storing objects given by Bob and retrieving objects requested by Carl, while adhering to the rules of the magic boxes.

### Constraints

1. **Storage Rules:**
   - Once a type of object is stored in a box, only that type can be added until the box is emptied.
   - After emptying a box, a new type of object can be stored in it.
   
2. **Action Types:**
   - `Bob gives a OBJECT` - Bob gives Alice a specific object to store.
   - `Carl takes a OBJECT` - Carl requests an object from Alice.

3. **Error Handling:**
   - If Alice cannot store the object given by Bob due to incompatible types in the available boxes, the program should return an error message.
   - If Carl requests an object that is not available, the program should return an error message.

### Example Scenarios

Consider the following cases:

1. **Bob gives a APPLE**  
   **Bob gives a BANANA**  
   **Bob gives a APPLE**  
   **Bob gives a CHERRY**  

   Result: Error, since Alice cannot store the CHERRY in any available box.

2. **Bob gives a APPLE**  
   **Bob gives a BANANA**  
   **Bob gives a APPLE**  
   **Carl takes a CHERRY**  
   **Bob gives a CHERRY**  

   Result: Error, as Alice cannot give Carl a CHERRY since no such object is stored.

3. **Bob gives a APPLE**  
   **Bob gives a BANANA**  
   **Bob gives a APPLE**  
   **Carl takes a BANANA**  
   **Bob gives a CHERRY**  

   Result: No errors, as the box with the BANANA is emptied and can now store the CHERRY.

## Solution

The solution simulates Alice's handling of objects with the following steps:

1. **Input:** A text file named `actions.txt` containing a sequence of actions performed by Bob and Carl.
2. **Simulation:** 
   - If Bob gives an object, it checks for an available or new box to store the object.
   - If Carl takes an object, it checks if the object is available in any of the boxes.
   - If a rule violation occurs (e.g., attempting to store an incompatible object or retrieving an unavailable object), an appropriate error message is displayed.

### Program Execution

To run the simulation:

1. Ensure the `actions.txt` file exists in the same directory as the program.
2. Run the program, which will read the file and simulate the actions.

### Error Handling

- **Incompatible Storage:** When Alice cannot store Bob's object due to type constraints, the program outputs an error message like:
  - `Error: Cannot store OBJECT in any box.`
  
- **Unavailable Object:** When Carl requests an object that is not available, the program outputs an error message like:
  - `Error: Cannot give Carl the OBJECT as it is not available.`

## Example Input (`actions.txt`)

```
Bob gives a APPLE
Bob gives a BANANA
Carl takes a BANANA
Bob gives a CHERRY
```

## Example Output

```
Stored APPLE in box 1.
Stored BANANA in box 2.
Carl takes BANANA from box 2.
Stored CHERRY in box 2.
```

## Author

Solution created as part of a Python project to simulate object storage and retrieval in constrained environments.
