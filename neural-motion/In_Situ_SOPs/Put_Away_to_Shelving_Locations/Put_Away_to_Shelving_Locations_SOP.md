# Put Away to Shelving Locations SOP (1x Episode: one put list, in situ)

One episode puts away one cart load to its shelving locations, at the shelving unit where the locations live. The
base is **passive**: it has no drive of its own, so it is pushed by hand to the front of the shelving and locked
there, and nothing is carried away to a table. Everything the episode touches is already at the shelving when
recording starts: the put-away cart with its cases, its tote of eaches, and its put list, the labeled locations on
the shelving, the scanner in its holster, and the list box.

The episode runs these three actions in this order and no other: **shelve the cases and eaches to their labeled
locations per the put list, scan-confirm each one, clear the cart.** Scan-confirming is not saved for the end: each
item is scanned at its location straight after it is put there, before the next item is touched.

The shelving is worked **as found**. The put-away cart stands braked against one end of the shelving. On its top deck
stand **two cases** and one **put tote** holding **four eaches**, and the **put list** sits in the list clip on the
cart handle. Every location on the shelving is empty. The episode ends with each case and each each in the location
its put-list line names, every put scan-confirmed green, the empty tote on the cart's lower deck, the put list posted
in the list box, and the top deck of the cart bare.

**The put list sets the order.** It is read top to bottom, one line at a time. Its **CASES** lines come first, then
its **EACHES** lines. Each line names a **location**, the **item** by its SKU, and the quantity, which is always one.
The order of the lines within each section changes from episode to episode, so the list is read every time and never
worked from memory.

**This is an in-situ task, and three things follow from that.** First, **each shelf level has a shelf directly above
it**, so **every reach into a location is from the front, straight in, level**. No gripper comes down into a location
from above. Second, the **shelving and the cart are never leaned on and never pushed**: no gripper, wrist, or forearm
rests on a shelf, an upright, a bin, or the cart, and the bins are fixed and never pulled out. Third, **each item goes
where its line says and nowhere else**: nothing is set down on a shelf edge, another location, or the floor on the way.

The shelving is set up in one of two ways. Only the **put-away cart** moves. The locations, the scanner holster, and
the list box are in the same place in both.

* **Config L:** the put-away cart stands against the **left end** of the shelving.
* **Config R:** the put-away cart stands against the **right end** of the shelving.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it
says so on an **IF** line. Look at the shelving and follow the line that matches.

What stays constant across all sessions:

* **Cart-side rule:** the gripper on the cart's side takes every item off the cart and clears the cart. That is the
  **left gripper** in Config L and the **right gripper** in Config R. It is called the **cart gripper**.
* **Half rule:** the **left gripper** puts into the **left half** of the shelving (column 1 and 2 locations) and the
  **right gripper** into the **right half** (column 3 and 4 locations). The gripper that puts an item scans it.
* **Hand-over rule:** when an item's location is in the other half from the cart, the cart gripper **hands it over**
  to the other gripper at the **hand-over point**, and the other gripper puts it and scans it. No arm reaches across
  the shelving.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches
over, under, around, or past the other. Nothing is moved two at a time: one gripper holds one thing, and the other
gripper is empty, taking a hand-over, or clear of the shelving.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered,
nudged, or repositioned once recording starts. It is parked once, before recording, and does not move again until the
episode is over.

1. Push the base by hand up to the shelving and stop it **square to its front**, so the shelf edges run straight across
   the frame of the camera.
2. Stop it **centered on the shelving**, so the middle of the base is in line with the middle upright, between
   columns 2 and 3.
3. Stop it **close enough** that both grippers reach into the back of a location straight in and level without either
   arm extending, and **far enough** that neither arm, wrist, nor any part of the base touches a shelf, an upright, or
   the cart while both arms work.
4. Check the **height band**: both grippers come level into every location on level A and level B without a wrist or
   forearm touching the shelf above it.
5. Check the **left side**: the **left gripper** reaches into A1, A2, and B1, the hand-over point, the scanner holster,
   and the list box, all without extending.
6. Check the **right side**: the **right gripper** reaches into A3, A4, and B2, the hand-over point, the scanner holster,
   and the list box, all without extending.
7. Check the **cart** for the config this episode runs: the **cart gripper** reaches both cases, every each in the
   tote, the tote itself, the lower deck, and the list clip.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not work a shelving
   unit the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the shelving hard enough to
shift it, nothing touches it by hand, and it is never repositioned mid-task. A base that moves after recording starts
ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the shelving and its frame includes the whole of it: all six locations and
   their labels, the scanner holster, the list box, and the cart with its top deck, lower deck, and list clip.
3. The camera reads every **location label** and the **SKU label** on every item, so which item went into which
   location is readable.
4. The camera reads the **put list** in its clip well enough to follow its lines.
5. The camera sees the **scanner light**, so each green or red scan is readable.
6. Both arms are at home with grippers open.
7. The **left arm** reaches A1, A2, B1, the hand-over point, the holster, and the list box without extending to a joint
   limit.
8. The **right arm** reaches A3, A4, B2, the hand-over point, the holster, and the list box without extending to a joint
   limit.
9. The cart arm for this config reaches everything on the cart without extending to a joint limit.
10. Both grippers come in and go out of every location **from the front and level**, and neither wrist nor forearm
    touches the shelf above on the way in or out.
11. The two arms do not collide, and neither arm passes in front of the other.
12. If a place cannot be reached, re-park the base by the Base positioning steps until lines 7 to 11 hold.

### Materials checklist

1. The **shelving unit** stands where it lives, fixed to the wall or the floor. It is not moved, not leaned on, and not
   pushed at any point.
2. It has **two working levels**, each with a shelf directly above it. **Level A** is the upper level and **level B** the
   lower. A **middle upright** splits the unit into a left half and a right half.
3. **Level A** holds **four open-front bins**, fixed side by side, one per location: **A1, A2** in the left half and
   **A3, A4** in the right half, numbered left to right. Each bin takes one each, set down on its floor.
4. **Level B** holds **two case lanes**, one per location: **B1** in the left half and **B2** in the right half. Each lane
   is a marked space on the shelf deck with a **back stop**, as wide as one case with a finger's gap each side.
5. Each location has a **location label** on the shelf edge right below it, with its name in large print and a
   barcode.
6. Every location starts empty.
7. The **scanner** stands in its **holster** on the middle upright, between level A and level B, window facing out. It
   reads a barcode by itself when the barcode is held about a hand in front of its window: a **green** light and one
   beep if the location is the one the current put-list line names, a **red** light and a buzz if it is not.
8. The **list box** is a small open-top box fixed to the middle upright below level B.
9. The **put-away cart** is a two-deck cart standing braked against the **left end** of the shelving in **Config L** and
   against the **right end** in **Config R**, its top deck at about the height of level B.
10. On its top deck stand **two cases**, closed, shoebox size, each light enough for one gripper to hold by its sides,
    each with an **SKU label** on one end face, turned toward the shelving.
11. Beside the cases stands the **put tote**, an open tote holding **four eaches**: small boxed items that fit one gripper,
    each with an SKU label on top, standing clear of each other.
12. The **lower deck** of the cart is empty. It is where the empty tote goes.
13. The **put list** is a card in the **list clip** on the cart handle, facing the camera. It has a **CASES** section of two
    lines (B1 and B2) above an **EACHES** section of four lines (A1 to A4). Each line reads location, SKU, quantity 1.
    The order of the lines within each section is shuffled per episode.
14. Every SKU on the list matches exactly one item on the cart, and every item on the cart is on the list.
15. Nothing else stands on the shelving or the cart within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the case lanes and the location labels. You judge every other place by
eye against the shelving itself.

* **Shelving unit:** the fixed unit the base is parked at. Never moved, never leaned on, never pushed.
* **Level A:** the upper level, bins A1 to A4 left to right. Eaches only.
* **Level B:** the lower level, case lanes B1 (left) and B2 (right). Cases only.
* **Left half:** A1, A2, B1. **Left gripper only.**
* **Right half:** A3, A4, B2. **Right gripper only.**
* **Hand-over point:** in front of the middle upright, a hand out from the shelf edge of level A.
* **Scanner holster:** on the middle upright between the levels. Either gripper, one at a time.
* **List box:** on the middle upright below level B. **Cart gripper only.**
* **Put-away cart:** braked against the left end (Config L) or the right end (Config R) of the shelving: top deck with the
  cases and the put tote, lower deck, list clip on the handle. **Cart gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the left half and the **right gripper** the right half. The **cart gripper** also works the cart.
* The two arms meet only at the **hand-over point**, and both use the scanner holster and the list box on the middle
  upright, one at a time.
* Neither arm goes into a location in the other half, and neither reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds one thing, and while it does, the other gripper is empty, taking a
  hand-over, or drawn **clear of the shelving**.

### Arm assignments

* **Cart gripper** (**left gripper** in Config L, **right gripper** in Config R). Reads each line, takes each item off
  the cart, puts and scans the items for its own half, and hands over the items for the other half. Stows the empty
  tote and posts the put list.
* **Other gripper.** Takes each hand-over, puts the item in its location, and scans it.
* Only items are handed over. The scanner, the tote, and the list are never handed over.

## Vocabulary

* **Put list:** the card in the list clip. It is read top to bottom, CASES first, then EACHES.
* **Current line:** the top line not yet put and scanned green. Only the item on the current line is ever touched.
* **Case / each:** a case is a closed shoebox-size box that goes into a case lane on level B. An each is one small boxed
  item that goes into a bin on level A.
* **SKU label:** the label on an item that names it. It must match the SKU on the current line.
* **Location:** one bin or case lane, named by the label under it (A1 to A4, B1, B2).
* **Cart gripper:** the gripper on the cart's side, the **left gripper** in Config L and the **right gripper** in Config R.
* **Putting gripper:** the gripper whose half holds the current line's location. It puts the item and scans it.
* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down into a location
  from above.
* **Seated case:** the case sits in its lane, flat, square, its back against the back stop, its SKU label facing out, clear
  of the lane sides.
* **Placed each:** the each stands on the floor of its bin, upright, SKU label up, and stays put when the gripper opens.
* **Hand over:** the cart gripper brings the item to the hand-over point and holds it still for a **half-second hold**.
  The putting gripper then closes on the far side of it. Only after the putting gripper is closed does the cart gripper
  open and draw back.
* **Scan-confirm:** straight after the put, the putting gripper takes the scanner from its holster by its handle, holds
  its window about a hand in front of the location label, waits for the light, and puts the scanner back in its holster.
* **Green / red:** green light and one beep is a confirmed put. Red light and a buzz means the item is in the wrong
  location.
* **Clear of the shelving:** the arm is drawn back so that no part of it is in front of a location, the cart, or the
  middle upright.

## Steps

Run Steps 1 to 3 in order, and end the episode with Step 4. Steps 1 and 2 are the put list's two sections, each line put
and scan-confirmed before the next. Step 3 clears the cart. Only the cart gripper and the hand-overs depend on the
config.

### Step 1: Shelve the cases

**Goal:** both cases are **seated** in the lanes their lines name, and each put is scanned green.

Run 1.1 to 1.4 for the first CASES line, then again for the second.

#### 1.1 Read the current line

* Read the **current line** on the put list: its location and its SKU.
* Find the case on the cart whose **SKU label** matches it.
* Find the location label on the shelving that matches it. That location's half decides the putting gripper.

**Check:** one case matches the line and one lane matches the line. If no case matches, stop and log a system issue.

#### 1.2 Take the case off the cart

* **IF Config L:** the **left gripper** is the cart gripper. **IF Config R:** the **right gripper** is the cart gripper.
* Then, in both: with the **cart gripper**, close on the two long sides of the case and lift it straight up just clear of
  the top deck.
* With the **cart gripper**, carry it level toward the shelving, SKU label facing out.
* **IF the lane is in the cart gripper's own half:** with the **cart gripper**, carry it on to the front of its lane.
* **IF the lane is in the other half:** with the **cart gripper**, carry it to the **hand-over point** and hold it still for
  a **half-second hold**. With the **putting gripper**, close on the far side of the case. With the **cart gripper**, open
  and draw back **clear of the shelving**.
* With the gripper that is not holding the case, stay open and clear of the shelving outside the hand-over.

**Check:** the case is held by its sides, SKU label out, and nothing else on the cart has moved.

#### 1.3 Put the case in its lane

* With the **putting gripper**, bring the case level to the front of its lane, square to it, just above the shelf deck.
* With the **putting gripper**, set it down on the deck at the front of the lane and push it straight back, level, until
  it touches the **back stop**.
* With the **putting gripper**, open and draw straight out to the front, level.
* With the **putting gripper**, do not come down into the lane from above, do not turn the case in the lane, and do not
  push it against a lane side.

**Check:** the case is **seated**. If it sits crooked or short of the back stop, close on its sides with the **putting
gripper** and push it straight back again.

#### 1.4 Scan-confirm the case

* With the **putting gripper**, close on the handle of the **scanner** and lift it straight up out of its holster.
* With the **putting gripper**, hold the scanner window about a hand in front of the lane's **location label** and hold
  still until the light shows.
* **IF green:** with the **putting gripper**, stand the scanner back in its holster, window out, open, and draw it **clear
  of the shelving**. The line is done.
* **IF red:** with the **putting gripper**, stand the scanner back in its holster. Read the line again. Take the case back
  out with the **putting gripper**, put it in the lane its line names, and scan again.

**Check:** the scan was green and the scanner stands in its holster, window out.

**Expected state:** both cases are seated in their lanes and scanned green. The tote of eaches is still on the cart.

### Step 2: Shelve the eaches

**Goal:** all four eaches are **placed** in the bins their lines name, and each put is scanned green.

Run 2.1 to 2.4 for each EACHES line, top to bottom.

#### 2.1 Read the current line

* Read the **current line**: its bin and its SKU.
* Find the each in the put tote whose **SKU label** matches it, and the bin label that matches it.

**Check:** one each matches the line and one bin matches it.

#### 2.2 Take the each out of the tote

* With the **cart gripper**, close on the sides of the matching each and lift it straight up out of the tote, touching no
  other each.
* **IF the bin is in the cart gripper's own half:** with the **cart gripper**, carry it level to the front of its bin.
* **IF the bin is in the other half:** with the **cart gripper**, carry it to the **hand-over point** and hold it still for a
  **half-second hold**. With the **putting gripper**, close on the far side of the each. With the **cart gripper**, open and
  draw back **clear of the shelving**.

**Check:** the each is held by its sides, SKU label up, and the other eaches are still standing in the tote.

#### 2.3 Put the each in its bin

* With the **putting gripper**, bring the each level into the bin from the front, just above its floor.
* With the **putting gripper**, set it down on the floor of the bin, upright, SKU label up, then open and draw straight out
  to the front, level.
* With the **putting gripper**, do not let the each go from above the bin floor and do not come down into the bin from
  above.

**Check:** the each is **placed**. If it has tipped, close on it with the **putting gripper** and stand it up again.

#### 2.4 Scan-confirm the each

* With the **putting gripper**, take the scanner out of its holster by its handle, hold its window about a hand in front of
  the bin's **location label**, and hold still until the light shows.
* **IF green:** with the **putting gripper**, stand the scanner back in its holster, window out, open, and draw it **clear
  of the shelving**.
* **IF red:** with the **putting gripper**, stand the scanner back in its holster, read the line again, move the each to the
  bin its line names, and scan again.

**Check:** the scan was green and the scanner stands in its holster.

**Expected state:** all four eaches are placed and scanned green, both cases are seated, and the put tote is empty.

### Step 3: Clear the cart

**Goal:** the empty tote is on the lower deck, the put list is in the list box, and the top deck is bare.

* With the **cart gripper**, close on the near rim of the empty **put tote**, lift it just clear of the top deck, and bring
  it straight down and in onto the **lower deck**, then open and draw back.
* With the **cart gripper**, close on the top edge of the **put list**, draw it straight up out of the list clip, carry it
  level to the **list box**, and let it down into the box from just above its rim. Open and draw the gripper **clear of the
  shelving**.
* Hold the other gripper open and **clear of the shelving** for the whole of this step.

**Check:** the top deck is bare, the tote sits on the lower deck, and the list lies in the list box. If the tote rests
half off the lower deck, push it straight in with the **cart gripper**.

**Expected state:** every location holds its item, every put scanned green, the cart is cleared, and both grippers are clear
of the shelving.

### Step 4: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the put-away done.

* Look once across the shelving: every location holds the item its line names, the scanner is in its holster, the tote is on
  the lower deck, the list is in the list box, and the top deck is bare.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the put-away is done and still, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take both cases out of their lanes and stand them on the cart's top deck, SKU label toward the shelving.
2. Take the four eaches out of their bins and stand them in the put tote, clear of each other, then stand the tote on the top
   deck.
3. Take the put list out of the list box and put a different shuffled list in the list clip, facing the camera.
4. Move the cart to the end of the shelving for the next episode's config and brake it.
5. Check every location is empty, every label is readable, and the scanner stands in its holster and still lights.
6. Pick up anything that landed on a shelf, the cart, or the floor.
7. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

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

* **Visible cue:** the shelving shifts in frame, the shelf edges change angle or size in frame, or the base rolls, creeps, or
  turns at any point after recording starts.
* **SOP rule broken:** Steps 1 to 4, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Approached from above or fouled the shelf**

* **Visible cue:** a gripper comes down into a lane or a bin from above instead of coming in level from the front, or a wrist,
  forearm, or item knocks, scrapes, or rests on the shelf above a location.
* **SOP rule broken:** Steps 1.3 and 2.3, every reach into a location is a front approach, level, straight in and straight out.
* **Coaching note:** straight in from the front, straight out the same way.

**Violation: Leaned on or pushed the shelving or cart**

* **Visible cue:** a gripper, wrist, or forearm rests on a shelf, an upright, a bin, or the cart; a bin shifts; or the cart or
  shelving rocks or moves.
* **SOP rule broken:** Steps 1 to 3, the shelving and the cart carry no weight and nothing fixed is pushed out of place.
* **Coaching note:** the arm holds itself up. Press only as hard as the put needs.

**Violation: Put list not followed**

* **Visible cue:** a line is skipped, lines are taken out of top-to-bottom order, an each is put before both cases, or an item
  is touched that is not on the current line.
* **SOP rule broken:** Steps 1.1 and 2.1, read the list top to bottom, CASES first, one current line at a time.
* **Coaching note:** read the line, then move. The list is the order, not the cart.

**Violation: Wrong location**

* **Visible cue:** an item is put into a location other than the one its line names, a case goes into a bin, or an each goes
  into a case lane.
* **SOP rule broken:** Steps 1.3 and 2.3, each item goes into the location its line names.
* **Coaching note:** match the label under the location to the line before the arm goes in.

**Violation: Wrong item**

* **Visible cue:** the item taken does not match the SKU on the current line, or two items go into one location.
* **SOP rule broken:** Steps 1.1 and 2.1, find the one item whose SKU label matches the line.
* **Coaching note:** SKU to line, every time. Two items that look alike are not the same item.

**Violation: Case not seated**

* **Visible cue:** a case sits crooked, short of the back stop, against a lane side, on its end, or with its SKU label facing
  in; or a case is turned in the lane.
* **SOP rule broken:** Step 1.3, set the case down at the front of its lane and push it straight back to the back stop, label
  out.
* **Coaching note:** square, straight back, label out. A crooked case blocks the next put.

**Violation: Each dropped in or not placed**

* **Visible cue:** an each is let go from above the bin floor and falls in, lies on its side, stands with its SKU label down, or
  sits on the bin lip.
* **SOP rule broken:** Step 2.3, set each each down on the bin floor, upright, SKU label up, before opening.
* **Coaching note:** down to the floor, then open. A dropped each is a damaged each.

**Violation: Item held wrong**

* **Visible cue:** a case is held by its top, one end, or a corner instead of its two long sides; an each is held by its label
  or top; or an item is dragged across the cart deck or a shelf edge.
* **SOP rule broken:** Steps 1.2 and 2.2, close on the sides of the item and lift it just clear before the carry.
* **Coaching note:** sides in the gripper, lift first, then carry.

**Violation: Scan skipped or done out of turn**

* **Visible cue:** a put is not scanned; the scan happens before the item is in its location; the next item is touched before
  the green light; or the item's own label is scanned instead of the location label.
* **SOP rule broken:** Steps 1.4 and 2.4, scan the location label straight after each put, and wait for green before the next
  line.
* **Coaching note:** put, scan, green, then the next line. The scan is the record that the put happened.

**Violation: Red scan ignored**

* **Visible cue:** a red light and buzz is followed by the next line instead of the item being moved and scanned again, or the
  same wrong location is scanned again until the operator moves on.
* **SOP rule broken:** Steps 1.4 and 2.4, on red, read the line again, move the item to its location, and scan again.
* **Coaching note:** red means the item is in the wrong place. Fix the item, not the scan.

**Violation: Scanner handled wrong**

* **Visible cue:** the scanner is held by its window or its cable, dropped, laid on a shelf or the cart, left in a gripper while
  the gripper puts, not stood back in its holster window out, or handed from one gripper to the other.
* **SOP rule broken:** Steps 1.4 and 2.4, the putting gripper takes the scanner by its handle, scans, and stands it back in its
  holster window out.
* **Coaching note:** holster to label and back to the holster. It lives in the holster.

**Violation: Hand-over done wrong**

* **Visible cue:** the cart gripper opens before the putting gripper has closed; the item is still moving when the putting
  gripper closes, with no half-second hold; the hand-over happens away from the hand-over point; or an item is handed over when
  its location is in the cart gripper's own half.
* **SOP rule broken:** Steps 1.2 and 2.2, hand over only for the other half, at the hand-over point, hold still, and open only
  after the other gripper has closed.
* **Coaching note:** stop, hold still, let the other gripper take it, then open.

**Violation: Cart not cleared**

* **Visible cue:** the empty tote is left on the top deck, dropped, or set on the floor or a shelf; the put list is left in the
  clip or put anywhere but the list box; or something is left on the top deck at the end.
* **SOP rule broken:** Step 3, the cart gripper stows the empty tote on the lower deck and posts the list in the list box.
* **Coaching note:** a cleared cart is the signal the put-away is done. Leave nothing on top.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the shelving is not set up in: the gripper away from the cart takes an item off the
  cart, a gripper reaches for a cart end that is empty, or the cart is moved before or during the episode.
* **SOP rule broken:** Steps 1.2, 2.2, and 3, look at the shelving, find the cart, and follow the IF line that matches the config
  the episode is set up in.
* **Coaching note:** look at the cart before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** an item is put before its line is read; the cart is cleared before every line is scanned green; the tote is
  moved while it still holds an each; or the list is posted before the tote is stowed.
* **SOP rule broken:** Steps 1 to 3, shelve the cases, then the eaches, each scanned straight after its put, then clear the cart.
* **Coaching note:** the order is the task. Each line leaves the shelving ready for the next one.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two items, an item and the scanner, or the tote with an each in it; both grippers carry
  different things at the same time outside a hand-over; or a gripper holds something while the other works instead of being
  clear of the shelving.
* **SOP rule broken:** Steps 1 to 3, one gripper holds one thing, and the other is empty, taking a hand-over, or clear of the
  shelving.
* **Coaching note:** one thing, one trip.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a case
  crooked or short of the back stop, an each tipped over, a tote half off the lower deck, or a scanner not in its holster.
* **SOP rule broken:** Steps 1.1 to 3, run each check and correct what it finds by the retry written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a case, an each, the tote, the scanner, or the list is dropped on the cart, a shelf, or the floor; an each in
  the tote or a bin is knocked over; or a put item is knocked out of its location.
* **SOP rule broken:** Steps 1 to 3, nothing is dropped or knocked out of its place, and every gripper comes out the way it went
  in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **left gripper** goes into A3, A4, or B2; the **right gripper** goes into A1, A2, or B1; the gripper away
  from the cart touches the cart; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 3, each gripper puts into its own half, only the cart gripper works the cart, and the arms
  never cross.
* **Coaching note:** left half, left arm. Right half, right arm. The cart side decides who picks.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with an item on the cart or in the wrong location, a put not scanned green, the scanner out of
  its holster, the tote on the top deck, the list in the clip, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 4, look once across the shelving, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for
coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a location label, an SKU label, the put list, or the scanner light**, so which item went where or whether a
  scan was green cannot be judged.
* **Scanner fault:** no light on a correctly held label, a green on a wrong location, or a red on the right one.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **List or item fault:** an SKU on the list with no matching item, an item with no line, or a torn or unreadable label.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a location, the hand-over
  point, the holster, the list box, or something on the cart cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Read one put-list line
2. Take one case off the cart
3. Hand one item over at the hand-over point
4. Push one case into its lane
5. Take one each out of the tote
6. Set one each down in its bin
7. Take the scanner out of its holster
8. Scan one location label
9. Stand the scanner back in its holster
10. Stow the empty tote on the lower deck
11. Post the put list in the list box
12. Return both arms home and end the episode
