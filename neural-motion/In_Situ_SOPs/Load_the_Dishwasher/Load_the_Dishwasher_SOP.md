# Load the Dishwasher SOP (1x Load, in situ)

One episode loads one empty dishwasher where it is installed and starts it. The base is **passive**:
it has no drive of its own, so it is pushed by hand up to the dishwasher and locked there, and
nothing is carried away to a table. Everything the episode touches is already at the machine when
recording starts: the empty dishwasher with its door open and the washed items standing on the
draining board beside it.

The dishwasher is worked **as found**. The door already hangs open and flat when recording starts,
both racks are pushed in, and the twelve items stand on the draining board where they were left:
two plates on edge in the plate rack, two bowls and two cups upside down, and six utensils standing
handle up in the utensil cup.

**This is an in-situ task, and three things follow from that.** First, the machine is built in under a
counter, so **nothing is loaded until its rack is drawn fully out past the counter edge**. No gripper
reaches in under the counter, and no item is lowered into a rack that is still under it. Second, **the
dishwasher is never leaned on and never pushed**: no gripper, wrist, or forearm rests on the door, a
rack rail, or the cabinet front, and no push is ever hard enough to move the machine. Third, **nothing
is turned over**: every item stands on the draining board in the pose it will be racked in, and it is
lifted straight up, carried level, and lowered straight down into its place.

The order never changes: **lower rack, then the cutlery basket, then the upper rack, then close,
latch, and start.** The upper rack is only drawn out after the lower one is pushed in,
because an upper rack that is out sits over the lower one and blocks it.

The station is set up in one of two ways. Only the **draining board** (the basin holding the dishes)
moves. The dishwasher, its racks, the cutlery basket, and the sink are the same in both.

* **Config L:** the draining board stands on the counter immediately **left** of the machine.
* **Config R:** the draining board stands on the counter immediately **right** of the machine.


One config per episode, chosen before recording and never changed mid-episode. Where a step depends on
the setup it says so on an **IF** line. Look at the counter and follow the line that matches.

What stays constant across all sessions:

* **Board-side rule:** the gripper on the draining board's side does all the item work: every plate,
  bowl, utensil, and cup off the draining board. It is called the **item gripper**: the **left gripper**
  in Config L and the **right gripper** in Config R.
* **Machine rule:** the other gripper works the machine: the rack rails, the door, and the Start button.
  It is called the **machine gripper**: the **right gripper** in Config L and the **left gripper** in
  Config R. It takes each rack rail at **its own end** of the rack.

* Roles never swap mid-episode, nothing is handed over, and neither gripper does the other's work.

The machine is powered but its water supply is shut off, so the cycle runs dry and the items go in
clean and dry. The cycle is cancelled during the reset.

## Setup

Complete the base positioning and all the checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never
steered, nudged, or repositioned once recording starts. It is parked once, before recording, and does
not move again until the episode is over.

1. Push the base by hand up to the dishwasher and stop it **square to the front of the machine**, so
   the front edge of the open door runs straight across the frame and neither end of it sits nearer
   than the other.
2. Stop it **centered on the door mouth**, so the left end and the right end of the racks are the same
   distance out from the middle of the base.
3. Stop it **far enough back** that a rack drawn fully out, and the door on its way up, both swing
   clear of the base and of both arms.
4. Stop it **close enough** that the **item gripper** reaches the back of each rack when that rack is
   fully out, without the arm extending.
5. Check the **height band**: with the base parked, the **item gripper** comes down onto a fully out
   rack from above and reaches the floor of the lower rack, the cutlery basket, and the bed of the
   upper rack, all without the wrist or forearm fouling the counter edge above.
6. Check the **draining board**: the **item gripper** reaches every item on the draining board, lifts
   each straight up without extending, and carries it to the racks without passing over the sink.
7. Check the **door swing**: the **machine gripper** reaches the door handle with the door open and flat,
   and can carry the door through its whole swing up to shut without extending and without the arm
   fouling the counter or the cabinet.
8. Check the **panel**: with the door shut, the **machine gripper** reaches the Start button on the front
   of the door, and the panel light is in the camera frame.
9. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
10. If any of lines 1 to 8 fails, push the base to a new park by hand and start again at line 1. Do
    not work a dishwasher the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the
machine or the counter hard enough to shift it, nothing and nobody touches it, and it is never
repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the door mouth and its frame includes    the open door, both
   racks pushed in and fully out, the draining board beside the machine, and the front of the door
   once it is shut.
3. The camera reads a fully out rack from above, so which slot a plate stands in, which way up a bowl
   or cup sits, and which compartment a utensil stands in are all readable.
4. The camera reads the door front once it is shut, so the gap along the door edge and the panel light
   are readable.
5. Both arms are at home with grippers open.
6. The **item arm** reaches every item on the draining board, the whole floor of the
   lower rack, the cutlery basket, and the whole bed of the upper rack, without extending to a joint
   limit. It reaches neither a rack rail nor the door.
7. The **machine arm** reaches both rack rails at its own end, the door handle, and the Start button,
   without extending to a joint limit. It reaches nothing on the draining board.
8. The **item gripper** comes down onto a fully out rack straight from above, and never reaches in
   under the counter edge toward a rack that is still in.
9. The two arms do not collide, and a rack drawn fully out is clear of the machine arm's path to the door
    handle.
10. If a place cannot be reached, re-park the base by the Base positioning steps until lines 6 to 9
    hold.

### Materials checklist

1. The **dishwasher** stands where it is installed, built in under the counter. It is not moved, not
   leaned on, and not pushed at any point.
2. The **door** is hinged at the bottom. At the start of the episode it hangs open and flat, inside
   face up, and stays there on its own without being held.
3. The door shuts with a latch that clicks. A correctly shut door sits flat against the cabinet with
   no gap along its edge and does not spring back open.
4. The **control panel** is on the front face of the door, below the handle, so it faces the arms once
   the door is shut. It carries the **Start** button and the panel light.
5. Both racks are **pushed fully in** and **empty**, and both roll out to a stop and back on their
   runners without being lifted.
6. A rack drawn fully out stands clear past the counter edge along its whole length, so the whole rack
   is loaded from above with nothing overhead.
7. The **cutlery basket** is clipped to the front rail of the lower rack at its right end. Its three
   compartments, marked forks, knives, spoons, are all empty.
8. The **draining board** is on the counter immediately **left** of the machine in **Config L** and
   immediately **right** of it in **Config R**, within reach of the item arm, and does not slide when an item is lifted off it. It holds the twelve items:
   * two plates standing on edge in its plate rack,
   * two bowls upside down, side by side and not nested,
   * two cups upside down, side by side, handles clear,
   * six utensils standing handle up in the utensil cup: two forks, two knives, two spoons.
9. The six utensils stand mixed in the utensil cup, not sorted by type, and none crosses or leans on
    another. Vary which utensil stands where between episodes.
10. Every item is clean, dry, and undamaged. No plate is chipped, no cup is cracked, and no tine is
    bent or missing.
11. The sink is empty and the tap is off, and nothing is carried over the sink at any point.
12. The floor in front of the machine is clear and dry, so nothing that is dropped rolls under the
    base.

### Workspace layout

* **Dishwasher:** built in under the counter, straight ahead of the parked base.
  * **Lower rack:** rolls out toward the arms, over the open door, to a stop past the counter edge. It
    has the **plate slots** across its back, the **bowl area** across its front left, and the
    **cutlery basket** clipped to the front rail at its right end.
  * **Upper rack:** rolls out over the lower rack, to a stop past the counter edge. It is one open bed
    of tines and holds the two cups.
    * **Door:** hanging open and flat, inside face up, carrying on its front face the **door handle**
    and the **control panel**.
* **Draining board:** on the counter immediately left (Config L) or right (Config R) of the machine,
  within reach of the item arm.
  It holds the plate rack, the bowls, the cups, and the utensil cup.

* **Sink:** beyond the draining board. Nothing is carried over it and no gripper goes near it.

The item arm works the draining board and the racks in front of the machine. The machine arm works the
machine itself and stays on its own side of it.

### Arm assignments

* **The item gripper owns the items.** It lifts every plate, bowl, utensil, and cup off the draining
  board, carries it, and lowers it into its place in a rack or the basket. It never touches a rack rail, the door, or the
  control panel.
* **The machine gripper owns the machine.** It draws each rack out and pushes it back in, holds the rack
  still while the item gripper loads it, swings the door up and latches it, and presses Start. It never
  picks up an item.
* **The machine gripper holds the rack still the whole time that rack is being loaded.** It takes the rack
  rail at its own end of the rack and keeps its hold until the rack is full.
* An item is released only into its place in a rack or in a basket compartment.
  Never open a gripper over open space, over the open door, over the counter, or over the sink.

## Vocabulary

* **In situ:** the machine is worked where it is installed. Nothing is taken out of the kitchen to a
  table, and nothing about the kitchen is rearranged for the task.
* **Passive base:** the base has no drive. It is pushed by hand to its park before recording, locked
  there, and it does not move at all during the episode.
* **Tines:** the rows of upright pegs standing in a rack.
* **Slot:** the gap between two neighbouring tines in the lower rack, wide enough for one plate
  standing on edge.
* **Plate slots:** the row of slots across the back of the lower rack, where the plates stand.
* **Bowl area:** the open stretch of tines across the front left of the lower rack, where the bowls go
  face down.
* **Rack rail:** the bar across the front of a rack. The machine gripper takes the rail to roll the rack
  and to hold it still.
* **Fully out:** the rack has been drawn forward until it stops, and its whole length stands past the
  counter edge with nothing overhead.
* **Fully in:** the rack has been pushed back until it stops and its rail is level with the front of
  the cabinet.
* **Cutlery basket:** the open box clipped to the front rail of the lower rack. It has three
  compartments in a row, one per type, marked forks, knives, spoons.
* **Head down, handle up:** how every utensil sits in the basket, with the eating end pointing down into
  the compartment, the handle standing above the rim.
* **Utensil cup:** the open pot on the draining board where the six utensils stand handle up.
* **Plate rack:** the slotted part of the draining board that keeps the two plates standing on edge.

* **Latched:** the door is up flat against the cabinet and the latch has clicked. A door that rests
  shut without a click is not latched.
* **Running:** the panel light is on and the machine hums.
* **Seated:** the item is resting down on the tines or on the floor of a compartment, and it stays
  still for 2 seconds after the item gripper opens. A seated item does not rock or lean on a
  neighbour.
* **Clear of:** not touching. Two racked items are clear of each other when a gap shows between them.

### Handling standard

* Move exactly one item at a time.
* Nothing is turned over. Every item is racked in the pose it stood in on the draining board.
* Load only a rack that is **fully out**. No gripper reaches in under the counter, and nothing is
  lowered into a rack that is still under it.
* Lift every item straight up, carry it level, and lower it straight down. Never swing an item over a
  rack that is already loaded, and never carry anything over the sink.
* Lower each item until it is resting, then release. Never drop an item in from above.
* Nothing is slid or dragged. If an item lands badly, the item gripper lifts it straight out and
  lowers it again rather than nudging it into place.
* If the item due next is crossed or covered by another, the item gripper lifts the covering item
  straight up, sets it clear on the draining board, and then takes the item that was due.
* Load each rack fully before the machine gripper pushes it in. Once a rack is in, nothing is added to it.
* Nothing rests on the machine. No gripper, wrist, or forearm leans on the door, a rack rail, or the
  cabinet front, and no push is ever hard enough to move the machine.

## Steps

Only the gripper names in 1.1 and 1.2 and the cup halves in 4.3 depend on the config. Every other
step is the same in both.

### Step 1: Draw the lower rack out and stand both plates in it

**Goal:** the lower rack is fully out past the counter edge and both plates stand on edge, one per
slot.

#### 1.1 Draw the lower rack out

* **IF Config L:** the **right gripper** is the machine gripper and takes the rail at the
  right end.
  **IF Config R:** the **left gripper** is the machine gripper and takes the rail at the left end.
* The **machine gripper** takes the rack rail of the lower rack at its own end and draws the rack
  straight forward, over the open door, until it is **fully out**.
* Draw it level and in one movement. If it catches on its runners, push it back and draw it again.
  Never lift a rack to free it.
* The **machine gripper** keeps its hold on the rail and holds the rack still.

**Check:** the whole rack stands past the counter edge with nothing overhead, and the rack is still.
If any part of it is still under the counter, the **machine gripper** draws it forward again.

#### 1.2 Stand each plate in its own slot

Work one plate at a time. Take the plate at the front of the plate rack first.

* **IF Config L:** the **left gripper** is the item gripper. **IF Config R:** the **right gripper** is the
  item gripper.
* The **item gripper** takes the plate by the rim edge standing above the plate rack, lifts it
  straight up out of the draining board, and carries it level to the **plate slots**, keeping it on
  edge.
* Come down onto the rack from above and lower the plate straight into an empty slot until it is
  resting on the floor of the rack, then release.
* Both plates face the same way, toward the front of the rack, and each one has its own slot.
* Repeat for the second plate, into the next empty slot.

**Check:** both plates stand on edge, one per slot, facing the same way, and neither leans on the
other or on a tine. If a plate leans or rocks, the **item gripper** lifts it straight out and lowers
it into the slot again. Do not push it upright.

**Expected state:** the lower rack is fully out with the **machine gripper** still on its rail, two plates
stand in the plate slots, and the bowl area, the basket, and the upper rack are all empty.

### Step 2: Rack the two bowls face down

**Goal:** both bowls sit upside down over the tines in the bowl area, clear of each other and of the
plates.

* The **machine gripper** keeps its hold on the rack rail throughout.
* Work one bowl at a time. Take the bowl nearer the front of the draining board first.
* The **item gripper** takes the bowl by any free stretch of its rim, lifts it straight up off the
  draining board, and carries it level to the **bowl area**, still upside down.
* Lower it straight down over the tines until it is resting, then release.
* The second bowl goes beside the first, not on it and not over it.

**Check:** both bowls are upside down and seated over the tines, clear of each other and clear of the
plates. If a bowl perches on a tine, rocks, or touches a plate, the **item gripper** lifts it straight
up and lowers it again.

**Expected state:** the lower rack is still fully out, two plates stand in the slots, two bowls sit face
down in the bowl area, and the cutlery basket is still empty.

### Step 3: Fill the cutlery basket by type

**Goal:** all six utensils stand head down in the basket, one type per compartment.

* The **machine gripper** keeps its hold on the rack rail throughout.
* Work one utensil at a time, in **type order: both forks, then both knives, then both spoons**,
  whichever way they happen to stand in the utensil cup. Within a type, take the one nearer the front
  of the cup first.
* If the utensil due next is crossed by another, the **item gripper** lifts the covering utensil
  straight up, stands it clear on the draining board, and then takes the one that was due.
* The **item gripper** takes the utensil by its handle above the rim of the utensil cup, lifts it
  straight up, and carries it upright to the basket.
* Lower it straight down into the compartment for its type until the head is resting on the floor of
  the compartment, then release. It stands **head down, handle up**.
* Never drag a utensil sideways out of the cup, and never carry two at once.

**Check:** six utensils stand in the basket, two per compartment, each head down with its handle above
the rim, forks in the fork compartment, knives in the knife compartment, spoons in the spoon
compartment. No utensil lies across the basket, leans out of it, or sits in a compartment for another
type. If one is in the wrong compartment, the **item gripper** lifts it straight up and lowers it into
the right one.

**Expected state:** the lower rack is full, with two plates, two bowls, and six utensils, and still fully out.
The draining board now holds only the two cups.

### Step 4: Close the lower rack, draw the upper rack out, and rack both cups

**Goal:** the lower rack is fully in, and both cups sit upside down on the upper rack, which is then
pushed fully in.

#### 4.1 Push the lower rack in

* The **machine gripper**, still on the rack rail, pushes the lower rack straight back until it is **fully
  in**, then releases and comes clear.
* Push it in level and in one movement. If it catches, draw it forward again, straighten it, and push
  it in again. Never force it.

#### 4.2 Draw the upper rack out

* The **machine gripper** takes the rack rail of the upper rack at its own end and draws it straight
  forward until it is **fully out**.
* The **machine gripper** keeps its hold on the rail and holds the rack still.

**Check:** the whole upper rack stands past the counter edge with nothing overhead, and the lower rack
is fully in beneath it.

#### 4.3 Rack the two cups upside down

* Work one cup at a time. Take the cup nearer the front of the draining board first.
* The **item gripper** grips the cup around its body, lifts it straight up off the draining board, and
  carries it level to the **upper rack**, still upside down.
* **IF Config L:** the first cup goes on the **left half** of the upper rack and the second on the
  **right half**. **IF Config R:** the first cup goes on the **right half** and the second on the
  **left half**.
* With the **item gripper**, come down onto the rack from above and lower the first cup straight over
  the tines on its half until it is resting, then release.
* With the **item gripper**, lower the second cup the same way on the other half, clear of the first.
* Neither cup goes down over another cup, and neither is set on the rack rail or on the edge of the
  rack.

**Check:** both cups are upside down and seated over the tines, one on each half of the upper rack,
clear of each other. If a cup rocks or perches on a tine, the **item gripper** lifts it straight up and
lowers it again.

#### 4.4 Push the upper rack in

* The **machine gripper**, still on the rail, pushes the upper rack straight back until it is **fully in**,
  then releases and comes clear.

**Expected state:** both racks are fully in and loaded, the door still hangs open and flat, and the
draining board is empty.

### Step 5: Close the door, latch it, and start the cycle

**Goal:** the door is latched and the machine is running.

#### 5.1 Swing the door up and latch it

* The **machine gripper** takes the **door handle** on the edge of the door nearest the arms.
* Swing the door up and back in one movement until it is flat against the cabinet.
* Press the door flat with the gripper closed until the **latch clicks**.
* If the door meets anything on the way up, lower it flat again, find what is sticking out of a rack or
  lying on the door, and put it right before closing again. Never force the door.

**Check:** the door sits flat against the cabinet with no gap along its edge, and the latch has clicked.
If it has not clicked, the **machine gripper** presses the door face once more. If it still does not catch,
lower the door and close it again.

#### 5.2 Press Start

* The **machine gripper** presses the **Start** button on the control panel with the gripper closed, then
  comes clear of the door.
* Watch for the panel light coming on and the machine starting to hum.
* If nothing happens, the **machine gripper** presses Start once more. If the machine still does not run,
  end the episode and log it as a machine fault.

**Check:** the panel light is on and the machine is running.

**Expected state:** the door is latched, the machine is running, the draining board is empty, and both
arms are clear of the machine.

### Step 6: End the episode

**Goal:** the load is complete, the machine is running, and both arms are safely home.

* Confirm the draining board is empty and nothing was left on the counter or on the
  door.
* Confirm the door is latched flat against the cabinet with no gap along its edge, and the panel light
  is on.
* Confirm the base has not moved: it is still square to the machine and still locked.
* Return both arms home, then stop recording.

## After the episode: reset the workspace

This reset is not recorded. The base stays parked and locked through the reset, and is only pushed away
by hand once the station is set for the next episode.

1. Press Cancel on the control panel and wait for the panel light to go out.
2. Unlatch the door by the handle and lower it open and flat, inside face up.
3. Draw the upper rack out, take both cups off it, and stand them upside down side by side on the
   draining board. Push the rack fully in.
4. Draw the lower rack out and empty it: the six utensils back into the utensil cup standing handle up,
   the two bowls upside down side by side on the draining board, and the two plates back on edge in the
   plate rack.
5. Mix the utensils in the cup so they are not sorted by type, and stand them so none crosses or leans
   on another. Vary which one stands where between episodes.
6. Push the lower rack fully in and leave the door hanging open and flat.
7. Dry and wipe anything that got wet, and wipe the counter and the draining board.
8. Replace anything chipped, cracked, or bent, and any rack with a bent or missing tine.
9. Check both racks still roll out and in freely, the basket is clipped firmly to the front rail, and
    the door latch still clicks.
10. Check the base is still square, centered, and locked, and push it firmly once by hand to confirm it
    does not roll. If it has moved, park it again by the Base positioning steps.
11. Run the Setup checklists again.

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

The violations below were written against **Config R** (left gripper on the machine, right gripper on
the items). In Config L read them with the grippers swapped. They will be revised in a later pass.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the station is not set up in: the gripper away from the
  draining board takes an item, the gripper on the board's side takes a rack rail or the door, the first cup goes on the half away from the
  board, or the draining board is moved before or during the episode.
* **SOP rule broken:** Steps 1.1, 1.2, and 4.3, look at the counter, find the draining board, and follow the IF line that matches the config the episode is set up in.
* **Coaching note:** look at the board before the arm moves. One config per episode, and it never
  changes mid-episode.

**Violation: Base moved during the episode**

* **Visible cue:** the base rolls, creeps, or turns after recording starts, the door mouth shifts in the
  frame, or an arm pushes off the machine or the counter hard enough to move the base.
* **SOP rule broken:** Step 6 and the Base positioning rule it confirms, the base is parked and locked
  before recording and does not move at all during the episode.
* **Coaching note:** park it, lock it, push-test it. If the park is wrong, fix it before recording, never
  during.

**Violation: Machine leaned on or pushed**

* **Visible cue:** a gripper, wrist, or forearm rests on the door, a rack rail, or the cabinet front; an
  arm pushes off the machine; or the machine or the open door visibly shifts under a push.
* **SOP rule broken:** Steps 1 to 5, nothing rests on the machine and no push is ever hard enough to move
  it.
* **Coaching note:** the machine holds nothing up for you. Take the weight on the arm.

**Violation: Loading order broken**

* **Visible cue:** the work does not run lower rack, then cutlery basket, then upper rack, then close,
  latch, start. For example the upper rack is drawn out before the lower rack is full, or the cups go in
  before the bowls.
* **SOP rule broken:** Steps 1 to 5, the order is lower rack, cutlery basket, upper rack, close, latch,
  start.
* **Coaching note:** say the next stage out loud before you reach for anything. The order never changes.

**Violation: Rack loaded before it is fully out**

* **Visible cue:** the right gripper puts an item into a rack that is still in, or only part way out, or
  reaches in under the counter edge to place something on a rack still under it.
* **SOP rule broken:** Steps 1.1 and 4.2, the left gripper draws the rack fully out past the counter edge
  before anything is put into it, and no gripper reaches in under the counter.
* **Coaching note:** rack all the way out into the open first, then come down onto it from above.

**Violation: Item put in the wrong rack or basket**

* **Visible cue:** a plate or a bowl goes into the upper rack, a cup goes into the lower rack, or a utensil
  goes anywhere other than the cutlery basket.
* **SOP rule broken:** Steps 1.2, 2, 3, and 4.3, plates and bowls in the lower rack, utensils in the cutlery
  basket, cups in the upper rack.
* **Coaching note:** flat things low, cups high, cutlery in the basket. Every time.

**Violation: Plates not standing one per slot**

* **Visible cue:** a plate lies flat in the rack, leans across the tines, shares a slot with the other plate,
  or the two plates face opposite ways.
* **SOP rule broken:** Step 1.2, both plates stand on edge, one per slot, facing the same way toward the
  front of the rack.
* **Coaching note:** one plate, one slot, both facing the same way.

**Violation: Bowl racked the wrong way up**

* **Visible cue:** a bowl goes in open side up, or on its side, instead of upside down over the tines.
* **SOP rule broken:** Step 2, both bowls go in upside down over the tines in the bowl area.
* **Coaching note:** the bowl is already upside down on the draining board and stays that way. Nothing is
  turned over.

**Violation: Racked items touching or stacked on each other**

* **Visible cue:** a bowl rests on a plate or on the other bowl, a cup rests on the other cup, or two items
  lean together instead of showing a gap.
* **SOP rule broken:** Steps 2 and 4.3, each bowl and each cup is seated clear of the others.
* **Coaching note:** leave a gap you can see. Nothing stacks in a rack.

**Violation: Cup not seated mouth down**

* **Visible cue:** a cup stands the right way up on the upper rack, sits on the rack rail or the rack edge, or
  is perched on a tine and rocking when the right gripper opens.
* **SOP rule broken:** Step 4.3, both cups go upside down over the tines, one on each half of the upper rack,
  and are seated before release.
* **Coaching note:** lower it until it stops moving, then let go.

**Violation: Cutlery taken out of type order**

* **Visible cue:** the utensils leave the utensil cup in an order other than both forks, then both knives,
  then both spoons, such as whatever stands nearest being taken first.
* **SOP rule broken:** Step 3, work in type order, forks, then knives, then spoons, and within a type take the
  one nearer the front of the cup first.
* **Coaching note:** the cup is mixed differently every episode; the order is not.

**Violation: Utensil in the wrong compartment**

* **Visible cue:** a fork stands in the knife or spoon compartment, two types share one compartment, or one
  compartment is left empty while another holds three.
* **SOP rule broken:** Step 3, one type per compartment, two utensils in each of forks, knives, and spoons.
* **Coaching note:** read the compartment before you lower the utensil, not after.

**Violation: Utensil not standing head down**

* **Visible cue:** a utensil goes into the basket handle first, lies flat across the top of the basket, hangs
  over the rim, or leans out of its compartment.
* **SOP rule broken:** Step 3, each utensil stands head down with its handle above the rim of its compartment.
* **Coaching note:** take it by the handle, keep it upright, lower it straight in.

**Violation: Utensil dragged or pulled from under another**

* **Visible cue:** a utensil is pulled sideways out of the utensil cup, or tugged free from under one crossing
  it, instead of the covering utensil being lifted straight up and stood clear first.
* **SOP rule broken:** Step 3, lift the covering utensil straight up, stand it clear on the draining board, then
  take the one that was due.
* **Coaching note:** uncover it, then lift it straight up. Never tug.

**Violation: Rack not held still while it is loaded**

* **Visible cue:** the left gripper lets go of the rack rail during Steps 1 to 3 or 4.3, or the rack rolls,
  shifts, or runs back in while the right gripper is putting an item in.
* **SOP rule broken:** Steps 1 to 4, the left gripper holds the rack rail the whole time that rack is being
  loaded.
* **Coaching note:** the left hand stays on the rail until the rack is full.

**Violation: Rack pushed in early or left part way out**

* **Visible cue:** a rack is pushed in with items still on the draining board that belong in it, something is
  added to a rack after it was pushed in, or a rack is left standing part way out at the end of its step.
* **SOP rule broken:** Steps 4.1 and 4.4, load each rack fully, then push it fully in, and add nothing to a rack
  that is in.
* **Coaching note:** full first, then all the way in, once.

**Violation: Item dropped in or dragged instead of lowered**

* **Visible cue:** the right gripper opens above a rack and the item falls the last stretch, or an item is slid
  or nudged across the tines or along a slot into place instead of being lifted out and lowered again.
* **SOP rule broken:** Steps 1 to 4, lower every item until it is resting, then release, and correct a bad
  placement by lifting it straight out and lowering it again.
* **Coaching note:** all the way down, then open. Never nudge a racked item.

**Violation: Door closed on an item or on a rack that is out**

* **Visible cue:** the door swings up against a rack that is still out, against a cup, plate, or utensil standing
  proud of a rack, or the door is forced against something in the way.
* **SOP rule broken:** Step 5.1, both racks are fully in before the door is closed, and a door that meets anything
  is lowered flat and the obstruction put right.
* **Coaching note:** if the door stops, put it back down. Never push through.

**Violation: Latch not confirmed**

* **Visible cue:** the door is left resting shut with a gap along its edge, or the episode moves on to Start with
  no press of the door and no click.
* **SOP rule broken:** Step 5.1, press the door flat until the latch clicks and there is no gap along its edge.
* **Coaching note:** a shut door is not a latched door. Press until it clicks.

**Violation: Start pressed at the wrong time or not confirmed**

* **Visible cue:** Start is pressed while the door is still open or unlatched, Start is never pressed, or the
  episode ends with a dark panel and a silent machine.
* **SOP rule broken:** Step 5.2, press Start after the door is latched and watch for the panel light and the hum.
* **Coaching note:** latch, press, then look at the panel before you move away.

**Violation: Wrong arm used**

* **Visible cue:** the left gripper picks up an item, or the right gripper takes a rack rail, the door handle,
  or the Start button.
* **SOP rule broken:** Steps 1 to 5, the right gripper handles the items, the left gripper handles the racks, the
  door, and the panel.
* **Coaching note:** right arm carries, left arm works the machine.

**Violation: Item dropped, knocked over, or carried the wrong way**

* **Visible cue:** an item falls off the draining board, out of a rack, onto the open door, or onto the floor; the
  right gripper knocks a racked item over while putting the next one in; or an item is carried across the sink
  or swung over a rack that is already loaded.
* **SOP rule broken:** Steps 1 to 4, lift straight up, carry level to its own place, never over the sink and never
  over a loaded rack, and lower straight down clear of what is already racked.
* **Coaching note:** plan the path before the lift. Carry high and level, come down straight, and stay clear of
  what is already in.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with an item still on the draining board, the door unlatched, the panel dark,
  or an arm away from home.
* **SOP rule broken:** Step 6 (confirm the empty draining board, the latched door, the panel light, and the locked
  base; return both arms home; then stop recording).
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never
use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake that releases on its own, or a caster that seizes so the base cannot be parked square.
  Fix it before the next episode.
* **Defective object:** a chipped plate, a cracked cup, a bent or missing tine, or a basket that comes unclipped. Replace it before the next episode.
* **Machine fault:** a rack that jams on its runners, a latch that will not catch after a correct press, or a
  machine that does not run after Start was pressed twice on a latched
  door.

## Annotation subtasks (from SOP)

1. Draw the lower rack fully out past the counter edge
2. Stand one plate on edge in a plate slot
3. Rack one bowl face down in the bowl area
4. Lift one covering utensil clear in the utensil cup
5. Stand one utensil head down in its compartment in the cutlery basket
6. Push the lower rack fully in
7. Draw the upper rack fully out past the counter edge
8. Rack one cup upside down on the upper rack
9. Push the upper rack fully in
10. Swing the door up and latch it
11. Press Start and confirm the machine is running
12. Return both arms home and end the episode
