# Induct Totes to the Conveyor SOP (1x Episode: two totes, in situ)

One episode inducts two totes onto the takeaway conveyor, at the induct bench where the conveyor starts. The base is **passive**: it
has no drive of its own, so it is pushed by hand to the front of the bench and locked there, and nothing is carried away to a table.
Everything the episode touches is already at the bench when recording starts: the bin of loose items, the stack of empty totes, the
label dispenser, the scale with its display, and the running takeaway conveyor.

The episode runs these four actions for each tote, in this order and no other: **load loose items into the tote, apply the tote label,
verify the weight, push the tote onto the takeaway conveyor.** The first tote is on the conveyor and gone before the second is taken off
the stack.

The bench is worked **as found**. The **item bin** holds **eight loose items**, all the same, lying as they fell. The **tote stack** holds
two empty totes, one nested in the other. The **scale** is empty and the **takeaway conveyor** is running, empty. The episode ends with two
totes on their way down the conveyor, each holding four items, each labelled, each weighed green, and the item bin and tote stack empty.

**The scale checks the count.** Every item weighs the same, so four items in a tote weigh the same every time. The scale knows that weight.
A **green** verify means the tote holds four items. A **red** verify means it does not, and the tote is fixed before it goes anywhere.

**This is an in-situ task, and three things follow from that.** First, **the takeaway conveyor is running**: once a tote is past the induct
line, it belongs to the conveyor, and no gripper touches it or the belt again. Second, the **bench, the scale, and the conveyor are never
leaned on and never pushed**: no gripper, wrist, or forearm rests on the worktop, the scale, the display, the dispenser, or the
conveyor frame, and nothing touches the tote on the scale while it is being weighed. Third, **each item goes from the bin to the tote and
nowhere else**: nothing is set down on the worktop, the scale edge, or the floor on the way.

The bench is set up in one of two ways. The **item bin** and the **tote stack with the label dispenser** swap ends. The scale, the display,
and the conveyor are in the same place in both.

* **Config L:** the item bin is at the **left end** of the bench, and the tote stack and the label dispenser are at the **right end**.
* **Config R:** the item bin is at the **right end** of the bench, and the tote stack and the label dispenser are at the **left end**.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says so on an **IF**
line. Look at the bench and follow the line that matches.

What stays constant across all sessions:

* **Bin-side rule:** the gripper on the item bin's side loads every item. It is called the **item gripper**: the **left gripper** in
  Config L and the **right gripper** in Config R.
* **Tote-side rule:** the gripper on the tote stack's side moves every empty tote, applies every label, and presses every scale button. It
  is called the **tote gripper**: the **right gripper** in Config L and the **left gripper** in Config R.
* **Push rule:** **both grippers** push each loaded tote onto the conveyor together, the left gripper on the left half of the tote and the
  right gripper on the right half.

Nothing is ever handed over. **The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm
reaches over, under, around, or past the other. Nothing is moved two at a time: outside the push, one gripper holds one thing, and the
other gripper is empty and clear of the scale.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or repositioned once
recording starts. It is parked once, before recording, and does not move again until the episode is over.

1. Push the base by hand up to the front of the bench and stop it **square to it**, so the worktop edge runs straight across the frame of the
   camera.
2. Stop it **centered on the scale**, so the middle of the base is in line with the middle of the scale platform.
3. Stop it **close enough** that both grippers reach the far side of a tote on the scale and the induct line without either arm extending,
   and **far enough** that neither arm, wrist, nor any part of the base touches the bench while both arms work.
4. Check the **item side** for the config this episode runs: the **item gripper** reaches the bottom of the item bin and every corner of a tote
   on the scale.
5. Check the **tote side**: the **tote gripper** reaches the top of the tote stack, the label dispenser, the tote's label panel on the scale,
   and both display buttons.
6. Check the **push**: with a tote on the scale, the **left gripper** reaches the left half of its front side and the **right gripper** the right
   half, and both reach the induct line.
7. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
8. If any of lines 1 to 6 fails, push the base to a new park by hand and start again at line 1. Do not work a bench the arms cannot reach
   comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the bench hard enough to shift it, nothing touches
it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the scale and its frame includes the whole worktop: the item bin, the tote stack, the label dispenser,
   the scale with its outline, the display, and the conveyor from the induct line to the edge of the bench.
3. The camera reads the **display**: the weight, and which of the green and red lights is lit.
4. The camera sees into a tote on the scale well enough to count the items in it, and reads the **tote label** on its front side.
5. Both arms are at home with grippers open.
6. The **item arm** for this config reaches the bin and the whole tote without extending to a joint limit.
7. The **tote arm** for this config reaches the stack, the dispenser, the label panel, and both buttons without extending to a joint limit.
8. Both arms reach the tote's front side and the induct line without extending to a joint limit.
9. The two arms do not collide, and neither arm passes in front of the other.
10. If a place cannot be reached, re-park the base by the Base positioning steps until lines 6 to 9 hold.

### Materials checklist

1. The **induct bench** stands where it lives, fixed to the floor. It is not moved, not leaned on, and not pushed at any point. Its worktop is
   at about waist height, and nothing is above it.
2. The **scale platform** is set flush into the middle of the worktop, with a painted **outline** one tote in size. It weighs whatever stands on
   it.
3. The **display** is fixed on the front edge of the bench, just below the middle of the scale, facing the base, clear of the push path. It shows the weight in large figures and has
   two buttons, **TARE** and **VERIFY**, and two lights, **green** and **red**. TARE sets the weight shown to zero. VERIFY lights green if the
   weight shown is that of four items, and red if it is not (**unvalidated**: the mock must know the four-item weight).
4. The **takeaway conveyor** runs along the back edge of the bench, level with the worktop, carrying away to the right, out of reach. It is
   **running** for the whole episode. A **transfer plate** bridges the gap between the back of the scale and the belt. The **induct line** is a
   painted line along the near edge of the belt.
5. The **item bin** is an open bin standing on the worktop at the **left end** in **Config L** and at the **right end** in **Config R**. It holds
   **eight loose items**, all the same: small boxed items that fit one gripper, the same weight to within a few grams, lying as they fell.
6. The **tote stack** stands on the worktop at the other end from the item bin, near the scale: **two empty totes**, one nested in the other.
   Each tote is small and light enough for one gripper to lift by its rim, and big enough for four items standing in two rows of two. Each has a
   flat **label panel** on one long side.
7. The **label dispenser** is fixed on the worktop beside the tote stack, at the back. It holds a roll of tote labels and presents **one label**
   at a time, peeled back from its backing with a dry **tab** at its top edge sticking out. When a label is taken, the next one comes forward.
8. Nothing else stands on the worktop or the conveyor within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the scale outline and the induct line. You judge every other place by eye against the bench itself.

* **Induct bench:** the fixed bench the base is parked at. Never moved, never leaned on, never pushed.
* **Item bin:** at the left end (Config L) or the right end (Config R). **Item gripper only.**
* **Tote stack and label dispenser:** at the other end. **Tote gripper only.**
* **Scale:** in the middle, with its outline. The tote stands here while it is loaded, labelled, and weighed.
* **Display:** on the front edge of the bench below the scale, with TARE and VERIFY. **Tote gripper only.**
* **Takeaway conveyor:** along the back edge, behind the scale, with the induct line. Both grippers during the push only. **Nothing touches a tote
  past the induct line.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **item gripper** works the item bin and the inside of the tote. The **tote gripper** works the tote stack, the dispenser, the label panel,
  and the display.
* Both grippers meet only at the tote's front side, for the push, one on each half.
* Neither arm reaches over, under, around, or past the other.
* Outside the push, only one thing is moved at a time. A gripper holds one thing, and while it does, the other gripper is empty and drawn **clear
  of the scale**.

### Arm assignments

* **Item gripper** (**left gripper** in Config L, **right gripper** in Config R). Takes each item out of the bin and sets it in the tote on the scale,
  and fixes the count after a red verify. Pushes the tote's half on its side.
* **Tote gripper** (**right gripper** in Config L, **left gripper** in Config R). Takes each empty tote off the stack and sets it on the scale, presses
  TARE and VERIFY, and applies the tote label. Pushes the tote's half on its side.
* Nothing is handed over.

## Vocabulary

* **Induct:** put a tote onto the conveyor so the conveyor system takes it from there.
* **Item gripper / tote gripper:** the gripper on the item bin's side and the gripper on the tote stack's side.
* **Seated tote:** the tote stands flat inside the scale outline, long sides running left to right, label panel facing the base, touching
  nothing but the scale.
* **Tare:** the tote gripper presses TARE once with the empty tote seated, so the display reads zero with the empty tote on it.
* **Tote order:** items go into the tote standing upright on its floor in two rows of two: back row first, then front row, each row filling from
  the item gripper's side outward. No item stands on another.
* **Set item:** the item stands upright on the tote floor in its place in the tote order and stays put when the gripper opens.
* **Tab:** the dry strip at the top edge of the presented label. It is the only part of a label a gripper touches.
* **Applied label:** the label is flat on the middle of the label panel, straight, its edges inside the panel, with no fold, bubble, or lifted
  corner.
* **Verify:** the tote gripper presses VERIFY once, then draws clear, and both grippers stay off the tote and the scale until a light shows.
* **Green / red:** green means the tote holds four items. Red means it does not.
* **Push:** both grippers, closed, press flat on the tote's front side, one on each half, low on the wall, and push it straight back across the
  transfer plate until its front side is past the induct line.
* **Press:** the closed gripper comes straight at a button, pushes it once until it clicks, and draws straight back.
* **Clear of the scale:** the arm is drawn back so that no part of it is over the tote, the scale, or the transfer plate.

## Steps

Run Steps 1 to 5 once for each of the two totes, then end the episode with Step 6. The config decides which gripper is the item gripper and which
is the tote gripper. Nothing else changes between configs.

### Step 1: Place an empty tote on the scale

**Goal:** one empty tote is **seated** on the scale and the display reads zero.

* **IF Config L:** the **right gripper** is the tote gripper. **IF Config R:** the **left gripper** is the tote gripper.
* With the **tote gripper**, close on the rim of the **top tote** in the stack at its end nearest the scale, and lift it straight up until it is
  clear of the tote under it.
* With the **tote gripper**, carry it level to the scale, long sides left to right, label panel facing the base, and set it down flat inside the
  outline, then open and draw back.
* With the **tote gripper**, closed, **press** TARE once, then draw back **clear of the scale**.
* With the item gripper, stay open and **clear of the scale** for the whole of this step.

**Check:** the tote is **seated** and the display reads zero. If the tote sits across the outline, close on its rim with the **tote gripper** and set
it straight, then press TARE again.

### Step 2: Load four items

**Goal:** four items are **set** in the tote in the tote order.

* **IF Config L:** the **left gripper** is the item gripper. **IF Config R:** the **right gripper** is the item gripper.
* With the **item gripper**, come down into the item bin from above and close on the two sides of the item lying nearest the top, one item only.
* With the **item gripper**, lift it straight up out of the bin and turn it upright in the air.
* With the **item gripper**, carry it level to the tote and bring it straight down to just above the tote floor at its place in the **tote order**.
* With the **item gripper**, set it down upright, then open and lift straight up.
* Count one. Repeat until four items are in the tote.
* With the tote gripper, stay open and **clear of the scale** for the whole of this step.

**Check:** the tote holds four items, each upright in its place, and nothing rests on the tote rim. If an item has tipped, close on it with the **item
gripper** and stand it up in its place.

### Step 3: Apply the tote label

**Goal:** one tote label is **applied** on the middle of the tote's label panel.

* With the **tote gripper**, close on the **tab** of the presented label and draw it straight up, off its backing, keeping the label hanging flat and
  its sticky face away from everything.
* With the **tote gripper**, carry it to the tote's label panel, sticky face toward the panel, and bring it in level until the label's middle is just
  in front of the middle of the panel.
* With the **tote gripper**, touch the label onto the panel, top edge first, and let the rest of it lie against the panel.
* With the **tote gripper**, open, and wipe once across the label with the closed gripper's side, from the middle outward to the left, then once from the
  middle outward to the right, pressing lightly.
* With the **tote gripper**, draw back **clear of the scale**.
* With the item gripper, stay open and **clear of the scale** for the whole of this step.

**Check:** the label is **applied**. If a corner has lifted, wipe that corner once more with the side of the closed **tote gripper**. If the label has
folded onto itself or stuck crooked, leave it on and log it as a label fault after the episode; do not peel it off.

### Step 4: Verify the weight

**Goal:** the tote is weighed and the display shows green.

* With the **tote gripper**, closed, **press** VERIFY once, then draw straight back **clear of the scale**.
* With **both grippers**, stay off the tote and the scale until a light shows.
* **IF green:** the tote holds four items. Go on to Step 5.
* **IF red:** count the items in the tote. With the **item gripper**, take an item out and put it back in the bin if there are more than four, or add one
  from the bin if there are fewer, then draw clear, and with the **tote gripper** press VERIFY again.

**Check:** the green light is lit, and neither gripper touched the tote while it was being weighed.

### Step 5: Push the tote onto the takeaway conveyor

**Goal:** the tote is past the induct line and being carried away, and both grippers are clear.

* Look at the conveyor behind the scale: the belt in front of the transfer plate is clear. **IF the last tote has not yet been carried past the edge of
  the scale:** wait with both grippers clear until it has.
* With the **left gripper** and the **right gripper**, both closed, come level to the tote's front side, low on the wall, the **left gripper** on its left
  half and the **right gripper** on its right half, keeping clear of the label.
* With **both grippers** together, push the tote straight back across the transfer plate, square to the belt, until its front side is past the **induct
  line**.
* With **both grippers**, draw straight back at once and **clear of the scale**. Do not touch the tote again.

**Check:** the tote is on the belt past the induct line and moving away, square, with its items upright and its label facing the base. If it stops on the
transfer plate short of the line, push it again with **both grippers** in the same way.

**Expected state:** the tote is inducted and the scale is empty. **IF a tote is still on the stack:** go back to Step 1. **IF the stack is empty:** go on
to Step 6.

### Step 6: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with both totes inducted.

* Look once across the bench: the item bin and the tote stack are empty, the scale is empty, and both totes have gone down the conveyor with four items
  each and their labels on.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** both totes are inducted, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take both totes off the end of the conveyor. Tip the items back into the item bin so they lie as they fall.
2. Peel the labels off the totes and nest the totes back into the tote stack.
3. Check the dispenser presents a label with its tab out, and refill the roll when it is low.
4. Swap the item bin and the tote stack with the dispenser to the ends for the next episode's config.
5. Check the scale reads zero when empty and VERIFY lights green with four items and red with three or five.
6. Pick up anything that landed on the worktop, the conveyor, or the floor.
7. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the reviewer sees. The coaching
note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the bench shifts in frame, the worktop edge changes angle or size in frame, or the base rolls, creeps, or turns at any point after
  recording starts.
* **SOP rule broken:** Steps 1 to 6, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Leaned on or pushed the bench, scale, or conveyor**

* **Visible cue:** a gripper, wrist, or forearm rests on the worktop, the scale, the display, the dispenser, or the conveyor frame, or the bench or
  display shakes.
* **SOP rule broken:** Steps 1 to 5, the bench, the scale, and the conveyor carry no weight from the arms.
* **Coaching note:** the arm holds itself up. Press only as hard as the move needs.

**Violation: Touched the running conveyor**

* **Visible cue:** a gripper touches the belt, reaches past the induct line, or touches a tote that is already past the induct line.
* **SOP rule broken:** Step 5, once a tote is past the induct line it belongs to the conveyor, and nothing touches it or the belt.
* **Coaching note:** push, then let go of it for good. The belt does not stop for a gripper.

**Violation: Tote taken wrong**

* **Visible cue:** both totes come off the stack together, the tote is dragged across the worktop, held by its label panel, or lifted by a corner so it
  swings.
* **SOP rule broken:** Step 1, lift the top tote alone by the rim at its end nearest the scale and carry it level.
* **Coaching note:** one tote, lifted clear of the one under it, then carry.

**Violation: Tote not seated**

* **Visible cue:** the tote stands across the scale outline, crooked, turned with its label panel away from the base, or touching the display or the
  item bin.
* **SOP rule broken:** Step 1, set the tote flat inside the outline, long sides left to right, label panel facing the base.
* **Coaching note:** inside the lines, square, label panel out. A tote off the scale weighs wrong.

**Violation: Tare skipped or done wrong**

* **Visible cue:** items go into the tote without TARE being pressed; TARE is pressed with items already in the tote or with a gripper touching the tote;
  or TARE is pressed before the tote is on the scale.
* **SOP rule broken:** Step 1, press TARE once with the empty tote seated and nothing else touching it.
* **Coaching note:** empty tote, hands off, tare. The zero is what the check is built on.

**Violation: Item taken wrong**

* **Visible cue:** two items come out of the bin together, the gripper digs under or drags items across the bin, or an item is held by one corner.
* **SOP rule broken:** Step 2, close on the sides of the item nearest the top, one item only, and lift it straight up.
* **Coaching note:** the top one, sides in the gripper, straight up.

**Violation: Item dropped in or not set**

* **Visible cue:** an item is let go from above the tote floor and falls in; it lies on its side, stands on another item, or rests on the rim; or the tote
  order is not kept.
* **SOP rule broken:** Step 2, bring each item down to just above the tote floor and set it upright in its place, back row first.
* **Coaching note:** down to the floor, then open. Back row, then front row.

**Violation: Wrong count loaded**

* **Visible cue:** the item gripper stops loading with more or fewer than four items in the tote.
* **SOP rule broken:** Step 2, load four items, counting each one.
* **Coaching note:** count as each one lands. The scale will catch you, but the count is yours.

**Violation: Label taken wrong**

* **Visible cue:** the label is gripped by its sticky face instead of its tab; it folds onto itself, tears, or sticks to the gripper; or two labels come
  off together.
* **SOP rule broken:** Step 3, close on the tab only and draw the label straight up, hanging flat, sticky face away from everything.
* **Coaching note:** tab only. A sticky face touched is a label spoiled.

**Violation: Label applied wrong**

* **Visible cue:** the label goes on the wrong side of the tote, off the middle of the panel, crooked, over the rim, or on the scale; it has a fold,
  bubble, or lifted corner left unwiped; or a stuck label is peeled back off.
* **SOP rule broken:** Step 3, touch the label onto the middle of the panel top edge first, then wipe it flat from the middle out.
* **Coaching note:** middle of the panel, top edge first, then wipe out. Once it is on, it stays on.

**Violation: Weight not verified**

* **Visible cue:** a tote is pushed without VERIFY being pressed, or without a green light; or VERIFY is pressed before the label is on.
* **SOP rule broken:** Step 4, press VERIFY after the label is applied, and push only on green.
* **Coaching note:** no green, no push. The scale is the last check before the tote is gone.

**Violation: Weight disturbed during the verify**

* **Visible cue:** a gripper touches the tote, an item, or the scale between the press of VERIFY and the light, or the tote gripper stays pressed on
  VERIFY.
* **SOP rule broken:** Step 4, press VERIFY once, draw clear, and keep both grippers off the tote and the scale until a light shows.
* **Coaching note:** hands off while it weighs. A touch is a false weight.

**Violation: Red ignored**

* **Visible cue:** a red light is followed by the push, or VERIFY is pressed again and again with no item added or taken away.
* **SOP rule broken:** Step 4, on red, count the items, fix the count to four with the item gripper, and verify again.
* **Coaching note:** red means the count is wrong. Fix the tote, not the scale.

**Violation: Push done wrong**

* **Visible cue:** the tote is lifted instead of pushed; it is pushed by one gripper, at a slant, by the rim, or by an item inside it; the label is pushed
  on; or the tote stops short of the induct line and is left there.
* **SOP rule broken:** Step 5, both grippers press flat on the front side, one on each half, low on the wall, and push it straight back past the induct line.
* **Coaching note:** two hands, low and flat, straight back, all the way past the line.

**Violation: Pushed onto an occupied belt**

* **Visible cue:** a tote is pushed while the last tote is still in front of the transfer plate, so the two totes touch or jam.
* **SOP rule broken:** Step 5, look at the belt first and push only when the belt in front of the transfer plate is clear.
* **Coaching note:** look, then push. Two totes in one place is a jam.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the bench is not set up in: the gripper away from the item bin loads an item, the gripper away from the tote
  stack moves a tote, takes a label, or presses a button, or the bin or the stack is moved before or during the episode.
* **SOP rule broken:** Steps 1 to 4, look at the bench, find the item bin and the tote stack, and follow the IF line that matches the config the episode is
  set up in.
* **Coaching note:** look at the bin before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** items go in before the tare; the label goes on before the four items are in; VERIFY is pressed before the label; or the second tote is
  taken off the stack before the first is past the induct line.
* **SOP rule broken:** Steps 1 to 5, for each tote: seat and tare, load, label, verify, push, then the next.
* **Coaching note:** the order is the task. Each tote is finished and gone before the next one starts.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two items, or an item and a label; both grippers carry things at the same time; or a gripper holds something while the
  other works instead of being clear of the scale.
* **SOP rule broken:** Steps 1 to 4, one gripper holds one thing, and the other is empty and clear of the scale. Only the push uses both grippers at once.
* **Coaching note:** one thing, one trip. Two hands only for the push.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a tote across the outline, a tipped item,
  a lifted label corner, or a tote stopped short of the induct line.
* **SOP rule broken:** Steps 1 to 5, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** an item, a tote, or a label is dropped on the worktop, the conveyor, or the floor; an item is knocked out of the tote or the bin; or the tote
  stack is knocked over.
* **SOP rule broken:** Steps 1 to 5, nothing is dropped or knocked out of its place, and every gripper comes out the way it went in.
* **Coaching note:** check the path and the landing place before the arm moves.

**Violation: Wrong arm used**

* **Visible cue:** the tote gripper loads an item, the item gripper moves a tote, takes a label, or presses a button, only one gripper pushes, or either arm
  passes in front of the other.
* **SOP rule broken:** Steps 1 to 5, the item gripper loads, the tote gripper does totes, labels, and buttons, both push, and the arms never cross.
* **Coaching note:** the bin side loads, the stack side does the rest, and both push.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a tote on the scale or the stack, an item in the bin, a tote inducted without green, an arm short of home, or a gripper
  not fully open.
* **SOP rule broken:** Step 6, look once across the bench, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read the display, the lights, the tote label, or the items in a tote**, so the weight, the count, or the label cannot be judged.
* **Scale fault:** TARE does not zero, the weight drifts with nothing touching it, or VERIFY shows red on four items or green on three or five.
* **Conveyor fault:** the belt stops, jams, or runs the wrong way.
* **Label fault:** the dispenser presents no label, presents two, or presents one with no dry tab; or a label folds or sticks crooked as it goes on.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so the bottom of the bin, the stack, the dispenser, a button,
  or the induct line cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Lift the top tote off the stack
2. Set the tote on the scale
3. Press TARE
4. Take one item out of the bin
5. Set one item in the tote
6. Take a label by its tab
7. Stick the label on the label panel
8. Wipe the label flat
9. Press VERIFY
10. Push the tote onto the conveyor with both grippers
11. Return both arms home and end the episode
