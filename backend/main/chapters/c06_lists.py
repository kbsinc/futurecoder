import random
from textwrap import dedent
from typing import List

from main.exercises import generate_list, generate_string
from main.text import Page, VerbatimStep, ExerciseStep, Step, MessageStep
from main.utils import returns_stdout


class IntroducingLists(Page):
    class first_list(VerbatimStep):
        """
It's time to learn about a powerful new type of value called lists. Here's an example:

__program_indented__
        """

        def program(self):
            words = ['This', 'is', 'a', 'list']

            for word in words:
                print(word)

    class can_contain_anything(VerbatimStep):
        """
A list is a *sequence* (an ordered collection/container) of any number of values.
The values are often referred to as *elements*.
They can be anything: numbers, strings, booleans, even lists! They can also be a mixture of types.

To create a list directly, like above:

1. Write some square brackets: `[]`
2. If you don't want an empty list, write some expressions inside to be the elements.
3. Put commas (`,`) between elements to separate them.

Here's another example of making a list:

__program_indented__
        """

        def program(self):
            x = 1
            things = ['Hello', x, x + 3]
            print(things)

    class numbers_sum(VerbatimStep):
        """
As you saw above, lists are *iterable*, meaning you can iterate over them with a `for loop`.
Here's a program that adds up all the numbers in a list:

__program_indented__
        """

        def program(self):
            numbers = [3, 1, 4, 1, 5, 9]

            total = 0
            for number in numbers:
                total += number

            print(total)

    class strings_sum(ExerciseStep):
        """
Now modify the program so that it can add up a list of strings instead of numbers.
For example, given:

    words = ['This', 'is', 'a', 'list']

it should print:

    Thisisalist
        """

        hints = """
This is very similar to the exercises you've done building up strings character by character.
The solution is very similar to the program that adds numbers.
In fact, what happens if you try running that program with a list of strings?
The problem is that 0. You can't add 0 to a string because numbers and strings are incompatible.
Is there a similar concept among strings to 0? A blank initial value?
"""

        @returns_stdout
        def solution(self, words: List[str]):
            total = ''
            for word in words:
                total += word

            print(total)

        tests = [
            (['This', 'is', 'a', 'list'], 'Thisisalist'),
            (['The', 'quick', 'brown', 'fox', 'jumps'], 'Thequickbrownfoxjumps'),
        ]

    class double_numbers(ExerciseStep):
        """
Optional bonus challenge: extend the program to insert a separator string *between* each word.
For example, given

    words = ['This', 'is', 'a', 'list']
    separator = ' - '

it would output:

    This - is - a - list

Lists and strings have a lot in common.
For example, you can add two lists to combine them together into a new list.
You can also create an empty list that has no elements.
Check for yourself:

    numbers = [1, 2] + [3, 4]
    print(numbers)
    new_numbers = []
    new_numbers += numbers
    new_numbers += [5]
    print(new_numbers)

With that knowledge, write a program which takes a list of numbers
and prints a list where each number has been doubled. For example, given:

    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

it would print:

    [6, 2, 8, 2, 10, 18, 4, 12, 10]
        """

        hints = """
Remember that you can multiply numbers using `*`.
This program is structurally very similar to the programs you've written to build up strings character by character.
Make a new list, and then build it up element by element in a for loop.
Start with an empty list.
You can make a list with one element `x` by just writing `[x]`.
You can add an element to a list by adding a list containing one element.
        """

        @returns_stdout
        def solution(self, numbers: List[int]):
            double = []
            for number in numbers:
                double += [number * 2]
            print(double)

        tests = [
            ([3, 1, 4, 1, 5, 9, 2, 6, 5], [6, 2, 8, 2, 10, 18, 4, 12, 10]),
            ([0, 1, 2, 3], [0, 2, 4, 6]),
        ]

    class filter_numbers(ExerciseStep):
        """
Great!

When you want to add a single element to the end of a list, instead of:

    some_list += [element]

it's actually more common to write:

    some_list.append(element)

There isn't really a big difference between these, but `.append`
will be more familiar and readable to most people.

Now use `.append` to write a program which prints a list containing only the numbers bigger than 5.

For example, given:

    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

it would print:

    [9, 6]
        """

        hints = """
This is very similar to the previous exercise.
The difference is that sometimes you should skip appending to the new list.
Use an `if` statement.
Use a comparison operator to test if a number is big enough to add.
        """

        # TODO enforce not using +=

        @returns_stdout
        def solution(self, numbers: List[int]):
            big_numbers = []
            for number in numbers:
                if number > 5:
                    big_numbers.append(number)
            print(big_numbers)

        tests = [
            ([3, 1, 4, 1, 5, 9, 2, 6, 5], [9, 6]),
            ([0, 2, 4, 6, 8, 10], [6, 8, 10]),
        ]

    final_text = """
Fantastic! We're making great progress.
"""


class UsingBreak(Page):
    title = "Using `break` to end a loop early"

    class list_contains_exercise(ExerciseStep):
        """
Exercise: write a program which takes a list and a value and checks
if the list contains the value. For example, given:

    things = ['This', 'is', 'a', 'list']
    thing_to_find = 'is'

it should print `True`, but for

    thing_to_find = 'other'

it should print `False`.
        """

        hints = """
You will need a loop.
You will need an `if` statement.
You will need a comparison operator.
Specifically `==`.
You need a boolean variable that you print at the end.
If you find the element in the list you should set that variable to `True`.
Once you've found the element, you can't unfind it.
That means that once you set the variable to `True`, it should never be set to anything else after that.
Don't use an `else`.
There is no reason to ever set the variable to `False` inside the loop.
        """

        @returns_stdout
        def solution(self, things, thing_to_find):
            found = False
            for thing in things:
                if thing == thing_to_find:
                    found = True

            print(found)

        tests = [
            ((['This', 'is', 'a', 'list'], 'is'), True),
            ((['This', 'is', 'a', 'list'], 'other'), False),
            (([1, 2, 3, 4], 1), True),
            (([1, 2, 3, 4], 0), False),
        ]

        @classmethod
        def generate_inputs(cls):
            contained = random.choice([True, False])
            things = generate_list(int)
            if contained:
                thing_to_find = random.choice(things)
            else:
                thing_to_find = random.choice([
                    min(things) - 1,
                    max(things) + 1,
                ])
            return dict(
                things=things,
                thing_to_find=thing_to_find,
            )

    final_text = """
Nice!

A typical solution looks something like this:

    found = False
    for thing in things:
        if thing == thing_to_find:
            found = True

    print(found)

Your solution is probably similar. It's fine, but it's a bit inefficient.
That's because it'll loop over the entire list even if it finds the element at the beginning.
You can stop any loop using a `break` statement, like so:

    for thing in things:
        if thing == thing_to_find:
            found = True
            break

This is just as correct but skips unnecessary iterations and checks once it finds the element.
You can use snoop to see the difference.
        """


class GettingElementsAtPosition(Page):
    title = "Getting Elements at a Position"

    class introducing_subscripting(VerbatimStep):
        """
Looping is great, but often you just want to retrieve a single element from the list at a known position.
Here's how:

__program_indented__
        """

        def program(self):
            words = ['This', 'is', 'a', 'list']

            print(words[0])
            print(words[1])
            print(words[2])
            print(words[3])

    class index_error(Step):
        """
In general, you can get the element at the position `i` with `words[i]`. The operation is called *subscripting* or *indexing*, and the position is called the *index*.

You've probably noticed that the first index is 0, not 1. In programming, counting starts at 0. It seems weird, but that's how most programming languages do it, and it's generally agreed to be better.

This also means that the last index in this list of 4 elements is 3. What happens if you try getting an index greater than that?
        """

        program = "words[4]"

        def check(self):
            return "IndexError" in self.result

    class introducing_len_and_range(VerbatimStep):
        """
There you go. `words[4]` and beyond don't exist, so trying that will give you an error.

By the way, you can get the number of elements in a list (commonly called the *length*) using `len(words)`.
That means that the last valid index of the list is `len(words) - 1`, so the last element is `words[len(words) - 1]`. Try these for yourself.

So in general, the valid indices are:

    [0, 1, 2, ..., len(words) - 2, len(words) - 1]

There's a handy built in function to give you these values, called `range`:

__program_indented__
        """

        def program(self):
            for i in range(10):
                print(i)

    class range_len(VerbatimStep):
        """
`range(n)` is similar to the list `[0, 1, 2, ..., n - 2, n - 1]`.
This gives us an alternative way to loop over a list:

__program_indented__
        """

        def program(self):
            words = ['This', 'is', 'a', 'list']

            for index in range(len(words)):
                print(index)
                print(words[index])

    class index_exercise(ExerciseStep):
        """
Let's get some exercise! Given a list `things` and a value `to_find`,
print the first index of `to_find` in the list, i.e. the lowest number `i` such that
`things[i]` is `to_find`. For example, for

    things = ['on', 'the', 'way', 'to', 'the', 'store']
    to_find = 'the'

your program should print `1`.

You can assume that `to_find` appears at least once.
        """

        hints = """
You will need to look at all the possible indices of `things` and check which one is the answer.
To look at all possible indices, you will need a loop over `range(len(things))`.
To check if an index is the answer, you will need to use:
- `if`
- the index in a subscript
- `==`
Since you're looking for the first index, you need to stop the loop once you find one.
You learned how to stop a loop in the middle recently.
You need to use `break`.
        """

        class all_indices(MessageStep, ExerciseStep):
            """
            You're almost there! However, this prints all the indices,
            not just the first one.
            """

            @returns_stdout
            def solution(self, things, to_find):
                for i in range(len(things)):
                    if to_find == things[i]:
                        print(i)

            tests = [
                ((['on', 'the', 'way', 'to', 'the', 'store'], 'the'), "1\n4"),
                (([0, 1, 2, 3, 4, 5, 6, 6], 6), "6\n7"),
            ]

        class last_index(MessageStep, ExerciseStep):
            """
            You're almost there! However, this prints the *last* index,
            not the first one.
            """

            @returns_stdout
            def solution(self, things, to_find):
                answer = None
                for i in range(len(things)):
                    if to_find == things[i]:
                        answer = i
                print(answer)

            tests = [
                ((['on', 'the', 'way', 'to', 'the', 'store'], 'the'), 4),
                (([0, 1, 2, 3, 4, 5, 6, 6], 6), 7),
            ]

        @returns_stdout
        def solution(self, things, to_find):
            for i in range(len(things)):
                if to_find == things[i]:
                    print(i)
                    break

        tests = [
            ((['on', 'the', 'way', 'to', 'the', 'store'], 'the'), 1),
            (([0, 1, 2, 3, 4, 5, 6, 6], 6), 6),
        ]

        @classmethod
        def generate_inputs(cls):
            things = generate_list(str)
            to_find = generate_string()
            things += [to_find] * random.randint(1, 3)
            random.shuffle(things)
            return dict(
                things=things,
                to_find=to_find,
            )

    class zip_exercise(ExerciseStep):
        """
Nice!

By the way, indexing and `len()` also work on strings. Try them out in the shell.

Here's another exercise. Given two strings of equal length, e.g:

    string1 = "Hello"
    string2 = "World"

print them vertically side by side, with a space between each character:

    H W
    e o
    l r
    l l
    o d
        """

        hints = """
Did you experiment with indexing and `len()` with strings in the shell?
Forget loops for a moment. How would you print just the first line, which has the first character of each of the two strings?
In the second line you want to print the second character of each string, and so on.
You will need a `for` loop.
You will need indexing (subscripting).
You will need `range`.
You will need `len`.
You will need `+`.
You will need to index both strings.
You will need to pass the same index to both strings each time to retrieve matching characters.
"""

        @returns_stdout
        def solution(self, string1, string2):
            for i in range(len(string1)):
                char1 = string1[i]
                char2 = string2[i]
                print(char1 + ' ' + char2)

        tests = {
            ("Hello", "World"): dedent("""\
                    H W
                    e o
                    l r
                    l l
                    o d
                    """),
            ("Having", "ablast"): dedent("""\
                    H a
                    a b
                    v l
                    i a
                    n s
                    g t
                    """),
        }

        @classmethod
        def generate_inputs(cls):
            length = random.randrange(5, 11)
            return dict(
                string1=generate_string(length),
                string2=generate_string(length),
            )

    class zip_longest_exercise(ExerciseStep):
        """
Incredible!

Your solution probably looks something like this:

    for i in range(len(string1)):
        char1 = string1[i]
        char2 = string2[i]
        print(char1 + ' ' + char2)

This doesn't work so well if the strings have different lengths.
In fact, it goes wrong in different ways depending on whether `string1` or `string2` is longer.
Your next challenge is to fix this problem by filling in 'missing' characters with spaces.

For example, for:

    string1 = "Goodbye"
    string2 = "World"

output:

    G W
    o o
    o r
    d l
    b d
    y  
    e  

and for:

    string1 = "Hello"
    string2 = "Elizabeth"

output:

    H E
    e l
    l i
    l z
    o a
      b
      e
      t
      h
        """

        hints = [
            "The solution has the same overall structure and "
            "essential elements of the previous solution, "
            "but it's significantly longer and will require "
            "a few additional ideas and pieces.",
            dedent("""
            In particular, it should still contain something like:

                for i in range(...):
                    ...
                    print(char1 + ' ' + char2)
            """),
            "What should go inside `range()`? Neither `len(string1)` nor `len(string2)` is good enough.",
            "You want a loop iteration for every character in the longer string.",
            "That means you need `range(<length of the longest string>)`",
            "In other words you need to find the biggest of the two values "
            "`len(string1)` and `len(string2)`. You've already done an exercise like that.",
            "Once you've sorted out `for i in range(...)`, `i` will sometimes be too big "
            "to be a valid index for both strings. You will need to check if it's too big before indexing.",
            "Remember, the biggest valid index for `string1` is `len(string1) - 1`. "
            "`len(string)` is too big.",
            "You will need two `if` statements, one for each string.",
            "You will need to set e.g. `char1 = ' '` when `string1[i]` is not valid.",
        ]

        # TODO catch user writing string1 < string2

        @returns_stdout
        def solution(self, string1, string2):
            length1 = len(string1)
            length2 = len(string2)

            if length1 > length2:
                length = length1
            else:
                length = length2

            for i in range(length):
                if i < len(string1):
                    char1 = string1[i]
                else:
                    char1 = ' '

                if i < len(string2):
                    char2 = string2[i]
                else:
                    char2 = ' '

                print(char1 + ' ' + char2)

        tests = {
            ("Goodbye", "World"): dedent("""\
                    G W
                    o o
                    o r
                    d l
                    b d
                    y  
                    e  
                    """),
            ("Hello", "Elizabeth"): dedent("""\
                    H E
                    e l
                    l i
                    l z
                    o a
                      b
                      e
                      t
                      h
                    """),
        }

        @classmethod
        def generate_inputs(cls):
            length1 = random.randrange(5, 11)
            length2 = random.randrange(12, 20)
            if random.choice([True, False]):
                length1, length2 = length2, length1
            return dict(
                string1=generate_string(length1),
                string2=generate_string(length2),
            )

    final_text = """
Magnificent! Take a break, you've earned it!
    """
