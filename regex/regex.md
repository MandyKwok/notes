# Regex

* [Regex Cheat Sheet](http://www.rexegg.com/regex-quickstart.html#ref)

* [Python Regex Tutorial](https://www.programiz.com/python-programming/regex)

  

* [Lazy vs. Greedy](https://stackoverflow.com/questions/2301285/what-do-lazy-and-greedy-mean-in-the-context-of-regular-expressions)

* [FuzzyWuzzy - fuzzy string matching](https://github.com/seatgeek/fuzzywuzzy)
  * __The Levenshtein Distance__: A metric to measure how apart are 2 sequences of words.
    * It measures the minimum number of edits (insertions, deletion, substitutions) that you need to do to change a one-word sequence into the other.



#### Python regex flags

*Python regex allows optional flags to specify when using regular expression patterns with `match()`, `search()` and `split()`, among others. [link](https://pynative.com/python-regex-flags/)*

* All RE module methods accept an optional flags argument that enables various unique features and syntax variations.
* `re.ASCII`: Perform ASCII-only matching instead of full Unicode matching.
* `re.IGNORECASE`: Perform case-insensitive matching.
* `re.MULTILINE`: This flag is used with metacharacter `^` (caret) and `$` (dollar).
  * When this flag is specified, the metacharacter `^` matches the pattern at beginning of the string and each newline’s beginning (`\n`). 
  * And the metacharacter `$` matches pattern at the end of the string and the end of each new line (`\n`).
* `re.DOTALL`: Make the DOT (`.`) special character match any character at all, including a newline. Without this flag, DOT(`.`) will match anything except a newline.
* `re.VERBOSE`: Allow comment in the regex. This flag is useful to make regex more readable by allowing comments in the regex.
* `re.LOCALE`: Perform case-insentitive matching dependent on the current locale. Use only with bytes patterns.

- *<u>To specify more than one flag, use the `|` operator to connect them.</u>*