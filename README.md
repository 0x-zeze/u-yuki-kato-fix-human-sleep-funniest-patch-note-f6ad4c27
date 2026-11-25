[![make.fun · u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/0x-zeze/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/0x-zeze/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

# Fix Human Sleep: Funniest Patch Note

Deterministic Python entry for the make.fun competition **Fix Human Sleep: Funniest Patch Note**. Running `python3 main.py` writes a single UTF-8 changelog line (1–160 characters) to `/output/entry.txt`.

## Entry

> Fixed: Sleeping a full 8 hours no longer leaves users groggier than a 2-hour nap; widened rest_hours from uint3 to uint8 so 8 stops wrapping to 0.

## How it was chosen

Five single-line patch notes were drafted with a three-beat structure (concrete sleep mechanism → escalation → deadpan system-artifact reversal), avoiding clichés and staying under 160 characters:

1. **146 chars (Winner):** `Fixed: Sleeping a full 8 hours no longer leaves users groggier than a 2-hour nap; widened rest_hours from uint3 to uint8 so 8 stops wrapping to 0.`
2. **151 chars:** `Fixed: Checking the clock at 03:14 no longer starts a recursive "if I sleep now" math loop until sunrise; revoked user read access to time until 06:30.`
3. **137 chars:** `Fixed: Sleeping motionless in bed no longer causes a 4-day neck injury from a 2-degree pillow shift; disabled ragdoll physics while idle.`
4. **156 chars:** `Fixed: Under-blanket overheating no longer deadlocks against exposed-limb frostbite; left foot is now hard-mounted outside the covers as a passive heatsink.`
5. **155 chars:** `Fixed: Bedtime shutdown no longer hangs trying to hotfix a 2011 "you too" to a waiter; stale regret processes now receive SIGKILL instead of 03:00 retries.`

**Why variant 1 won:** It fixes the core paradox of human sleep—getting the recommended 8 hours and waking up worse than after a 2-hour nap—with an exact, deadpan systems root cause (`uint3` holds `0..7`, so `8` wraps to `0`). Compared to the runner-ups, variant 2 leans on a quoted phrase and fixes clock visibility rather than rest itself, variant 3 hits neck posture rather than sleep quality, and variants 4 and 5 tread closer to familiar blanket-foot and 3 AM regret tropes. Variant 1 scores highest on authentic changelog voice, single-read click, and unexpected specificity.

## Usage

```bash
python3 main.py
```

Writes the 146-character UTF-8 entry plus a trailing newline to `/output/entry.txt`.
