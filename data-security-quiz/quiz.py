#!/usr/bin/env python3
import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"

QUESTIONS = [
    {
        "q": "What does GDPR stand for?",
        "opts": [
            "A) General Data Privacy Regulation",
            "B) General Data Protection Regulation",
            "C) Global Data Privacy Rules",
            "D) General Document Protection Regulation",
        ],
        "ans": "B",
    },
    {
        "q": "Which of the following is considered Personally Identifiable Information (PII)?",
        "opts": [
            "A) A user's favorite color",
            "B) An anonymized demographic dataset",
            "C) A user's email address",
            "D) A random website visitor counter",
        ],
        "ans": "C",
    },
    {
        "q": "What is the primary purpose of data encryption?",
        "opts": [
            "A) To compress data for faster transfer",
            "B) To protect data from unauthorized access",
            "C) To format data for databases",
            "D) To back up data automatically",
        ],
        "ans": "B",
    },
    {
        "q": "What is a phishing attack?",
        "opts": [
            "A) Overloading a server with traffic",
            "B) A deceptive attempt to steal sensitive information",
            "C) Physically stealing a hard drive",
            "D) Encrypting a victim's files for ransom",
        ],
        "ans": "B",
    },
    {
        "q": "What does the 'principle of least privilege' mean in data security?",
        "opts": [
            "A) Users should only have access to the data they need to perform their job",
            "B) Administrators must use the least powerful computers",
            "C) Security policies should be as simple as possible",
            "D) Passwords should only be changed when compromised",
        ],
        "ans": "A",
    },
    {
        "q": "What does MFA stand for?",
        "opts": [
            "A) Multiple Firewall Architecture",
            "B) Mandatory File Access",
            "C) Multi-Factor Authentication",
            "D) Mobile Format Authorization",
        ],
        "ans": "C",
    },
    {
        "q": "Which protocol is recommended for secure web communication?",
        "opts": ["A) HTTP", "B) FTP", "C) Telnet", "D) HTTPS"],
        "ans": "D",
    },
    {
        "q": "What is a zero-day vulnerability?",
        "opts": [
            "A) A bug that takes zero days to fix",
            "B) A software flaw unknown to the vendor and without a patch",
            "C) A vulnerability that has been known for exactly one day",
            "D) A virus that wipes the hard drive on day zero",
        ],
        "ans": "B",
    },
    {
        "q": "In cryptography, what is 'salting' a password?",
        "opts": [
            "A) Adding random data to the password before hashing it",
            "B) Sending the password in plain text over a secure channel",
            "C) Changing the password every 30 days",
            "D) Using special characters in the password",
        ],
        "ans": "A",
    },
    {
        "q": "What is ransomware?",
        "opts": [
            "A) Software that steals passwords silently",
            "B) Software that encrypts the victim's data and demands payment",
            "C) Software used to test network security",
            "D) Hardware device used to steal credit card information",
        ],
        "ans": "B",
    },
]


def print_header():
    print(
        f"\n{MAGENTA}{BOLD}===================================================={RESET}"
    )
    print(f"{CYAN}{BOLD}      DATA SECURITY & PRIVACY TERMINAL QUIZ       {RESET}")
    print(
        f"{MAGENTA}{BOLD}===================================================={RESET}\n"
    )
    print("Test your knowledge with these 10 questions.")
    print("Type A, B, C, or D and press Enter.\n")


def run_quiz():
    print_header()
    score = 0
    total = len(QUESTIONS)

    for i, item in enumerate(QUESTIONS, 1):
        print(f"{YELLOW}{BOLD}Question {i}/{total}:{RESET} {item['q']}")
        for opt in item["opts"]:
            print(f"  {opt}")

        while True:
            ans = input(f"{CYAN}Your Answer (A/B/C/D): {RESET}").strip().upper()
            if ans in ["A", "B", "C", "D"]:
                break
            print(f"{RED}Invalid input. Please enter A, B, C, or D.{RESET}")

        if ans == item["ans"]:
            print(f"{GREEN}{BOLD}Correct!{RESET}\n")
            score += 1
        else:
            print(
                f"{RED}{BOLD}Incorrect.{RESET} The correct answer was {GREEN}{item['ans']}{RESET}.\n"
            )

        time.sleep(0.5)

    print(f"{MAGENTA}{BOLD}===================================================={RESET}")
    print(f"{CYAN}{BOLD}                  QUIZ COMPLETE                     {RESET}")
    print(f"{MAGENTA}{BOLD}===================================================={RESET}")
    print(f"\nYour Final Score: {YELLOW}{BOLD}{score} / {total}{RESET}\n")

    if score == total:
        print(f"{GREEN}{BOLD}Outstanding! You are a Data Security Expert!{RESET}")
    elif score >= 7:
        print(
            f"{GREEN}Great job! You have a solid understanding of data security.{RESET}"
        )
    elif score >= 5:
        print(
            f"{YELLOW}Not bad! But there is room to brush up on some privacy concepts.{RESET}"
        )
    else:
        print(
            f"{RED}You might want to review some fundamental data security principles.{RESET}"
        )

    print()


if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print(f"\n\n{RED}{BOLD}Quiz cancelled by user. Goodbye!{RESET}\n")
        sys.exit(1)
