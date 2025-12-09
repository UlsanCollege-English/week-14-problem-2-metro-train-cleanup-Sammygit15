[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/j7mjNw0c)
# HW02 — Metro Train Cleanup (Linked List Filter)

## Story

You are working on software for a big city's metro system. Each train is represented as a **linked list** of cars. Some cars are marked as "out of service" and must be removed from the train before it can leave the depot.

Your job: given the head of a singly linked list of car IDs and a target ID, remove **all** cars with that ID from the train.

---

## Technical Description

You will implement a simple singly linked list node and a function:

```python
class Node
remove_cars(head, target) -> Node or None
```

### Node Structure

In `main.py`, you must use this constructor signature:

```python
Node(value, next=None)
```

Each node has:

- `value`: the car ID (an integer)
- `next`: the next `Node` or `None`

### Inputs

- `head`: the head `Node` of a singly linked list, or `None` for an empty train
- `target`: an integer car ID to remove

### Outputs

- Return the **new head** of the list, with **all nodes whose value == target removed**
- If all cars are removed, return `None`

### Constraints

- You must **modify the list in place** (no new list of nodes; changing pointers is okay)
- Time complexity: **O(N)** where N is the number of nodes
- Extra space: **O(1)** (do not create new nodes to copy the entire list)

---

## 8 Steps of Coding (ESL Scaffold)

1. **Read and understand the problem**
   - What does the list represent? What does "remove" mean here?

2. **Re-phrase the problem**
   - In your own words: what do we do to the linked list? What do we return?

3. **Identify input, output, variables**
   - Input: `head` (Node or None), `target` (int)
   - Output: new `head` after removals
   - Variables:
     - A pointer for the new head
     - A pointer for the current node
     - Maybe a pointer for the previous node

4. **Break down the problem**
   - How will you handle:
     - Cars that should be removed at the **front** of the list?
     - Cars that should be removed in the **middle**?
     - Cars at the **end**?
   - When do you move `prev` vs `current`?

5. **Pseudocode the solution**
   - Use English + indentation to plan your pointer movements
   - Include while loops and if-statements clearly

6. **Write the actual code (hint)**
   - Translate your pseudocode carefully
   - Update pointers instead of reallocating the whole list

7. **Debug (hint)**
   - Walk through a small list on paper:
     - Example: `3 -> 5 -> 5 -> 7`, target = 5
   - Check result after each pointer move

8. **Optimize (hint)**
   - Confirm you are only walking the list **once** (O(N)) and using only a few extra variables

---

## Hints

1. It is often easier to **first remove matching nodes at the head** in a loop, and then process the rest of the list
2. After the head is cleaned, you can use a `prev` pointer and a `current` pointer; adjust `prev.next` when removing
3. Remember that `head` can be `None` (empty train), and all cars might be removed

---

## How to Run Tests Locally

From the project root (where `hw02/` lives), run:

```bash
python -m pytest -q
```

Pytest will discover `hw02/tests/test_hw02.py` and run the test suite.

---

## FAQ

**Q1: Do I have to write the Node class?**

Yes. Use the constructor `__init__(self, value, next=None)` as shown in `main.py`. The tests will import `Node` from `main.py`.

**Q2: What about `__repr__` or `__eq__`?**

You do not need to override them. The tests will convert lists of nodes to Python lists using `value`.

**Q3: What Big-O is required?**

- Time: O(N) — one pass over the list
- Space: O(1) — no full copy of the list

**Q4: What happens if `head` is `None`?**

Just return `None`. There is no train.

**Q5: What if the target does not appear at all?**

Return the original list (same nodes, same head).

**Q6: The tests failed — how do I read the error?**

Look at:

- The input case that failed (shown in the test output)
- The expected result vs your result

Rebuild that exact case in a small script and print the list step by step.

**Q7: Can I use Python lists instead of linked lists internally?**

No. The goal is to practice linked list pointer manipulation. You must use the `Node` structure and adjust `next` pointers in place.