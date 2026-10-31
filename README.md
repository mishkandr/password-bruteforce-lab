# Password Bruteforce Lab

An educational Python project demonstrating exhaustive search: generating possible passwords, counting attempts, and measuring execution time.

## Status

In development. The project structure has been prepared; the interactive search is not implemented yet.

## Planned functionality

- Enter a short practice password locally.
- Choose the character set: digits, lowercase letters, uppercase letters, and symbols.
- Calculate the number of possible combinations.
- Search through combinations until a match is found.
- Display the number of attempts and the measured search time.

The experiment assumes that the password length and character set are known. Its timing describes this program running on the current computer, not the security of a real account.

## Project structure

```text
crack.py       — user input, program flow, and output
alphabet.py    — character-set construction
search.py      — combination generation and search
```

## Purpose

This project is a practical exercise in Python functions, loops, imports, input validation, and performance measurement.

It operates locally on practice inputs and does not connect to websites or accounts.

## Origin

Inspired by the brute-force demonstration in
[Securing Accounts](https://cs50.harvard.edu/cybersecurity/notes/0/),
part of CS50's Introduction to Cybersecurity, taught by David J. Malan.

Related educational source code:
[dmalan/cybersecurity](https://github.com/dmalan/cybersecurity).

This is an independent learning project, not affiliated with or endorsed by Harvard University or CS50.

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
See [LICENSE](LICENSE) for the license notice and attribution.