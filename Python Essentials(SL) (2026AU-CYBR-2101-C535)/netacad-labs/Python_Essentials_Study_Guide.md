# Python Essentials: Study Guide & Writing Rules

Prepared for James T. Jordon | Hocking College

Python Essentials (S1) | 2026AU-CYBR-2101-C535

Companion to Cengage textbook study, Cisco Networking Academy Python courses, and your end-of-semester PCEP goal.

Prepared October 29, 2026. Uses established Python 3 features; references are pinned to Python 3.14 where practical. Examples are validated with Python 3.12.14. This is a foundation-to-PCEP guide with selected next steps, not an encyclopedia of every Python library.

## 01. How to use this guide

**Start where you are:** You have practiced `print()` in NetAcad Lab 2.1.5. Begin with Sections 02-06, then move into decisions, loops, collections, and functions. Cengage chapter numbers are intentionally omitted because your textbook title and edition have not been supplied.

### A study cycle that produces evidence

1. Read one topic in your assigned textbook or NetAcad lesson.
2. Predict what a short example will do before running it.
3. Type the example yourself. Change one value or operator.
4. Explain why the output changed, using the variable values.
5. Write a small program from a blank file.
6. Save your code, sample output, and a brief reflection in your portfolio.

### The four PCEP study areas

| Area | Work to practice |
| --- | --- |
| Fundamentals | Syntax, literals, operators, conversions, input/output |
| Control flow | Conditions, loops, nesting, break/continue, loop else |
| Collections | Strings, lists, tuples, dictionaries, slicing and copying |
| Functions and exceptions | Arguments, scope, returns, recursion, generators, error handling |

**Exam version:** On October 29, 2026, the Python Institute lists PCEP-30-02 as active and PCEP-30-03 as scheduled for October 31, 2026. This guide uses the published PCEP-30-02 topic outline. Check the syllabus for your booked version before testing. It is a study aid, not an official practice exam or certification guarantee. [16, 17]

### Read the examples correctly

Python code appears in code blocks. Comments after `#` explain a line or its expected result. A block labeled **Output** shows what you should see; do not paste output into your program. Shell commands run in your terminal, not inside a `.py` file.

**Your goal:** Be able to write, trace, explain, and repair a small program. Recognition alone is not the same as being able to build it.

## 02. Get a program running

### Three different places you may type

| Place | Purpose | Example |
| --- | --- | --- |
| Code editor | Save source code in a `.py` file | `print("Ready")` |
| Python interactive prompt | Try Python expressions immediately | `2 + 5` |
| Operating-system terminal | Launch Python and scripts | `python lab_02_01_05.py` |

Create a file named `lab_02_01_05.py` and save this code:

```python
print("Python Essentials")
print("James", "Lab 2.1.5", sep=" | ")
```

From the terminal in that file's folder:

```shell
python --version
python lab_02_01_05.py
```

If your system uses the Windows launcher, try `py --version` and `py lab_02_01_05.py`. On some systems, use `python3`. Use whichever command launches the Python installation required by your course.

### Know these terms

- **Source code:** The instructions you write as text.
- **Interpreter:** The program that executes Python code. CPython normally compiles source to bytecode internally before executing it; "interpreted" does not mean compilation never occurs.
- **Syntax:** The grammatical form of legal code.
- **Semantics:** What that code means and does.
- **Algorithm:** A sequence of steps for solving a problem.
- **Expression:** Code that produces a value, such as `3 * 4`.
- **Statement:** An instruction, such as an assignment or `return`.

**Common trap:** `>>>` is the interactive prompt shown in documentation. Do not copy it into a script. In a script, a bare expression such as `2 + 5` is not automatically printed.

References: [2, 12].

## 03. Required syntax versus readable style

Some rules determine whether Python can run your code. Others are conventions that help people read it. Use both, but understand the difference.

| Python requires | Readable-code convention |
| --- | --- |
| Consistent indentation defines blocks | Use four spaces per indentation level |
| Block headers such as `if` and `def` end with `:` | Put a block's statements on separate lines |
| Names are case-sensitive | Use `snake_case` for variables and functions |
| A name cannot begin with a digit | Choose descriptive names such as `attempt_count` |
| Reserved keywords cannot be ordinary variable names | Avoid hiding built-ins such as `list` or `print` |
| Strings need matching quote delimiters | Use one consistent quote style where practical |
| Parentheses/brackets/braces must balance | Wrap long expressions inside parentheses |

```python
attempt_count = 2
max_attempts = 3

if attempt_count < max_attempts:
    print("Another attempt is available.")
    attempt_count += 1

print("Check complete.")
```

The two indented lines belong to the `if`. The last line is outside it. Indentation changes behavior; it is not merely decoration.

### PEP 8 habits to adopt

- Spaces around assignment and most binary operators: `total = price * quantity`.
- A space after a comma: `print(name, score)`.
- No unnecessary spaces inside parentheses: `len(items)`.
- No spaces around a simple keyword argument: `print("A", end="!")`.
- Constants use `UPPER_SNAKE_CASE`; class names use `CapWords`.
- PEP 8 recommends 79 characters for code lines and 72 for flowing comments/docstrings. Follow your course or project's established limit.
- Separate top-level functions with two blank lines. Put imports near the top.

**Avoid:** tabs mixed with spaces, unnecessary semicolons, vague names, and long one-line programs. Python permits many things that are poor teaching or maintenance choices. [3, 4]

## 04. Names, values, and data types

Assignment binds a name to an object. `=` assigns; it does not ask whether two values are equal. Python objects have types; a name can later refer to a different object.

```python
lab_number = 5             # int: a whole number
completion_rate = 0.75    # float: an approximate real value
student_name = "James"   # str: text
is_complete = False      # bool: True or False
result = None            # no result available yet

print(type(lab_number).__name__)  # int
lab_number = "2.1.5"      # legal, but now refers to text
```

| Type | Example | Typical use |
| --- | --- | --- |
| `int` | `42`, `-7`, `1_000` | Counts and whole-number calculations |
| `float` | `3.5`, `2e3` | Measurements and fractional values |
| `bool` | `True`, `False` | Conditions and flags |
| `str` | `"lab complete"` | Text |
| `list` | `[22, 80, 443]` | An ordered, editable collection |
| `tuple` | `("host-a", 443)` | An ordered, fixed collection |
| `dict` | `{"host": "lab-pc"}` | Key/value lookup |
| `set` | `{"INFO", "WARN"}` | Unique members and set operations |
| `NoneType` | `None` | An absent or unavailable value |

### Naming rules and common confusion

For simple ASCII names, use letters, digits, and underscores, starting with a letter or underscore. Python also supports many Unicode letters. `user_name` is valid; `2users` and `user-name` are not valid single identifiers. `Score` and `score` are different names.

`"False"` is text; `False` is a Boolean. `"42"` is text; `42` is an integer. `None` is not the string `"None"` or the number zero.

**Check yourself:** Before a calculation, identify each value's type. Many beginner errors are really "text versus number" errors. [4, 5]

## 05. Master print(): your Lab 2.1.5 foundation

`print()` displays values. Multiple positional arguments are separated by a space by default; output normally ends with a newline. It returns `None`. [1]

```python
print("Python", "Essentials")
print("Lab", "2.1.5", sep=" - ")
print("Loading", end="...")
print("done")
print()  # a blank line
```

**Output:**

```text
Python Essentials
Lab - 2.1.5
Loading...done

```

### Know the controls

| Argument | What it controls | Example |
| --- | --- | --- |
| `sep` | Text between multiple values | `sep=" \| "` |
| `end` | Text after the last value | `end="!\n"` |
| `file` | Destination text stream | `file=report` for an open text file |
| `flush` | Whether buffered output is flushed immediately | `flush=True` |

`sep` does not insert characters inside one string. Compare `print("AB", sep="-")`, which prints `AB`, with `print("A", "B", sep="-")`, which prints `A-B`.

### Escapes and formatted strings

```python
print("First line\nSecond line")
print("Name\tScore")
print("She said, \"Keep practicing.\"")
print("C:\\Labs\\Python")

student = "James"
score = 92.5
print(f"{student}: {score:.1f}%")  # James: 92.5%
```

`\n` means newline, `\t` means tab, and `\\` represents one literal backslash. An `f` prefix allows expressions inside braces. `.1f` formats one digit after the decimal point. A raw string such as `r"C:\Labs\Python"` preserves backslashes, but cannot end with an odd number of backslashes. [4, 11]

**Practice:** Print three course topics separated by ` / `, and finish the line with `!` followed by a newline.

## 06. Input and conversion

`input()` returns a string. A numeric-looking response still needs conversion before arithmetic. Treat data entry and calculation as separate steps.

```python
name = input("Name: ").strip()
raw_count = input("Completed labs: ")
completed = int(raw_count)

print(f"{name}, after one more lab you will have {completed + 1}.")
```

With inputs `James` and `4`, the final line is:

```text
James, after one more lab you will have 5.
```

| Expression | Result or behavior |
| --- | --- |
| `int("12")` | Integer `12` |
| `float("12.5")` | Float `12.5` |
| `str(12)` | String `"12"` |
| `int(12.9)` | `12`; truncates toward zero |
| `int(-12.9)` | `-12`; does not round down |
| `int("12.9")` | Raises `ValueError` |
| `bool("")` | `False` |
| `bool("False")` | `True`; the string is nonempty |

### Validate what the number means

```python
try:
    completed = int(input("Completed labs: "))
    if completed < 0:
        print("Enter zero or a positive count.")
    else:
        print(f"Recorded: {completed}")
except ValueError:
    print("Enter a whole number, such as 4.")
```

Successful conversion only tells you the format was acceptable. A negative lab count is still unsuitable for this task. Convert first, then check the allowed range.

**Common trap:** `"4" + "1"` produces `"41"`. `4 + 1` produces `5`. Do not use `eval(input(...))` to convert user input; it can execute code. [1, 5, 10]

## 07. Arithmetic, precedence, and numeric precision

| Operator | Meaning | Example |
| --- | --- | --- |
| `+`, `-`, `*` | Add, subtract, multiply | `6 * 4` gives `24` |
| `/` | True division | `9 / 2` gives `4.5` |
| `//` | Floor division | `9 // 2` gives `4` |
| `%` | Remainder | `9 % 2` gives `1` |
| `**` | Exponentiation | `3 ** 2` gives `9` |
| `+=`, `-=`, `*=` | Augmented assignment | `count += 1` updates `count` |

### Predict these before running them

```python
print(2 + 3 * 4)       # 14
print((2 + 3) * 4)     # 20
print(2 ** 3 ** 2)     # 512: 2 ** (3 ** 2)
print(-3 ** 2)         # -9: -(3 ** 2)
print((-3) ** 2)       # 9
print(2 ** -2)         # 0.25
print(-7 // 3, -7 % 3) # -3 2
```

Floor division rounds toward negative infinity. For nonzero integer `b`, the relationship is `a == (a // b) * b + a % b`. A nonzero remainder has the divisor's sign.

### Common precedence, high to low

Grouping/calls/indexing; exponentiation; unary signs and `~`; multiplication/division/remainder; addition/subtraction; shifts; bitwise `&`, then `^`, then `|`; comparisons/membership/identity; `not`; `and`; `or`. Exponentiation binds unusually with a unary sign on its right, as `2 ** -2` shows. Use parentheses when intent might be unclear. [6]

### Floats are approximate

```python
import math

print(0.1 + 0.2 == 0.3)                 # False
print(math.isclose(0.1 + 0.2, 0.3))     # True
print(round(2.5), round(3.5))           # 2 4
```

Binary floating-point cannot represent every decimal exactly. `round()` uses nearest-even rounding for exact halfway cases; representation can affect apparent decimal ties. For simple money examples, integer cents avoid this issue. `decimal.Decimal` is another option when configured for the task. [13]

## 08. Number systems and bitwise operators

Integer literals can use different bases. The stored value is an integer either way; the notation describes how you wrote it.

```python
print(0b1010, 0o12, 10, 0xA)  # 10 10 10 10
print(bin(10))                # 0b1010
print(oct(10))                # 0o12
print(hex(10))                # 0xa
print(int("1010", 2))        # 10
print(int("0xff", 0))        # 255: infer base from prefix
```

| Operator | Meaning for integers | Example |
| --- | --- | --- |
| `&` | Bitwise AND | `6 & 3` is `2` |
| `\|` | Bitwise OR | `6 \| 3` is `7` |
| `^` | Bitwise exclusive OR | `6 ^ 3` is `5` |
| `~` | Bitwise inversion | `~6` is `-7` |
| `<<` | Shift bits left | `3 << 2` is `12` |
| `>>` | Shift bits right | `12 >> 2` is `3` |

For positive values, compare `6` as binary `110` and `3` as `011`: AND keeps positions where both have a one, giving `010`.

### A flag example

```python
READ = 0b100
WRITE = 0b010
EXECUTE = 0b001

permissions = READ | WRITE
print(bool(permissions & READ))     # True
print(bool(permissions & EXECUTE))  # False
```

This is a small integer flag demonstration, not a complete operating-system permission model. It illustrates how multiple flags can fit into one value.

**Two traps:** `^` means XOR, not exponentiation. `and`/`or` use truth values and short-circuit evaluation; `&`/`|` operate on bits for integers and are not interchangeable with them. Python integers do not have a fixed-width overflow at 8 or 32 bits. For integers, `~x` equals `-x - 1`. [5, 6]

## 09. Conditions, truth values, and comparisons

```python
score = 84

if score >= 90:
    result = "Excellent"
elif score >= 70:
    result = "Keep building"
else:
    result = "Review and retry"

print(result)  # Keep building
```

An `if`/`elif`/`else` chain selects the first matching branch. Separate `if` statements can each run. Choose the structure that matches your decision.

| Expression | Meaning |
| --- | --- |
| `a == b`, `a != b` | Equal or unequal values |
| `a < b`, `a <= b`, `a > b`, `a >= b` | Ordering comparisons |
| `0 <= score <= 100` | Chained comparison |
| `item in items` | Membership |
| `result is None` | Identity comparison with `None` |
| `ready and allowed` | Both truthy |
| `ready or override` | At least one truthy |
| `not ready` | Inverted truth value |

False-like values include `False`, `None`, numeric zero, and empty strings/collections. Nonempty strings such as `"0"` and `"False"` are truthy.

```python
name = ""
display_name = name or "Guest"
print(display_name)  # Guest

values = []
if values and values[0] > 0:
    print("First value is positive.")
```

The second condition does not access `values[0]` when the list is empty. `and` and `or` short-circuit and return an operand, not necessarily a Boolean.

**Avoid:** `if role == "admin" or "teacher":` is always truthy because `"teacher"` is nonempty. Use `if role in ("admin", "teacher"):`. Use `==` for ordinary value equality; `is` asks whether both names refer to the same object. [5, 6]

## 10. Loops, ranges, break, and continue

Use `for` to visit items. Use `while` to repeat while a condition holds. A `range` excludes its stop value.

```python
for lab in range(1, 4):
    print(f"Lab {lab}")  # Lab 1, Lab 2, Lab 3 on separate lines

attempts_left = 3
while attempts_left > 0:
    print(attempts_left)
    attempts_left -= 1
```

| Expression | Values produced |
| --- | --- |
| `range(4)` | `0, 1, 2, 3` |
| `range(2, 5)` | `2, 3, 4` |
| `range(2, 9, 3)` | `2, 5, 8` |
| `range(3, 0, -1)` | `3, 2, 1` |
| `range(3, 0)` | No values |

`range` is an iterable range object, not a prebuilt list. Its step cannot be zero.

### Loop controls

- `break`: Exit the nearest enclosing loop.
- `continue`: Skip the remaining body for this iteration.
- `pass`: Do nothing; useful as a temporary empty body.
- Loop `else`: Run when the loop finishes normally, without `break`.

```python
statuses = ["OK", "SKIP", "FAIL", "OK"]
for status in statuses:
    if status == "SKIP":
        continue
    if status == "FAIL":
        print("Failure found")
        break
else:
    print("No failure found")
```

This prints `Failure found`; the `else` does not run. Without a failure, the `else` would run, even for an empty list. It belongs to the loop, not the inner `if`.

**Trace carefully:** In nested loops, the inner loop runs for each outer iteration. `break` exits only the inner loop when it occurs there. In a `while` loop, make sure progress toward termination happens even when `continue` is used. [7]

## 11. Strings, indexing, slicing, and methods

```python
course = "Python"
print(course[0], course[-1])  # P n
print(course[1:4])           # yth
print(course[:2])            # Py
print(course[::2])           # Pto
print(course[::-1])          # nohtyP
```

Indexes start at zero. Negative indexes count backward from the end. A slice has the form `sequence[start:stop:step]`, excluding `stop`. An invalid single index raises `IndexError`; slices can safely extend beyond the available range. A zero slice step raises `ValueError`.

Strings are immutable. You can build a new string and assign it to the same name, but cannot replace a character with `course[0] = "J"`.

| Operation | Example and result |
| --- | --- |
| Strip surrounding whitespace | `"  lab  ".strip()` becomes `"lab"` |
| Normalize case | `"ERROR".lower()` becomes `"error"` |
| Replace text | `"lab-1".replace("-", "_")` becomes `"lab_1"` |
| Split into a list | `"INFO login ok".split()` gives three words |
| Join strings | `"-".join(["lab", "one"])` becomes `"lab-one"` |
| Check a prefix | `"ERROR disk".startswith("ERROR")` is `True` |
| Find a substring | `"Python".find("th")` gives `2` |

### Parse a tiny log line

```python
line = "  WARN storage_low  "
level, message = line.strip().split(maxsplit=1)
print(level)                    # WARN
print(message.replace("_", " "))  # storage low
```

The unpacking assumes two parts. Production code should handle missing fields. Build up from controlled examples before processing unfamiliar input.

**Function versus method:** `len(course)` calls a built-in function. `course.upper()` calls a method belonging to a string. `upper()` returns new text; it does not change `course` in place. [2, 5]

## 12. Lists, mutation, and copying

```python
ports = [443, 22, 80]
ports.append(8080)
ports.insert(0, 53)
ports.remove(22)             # remove the first matching value
last_port = ports.pop()      # remove and return the final item
print(ports, last_port)      # [53, 443, 80] 8080
print(sorted(ports))         # [53, 80, 443]; new list
ports.sort()                # rearrange the existing list
```

Other essentials: `len(ports)` counts items; `ports.index(80)` finds the first matching index; `ports.extend([25, 110])` adds multiple items; `del ports[0]` deletes by position.

### Assignment is not copying

```python
original = [1, 2]
alias = original
copy = original.copy()
alias.append(3)

print(original)  # [1, 2, 3]
print(copy)      # [1, 2]
print(alias is original)  # True
```

`original[:]` also makes a shallow copy. With nested lists, a shallow copy shares inner objects:

```python
rows = [[1], [2]]
other_rows = rows.copy()
other_rows[0].append(9)
print(rows)  # [[1, 9], [2]]
```

### Three habits that prevent mistakes

1. Use `items.sort()` on its own. `items = items.sort()` replaces your name with `None`.
2. Know whether a method takes a value or an index: `remove(value)` versus `pop(index)`.
3. Avoid adding/removing items from the same list you are traversing. Build a new list or iterate over a suitable copy instead.

**Check yourself:** Which operations change the existing list? Which produce a new object? Say this aloud while tracing code. [8]

## 13. Tuples, dictionaries, and sets

| Collection | Ordered? | Mutable? | Best fit |
| --- | --- | --- | --- |
| List | Yes | Yes | A sequence you will edit |
| Tuple | Yes | No | A fixed sequence or record |
| Dictionary | In insertion order | Yes | Lookup by key |
| Set | No positional order | Yes | Unique members and set operations |

### Tuples and unpacking

```python
endpoint = ("lab-pc", 443)
host, port = endpoint
single_item = (443,)  # comma makes a one-item tuple
print(host, port)     # lab-pc 443
```

A tuple can contain a mutable list; the tuple's references are fixed, but that inner list can still change.

### Dictionaries

```python
device = {"host": "lab-pc", "port": 443}
device["status"] = "online"
print(device["host"])                  # lab-pc
print(device.get("owner", "unknown")) # unknown

for key, value in device.items():
    print(f"{key}: {value}")
```

`in` checks dictionary keys. Missing bracket lookup raises `KeyError`; `get()` can return a default. Keys must be hashable: strings and integers work; lists do not. Reassigning an existing key replaces its value. Use `keys()`, `values()`, and `items()` to select what you iterate over.

### Sets

```python
observed = {22, 80, 80, 443}
allowed = {22, 443}
print(sorted(observed - allowed))  # [80]
print(sorted(observed & allowed))  # [22, 443]
```

Use `set()` for an empty set; `{}` creates an empty dictionary. Sets require hashable members and do not support indexing. Print a sorted view when you need predictable presentation. [8]

## 14. Comprehensions and nested collections

A comprehension builds a collection from an iterable, optionally filtering items. Start with an ordinary loop; shorten it only when the result stays readable.

```python
squares = []
for number in range(1, 5):
    squares.append(number ** 2)

same_squares = [number ** 2 for number in range(1, 5)]
print(same_squares)  # [1, 4, 9, 16]
```

### Filtering versus choosing a value

```python
scores = [62, 75, 91]
passing = [score for score in scores if score >= 70]
labels = ["pass" if score >= 70 else "review" for score in scores]
print(passing)  # [75, 91]
print(labels)   # ['review', 'pass', 'pass']
```

The trailing `if` filters out items. The `if ... else` before `for` chooses the value for every item.

### Build independent matrix rows

```python
matrix = [[0 for column in range(3)] for row in range(2)]
matrix[0][1] = 7
print(matrix)  # [[0, 7, 0], [0, 0, 0]]

shared_rows = [[0] * 3] * 2
shared_rows[0][1] = 7
print(shared_rows)  # [[0, 7, 0], [0, 7, 0]]
```

The multiplication in `shared_rows` repeats references to one inner list. Separate row construction avoids that aliasing problem.

### Other forms

```python
lengths = {word: len(word) for word in ["loop", "function"]}
unique_lengths = {len(word) for word in ["loop", "code"]}
print(lengths)         # {'loop': 4, 'function': 8}
print(unique_lengths) # {4}
```

**Rule of thumb:** If a comprehension needs several conditions or nested loops to explain, use a regular loop with named intermediate values. [8]

## 15. Functions, parameters, and return values

```python
def completion_percent(completed, total):
    """Return completed work as a percentage of a positive total."""
    if total <= 0:
        raise ValueError("total must be positive")
    return completed / total * 100


progress = completion_percent(3, 4)
print(f"Progress: {progress:.1f}%")  # Progress: 75.0%
```

`completed` and `total` are **parameters** in the definition. `3` and `4` are **arguments** supplied in the call. The function body runs when called. `return` ends that call and sends a value back; reaching the end without `return` returns `None`.

### Displaying versus returning

```python
def show_total(a, b):
    print(a + b)


def calculate_total(a, b):
    return a + b


value = show_total(2, 3)       # prints 5; value becomes None
answer = calculate_total(2, 3) # answer becomes 5
print(answer * 2)             # 10
```

Prefer returning calculated results when other code needs to use them. Let the calling code decide how to display or store the result.

### Positional, keyword, and default arguments

```python
def label_lab(number, status="in progress"):
    return f"Lab {number}: {status}"


print(label_lab("2.1.5"))
print(label_lab("2.1.5", status="complete"))
```

In ordinary calls, positional arguments come before keyword arguments. Do not provide the same parameter twice. A default is used only when that argument is omitted; passing `None` explicitly does not select the default.

**Try it:** Write a function that accepts a score and returns `"pass"` or `"review"`. Keep `input()` and `print()` outside it so the calculation is easy to check. [7]

## 16. Scope and mutable arguments

A useful name-lookup model is **LEGB**: local, enclosing function, global/module, then built-in. Assignment inside a function normally creates or changes a local binding. [9]

```python
count = 10


def next_count(count):
    return count + 1


print(next_count(count))  # 11
print(count)              # 10
```

`global` targets a module-level binding; `nonlocal` targets an existing binding in an enclosing function. For beginner programs, passing inputs and returning results usually makes dependencies clearer.

### Mutating an argument is visible to the caller

```python
def add_status(statuses):
    statuses.append("complete")


records = ["started"]
add_status(records)
print(records)  # ['started', 'complete']
```

The parameter and caller refer to the same list. Rebinding the parameter to a new list would be different from changing that shared object.

### Avoid a shared mutable default

```python
def record_lab(lab, records=None):
    if records is None:
        records = []
    records.append(lab)
    return records


print(record_lab("2.1.5"))  # ['2.1.5']
print(record_lab("next"))   # ['next']
```

A default such as `records=[]` is created once when the definition executes, not anew on each call. `None` lets the function create a fresh list when needed. [7]

**Name-hiding trap:** `list = [1, 2]` is legal, but then `list("abc")` tries to call your list object and fails. Use `numbers`, `records`, or another descriptive name.

## 17. Recursion, iterators, and generators

### Recursion: solve a smaller version

```python
def factorial(number):
    if number < 0:
        raise ValueError("number must be nonnegative")
    if number <= 1:
        return 1
    return number * factorial(number - 1)


print(factorial(4))  # 24
```

This teaching function expects an integer. Trace `4 * 3 * 2 * 1`. The base case stops the recursion, and every recursive call moves toward it. Excessive recursion can raise `RecursionError`; a loop is often simpler for large repetitive tasks.

### Iteration: request the next item

```python
iterator = iter(["start", "finish"])
print(next(iterator))          # start
print(next(iterator))          # finish
print(next(iterator, "done")) # done
```

Without a default, requesting beyond the end raises `StopIteration`. A `for` loop handles normal iterator exhaustion for you.

### Generators: produce items as needed

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1


sequence = countdown(3)
print(list(sequence))  # [3, 2, 1]
print(list(sequence))  # []: this generator is exhausted
```

`yield` pauses the generator while preserving its state. A normal `return` ends the call. A generator expression uses parentheses: `(n * n for n in range(4))`; list comprehension brackets build a list immediately.

**Study distinction:** Iterable means "can provide an iterator." Iterator means "tracks progress and supplies successive items." A list can be iterated again; one exhausted generator cannot be restarted without creating a new one. [1, 9]

## 18. Exceptions and error handling

| Error | Typical cause | First thing to inspect |
| --- | --- | --- |
| `SyntaxError` | Malformed Python | Colon, quote, bracket, or preceding line |
| `IndentationError` | Incorrect block indentation | Leading whitespace |
| `NameError` | Unknown name | Spelling, scope, execution order |
| `TypeError` | Unsupported operation or wrong argument type | Types of the values |
| `ValueError` | Right kind of input, invalid value | Conversion or allowed values |
| `IndexError` | Sequence position does not exist | Index and sequence length |
| `KeyError` | Dictionary key does not exist | Actual keys or use of `get()` |
| `ZeroDivisionError` | Division by zero | Denominator |
| `FileNotFoundError` | Requested file is missing | Path and working directory |

```python
def parse_count(text):
    count = int(text)
    if count < 0:
        raise ValueError("count cannot be negative")
    return count


try:
    count = parse_count("-2")
except ValueError as error:
    print(f"Invalid count: {error}")
else:
    print(f"Count accepted: {count}")
finally:
    print("Validation attempt finished.")
```

`except` handles a matching exception. `else` runs if the `try` finishes without an exception. `finally` runs as control leaves the statement during normal Python execution, whether or not a matching handler ran. `raise` signals a problem to the caller. An unhandled exception propagates up the call stack. [10]

### Know the hierarchy

`BaseException` includes `Exception`, `KeyboardInterrupt`, and `SystemExit`. `ArithmeticError` and `LookupError` are categories under `Exception`; division errors fall under the former, key/index errors under the latter. Handle a specific subclass before its broader parent. [18]

**Good habit:** Catch the errors you expect around the operation that can fail. Avoid a bare `except:` and avoid silently ignoring failures. Read the last traceback line first, then work upward to your code.

## 19. Built-ins to learn first

Built-ins are available without an import. Some entries in the documentation are types such as `int` and `list`, which you call to construct values. This is an original practice reference, not a replacement for their full documentation. [1]

| Task | Example | Expected result |
| --- | --- | --- |
| Count items | `len([22, 80, 443])` | `3` |
| Add values | `sum([5, 7, 9])` | `21` |
| Find extremes | `min([5, 7, 9])`, `max([5, 7, 9])` | `5`, `9` |
| Absolute value | `abs(-12)` | `12` |
| Quotient and remainder | `divmod(17, 5)` | `(3, 2)` |
| Build a sorted list | `sorted([3, 1, 2])` | `[1, 2, 3]` |
| Reverse traversal | `list(reversed([1, 2, 3]))` | `[3, 2, 1]` |
| Check every item | `all([True, True, False])` | `False` |
| Check any item | `any([False, True])` | `True` |
| Character to code point | `ord("A")` | `65` |
| Code point to character | `chr(65)` | `"A"` |
| Inspect a value's type | `type(5).__name__` | `"int"` |
| Check a type relationship | `isinstance(5, int)` | `True` |
| Developer representation | `repr("a\nb")` | Text showing the newline as an escape |

### Enumerate and zip

```python
labs = ["print", "input", "loops"]
for number, topic in enumerate(labs, start=1):
    print(number, topic)

names = ["lab-a", "lab-b"]
scores = [80, 95]
for name, score in zip(names, scores, strict=True):
    print(name, score)
```

`enumerate()` supplies a counter and item. `zip()` pairs corresponding items. Normal `zip()` stops at the shortest input; `strict=True` raises `ValueError` on unequal lengths when consumed and requires Python 3.10+.

**Edge cases:** `all([])` is `True`; `any([])` is `False`. `min([])` and `max([])` raise `ValueError` unless an appropriate `default` is supplied. `sum([])` is `0`.

## 20. Read function documentation confidently

Your linked built-in-functions page is a reference to consult while coding. You do not need to memorize every entry. Begin with the function's purpose, signature, return value, exceptions, and version notes.

### Reading a signature

```text
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

`*objects` allows multiple positional values. The following options are keyword-only. The displayed values after `=` are defaults. This signature does not mean you type an actual star before each object you print.

| Symbol or pattern | Meaning |
| --- | --- |
| `parameter=value` | An optional parameter with a default |
| `/` in a definition/signature | Parameters before it are positional-only |
| Bare `*` in a definition/signature | Parameters after it are keyword-only |
| `*args` | Collect extra positional arguments into a tuple |
| `**kwargs` | Collect extra keyword arguments into a dictionary |
| `*values` in a call | Unpack an iterable into positional arguments |
| `**options` in a call | Unpack a mapping into keyword arguments |

```python
def lab_label(number, /, *, status="started"):
    return f"{number}: {status}"


print(lab_label("2.1.5", status="complete"))
values = ["Python", "Essentials"]
print(*values, sep=" / ")
```

### Built-in, method, or imported function?

`len(values)` is built in. `values.append("practice")` is a list method. `math.sqrt(25)` is a standard-library function accessed after `import math`.

Use `help(print)` for interactive documentation and `dir(str)` to explore available string attributes. A return type matters: `sorted()` gives a list, while `map()`, `filter()`, and `zip()` give iterators in Python 3.

**Version habit:** Match the documentation version to your course interpreter. A feature on the moving `/3/` documentation page may be newer than your installed Python. [1, 7]

## 21. Built-ins to recognize and revisit

The following map includes the remaining Python 3.14 built-ins, grouped by purpose. Learn the core topics first; use this page to recognize unfamiliar names when reading code. [1]

| Group | Built-ins and purpose |
| --- | --- |
| Numeric construction | `complex()` creates complex numbers; `pow()` computes powers, optionally modulo a value |
| Binary/text representation | `ascii()` escapes non-ASCII characters; `format()` applies a format specification |
| Binary containers | `bytes()` is immutable; `bytearray()` is mutable; `memoryview()` exposes a buffer view |
| Immutable collection | `frozenset()` creates an immutable set |
| Collection construction | `list()`, `tuple()`, `dict()`, `set()`, `range()` |
| Functional iteration | `map()` transforms items; `filter()` retains matching items |
| Slicing object | `slice()` represents slice parameters |
| Inspection | `callable()`, `id()`, `vars()`, `globals()`, `locals()` |
| Attributes | `getattr()`, `setattr()`, `hasattr()`, `delattr()` |
| Classes | `object()`, `super()`, `issubclass()`, `classmethod()`, `staticmethod()`, `property()` |
| Hashing | `hash()` provides an object's hash; it is not a cryptographic digest |
| Debugging | `breakpoint()` enters a debugger |
| Dynamic execution | `compile()`, `eval()`, `exec()`; execute only appropriately trusted code |
| Import machinery | `__import__()`; ordinary application code normally uses `import` |
| Asynchronous iteration | `aiter()`, `anext()`; revisit when learning `async`/`await` |

### A small map/filter demonstration

```python
numbers = [1, 2, 3, 4]
print(list(map(str, numbers)))  # ['1', '2', '3', '4']
print(list(filter(lambda n: n % 2 == 0, numbers)))  # [2, 4]
```

`lambda n: ...` creates a small anonymous function with one expression. A named function or list comprehension is often clearer for beginners.

**Practical boundary:** Understanding a function's name is not the same as needing it. Your next useful skill is usually better control flow, clearer functions, or stronger debugging, rather than dynamic execution or advanced object customization.

## 22. Files and structured data

Use `with` to manage an open file's lifetime. Choose an explicit text encoding, commonly UTF-8. Relative paths are resolved from the process's current working directory. [11]

```python
from pathlib import Path

report_path = Path("lab_notes.txt")

with report_path.open("w", encoding="utf-8") as report:
    report.write("Lab 2.1.5: practiced print()\n")

with report_path.open("r", encoding="utf-8") as report:
    for line in report:
        print(line.rstrip("\n"))
```

| Mode | Meaning |
| --- | --- |
| `r` | Read; file must exist |
| `w` | Write; create or truncate existing contents |
| `a` | Append; create if missing |
| `x` | Create exclusively; fail if already present |
| `b` | Binary mode modifier, such as `rb` |

**Run this example in a practice folder:** `w` replaces an existing file with the same name. `write()` does not add a newline automatically.

### JSON for structured records

```python
import json

record = {"lab": "2.1.5", "completed": True}
encoded = json.dumps(record)
decoded = json.loads(encoded)
print(decoded["lab"])        # 2.1.5
print(decoded["completed"])  # True
```

JSON text and Python code are different formats: JSON uses `true`, `false`, and `null`, while Python uses `True`, `False`, and `None`. Use a parser for data; do not use `eval()` to read a data file.

**Extension:** Use `csv` for CSV records instead of manually splitting every line on a comma; real CSV can contain quoted commas. Files and JSON are useful portfolio extensions beyond the core beginner examples.

## 23. Modules, environments, and project habits

A module lets you reuse definitions. The standard library ships with Python; third-party packages are installed separately. All worked examples in this guide use only built-ins or the standard library.

```python
import math
from pathlib import Path

print(math.sqrt(81))  # 9.0
print(Path("lab_notes.txt").suffix)  # .txt
```

Avoid filenames such as `math.py`, `random.py`, or `json.py` in a project using those modules; a local file can hide the module you intended to import. Avoid `from module import *`, which makes name origins harder to follow. [12]

### Keep project dependencies separate

A virtual environment isolates installed packages for one project. From a terminal in the project directory:

```shell
python -m venv .venv
```

Activate it with `.venv\Scripts\Activate.ps1` in Windows PowerShell, `.venv\Scripts\activate.bat` in Windows Command Prompt, or `source .venv/bin/activate` in a typical macOS/Linux shell. Use `deactivate` to leave it. Shell policy can affect PowerShell activation; using the environment's Python executable directly is also possible. [14]

Use `python -m pip` when package installation is needed so pip belongs to the selected interpreter. You do not need to install a package to use `print`, `math`, or `json`.

### Portfolio habits

- Give scripts clear names, such as `lab_02_01_05_print.py`.
- Record the lab objective, your solution, sample inputs/output, and lessons learned.
- Credit Cengage and NetAcad where their assignments or explanations informed your work; record the actual textbook title/edition when available.
- Keep `.venv/`, `__pycache__/`, passwords, tokens, and personal data out of commits.
- Save small, working changes with commit messages that explain what you added or fixed.

**Reproducibility:** A reader should know which Python version you used, how to run the file, and what a successful result looks like.

## 24. A reusable beginner script

This program combines functions, validation, a loop, and formatted output. Type hints describe expected types; Python does not enforce them automatically at runtime.

```python
"""Calculate progress toward a target number of Python labs."""


def read_nonnegative_integer(prompt: str) -> int:
    """Keep asking until the user enters a nonnegative integer."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Enter a whole number.")
            continue

        if value < 0:
            print("Enter zero or a positive number.")
            continue
        return value


def completion_percent(completed: int, total: int) -> float:
    """Calculate progress for a valid count and positive total."""
    if total <= 0:
        raise ValueError("Total must be positive.")
    if not 0 <= completed <= total:
        raise ValueError("Completed must be between zero and total.")
    return completed / total * 100


def main() -> None:
    total = read_nonnegative_integer("Total planned labs: ")
    completed = read_nonnegative_integer("Completed labs: ")
    try:
        percent = completion_percent(completed, total)
    except ValueError as error:
        print(f"Cannot calculate progress: {error}")
        return
    print(f"Progress: {percent:.1f}%")


if __name__ == "__main__":
    main()
```

The guard calls `main()` when the file runs directly, and avoids calling it merely because another module imports the file. Try totals/completed pairs of `4/3`, `0/0`, and `4/5`, plus text and negative entries at the prompts. [12]

## 25. Debugging and checking your work

### Use a repeatable debugging process

1. State what the program should do for one specific input.
2. Reproduce the problem with the smallest useful example.
3. Read the error type and message; find the relevant line in your file.
4. Inspect values and types just before that line.
5. Change one thing, rerun, and compare with your prediction.
6. Add another case that would reveal the same mistake later.

```python
raw = "7"
print(repr(raw), type(raw).__name__)  # '7' str
count = int(raw)
print(count + 1)                     # 8
```

`repr()` exposes details such as quotes and escape characters that normal output can hide. Debugger breakpoints let you pause and inspect the same information without adding many prints.

### Build a useful set of checks

| Case | Example | What it reveals |
| --- | --- | --- |
| Typical | Three labs completed out of four | Normal calculation |
| Boundary | Zero completed; all completed | Inclusive/exclusive comparisons |
| Invalid format | `"three"` entered as a count | Conversion handling |
| Invalid meaning | Negative count or completed above total | Range validation |
| Empty input | Empty text/list/file | Assumptions about available data |

For the function in Section 24, you can use:

```python
# Run after defining completion_percent from Section 24.
assert completion_percent(3, 4) == 75.0
assert completion_percent(0, 4) == 0.0
assert completion_percent(4, 4) == 100.0
```

Assertions help verify development assumptions. Do not use them as the only validation for user input or security checks: optimized Python execution can disable them.

**A logic error may produce no exception.** If your loop runs four times when it should run five, Python can execute it perfectly while your answer is still wrong. Trace variables, not just error messages.

## 26. Classes and other next steps

Classes bundle data and behavior into objects. Learn this after functions and collections feel comfortable; it is a preview, not the center of this guide's PCEP preparation. [9]

```python
class LabRecord:
    """Track a lab identifier and its completion state."""

    def __init__(self, number):
        self.number = number
        self.completed = False

    def mark_complete(self):
        self.completed = True


lab = LabRecord("2.1.5")
lab.mark_complete()
print(lab.number, lab.completed)  # 2.1.5 True
```

`LabRecord` is the class; `lab` refers to an instance. `__init__` initializes the instance after construction. `self` is the conventional first parameter in an instance method and refers to that instance.

### Where to go after the foundation

| Topic | Why learn it next? |
| --- | --- |
| Automated testing | Check behavior as programs change |
| Type hints | Document expected values and support static analysis |
| `pathlib`, `csv`, `json` | Process local files and structured records |
| Regular expressions | Search text using patterns |
| `logging` | Record useful events and troubleshooting context |
| APIs and HTTP | Exchange data with services you are authorized to use |
| Classes/dataclasses | Model records and behavior clearly |
| Async programming | Coordinate tasks that spend time waiting |

### Cybersecurity habits from the beginning

Use sample logs and synthetic data while learning. Keep secrets out of code and repositories. Validate inputs before using them in paths, commands, or calculations. Prefer data parsers to dynamic code execution. A small, understandable script that handles bad input is more useful than a large script you cannot explain.

**Do not rush past the foundation:** A clear function, a correct loop, and reliable error handling support almost every advanced topic on this page.

## 27. Practice: predict the result

Write your prediction and reasoning before running each example. These are original practice exercises, not copied exam questions. Each numbered snippet is independent.

### 1. Output controls

```python
print("A", "B", sep=":", end="!")
print("C")
```

### 2. Text and numeric conversion

```python
value = "6"
print(value * 2)
print(int(value) * 2)
```

### 3. Arithmetic

```python
print(3 + 2 ** 3 * 2)
print(-8 // 3, -8 % 3)
```

### 4. Truthiness

```python
print(bool("False"), bool(""))
print("" or "fallback")
```

### 5. Loop control

```python
for number in range(1, 6):
    if number == 2:
        continue
    if number == 4:
        break
    print(number)
else:
    print("finished")
```

### 6. Slicing

```python
word = "security"
print(word[1:6:2])
print(word[-3:])
```

## 28. Practice: trace, repair, and build

### 7. List references

```python
a = [2, 4]
b = a
c = a[:]
b.append(6)
print(a, c)
```

### 8. A return-value trap

```python
def double(number):
    print(number * 2)


result = double(5)
print(result)
```

### 9. Repair these independent fragments

```text
if score >= 70
    print("Pass")

count = input("Count: ")
print(count + 1)

items = [3, 1, 2]
items = items.sort()

if role == "admin" or "teacher":
    print("Allowed")
```

For each fragment, name the problem before changing it. Assume `score` and `role` already exist.

### 10. Build a status counter

Write `count_statuses(statuses)` to count strings in a list and return a dictionary. For `["OK", "FAIL", "OK", "WARN"]`, return `{"OK": 2, "FAIL": 1, "WARN": 1}`. Empty input should return `{}`. Preserve the supplied spelling; do not silently merge differently cased values.

### 11. Build a bounded count reader

Ask for a whole number between 1 and 5, inclusive. Keep asking after invalid text or an out-of-range number. Return the accepted integer from a function.

### 12. Trace a generator

Using `countdown()` from Section 17, create `g = countdown(2)`. Predict `next(g)`, then `list(g)`, then `list(g)` again.

## 29. Answers and explanations: 1-9

| Exercise | Answer | Why |
| --- | --- | --- |
| 1 | `A:B!C` followed by a newline | The first call ends with `!`, so the next call continues that line |
| 2 | `66`, then `12`, on separate lines | Repeating text differs from multiplying an integer |
| 3 | `19`, then `-3 1` | Power before multiplication; floor division rounds downward |
| 4 | `True False`, then `fallback` | Nonempty text is truthy; `or` returns the fallback operand |
| 5 | `1`, then `3`, on separate lines | Skip 2; break at 4; loop else is bypassed |
| 6 | `eui`, then `ity` | Indexes 1, 3, 5; then the final three characters |
| 7 | `[2, 4, 6] [2, 4]` | `b` aliases `a`; `c` is a separate shallow copy |
| 8 | `10`, then `None`, on separate lines | The function prints but does not return a calculated value |

### 9. Repairs

```python
score = 80
if score >= 70:
    print("Pass")
```

Add the missing colon. A colon announces the block that follows.

```python
count = int(input("Count: "))
print(count + 1)
```

Convert the string. For a robust program, add `ValueError` handling as in Section 06.

```python
items = [3, 1, 2]
items.sort()
print(items)  # [1, 2, 3]
```

Keep the list name. Alternatively, `items = sorted(items)` assigns a new sorted list.

```python
role = "teacher"
if role in ("admin", "teacher"):
    print("Allowed")
```

Test both allowed values through membership. This is only a condition demonstration, not a complete authorization system.

## 30. Answers and explanations: 10-12

### 10. Status counter

```python
def count_statuses(statuses):
    counts = {}
    for status in statuses:
        counts[status] = counts.get(status, 0) + 1
    return counts


sample = ["OK", "FAIL", "OK", "WARN"]
print(count_statuses(sample))
assert count_statuses([]) == {}
assert count_statuses(["OK", "OK"]) == {"OK": 2}
assert count_statuses(["ok", "OK"]) == {"ok": 1, "OK": 1}
```

`get(status, 0)` starts a new category at zero. Each item increments exactly one category. Empty input skips the loop and returns an empty dictionary.

### 11. Bounded count reader

```python
def read_count():
    while True:
        try:
            count = int(input("Enter a count from 1 to 5: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if 1 <= count <= 5:
            return count
        print("The count must be between 1 and 5.")


print(f"Accepted: {read_count()}")
```

The exception handler addresses format; the comparison addresses meaning. `return` exits the function once an acceptable integer arrives. Try `hello`, `0`, `6`, and `3` in that order.

### 12. Generator state

The results are `2`, then `[1]`, then `[]`. `next(g)` consumes the first value; `list(g)` consumes the remaining one. The final conversion finds the same generator already exhausted.

**After checking:** Redo every missed question with different values. Write the rule that explains the result, not just the correct output.

## 31. Portfolio projects and a study routine

### Four projects that build on one another

| Project | Requirements | Evidence to save |
| --- | --- | --- |
| Lab 2.1.5 output showcase | Use multiple arguments, `sep`, `end`, escapes, and f-strings | Script plus exact output and a note on each change |
| Lab progress tracker | Input validation, functions, percentage calculation | Typical/boundary/invalid examples |
| Sample log summary | Read synthetic lines, count statuses, report totals | Small sample file, code, expected counts |
| Little Legends inventory practice | Store fictional item names, quantities, and integer-cent prices | Record structure, totals, and checks for invalid quantities |

For the inventory project, compute `quantity * unit_price_cents` and sum across items. Format dollars only when displaying results. Use sample inventory so the project can be shared without exposing private business records.

### A repeatable 30-minute session

1. **Five minutes:** Recall yesterday's rules without looking.
2. **Ten minutes:** Read one small Cengage/NetAcad topic and trace an example.
3. **Ten minutes:** Write or repair a small program from scratch.
4. **Five minutes:** Record one mistake, its cause, and the fix.

### Study order

- Sessions 1-3: Syntax, names/types, `print()`, input, conversion.
- Sessions 4-6: Arithmetic, Boolean logic, branches, loops.
- Sessions 7-9: Strings, collections, slicing, copying, comprehensions.
- Sessions 10-12: Functions, scope, recursion, generators, exceptions.
- Later sessions: Mixed practice, small projects, and your booked exam's syllabus.

### Before you call a topic learned

Can you explain it in your own words? Predict a result? Write an example without copying? Fix a broken example? Test an edge case? If one answer is no, use it to choose the next practice task.

**Portfolio reflection prompt:** "My program needed to ___. I first tried ___. The problem was ___. I corrected it by ___. I checked it using ___."

## 32. One-page writing checklist

### Before writing

- State the problem, required inputs, expected outputs, and allowed ranges.
- Choose simple types and write the steps in plain language.
- Decide which calculations should become functions.

### While writing

- Use four spaces per indentation level and consistent, descriptive names.
- Finish block headers with a colon; balance quotes and delimiters.
- Distinguish `=` from `==`, and `==` from `is`.
- Remember that `input()` produces text and `print()` returns `None`.
- Use parentheses when operator precedence is hard to read.
- Remember that range/slice stop positions are excluded.
- Separate calculating a value from displaying that value.
- Know whether an operation mutates an object or returns a new one.
- Use `is None` to check the absence of a value.
- Keep functions focused; pass inputs and return useful outputs.
- Write comments explaining purpose or a non-obvious decision.

### Before submitting or committing

- Run from a fresh process so old interactive variables do not hide problems.
- Check normal, boundary, empty, and invalid cases where they apply.
- Verify the exact output format required by the assignment.
- Remove temporary debugging output and unused code/imports.
- Include a short docstring for a reusable function or module.
- Confirm the filename, run command, and Python version are documented.
- Attribute sources and follow course rules for publishing assignments.
- Inspect files for secrets or personal data before committing.

### Ten traps to recognize immediately

`"2" + "3"` concatenates text. `^` is XOR. `//` floors. `bool("False")` is true. `list.sort()` returns `None`. Assignment does not copy a list. Mutable defaults persist across calls. A loop's `else` is skipped after `break`. `is` compares identity. A function without a returned value yields `None`.

## 33. Official references and scope

Use the numbered references throughout the guide to continue reading. Explanations, exercises, and project ideas were written for this guide; they are not reproductions of Cengage textbook passages or NetAcad lab solutions.

1. [Python built-in functions, Python 3.14](https://docs.python.org/3.14/library/functions.html). Your original link: [moving Python 3 built-ins page](https://docs.python.org/3/builtins/functions.html).
2. [Python tutorial: introduction](https://docs.python.org/3.14/tutorial/introduction.html).
3. [PEP 8: Style Guide for Python Code](https://peps.python.org/pep-0008/).
4. [Lexical analysis: names, indentation, literals](https://docs.python.org/3.14/reference/lexical_analysis.html).
5. [Built-in types](https://docs.python.org/3.14/library/stdtypes.html).
6. [Expressions and operator precedence](https://docs.python.org/3.14/reference/expressions.html).
7. [Control flow and defining functions](https://docs.python.org/3.14/tutorial/controlflow.html).
8. [Data structures](https://docs.python.org/3.14/tutorial/datastructures.html).
9. [Classes, scope, iterators, and generators](https://docs.python.org/3.14/tutorial/classes.html).
10. [Errors and exceptions](https://docs.python.org/3.14/tutorial/errors.html).
11. [Input/output, formatting, files, and JSON](https://docs.python.org/3.14/tutorial/inputoutput.html).
12. [Modules and script execution](https://docs.python.org/3.14/tutorial/modules.html).
13. [Floating-point limitations](https://docs.python.org/3.14/tutorial/floatingpoint.html).
14. [Virtual environments and packages](https://docs.python.org/3.14/tutorial/venv.html).
15. [Python tutorial index](https://docs.python.org/3.14/tutorial/index.html).
16. [Python Institute: PCEP certification and exam versions](https://pythoninstitute.org/pcep).
17. [Python Institute: PCEP exam syllabus](https://pythoninstitute.org/pcep-exam-syllabus).
18. [Built-in exceptions and hierarchy](https://docs.python.org/3.14/library/exceptions.html).

**How to pair with class materials:** Match the topic names to your assigned Cengage reading and NetAcad lesson. Add exact chapter/page references to your own notes after checking your edition. NetAcad Lab 2.1.5 and its `print()` focus are included from your description of the course.

**Version scope:** The guide avoids relying on new interpreter features for its core lessons. `zip(strict=True)` requires Python 3.10 or later. Confirm your instructor's interpreter and exam version when using external documentation.
