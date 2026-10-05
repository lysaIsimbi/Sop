# Tend a CNC Mock Cell SOP (1x Part, in situ)

One episode tends the CNC mock once where it stands: open the doors, take the finished part out of the
vise, blow the chips off the vise, load one stock block in the vise, tighten the vise handle, close the
doors, and press Cycle Start. The episode ends when the finished part lies in the finished tray, the stock
block is clamped in the vise, the doors are shut, and the machine shows its CYCLE lamp. Never split one
part change into two episodes.

The base is **passive**: it has no drive of its own, so it is pushed by hand up to the front of the
machine and locked there. Everything the episode touches is already at the machine when recording
starts: the machine with its doors, vise, and control panel, the stock tray, the blower, and the finished
tray.

The machine is worked **as found**. It starts at the end of a cycle: the doors are shut, the finished
part is still clamped in the vise, and chips lie on the vise and the table round it. The stock tray holds
one stock block. The finished tray is empty.

**This is an in-situ task, and four things follow from that.** First, **the machine is never leaned on
and never pushed**: no gripper, wrist, or forearm rests on the doors, the door opening, the front ledge,
or the control panel, and the only pushes in this SOP are the doors being slid, the vise handle being
turned, and Cycle Start being pressed. Second, **the grippers come into the machine only through the
door opening, level, and only once both leaves are open.** Third, **chips are blown to the back, never
out**: the blower always points to the back of the machine, away from the doors and the base. Fourth,
**nothing is dropped or thrown**: the part, the block, and the blower are held over the place they go
and let go there.

The order never changes: **open the doors; unload the finished part; blow the chips; load the stock;
tighten the vise and torque the handle; close the doors; press Cycle Start.** The vise is clean before
the block goes in, the handle is torqued before the doors close, and the doors are shut before Cycle
Start is pressed.

The station is set up in one of two ways. Only the **stock end** (the stock tray with the blower cup
beside it) and the **finished end** (the finished tray) swap. The machine, the vise, the doors, and the
control panel are the same in both.

* **Config L:** the stock tray and the blower cup stand at the **left** end of the front ledge. The
  finished tray stands at the **right** end.
* **Config R:** the stock tray and the blower cup stand at the **right** end of the front ledge. The
  finished tray stands at the **left** end.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on
the setup it says so on an **IF** line. Look at the ledge and follow the line that matches.

What stays constant across both configs:

* **Stock-side rule:** the gripper on the stock tray's side is the **stock gripper**: the **left
  gripper** in Config L and the **right gripper** in Config R. It blows the chips, takes the stock block,
  sets it in the vise, and holds it down while the vise is tightened.
* **Finished-side rule:** the other gripper is the **part gripper**: the **right gripper** in Config L
  and the **left gripper** in Config R. It loosens the vise, takes the finished part out and lays it in
  the finished tray, and closes and torques the vise handle.
* **Door rule:** each gripper works the leaf on its own side. The **left gripper** slides the left leaf
  and the **right gripper** slides the right leaf, in both configs.
* **Panel rule:** the control panel is on the right of the machine, so the **right gripper** presses
  Cycle Start in both configs.
* Nothing is handed over, and neither gripper does the other's work.

The machine is a mock. Nothing cuts. The spindle stays parked high at the back. Cycle Start lights the
CYCLE lamp and nothing else moves. The cycle is stopped during the reset.

## Setup

Complete the base positioning and all the checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never
steered, pushed, or moved once recording starts. It is parked once, before recording, and does not move
again until the episode is over.

1. Push the base by hand up to the front ledge and stop it **square to the front of the machine**, so the
   front ledge runs straight across the frame and neither end sits nearer than the other.
2. Stop it **in the middle of the doors**, so the line where the two leaves meet is straight ahead of the
   middle of the base.
3. Stop it **close enough** that each gripper reaches through the door opening to the back of the vise
   without the arm stretching out, and **far enough** that no arm, wrist, or part of the base touches
   the front ledge or the doors while both arms work.
4. Check the **doors**: the **left gripper** reaches the left leaf's handle and slides the leaf all the
   way open and all the way shut. The **right gripper** does the same with the right leaf. Neither arm
   stretches out.
5. Check the **vise**: both grippers reach the vise handle knob all the way round its half turn, and both
   reach down to the vise ledges, without stretching out and without touching the door opening.
6. Check the **ledge**: the stock gripper reaches the stock tray and the blower cup, and the part gripper
   reaches the finished tray, all without stretching out and without knocking anything over.
7. Check the **panel**: the **right gripper** reaches the Cycle Start button from the front without
   stretching out.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not
   work a machine the arms cannot reach easily.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the machine
hard enough to shift it, nothing and nobody touches it, and it is never moved mid-task. A base that moves
after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is in the middle of the doors, and its frame shows both leaves with their
   handles, the whole door opening, the vise with its handle, the whole front ledge with the stock tray,
   the blower cup, and the finished tray, and the control panel with Cycle Start and the lamps.
3. The camera reads into the machine through the open doors, so the vise ledges, the jaw faces, and any
   chips on them can be seen.
4. The camera reads the vise handle, so whether it points left or right, and its small jump at the
   click, can be seen.
5. The camera reads the line where the two leaves meet, so a gap between them can be seen.
6. The camera reads the DOOR lamp and the CYCLE lamp on the control panel.
7. Both arms are at home with grippers open.
8. The **right arm** reaches the right leaf's handle, the vise, the vise handle knob all the way round,
   the right end of the front ledge, and Cycle Start, without reaching a joint limit.
9. The **left arm** reaches the left leaf's handle, the vise, the vise handle knob all the way round, and
   the left end of the front ledge, without reaching a joint limit.
10. The two arms do not collide when one holds the block down in the vise and the other turns the vise
    handle.
11. If a place cannot be reached, park the base again by the Base positioning steps until lines 8 to 10
    hold.

### Materials checklist

1. The **CNC mock** is a practice copy of a small milling machine, standing where it is installed on its
   own stand, with the vise about level with the arms. It is not moved, not leaned on, and not pushed at
   any point. It is powered, nothing in it cuts, and its spindle stays parked high at the back.
2. The **doors** are two sliding **leaves** that meet in the middle of the front. Each leaf has an
   upright **handle** near the middle edge. The left leaf slides left and the right leaf slides right,
   each until it stops hard. At the start both leaves are shut and the **DOOR lamp** is lit.
3. The **vise** is bolted to the table in the middle of the machine, straight behind the door opening.
   The **fixed jaw** is at the back and the **moving jaw** at the front. Each jaw has a low **ledge**
   along its bottom that the part sits on. A **middle mark** is scratched on the top of the fixed jaw.
4. The **vise handle** sits on the screw at the front of the vise. It has a round **knob** at its end.
   Turned clockwise, seen from the base, it closes the vise. Turned counterclockwise, it opens it. A half
   turn opens the jaw about the thickness of a coin, enough for the part to lift straight out.
   **Unvalidated:** the jaw gap given by a half turn on the station vise.
5. The vise handle has a **click** in its hub. When the vise is tight enough, the handle clicks and gives
   a small jump. At the start the vise is tight and the handle points to the **right**, about level.
   **Unvalidated:** whether the jump can be seen from the environment camera.
6. The **finished part** is one aluminium block, about 60 mm long, 40 mm from front to back, and 30 mm
   tall, with a pocket cut in its top. It sits clamped in the vise, long side left to right, pocket up.
7. **Chips** lie on the vise and on the table round it: about twenty small, light plastic chips, some on
   the ledges and jaw faces. The **chip trough** is the channel behind the vise at the back of the table.
8. The **front ledge** is a flat shelf along the front of the machine, below the door opening, outside
   the doors. The trays and the blower cup stand on it.
9. The **stock tray** is a shallow open tray holding **one stock block**: a plain aluminium block the
   same size as the finished part, with no pocket, lying long side left to right. It stands at the
   **left** end of the front ledge in **Config L** and at the **right** end in **Config R**.
10. The **blower** is a rubber bulb about the size of a fist with a stiff nozzle. Squeezing the bulb gives
    one **puff** of air out of the nozzle. It stands nozzle up in the **blower cup**, next to the stock
    tray, on the side nearer the middle.
11. The **finished tray** is a shallow open tray, empty. It stands at the other end of the front ledge:
    the **right** end in **Config L** and the **left** end in **Config R**.
12. The **control panel** is on the right of the machine front. It has a green **Cycle Start** button, a
    yellow Feed Hold button, a red emergency stop, the DOOR lamp, and the **CYCLE lamp**. Cycle Start
    works only when both leaves are shut and the DOOR lamp is lit.
13. The floor round the machine and the base is clear.

### Workspace layout

* **CNC mock:** straight ahead of the parked base, on its stand.
  * **Doors:** two leaves meeting in the middle of the front. The left leaf slides left, the right leaf
    slides right.
  * **Door opening:** the space the leaves uncover. The grippers go in and out only here.
  * **Vise:** in the middle of the machine table, straight behind the door opening. Fixed jaw at the
    back, moving jaw at the front, handle at the front pointing right at the start.
  * **Chip trough:** behind the vise, at the back of the table.
  * **Control panel:** on the right of the machine front, right of the right leaf's open position.
* **Front ledge:** below the door opening, outside the doors.
  * **Stock end:** the left end (Config L) or the right end (Config R). The stock tray stands at the end
    and the blower cup stands beside it, nearer the middle.
  * **Finished end:** the other end. The finished tray stands here.

The stock gripper works the stock end and the vise. The part gripper works the finished end, the vise,
and the vise handle. Neither reaches across to the other end of the ledge.

### Arm assignments

* **The stock gripper owns the blower and the stock block.** It takes the blower, blows the chips to the
  back, and puts the blower back. It takes the stock block, sets it in the vise, and holds it down until
  the vise is tight. It never turns the vise handle and never touches the finished part or the finished
  tray.
* **The part gripper owns the vise handle and the finished part.** It loosens the vise, lifts the
  finished part out, and lays it in the finished tray. It closes the vise and torques the handle. It
  never touches the blower, the stock tray, or the stock block.
* **The left gripper slides the left leaf and the right gripper slides the right leaf.** The **right
  gripper** presses Cycle Start. These are the same in both configs.
* The finished part is let go only over the finished tray. The stock block is let go only once the vise
  is torqued. The blower is let go only over its cup. Never open a gripper over the door opening, the
  front ledge, or the floor while it holds something.

## Vocabulary

* **In situ:** the machine is worked where it is installed. Nothing is taken away from it, and nothing
  about the cell is moved around for the task.
* **Passive base:** the base has no drive. It is pushed by hand to its park before recording, locked
  there, and it does not move at all during the episode.
* **Config:** the side the stock tray stands on. **Config L:** stock end left, finished end right.
  **Config R:** stock end right, finished end left.
* **Stock gripper:** the gripper on the stock tray's side. Left in Config L, right in Config R.
* **Part gripper:** the gripper on the finished tray's side. Right in Config L, left in Config R.
* **CNC mock:** a practice copy of a milling machine. It looks and opens like the real one but cuts
  nothing.
* **Leaf:** one of the two sliding halves of the doors.
* **Open:** a leaf has slid all the way out to its side and stopped hard.
* **Shut:** both leaves have slid all the way in, they meet in the middle with no gap, and the DOOR lamp
  is lit.
* **Vise:** the clamp bolted to the machine table that holds the part.
* **Fixed jaw:** the back jaw of the vise. It never moves. The part is pushed against it.
* **Moving jaw:** the front jaw of the vise. The handle moves it.
* **Ledge:** the low step along the bottom of each jaw. The part sits flat on both ledges.
* **Middle mark:** the line scratched on the top of the fixed jaw. The middle of the block lines up
  with it.
* **Vise handle:** the bar on the vise screw at the front, with a **knob** at its end. The part gripper
  holds it only by the knob.
* **Half turn:** the knob goes round from pointing one side, up over the top, to pointing the other side.
* **Loosen:** turn the vise handle a half turn **counterclockwise**, from pointing right to pointing
  left.
* **Close:** turn the vise handle **clockwise**, from pointing left up over the top toward the right,
  until the moving jaw meets the block and the handle goes stiff.
* **Torque:** the last firm push on the knob, clockwise, until the handle **clicks** once and gives a
  small jump. One click, never two.
* **Finished part:** the block with the pocket cut in it. It goes in the finished tray.
* **Stock block:** the plain block with no pocket. It goes in the vise.
* **Ends:** the two short sides of a block, left and right. Blocks are held only by their ends.
* **Chips:** the small plastic bits left by the mock cut. They are blown, never picked up.
* **Blower:** the rubber bulb with a nozzle. Squeezing the bulb gives one **puff**.
* **Round:** three puffs along the gap between the jaws: one at the left end, one at the middle, one at
  the right end.
* **Clean:** no chip lies on either ledge, on either jaw face, or in the gap between the jaws. Chips on
  the table beside the vise do not count.
* **Seated:** the stock block sits flat on both ledges, its back face touches the fixed jaw all along,
  and its middle lines up with the middle mark.
* **Resting:** the thing has stopped moving and stays still for 2 seconds after the gripper opens.
* **Clear of:** not touching. A gap shows between the two things.

### Handling standard

* Hold one thing at a time in each gripper.
* Blocks are held only by their two ends, never by the top, the pocket, or the faces that touch the
  jaws.
* No gripper goes into the machine until both leaves are open. Both grippers are out of the machine
  before a leaf is closed.
* The vise handle is held only by its knob and turned in one smooth move. It is never let spin on its
  own.
* The blower always points to the back of the machine, toward the chip trough. It is never pointed at
  the doors, the ledge, the base, or the other gripper.
* No gripper touches the chips.
* The block goes into the vise only once the vise is clean.
* The stock gripper holds the block down until the handle has clicked.
* Nothing rests on the machine. No gripper, wrist, or forearm leans on the doors, the door opening, the
  front ledge, or the control panel.
* The emergency stop and Feed Hold are never touched.

## Steps

Only Steps 2, 3, and 4 depend on the config. Steps 1, 5, and 6 are the same in both.

### Step 1: Open the doors

**Goal:** both leaves are open and the door opening is clear.

#### 1.1 Slide the left leaf open

* With the **left gripper**, come to the left leaf's handle from the front and close on it across its
  two sides.
* With the **left gripper**, slide the leaf steadily to the left until it stops hard. Do not jerk it and
  do not let it slide on its own.
* With the **left gripper**, open and draw straight back off the handle.
* The **right gripper** waits clear of the doors.

**Check:** the left leaf is open, stopped hard at its left end.

#### 1.2 Slide the right leaf open

* With the **right gripper**, come to the right leaf's handle from the front and close on it across its
  two sides.
* With the **right gripper**, slide the leaf steadily to the right until it stops hard.
* With the **right gripper**, open and draw straight back off the handle.
* The **left gripper** waits clear of the doors.

**Check:** both leaves are open and the vise can be seen through the door opening. If a leaf stopped
short, the gripper on its side takes the handle again and slides it to its stop.

**Expected state:** both leaves are open, the finished part is still clamped in the vise, the vise handle
points right, and both grippers are empty and out of the machine.

### Step 2: Unload the finished part

**Goal:** the finished part lies in the finished tray and the vise is open and empty.

#### 2.1 Loosen the vise

* **IF Config L:** the **right gripper** is the part gripper. **IF Config R:** the **left gripper** is
  the part gripper.
* With the **part gripper**, reach in through the door opening and close on the vise handle **knob**.
* With the **part gripper**, **loosen** the vise: turn the knob a half turn **counterclockwise**, up over
  the top, in one smooth move, until the handle points left.
* With the **part gripper**, open and draw back off the knob.
* The **stock gripper** waits clear of the door opening.

**Check:** the handle points left and the finished part sits loose on the ledges.

#### 2.2 Lift the part out and lay it in the finished tray

* **IF Config L:** the **right gripper** carries the part to the **right** end. **IF Config R:** the
  **left gripper** carries it to the **left** end.
* With the **part gripper**, come down over the vise and close on the finished part by its two **ends**.
* With the **part gripper**, lift it **straight up** until it is clear of both jaws. Do not drag it along
  a jaw and do not tip it.
* With the **part gripper**, carry it level out through the door opening to the **finished tray**.
* With the **part gripper**, bring it down flat into the tray, pocket up, and open.
* With the **part gripper**, lift straight away.
* The **stock gripper** waits clear of the vise and the door opening.

**Check:** the finished part lies **resting** in the finished tray, pocket up. If it lies tipped, the
**part gripper** takes it by its ends again and lays it flat. A part that falls on the machine table is
taken by its ends with the **part gripper** and laid in the tray. A part that falls on the floor is left
where it is.

**Expected state:** the finished part lies in the finished tray, the vise is open and empty with chips on
it, the handle points left, and both grippers are empty and out of the machine.

### Step 3: Blow the chips off the vise

**Goal:** the vise is **clean** and the blower is back in its cup.

#### 3.1 Take the blower

* **IF Config L:** the **left gripper** is the stock gripper. **IF Config R:** the **right gripper** is
  the stock gripper.
* With the **stock gripper**, come down over the blower cup and close **lightly** on the bulb across its
  middle, with the nozzle up. Do not squeeze it yet.
* With the **stock gripper**, lift it straight up out of the cup and turn it so the nozzle points to the
  **back** of the machine.
* The **part gripper** waits clear of the door opening.

**Check:** the blower is held by its bulb, nozzle pointing to the back, and no puff has been given yet.

#### 3.2 Blow the vise clean

* With the **stock gripper**, carry the blower in through the door opening and hold it a hand's length in
  front of the moving jaw, just above the top of the jaws, nozzle pointing to the back.
* With the **stock gripper**, give one **round**: aim at the left end of the gap between the jaws and
  squeeze the bulb once, then ease off so it fills. Do the same at the middle, then at the right end.
* With the **stock gripper**, keep the nozzle pointing to the back the whole time, so the chips fly over
  the fixed jaw into the chip trough.
* Look at the ledges and the jaw faces. If they are not **clean**, with the **stock gripper** give
  another round. Give no more than three rounds. After that, give single puffs only at the spots where a
  chip still lies.
* The **part gripper** waits clear of the door opening.

**Check:** the vise is **clean**: no chip on either ledge, either jaw face, or in the gap. Never touch a
chip with a gripper.

#### 3.3 Put the blower back

* With the **stock gripper**, carry the blower back out through the door opening, turn it nozzle up, and
  bring it down into the blower cup.
* With the **stock gripper**, open and lift straight away.

**Check:** the blower stands nozzle up in its cup. If it fell over, the **stock gripper** takes it by the
bulb and stands it in the cup again.

**Expected state:** the vise is clean and open with the handle pointing left, the blower is in its cup,
and both grippers are empty and out of the machine.

### Step 4: Load the stock and tighten the vise

**Goal:** the stock block is **seated** in the vise and the handle has been **torqued** to one click.

#### 4.1 Take the stock block

* **IF Config L:** the **left gripper** is the stock gripper. **IF Config R:** the **right gripper** is
  the stock gripper.
* With the **stock gripper**, come down over the stock tray and close on the stock block by its two
  **ends**.
* With the **stock gripper**, lift it straight up out of the tray.
* The **part gripper** waits clear of the door opening.

**Check:** one stock block is held by its ends, long side left to right.

#### 4.2 Set the block in the vise

* With the **stock gripper**, carry the block level in through the door opening and hold it above the
  gap between the jaws, long side left to right.
* With the **stock gripper**, bring it **straight down** until it sits flat on both ledges.
* With the **stock gripper**, slide it back until its back face touches the **fixed jaw**, and left or
  right until its middle lines up with the **middle mark**.
* With the **stock gripper**, keep hold of the block by its ends and press down lightly. Do not open.

**Check:** the block is **seated**: flat on both ledges, touching the fixed jaw all along, middle on the
mark. If it is not, the **stock gripper** lifts it a finger's width and sets it down again.

#### 4.3 Close the vise

* **IF Config L:** the **right gripper** is the part gripper. **IF Config R:** the **left gripper** is
  the part gripper.
* With the **part gripper**, reach in through the door opening and close on the vise handle **knob**.
* With the **part gripper**, **close** the vise: turn the knob **clockwise**, up over the top toward the
  right, in one smooth move, until the moving jaw meets the block and the handle goes stiff.
* The **stock gripper** keeps holding the block down by its ends the whole time.

**Check:** the moving jaw touches the block and the handle points about right. The block has not lifted
off the ledges.

#### 4.4 Torque the handle

* With the **part gripper**, still on the knob, push it firmly **clockwise** until the handle **clicks**
  once and gives a small jump.
* With the **part gripper**, stop pushing at the first click. Do not push for a second click.
* With the **part gripper**, open and draw back off the knob and out of the machine.
* With the **stock gripper**, open, lift straight up off the block, and draw out of the machine.

**Check:** the handle has clicked once, and the block has not moved: still flat on the ledges and on the
middle mark. If the handle did not click, the **stock gripper** takes the block by its ends again and the
**part gripper** pushes the knob again until it clicks. If the block lifted or slid, the **part gripper**
loosens the vise and the load starts again at 4.2.

**Expected state:** the stock block is clamped in the vise, the handle points about right after one
click, no tool is left in the machine, and both grippers are empty and out of the machine.

### Step 5: Close the doors

**Goal:** the doors are **shut** and the DOOR lamp is lit.

#### 5.1 Slide the left leaf shut

* Check first that both grippers are empty and out of the machine, and that nothing is left inside but
  the block in the vise.
* With the **left gripper**, close on the left leaf's handle and slide the leaf steadily to the right
  until it reaches the middle. Do not slam it.
* With the **left gripper**, open and draw straight back off the handle.
* The **right gripper** waits clear of the doors.

**Check:** the left leaf stands at the middle.

#### 5.2 Slide the right leaf shut

* With the **right gripper**, close on the right leaf's handle and slide the leaf steadily to the left
  until it meets the left leaf.
* With the **right gripper**, open and draw straight back off the handle.
* The **left gripper** waits clear of the doors.

**Check:** the doors are **shut**: the leaves meet with no gap and the DOOR lamp is lit. If a gap shows or
the lamp is dark, the gripper on the short leaf's side slides it the rest of the way.

**Expected state:** the doors are shut with the block clamped inside, the DOOR lamp is lit, and both
grippers are clear of the machine.

### Step 6: Press Cycle Start

**Goal:** the machine shows its CYCLE lamp.

* With the **right gripper** closed, come to the green **Cycle Start** button from the front.
* With the **right gripper**, press it straight in until it clicks. Hold for 1 second.
* With the **right gripper**, draw straight back off the button.
* The **left gripper** waits clear of the control panel.

**Check:** the CYCLE lamp is lit. If it is not, look at the DOOR lamp. If the DOOR lamp is dark, go back to
5.2. If the DOOR lamp is lit, the **right gripper** presses Cycle Start once more.

**Expected state:** the CYCLE lamp is lit, the doors are shut, and the finished part lies in the finished
tray.

### Step 7: End the episode

**Goal:** the part change is done and both arms are safely home.

* Look once across the station: doors shut, CYCLE lamp lit, finished part in the finished tray, stock
  tray empty, blower in its cup, base still locked in place.
* With **both grippers**, return home.
* Stop recording.

**Check:** both arms are at home with grippers open.

**Expected state:** the machine is in its mock cycle with the stock block clamped inside, and both arms are
at home.

## After the episode: reset the workspace

This reset is not recorded. The base stays parked and locked through the reset, and is only pushed away
by hand once the station is set for the next episode.

1. Press Feed Hold, then reset the machine so the CYCLE lamp goes dark.
2. Open both leaves.
3. Loosen the vise and take the stock block out. Put it with the unused stock.
4. Clamp a finished part in the vise, long side left to right, pocket up, seated on the middle mark, and
   tighten the handle until it clicks, so it points right.
5. Empty the chip trough and scatter about twenty chips over the vise again, some on the ledges and jaw
   faces. Change where they lie from one episode to the next.
6. Take the finished part out of the finished tray and put it with the finished parts.
7. Put one stock block in the stock tray, long side left to right.
8. Set the stock tray and the blower cup at the stock end and the finished tray at the finished end for
   the next episode's config. Stand the blower nozzle up in its cup.
9. Shut both leaves and check the DOOR lamp is lit.
10. Check the leaves slide easily, the vise handle still clicks, and the blower still gives a puff.
11. Check the base is still square, in the middle, and locked, and push it firmly once by hand to check it
    does not roll. If it has moved, park it again by the Base positioning steps.
12. Run the Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The
visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation
label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete
it just because a rule was broken.

### Violations

**Violation: Config misaligned**

* **Visible cue:** the work does not match the config the episode is set up in: the gripper on the stock
  tray's side turns the vise handle or takes the finished part, the gripper on the finished tray's side
  takes the blower or the stock block, or an arm reaches across to the far end of the ledge.
* **SOP rule broken:** the stock-side and finished-side rules and the IF lines in Steps 2.1, 2.2, 3.1,
  4.1, and 4.3.
* **Coaching note:** look at where the stock tray is before you move. That side's gripper is the stock
  gripper for the whole episode.

**Violation: Base moved during the episode**

* **Visible cue:** the base rolls, creeps, or turns after recording starts, the doors shift in the frame,
  or an arm pushes off the machine hard enough to move the base.
* **SOP rule broken:** Base positioning, the base is parked and locked before recording and does not move
  at all during the episode.
* **Coaching note:** park it, lock it, push-test it. If the park is wrong, fix it before recording, never
  during.

**Violation: Machine leaned on or pushed**

* **Visible cue:** a gripper, wrist, or forearm rests on a leaf, the door opening, the front ledge, or the
  control panel, or an arm pushes off any of them.
* **SOP rule broken:** Steps 1 to 6, nothing rests on the machine, and the only pushes are the leaves
  being slid, the vise handle being turned, and Cycle Start being pressed.
* **Coaching note:** nothing on the machine holds an arm up. Take the weight on the arm.

**Violation: Work order broken**

* **Visible cue:** the work does not run open, unload, blow, load, tighten, close, start. For example the
  chips are blown with the finished part still in the vise, the block goes in before the chips are blown,
  or a leaf is closed before the handle is torqued.
* **SOP rule broken:** Steps 1 to 6, the order never changes.
* **Coaching note:** say the next stage out loud before you reach for anything.

**Violation: Leaf slid wrongly**

* **Visible cue:** a leaf is slid by the gripper on the other side, jerked, slammed, let slide on its own,
  pushed by its glass instead of its handle, or left short of its stop when opened.
* **SOP rule broken:** Steps 1 and 5, each gripper slides the leaf on its own side by its handle, steadily,
  all the way to its stop.
* **Coaching note:** your side, your leaf, by the handle, slow and all the way.

**Violation: Gripper in the machine with the doors not open**

* **Visible cue:** a gripper goes into the machine while a leaf is still shut or part way open, goes in
  anywhere but through the door opening, or a leaf is slid shut while a gripper is still inside.
* **SOP rule broken:** Handling standard and Steps 1 and 5.1, no gripper goes in until both leaves are
  open, and both grippers are out before a leaf is closed.
* **Coaching note:** both leaves open, then in. Both hands out, then close.

**Violation: Vise loosened wrongly**

* **Visible cue:** the handle is turned clockwise to loosen, turned more or less than a half turn, held
  anywhere but the knob, let spin on its own, or turned by the stock gripper.
* **SOP rule broken:** Step 2.1, the part gripper turns the knob a half turn counterclockwise in one
  smooth move, from pointing right to pointing left.
* **Coaching note:** knob only, counterclockwise, over the top, stop at the left.

**Violation: Finished part dragged or tipped out**

* **Visible cue:** the finished part is taken by its top, its pocket, or a jaw face instead of its ends,
  dragged along a jaw, pulled out sideways, or tipped while it is lifted.
* **SOP rule broken:** Step 2.2, close on the part by its two ends and lift it straight up until it is
  clear of both jaws.
* **Coaching note:** ends only, straight up. A dragged part is a scratched part.

**Violation: Finished part not laid in the finished tray**

* **Visible cue:** the finished part is let go over the stock tray, the ledge, the machine table, or the
  floor, dropped into the tray from high, or left tipped or pocket down.
* **SOP rule broken:** Step 2.2, carry the part to the finished tray, bring it down flat, pocket up, and
  open.
* **Coaching note:** down flat, then open. Finished parts go only in the finished tray.

**Violation: Chips blown the wrong way**

* **Visible cue:** the blower points at the doors, the ledge, the base, or the other gripper while it is
  squeezed, or chips fly out of the door opening.
* **SOP rule broken:** Step 3.2 and the Handling standard, the nozzle points to the back the whole time so
  the chips fly into the chip trough.
* **Coaching note:** nozzle to the back, always. Chips go away from you, never toward you.

**Violation: Vise loaded with chips on it**

* **Visible cue:** the stock block goes in while a chip still lies on a ledge, a jaw face, or in the gap,
  or blowing stops after one round with chips still showing.
* **SOP rule broken:** Step 3.2, give rounds until the vise is clean, then single puffs at the spots left.
* **Coaching note:** look at the ledges before you put the blower down. A chip under the block tilts the
  whole part.

**Violation: Chips touched with a gripper**

* **Visible cue:** a gripper picks up, pushes, or sweeps a chip instead of blowing it.
* **SOP rule broken:** Step 3.2, chips are blown, never touched.
* **Coaching note:** the air moves the chips. The gripper stays off them.

**Violation: Blower handled wrongly**

* **Visible cue:** the blower is squeezed hard enough to crush the bulb flat and held that way, taken by
  the nozzle, squeezed outside the machine, dropped, or not stood back nozzle up in its cup.
* **SOP rule broken:** Steps 3.1 and 3.3, hold the bulb lightly across its middle, squeeze only inside the
  machine, and stand it back nozzle up in its cup.
* **Coaching note:** light hold to carry, one squeeze to puff, back in the cup when done.

**Violation: Stock block taken wrongly**

* **Visible cue:** the stock block is taken by its top or its long faces instead of its ends, dragged out
  of the tray, turned end on, or dropped on the way.
* **SOP rule broken:** Step 4.1, close on the block by its two ends and lift it straight up.
* **Coaching note:** ends only, straight up, long side left to right.

**Violation: Stock block not seated**

* **Visible cue:** the block is tightened while it sits on one ledge only, stands off the fixed jaw, sits
  off the middle mark, or is tilted.
* **SOP rule broken:** Step 4.2, the block sits flat on both ledges, touches the fixed jaw all along, and
  lines up with the middle mark before the vise is closed.
* **Coaching note:** down, back, middle. Look at all three before the handle turns.

**Violation: Block let go before the handle clicked**

* **Visible cue:** the stock gripper opens or lifts off the block before the handle has clicked, or the
  block lifts or slides while the vise closes.
* **SOP rule broken:** Steps 4.3 and 4.4, the stock gripper holds the block down by its ends until the
  handle has clicked.
* **Coaching note:** hold it down until you see the click. Then let go.

**Violation: Vise closed wrongly**

* **Visible cue:** the handle is turned counterclockwise to close, held anywhere but the knob, let spin,
  turned in jerks, or turned by the stock gripper.
* **SOP rule broken:** Step 4.3, the part gripper turns the knob clockwise, over the top, in one smooth
  move until the jaw meets the block.
* **Coaching note:** knob only, clockwise, over the top, stop when it goes stiff.

**Violation: Handle not torqued or torqued twice**

* **Visible cue:** the episode goes on without a click, the knob is pushed on past the first click to a
  second, or the handle is hit or knocked instead of pushed.
* **SOP rule broken:** Step 4.4, push the knob firmly clockwise until the handle clicks once, and stop at
  the first click.
* **Coaching note:** one firm push, one click, stop.

**Violation: Something left in the machine**

* **Visible cue:** the doors are closed with the blower, the finished part, or anything but the clamped
  stock block inside the machine.
* **SOP rule broken:** Step 5.1, check nothing is left inside but the block in the vise before a leaf is
  closed.
* **Coaching note:** look in before you close. Only the block stays inside.

**Violation: Doors not shut**

* **Visible cue:** the episode goes on with a gap between the leaves or the DOOR lamp dark, or the leaves
  are closed in the wrong order.
* **SOP rule broken:** Step 5, slide the left leaf to the middle, then the right leaf to meet it, and check
  the DOOR lamp is lit.
* **Coaching note:** left, then right, then look at the lamp.

**Violation: Cycle Start pressed wrongly or not pressed**

* **Visible cue:** Cycle Start is pressed before the doors are shut, pressed by the left gripper, pressed
  at an angle or hit, pressed more than twice, or never pressed, or Feed Hold or the emergency stop is
  touched.
* **SOP rule broken:** Step 6, the right gripper presses Cycle Start straight in once the DOOR lamp is lit,
  holds for 1 second, and presses once more only if the CYCLE lamp stays dark.
* **Coaching note:** DOOR lamp first, then one straight press on the green button.

**Violation: Idle gripper in the way**

* **Visible cue:** the gripper not working hangs in the door opening or over the vise while the other
  gripper works there, is in the machine while the blower is squeezed, or the two grippers touch.
* **SOP rule broken:** Steps 1 to 6, the gripper not named in a bullet waits clear of the work.
* **Coaching note:** if your hand is not working, it is out of the way.

**Violation: Correction made without looking at the check**

* **Visible cue:** a step's check is skipped: the episode moves on with a leaf short of its stop, the
  finished part tipped in the tray, chips on a ledge, the block off the middle mark, no click, or a gap
  between the leaves, and nothing is fixed.
* **SOP rule broken:** Steps 1 to 6, each check is looked at before the next stage begins, and a bad
  result is fixed the way the step says.
* **Coaching note:** look at it before you reach for the next thing. Fix it now, not at the end.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with the doors open, the CYCLE lamp dark, the finished part still in
  the machine, the stock block still in the stock tray, or an arm away from home.
* **SOP rule broken:** Step 7, look once across the station, return both arms home, then stop recording.
* **Coaching note:** one look, then home. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode,
and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake that lets go on its own, or a wheel that sticks so the base cannot be parked
  straight.
* **Bad object:** a stock block or finished part with a burr or a bent end, a blower with a split bulb or
  a blocked nozzle, or chips stuck to the vise.
* **Machine fault:** a leaf that sticks or jumps its track, a DOOR lamp that stays dark with the leaves
  shut, a vise handle that does not click, or a CYCLE lamp that stays dark after a correct press with the
  DOOR lamp lit.

## Annotation subtasks (from SOP)

1. Slide the left leaf open
2. Slide the right leaf open
3. Loosen the vise
4. Lift the finished part out and lay it in the finished tray
5. Take the blower
6. Blow the vise clean
7. Put the blower back
8. Take the stock block
9. Set the block in the vise
10. Close the vise
11. Torque the handle
12. Slide the left leaf shut
13. Slide the right leaf shut
14. Press Cycle Start
15. Return both arms home and end the episode
