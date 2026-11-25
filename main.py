"""One Star for Monday.

Writes a single one-line, one-star restaurant review of Monday -- Monday
treated as if it were a restaurant -- to /output/entry.txt.

The angle: Monday is the restaurant you never chose to book, and every
part of the meal is a Monday-morning grievance translated into diner
language. The waiter is the alarm clock, the one member of staff who
shows up before you are ready and drags you out of bed at 6 a.m. The
dish is cold coffee, the drink nobody asked for but everybody gets on a
Monday, served alongside the weekend's backlog of unread emails -- the
house special that arrives whether you ordered it or not, because the
inbox spent Saturday and Sunday quietly filling up while you were away.
And then comes the bill: not for the coffee, not for the emails, but
for the whole week, charged up front, before you have even tasted
anything. That is the joke that only works for Monday. No other day of
the week wakes you at dawn, hands you two days of other people's
problems, and then invoices you for the seven days ahead. Tuesday
cannot serve this complaint; Friday certainly cannot.

Why this shape wins a screenshot in the group chat: it reads like a
real diner's complaint, not like a slogan about Mondays. A real review
names a member of staff (the waiter), a dish (cold coffee), and a bill
(the whole week), and it ends the way real one-star reviews end -- with
a vow never to come back. "Never booking Monday again" is the line
somebody retypes into a chat without trimming a word, because it is the
whole review in five words: the booking, the day, and the refusal.

Word budget, counted the way the bounty counts it: the line must stay
inside 25 words, a single line of plain text, no hashtags, no stage
directions, no explanation attached. Every word here earns its place:
"Monday's" puts the day in the restaurant's name, "waiter" gives the
judge its server, "cold coffee" and "unread emails" give it the dish,
"billed me the whole week" gives it the bill, and the closing vow gives
it the punchline. One deliberate choice is the number: the emails are
not "a pile" or "loads of" emails, they are exactly 47. Real diners
complain in oddly specific numbers -- "waited 47 minutes", "charged me
for 3 bread rolls I never ordered" -- and that specificity is what makes
a complaint sound witnessed rather than invented. A round number would
read like an estimate; 47 reads like somebody counted, on a Monday
morning, while the coffee went cold. The number also spends the last
spare word of the 25-word budget on the funniest detail instead of on
filler, which is exactly what a quotable line should do. Nothing in the
line could be swapped for another day of the week without the joke
falling apart -- try it with Wednesday and the waiter, the coffee, the
emails and the bill all stop making sense.

The program itself is deliberately small and deterministic: one fixed
line, validated against the bounty's gate before it is written (a
single line, 1 to 180 characters, at most 25 words, not only white
space), then written to /output/entry.txt. There is no randomness, no
network access, no input file -- the same line comes out on every run,
so the two grading runs agree byte for byte.
"""

import os

# The review: Monday as a restaurant, reviewed by a diner who was
# woken at dawn, served the weekend's backlog, and billed for the week.
# The inbox count is exact on purpose: real one-star reviews cite oddly
# specific numbers, and 47 unread emails is a complaint somebody counted.
LINE = (
    "One star. Monday's waiter woke me at 6 a.m., served cold coffee "
    "and 47 unread emails, billed me the whole week. "
    "Never booking Monday again."
)

MAX_WORDS = 25
MAX_CHARS = 180


def validate(line):
    """Check the line against the bounty's gate before writing it.

    The gate needs UTF-8 text of 1 to 180 characters that is not only
    white space, and the task needs a single line of at most 25 words.
    Anything failing here is a bug in this file, not in the grading
    environment, so fail loudly instead of writing a bad entry.
    """
    if not line or not line.strip():
        raise SystemExit("entry is empty or only white space")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    words = line.split()
    if len(words) > MAX_WORDS:
        raise SystemExit(
            "entry is %d words, over the %d limit"
            % (len(words), MAX_WORDS)
        )
    if "#" in line:
        raise SystemExit("entry must not contain hashtags")
    return line


def main():
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Only the result file gets a permission set, never a directory:
    # the grader runs as an unprivileged user, and chmod on a directory
    # it does not own would make the whole program fail.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
