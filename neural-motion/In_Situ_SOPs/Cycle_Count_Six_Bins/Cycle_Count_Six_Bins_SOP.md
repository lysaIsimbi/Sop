# Cycle-Count Six Bins SOP (1x Episode: six bins, in situ)

One episode cycle-counts six bins against one count sheet, at the shelving where the bins live. The base is **passive**: it has no
drive of its own, so it is pushed by hand to the front of the shelving and locked there, and nothing is carried away to a table.
Everything the episode touches is already at the shelving when recording starts: the six bins and their units, the count tray on the
work ledge, and the log stand with the count sheet, the marker, and the discrepancy tags.

The episode runs these four actions in this order for each bin, and no other: **count the units in the bin against the sheet, log the
count, recount any variance, flag a discrepancy tag on the bin.** A bin is finished, and its units are back in it, before the next bin
is touched.

The shelving is worked **as found**. Each bin holds a row of units of one SKU. The **count sheet** gives the **expected quantity** for
each bin. Most bins hold exactly that many. One or two bins, chosen at reset, hold one unit more or one unit fewer, and nothing on the
shelving shows which. The episode ends with all six bins counted and logged, every variance recounted, a discrepancy tag on every bin
whose recount still differs from the sheet, every unit back in its own bin, and the marker back in its clip.

**Counting is done by moving.** A unit hidden behind another cannot be counted by looking, so every unit is taken out of its bin one at a
time and set in the next pocket of the **count tray**. The count is the number of filled pockets. The units then go back into their bin.

**This is an in-situ task, and three things follow from that.** First, **each shelf level has a shelf directly above it**, so **every
reach into a bin is from the front, straight in, level**. No gripper comes down into a bin from above. Second, the **shelving, the ledge,
and the log stand are never leaned on and never pushed**: no gripper, wrist, or forearm rests on a shelf, an upright, a bin, the ledge, or
the stand, and the bins are fixed and never pulled out. Third, **a unit goes only between its own bin and the count tray**: nothing is set
down on a shelf edge, another bin, the ledge, or the floor on the way.

The shelving is set up in one of two ways. Only the **log stand** moves. The bins, their units, and the count tray are in the same place
in both.

* **Config L:** the log stand stands at the **left end** of the work ledge.
* **Config R:** the log stand stands at the **right end** of the work ledge.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says so on an
**IF** line. Look at the ledge and follow the line that matches. Which bins hold a variance is not a config: it is found only by counting.

What stays constant across all sessions:

* **Column rule:** the **left gripper** counts, returns, and tags the **left column** (A1, B1, C1) and the **right gripper** the **right
  column** (A2, B2, C2).
* **Log-side rule:** the gripper on the log stand's side ticks every line of the sheet and takes every tag out of the tag cup. That is
  the **left gripper** in Config L and the **right gripper** in Config R. It is called the **log gripper**.
* **Hand-over rule:** a tag for a bin in the column away from the log stand is **handed over** by the log gripper to that column's gripper
  at the **hand-over point**. No arm reaches across the shelving.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches over, under, around, or
past the other. Nothing is moved two at a time: one gripper holds one thing, and the other gripper is empty, taking a hand-over, or clear
of the shelving.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or repositioned
once recording starts. It is parked once, before recording, and does not move again until the episode is over.

1. Push the base by hand up to the front of the work ledge and stop it **square to the shelving**, so the shelf edges run straight across
   the frame of the camera.
2. Stop it **centered on the shelving**, so the middle of the base is in line with the middle upright between the two columns.
3. Stop it **close enough** that both grippers reach the back of a bin straight in and level without either arm extending, and **far
   enough** that neither arm, wrist, nor any part of the base touches a shelf, an upright, the ledge, or the log stand while both arms
   work.
4. Check the **height band**: both grippers come level into every bin on levels A, B, and C without a wrist or forearm touching the shelf
   above it.
5. Check the **left side**: the **left gripper** reaches the back of A1, B1, and C1, the front lip of each, all six pockets of the count
   tray, and the hand-over point, all without extending.
6. Check the **right side**: the **right gripper** reaches the back of A2, B2, and C2, the front lip of each, all six pockets of the count
   tray, and the hand-over point, all without extending.
7. Check the **log stand** for the config this episode runs: the **log gripper** reaches every tick box on the sheet, the marker clip, and
   the tag cup.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not work shelving the arms cannot reach
   comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the shelving hard enough to shift it, nothing
touches it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the middle upright and its frame includes all six bins and their labels, the count tray with its
   pocket numbers, and the log stand with the sheet, the marker, and the tag cup.
3. The camera sees into the count tray well enough to count the filled pockets at a glance.
4. The camera reads the **count sheet** well enough to see the expected quantities and which boxes are ticked.
5. The camera sees the front lip of every bin, so a hung tag is readable.
6. Both arms are at home with grippers open.
7. The **left arm** reaches the back of A1, B1, C1, the whole count tray, and the hand-over point without extending to a joint limit.
8. The **right arm** reaches the back of A2, B2, C2, the whole count tray, and the hand-over point without extending to a joint limit.
9. The log arm for this config reaches the sheet, the marker clip, and the tag cup without extending to a joint limit.
10. Both grippers come in and go out of every bin **from the front and level**, and neither wrist nor forearm touches the shelf above on
    the way in or out.
11. The two arms do not collide, and neither arm passes in front of the other.
12. If a place cannot be reached, re-park the base by the Base positioning steps until lines 7 to 11 hold.

### Materials checklist

1. The **shelving** stands where it lives, fixed to the wall or the floor. It is not moved, not leaned on, and not pushed at any point.
2. It has **three levels**, each with a shelf directly above it: **level A** at the top, **level B** in the middle, **level C** at the
   bottom. A **middle upright** splits it into a **left column** and a **right column**.
3. Each level holds **two fixed open-front bins**, one per column: **A1, A2**, **B1, B2**, **C1, C2**, numbered left to right. That makes
   **six bins**. Each has a **location label** on the shelf edge right below it.
4. Each bin is one unit wide and six units deep. Its units stand upright in one row from the back, SKU label facing out, with no gap
   between them.
5. Every unit is a small boxed item that fits one gripper. Each bin holds one SKU, and no two bins hold the same SKU.
6. Each bin holds between two and five units. Most hold exactly the **expected quantity** on the sheet. **One or two bins**, chosen at
   random at reset, hold **one unit more or one unit fewer** than the sheet says.
7. The **work ledge** is a fixed flat ledge running along the front of the shelving below level C. Its **front strip** sticks out past the
   shelf edges, so nothing is above it.
8. The **count tray** is fixed in the middle of the front strip, in line with the middle upright. It has **six pockets** in two rows of
   three, each the size of one unit, with its number, **1 to 6**, printed large on the tray beside it. Pockets 1 to 3 are the back row,
   left to right. Pockets 4 to 6 are the front row, left to right. It starts empty.
9. The **log stand** is a small stand at the **left end** of the front strip in **Config L** and at the **right end** in **Config R**. It
   holds, fixed on its face:
   * the **count sheet** in a sheet holder, standing upright, facing out;
   * the **marker** in its marker clip, point down;
   * the **tag cup**, an open cup holding **three discrepancy tags** standing on end.
10. The **count sheet** has six lines, one per bin, in the order **A1, A2, B1, B2, C1, C2**. Each line gives the bin, its expected
    quantity in large print, and two rows of **tick boxes** numbered **0 to 6**: the **COUNT** row and, under it, the **RECOUNT** row.
    The sheet is fresh: no box is ticked.
11. A **discrepancy tag** is a stiff red card printed **COUNT DISCREPANCY**, with a spring clip along its top edge that pushes down over a
    bin's front lip and holds there.
12. Nothing else stands on the shelving or the ledge within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the location labels and the pocket numbers. You judge every other place by eye against the
shelving itself.

* **Shelving:** the fixed unit the base is parked at. Never moved, never leaned on, never pushed.
* **Left column:** A1, B1, C1. **Left gripper only.**
* **Right column:** A2, B2, C2. **Right gripper only.**
* **Count tray:** fixed in the middle of the ledge's front strip. Either gripper, one at a time.
* **Hand-over point:** in front of the middle upright, a hand out from the shelf edge of level B.
* **Log stand:** at the left end (Config L) or the right end (Config R) of the front strip, with the sheet, the marker, and the tag cup.
  **Log gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the left column and the **right gripper** works the right column. The **log gripper** also works the log
  stand.
* The two arms meet only at the **hand-over point**, and both use the count tray, one at a time.
* Neither arm goes into a bin in the other column, and neither reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds one thing, and while it does, the other gripper is empty, taking a hand-over, or
  drawn **clear of the shelving**.

### Arm assignments

* **Counting gripper** (the gripper of the current bin's column). Takes the bin's units out into the count tray, puts them back, and hangs
  the bin's tag.
* **Log gripper** (**left gripper** in Config L, **right gripper** in Config R). Ticks the sheet for every bin, takes every tag out of the
  tag cup, and hands over each tag for the other column. It is also the counting gripper for its own column.
* Only tags are handed over. Units, the marker, and the sheet are never handed over.

## Vocabulary

* **Cycle count:** counting the stock in a few bins and checking it against what the records say.
* **Count sheet:** the sheet on the log stand, one line per bin, read top to bottom.
* **Current line:** the top line whose bin is not yet finished. Only the bin on the current line is ever touched.
* **Expected quantity:** the number of units the sheet says the bin holds.
* **Count:** the number of units in the bin, found by moving them one at a time into the count tray. It is the number of the highest
  filled pocket.
* **Variance:** the count differs from the expected quantity.
* **Recount:** a second full count of the same bin, made the same way, only after a variance.
* **Discrepancy:** the recount still differs from the expected quantity. A discrepancy gets a tag. If the recount matches the expected
  quantity, there is no discrepancy and no tag.
* **Counting gripper:** the gripper of the current bin's column.
* **Log gripper:** the gripper on the log stand's side, the **left gripper** in Config L and the **right gripper** in Config R.
* **Front unit:** the unit nearest the front of the bin. Units always come out front unit first.
* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down into a bin from above.
* **Next pocket:** the lowest-numbered empty pocket of the count tray. Each unit goes into the next pocket, so the filled pockets always run
  from 1 upward with no gap.
* **Set unit:** the unit stands upright on the floor of its pocket or its bin slot, SKU label facing out, and stays put when the gripper
  opens.
* **Tick:** one mark with the marker inside a tick box: a short stroke down and to the right, then a longer stroke up and to the right,
  without lifting.
* **Hung tag:** the tag's clip is pushed all the way down over the middle of the bin's front lip, the tag hangs straight down in front of
  the bin, printed side out, and it stays there with the gripper off it.
* **Hand over:** the log gripper brings the tag to the hand-over point and holds it still for a **half-second hold**. The counting gripper
  then closes on the far edge of it. Only after the counting gripper is closed does the log gripper open and draw back.
* **Clear of the shelving:** the arm is drawn back so that no part of it is in front of a bin, the count tray, or the log stand.

## Steps

Run Steps 1 to 5 once for each line of the count sheet, top to bottom: A1, A2, B1, B2, C1, C2. Then end the episode with Step 6. Step 4
runs only after a variance, and Step 5 only after a discrepancy. Only the log gripper and the tag hand-over depend on the config.

### Step 1: Count the bin

**Goal:** every unit in the current bin is in the count tray, filling pockets 1 upward, and the bin is empty.

#### 1.1 Read the current line

* Read the **current line** on the count sheet: its bin and its **expected quantity**.
* Find the bin whose **location label** matches it. That bin's column decides the **counting gripper**: the **left gripper** for A1, B1,
  C1 and the **right gripper** for A2, B2, C2.

**Check:** one bin matches the line, and the count tray is empty.

#### 1.2 Move the units into the count tray

* With the **counting gripper**, come level into the bin from the front and close on the two sides of the **front unit**.
* With the **counting gripper**, lift it just clear of the bin floor, draw it straight out, level, and carry it to the **next pocket** of
  the count tray.
* With the **counting gripper**, set it down in that pocket, upright, SKU label out, then open and lift straight up.
* With the **counting gripper**, go back for the next front unit, and keep going one unit at a time until the bin is empty.
* With the other gripper, stay open and **clear of the shelving**.

**Check:** the bin is empty to its back wall, the filled pockets run from 1 upward with no gap, and each pocket holds one unit. The number
of the highest filled pocket is the **count**.

**Expected state:** the bin is empty and its units stand in the count tray.

### Step 2: Log the count

**Goal:** the current line carries one tick in the box of the count, on the COUNT row the first time and on the RECOUNT row after a
recount.

* **IF Config L:** the **left gripper** is the log gripper. **IF Config R:** the **right gripper** is the log gripper.
* With the **log gripper**, close on the **barrel** of the marker, not on its point, and lift it straight up out of its clip.
* With the **log gripper**, bring the marker point level to the current line's row, to the box numbered with the count, and draw one
  **tick** inside it, then draw the point straight back off the sheet.
* With the **log gripper**, press only hard enough to leave a mark, then stand the marker back in its clip, point down, and open.
* With the other gripper, stay open and **clear of the shelving** unless it is the log gripper.

**Check:** the row carries one tick, in the box whose number matches the filled pockets. If a tick has run outside its box, leave it. Do
not draw over it and do not draw a second tick on that row.

**Expected state:** the count is logged, the marker is in its clip, and the units are still in the count tray.

### Step 3: Return the units

**Goal:** every unit from the count tray is back in its own bin, filling from the back, and the tray is empty.

* With the **counting gripper**, close on the sides of the unit in the **highest-numbered** filled pocket and lift it straight up out of
  the tray.
* With the **counting gripper**, carry it level into the bin and set it down in the back-most empty place, upright, SKU label out, touching
  the unit behind it.
* With the **counting gripper**, open and draw straight out to the front, level.
* With the **counting gripper**, keep going one unit at a time, highest pocket first, until the tray is empty.

**Check:** the tray is empty, and the bin holds the same number of units as the count, in one row from the back, upright, labels out. If a
unit has tipped, close on it with the **counting gripper** and stand it up in its place.

**Expected state:** the bin holds all its units again and the tray is empty. Now compare the count with the expected quantity.

### Step 4: Recount any variance

**Goal:** a bin with a variance has been counted a second time and the recount is logged.

* **IF the count matches the expected quantity:** there is no variance. Skip Steps 4 and 5 and go to the next line.
* **IF the count differs from the expected quantity:** run Step 1.2, Step 2 on the **RECOUNT** row, and Step 3 again for the same bin,
  with the same grippers.

**Check:** the RECOUNT row carries one tick, and the bin holds all its units again with the tray empty.

**Expected state:** the recount is logged. Now compare the recount with the expected quantity.

### Step 5: Flag a discrepancy

**Goal:** a bin whose recount still differs from the expected quantity carries a **hung tag**.

* **IF the recount matches the expected quantity:** there is no discrepancy. Hang no tag and go to the next line.
* **IF the recount differs from the expected quantity:** run 5.1 and 5.2.

#### 5.1 Take a tag to the bin

* With the **log gripper**, close on the top of one **discrepancy tag**, above its clip, and lift it straight up out of the tag cup.
* **IF the bin is in the log gripper's own column:** with the **log gripper**, carry the tag level to the front of the bin.
* **IF the bin is in the other column:** with the **log gripper**, carry the tag to the **hand-over point** and hold it still for a
  **half-second hold**. With the **counting gripper**, close on the far edge of the tag. With the **log gripper**, open and draw back
  **clear of the shelving**. With the **counting gripper**, carry the tag level to the front of the bin.

**Check:** the **counting gripper** holds one tag, printed side out, clip at the top and open side down.

#### 5.2 Hang the tag on the bin

* With the **counting gripper**, bring the tag's clip level to just above the middle of the bin's front lip.
* With the **counting gripper**, push the clip straight down over the lip until it stops, then open and draw straight back, level.
* With the **counting gripper**, do not reach into the bin and do not cover the location label.

**Check:** the tag is **hung**. If it hangs crooked or only part way on, close on it with the **counting gripper** and push it straight
down again.

**Expected state:** the discrepancy is flagged on the bin, the tray is empty, and the next line can start.

### Step 6: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the count done.

* Look once across the shelving and the log stand: every line has a COUNT tick, every variance has a RECOUNT tick, every discrepancy bin
  has a hung tag, every unit is back in its bin, the tray is empty, and the marker is in its clip.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the cycle count is done and still, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take every hung tag off its bin and stand it back in the tag cup, so the cup holds three.
2. Take the ticked sheet out of its holder and put in a fresh one. Check the marker still marks.
3. Choose one or two bins at random for the next episode. Add or take away one unit in each, so they differ from the sheet by one. Set every
   other bin back to its expected quantity.
4. Check every bin's units stand in one row from the back, upright, labels out, and the count tray is empty.
5. Move the log stand to the end of the ledge for the next episode's config.
6. Pick up anything that landed on a shelf, the ledge, or the floor.
7. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the reviewer sees.
The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the shelving shifts in frame, the shelf edges change angle or size in frame, or the base rolls, creeps, or turns at any
  point after recording starts.
* **SOP rule broken:** Steps 1 to 6, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Approached from above or fouled the shelf**

* **Visible cue:** a gripper comes down into a bin from above instead of coming in level from the front, or a wrist, forearm, unit, or tag
  knocks, scrapes, or rests on the shelf above a bin.
* **SOP rule broken:** Steps 1.2, 3, and 5.2, every reach into a bin is a front approach, level, straight in and straight out.
* **Coaching note:** straight in from the front, straight out the same way.

**Violation: Leaned on or pushed the shelving, ledge, or stand**

* **Visible cue:** a gripper, wrist, or forearm rests on a shelf, an upright, a bin, the ledge, or the log stand; a bin shifts; or the stand
  rocks or slides.
* **SOP rule broken:** Steps 1 to 5, the shelving, the ledge, and the log stand carry no weight from the arms.
* **Coaching note:** the arm holds itself up. Press only as hard as the move needs.

**Violation: Sheet not followed**

* **Visible cue:** a line is skipped, bins are counted out of top-to-bottom order, or a bin is touched that is not on the current line.
* **SOP rule broken:** Step 1.1, read the sheet top to bottom, one current line at a time.
* **Coaching note:** read the line, then move. The sheet is the order.

**Violation: Count not made by moving**

* **Visible cue:** a count is logged without the bin being emptied into the tray; a unit is left in the bin; two units are moved at once;
  or the gripper counts by pushing or tapping units in the bin.
* **SOP rule broken:** Step 1.2, take every unit out one at a time, front unit first, until the bin is empty to its back wall.
* **Coaching note:** a hidden unit is not a counted unit. Empty the bin, one by one.

**Violation: Pocket order broken**

* **Visible cue:** a unit goes into a pocket other than the next pocket, two units share a pocket, a gap is left between filled pockets, or
  units from two bins are in the tray at the same time.
* **SOP rule broken:** Steps 1.1 and 1.2, the tray starts empty and each unit goes into the lowest-numbered empty pocket.
* **Coaching note:** 1, 2, 3, in order. The tray is the count, so keep it honest.

**Violation: Wrong count logged**

* **Visible cue:** the ticked box does not match the number of the highest filled pocket, or the tick is on the line of another bin.
* **SOP rule broken:** Step 2, tick the box numbered with the count, on the current line's row.
* **Coaching note:** read the tray, then find the number. Tick what is there, not what the sheet expects.

**Violation: Log filled in wrong**

* **Visible cue:** a row is ticked twice; a tick is drawn over; a COUNT tick goes on the RECOUNT row or the other way round; the count is
  logged after the units are back in the bin; or any other mark is made on the sheet.
* **SOP rule broken:** Step 2, one tick per row, on the right row, while the units are still in the tray.
* **Coaching note:** one tick, the right row, the right box. The log is the record.

**Violation: Marker handled wrong**

* **Visible cue:** the marker is held by its point, pressed hard enough to bend its tip or push the sheet, laid on the ledge, dropped,
  carried to a bin, or not stood back in its clip point down.
* **SOP rule broken:** Step 2, hold the marker by its barrel and stand it back in its clip, point down, after every tick.
* **Coaching note:** barrel in the gripper, light on the sheet, back in the clip.

**Violation: Units not returned or returned wrong**

* **Visible cue:** a unit is left in the tray; a unit goes into a bin other than its own; a unit is set crooked, on its side, label in, or
  with a gap behind it; or the next line starts with units still in the tray.
* **SOP rule broken:** Step 3, return every unit to its own bin, highest pocket first, back-most empty place first, upright, label out.
* **Coaching note:** every unit goes home before the next bin. The bin ends as a tidy row.

**Violation: Recount rule broken**

* **Visible cue:** a bin whose count differs from the expected quantity is not recounted; a bin whose count matches is recounted; or the
  recount is made without emptying the bin into the tray again.
* **SOP rule broken:** Step 4, recount only after a variance, and recount the whole bin the same way as the first count.
* **Coaching note:** compare the count with the sheet before you move on. A variance always gets a second count.

**Violation: Tag missed or hung without cause**

* **Visible cue:** a bin whose recount still differs from the sheet gets no tag; a tag is hung on a bin with no variance or whose recount
  matched; or two tags are hung on one bin.
* **SOP rule broken:** Step 5, hang one tag only when the recount still differs from the expected quantity.
* **Coaching note:** the recount decides. Differs, tag it. Matches, leave it.

**Violation: Tag hung wrong**

* **Visible cue:** the tag is hung on the wrong bin, off the middle of the lip, crooked, only part way on, face in, over the location label,
  or it falls off when the gripper opens.
* **SOP rule broken:** Step 5.2, push the clip straight down over the middle of the bin's front lip until it stops, printed side out.
* **Coaching note:** middle of the lip, straight down, face out. A tag nobody can read flags nothing.

**Violation: Hand-over done wrong**

* **Visible cue:** the log gripper opens before the counting gripper has closed; the tag is still moving when the counting gripper closes,
  with no half-second hold; the hand-over happens away from the hand-over point; or a tag for the log gripper's own column is handed over.
* **SOP rule broken:** Step 5.1, hand over only tags for the other column, at the hand-over point, held still, and open only after the
  counting gripper has closed.
* **Coaching note:** stop, hold still, let the counting gripper take it, then open.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the ledge is not set up in: the gripper away from the log stand ticks the sheet or takes a tag, a
  gripper reaches for a ledge end with no stand, or the stand is moved before or during the episode.
* **SOP rule broken:** Steps 2 and 5.1, look at the ledge, find the log stand, and follow the IF line that matches the config the episode is
  set up in.
* **Coaching note:** look at the stand before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** the next bin is touched before the current bin is finished; the count is logged before the bin is empty; the units go
  back before the count is logged; or a tag is hung before the recount.
* **SOP rule broken:** Steps 1 to 5, for each bin: count, log, return, then recount and tag only if needed, before the next line.
* **Coaching note:** one bin at a time, start to finish. The order is the task.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two units, or a unit and the marker or a tag; both grippers carry different things at the same time
  outside a hand-over; or a gripper holds something while the other works instead of being clear of the shelving.
* **SOP rule broken:** Steps 1 to 5, one gripper holds one thing, and the other is empty, taking a hand-over, or clear of the shelving.
* **Coaching note:** one thing, one trip.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a unit left at the back
  of the bin, a tipped unit, or a tag only part way on.
* **SOP rule broken:** Steps 1.1 to 5.2, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a unit, the marker, or a tag is dropped on a shelf, the ledge, or the floor; a unit in a bin or the tray is knocked over;
  the tag cup is tipped; or a unit is knocked out of its bin.
* **SOP rule broken:** Steps 1 to 5, nothing is dropped or knocked out of its place, and every gripper comes out the way it went in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **left gripper** goes into A2, B2, or C2; the **right gripper** goes into A1, B1, or C1; the gripper away from the log
  stand touches the stand, the marker, or the tag cup; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 5, each gripper works its own column, only the log gripper works the log stand, and the arms never cross.
* **Coaching note:** left column, left arm. Right column, right arm. The stand side decides who logs.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a line not counted or logged, a variance not recounted, a discrepancy bin without a tag, a unit in the
  tray, the marker out of its clip, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 6, look once across the shelving and the log stand, then return both arms home with grippers open and stop
  recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read the count tray, the sheet, a location label, or a hung tag**, so the count, the ticks, or the flags cannot be judged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Setup fault:** a bin seeded with more than six units or none, no bin or more than two bins seeded with a variance, a sheet line that does
  not match a bin, a tag clip that will not hold, or a marker that has dried out.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so the back of a bin, a pocket, the
  hand-over point, the sheet, or the tag cup cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Read one count-sheet line
2. Take the front unit out of a bin
3. Set one unit in the next pocket
4. Take the marker from its clip
5. Tick one count box
6. Stand the marker back in its clip
7. Return one unit from the tray to its bin
8. Take a tag out of the tag cup
9. Hand a tag over at the hand-over point
10. Hang a tag on a bin's front lip
11. Return both arms home and end the episode
