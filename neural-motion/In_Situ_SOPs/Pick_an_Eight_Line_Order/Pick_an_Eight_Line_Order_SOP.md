# Pick an Eight-Line Order SOP (1x Episode: eight lines, in situ)

One episode picks one eight-line order into one order tote, at the two shelf bays where the stock lives. The base is
**passive**: it has no drive of its own, so it is pushed by hand to the front of the bays and locked there, and nothing is
carried away to a table. Everything the episode touches is already at the bays when recording starts: the stocked bins,
the scanner in its holster, and the pick cart with its empty order tote and its pick list.

The episode runs these four actions in this order and no other: **walk the pick list across the shelf bays, pick eight
SKUs to the order tote, scan-confirm each one, stage the tote.** Scan-confirming is not saved for the end: each item is
scanned straight after it comes out of its bin, before it goes into the tote and before the next line is read.

The bays are worked **as found**. The pick cart stands braked against one end of the bays. The empty **order tote** sits
on the **fill spot** of its top deck and the **pick list** sits in the list clip on the cart handle. Each of the eight bins
holds three units of one SKU. The episode ends with one unit of each of the eight SKUs standing in the order tote, every
pick scanned green, the pick list in the tote's list pocket, and the tote slid onto the **staged spot** of the cart.

**The pick list sets the order.** It is printed in walk order and read top to bottom, one line at a time. Its **BAY 1**
lines come first, then its **BAY 2** lines. Each line names a **location**, the **SKU**, and the quantity, which is always
one. The order of the lines within each bay changes from episode to episode, so the list is read every time and never
worked from memory.

**This is an in-situ task, and three things follow from that.** First, **each shelf level has a shelf directly above
it**, so **every reach into a bin is from the front, straight in, level**. No gripper comes down into a bin from above.
Second, the **bays and the cart are never leaned on and never pushed**: no gripper, wrist, or forearm rests on a shelf, an
upright, a bin, or the cart, and the bins are fixed and never pulled out. Third, **each item goes from its bin to the tote
and nowhere else**: nothing is set down on a shelf edge, another bin, the cart deck, or the floor on the way.

The bays are set up in one of two ways. Only the **pick cart** moves. The bins, the scanner holster, and the stock in
each bin are in the same place in both.

* **Config L:** the pick cart stands against the **left end** of the bays, beside Bay 1.
* **Config R:** the pick cart stands against the **right end** of the bays, beside Bay 2.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says
so on an **IF** line. Look at the bays and follow the line that matches.

What stays constant across all sessions:

* **Bay rule:** the **left gripper** picks from **Bay 1** and the **right gripper** from **Bay 2**. The gripper that picks
  an item scans it.
* **Cart-side rule:** the gripper on the cart's side sets every item in the tote and stages the tote. That is the **left
  gripper** in Config L and the **right gripper** in Config R. It is called the **cart gripper**.
* **Hand-over rule:** when an item comes from the bay away from the cart, the picking gripper scans it and then **hands it
  over** to the cart gripper at the **hand-over point**. No arm reaches across the bays.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches over,
under, around, or past the other. Nothing is moved two at a time: one gripper holds one thing, and the other gripper is
empty, taking a hand-over, or clear of the bays.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or
repositioned once recording starts. It is parked once, before recording, and does not move again until the episode is
over.

1. Push the base by hand up to the bays and stop it **square to their front**, so the shelf edges run straight across the
   frame of the camera.
2. Stop it **centered on the bays**, so the middle of the base is in line with the middle upright between Bay 1 and Bay 2.
3. Stop it **close enough** that both grippers reach into the back of a bin straight in and level without either arm
   extending, and **far enough** that neither arm, wrist, nor any part of the base touches a shelf, an upright, or the cart
   while both arms work.
4. Check the **height band**: both grippers come level into every bin on level A and level B without a wrist or forearm
   touching the shelf above it.
5. Check the **left side**: the **left gripper** reaches into all four Bay 1 bins, the scanner window, and the hand-over
   point, all without extending.
6. Check the **right side**: the **right gripper** reaches into all four Bay 2 bins, the scanner window, and the hand-over
   point, all without extending.
7. Check the **cart** for the config this episode runs: the **cart gripper** reaches every corner of the order tote on the
   fill spot, the list clip, and the far end of the staged spot.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not work bays the arms
   cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the bays hard enough to shift
it, nothing touches it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the
episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the middle upright and its frame includes both bays: all eight bins and their
   labels, the scanner and its light, and the cart with its fill spot, staged spot, and list clip.
3. The camera reads every **location label** and the **SKU label** on the front unit of every bin, so which item came from
   which bin is readable.
4. The camera reads the **pick list** in its clip well enough to follow its lines.
5. The camera sees the **scanner light**, so each green or red scan is readable.
6. The camera sees into the order tote well enough to count the items in it.
7. Both arms are at home with grippers open.
8. The **left arm** reaches all four Bay 1 bins, the scanner window, and the hand-over point without extending to a joint
   limit.
9. The **right arm** reaches all four Bay 2 bins, the scanner window, and the hand-over point without extending to a joint
   limit.
10. The cart arm for this config reaches the whole tote, the list clip, and the staged spot without extending to a joint
    limit.
11. Both grippers come in and go out of every bin **from the front and level**, and neither wrist nor forearm touches the
    shelf above on the way in or out.
12. The two arms do not collide, and neither arm passes in front of the other.
13. If a place cannot be reached, re-park the base by the Base positioning steps until lines 8 to 12 hold.

### Materials checklist

1. The **two shelf bays** stand where they live, side by side and fixed to the wall or the floor. They are not moved, not
   leaned on, and not pushed at any point.
2. **Bay 1** is on the left and **Bay 2** on the right. A **middle upright** stands between them.
3. Each bay has **two working levels**, each with a shelf directly above it. **Level A** is the upper level and **level B**
   the lower.
4. Each level of each bay holds **two open-front bins**, fixed side by side. That makes **eight bins**, named by bay, level,
   and slot, left to right: **1-A1, 1-A2, 1-B1, 1-B2** in Bay 1 and **2-A1, 2-A2, 2-B1, 2-B2** in Bay 2.
5. Each bin has a **location label** on the shelf edge right below it, with its name in large print.
6. Each bin holds **three units of one SKU**, standing upright in a single row from the front of the bin to the back, SKU
   label up and facing out. Every unit is a small boxed item that fits one gripper. No two bins hold the same SKU.
7. The **scanner** stands fixed in its **holster** on the middle upright, between level A and level B, window facing out.
   It stays in its holster for the whole episode. It reads a barcode by itself when the barcode is held about a hand in
   front of its window: a **green** light and one beep if the SKU is the one the current pick-list line names, a **red**
   light and a buzz if it is not.
8. The **pick cart** is a flat-top cart standing braked against the **left end** of the bays in **Config L** and against the
   **right end** in **Config R**, its top deck at about the height of level B.
9. The top deck has two taped spots. The **fill spot** is the half of the deck nearest the bays. The **staged spot** is the
   half nearest the cart handle, marked **STAGED**, with a low **stop lip** along the handle end of the deck.
10. The **order tote** stands empty on the fill spot, square to the deck edges. It is an open tote big enough for eight units
    standing in two rows of four. A clear **list pocket** is fixed on the side of the tote facing the base.
11. The **pick list** is a card in the **list clip** on the cart handle, facing the camera. It has a **BAY 1** section of four
    lines above a **BAY 2** section of four lines. Each line reads location, SKU, quantity 1. The order of the lines within
    each section is shuffled per episode.
12. Every SKU on the list matches the SKU in exactly one bin, and every bin is on the list once.
13. Nothing else stands on the bays or the cart within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the location labels and the two cart spots. You judge every other place by
eye against the bays themselves.

* **Shelf bays:** the fixed bays the base is parked at. Never moved, never leaned on, never pushed.
* **Bay 1:** the left bay, bins 1-A1, 1-A2 on level A and 1-B1, 1-B2 on level B. **Left gripper only.**
* **Bay 2:** the right bay, bins 2-A1, 2-A2 on level A and 2-B1, 2-B2 on level B. **Right gripper only.**
* **Scanner:** fixed in its holster on the middle upright between the levels. Either gripper holds an item up to it, one at
  a time.
* **Hand-over point:** in front of the middle upright, a hand out from the shelf edge of level A, above the scanner.
* **Pick cart:** braked against the left end (Config L) or the right end (Config R) of the bays: fill spot, staged spot,
  and list clip on the handle. **Cart gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works Bay 1 and the **right gripper** works Bay 2. The **cart gripper** also works the cart.
* The two arms meet only at the **hand-over point**, and both use the scanner, one at a time.
* Neither arm goes into a bin in the other bay, and neither reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds one thing, and while it does, the other gripper is empty, taking a
  hand-over, or drawn **clear of the bays**.

### Arm assignments

* **Cart gripper** (**left gripper** in Config L, **right gripper** in Config R). Picks and scans the lines of its own bay,
  takes each hand-over, sets every item in the tote, posts the pick list, and slides the tote to the staged spot.
* **Other gripper.** Picks and scans the lines of its own bay and hands each item over to the cart gripper. It never
  touches the cart or the tote.
* Only items are handed over. The tote and the list are never handed over, and the scanner never leaves its holster.

## Vocabulary

* **Pick list:** the card in the list clip. It is read top to bottom, BAY 1 first, then BAY 2.
* **Current line:** the top line not yet picked, scanned green, and set in the tote. Only the bin on the current line is
  ever reached into.
* **Location:** one bin, named by the label under it (for example 2-B1): bay, level, slot.
* **SKU label:** the label on a unit that names it. It must match the SKU on the current line.
* **Front unit:** the unit nearest the front of its bin. It is the only unit ever taken.
* **Picking gripper:** the gripper whose bay holds the current line's bin. It takes the unit and scans it.
* **Cart gripper:** the gripper on the cart's side, the **left gripper** in Config L and the **right gripper** in Config R.
* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down into a bin from
  above.
* **Scan-confirm:** straight after the unit comes out of its bin, the picking gripper holds the unit's SKU label about a hand
  in front of the scanner window, still, until the light shows. The scanner is never touched.
* **Green / red:** green light and one beep is a confirmed pick. Red light and a buzz means the unit is not the SKU the
  current line names.
* **Hand over:** the picking gripper brings the scanned unit to the hand-over point and holds it still for a **half-second
  hold**. The cart gripper then closes on the far side of it. Only after the cart gripper is closed does the picking gripper
  open and draw back.
* **Tote order:** units go into the tote standing, SKU label up, in two rows of four. The first row runs along the side of
  the tote nearest the bays and the second row along the side nearest the base. Each row fills from the end of the tote
  nearest the middle upright outward, each unit beside the one before, never on top of another.
* **Placed unit:** the unit stands on the tote floor in its place in the tote order, upright, SKU label up, and stays put when
  the gripper opens.
* **Staged tote:** the tote sits inside the STAGED tape, square, its end against the stop lip, with the pick list in its list
  pocket and nothing on the fill spot.
* **Clear of the bays:** the arm is drawn back so that no part of it is in front of a bin, the scanner, or the cart.

## Steps

Run Steps 1 to 3 in order, and end the episode with Step 4. Steps 1 and 2 are the pick list's two sections, each line
picked, scanned, and set in the tote before the next line is read. Step 3 stages the tote. Only the cart gripper and the
hand-overs depend on the config.

### Step 1: Pick the Bay 1 lines

**Goal:** one unit of each of the four Bay 1 SKUs is **placed** in the tote, and each pick is scanned green.

Run 1.1 to 1.4 for each BAY 1 line, top to bottom.

#### 1.1 Read the current line

* Read the **current line** on the pick list: its location and its SKU.
* Find the Bay 1 bin whose **location label** matches it, and check that the SKU label on its **front unit** matches the
  line.

**Check:** one bin matches the line and its front unit carries the line's SKU. If no bin matches, stop and log a system
issue.

#### 1.2 Take the front unit

* With the **left gripper**, come level into the bin from the front, just above the bin floor, and close on the two sides of
  the **front unit**.
* With the **left gripper**, lift it just clear of the bin floor and draw it straight out to the front, level, touching no
  other unit.
* With the **right gripper**, stay open and **clear of the bays** unless it is the cart gripper waiting at the hand-over
  point.

**Check:** the left gripper holds one unit by its sides, and the two units left in the bin still stand upright in their row.
If a unit left in the bin has tipped, finish this line first, then stand it up with the **left gripper** before reading the
next line.

#### 1.3 Scan-confirm the unit

* With the **left gripper**, carry the unit level to the scanner and hold its **SKU label** about a hand in front of the
  scanner window, still, until the light shows.
* **IF green:** the pick is confirmed. Go on to 1.4.
* **IF red:** with the **left gripper**, carry the unit back and set it down in its bin, at the front of the row, SKU label
  up and out, then draw straight out. Read the line again and go back to 1.1.

**Check:** the scan was green, the unit never touched the scanner, and the scanner still stands in its holster.

#### 1.4 Put the unit in the tote

* **IF Config L:** the **left gripper** is the cart gripper. With the **left gripper**, carry the unit level to the tote and
  bring it down to just above the tote floor at its place in the **tote order**.
* **IF Config R:** the **right gripper** is the cart gripper. With the **left gripper**, carry the unit to the
  **hand-over point** and hold it still for a **half-second hold**. With the **right gripper**, close on the far side of the
  unit. With the **left gripper**, open and draw back **clear of the bays**. With the **right gripper**, carry the unit level
  to the tote and bring it down to just above the tote floor at its place in the **tote order**.
* Then, in both: with the **cart gripper**, set the unit down on the tote floor, upright, SKU label up, then open and lift
  straight up out of the tote.
* With the **cart gripper**, do not let the unit go from above the tote floor and do not set it on top of another unit.

**Check:** the unit is **placed**. If it has tipped, close on it with the **cart gripper** and stand it up in its place.

**Expected state:** four Bay 1 units are placed in the tote in the tote order, each scanned green, and each Bay 1 bin holds
two units in an upright row.

### Step 2: Pick the Bay 2 lines

**Goal:** one unit of each of the four Bay 2 SKUs is **placed** in the tote, and each pick is scanned green.

Run 2.1 to 2.4 for each BAY 2 line, top to bottom. These are the moves of Step 1, made by the **right gripper** in Bay 2.

#### 2.1 Read the current line

* Read the **current line**: its location and its SKU.
* Find the Bay 2 bin whose **location label** matches it, and check the SKU label on its **front unit**.

**Check:** one bin matches the line and its front unit carries the line's SKU.

#### 2.2 Take the front unit

* With the **right gripper**, come level into the bin from the front, close on the sides of the **front unit**, lift it just
  clear of the bin floor, and draw it straight out, touching no other unit.
* With the **left gripper**, stay open and **clear of the bays** unless it is the cart gripper waiting at the hand-over
  point.

**Check:** the right gripper holds one unit by its sides, and the two units left in the bin still stand upright in their row.
If a unit left in the bin has tipped, finish this line first, then stand it up with the **right gripper** before reading the
next line.

#### 2.3 Scan-confirm the unit

* With the **right gripper**, hold the unit's **SKU label** about a hand in front of the scanner window, still, until the
  light shows.
* **IF green:** go on to 2.4.
* **IF red:** with the **right gripper**, set the unit back in its bin at the front of the row, SKU label up and out, read
  the line again, and go back to 2.1.

**Check:** the scan was green and the scanner still stands in its holster.

#### 2.4 Put the unit in the tote

* **IF Config R:** the **right gripper** is the cart gripper. With the **right gripper**, carry the unit level to the tote,
  to its place in the **tote order**.
* **IF Config L:** the **left gripper** is the cart gripper. With the **right gripper**, carry the unit to the
  **hand-over point** and hold it still for a **half-second hold**. With the **left gripper**, close on the far side of the
  unit. With the **right gripper**, open and draw back **clear of the bays**. With the **left gripper**, carry the unit
  level to the tote, to its place in the **tote order**.
* Then, in both: with the **cart gripper**, set the unit down on the tote floor, upright, SKU label up, then open and lift
  straight up out of the tote.

**Check:** the unit is **placed**. If it has tipped, close on it with the **cart gripper** and stand it up in its place.

**Expected state:** all eight units are placed in the tote in two rows of four, each scanned green, and every bin holds two
units in an upright row.

### Step 3: Stage the tote

**Goal:** the pick list is in the tote's list pocket and the tote is **staged**.

#### 3.1 Post the pick list

* With the **cart gripper**, close on the top edge of the **pick list**, draw it straight up out of the list clip, and carry
  it level to the tote.
* With the **cart gripper**, slide it down into the **list pocket** from the top, printed side facing the base, until it
  stops, then open and draw back.
* Hold the other gripper open and **clear of the bays** for the whole of this step.

**Check:** the list sits all the way down in the pocket and can be read through it.

#### 3.2 Slide the tote to the staged spot

* With the **cart gripper**, come to the end of the tote nearest the bays and press the gripper flat against the outside of
  that end, open, low on the tote wall.
* With the **cart gripper**, push the tote straight along the deck toward the handle, keeping it square to the deck edges,
  until its far end touches the **stop lip**.
* With the **cart gripper**, draw straight back from the tote and **clear of the bays**.
* With the **cart gripper**, never lift the full tote and never push it by a unit inside it.

**Check:** the tote is **staged**. If it sits crooked or short of the stop lip, press the same end again with the **cart
gripper** and push it straight on.

**Expected state:** the tote is staged with eight units and the pick list, the fill spot and the list clip are empty, and both
grippers are clear of the bays.

### Step 4: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the order picked and staged.

* Look once across the bays and the cart: every bin holds two upright units, the scanner is in its holster, the tote holds
  eight units in the tote order, and it sits staged with the list in its pocket.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the order is picked and staged, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the list out of the list pocket.
2. Take each unit out of the tote and stand it back at the front of the bin its SKU belongs to, so every bin holds three
   units in an upright row, SKU label up and facing out.
3. Slide the empty tote back onto the fill spot, square to the deck edges.
4. Put a different shuffled pick list in the list clip, facing the camera.
5. Move the cart to the end of the bays for the next episode's config and brake it.
6. Check every label is readable and the scanner stands in its holster and still lights.
7. Pick up anything that landed on a shelf, the cart, or the floor.
8. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the
reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule
was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the bays shift in frame, the shelf edges change angle or size in frame, or the base rolls, creeps, or turns
  at any point after recording starts.
* **SOP rule broken:** Steps 1 to 4, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Approached from above or fouled the shelf**

* **Visible cue:** a gripper comes down into a bin from above instead of coming in level from the front, or a wrist, forearm,
  or unit knocks, scrapes, or rests on the shelf above a bin.
* **SOP rule broken:** Steps 1.2 and 2.2, every reach into a bin is a front approach, level, straight in and straight out.
* **Coaching note:** straight in from the front, straight out the same way.

**Violation: Leaned on or pushed the bays or cart**

* **Visible cue:** a gripper, wrist, or forearm rests on a shelf, an upright, a bin, or the cart; a bin shifts; or the cart or
  a bay rocks or moves.
* **SOP rule broken:** Steps 1 to 3, the bays and the cart carry no weight and nothing fixed is pushed out of place.
* **Coaching note:** the arm holds itself up. Press only as hard as the pick needs.

**Violation: Pick list not followed**

* **Visible cue:** a line is skipped, lines are taken out of top-to-bottom order, a Bay 2 line is picked before every Bay 1
  line is done, or a bin is reached into that is not on the current line.
* **SOP rule broken:** Steps 1.1 and 2.1, read the list top to bottom, BAY 1 first, one current line at a time.
* **Coaching note:** read the line, then move. The list is the walk, not the shelf.

**Violation: Wrong bin**

* **Visible cue:** a unit is taken from a bin other than the one the current line names, including the bin next to it or the
  same slot on the other level.
* **SOP rule broken:** Steps 1.1 and 2.1, find the bin whose label matches the line before the arm goes in.
* **Coaching note:** match the label under the bin to the line. Bins that look alike are not the same bin.

**Violation: Wrong quantity**

* **Visible cue:** a gripper comes out of a bin with two units, a second unit of the same SKU goes into the tote, or a line
  ends with no unit in the tote.
* **SOP rule broken:** Steps 1.2 to 1.4 and 2.2 to 2.4, every line is quantity one: one unit out, one unit in.
* **Coaching note:** one line, one unit. Count what is in the gripper before it leaves the bin.

**Violation: Not the front unit or bin left disturbed**

* **Visible cue:** a unit is taken from the middle or back of the row; units left in the bin are pulled forward, tipped, turned,
  or pushed crooked; or a unit is dragged out along the bin floor.
* **SOP rule broken:** Steps 1.2 and 2.2, take only the front unit, lift it just clear, and draw it straight out touching no
  other unit.
* **Coaching note:** front unit only, lift then draw. The next picker needs the row as you found it.

**Violation: Item held wrong**

* **Visible cue:** a unit is held by its top, its label, one end, or a corner instead of its two sides, or it is held so the
  SKU label is covered when it reaches the scanner.
* **SOP rule broken:** Steps 1.2 and 2.2, close on the two sides of the unit.
* **Coaching note:** sides in the gripper, label free for the scanner.

**Violation: Scan skipped or done out of turn**

* **Visible cue:** a unit goes into the tote without a scan; the scan happens after the unit is in the tote or after a
  hand-over; the next line is read before the green light; or a location label is scanned instead of the unit's SKU label.
* **SOP rule broken:** Steps 1.3 and 2.3, the picking gripper scans the unit's SKU label straight after it leaves the bin, and
  waits for green before the unit goes on.
* **Coaching note:** pick, scan, green, then the tote. The scan is the record that the right thing was picked.

**Violation: Red scan ignored**

* **Visible cue:** a red light and buzz is followed by a hand-over or a put into the tote instead of the unit going back to its
  bin, or the same unit is held up again and again until the operator moves on.
* **SOP rule broken:** Steps 1.3 and 2.3, on red, set the unit back at the front of its bin, read the line again, and pick again.
* **Coaching note:** red means the wrong thing is in the gripper. Fix the pick, not the scan.

**Violation: Scanner handled or knocked**

* **Visible cue:** a gripper takes the scanner out of its holster, a unit or gripper bumps the scanner window, or the scanner
  is turned or knocked in its holster.
* **SOP rule broken:** Steps 1.3 and 2.3, hold the unit a hand in front of the scanner window; the scanner stays in its holster
  and is never touched.
* **Coaching note:** bring the label to the scanner and stop a hand short.

**Violation: Hand-over done wrong**

* **Visible cue:** the picking gripper opens before the cart gripper has closed; the unit is still moving when the cart gripper
  closes, with no half-second hold; the hand-over happens away from the hand-over point; a unit from the cart's own bay is
  handed over; or a unit is handed over before its green scan.
* **SOP rule broken:** Steps 1.4 and 2.4, hand over only units from the bay away from the cart, after the green scan, at the
  hand-over point, held still, and open only after the other gripper has closed.
* **Coaching note:** scan, stop, hold still, let the cart gripper take it, then open.

**Violation: Unit dropped in or not placed**

* **Visible cue:** a unit is let go from above the tote floor and falls in, lies on its side, stands with its SKU label down, or
  rests on the tote rim or against the tote wall at a slant.
* **SOP rule broken:** Steps 1.4 and 2.4, set each unit down on the tote floor, upright, SKU label up, before opening.
* **Coaching note:** down to the floor, then open. A dropped unit is a damaged unit.

**Violation: Tote order not kept**

* **Visible cue:** a unit is set on top of another, set in the second row before the first row is full, set away from the unit
  before it, or pushed in so the rows are crooked or crowded.
* **SOP rule broken:** Steps 1.4 and 2.4, units go in two rows of four, the row nearest the bays first, each row filling from the
  middle-upright end outward.
* **Coaching note:** next place in the row, every time. A tidy tote packs and checks fast.

**Violation: List not posted**

* **Visible cue:** the pick list is left in the clip, set loose in the tote or on the cart, stuck halfway in the pocket, put in
  facing the tote, or bent or torn.
* **SOP rule broken:** Step 3.1, the cart gripper slides the list all the way down into the list pocket, printed side facing the
  base.
* **Coaching note:** the list travels with the order. It goes in the pocket, all the way down.

**Violation: Tote not staged**

* **Visible cue:** the tote is lifted instead of slid; it is pushed by a unit inside it; it ends crooked, short of the stop lip,
  or outside the STAGED tape; or a unit tips or falls out during the push.
* **SOP rule broken:** Step 3.2, push the tote flat along the deck by the end nearest the bays until it touches the stop lip,
  square.
* **Coaching note:** low on the wall, slow and straight, stop at the lip.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the bays are not set up in: the gripper away from the cart sets a unit in the tote or
  touches the cart, a gripper carries a unit toward a cart end that is empty, or the cart is moved before or during the episode.
* **SOP rule broken:** Steps 1.4, 2.4, and 3, look at the bays, find the cart, and follow the IF line that matches the config the
  episode is set up in.
* **Coaching note:** look at the cart before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** a unit is taken before its line is read; the next line is read before the unit is placed in the tote; the list
  is posted or the tote pushed before all eight units are placed; or the tote is pushed before the list is posted.
* **SOP rule broken:** Steps 1 to 3, pick Bay 1, then Bay 2, each unit read, taken, scanned, and placed before the next line,
  then post the list and slide the tote.
* **Coaching note:** the order is the task. Each line leaves the bays ready for the next one.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two units, or a unit and the list; both grippers carry different units at the same time
  outside a hand-over; or a gripper holds a unit while the other works instead of being clear of the bays.
* **SOP rule broken:** Steps 1 to 3, one gripper holds one thing, and the other is empty, taking a hand-over, or clear of the bays.
* **Coaching note:** one thing, one trip.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a unit
  tipped in a bin or the tote, a list not all the way down in its pocket, or a tote crooked or short of the stop lip.
* **SOP rule broken:** Steps 1.1 to 3.2, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a unit, the list, or the tote is dropped or knocked on the cart, a shelf, or the floor; a unit in a bin or the
  tote is knocked over; or a unit is knocked out of its bin.
* **SOP rule broken:** Steps 1 to 3, nothing is dropped or knocked out of its place, and every gripper comes out the way it went
  in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **left gripper** goes into a Bay 2 bin; the **right gripper** goes into a Bay 1 bin; the gripper away from
  the cart touches the tote, the list, or the cart; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 3, each gripper picks from its own bay, only the cart gripper works the cart and the tote, and
  the arms never cross.
* **Coaching note:** Bay 1, left arm. Bay 2, right arm. The cart side decides who fills the tote.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with fewer or more than eight units in the tote, a pick not scanned green, the list outside
  its pocket, the tote not staged, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 4, look once across the bays and the cart, then return both arms home with grippers open and stop
  recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for
coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a location label, an SKU label, the pick list, the scanner light, or the inside of the tote**, so which
  unit came from where or whether a scan was green cannot be judged.
* **Scanner fault:** no light on a correctly held label, a green on a wrong SKU, or a red on the right one.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **List or stock fault:** a line with no matching bin, a bin with no line, a bin holding the wrong SKU or fewer than three units,
  or a torn or unreadable label.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a bin, the scanner, the
  hand-over point, or the far end of the staged spot cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Read one pick-list line
2. Take the front unit out of one bin
3. Scan one unit at the scanner
4. Set one unit back in its bin after a red scan
5. Hand one unit over at the hand-over point
6. Set one unit down in the tote
7. Post the pick list in the tote's list pocket
8. Slide the tote to the staged spot
9. Return both arms home and end the episode
