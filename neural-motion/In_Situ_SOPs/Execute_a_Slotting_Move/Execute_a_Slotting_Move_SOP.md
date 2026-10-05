# Execute a Slotting Move SOP (1x Episode: one swap, in situ)

One episode carries out one slotting move: two SKUs trade bins between the upper and the lower shelf level, as the slotting plan
says, at the shelving where the bins live. The base is **passive**: it has no drive of its own, so it is pushed by hand to the
front of the shelving and locked there, and nothing is carried away to a table. Everything the episode touches is already at the
shelving when recording starts: the four bins and their stock, the bin label cards in their holders, the slotting plan, the move
tote on the work ledge, and the scanner in its holster.

The episode runs these three actions in this order and no other: **relocate the SKU stock between the shelf levels per the plan,
swap the bin labels, scan-confirm both locations.** The labels are swapped only after all the stock has moved, and the scans
come last, one for each of the two locations, because a scan checks that the stock, the label, and the location all agree.

The shelving is worked **as found**. It has four bins, two on each level. Each bin holds **three units** of one SKU and a **bin
label card** naming that SKU. The **slotting plan** names two of the four bins, one on each level, and says their SKUs trade
places. The other two bins are not part of the move and are never touched. The episode ends with the two plan bins holding each
other's stock, each carrying the bin label card of its new SKU, both locations scanned green, and the move tote empty.

**The plan sets the move.** It is a card in the plan holder, read before any unit is touched. It names the **upper bin** (on level
A) and the **lower bin** (on level B), and the SKU that goes from each to the other. Which two bins it names changes from episode
to episode, so the plan is read every time and never worked from memory.

**This is an in-situ task, and three things follow from that.** First, **each shelf level has a shelf directly above it**, so **every
reach into a bin is from the front, straight in, level**. No gripper comes down into a bin from above. Second, the **shelving and
the ledge are never leaned on and never pushed**: no gripper, wrist, or forearm rests on a shelf, an upright, a bin, or the ledge,
and the bins are fixed and never pulled out. Third, **stock goes only between the two plan bins and the move tote**: nothing is set
down on a shelf edge, another bin, the ledge, or the floor on the way.

The plan names one of four pairs. The shelving, the stock in the four bins, the move tote, and the scanner are in the same place in
all four; only which two bins swap changes.

* **Config L:** the plan swaps **A1 and B1**, both in the left column.
* **Config R:** the plan swaps **A2 and B2**, both in the right column.
* **Config LR:** the plan swaps **A1 and B2**, upper bin left, lower bin right.
* **Config RL:** the plan swaps **A2 and B1**, upper bin right, lower bin left.

One config per episode, set by the plan card before recording and never changed mid-episode. Where a step depends on the plan it
says so on an **IF** line. Read the plan and follow the line that matches.

What stays constant across all sessions:

* **Column rule:** the **left gripper** works the **left column** (A1, B1) and the **right gripper** works the **right column** (A2,
  B2). The gripper of the upper bin's column is the **upper gripper**. The gripper of the lower bin's column is the **lower
  gripper**. In Config L and Config R they are the same gripper.
* **Middle rule:** the **move tote** and the **hand-over point** are in the middle, and both grippers reach them. Stock waits in the
  move tote, never on a shelf.
* **Hand-over rule:** when something goes straight from one column to the other (Config LR and Config RL), the gripper it comes
  from **hands it over** to the other gripper at the hand-over point. No arm reaches across the shelving.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches over, under,
around, or past the other. Nothing is moved two at a time: one gripper holds one thing, and the other gripper is empty, taking a
hand-over, or clear of the shelving.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or
repositioned once recording starts. It is parked once, before recording, and does not move again until the episode is over.

1. Push the base by hand up to the front of the work ledge and stop it **square to the shelving**, so the shelf edges run straight
   across the frame of the camera.
2. Stop it **centered on the shelving**, so the middle of the base is in line with the middle upright between the two columns.
3. Stop it **close enough** that both grippers reach the back of a bin straight in and level without either arm extending, and
   **far enough** that neither arm, wrist, nor any part of the base touches a shelf, an upright, or the ledge while both arms work.
4. Check the **height band**: both grippers come level into every bin on level A and level B without a wrist or forearm touching the
   shelf above it.
5. Check the **left side**: the **left gripper** reaches the back of A1 and B1, their label holders and location labels, the move
   tote, the hand-over point, and the scanner holster, all without extending.
6. Check the **right side**: the **right gripper** reaches the back of A2 and B2, their label holders and location labels, the move
   tote, the hand-over point, and the scanner holster, all without extending.
7. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
8. If any of lines 1 to 6 fails, push the base to a new park by hand and start again at line 1. Do not work shelving the arms cannot
   reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the shelving hard enough to shift it,
nothing touches it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the middle upright and its frame includes all four bins, their label cards and location
   labels, the plan, the scanner and its light, and the move tote on the ledge.
3. The camera reads every **location label**, every **bin label card**, and the **SKU label** on every unit, so which SKU is in which
   bin, and which card is in which holder, is readable at every moment.
4. The camera reads the **slotting plan** in its holder.
5. The camera sees the **scanner light**, so each green or red scan is readable.
6. The camera sees into the move tote well enough to count the units in it.
7. Both arms are at home with grippers open.
8. The **left arm** reaches A1, B1, the move tote, the hand-over point, and the holster without extending to a joint limit.
9. The **right arm** reaches A2, B2, the move tote, the hand-over point, and the holster without extending to a joint limit.
10. Both grippers come in and go out of every bin **from the front and level**, and neither wrist nor forearm touches the shelf above
    on the way in or out.
11. The two arms do not collide, and neither arm passes in front of the other.
12. If a place cannot be reached, re-park the base by the Base positioning steps until lines 8 to 11 hold.

### Materials checklist

1. The **shelving** stands where it lives, fixed to the wall or the floor. It is not moved, not leaned on, and not pushed at any point.
2. It has **two levels**, each with a shelf directly above it. **Level A** is the upper level and **level B** the lower. A **middle
   upright** splits it into a **left column** and a **right column**.
3. Each level holds **two fixed open-front bins**, one per column: **A1, A2** on level A and **B1, B2** on level B, numbered left to
   right. Each bin is one unit wide and three units deep: a **front slot**, a **middle slot**, and a **back slot**.
4. Each bin has a fixed **location label** on the shelf edge right below it, with its name in large print and a barcode.
5. Each bin has a **label holder** on its front lip: a clear slot open at the top. In it stands a **bin label card**, a stiff card
   with the SKU's name in large print and its barcode, printed side out.
6. Each bin holds **three units** of its own SKU, standing upright in its three slots, SKU label facing out. Every unit is a small boxed
   item that fits one gripper. No two bins hold the same SKU.
7. The **work ledge** is a fixed flat ledge running along the front of the shelving below level B. Its **front strip** sticks out past
   the shelf edges, so nothing is above it.
8. The **move tote** is a small open tote standing empty in the middle of the front strip, in line with the middle upright, big enough
   for three units standing side by side. It is fixed in place and is never moved.
9. The **scanner** stands in its **holster** on the middle upright, between level A and level B, window facing out. It reads a barcode
   by itself when the barcode is held about a hand in front of its window. It is linked to the plan: after it reads a **location label**
   and then a **bin label card**, it shows a **green** light and one beep if that card belongs in that location by the plan, and a
   **red** light and a buzz if it does not.
10. The **slotting plan** is a card in the **plan holder** on the middle upright below level B, facing the camera. It reads two lines,
    for example **SKU P: A1 TO B2** and **SKU Q: B2 TO A1**. The pair it names is set per episode.
11. Nothing else stands on the shelving or the ledge within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the location labels. You judge every other place by eye against the shelving itself.

* **Shelving:** the fixed unit the base is parked at. Never moved, never leaned on, never pushed.
* **Left column:** A1 and B1, with their label holders. **Left gripper only.**
* **Right column:** A2 and B2, with their label holders. **Right gripper only.**
* **Move tote:** fixed in the middle of the ledge's front strip. Either gripper, one at a time.
* **Hand-over point:** in front of the middle upright, a hand out from the shelf edge of level A.
* **Scanner holster and plan holder:** on the middle upright. Either gripper uses the scanner, one at a time. The plan is only read.

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the left column and the **right gripper** works the right column.
* The two arms meet only at the **hand-over point**, and both use the move tote and the scanner, one at a time.
* Neither arm goes into a bin in the other column, and neither reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds one thing, and while it does, the other gripper is empty, taking a hand-over, or
  drawn **clear of the shelving**.

### Arm assignments

* **Upper gripper** (the gripper of the upper bin's column). Empties the upper bin into the move tote, sets the lower bin's stock into
  the upper bin, puts the upper card in the move tote, puts the lower card in the upper holder, and scans the upper bin.
* **Lower gripper** (the gripper of the lower bin's column). Takes the lower bin's stock out, sets the move tote's stock into the lower
  bin, takes the lower card out, puts the upper card in the lower holder, and scans the lower bin.
* In Config L and Config R one gripper is both, and the other gripper stays open and **clear of the shelving** for the whole episode.
* Only units and cards are handed over. The scanner and the plan are never handed over, and the move tote is never moved.

## Vocabulary

* **Slotting move:** changing which bin an SKU lives in. Here, two SKUs trade bins.
* **Slotting plan:** the card in the plan holder that names the two bins and which SKU goes to which.
* **Upper bin / lower bin:** the plan's bin on level A and the plan's bin on level B.
* **Upper gripper / lower gripper:** the gripper of the upper bin's column and the gripper of the lower bin's column.
* **Untouched bins:** the two bins the plan does not name. Nothing goes into them or comes out of them.
* **Location label:** the fixed label on the shelf edge under a bin. It names the place and never moves.
* **Bin label card:** the card in the label holder on a bin's front lip. It names the SKU in the bin and moves when the SKU moves.
* **Front unit:** the unit nearest the front of a bin. Units always come out front unit first.
* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down into a bin from above.
* **Set unit:** the unit stands upright on the bin floor in its slot, SKU label facing out, square to the bin, and stays put when the
  gripper opens. A bin fills back slot first, then middle, then front.
* **Mixed stock:** units of two different SKUs in the same bin or the move tote at the same time. It never happens.
* **Seated card:** the card stands all the way down in its holder, printed side out, straight.
* **Hand over:** the giving gripper brings the unit or card to the hand-over point and holds it still for a **half-second hold**. The
  taking gripper then closes on the far side of it. Only after the taking gripper is closed does the giving gripper open and draw back.
* **Scan-confirm:** the gripper takes the scanner out of its holster by its handle, holds its window about a hand in front of the bin's
  **location label** until it beeps, then in front of the bin's **label card**, waits for the light, and stands the scanner back in
  its holster.
* **Green / red:** green light and one beep means the card belongs in that location by the plan. Red light and a buzz means it does
  not.
* **Clear of the shelving:** the arm is drawn back so that no part of it is in front of a bin, the move tote, or the middle upright.

## Steps

Run Steps 1 to 5 in order, and end the episode with Step 6. Steps 1 to 3 relocate the stock, Step 4 swaps the labels, and Step 5
scan-confirms both locations. The plan decides which gripper is the upper gripper and which is the lower gripper, and whether a
hand-over is needed.

### Step 1: Empty the upper bin into the move tote

**Goal:** the upper bin's three units stand in the move tote and the upper bin is empty.

#### 1.1 Read the plan

* Read the **slotting plan**: the upper bin, the lower bin, and their two SKUs.
* Find both bins by their location labels, and check the bin label card on each matches the SKU the plan names for it.
* **IF Config L:** the **left gripper** is both the upper and the lower gripper. **IF Config R:** the **right gripper** is both.
  **IF Config LR:** the **left gripper** is the upper gripper and the **right gripper** the lower gripper. **IF Config RL:** the
  **right gripper** is the upper gripper and the **left gripper** the lower gripper.

**Check:** each plan bin holds three units of the SKU the plan names for it, and its card matches. If not, stop and log a system issue.

#### 1.2 Move one unit to the move tote

* With the **upper gripper**, come level into the upper bin from the front, close on the two sides of the **front unit**, lift it just
  clear of the bin floor, and draw it straight out, level.
* With the **upper gripper**, carry it level to the **move tote** and set it down on the tote floor, upright, SKU label facing out,
  beside any unit already there.
* With the **upper gripper**, open and lift straight up out of the tote.
* With the other gripper, stay open and **clear of the shelving**.

**Check:** the unit stands upright in the tote, and the units left in the upper bin still stand in their row.

Run 1.2 three times, until the upper bin is empty.

**Expected state:** the move tote holds the upper bin's three units, the upper bin is empty, and its card is still in its holder.

### Step 2: Move the lower bin's stock up

**Goal:** the lower bin's three units stand in the upper bin, filled back slot first, and the lower bin is empty.

#### 2.1 Take one unit out of the lower bin

* With the **lower gripper**, come level into the lower bin, close on the sides of the **front unit**, lift it just clear, and draw it
  straight out, level.
* **IF Config L or Config R:** with the same gripper, carry it level to the front of the upper bin.
* **IF Config LR or Config RL:** with the **lower gripper**, carry it to the **hand-over point** and hold it still for a **half-second
  hold**. With the **upper gripper**, close on the far side of the unit. With the **lower gripper**, open and draw back **clear of the
  shelving**.

**Check:** the **upper gripper** holds one unit by its sides, SKU label out.

#### 2.2 Set the unit in the upper bin

* With the **upper gripper**, bring the unit level into the upper bin and set it down in the back-most empty slot, upright, SKU label
  facing out.
* With the **upper gripper**, open and draw straight out to the front, level.
* With the **upper gripper**, do not let the unit go from above the bin floor and do not come down into the bin from above.

**Check:** the unit is **set**. If it has tipped, close on it with the **upper gripper** and stand it up in its slot.

Run 2.1 and 2.2 three times, until the lower bin is empty.

**Expected state:** the upper bin is full with the lower bin's three units, the lower bin is empty, and the tote still holds the other
three units.

### Step 3: Move the tote stock down

**Goal:** the move tote's three units stand in the lower bin, filled back slot first, and the tote is empty.

* With the **lower gripper**, close on the sides of one unit in the **move tote**, lift it straight up out of the tote, touching no other
  unit.
* With the **lower gripper**, carry it level into the lower bin and set it down in the back-most empty slot, upright, SKU label facing out.
* With the **lower gripper**, open and draw straight out to the front, level.
* With the other gripper, stay open and **clear of the shelving** unless it is the same gripper.
* Run these moves three times, until the tote is empty.

**Check:** each unit is **set**, the lower bin is full, and the tote is empty. If a unit has tipped, close on it with the **lower gripper**
and stand it up in its slot.

**Expected state:** the stock has traded bins. Each plan bin holds three units of its new SKU, and there is no **mixed stock**
anywhere. The cards have not moved yet.

### Step 4: Swap the bin labels

**Goal:** each plan bin carries the bin label card of the SKU now in it, **seated**.

#### 4.1 Put the upper card in the move tote

* With the **upper gripper**, close on the top edge of the upper bin's **label card**, draw it straight up out of its holder, and carry
  it level to the **move tote**.
* With the **upper gripper**, lay it flat on the tote floor, printed side up, then open and lift straight up.

**Check:** the card lies flat in the tote, and the upper holder is empty.

#### 4.2 Move the lower card up

* With the **lower gripper**, close on the top edge of the lower bin's **label card** and draw it straight up out of its holder.
* **IF Config L or Config R:** with the same gripper, carry it level to the upper bin's holder.
* **IF Config LR or Config RL:** with the **lower gripper**, carry it to the **hand-over point** and hold it still for a **half-second
  hold**. With the **upper gripper**, close on the far edge of the card. With the **lower gripper**, open and draw back **clear of the
  shelving**.
* With the **upper gripper**, bring the card down into the upper bin's holder from just above it, printed side out, and let it slide
  all the way down, then open and draw back.

**Check:** the card is **seated** in the upper holder, and the lower holder is empty.

#### 4.3 Put the upper card in the lower holder

* With the **lower gripper**, close on the edge of the card lying in the **move tote**, lift it straight up, and turn it upright,
  printed side out.
* With the **lower gripper**, bring it down into the lower bin's holder from just above it and let it slide all the way down, then open
  and draw back **clear of the shelving**.

**Check:** the card is **seated** in the lower holder, and the move tote is empty.

**Expected state:** each plan bin carries the card of the SKU now in it, the move tote is empty, and the untouched bins are as found.

### Step 5: Scan-confirm both locations

**Goal:** the upper bin and then the lower bin are each scanned green.

#### 5.1 Scan the upper bin

* With the **upper gripper**, close on the handle of the **scanner** and lift it straight up out of its holster.
* With the **upper gripper**, hold its window about a hand in front of the upper bin's **location label** until it beeps, then about a
  hand in front of the upper bin's **label card**, still, until the light shows.
* **IF green:** with the **upper gripper**, stand the scanner back in its holster, window out, open, and draw back **clear of the
  shelving**.
* **IF red:** with the **upper gripper**, stand the scanner back in its holster. Read the plan again, find what is wrong with the upper bin
  (its card or its stock), put it right by the moves of Steps 2 to 4, and scan again.

**Check:** the scan was green and the scanner stands in its holster, window out.

#### 5.2 Scan the lower bin

* With the **lower gripper**, take the scanner out of its holster by its handle.
* With the **lower gripper**, hold its window about a hand in front of the lower bin's **location label** until it beeps, then in front of
  the lower bin's **label card**, still, until the light shows.
* **IF green:** with the **lower gripper**, stand the scanner back in its holster, window out, open, and draw back **clear of the
  shelving**.
* **IF red:** with the **lower gripper**, stand the scanner back in its holster, read the plan again, put the lower bin right, and scan again.

**Check:** the scan was green and the scanner stands in its holster, window out.

**Expected state:** both locations are scanned green, both arms are clear of the shelving, and the move tote is empty.

### Step 6: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the slotting move done.

* Look once across the shelving: each plan bin holds three units of its new SKU with the matching card, the untouched bins are as found,
  the move tote is empty, and the scanner is in its holster.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the slotting move is done and still, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Choose the next episode's pair, one level A bin and one level B bin, and put that plan card in the plan holder, facing the camera.
2. Set every bin to the next plan's start: each bin holds three units of one SKU with that SKU's card seated in its holder. Swapping the
   last two bins back is one way to do it.
3. Check the move tote is empty and still in the middle of the ledge.
4. Check every label is readable and the scanner stands in its holster and still lights.
5. Pick up anything that landed on a shelf, the ledge, or the floor.
6. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

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

* **Visible cue:** a gripper comes down into a bin from above instead of coming in level from the front, or a wrist, forearm, unit, or
  card knocks, scrapes, or rests on the shelf above a bin.
* **SOP rule broken:** Steps 1.2, 2.1, 2.2, and 3, every reach into a bin is a front approach, level, straight in and straight out.
* **Coaching note:** straight in from the front, straight out the same way.

**Violation: Leaned on or pushed the shelving or ledge**

* **Visible cue:** a gripper, wrist, or forearm rests on a shelf, an upright, a bin, or the ledge; a bin shifts; or the shelving rocks.
* **SOP rule broken:** Steps 1 to 5, the shelving and the ledge carry no weight from the arms.
* **Coaching note:** the arm holds itself up. Press only as hard as the move needs.

**Violation: Plan not followed**

* **Visible cue:** stock moves between bins the plan does not name, goes the wrong way, or the arms start moving before the plan is read.
* **SOP rule broken:** Step 1.1, read the plan, find both bins, and move only between them, in the direction it names.
* **Coaching note:** read the plan, then find both labels. The plan is the move.

**Violation: Untouched bin disturbed**

* **Visible cue:** a unit or card goes into, or comes out of, a bin the plan does not name, or a unit in such a bin is pushed or tipped.
* **SOP rule broken:** Steps 1 to 4, the two bins the plan does not name are never touched.
* **Coaching note:** two bins move. The other two do not exist for this episode.

**Violation: Mixed stock**

* **Visible cue:** units of two different SKUs stand in the same bin or in the move tote at the same time, for example a lower bin unit
  set into the upper bin before it is empty.
* **SOP rule broken:** Steps 1 to 3, empty the upper bin into the tote, then move the lower stock up, then the tote stock down.
* **Coaching note:** one SKU per place, always. Empty before you fill.

**Violation: Stock left behind**

* **Visible cue:** a step ends with a unit still in the bin or the tote it was meant to leave, so a bin ends with fewer or more than three
  units.
* **SOP rule broken:** Steps 1.2, 2.2, and 3, run each move three times, until the bin or tote it empties is empty.
* **Coaching note:** count to three. The step is over when the source is empty.

**Violation: Unit held wrong**

* **Visible cue:** a unit is held by its top, its label, or one corner, dragged along the bin floor, or taken from the middle or back of a
  row instead of the front.
* **SOP rule broken:** Steps 1.2, 2.1, and 3, close on the sides of the front unit and lift it just clear before drawing it out.
* **Coaching note:** front unit, sides in the gripper, lift then draw.

**Violation: Unit dropped in or not set**

* **Visible cue:** a unit is let go from above the bin or tote floor and falls, lies on its side, stands crooked, or has its SKU label
  facing in; or a bin fills front slot first, leaving a gap at the back.
* **SOP rule broken:** Steps 1.2, 2.2, and 3, set each unit down on the floor, upright, label out, back-most empty slot first.
* **Coaching note:** down to the floor, then open. Back first, then forward.

**Violation: Move tote misused**

* **Visible cue:** the move tote is pushed or moved; a unit is set beside it on the ledge instead of in it; or a card is laid on top of
  units still in it.
* **SOP rule broken:** Steps 1.2, 3, and 4.1, the move tote stays fixed, units and the waiting card go inside it, and the card goes in only
  once it is empty.
* **Coaching note:** the tote is the only waiting place. Use it, do not move it.

**Violation: Hand-over done wrong**

* **Visible cue:** the giving gripper opens before the taking gripper has closed; the unit or card is still moving when the taking gripper
  closes, with no half-second hold; the hand-over happens away from the hand-over point; or something is handed over in Config L or
  Config R.
* **SOP rule broken:** Steps 2.1 and 4.2, hand over only in Config LR and Config RL, at the hand-over point, held still, and open only
  after the other gripper has closed.
* **Coaching note:** stop, hold still, let the other gripper take it, then open.

**Violation: Labels swapped wrong**

* **Visible cue:** a card ends in the wrong holder, both cards end up in one bin, a card is put back in the holder it came from, a card
  faces in or stands crooked or only part way down, or an untouched bin's card is moved.
* **SOP rule broken:** Step 4, the upper card waits in the tote, the lower card goes up, then the upper card goes down, each one seated,
  printed side out.
* **Coaching note:** the card follows its SKU. Read the card against the units before you let go.

**Violation: Card handled wrong**

* **Visible cue:** a card is bent, creased, pressed into its holder from the front, held over its barcode, dropped, or laid on a shelf or
  the ledge.
* **SOP rule broken:** Step 4, hold each card by its edge, keep it flat in the tote, and let it slide down into its holder from above.
* **Coaching note:** edges only, and let the holder take it. A bent card scans badly.

**Violation: Scan skipped or done out of turn**

* **Visible cue:** a location is not scanned; the card is scanned before the location label; a scan is made before the labels are swapped;
  only one location is scanned; or the lower bin is scanned before the upper.
* **SOP rule broken:** Step 5, after the swap, scan the upper bin, then the lower bin: location label first, then the card.
* **Coaching note:** place, then card, then wait. Two bins, two green lights.

**Violation: Red scan ignored**

* **Visible cue:** a red light and buzz is followed by the next scan or the end of the episode instead of a fix, or the same pair is
  scanned again and again with nothing put right.
* **SOP rule broken:** Step 5, on red, read the plan again, put the bin right, and scan again.
* **Coaching note:** red means the bin and the plan disagree. Fix the bin, not the scan.

**Violation: Scanner handled wrong**

* **Visible cue:** the scanner is held by its window or its cable, dropped, laid on a shelf or the ledge, not stood back in its holster
  window out, or handed from one gripper to the other.
* **SOP rule broken:** Step 5, the scanning gripper takes the scanner by its handle, scans, and stands it back in its holster window out.
* **Coaching note:** holster to label and back to the holster. It lives in the holster.

**Violation: Config misaligned**

* **Visible cue:** the arms work a pair the plan does not name, the wrong gripper acts as the upper or lower gripper, a hand-over is
  skipped where the plan's bins are in different columns, or a gripper reaches into the other column to avoid one.
* **SOP rule broken:** Steps 1.1, 2.1, and 4.2, read the plan, find the two bins, and follow the IF line that matches the pair it names.
* **Coaching note:** the plan is the config. Name the upper and lower gripper before the first move.

**Violation: Wrong order of work**

* **Visible cue:** a card is moved before all the stock has traded bins; the lower bin's stock is moved before the upper bin is empty; the
  tote stock is moved before the lower bin is empty; or a scan is made before both cards are seated.
* **SOP rule broken:** Steps 1 to 5, empty the upper bin into the tote, move the lower stock up, move the tote stock down, swap the cards,
  then scan.
* **Coaching note:** the order is the task. Stock first, labels second, scans last.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two units, or a unit and a card; both grippers carry different things at the same time outside a
  hand-over; or a gripper holds something while the other works instead of being clear of the shelving.
* **SOP rule broken:** Steps 1 to 5, one gripper holds one thing, and the other is empty, taking a hand-over, or clear of the shelving.
* **Coaching note:** one thing, one trip.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a unit tipped, a card
  not seated, or a scanner not in its holster.
* **SOP rule broken:** Steps 1.1 to 5.2, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a unit, a card, or the scanner is dropped on a shelf, the ledge, or the floor; a unit in a bin or the tote is knocked
  over; or a unit is knocked out of its bin.
* **SOP rule broken:** Steps 1 to 5, nothing is dropped or knocked out of its place, and every gripper comes out the way it went in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **left gripper** goes into A2 or B2; the **right gripper** goes into A1 or B1; the idle gripper in Config L or Config
  R moves anything; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 5, each gripper works its own column, and the arms never cross.
* **Coaching note:** left column, left arm. Right column, right arm. The middle is shared, the columns are not.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a plan bin holding the wrong SKU or card, a unit in the move tote, a location not scanned green,
  the scanner out of its holster, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 6, look once across the shelving, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a location label, a label card, an SKU label, the plan, or the scanner light**, so which SKU or card is where, or
  whether a scan was green, cannot be judged.
* **Scanner fault:** no beep on a correctly held label, a green on a wrong pair, or a red on the right one.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Plan or stock fault:** a plan naming two bins on the same level, a plan bin that does not hold the SKU the plan names, a bin short of
  units, or a torn or unreadable card.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so the back of a bin, a label holder, the
  move tote, the hand-over point, or the holster cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Read the slotting plan
2. Take the front unit out of a bin
3. Set one unit in the move tote
4. Hand one unit or card over at the hand-over point
5. Set one unit in a bin
6. Take one unit out of the move tote
7. Draw a label card out of its holder
8. Lay a label card in the move tote
9. Seat a label card in its holder
10. Scan one location label and its card
11. Stand the scanner back in its holster
12. Return both arms home and end the episode
