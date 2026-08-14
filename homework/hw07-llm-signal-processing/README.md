# HW7 — Finding a signal you have not been told about

This assignment is about **using a large language model as a research tool, and checking
its work.** You will use one throughout, and you are expected to. What is being assessed is
not whether you can get code written — it is whether you can tell when the code is wrong.

There is a real signal buried in `data/search_data_01.fil`. Nobody is going to tell you what
it is. If your analysis is correct you will find it, and the physics will confirm it.

## What you hand in

1. **The completed notebook**, `notebooks/hw07.ipynb`.
2. **A prompt log** — every prompt you sent, in order, with the model named. Copy them into
   the notebook section provided. Do not clean them up; the false starts are the interesting
   part.
3. **A short write-up** (Canvas) — see *What is being graded* below.

## Part 0 — Find the bug yourself, then ask

The notebook contains a function that finds the dominant frequency in a signal. It runs
without error. It is wrong.

**Do this in order. The order is the point.**

1. Read the code and **write down what you think it will output** for a signal whose
   frequency you already know. Commit to a number before running anything.
2. Run it. Compare.
3. Find the bug **by hand** — no LLM yet. Fix it.
4. *Now* give the original buggy function to an LLM and ask it to find the problem.
5. Compare: did it find the same bug? A different one? Did it invent a problem that was not
   there? Was its explanation correct even when its fix was?

You will be asked what you got wrong at step 1 and why you think you missed it. **An honest
answer here is worth more than a clean one** — "I assumed the frequency axis was fine because
the plot looked reasonable" is exactly the kind of observation this assignment is about.

## Part 1 — Learn something niche, with help

Your data is *dispersed*: the signal arrives at different times in different frequency
channels, because the interstellar medium is not empty. Until you correct for that, the
signal is smeared out and invisible.

Use an LLM to teach yourself about **dispersion and dedispersion**. Then, in the notebook:

- Explain in your own words what causes the delay, and how it scales with frequency.
- Write down the delay equation, and say where each constant comes from.
- **Verify at least one claim the model made against an independent source** — a textbook,
  a paper, lecture notes, anything not the model. Say what you checked and what you found.

An LLM will state the dispersion constant confidently. Confirm it, and note its units.

## Part 2 — Build the analysis

Use the LLM to help you write code that:

1. **Reads the file.** It is SIGPROC filterbank format: a header of length-prefixed
   key/value pairs, then raw samples. *Sanity check: a correct parser reports 96 frequency
   channels and a sampling time of 72 µs.* If you get something else, your parser is wrong.
2. **Dedisperses** the data over a range of trial dispersion measures.
3. **Searches for periodicity** in each dedispersed time series.
4. **Folds** the data at your best candidate to confirm it.

You have written most of these pieces before, in other forms. What you already have in the
course notebooks is fair game and probably better suited to this data than something written
from scratch.

## Part 3 — Report what you found

State your best estimate of the **dispersion measure** and the **period**, with an honest
uncertainty on each. Show the evidence: the periodogram, the DM search, the folded profile.

## Part 4 — Check it against physics the analysis never saw

Anyone can produce a number. Now find out whether it is right.

The source is real and catalogued. **Your two measured numbers are enough to identify it.**
Search a pulsar catalogue — the ATNF catalogue is the standard one — for an object matching
your period and dispersion measure.

- Did you find it? What is it?
- How well do your measurements agree with the published values?
- If they disagree, by how much, and in which direction? **Is the disagreement larger than
  your uncertainty?** If so, something is unmodelled — what?

That last question has a real answer, and finding it is worth more than getting the period
right in the first place.

## What is being graded

**Not the code.** The model can write code. The assessment is:

| | |
|---|---|
| **Part 0 reflection** | Did you predict before running? What did you miss, and why? |
| **The prompt log** | How did you steer the model? What did you do when it was wrong? |
| **Verification** | Every claim you accepted — how did you check it? |
| **Part 4** | Does your answer survive contact with an independent source? |

A notebook that finds the signal with no account of how you checked anything is worth less
than one that misses it but shows exactly where the analysis broke and how you know.

**One rule:** do not ask the model to verify its own output. If it writes the dedispersion
code, it does not get to be the thing that tells you the dedispersion is right. That is what
Part 4 is for.

## Data

`data/search_data_01.fil` — 38.2 s of radio telescope data, 96 frequency channels across
1352.5–1447.5 MHz, 72 µs sampling. Provenance is deliberately withheld until after the
assignment; knowing where it came from would tell you what is in it.

## Graduate Students

1. Your period was measured from a telescope on a moving Earth. Estimate the size of that
   effect for this observation and correct for it. Does the agreement improve?
2. A dedispersion search over a fine DM grid is expensive. What sets the *necessary* DM
   spacing — how far can two trial DMs be apart before you would miss the signal? Derive it
   from the observation's parameters rather than looking it up, then compare.
3. Real pulse profiles are not sinusoidal, so a periodicity search misses power spread into
   harmonics. Describe what you would do about that, and if you can, do it.
