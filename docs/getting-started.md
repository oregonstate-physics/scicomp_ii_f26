# Git and GitHub, the parts this class uses

You do not need to be good at git to do well in this course. You need four commands
and one habit. This page covers those, and then explains the handful of terms you
will see on GitHub but never have to operate.

If you have never used git at all, start here and then do
[HW0](../homework/hw00-getting-started), which walks through the same steps with
your own repository in front of you.

## What these two things are

**Git** records the history of a folder. Every time you commit, it saves a snapshot
of what changed, who changed it, and when — so you can look back, compare, and
recover work you thought you had lost.

**GitHub** stores those histories on the internet and gives them a web page. It is
how I hand assignments to you and how you hand them back.

The two are separate. Git runs on your machine and works with no network at all;
GitHub is one of several places a git history can be sent.

## How work moves in this class

Every assignment follows the same path:

1. **Accept** the assignment from the link in Canvas. That creates a repository that
   belongs to you, private, visible to you and the teaching staff.
2. **Clone** it to wherever you work.
3. **Commit** as you go, and **push** when you have something worth keeping.

There is nothing to copy by hand, nothing to merge, and no second remote to keep in
step. Lecture notebooks live in a separate public repository you only ever pull from.

## The four commands

**Clone** — make a local copy. Once per repository:

```bash
git clone git@github.com:osu-scicomp/f26-hw01-yourusername.git
cd f26-hw01-yourusername
```

**Status** — what have I changed? Run it constantly; it is the cheapest way to know
where you are:

```bash
git status
```

**Commit** — save a snapshot. `add` chooses what goes in, `commit` records it:

```bash
git add hw01.ipynb answers.json
git commit -m "finished problem 2"
```

The message is for you, three weeks later. "finished problem 2" is a good message;
"update" is not.

**Push** — send your commits to GitHub:

```bash
git push
```

### The habit

**Push early and push often.** A commit that only exists on your laptop is not handed
in, and it is one spilled coffee from gone. Pushing unfinished work costs nothing and
carries no penalty.

The page on GitHub is the truth about what you submitted. When in doubt, open your
repository in a browser and look.

## Things you will see but do not have to do

- **Branches.** Parallel lines of work. You will stay on `main` all term. Worth
  knowing the word; you don't need to make one.
- **Pull requests.** A proposal to merge one branch into another, and the place code
  review happens in industry. Each of your assignment repositories has exactly one,
  called **Feedback**, opened automatically and left open. It is where comments on
  your work appear. Don't close it, and don't merge it.
- **Releases.** Ordinarily a way to publish a finished version of software. Here, the
  automatic checker posts each submission's result as a release, which is why your
  Releases tab is where you read your result.
- **Issues, stars, and the rest of GitHub's collaboration machinery.** Real, useful,
  and not used in this course.

## When something goes wrong

**"Permission denied (publickey)"** or a password prompt that never works. Your
authentication isn't set up. GitHub stopped accepting account passwords on the
command line in 2021: you need an SSH key or a personal access token. HW0 links both.

**"Updates were rejected because the remote contains work that you do not have."**
The copy on GitHub has a commit yours doesn't — usually because you edited the file
in the browser, or worked on two machines. Fix it with:

```bash
git pull --rebase
git push
```

**A merge conflict in a notebook.** Notebooks are JSON, so git's automatic merge often
can't resolve them and leaves `<<<<<<<` markers in the file, which makes it unopenable.
Avoid this by only ever editing a notebook in one place. If it happens, ask me —
don't spend an hour hand-editing JSON.

**You committed a huge file.** GitHub rejects anything over 100 MB, and deleting the
file in a later commit does not help, because it is still in the history. Ask rather
than fight it.

**You cannot find your repository.** Check
[github.com/osu-scicomp](https://github.com/osu-scicomp), or the accept link in
Canvas, which will take you to your existing repository if you already accepted.

## If you want to understand it properly

Optional, and none of it is required for this course:

- [The Pro Git book](https://git-scm.com/book/en/v2) — free, and the standard
  reference. Chapters 1–3 cover more than you will need here.
- [GitHub's git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
  — one page, worth printing.
- [Oh Shit, Git!?!](https://ohshitgit.com/) — how to get out of the common messes,
  written for exactly the moment you are in when you need it.
