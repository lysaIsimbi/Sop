# Nest and Stage Empty Totes SOP (1x Episode: 10 Totes)

One episode clears, nests, stages, and straps **ten empty totes**. The ten totes stand upright in the
**supply grid** when recording starts, each with one old **label** stuck to its front wall.
Every tote is moved one at a time to the **work spot** in the middle, its label is peeled off and dropped in
the **scrap bin**, and the bare tote is nested onto the **stack** at the **nest spot**. When a stack holds five
totes it is carried to the **dolly** and set on the **deck**. Two stacks of five stand side by side against the
**back rail** as the **column**, and one **strap** goes across the front of the column and is pressed onto its
landing patch.

The order never changes for each tote: lift it to the work spot, peel the label, drop the label in the scrap
bin, nest it. **No tote is ever nested with a label still on it**, because once a tote is nested its front wall
cannot be reached. No stack is staged before it holds five totes. The second stack is not started until the
first stack is standing on the deck. The column is not strapped until both stacks have been read.

The right gripper does the primary work: it peels every label, drops every label in the scrap bin, nests every
tote onto the stack, and lays and presses the strap. The left gripper supports: it lifts each tote out of the
supply grid onto the work spot, holds the stack steady while the right gripper lowers a tote into it, and
presses the column back against the back rail while the strap is drawn. Both grippers take one side wall each
of a finished stack for the carry to the dolly — that carry is the only time the left gripper goes to the deck.

The dolly never moves. Its brake stays set for the whole episode. Nothing is taken back out of a stack once it
is nested, and nothing is taken back off the deck once it is staged.

The table is set up in one of three ways. Only the **supply grid** moves; the work spot, the nest spot, the
scrap bin, the dolly, and the strap home are in the same place in all three.

* **Config L1:** the supply grid is at the back-left.
* **Config L2:** the supply grid is at the front-left, left of the scrap bin.
* **Config M:** the supply grid is at the back-center, behind the work spot and the nest spot.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the supply grid is at the back-left (**Config L1**), the front-left (**Config L2**), or
  the back-center (**Config M**). One config per episode, chosen before recording and never changed
  mid-episode.
* **Same-side rule:** the **left gripper** takes every tote out of the supply grid in all three configs — the
  grid is on the left or in the center, never on the right. No arm reaches across the table and nothing is
  handed over.
* **Fixed roles:** the right side of the table is taken by the nest spot, the dolly, and the strap home, so no
  start zone is on the right and the right gripper never takes a tote out of the grid. In every config the
  right gripper peels, nests, and straps, the left gripper feeds the work spot and steadies, and both grippers
  carry each stack. The grid's two rows, its outline order 1 to 10, and every front wall facing the front edge
  are the same in all three.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the supply grid in the start zone for this episode's config
   with the other two start zones bare, the work spot in the middle, the nest spot just right of the work spot,
   the scrap bin at the front-center, and the dolly on the right side with its deck and its back rail.
3. The **front wall of every tote in the supply grid** is readable in frame, so a label still stuck on a wall can
   be seen from the recording.
4. The **nest spot is visible from the side**, so the **rim lines** of a stack can be counted from the recording.
5. The **deck of the dolly is visible from the side and from above**, so both stacks, the back rail, and the
   strap can be seen.
6. Both arms are at home with grippers open.
7. The table is bare apart from the ten totes, the supply grid outlines, the work spot outline, the nest spot
   outline, the scrap bin, the dolly, the strap, and robot hardware.
8. The **left arm** reaches every one of the ten supply outlines (in all three configs), the work spot, and the
   nest spot without stretching or leaning out. The left arm reaches the deck only for the stack carry and the
   rail press.
9. The **right arm** reaches the work spot, the scrap bin, the nest spot, both deck outlines, the strap home, and
   the landing patch on the right post without stretching or leaning out.
10. The travel from the nest spot to the deck is bare and level, with nothing standing in it.

### Materials checklist

1. **Ten totes**, all identical, open-top, upright, empty, and dry. The walls taper inward toward the base so
   one tote drops down inside another and seats. Each tote is small enough for one gripper to close across a
   side wall, and light enough that two grippers lift a nest of five.
2. Each tote stands in its own **printed outline** in the **supply grid**: a back row of five and a front row of
   five, laid at the start zone for this episode's config, with the other two start zones bare:
   * **Config L1:** back-left
   * **Config L2:** front-left, left of the scrap bin
   * **Config M:** back-center, behind the work spot and the nest spot, clear of the dolly

   Every tote sits square in its outline with its **front wall facing the front edge**. No tote is nested in
   another and no tote touches its neighbor.
3. The supply outlines are numbered **1 to 5 left to right along the back row**, then **6 to 10 left to right
   along the front row**. The numbers are readable in frame.
4. Each tote carries exactly one **label** stuck flat on the outside of its **front wall**, with its **near
   corner lifted free of the wall** so a gripper pinches it without scraping the wall. Labels are printed side
   out, none torn, none folded over on itself.
5. One **work spot**, a printed outline in the middle of the table, bare and dry. It is wide enough for one tote
   with clear table on all four sides.
6. One **nest spot**, a printed outline just right of the work spot, bare and dry, with clear table around it so
   a stack is reached from the side.
7. One **scrap bin**, open-top and empty, at the front-center of the table in front of the work spot. Its mouth
   is wide and its walls are low enough that a gripper clears them going in and out.
8. One **dolly** on the right side of the table, standing square in its printed outline with its **brake set**.
   It does not roll, slide, or rock when pushed by hand.
9. The dolly carries a flat **deck** with two printed outlines on it, a **deck left outline** and a **deck right
   outline**, side by side and touching. The deck is bare, dry, and level.
10. An upright **back rail** runs along the back of the deck, tall enough that a stack of five leans back
    against it and stops.
11. A **left post** and a **right post** stand at the two ends of the deck, clear of both deck outlines.
12. One **strap**, a flat webbing band. Its **fixed end** is already anchored to the **left post** and is never
    unhooked. Its **free end** carries a stiff **pull tab** and a **hook patch** on its underside. The free end
    lies flat on the table just in front of the dolly at the **strap home**, printed side up, pull tab toward
    the front edge, with no part of it on the deck.
13. The **right post** carries a **landing patch**, a flat pad that the strap's hook patch grips when it is
    pressed onto it. The landing patch is clean and clear of loose fibre.
14. Before collection, confirm by hand that:
    - each of the ten totes lifts out of its outline without bringing a second tote with it;
    - one tote lowered into another seats all the way down and its **rim line** shows clearly from the side;
    - a nest of five lifts clear by the **bottom tote's** two side walls without any tote sliding out;
    - every label peels off its wall in one piece from its lifted corner and leaves no paper behind;
    - a stack of five stands against the back rail without leaning forward when it is released;
    - the strap reaches from the left post across the front of both stacks to the landing patch, and its hook
      patch holds when it is pressed down.

### Workspace layout

* **Supply grid:** ten printed outlines in two rows of five, at the back-left (**Config L1**), the front-left
  (**Config L2**), or the back-center (**Config M**). All ten totes start here and the grid is bare when the
  episode ends. Only the left gripper works here.
* **Work spot:** the middle of the table. Every label is peeled here. It holds one tote at a time and it is bare
  at the start and at the end. Both grippers work here.
* **Nest spot:** just right of the work spot. Each stack is built here and it is bare between stacks and at the
  end. The right gripper nests here and the left gripper steadies here.
* **Scrap bin:** the front-center, in front of the work spot. Every peeled label goes in here. Only the right
  gripper works here.
* **Dolly:** the right side of the table, in its printed outline, brake set. Its **deck** carries the deck left
  outline and the deck right outline, its **back rail** runs along the back of the deck, and its **left post**
  and **right post** stand at the two ends.
* **Strap home:** the table just in front of the dolly, clear of the deck. The strap's free end lies here at the
  start of the episode.
* The left arm's zones are the supply grid (in all three configs), the work spot, and the nest spot. The right
  arm's zones are the work spot, the scrap bin, the nest spot, the deck, the strap home, and the landing patch.
  The work spot and the nest spot are shared. The left gripper enters the deck only in Step 5 and Step 8.

### Arm assignments

* **Right gripper:** peels every label off its wall, carries every label to the scrap bin, lifts every bare tote
  off the work spot and nests it onto the stack, takes the right side wall of a finished stack for the carry,
  and takes, draws, and presses the strap. Its work is the same in all three configs.
* **Left gripper:** lifts every tote out of the supply grid — from the back-left in Config L1, the front-left in
  Config L2, or the back-center in Config M — and sets it on the work spot, holds the stack's bottom tote down
  while the right gripper lowers a tote into it, takes the left side wall of a finished stack
  for the carry, and presses the top of the column back against the back rail while the strap is drawn.

## Vocabulary

* **Tote:** one empty open-top box from the supply grid. All ten are identical, so any tote satisfies any place
  in a stack.
* **Start zone:** where the supply grid stands at the start of the episode — back-left (**Config L1**),
  front-left (**Config L2**), or back-center (**Config M**). One per episode, chosen before recording and never
  changed mid-episode. The zone is bare when the episode ends.
* **Label:** the old printed sticker on the outside of a tote's front wall. It has one **lifted corner** — a
  near corner already peeled free of the wall — which is the only part a gripper pinches. Every label goes in
  the scrap bin and nowhere else.
* **Bare wall:** a tote's front wall with no paper on it — no label, no torn half, no strip left along an edge,
  and no glue lump standing proud enough to catch a fingernail.
* **Nest:** lowering one tote straight down inside the tote below it until it stops going down on its own. A
  tote is nested only when it is **seated**.
* **Seated:** the tote has stopped going down, sits level, and its rim runs parallel to the rim below it with an
  even gap all the way round. A tote that rides high on one side, sits cocked, or rocks when the gripper opens
  is **not** seated.
* **Rim line:** the visible step at the rim of each tote in a nest, seen from the side. A stack of five shows
  five rim lines, so the count is read from the recording without touching the stack.
* **Stack:** the totes nested together at the nest spot. The **bottom tote** is the outermost one, standing on
  the table; every later tote goes down inside it. A stack is finished when it holds five totes.
* **Stage:** carrying a finished stack of five from the nest spot to its outline on the dolly deck and setting it
  down against the back rail.
* **Stack grasp:** the **bottom tote's two side walls**, taken just below the rim, one gripper on each side. It
  is the only grasp used for a stack. Taking any other tote of the stack lifts that tote alone and leaves the
  rest behind.
* **Deck:** the flat top of the dolly. It carries the **deck left outline** and the **deck right outline**, side
  by side and touching.
* **Back rail:** the upright along the back of the deck. Every staged stack stands leaning back against it.
* **Column:** the two stacks of five standing side by side on the deck, both square in their outlines, both back
  against the back rail, and their side walls touching each other. The column is what the strap holds.
* **Strap:** the flat webbing band across the front of the column. Its **fixed end** stays anchored to the left
  post all episode. Its **free end** carries the **pull tab**, which is the only part a gripper takes, and a
  **hook patch** underneath, which grips the **landing patch** on the right post when it is pressed onto it.
* **Taut:** the strap lies against the front walls of both stacks along its whole length, with no loop, sag, or
  daylight between the strap and either stack.
* **Lift:** taking a tote or a stack straight down onto its grasp, closing, and raising it straight up until
  there is daylight under it, before anything moves sideways.
* **Lower in:** carrying a tote level over the stack, lowering it straight down until it is seated, and
  releasing once it has stopped moving. A tote is never dropped in from above the rim.
* **Settled:** the thing stays put for 2 seconds after the gripper lifts clear, with nothing rocking, sliding,
  tipping, or leaning further.
* **Read hold:** both grippers clear of the deck and out of the way, the whole column and both posts in frame,
  held still for 2 seconds so the rim lines of both stacks can be counted from the recording.
* **Release point:** over the work spot, over the scrap bin, over the stack, or over the deck outline the thing
  in the gripper is going to. A gripper opens nowhere else.

## Steps

Steps 1 to 4 are one tote and run ten times. Step 5 stages a finished stack and runs twice. Every tote is lifted
straight up and carried in the upright position it will be set down in. No tote is ever turned over.

Only Step 1 depends on where the supply grid is: the **left gripper** takes each tote from the back-left in
Config L1, from the front-left in Config L2, or from the back-center in Config M, and carries it to the work
spot. Every other line of Steps 1 to 9 is the same in all three configs.

### Step 1: Move one tote to the work spot

**Goal:** one tote standing square on the work spot with its front wall facing the front edge, and its supply
outline bare.

Look where the supply grid is before reaching for the first tote.

* **IF the supply grid is at the back-left (Config L1):** the **left gripper** closes across one **side wall**
  of the next tote, lifts it straight up until there is daylight under it, and carries it level forward and to
  the right to the **work spot**.
* **IF the supply grid is at the front-left (Config L2):** the **left gripper** closes across one **side wall**
  of the next tote, lifts it straight up until there is daylight under it, and carries it level back and to the
  right to the **work spot**, clear of the scrap bin.
* **IF the supply grid is at the back-center (Config M):** the **left gripper** closes across one **side wall**
  of the next tote, lifts it straight up until there is daylight under it, and carries it level straight forward
  to the **work spot**.

Then, in all three:

* Lower the tote until it is standing on the table on the work spot, and release.
* Take the totes in outline order: **1 to 5 left to right along the back row, then 6 to 10 left to right along
  the front row**. Never skip an outline and never come back for one.
* Take one tote at a time. Never close the gripper across two totes and never lift a tote that has a second one
  hanging on it.

The tote goes down with its **front wall facing the front edge**, the same way it stood in the grid. Never turn
it on the way over and never set it down on its side.

**Check:** one tote stands square on the work spot, upright, front wall toward the front edge, label still on it,
and its supply outline is bare. If a second tote came up with the first, put the second one back in its own
outline before going on.

### Step 2: Clear the label

**Goal:** the tote's front wall bare and the label in the scrap bin.

* The **right gripper** pinches the **lifted corner** of the label.
* Pull the label off the wall in one steady peel along the wall, keeping the gripper close to the wall so the
  label rolls off rather than tearing across.
* The **right gripper** carries the label level to the **scrap bin**, lowers it inside the mouth, and releases.
* Peel every label at the work spot. Never peel a label while the tote is still in the supply grid, on the nest
  spot, or on the deck.

**Check:** the tote's front wall is **bare** — no label, no torn half, no strip along an edge — and the scrap bin
holds the label. If a piece of the label stays on the wall, pinch that piece with the **right gripper** and peel
it off the same way before going on. If the label falls short of the bin, pick it up with the **right gripper**
and put it in the bin before going on.

### Step 3: Nest the tote onto the stack

**Goal:** the tote seated on the stack at the nest spot.

**3.1 The first tote of a stack**

* The **right gripper** closes across one **side wall** of the bare tote on the work spot, lifts it straight up,
  carries it level to the **nest spot**, lowers it until it is standing square in the outline, and releases.
* This tote is the **bottom tote**. It stands on the table and everything else goes down inside it.

**3.2 The second to the fifth tote of a stack**

* The **left gripper** comes down on the rim of the stack's **bottom tote** and holds it down against the table,
  so the stack cannot slide or tip while a tote goes in.
* The **right gripper** closes across one **side wall** of the bare tote on the work spot, lifts it straight up,
  carries it level over the stack, and **lowers it straight down inside** the tote below until it stops going
  down on its own.
* Release once the tote is **seated** and has stopped moving. Then the **left gripper** lifts clear of the rim.
* Let the tote find its own seat. Never press, tap, or hammer a tote down to make it seat.

**Check:** the tote is seated — level, its rim parallel to the rim below with an even gap all the way round,
nothing rocking when the grippers lift clear — and its front wall faces the front edge like the ones below it.
If the tote rides high, sits cocked, or rocks, lift it straight back out with the **right gripper** and lower it
in again.

**Expected state:** the stack shows one rim line for every tote in it, counted from the side.

### Step 4: Clear the work spot and take the next tote

**Goal:** the work spot bare and the next move chosen.

* Confirm the **work spot is bare** — no tote, no label, no torn paper.
* Count the **rim lines** on the stack at the nest spot.
* If the stack holds **fewer than five** totes, go back to **Step 1** and take the next tote in outline order.
* If the stack holds **five** totes, go on to **Step 5**.

**Check:** the work spot is bare and the rim line count matches the number of totes nested so far. If a label or
a torn piece is still on the work spot, put it in the scrap bin with the **right gripper** before going on.

### Step 5: Stage the stack to the dolly

**Goal:** the stack of five standing square in its deck outline, back against the back rail.

* The **left gripper** closes across the **left side wall** of the stack's **bottom tote**, just below the rim,
  and the **right gripper** closes across the **right side wall** of the same **bottom tote**, just below the
  rim. This is the **stack grasp**. Never lift a stack by any other tote and never lift it by a rim alone.
* Both grippers raise the stack straight up together until there is daylight under it, keeping the stack level
  and upright.
* Both grippers carry the stack level to the **deck** and lower it straight down into its outline until it is
  standing on the deck, then slide it back until it touches the **back rail**, and release.
* The **first stack** goes in the **deck left outline**. The **second stack** goes in the **deck right outline**,
  set down so its side wall **touches** the first stack.
* Keep the stack upright and square the whole way. Never tilt it, never turn it, and never take a new hold in the
  air — if the grasp slips, lower the stack back onto the table, release, and take the stack grasp again.

**Check:** the stack stands square in its deck outline, upright, back against the back rail, showing five rim
lines from the side, with no tote lifted out of the nest by the carry. The nest spot is bare. If the stack is
leaning forward, off its outline, or clear of the rail, take the **stack grasp** again, lift it straight up, and
set it down again.

**Expected state:** after the first stack, the deck left outline is filled and the deck right outline is bare.
After the second stack, both outlines are filled and the two stacks touch.

### Step 6: Start the next stack or move on

**Goal:** the next move chosen.

* Look at the **supply grid**.
* If the grid **still holds totes**, go back to **Step 1** and build the second stack the same way.
* If the grid is **bare**, go on to **Step 7**.

Never start the second stack before the first stack is standing on the deck. Only one stack is at the nest spot
at a time.

**Check:** the nest spot is bare, the work spot is bare, and either the supply grid still holds totes or it is
bare down to its outlines.

### Step 7: Read the column

**Goal:** both stacks counted and standing as the column before anything is strapped.

* Hold both grippers clear of the deck for the **read hold**, with the whole column and both posts in frame.
* Count the **rim lines** on the left stack and on the right stack. Each must show **five**.
* Confirm both stacks stand square in their outlines, both back against the back rail, and their side walls
  touching each other.

If either stack shows a number of rim lines other than five, or a tote is still in the supply grid, on the work
spot, or on the nest spot, end the episode as a **count mismatch** (see Non-violation failures). Do not add a
tote to a staged stack and do not take one off.

**Check:** ten rim lines across the two stacks, five and five, both stacks square, back against the rail, and
touching, and the supply grid, work spot, and nest spot all bare.

### Step 8: Strap the column

**Goal:** one strap taut across the front of the column with its hook patch pressed onto the landing patch.

* The **left gripper** comes down on the **top rim of the left stack** and presses it back against the **back
  rail**, holding the column steady while the strap is drawn.
* The **right gripper** pinches the strap's **pull tab** at the **strap home**, lifts the free end straight up,
  and carries it to the **left post** end of the column.
* Draw the free end level across the **front walls of both stacks**, keeping the strap flat and untwisted, at a
  height **above the middle of the column and below its top rim**.
* Pull the free end on toward the **right post** until the strap is **taut** — lying against the front walls of
  both stacks with no loop, sag, or daylight behind it.
* Lay the free end's **hook patch** flat onto the **landing patch** on the right post and press it down for
  **2 seconds** with the **right gripper**, then lift the gripper straight up clear of it.
* The **left gripper** lifts clear of the top rim last, after the patch is pressed.
* Never let the free end drag across the deck or across the top of the column, and never take the strap by
  anything but its pull tab.

**Check:** the strap runs in one straight flat line from the left post across the front of both stacks to the
landing patch, with no twist and no sag, above the middle of the column and below its top rim, and the hook
patch sits fully on the landing patch with no corner hanging off. The column is still square, back against the
rail, and the two stacks are still touching.

If the strap sags, is twisted, misses a stack, or the patch hangs off its landing patch, peel the free end off
the landing patch with the **right gripper**, draw it again, and press it down again.

**Expected state:** the strap holds the column back against the rail and does not lift away when the grippers
are clear.

### Step 9: Confirm the load and end the episode

* Confirm the deck holds two stacks of five standing square in their outlines, back against the back rail and
  touching each other, with the strap taut across the front of both and its hook patch pressed onto the landing
  patch.
* Confirm the supply grid, the work spot, and the nest spot are bare, the scrap bin holds ten labels, and the
  dolly is still square in its outline with its brake set.
* Return both arms home, clear of the deck, the nest spot, and the scrap bin, then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

### After each episode

1. Peel the strap's free end off the **landing patch** and lay it flat at the **strap home**, printed side up
   with its pull tab toward the front edge and no part of it on the deck. Leave the fixed end anchored to the
   left post.
2. Take both stacks off the deck, un-nest all ten totes, and set the deck bare.
3. Empty the **scrap bin** of the ten peeled labels and set it back at the front-center, empty.
4. Stick one fresh **label** on the outside of each tote's front wall, printed side out, flat, with its **near
   corner lifted free of the wall**. Replace any label that will not lie flat or whose corner will not stay
   lifted.
5. Wipe any glue left on a tote's front wall so the wall is bare before the next label goes on.
6. Stand all ten totes back in the **supply grid**, laid at the start zone for the next episode's config —
   back-left (Config L1), front-left (Config L2), or back-center (Config M) — one to an outline, upright,
   square, front wall facing the front edge, none nested and none touching a neighbor. The other two start
   zones are bare.
7. Vary which tote goes in which outline between episodes rather than rebuilding the same order every time. The
   count stays at ten totes in ten outlines.
8. Check the **dolly**: square in its outline, brake set, and it does not roll, slide, or rock when pushed by
   hand. Reset the brake if it has loosened.
9. Confirm the **deck** is bare and dry, the **back rail** is upright and firm, and both posts stand square.

### At the end of the session

1. Check every tote: replace one that is cracked, split, warped, or that no longer seats all the way down
   inside another, and one whose rim will not sit level in a nest.
2. Check the **strap**: replace one that is frayed, stretched so it no longer pulls taut across the column, or
   whose hook patch no longer holds when it is pressed onto the landing patch.
3. Check the **landing patch**: clear it of loose fibre and replace it if it no longer grips the hook patch.
4. Check the **printed outlines** of the supply grid, the work spot, the nest spot, and the two deck outlines.
   Replace any that has lifted, torn, or gone unreadable in frame.
5. Wipe the table and the deck and confirm both are dry and bare. A slick or dusty deck lets a staged stack
   slide off its outline.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue
is what the reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just
because a rule was broken.

### Violations

**Note on the start position:** the violations below were written for Config L1 (supply grid at the back-left).
The pickup and arm-role cues will be rewritten later to cover all three start positions; they are left as they
are for now. Until then, anything that does not match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the operator does does not match the config on the table — the supply grid is not in
  the start zone for the config; a gripper reaches across the table for a tote; or the wrong IF line is
  followed.
* **SOP rule broken:** the start position and the same-side rule (the left gripper takes every tote out of the
  supply grid in all three configs, no arm reaches across the table, and the IF line followed is the one for
  the config on the table).
* **Coaching note:** look where the supply grid is before the first reach, then follow that config's IF line
  through Step 1.

**Violation: Wrong order of work**

* **Visible cue:** a tote is nested before its label is off, a stack is carried to the deck before it holds five
  totes, a tote is taken for the second stack before the first stack is standing on the deck, or the strap is
  taken up before the read hold on the column.
* **SOP rule broken:** Steps 1 to 8, the order never changes.
* **Coaching note:** finish the step you are in before you start the next one.

**Violation: Wrong arm used**

* **Visible cue:** the right gripper takes a tote out of the supply grid; the left gripper peels a label, carries
  a label, reaches the scrap bin, nests a tote onto the stack, or touches the strap; or the left gripper goes to
  the deck for anything other than the stack carry in Step 5 and the rail press in Step 8.
* **SOP rule broken:** Steps 1 to 8, the left gripper feeds the work spot and steadies, the right gripper peels,
  nests, and straps.
* **Coaching note:** left arm feeds and holds. Right arm does the work.

**Violation: More than one tote taken, or taken out of order**

* **Visible cue:** the left gripper closes across two totes at once, a second tote comes up hanging on the first
  and is carried anyway, an outline in the supply grid is skipped, or a skipped outline is picked up later.
* **SOP rule broken:** Step 1, one tote at a time, in outline order 1 to 10.
* **Coaching note:** one tote, in order, every time. Put a passenger back before you carry.

**Violation: Tote dragged instead of lifted**

* **Visible cue:** a tote slides along the table, the deck, or the rim of the tote below it, still touching, with
  no daylight under it in transit.
* **SOP rule broken:** Steps 1, 3, and 5, lift straight up until there is daylight before moving sideways.
* **Coaching note:** the lift is its own motion, not the start of the carry.

**Violation: Label peeled away from the work spot**

* **Visible cue:** the right gripper peels a label while the tote is still in the supply grid, standing on the
  nest spot, already nested on a stack, or on the deck.
* **SOP rule broken:** Step 2, every label is peeled at the work spot.
* **Coaching note:** the label comes off in the middle of the table, nowhere else.

**Violation: Label left on the wall**

* **Visible cue:** the tote leaves the work spot with the label still on it, with a torn half stuck to the wall,
  or with a strip left along an edge; or the label is torn across instead of rolled off from its lifted corner.
* **SOP rule broken:** Step 2, the tote's front wall is bare before it leaves the work spot.
* **Coaching note:** pinch the lifted corner and peel along the wall. Bare wall or peel again.

**Violation: Label not put in the scrap bin**

* **Visible cue:** a peeled label is dropped on the table, dropped into a tote, laid on the deck, released above
  the bin so it lands outside, or carried on into the next step still in the gripper.
* **SOP rule broken:** Step 2, every label goes inside the mouth of the scrap bin.
* **Coaching note:** the label has one destination. Take it all the way in.

**Violation: Tote nested with its label still on**

* **Visible cue:** a tote goes down into the stack with paper still on its front wall, or a stack on the deck
  shows a label between its rim lines.
* **SOP rule broken:** Steps 2 and 3, no tote is nested until its wall is bare.
* **Coaching note:** once it is nested you cannot reach the wall. Clear it first, every time.

**Violation: Work spot not cleared**

* **Visible cue:** the next tote is set on the work spot while a label, a torn piece, or the previous tote is
  still there; or the episode goes on with something left on the work spot.
* **SOP rule broken:** Step 4, the work spot is bare before the next tote comes over.
* **Coaching note:** clear the spot before you fill it again.

**Violation: Tote dropped in instead of lowered**

* **Visible cue:** the right gripper opens above the rim of the stack and the tote falls the rest of the way in,
  or the tote is released before it has stopped going down.
* **SOP rule broken:** Step 3.2, lower straight down until it is seated and release only once it has stopped
  moving.
* **Coaching note:** take it all the way down before you open the gripper.

**Violation: Tote not seated, or forced down**

* **Visible cue:** the episode goes on with a tote riding high on one side, sitting cocked, rocking after the
  gripper lifts clear, or with an uneven gap between its rim and the rim below; or a gripper presses, taps,
  pushes, or hammers a tote down to make it seat, or holds a tote down after it has already stopped going down.
* **SOP rule broken:** Step 3.2, lower the tote until it stops going down on its own, let it find its own seat,
  and a tote is nested only when it is seated.
* **Coaching note:** lower it and let go. If it will not seat, lift it straight back out and lower it in again.

**Violation: Stack not steadied while a tote goes in**

* **Visible cue:** the right gripper lowers a tote into the stack with the left gripper away from the bottom
  tote's rim, or the stack slides, turns, or tips during a lower in.
* **SOP rule broken:** Step 3.2, the left gripper holds the bottom tote down against the table while a tote goes
  in.
* **Coaching note:** hold the bottom before you fill the top.

**Violation: Stack staged with the wrong number of totes**

* **Visible cue:** a stack is carried to the deck showing four rim lines or six, or a stack is staged without the
  rim lines being counted at the nest spot.
* **SOP rule broken:** Steps 4 and 5, a stack is staged only when it holds five totes.
* **Coaching note:** count the rim lines before you lift.

**Violation: Stack lifted by the wrong tote**

* **Visible cue:** a gripper takes the top tote, a middle tote, or a rim alone to lift a stack, and the rest of
  the nest is left behind or slips out during the lift.
* **SOP rule broken:** Step 5, both grippers take the bottom tote's two side walls just below the rim.
* **Coaching note:** the bottom tote carries the whole nest. Take it there.

**Violation: Stack tilted, turned, or regripped in the carry**

* **Visible cue:** the stack leans, turns, or swings during the carry, a tote slides within the nest, or a
  gripper shifts or re-seats its hold on the stack in the air instead of setting it down first.
* **SOP rule broken:** Step 5, keep the stack upright and square the whole way, and set it down before taking a
  new hold.
* **Coaching note:** level all the way across. Put it down before you take a new hold.

**Violation: Stack set down wrong on the deck**

* **Visible cue:** a stack stands off its deck outline, in the wrong outline, clear of the back rail, leaning
  forward, or with a gap between it and the other stack.
* **SOP rule broken:** Step 5, the first stack goes in the deck left outline and the second in the deck right
  outline, both square, back against the rail, and touching.
* **Coaching note:** back to the rail, square in the outline, side by side.

**Violation: Column not read**

* **Visible cue:** the strap is taken up with no still hold on the column, the grippers stay over the deck
  through the hold so the rim lines cannot be counted, or a stack showing a number other than five rim lines is
  strapped anyway.
* **SOP rule broken:** Step 7, hold both grippers clear for 2 seconds with the whole column in frame and count
  five rim lines on each stack.
* **Coaching note:** stop, get clear, and let the count be seen before you strap.

**Violation: Tote added to or taken off a staged stack**

* **Visible cue:** a tote is lowered into a stack already standing on the deck, or a tote is lifted out of a
  staged stack, off the deck, or back to the nest spot.
* **SOP rule broken:** Steps 5 and 7, nothing is added to or taken off the deck once a stack is staged.
* **Coaching note:** the stack is finished at the nest spot. The deck is not a work spot.

**Violation: Dolly moved or its brake released**

* **Visible cue:** the dolly rolls, slides, turns, or rocks off its printed outline, a gripper leans on the deck
  or the back rail hard enough to shift it, or the brake is knocked off.
* **SOP rule broken:** Steps 5, 7, and 8, the dolly stays square in its outline with its brake set for the whole
  episode.
* **Coaching note:** the dolly does not move. Only what goes on it does.

**Violation: Fixture knocked off its spot**

* **Visible cue:** the scrap bin is pushed, dragged, or tipped; a supply grid outline, the work spot, or the nest
  spot is covered by something that does not belong there; or a post or the back rail is knocked out of square.
* **SOP rule broken:** Steps 1 to 8, every fixture stays where it is set.
* **Coaching note:** work around the fixtures. They do not move.

**Violation: Strap laid wrong across the column**

* **Visible cue:** the strap is taken by anything but its pull tab, is dragged across the deck or over the top of
  the column, lands twisted, crosses only one stack, or sits above the top rim or below the middle of the
  column.
* **SOP rule broken:** Step 8, take the pull tab and draw the strap flat and untwisted across the front walls of
  both stacks, above the middle and below the top rim.
* **Coaching note:** tab in hand, flat across both fronts, one clean line.

**Violation: Strap left slack**

* **Visible cue:** the strap sags, loops, or shows daylight behind it against either stack, or the column leans
  forward off the rail once the grippers are clear.
* **SOP rule broken:** Step 8, pull the free end until the strap is taut against the front walls of both stacks.
* **Coaching note:** pull it in before you press it down.

**Violation: Strap patch not pressed or not checked**

* **Visible cue:** the hook patch is laid on the landing patch without the 2 second press, hangs off the edge of
  the landing patch, or lifts away after the gripper is clear, and the episode goes on.
* **SOP rule broken:** Step 8, press the hook patch flat onto the landing patch for 2 seconds and confirm it
  holds.
* **Coaching note:** press it, then look at it. A patch that lifts is not a strap.

**Violation: Tote, stack, or strap dropped or knocked over**

* **Visible cue:** a tote falls to the table or the floor short of its spot, a stack topples or spills totes, a
  staged stack is struck and shifts off its outline, the strap's free end falls off the table, or the two arms
  strike each other.
* **SOP rule broken:** Steps 1 to 8, keep each thing on a clear travel path and release only after a settled
  placement.
* **Coaching note:** check the path and the landing spot before you move.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a tote still in the supply grid, on the work spot, or on the nest spot;
  a label outside the scrap bin; a stack off its deck outline or clear of the rail; the strap slack, unpressed,
  or still at the strap home; an arm away from home; or an arm still over the deck.
* **SOP rule broken:** Step 9, confirm the column and the strap, confirm the grid, work spot, and nest spot are
  bare, return both arms home clear of the scene, then stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never
use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Count mismatch:** the supply grid holds more or fewer than ten totes when the episode begins, or a tote is
  already nested in another. Discard the episode and restock the grid.
* **Defective tote:** a tote that is cracked, split, or warped, one that will not seat all the way down inside
  another, or one whose rim will not sit level in a nest. Replace it before the next episode.
* **Nest binds:** two totes jam together so the nest cannot be un-nested by hand at reset. Replace the pair
  before the next episode.
* **Label fault:** a label that is missing when the step begins, has no lifted corner, is already torn, or that
  will not peel off its wall in one piece under a steady pull. Replace it before the next episode.
* **Strap fault:** the strap is frayed or stretched so it will not pull taut across the column, or its hook patch
  no longer holds when it is pressed onto a clean landing patch. Replace the strap before the next episode.
* **Landing patch worn:** the landing patch no longer grips a good hook patch. Replace it before the next
  episode.
* **Dolly fault:** the brake will not hold, or the dolly rolls, slides, or rocks under a correct set down.
  Replace or re-brake it before the next episode.
* **Stack slides on the deck** under a correct set down because the deck is slick, dusty, or damp. Wipe and dry
  the deck before the next episode.
* **Printed outline unreadable:** a supply grid outline, the work spot, the nest spot, or a deck outline has
  lifted, torn, or gone unreadable in frame. Replace it before the next episode.

## Annotation subtasks (from SOP)

1. Move one tote from the supply grid to the work spot
2. Peel one label off a tote and put it in the scrap bin
3. Nest one tote onto the stack at the nest spot
4. Stage one stack of five from the nest spot to the dolly deck
5. Read the column on the deck
6. Strap the column
7. Confirm the load and end the episode
