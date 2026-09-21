# Consolidate Two Partial Bins SOP (1x Episode: 2 Bins)

One episode consolidates one pair of partial bins: both bins are counted, everything is moved into one bin,
the merged count is verified, both bins are relabelled, the emptied bin is flagged **EMPTY**, and the bin card
is updated. The table begins with two open-top **bins** standing rim to rim, square to the front edge, with a
small even gap between their rims. The **keep bin** sits on the **keep spot**, just right of the center of the
table, and its front rail is printed **B**. The **source bin** sits on the **source spot**, beside the keep bin
on the side the config sets, and its front rail is printed **A**. Both bins hold the same part type, **hex nuts**,
and both are part full.

Each bin has a **label window** on its front rail that holds one upright card. Bin A starts with the count
label **5** in its window; bin B starts with the count label **6**. A **label rack** at the **front-right**
holds count labels **1** through **12**, each standing in its own numbered slot, plus one **EMPTY flag** in a
slot at the right end. Slots **5** and **6** start empty, because those two labels are in the bins. A **bin
card holder** stands at the **back-right corner** with two pockets, **OPEN** on the left and **CLOSED** on the
right. Two **tickets**, printed **A** and **B**, both start in the **OPEN** pocket.

The order never changes: count bin A, then count bin B; move every part from bin A into bin B; verify the
merged count; relabel bin B, then relabel bin A; then move ticket A to **CLOSED**. Nothing moves out of bin A
until both bins have been counted. No label is touched until the merged count has been verified. The episode
does not end until ticket A stands in the **CLOSED** pocket.

The right gripper does all the work: it fans and counts both bins, moves every part, pulls and places every
label, and moves the ticket. The left gripper presses the keep bin flat against the table by its left rim and
holds it there for the whole episode, so the keep bin cannot slide while parts go in, while it is fanned for
counting, or while a label is pushed home. The left gripper stays on the left rim of the keep bin and never
reaches across it.

The table is set up in one of three ways. Only the source bin moves; the keep bin, the label rack, and the bin
card holder are in the same place in all three.

* **Config M1:** the source bin is at the front-center, directly in front of the keep bin.
* **Config M2:** the source bin is at the back-center, directly behind the keep bin.
* **Config R:** the source bin is directly right of the keep bin.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the source bin starts at the front-center (**Config M1**), the back-center
  (**Config M2**), or directly right of the keep bin (**Config R**). One config per episode, chosen before
  recording and never changed mid-episode.
* **Same-side rule:** the **right gripper** reaches into the source bin in every config, because the left
  gripper holds the keep bin. The left side of the table is never a start zone: the left gripper comes in from
  there onto the keep bin's left rim, and the right gripper never reaches across the table.
* **Fixed roles:** everything else is the same in all three configs — the left gripper pins the keep bin, the
  right gripper counts, moves every part, and handles every card, and the order (count, merge, verify, label,
  card) never changes. The config changes only the direction the right gripper reaches for the source bin and
  carries each part.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: both bins rim to rim, both label windows, the label rack at
   the front-right, and the bin card holder at the back-right.
3. Both bins are visible from above, so the inside floor of each bin and every part in it can be seen.
4. Both **label windows** are readable from above, so the number on each label can be read without moving a
   bin.
5. Both arms are at home with grippers open.
6. The table is bare apart from the two bins, the label rack, the bin card holder, and robot hardware.
7. The right arm reaches the far side of the source bin on its spot for this episode's config, the far side of
   the keep bin, slot 1 and slot 12 of
   the label rack, the EMPTY flag slot, and both pockets of the bin card holder without stretching. The left
   arm reaches the left rim of the keep bin without stretching.

### Materials checklist

1. Two open-top **bins** stand rim to rim on the table, square to the front edge, with a small even gap
   between their rims.
2. The **keep bin** is on the **keep spot**, just right of the center of the table. Its front rail is printed
   **B**.
3. The **source bin** is on the **source spot** for this episode's config. Its front rail is printed **A**.
   * **Config M1:** front-center, directly in front of the keep bin
   * **Config M2:** back-center, directly behind the keep bin
   * **Config R:** directly right of the keep bin
4. Both bins hold the same part type, **hex nuts**, and nothing else.
5. The **source bin** holds **5** hex nuts. The **keep bin** holds **6** hex nuts.
6. Each bin has a **label window** on its front rail, angled up toward the front, holding one upright card.
   The source bin's window holds count label **5**. The keep bin's window holds count label **6**.
7. The **label rack** sits at the **front-right**, angled toward the front. It has twelve numbered slots,
   **1** to **12**, each holding the matching **count label** standing upright with its number facing the
   front. Slots **5** and **6** are empty, because those labels are in the bins.
8. One **EMPTY flag** stands in the **flag slot** at the right end of the label rack, printing facing the
   front.
9. The **bin card holder** stands at the **back-right corner**, angled toward the front, with two pockets:
   **OPEN** on the left and **CLOSED** on the right. The **CLOSED** pocket is empty.
10. Two **tickets**, printed **A** and **B**, stand in the **OPEN** pocket, printing facing the front, with
    ticket **A** in front.
11. Keep the left side of the table clear. The left gripper comes in from there onto the keep bin's left rim.
12. Before collection, confirm by hand that:
    - one hex nut can be pinched off the floor of each bin without dragging others with it;
    - a hex nut laid in the keep bin stays inside it and does not bounce out;
    - all eleven hex nuts fit on the floor of the keep bin in a **single layer**;
    - neither bin slides on the table when a hex nut is pinched out of it;
    - a count label slides into a bin's label window and stands there on its own;
    - a ticket slides into each pocket of the bin card holder and stands there on its own.

### Workspace layout

- **Keep spot:** just right of the center of the table — the keep bin, rail **B**, stays here all episode
- **Source spot:** front-center in front of the keep spot (Config M1), back-center behind it (Config M2), or
  directly right of it (Config R) — the source bin, rail **A**, stays here all episode
- **Front rail of each bin:** the label window that holds that bin's card
- **Front-right supply zone:** the label rack, slots 1 to 12, with the EMPTY flag in the flag slot at its
  right end
- **Back-right corner:** the bin card holder, OPEN pocket on the left, CLOSED pocket on the right
- **Left side:** kept clear, so the left gripper can come in onto the keep bin's left rim

### Arm assignments

- **Left gripper:** presses the keep bin flat by its left rim and holds it there for the whole episode, in
  every config, so the keep bin cannot slide while the right gripper works.
- **Right gripper:** fans and counts both bins, moves every hex nut from the source bin to the keep bin, pulls
  and places the labels and the EMPTY flag, and moves ticket A to the CLOSED pocket, in every config. Only the
  direction it reaches for the source bin and carries each part changes with the config.

## Vocabulary

- **Keep spot:** the place on the table, just right of center, where the keep bin sits. The bin stays here for
  the whole episode.
- **Source spot:** the place on the table where the source bin sits — front-center in front of the keep spot
  (**Config M1**), back-center behind it (**Config M2**), or directly right of it (**Config R**). One per
  episode, chosen before recording and never changed mid-episode. The bin stays here for the whole episode.
- **Keep bin:** the bin printed **B** on its front rail. Everything ends up in this bin.
- **Source bin:** the bin printed **A** on its front rail. This bin ends the episode empty.
- **Square:** the front rail of a bin lines up with the front edge of the table, so neither end of the bin sits
  nearer the front.
- **Rim:** the top edge of a bin wall.
- **Front rail:** the front wall of a bin, the one facing the front edge of the table. It carries the printed
  letter and the label window.
- **Part:** one hex nut.
- **Label window:** the slot on a bin's front rail that holds one upright card, either a count label or the
  EMPTY flag.
- **Count label:** a card printed with one big number. It says how many parts are in the bin it stands in.
- **Label rack:** the rack at the front-right that the count labels and the EMPTY flag stand in.
- **Slot number:** the number printed beside a slot on the label rack. The count label with that number lives
  in that slot.
- **EMPTY flag:** the card printed **EMPTY** that stands in the flag slot at the right end of the label rack.
  It goes into the source bin's label window at the end of the episode.
- **Fan flat:** spread the parts on the floor of a bin with the closed right gripper until they lie in a
  **single layer**, so each one can be seen and counted on its own.
- **Single layer:** every part sits on the floor of the bin, and no part sits on top of another.
- **Count-verify:** fan a bin flat, lift the right gripper clear, count the parts, and compare that number with
  the number it should be.
- **Starting count:** the number of parts counted in a bin in Step 2, before anything is moved.
- **Merged total:** the number of parts counted in the keep bin in Step 4, after everything has been moved.
  This is the number that goes on the keep bin's new label.
- **Short:** fewer parts are counted than expected.
- **Over:** more parts are counted than expected.
- **Ticket:** one of the two cards in the bin card holder, printed **A** or **B**. Each one stands for the bin
  with the same letter.
- **Bin card holder:** the two-pocket holder at the back-right corner that the tickets stand in.
- **OPEN pocket:** the left pocket of the bin card holder. A ticket here means that bin is still in use.
- **CLOSED pocket:** the right pocket of the bin card holder. A ticket here means that bin has been emptied.
- **Seated:** a label, flag, or ticket has been pushed down into its window or pocket, stands upright with its
  printing facing the front, and stays there when the right gripper lets go.

## Steps

Run Steps 1–6 in order on the one pair of bins, then end the episode with Step 7. Only 2.1, 3.1, and 5.2
depend on the config: they set which way the **right gripper** reaches for the source bin, carries each part
into the keep bin, and carries each card between the source bin's window and the rack. Every other line is
the same in all three configs.

### Step 1: Hold the keep bin down

**Goal:** the keep bin is pinned flat on the keep spot and cannot slide for the rest of the episode.

- With the **left gripper**, press down on the **left rim** of the keep bin and hold it against the table.
- Keep the **left gripper** there through Steps 2, 3, 4, 5, and 6.

**Check:** the keep bin is flat on the table, **square** to the front edge, and does not slide when the left
gripper presses. If the bin is crooked, straighten it with the **left gripper** first, then press it down.

**Expected state:** the keep bin is held, both bins hold parts, both label windows hold a count label, and both
tickets stand in the OPEN pocket.

### Step 2: Count both bins

**Goal:** the starting count of each bin is known from counting it, not from reading its label.

- With the **left gripper**, keep pressing the keep bin down.
- Count the **source bin first**, then the **keep bin**. Count both bins, every episode.
- Do not move any part out of a bin until both bins have been counted.

#### 2.1 Count the source bin

- **IF Config M1:** the source bin is in front of the keep bin. **IF Config M2:** it is behind the keep bin.
  **IF Config R:** it is right of the keep bin. Reach for it there.
- Close the **right gripper** and bring its tips down onto the floor of the **source bin**.
- Sweep the tips gently across the floor to **fan flat** the parts into a **single layer**.
- Lift the **right gripper** up and clear of the bin, so nothing is hidden under it.
- Count the parts now visible in the source bin. This is the source bin's **starting count**.
- Read the count label in the source bin's **label window** and compare the two numbers.

#### 2.2 Count the keep bin

- Close the **right gripper** and bring its tips down onto the floor of the **keep bin**.
- Sweep the tips gently across the floor to **fan flat** the parts into a **single layer**.
- Lift the **right gripper** up and clear of the bin.
- Count the parts now visible in the keep bin. This is the keep bin's **starting count**.
- Read the count label in the keep bin's **label window** and compare the two numbers.

**Check:** both bins were fanned flat and counted with the right gripper clear of the bin. If a count does not
match that bin's label, fan and count that bin again with the **right gripper**. Use the number you counted.
Do not use the number on the label.

**Expected state:** both bins are in a single layer, both starting counts are known, nothing has been moved
between the bins, and both labels are still in their windows.

### Step 3: Move every part into the keep bin

**Goal:** the source bin is empty and every part is in the keep bin.

- With the **left gripper**, keep pressing the keep bin down.
- With the **right gripper**, move **one part at a time**, from the **source bin** into the **keep bin**.
- Never scoop, never carry two parts, and never tip or pour a bin out.
- Parts only move from the source bin to the keep bin. Never move a part the other way.

#### 3.1 Move one part

- **IF the source bin is at the front-center (Config M1):** with the **right gripper**, reach down into the
  **source bin**, pinch **one part** off the floor, lift it straight up until it is clear of the source bin's
  rim, and carry it straight back, low over the gap between the two rims, to the **keep bin**.
- **IF the source bin is at the back-center (Config M2):** with the **right gripper**, reach down into the
  **source bin**, pinch **one part** off the floor, lift it straight up until it is clear of the source bin's
  rim, and carry it straight forward, low over the gap between the two rims, to the **keep bin**.
- **IF the source bin is right of the keep bin (Config R):** with the **right gripper**, reach down into the
  **source bin**, pinch **one part** off the floor, lift it straight up until it is clear of the source bin's
  rim, and carry it left, low over the gap between the two rims, to the **keep bin**.

Then, in all three:

- Do not lift it high above the bins.
- Lower the part into the keep bin until it is inside the walls, then open the **right gripper** and let go.
- Do not drop or toss a part in from above the rim.
- If more than one part comes up together, put the extra parts back on the floor of the **source bin** with the
  **right gripper** before going on.
- Repeat 3.1 until no part is left in the source bin.

#### 3.2 Check the source bin is empty

- Close the **right gripper** and sweep its tips gently across the floor of the **source bin**, into every
  corner.
- Lift the **right gripper** up and clear of the bin and look at the bin floor.
- If a part is still there, go back to 3.1 and move it.

**Check:** the source bin floor is bare in every corner, and no part is sitting on a rim or on the table. If a
part is on the table, pick it up with the **right gripper** and put it in the **keep bin**.

**Expected state:** the source bin is empty, the keep bin holds every part, both bins are still square on their
spots, and both labels are still in their windows.

### Step 4: Verify the merged count

**Goal:** the merged total is known from counting the keep bin.

- With the **left gripper**, keep pressing the keep bin down.
- Close the **right gripper** and sweep its tips across the floor of the **keep bin** to **fan flat** the parts
  into a **single layer**.
- Lift the **right gripper** up and clear of the bin.
- Count the parts in the keep bin. This is the **merged total**.
- Add the two **starting counts** from Step 2 and compare that number with the merged total.

**Check:** the merged total equals the two starting counts added together. If it is **short** or **over**, fan
and count the keep bin again with the **right gripper**. If it is still short, look in the source bin and on
the table, and move any part you find into the keep bin with the **right gripper**, then fan and count again.
The number you count in the keep bin is the **merged total**, and it is the number that goes on the new label.

**Expected state:** the keep bin holds every part in a single layer, the merged total is known, the source bin
is empty, and no label has been touched yet.

### Step 5: Relabel both bins

**Goal:** the keep bin's window shows the merged total and the source bin's window shows the EMPTY flag.

- With the **left gripper**, keep pressing the keep bin down.
- Relabel the **keep bin first**, then the **source bin**.
- Handle one card at a time with the **right gripper**. Do not carry a card over an open bin.

#### 5.1 Relabel the keep bin

- With the **right gripper**, pinch the old count label in the keep bin's **label window** by its top edge and
  pull it straight up and out.
- Carry it to the **label rack** and push it down into the slot whose **slot number** matches the number on the
  label, printing facing the front. Open the **right gripper** and let go.
- With the **right gripper**, pinch the count label in the slot whose **slot number** is the **merged total**,
  and lift it straight up out of the rack.
- Carry it in one go to the keep bin's **label window**, line it up, printing facing the front, and push it
  straight down until it stands on its own. Open the **right gripper** and let go.

#### 5.2 Flag the source bin empty

- **IF Config M1 or R:** carry each card straight between the source bin's window and the rack. **IF Config
  M2:** the source bin's window is behind the keep bin — carry each card right around the keep bin, never
  over it.
- With the **right gripper**, pinch the old count label in the source bin's **label window** by its top edge
  and pull it straight up and out.
- Carry it to the **label rack** and push it down into the slot whose **slot number** matches the number on the
  label, printing facing the front. Open the **right gripper** and let go.
- With the **right gripper**, pinch the **EMPTY flag** by its top edge and lift it straight up out of the flag
  slot.
- Carry it in one go to the source bin's **label window**, line it up, printing facing the front, and push it
  straight down until it stands on its own. Open the **right gripper** and let go.

**Check:** the keep bin's window holds the label with the **merged total**, the source bin's window holds the
**EMPTY flag**, both are **seated**, and both old labels stand in their own numbered slots. If a card leans,
falls, or faces backwards, take it out with the **right gripper**, turn it printing-forward, and push it down
again. If an old label is in the wrong slot, move it to its own slot with the **right gripper**.

**Expected state:** both label windows are filled and seated, the label rack holds the two old labels in their
own slots, the flag slot is empty, and the slot for the merged total is empty.

### Step 6: Update the bin card

**Goal:** ticket A stands in the CLOSED pocket, so the card shows bin A has been emptied.

- With the **left gripper**, keep pressing the keep bin down.
- With the **right gripper**, pinch **ticket A** by its top edge in the **OPEN pocket** and lift it straight up
  out of the pocket.
- Carry it across to the **CLOSED pocket** and push it straight down into the pocket, printing facing the
  front, until it stands on its own. Open the **right gripper** and let go.
- Leave **ticket B** standing in the **OPEN pocket**. Do not touch it.

**Check:** ticket **A** is **seated** in the CLOSED pocket and ticket **B** still stands in the OPEN pocket. If
the wrong ticket was moved, take it out with the **right gripper**, stand it back in the OPEN pocket, and move
ticket A instead. If a ticket leans or falls, pick it up with the **right gripper** and push it down again.

**Expected state:** ticket A stands in CLOSED, ticket B stands in OPEN, both bins are square on their spots,
and both label windows are filled.

### Step 7: End the episode

**Goal:** recording ends with the bins merged, counted, relabelled, flagged, and carded.

1. Confirm the end state:
   - the source bin is empty, with a bare floor in every corner;
   - the keep bin holds every part, in a single layer, with none on a rim or on the table;
   - the keep bin's label window holds the count label for the **merged total**, seated and facing the front;
   - the source bin's label window holds the **EMPTY flag**, seated and facing the front;
   - the two old count labels stand in their own numbered slots on the label rack;
   - ticket **A** stands seated in the **CLOSED** pocket and ticket **B** in the **OPEN** pocket;
   - both bins are still **square** on the keep spot and the source spot.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

### After each episode

1. Take ticket A out of the CLOSED pocket and stand it back in the OPEN pocket, in front of ticket B, printing
   facing the front.
2. Take the EMPTY flag out of the source bin's label window and stand it back in the flag slot at the right end
   of the label rack.
3. Take the count label out of the keep bin's label window and stand it back in its own numbered slot.
4. Move parts back until the source bin holds **5** hex nuts and the keep bin holds **6**. Pick up any part
   that ended up on the table or the floor and put it back in a bin.
5. Put the count label **5** into the source bin's label window and the count label **6** into the keep bin's
   label window, both seated and facing the front. Slots 5 and 6 on the rack are now empty again.
6. Brush dust and chips out of both bins, both label windows, and both card pockets.
7. Set the keep bin **square** on the keep spot and the source bin **square** on the source spot for the next
   episode's config — front-center (Config M1), back-center (Config M2), or directly right of the keep bin
   (Config R) — rim to rim with a small even gap between them.
8. Run both Setup checklists before the next episode.

### At the end of the session

1. Inspect the parts and the fixtures. Throw out any hex nut that is burred, cracked, or thread-damaged.
   Replace a bin whose label window no longer holds a card upright, or whose floor is cracked so a part will
   not lie flat. Replace any count label, EMPTY flag, or ticket that is bent, torn, soft, or no longer
   readable. Replace the label rack or the bin card holder if a slot or pocket no longer holds a card upright.
2. Leave the source bin holding 5 hex nuts with label **5** in its window, the keep bin holding 6 hex nuts with
   label **6** in its window, both bins square and rim to rim, the label rack holding labels 1 to 12 with
   slots 5 and 6 empty, the EMPTY flag in the flag slot, and both tickets standing in the OPEN pocket.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

- the **start timestamp** in the video;
- the **violation name** from the list below; and
- the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain multiple violations; tag each
separately. Retain the episode in training data with its violation tags. Do not delete a recorded episode
solely because it contains a violation.

### Violations

**Note on the start position:** the violations below were written for Config R (source bin directly right of
the keep bin, parts carried left). The pickup and arm-role cues will be rewritten later to cover all three
start positions; they are left as they are for now. Until then, anything that does not match the episode's
config goes under **Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the source bin is not on
  the source spot for the config; the source bin stands on the left side of the table; the left gripper
  reaches into the source bin, or the right gripper reaches across the table for it; or the wrong IF line is
  followed.
- **SOP rule broken:** the start position and the same-side rule (the source bin starts at the front-center,
  the back-center, or directly right of the keep bin; the right gripper reaches into it in every config and
  never across the table; the IF line followed is the one for the config on the table).
- **Coaching note:** look where the source bin is before the first reach, then follow that config's IF lines
  through Steps 2, 3, and 5.

**Violation: Keep bin not held**
- **Visible cue:** the left gripper is off the left rim of the keep bin while the right gripper moves a part,
  fans a bin, or pushes a label in, and the keep bin slides, lifts, or is chased across the spot.
- **SOP rule broken:** Step 1 (the left gripper presses the keep bin down by its left rim and holds it there
  through Steps 2 to 6).
- **Coaching note:** left gripper on the keep bin rim first, and leave it there until the episode ends.

**Violation: Bin moved off its spot**
- **Visible cue:** either gripper lifts, turns, drags, or pushes a bin, or a bin ends the episode out of square
  with the front edge or out of line with the other bin.
- **SOP rule broken:** Steps 1–6 (both bins stay flat and square on the keep spot and the source spot for the
  whole episode and are never lifted).
- **Coaching note:** reach down inside over the rim. Never push a bin wall, and never move a bin.

**Violation: A starting count skipped**
- **Visible cue:** the right gripper fans and counts only one bin, or neither, before parts start moving in
  Step 3.
- **SOP rule broken:** Step 2 (count the source bin first, then the keep bin; count both bins, every episode).
- **Coaching note:** two bins, two counts, before anything moves. Say each number out loud.

**Violation: Counted without fanning flat**
- **Visible cue:** the right gripper counts a bin while parts sit stacked on each other, never brings its tips
  down to spread them, or stays over the bin so parts are hidden under the gripper while counting.
- **SOP rule broken:** Steps 2 and 4 (fan the parts into a single layer with the closed right gripper, then
  lift the gripper clear of the bin before counting).
- **Coaching note:** spread it out, pull the gripper back, then count what you can see.

**Violation: Label number used instead of the counted number**
- **Visible cue:** a bin's count disagrees with the card in its label window, and the episode carries the
  label's number forward without the right gripper fanning and counting that bin again.
- **SOP rule broken:** Step 2 (if a count does not match that bin's label, fan and count again and use the
  number you counted, not the number on the label).
- **Coaching note:** the parts are the count, not the card. Recount, then trust what you counted.

**Violation: Work done out of order**
- **Visible cue:** the phases run out of sequence — a part leaves the source bin before both bins are counted,
  a label is touched before the merged count is verified, or the ticket moves before both bins are relabelled.
- **SOP rule broken:** Steps 2–6 (count both, merge, verify, relabel, then update the card, in that order).
- **Coaching note:** finish the phase before you start the next one. Count, merge, verify, label, card.

**Violation: More than one part moved at a time**
- **Visible cue:** the right gripper scoops, rakes, or lifts two or more parts together, tips or pours a bin
  out, or carries a handful across, and the extras are not put back.
- **SOP rule broken:** Step 3 (move one part at a time; if more than one comes up together, put the extras back
  on the floor of the source bin before going on).
- **Coaching note:** one pinch, one part. If two come up, drop the spare back in the source bin first.

**Violation: Merged in the wrong direction**
- **Visible cue:** the right gripper takes a part out of the keep bin and puts it in the source bin, so parts
  move right instead of left.
- **SOP rule broken:** Step 3 (parts only move from the source bin to the keep bin; never move a part the other
  way).
- **Coaching note:** bin A empties into bin B, one way only. Nothing goes back into A.

**Violation: Part carried high above the bins**
- **Visible cue:** the right gripper lifts a part well above the rims on its way across, instead of a low carry
  over the gap between the two rims.
- **SOP rule broken:** Step 3 (lift the part clear of the source bin's rim and carry it left, low over the gap;
  do not lift it high above the bins).
- **Coaching note:** just clear the rim, then straight across low. Height is where parts get dropped.

**Violation: Part dropped in instead of placed**
- **Visible cue:** the right gripper opens above the keep bin's rim and the part falls, tosses, or bounces in,
  rather than being lowered inside the walls and released there.
- **SOP rule broken:** Step 3 (lower the part into the keep bin until it is inside the walls, then open the
  right gripper; do not drop or toss a part in from above the rim).
- **Coaching note:** take it all the way down inside the bin before you open the gripper.

**Violation: Source bin not emptied or not checked**
- **Visible cue:** the episode moves on to Step 4 or later with a part still on the floor of the source bin or
  sitting on its rim, or the right gripper never sweeps the source bin floor into the corners and lifts clear
  to look at it before counting the keep bin.
- **SOP rule broken:** Step 3 (repeat the move until no part is left in the source bin, then sweep the floor
  into every corner with the closed right gripper, lift clear, and look at the bin floor).
- **Coaching note:** sweep the corners, pull back, look. Bin A leaves the episode bare.

**Violation: Merged count not verified**
- **Visible cue:** the right gripper never fans and counts the keep bin after the merge, or the episode reaches
  the labels with no count taken.
- **SOP rule broken:** Step 4 (fan the keep bin flat, lift the right gripper clear, and count the parts to get
  the merged total).
- **Coaching note:** the merged total comes from counting, every time. No count, no label.

**Violation: Count mismatch found but not resolved**
- **Visible cue:** the merged total does not equal the two starting counts added together, and the episode
  moves on to the labels without the right gripper fanning and counting the keep bin again or searching the
  source bin and the table.
- **SOP rule broken:** Step 4 (on a short or over count, fan and count again, and if still short search the
  source bin and the table and move what you find into the keep bin).
- **Coaching note:** numbers that do not add up earn another count and a search before you label anything.

**Violation: Wrong count label taken**
- **Visible cue:** the right gripper takes the new keep-bin label from a slot whose number is not the merged
  total, so the number in the keep bin's window does not match what was counted.
- **SOP rule broken:** Step 5 (take the count label from the slot whose slot number is the merged total).
- **Coaching note:** say the merged total, find that slot number, then reach.

**Violation: Old label not returned to its own slot**
- **Visible cue:** an old label pulled from a bin's window is pushed into a slot with a different number, laid
  on the rack, dropped in a bin, or left on the table.
- **SOP rule broken:** Step 5 (push each old label down into the slot whose slot number matches the number on
  the label).
- **Coaching note:** read the number on the card in your gripper, then put it in the slot with that number.

**Violation: Label or flag put in the wrong bin**
- **Visible cue:** the EMPTY flag goes into the keep bin's window, the count label goes into the source bin's
  window, or a card is left standing in a bin that already holds one.
- **SOP rule broken:** Step 5 (the keep bin's window takes the count label for the merged total; the source
  bin's window takes the EMPTY flag).
- **Coaching note:** the number goes on the full bin, EMPTY goes on the bare one. Check the rail letter first.

**Violation: Source bin left unflagged**
- **Visible cue:** the episode ends with the source bin's label window empty, or with the EMPTY flag lying
  loose in the bin or on the table instead of standing in the window.
- **SOP rule broken:** Step 5 (push the EMPTY flag down into the source bin's label window before the episode
  ends).
- **Coaching note:** an empty bin never leaves unflagged. EMPTY goes in the window, not in the bin.

**Violation: Card mishandled on the way**
- **Visible cue:** the right gripper pulls more than one card at a time, bends or creases a card, sets a card
  down on the way, or carries a card over an open bin.
- **SOP rule broken:** Step 5 (handle one card at a time and carry it in one go, not over an open bin and not
  set down on the way).
- **Coaching note:** one card, top edge, straight to where it goes.

**Violation: Label, flag, or ticket not seated**
- **Visible cue:** a count label, the EMPTY flag, or a ticket leans, falls, sits on top of its window, slot, or
  pocket, or stands with its printing facing away from the front, and the right gripper leaves it that way.
- **SOP rule broken:** Steps 5 and 6 (push each card straight down, printing facing the front, and let go only
  once it stands on its own).
- **Coaching note:** printing to the front, push it down, then let go and watch that it stays.

**Violation: Card not updated**
- **Visible cue:** the episode ends with ticket A still standing in the OPEN pocket, or with the CLOSED pocket
  empty.
- **SOP rule broken:** Step 6 (ticket A is moved into the CLOSED pocket before the episode ends).
- **Coaching note:** the bin is not consolidated until the card says so. Ticket A goes to CLOSED.

**Violation: Wrong ticket moved**
- **Visible cue:** the right gripper lifts ticket B, moves ticket B into the CLOSED pocket, or moves both
  tickets across.
- **SOP rule broken:** Step 6 (move ticket A into the CLOSED pocket and leave ticket B standing in the OPEN
  pocket).
- **Coaching note:** only the emptied bin closes. Read the letter on the ticket before you lift it.

**Violation: Label rack or card holder knocked out of place**
- **Visible cue:** either gripper tips, pushes, or drags the label rack or the bin card holder off its spot,
  spills the labels or the tickets, or leaves a card lying flat in the rack.
- **SOP rule broken:** Steps 5 and 6 (the label rack stays on its spot at the front-right and the bin card
  holder stays on its spot at the back-right through the whole episode).
- **Coaching note:** reach in from above, straight down and straight up. Work slower so nothing gets shoved.

**Violation: Part or card dropped and left**
- **Visible cue:** either gripper drops a part, a label, the flag, or a ticket onto the table, into the wrong
  bin, or on the floor, and the episode moves on without it being picked up and put where it belongs.
- **SOP rule broken:** Step 3 (a part that ends up on the table is picked up with the right gripper and put in
  the keep bin) and Steps 5 and 6 (a dropped card is retrieved and seated before the episode ends).
- **Coaching note:** pick up what you drop before the next move. Nothing stays loose on the table.

**Violation: Wrong arm used**
- **Visible cue:** an action assigned to one gripper is done by the other, including the left gripper fanning a
  bin, counting, moving a part, handling a label or a ticket, or the right gripper holding down the keep bin.
- **SOP rule broken:** Steps 1–6 (the right gripper fans, counts, moves parts, handles cards, and moves the
  ticket; the left gripper holds the keep bin).
- **Coaching note:** right gripper does the work, left gripper holds the keep bin. It does not swap.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before the empty source bin, the merged count, both labels, and the ticket
  are confirmed, an arm is not home, a gripper is closed, or an arm does something else after homing.
- **SOP rule broken:** Step 7 (confirm the end state, return both arms home with grippers open as their final
  action, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than tagging
them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- A bin arrives holding a second part type mixed in with the hex nuts.
- A bin arrives holding so many parts that they will not lie in a single layer in the keep bin.
- A part is burred, cracked, or thread-damaged, so it will not lie flat on the bin floor.
- A bin's label window is broken or spread open, so a correctly pushed card will not stand.
- A pocket on the bin card holder is broken, so a correctly pushed ticket will not stand.
- A count label, the EMPTY flag, or a ticket is misprinted or unreadable.
- The label rack is missing the slot for the merged total, so the correct label cannot be taken.

## Annotation subtasks (from SOP)

1. Press the keep bin flat and hold it with the left gripper
2. Fan the source bin flat with the closed right gripper and count it
3. Fan the keep bin flat with the closed right gripper and count it
4. Pick one part from the source bin with the right gripper
5. Place the part in the keep bin
6. Repeat the pick and place until the source bin is empty
7. Sweep the source bin floor and confirm it is bare
8. Fan the keep bin flat and count the merged total
9. Pull the old label from the keep bin and stand it in its own rack slot
10. Take the count label for the merged total and seat it in the keep bin's window
11. Pull the old label from the source bin and stand it in its own rack slot
12. Take the EMPTY flag and seat it in the source bin's window
13. Move ticket A from the OPEN pocket to the CLOSED pocket
14. Confirm the end state, return both arms home, and end the episode
