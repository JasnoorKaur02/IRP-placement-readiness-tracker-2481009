# Placement Readiness Tracker

A Python command-line program that records practice-test scores, computes grades,
and identifies students who need extra practice. The five starting records use
fictional names, IDs, and scores. A sixth record is collected each time the
tracker runs. Scores are held in memory for that run.

## Run the tracker

Use Python 3. No packages are required.

```sh
python3 tracker.py
```

Enter a name, roll number and three integer scores from 0 to 100. Grades use
the raw average: A starts at 80, B at 60, C at 40, and averages under 40 are
flagged for extra practice.

Example: enter Anaya Verma, roll 006, and scores 93, 89 and 97. The final
section of the output is:

```text
Top scorer: Anaya Verma (93.00)
Extra practice (average below 40): Meera Sethi
Students needing practice: 1
```

## Run the runner-up program

Give the count on the first line and the scores on the second line. The program
prints the second-highest distinct score.

```sh
printf '6\n98 72 98 61 84 84\n' | python3 runner_up.py
```

Expected output: `84`.

## Inspect the Git history

```sh
git log --oneline --graph --all
```

The grading functions and results table were developed on `feature-grades`
and merged into `main`.

AI assistance: OpenAI Codex helped implement, test, document, and prepare this worked project.
