# HW 0 — Getting started

Work through `getting-started.ipynb`. It sets up your environment and walks through the
tools the course uses.

This assignment is checked for **completion only** — that you did it, not whether any
particular answer is right.

## How handing work in works, this term

Every assignment follows the same three steps, and this one is where you practise them.

1. **Accept the assignment** through the link posted in Canvas. That creates a private
   repository on GitHub that belongs to you. Nobody else in the class can see it.
2. **Clone it** to wherever you work, and do the assignment there:

   ```
   git clone https://github.com/osu-scicomp/<the repository you were given>.git
   ```
3. **Commit and push** when you are done, and any time along the way. Pushing early and
   often is a good habit, and there is no penalty for pushing work in progress.

Push your final state before the deadline. The last thing you push is what is read.

## Where to find your result

Most assignments run an automatic check when you push. **Its verdict is in your
repository's Releases tab, not the Actions tab.**

- **Releases** — one entry per push, newest first. Open the newest one: it lists which
  checks passed, and for anything that failed, the reason.
- **The mark beside your latest commit** — a green tick or a red cross, the same verdict
  at a glance.
- **A green check in the Actions tab does not mean you passed.** It only means the
  checker ran. The result is in the Release.

Those checks are a small part of the grade. They catch a number that came out wrong or a
notebook that was never run; they say nothing about the reasoning, which is what is
actually being assessed. **This assignment has no automatic check at all** — pushing your
completed notebook is the whole requirement.

There is also a pull request called **Feedback** sitting open in your repository. Leave
it alone: it is where comments on your work will appear.

## Signing in to Classroom 50

Accepting an assignment asks you to authorize Classroom 50, the tool this course uses to
hand out repositories. GitHub's permission system has no way to limit that request to one
organization, so what it asks for covers all of your repositories.

If you would rather grant less, use a **fine-grained personal access token** scoped to
`osu-scicomp` alone: on the sign-in card choose **Other sign-in methods**, then **Use a
personal access token (fine-grained)**. It is a few more clicks once, and nothing about
the course depends on which route you take.
