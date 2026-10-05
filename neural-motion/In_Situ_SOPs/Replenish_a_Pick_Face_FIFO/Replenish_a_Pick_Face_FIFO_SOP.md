# Replenish a Pick Face (FIFO) SOP (1x Episode: two lanes, in situ)

One episode replenishes one pick face from one bulk carton, at the shelving where the pick face lives. The base is **passive**:
it has no drive of its own, so it is pushed by hand to the front of the shelving and locked there, and nothing is carried away
to a table. Everything the episode touches is already at the shelving when recording starts: the two pick-face lanes with their
older units, the replenishment cart with its open bulk carton, the work ledge, the flat-carton sleeve, the log card, and the
marker.

The episode runs these four actions in this order and no other: **move bulk stock to the pick-face bins, rotate older units to
the front, break down the empty carton, log.** Rotation comes first in each lane: the older unit is pulled to the front before
any new unit goes in, so the new units always go in behind it. This is **FIFO**, first in, first out: the unit that has waited
longest is the next one a picker takes.

The shelving is worked **as found**. The pick face is one SKU in **two lanes**, Lane 1 on the left and Lane 2 on the right. Each
lane holds **one older unit**, left somewhere behind the front by the last picks. The **bulk carton** stands open on the
replenishment cart, braked against one end of the shelving, holding **four new units** of the same SKU. The episode ends with
each lane holding its older unit at the front and two new units behind it, the empty carton folded flat in the flat-carton
sleeve, the three lines of the log card ticked, and the marker back in its clip.

**This is an in-situ task, and three things follow from that.** First, **the pick-face level has a shelf directly above it**, so
**every reach into a lane is from the front, straight in, level**. No gripper comes down into a lane from above. Second, the
**shelving, the ledge, and the cart are never leaned on and never pushed**: no gripper, wrist, or forearm rests on a shelf, an
upright, a bin, the ledge, or the cart, and the bins are fixed and never pulled out. Third, **each unit goes from the carton to
its slot and nowhere else**: nothing is set down on a shelf edge, the ledge, the cart deck, or the floor on the way.

The shelving is set up in one of two ways. Only the **replenishment cart** moves. The lanes, the ledge, the log card, and the
marker are in the same place in both.

* **Config L:** the replenishment cart stands against the **left end** of the shelving, beside Lane 1.
* **Config R:** the replenishment cart stands against the **right end** of the shelving, beside Lane 2.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says so on an
**IF** line. Look at the shelving and follow the line that matches.

What stays constant across all sessions:

* **Lane rule:** the **left gripper** works **Lane 1** and the **right gripper** works **Lane 2**. The gripper that works a lane
  rotates its older unit and sets its new units.
* **Cart-side rule:** the gripper on the cart's side takes every new unit out of the carton, carries the empty carton, stows the
  flat carton, and fills in the log. That is the **left gripper** in Config L and the **right gripper** in Config R. It is called
  the **cart gripper**.
* **Hand-over rule:** a new unit for the lane away from the cart is **handed over** by the cart gripper to that lane's gripper at the
  **hand-over point**. No arm reaches across the shelving.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches over, under,
around, or past the other. Nothing is moved two at a time: one gripper holds one thing, and the other gripper is empty, taking a
hand-over, pinning the carton at the breakdown spot, or clear of the shelving.

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
2. Stop it **centered on the shelving**, so the middle of the base is in line with the middle upright between Lane 1 and Lane 2.
3. Stop it **close enough** that both grippers reach the back slot of a lane straight in and level without either arm extending,
   and **far enough** that neither arm, wrist, nor any part of the base touches a shelf, an upright, the ledge, or the cart while
   both arms work.
4. Check the **height band**: both grippers come level into the back slot of each lane, above a unit standing in the front slot,
   without a wrist or forearm touching the shelf above.
5. Check the **left side**: the **left gripper** reaches all three slots of Lane 1, the hand-over point, and the breakdown spot, all
   without extending.
6. Check the **right side**: the **right gripper** reaches all three slots of Lane 2, the hand-over point, and the breakdown spot,
   all without extending.
7. Check the **cart** for the config this episode runs: the **cart gripper** reaches the bottom of the bulk carton, the flat-carton
   sleeve, the log card, and the marker clip.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not work shelving the arms
   cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the shelving hard enough to shift it,
nothing touches it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the middle upright and its frame includes both lanes and their labels, the log card and
   the marker, the whole work ledge, and the cart with the bulk carton and the flat-carton sleeve.
3. The camera reads the **date label** on every unit in both lanes and in the carton, so which unit is older and where it ends up
   is readable.
4. The camera reads the **log card** well enough to see which boxes are ticked.
5. Both arms are at home with grippers open.
6. The **left arm** reaches all of Lane 1, the hand-over point, and the breakdown spot without extending to a joint limit.
7. The **right arm** reaches all of Lane 2, the hand-over point, and the breakdown spot without extending to a joint limit.
8. The cart arm for this config reaches the carton, the sleeve, the log card, and the marker without extending to a joint limit.
9. Both grippers come in and go out of each lane **from the front and level**, and neither wrist nor forearm touches the shelf above
   on the way in or out.
10. The two arms do not collide, and neither arm passes in front of the other.
11. If a place cannot be reached, re-park the base by the Base positioning steps until lines 6 to 10 hold.

### Materials checklist

1. The **shelving** stands where it lives, fixed to the wall or the floor. It is not moved, not leaned on, and not pushed at any
   point.
2. Its **pick-face level** has a shelf directly above it. A **middle upright** splits it into a left half and a right half.
3. The pick face is **two fixed open-front bins**, one per half: **Lane 1** on the left and **Lane 2** on the right. Each has a **lane
   label** on the shelf edge right below it. Each lane is one unit wide and three units deep: a **front slot**, a **middle slot**,
   and a **back slot**.
4. There is room between the top of a unit standing in a lane and the shelf above for a gripper holding a unit to pass level over
   it (**unvalidated**).
5. Every unit is a small boxed item of the one SKU, light enough for one gripper to hold by its sides, with a **date label** in large
   print on its front face. The **older units** carry an earlier date than the **new units**.
6. Each lane starts with **one older unit**, standing upright, date label facing out, in its **middle slot** or its **back slot**.
   Which slot is chosen per lane at reset, so it changes from episode to episode. The other slots are empty.
7. The **replenishment cart** is a flat-top cart standing braked against the **left end** of the shelving in **Config L** and against
   the **right end** in **Config R**, its top deck at about the height of the ledge.
8. On its top deck stands the **bulk carton**: a small corrugated carton, open at the top, its four top flaps folded down flat against
   its outside walls. It holds **four new units**, standing upright in one layer, date labels facing the shelving.
9. The carton's **bottom is closed by its four flaps folded into each other**, with no tape, and its fold lines are already broken in,
   so it opens when pushed from inside and folds flat by hand (**unvalidated**).
10. The **flat-carton sleeve** is an open-top sleeve hung on the side of the cart facing the base, wide and deep enough to take the
    carton folded flat.
11. The **work ledge** is a fixed flat ledge running along the front of the shelving below the pick-face level. Its **front strip**
    sticks out past the shelf edges, so nothing is above it. The **breakdown spot** is the middle of the front strip, in line with
    the middle upright.
12. The **log card** sits in a fixed **log holder** on the face of the middle upright, between the pick-face level and the ledge,
    facing out. It has three lines, each with a **tick box** at its right end: **LANE 1 ROTATED AND FILLED**, **LANE 2 ROTATED AND
    FILLED**, **CARTON BROKEN DOWN**. The card is fresh: no box is ticked.
13. The **marker** stands in its **marker clip** beside the log holder, point down.
14. Nothing else stands on the shelving, the ledge, or the cart within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the lane labels. You judge every other place by eye against the shelving itself.

* **Shelving:** the fixed unit the base is parked at. Never moved, never leaned on, never pushed.
* **Lane 1:** the left bin on the pick-face level: front, middle, and back slot. **Left gripper only.**
* **Lane 2:** the right bin on the pick-face level: front, middle, and back slot. **Right gripper only.**
* **Hand-over point:** in front of the middle upright, a hand out from the shelf edge of the pick-face level.
* **Work ledge and breakdown spot:** the ledge below the pick face, with the breakdown spot in the middle of its front strip. **Both
  grippers, for the breakdown only.**
* **Log holder and marker clip:** on the middle upright between the pick-face level and the ledge. **Cart gripper only.**
* **Replenishment cart:** braked against the left end (Config L) or the right end (Config R) of the shelving: bulk carton on the top
  deck, flat-carton sleeve on its side facing the base. **Cart gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works Lane 1 and the **right gripper** works Lane 2. The **cart gripper** also works the cart, the log, and the
  marker.
* The two arms meet only at the **hand-over point** and at the **breakdown spot**.
* Neither arm goes into the other lane, and neither reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds one thing, and while it does, the other gripper is empty, taking a hand-over,
  pinning the carton, or drawn **clear of the shelving**.

### Arm assignments

* **Cart gripper** (**left gripper** in Config L, **right gripper** in Config R). Rotates and fills the lane on its own side, takes
  every new unit out of the carton, hands over the new units for the other lane, carries the empty carton to the breakdown spot,
  opens and folds it, stows it in the sleeve, and ticks the log.
* **Other gripper.** Rotates the older unit in its own lane, takes each hand-over and sets it in its lane, and pins the carton at the
  breakdown spot. It never touches the cart, the carton on the cart, the log, or the marker.
* Only new units are handed over. The carton, the log card, and the marker are never handed over.

## Vocabulary

* **Pick face:** the two lanes pickers take this SKU from.
* **Lane:** one fixed bin of the pick face, one unit wide and three units deep. **Front slot**, **middle slot**, and **back slot**
  name its three places, front to back.
* **Date label:** the large-print date on a unit's front face. An earlier date means an **older unit**.
* **FIFO:** first in, first out. The oldest unit stands at the front, where the next picker takes it, and newer units stand behind it.
* **Lane gripper:** the gripper that works a lane, the **left gripper** for Lane 1 and the **right gripper** for Lane 2.
* **Cart gripper:** the gripper on the cart's side, the **left gripper** in Config L and the **right gripper** in Config R.
* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down into a lane from above.
* **Rotate:** the lane gripper closes on the sides of the older unit, lifts it just clear of the bin floor, draws it straight forward
  to the front slot, and sets it down there.
* **Lift over:** carrying a new unit level, just above the top of the unit in the front slot, to a slot behind it, without touching it.
* **Set unit:** the unit stands upright in its slot on the bin floor, date label facing out, square to the lane, and stays put when the
  gripper opens.
* **Hand over:** the cart gripper brings the new unit to the hand-over point and holds it still for a **half-second hold**. The lane
  gripper then closes on the far side of it. Only after the lane gripper is closed does the cart gripper open and draw back.
* **Pin:** a gripper, open, pressed flat on the carton only as hard as it takes to keep the carton from sliding.
* **Flat carton:** the carton folded along its fold lines into one flat piece, two walls thick, every flap lying flat, nothing torn.
* **Tick:** one mark with the marker inside a tick box: a short stroke down and to the right, then a longer stroke up and to the right,
  without lifting.
* **Clear of the shelving:** the arm is drawn back so that no part of it is in front of a lane, the ledge, the middle upright, or the
  cart.

## Steps

Run Steps 1 to 4 in order, and end the episode with Step 5. Steps 1 and 2 replenish the two lanes, rotation first. Step 3 breaks down
the empty carton and Step 4 logs the work. Only the cart gripper and the hand-overs depend on the config.

### Step 1: Replenish Lane 1

**Goal:** Lane 1 holds its older unit in the front slot and two new units behind it, back slot first.

#### 1.1 Rotate the older unit to the front

* Read the date labels in Lane 1 and find the **older unit**.
* With the **left gripper**, come level into Lane 1 from the front and close on the two sides of the older unit.
* With the **left gripper**, lift it just clear of the bin floor, draw it straight forward to the **front slot**, and set it down there,
  upright, date label facing out.
* With the **left gripper**, open and draw straight out to the front, level.
* With the **right gripper**, stay open and **clear of the shelving** unless it is the cart gripper.

**Check:** the older unit stands in the front slot, upright, date label out, and the middle and back slots are empty. If it sits
crooked, close on its sides with the **left gripper** and set it straight.

#### 1.2 Take a new unit out of the carton

* **IF Config L:** the **left gripper** is the cart gripper. **IF Config R:** the **right gripper** is the cart gripper.
* With the **cart gripper**, close on the two sides of one new unit and lift it straight up out of the carton, touching no other unit
  and not the carton walls.
* Check its date label: it carries the newer date.
* **IF Config L:** with the **left gripper**, carry it level to the front of Lane 1.
* **IF Config R:** with the **right gripper**, carry it to the **hand-over point** and hold it still for a **half-second hold**. With
  the **left gripper**, close on the far side of the unit. With the **right gripper**, open and draw back **clear of the shelving**.

**Check:** the **left gripper** holds one new unit by its sides, date label out, and the units left in the carton still stand.

#### 1.3 Set the new unit behind the older unit

* With the **left gripper**, bring the new unit level into Lane 1, **lifted over** the older unit in the front slot.
* With the **left gripper**, set it down in the **back slot** if the back slot is empty, otherwise in the **middle slot**, upright, date
  label facing out.
* With the **left gripper**, open and draw straight out to the front, level, passing over the older unit without touching it.
* With the **left gripper**, do not let the unit go from above the bin floor and do not push the older unit out of the front slot.

**Check:** the new unit is **set** and the older unit still stands in the front slot. If the older unit has moved, close on it with the
**left gripper** and set it back in the front slot.

Run 1.2 and 1.3 again for the second new unit, so that the back slot and then the middle slot are filled.

**Expected state:** Lane 1 holds the older unit in the front slot and two new units in the middle and back slots, all upright, date
labels out. Two new units are left in the carton.

### Step 2: Replenish Lane 2

**Goal:** Lane 2 holds its older unit in the front slot and two new units behind it, back slot first.

These are the moves of Step 1, made by the **right gripper** in Lane 2.

#### 2.1 Rotate the older unit to the front

* Read the date labels in Lane 2 and find the **older unit**.
* With the **right gripper**, come level into Lane 2, close on the sides of the older unit, lift it just clear, draw it straight
  forward to the **front slot**, and set it down there, date label out.
* With the **right gripper**, open and draw straight out to the front, level.
* With the **left gripper**, stay open and **clear of the shelving** unless it is the cart gripper.

**Check:** the older unit stands in the front slot and the middle and back slots are empty.

#### 2.2 Take a new unit out of the carton

* With the **cart gripper**, close on the sides of one new unit and lift it straight up out of the carton, touching nothing else, and
  check its date label.
* **IF Config R:** with the **right gripper**, carry it level to the front of Lane 2.
* **IF Config L:** with the **left gripper**, carry it to the **hand-over point** and hold it still for a **half-second hold**. With the
  **right gripper**, close on the far side of the unit. With the **left gripper**, open and draw back **clear of the shelving**.

**Check:** the **right gripper** holds one new unit by its sides, date label out.

#### 2.3 Set the new unit behind the older unit

* With the **right gripper**, bring the new unit level into Lane 2, **lifted over** the older unit, and set it down in the **back
  slot** if it is empty, otherwise in the **middle slot**, upright, date label out.
* With the **right gripper**, open and draw straight out, passing over the older unit without touching it.

**Check:** the new unit is **set** and the older unit still stands in the front slot.

Run 2.2 and 2.3 again for the second new unit.

**Expected state:** both lanes hold the older unit at the front and two new units behind it. The carton on the cart is empty.

### Step 3: Break down the empty carton

**Goal:** the empty carton is a **flat carton** standing in the flat-carton sleeve.

#### 3.1 Carry the carton to the breakdown spot

* Look into the carton: it is empty.
* With the **cart gripper**, close on the top rim of the carton wall nearest the shelving, lift the carton straight up just clear of
  the deck, and carry it level to the **breakdown spot**.
* With the **cart gripper**, set it down on its **side**, open top toward the cart's end of the ledge, bottom toward the other end,
  then open and let go.
* With the other gripper, stay open and **clear of the shelving** until the carton is down.

**Check:** the carton lies on its side on the front strip of the ledge, square to the ledge edge, all of it on the ledge.

#### 3.2 Open the bottom

* With the **other gripper**, **pin** the carton: press it flat on the upper side wall, near the bottom end.
* With the **cart gripper**, reach level in through the open top to the inside of the bottom and push it straight out, toward the
  bottom end, until the bottom flaps come apart and swing open.
* With the **cart gripper**, draw straight back out through the open top.
* With the **other gripper**, keep pinning until the **cart gripper** is out, then open and draw back **clear of the shelving**.

**Check:** all four bottom flaps are open and the carton is an open tube on its side. If one flap is still caught, pin again with the
**other gripper** and push that flap out from inside with the **cart gripper**.

#### 3.3 Fold the carton flat

* With the **cart gripper**, open, press flat on the upper side wall near the edge farthest from the base, and push it down and toward
  the shelving, so the tube leans over and folds flat along its fold lines.
* With the **cart gripper**, press each flap that still stands up down flat, one at a time.
* With the other gripper, stay open and **clear of the shelving**.

**Check:** the carton is a **flat carton**. If it has folded across a wall instead of along its fold lines, open it back into a tube with
the **cart gripper** and fold it again along the lines.

#### 3.4 Stow the flat carton

* With the **cart gripper**, close on the edge of the flat carton nearest the cart, lift it just clear of the ledge, and carry it level
  to the **flat-carton sleeve**, turned upright, edge down.
* With the **cart gripper**, lower it straight down into the sleeve until it stands on the bottom, then open and draw straight up and
  **clear of the shelving**.

**Check:** the flat carton stands all the way down in the sleeve, and the ledge and the cart top deck are bare.

**Expected state:** the carton is flat in the sleeve, the ledge and the top deck are bare, and both lanes are still as Step 2 left them.

### Step 4: Log the replenishment

**Goal:** all three lines of the log card carry **one tick** each, and the marker is back in its clip.

#### 4.1 Take the marker

* With the **cart gripper**, close on the **barrel** of the marker, not on its point, and lift it straight up out of its clip.
* With the other gripper, stay open and **clear of the shelving** for the whole of this step.

**Check:** the **cart gripper** holds the marker by its barrel and the point hangs clear.

#### 4.2 Tick the three lines

* Before ticking each line, look at what it names: Lane 1 and Lane 2 each show the older unit at the front with two new units behind
  it, and the carton stands flat in the sleeve.
* With the **cart gripper**, bring the marker point level to the first line's **tick box**, left of its middle, and draw one **tick**,
  then draw the point straight back off the card.
* With the **cart gripper**, keep the tick inside its box. Press only hard enough to leave a mark.
* With the **cart gripper**, tick the second line and then the third line the same way, top to bottom.

**Check:** each of the three lines carries **one tick**, inside its box. If a tick has run outside its box, leave it. Do not draw over
it and do not draw a second tick in the same box.

#### 4.3 Put the marker back

* With the **cart gripper**, carry the marker back and stand it in its clip, point down, then open and draw back **clear of the
  shelving**.

**Check:** the marker stands in its clip point down, and it stays there with the **cart gripper** off it.

**Expected state:** the log is ticked, the marker is in its clip, and both grippers are clear of the shelving.

### Step 5: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the pick face replenished.

* Look once across the shelving and the cart: each lane holds its older unit at the front and two new units behind it, the carton
  stands flat in the sleeve, the log card is ticked, and the marker is in its clip.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the pick face is replenished in FIFO order and logged, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the four new units out of the lanes and stand them back in a fresh or re-folded carton, upright, date labels toward the shelving.
2. In each lane, stand the older unit in the middle slot or the back slot, chosen at random for each lane, date label out.
3. Take the flat carton out of the sleeve. Fold it back into a carton with its bottom flaps folded into each other, or use a fresh one,
   and fold its top flaps down flat against its walls.
4. Stand the carton with its four new units on the cart's top deck.
5. Take the ticked log card out of its holder and put in a fresh one with no box ticked. Check the marker still marks.
6. Move the cart to the end of the shelving for the next episode's config and brake it.
7. Pick up anything that landed on a shelf, the ledge, the cart, or the floor.
8. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the reviewer
sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule was
broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the shelving shifts in frame, the shelf edges change angle or size in frame, or the base rolls, creeps, or turns at
  any point after recording starts.
* **SOP rule broken:** Steps 1 to 5, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Approached from above or fouled the shelf**

* **Visible cue:** a gripper comes down into a lane from above instead of coming in level from the front, or a wrist, forearm, or unit
  knocks, scrapes, or rests on the shelf above the pick face.
* **SOP rule broken:** Steps 1 and 2, every reach into a lane is a front approach, level, straight in and straight out.
* **Coaching note:** straight in from the front, straight out the same way.

**Violation: Leaned on or pushed the shelving, ledge, or cart**

* **Visible cue:** a gripper, wrist, or forearm rests on a shelf, an upright, a bin, the ledge, or the cart; a bin shifts; or the cart
  or shelving rocks or moves.
* **SOP rule broken:** Steps 1 to 4, the shelving, the ledge, and the cart carry no weight from the arms.
* **Coaching note:** the arm holds itself up. Press only as hard as the move needs.

**Violation: FIFO broken**

* **Visible cue:** a new unit ends up in front of the older unit; the older unit is left in the middle or back slot; or a new unit goes
  into a lane before its older unit has been rotated to the front.
* **SOP rule broken:** Steps 1.1, 1.3, 2.1, and 2.3, rotate the older unit to the front first, then set the new units behind it.
* **Coaching note:** oldest out first. Read the dates, then move the old one forward before anything new goes in.

**Violation: Rotation done wrong**

* **Visible cue:** the older unit is taken right out of the lane, dragged along the bin floor, turned so its date label faces in, or
  pushed forward by another unit instead of being lifted and drawn forward by its sides.
* **SOP rule broken:** Steps 1.1 and 2.1, close on the older unit's sides, lift it just clear, and draw it straight forward to the front
  slot.
* **Coaching note:** lift, draw forward, set down. It stays in its lane the whole time.

**Violation: Slots filled out of order**

* **Visible cue:** the first new unit in a lane goes into the middle slot while the back slot is empty, a lane ends with a gap between
  units, or a lane gets more or fewer than two new units.
* **SOP rule broken:** Steps 1.3 and 2.3, fill the back slot first, then the middle slot, two new units per lane.
* **Coaching note:** back first, then middle. A gap is a unit a picker cannot reach.

**Violation: Front unit knocked during the lift over**

* **Visible cue:** a new unit or the gripper touches, pushes, or tips the older unit in the front slot on the way in or out, or the older
  unit ends up out of its slot.
* **SOP rule broken:** Steps 1.3 and 2.3, carry the new unit level, lifted over the older unit, and come out the same way.
* **Coaching note:** over the top, not through it. Check the gap above the front unit before the arm goes in.

**Violation: Unit dropped in or not set**

* **Visible cue:** a unit is let go from above the bin floor and falls in, lies on its side, stands crooked or across the lane, or has its
  date label facing in.
* **SOP rule broken:** Steps 1.1, 1.3, 2.1, and 2.3, set each unit down on the bin floor, upright, date label out, before opening.
* **Coaching note:** down to the floor, then open. A dropped unit is a damaged unit.

**Violation: New unit taken wrong**

* **Visible cue:** a new unit is held by its top, its label, or one corner; dragged up the carton wall; or lifted so that another unit
  in the carton tips or comes out with it.
* **SOP rule broken:** Steps 1.2 and 2.2, close on the sides of one new unit and lift it straight up, touching nothing else.
* **Coaching note:** one unit, sides in the gripper, straight up.

**Violation: Hand-over done wrong**

* **Visible cue:** the cart gripper opens before the lane gripper has closed; the unit is still moving when the lane gripper closes, with
  no half-second hold; the hand-over happens away from the hand-over point; or a unit for the cart's own lane is handed over.
* **SOP rule broken:** Steps 1.2 and 2.2, hand over only units for the lane away from the cart, at the hand-over point, held still, and
  open only after the lane gripper has closed.
* **Coaching note:** stop, hold still, let the lane gripper take it, then open.

**Violation: Carton broken down too early or carried wrong**

* **Visible cue:** the carton is moved while a unit is still in it; it is carried by a flap, dragged across the deck or the ledge, or
  set down upright or off the front strip of the ledge.
* **SOP rule broken:** Step 3.1, check the carton is empty, carry it by the top rim of a wall, and lay it on its side at the breakdown
  spot.
* **Coaching note:** empty first, then carry it by the rim, flat and level.

**Violation: Bottom opened wrong**

* **Visible cue:** the bottom is pushed out with the carton not pinned, so the carton slides along or off the ledge; a flap is torn or
  pulled off; or the carton is opened by pulling the flaps from outside.
* **SOP rule broken:** Step 3.2, the other gripper pins the carton while the cart gripper pushes the bottom out from inside.
* **Coaching note:** pin, then push. The pin is what makes the push work.

**Violation: Carton not flat**

* **Visible cue:** the carton is folded across a wall instead of along its fold lines, crushed, torn, or left with a flap standing up.
* **SOP rule broken:** Step 3.3, fold the tube flat along its fold lines and press every flap down flat.
* **Coaching note:** let the fold lines do the work. Lean the tube over, do not crush it.

**Violation: Flat carton not stowed**

* **Visible cue:** the flat carton is left on the ledge or the cart deck, dropped, set on the floor, or left standing only part way
  into the sleeve.
* **SOP rule broken:** Step 3.4, the cart gripper lowers the flat carton all the way down into the flat-carton sleeve.
* **Coaching note:** into the sleeve, all the way down. The ledge ends bare.

**Violation: Log filled in wrong**

* **Visible cue:** a line is skipped or ticked twice; lines are ticked out of top-to-bottom order; a line is ticked before the work it
  names is done; a tick is drawn over; or any other mark is made on the card.
* **SOP rule broken:** Step 4.2, look at what each line names, then tick it once, top to bottom, inside its box.
* **Coaching note:** the log is the record. Look, then tick, one tick per line.

**Violation: Marker handled wrong**

* **Visible cue:** the marker is held by its point, pressed hard enough to bend its tip or push the card, laid on a shelf or the ledge,
  dropped, or not stood back in its clip point down.
* **SOP rule broken:** Steps 4.1 and 4.3, hold the marker by its barrel and stand it back in its clip, point down.
* **Coaching note:** barrel in the gripper, light on the card, back in the clip.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the shelving is not set up in: the gripper away from the cart takes a unit out of the carton,
  carries the carton, or ticks the log; a gripper reaches for a cart end that is empty; or the cart is moved before or during the
  episode.
* **SOP rule broken:** Steps 1.2, 2.2, 3, and 4, look at the shelving, find the cart, and follow the IF line that matches the config the
  episode is set up in.
* **Coaching note:** look at the cart before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** Lane 2 is worked before Lane 1 is full; the carton is moved before both lanes are full; the log is ticked before the
  carton is in the sleeve; or a lane is fixed after the log is ticked.
* **SOP rule broken:** Steps 1 to 4, replenish Lane 1, then Lane 2, rotation first in each, then break down the carton, then log.
* **Coaching note:** the order is the task. Each step leaves the pick face ready for the next one.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two units, or a unit and the marker; both grippers carry different things at the same time outside a
  hand-over; or a gripper holds something while the other works instead of being clear of the shelving.
* **SOP rule broken:** Steps 1 to 4, one gripper holds one thing, and the other is empty, taking a hand-over, pinning the carton, or clear
  of the shelving.
* **Coaching note:** one thing, one trip.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a unit crooked or
  out of its slot, a bottom flap still caught, a carton folded across a wall, a flat carton part way into the sleeve.
* **SOP rule broken:** Steps 1.1 to 4.3, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a unit, the carton, or the marker is dropped on a shelf, the ledge, the cart, or the floor; a unit in a lane or the
  carton is knocked over; or a unit is knocked out of its lane.
* **SOP rule broken:** Steps 1 to 4, nothing is dropped or knocked out of its place, and every gripper comes out the way it went in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **left gripper** goes into Lane 2; the **right gripper** goes into Lane 1; the gripper away from the cart touches
  the cart, the carton on the cart, the log, or the marker; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 4, each gripper works its own lane, only the cart gripper works the cart and the log, and the arms never
  cross.
* **Coaching note:** Lane 1, left arm. Lane 2, right arm. The cart side decides who fetches and who logs.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with an older unit behind a new one, a lane short of units, the carton not flat in the sleeve, a log
  line not ticked, the marker out of its clip, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 5, look once across the shelving and the cart, then return both arms home with grippers open and stop
  recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a date label, a lane label, or the log card**, so which unit is older, where it ended up, or which box is ticked
  cannot be judged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Stock or carton fault:** a new unit with an older date than a lane's older unit, a unit missing or damaged at the start, a carton
  whose bottom will not open or whose fold lines are not broken in, or a marker that has dried out.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a back slot, the hand-over point,
  the breakdown spot, the sleeve, or the log card cannot be reached without extending or folding the arm, or the gap above a front unit
  is too small for a lift over.

## Annotation subtasks (from SOP)

1. Rotate one older unit to the front slot
2. Take one new unit out of the carton
3. Hand one new unit over at the hand-over point
4. Set one new unit behind the older unit
5. Carry the empty carton to the breakdown spot
6. Push the carton's bottom open
7. Fold the carton flat
8. Stow the flat carton in the sleeve
9. Take the marker from its clip
10. Tick one log line
11. Stand the marker back in its clip
12. Return both arms home and end the episode
