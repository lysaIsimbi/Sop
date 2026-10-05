# Pick at a Goods-to-Person Port SOP (1x Episode: three presented totes, in situ)

One episode works three source totes at a goods-to-person port, at the port where they are presented. The base is **passive**: it
has no drive of its own, so it is pushed by hand to the front of the port and locked there, and nothing is carried away to a table.
Everything the episode touches is already at the port when recording starts: the first source tote in the port window, the four
order totes in their slots, and the panel.

The episode runs these four actions for each presented tote, in this order and no other: **pick the counted units from the presented
tote to the order slot, confirm on the panel, release the tote, take the next.** The port brings the stock to the arms: the source
totes come to the window one at a time, and the arms never go looking for stock.

The port is worked **as found**. The first **source tote** stands in the **port window**, held by the port against its stop. Two more
wait inside the port, out of reach. Each source tote holds six units of one SKU. The **panel** shows how many units to pick from the
presented tote, and a **slot light** shows which order slot they go to. The episode ends when the third tote has been released and the
panel shows **DONE**, with each order slot holding exactly the units the panel asked for, and every light off.

**The panel and the slot light decide the pick.** Before each pick, the panel shows **PICK** and a number, 1, 2, or 3, and one slot light
is lit. That number, and that slot, are the only ones that count. They change from tote to tote and from episode to episode, so the panel
is read every time and never worked from memory. Each tote's pick goes to a different slot.

**This is an in-situ task, and three things follow from that.** First, **the window moves totes**: when a tote is released it rolls away
and the next one rolls in, so **no gripper is ever in the window while a tote is moving**, and nothing reaches into the port past the
window. Second, the **port, the panel, and the slot ledges are never leaned on and never pushed**: no gripper, wrist, or forearm rests on
the window frame, the port top, a ledge, an order tote, or the panel stand. Third, **each unit goes from the presented tote to the lit
slot and nowhere else**: nothing is set down on the port top, the window frame, another slot, or the floor on the way.

The port is set up in one of two ways. Only the **panel** moves. The window, the order slots, and their lights are in the same place in
both.

* **Config L:** the panel stands at the **left end** of the port front, beyond slot S1.
* **Config R:** the panel stands at the **right end** of the port front, beyond slot S4.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says so on an **IF**
line. Look at the port and follow the line that matches. Which slot is lit and how many units to pick change per tote, but they are not a
config: the panel shows them.

What stays constant across all sessions:

* **Slot-side rule:** the **left gripper** picks for the **left slots** (S1, S2) and the **right gripper** for the **right slots** (S3, S4).
  Both grippers reach the whole window, so no unit is ever handed over.
* **Panel-side rule:** the gripper on the panel's side presses every panel button. That is the **left gripper** in Config L and the **right
  gripper** in Config R. It is called the **panel gripper**.
* **Clear-window rule:** before any release, both grippers are drawn up out of the window and **clear of the port**, and neither goes back
  in until the next tote has stopped and the panel shows its pick.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches over, under, around, or
past the other. Nothing is moved two at a time: one gripper holds one unit, and the other gripper is empty and clear of the window.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or repositioned once
recording starts. It is parked once, before recording, and does not move again until the episode is over.

1. Push the base by hand up to the port and stop it **square to its front**, so the port top runs straight across the frame of the camera.
2. Stop it **centered on the window**, so the middle of the base is in line with the middle of the presented tote.
3. Stop it **close enough** that both grippers reach the far corners of the presented tote from above without either arm extending, and **far
   enough** that neither arm, wrist, nor any part of the base touches the port front, a ledge, or the panel stand while both arms work.
4. Check the **left side**: the **left gripper** reaches the whole presented tote, the floor of S1 and S2, all without extending.
5. Check the **right side**: the **right gripper** reaches the whole presented tote, the floor of S3 and S4, all without extending.
6. Check the **panel** for the config this episode runs: the **panel gripper** reaches the CONFIRM and RELEASE buttons straight on.
7. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
8. If any of lines 1 to 6 fails, push the base to a new park by hand and start again at line 1. Do not work a port the arms cannot reach
   comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the port hard enough to shift it, nothing
touches it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the window and its frame includes the whole window and the presented tote, all four order slots
   with their lights, and the panel with its display and buttons.
3. The camera reads the **panel display** and sees which **slot light** and which **panel button** is lit at every moment.
4. The camera sees into the presented tote and every order tote well enough to count the units in them.
5. The camera sees the window edges, so a gripper inside the window while a tote moves is readable.
6. Both arms are at home with grippers open.
7. The **left arm** reaches the whole window and S1 and S2 without extending to a joint limit.
8. The **right arm** reaches the whole window and S3 and S4 without extending to a joint limit.
9. The panel arm for this config reaches both panel buttons without extending to a joint limit.
10. Neither gripper touches the window frame on the way into or out of the presented tote.
11. The two arms do not collide, and neither arm passes in front of the other.
12. If a place cannot be reached, re-park the base by the Base positioning steps until lines 7 to 11 hold.

### Materials checklist

1. The **port** stands where it lives, fixed to the floor. It is not moved, not leaned on, and not pushed at any point.
2. Its **top** is a flat deck at about waist height with the **window**, an opening a little larger than one tote, in the middle. Nothing is
   above the window.
3. A tote in the window is the **presented tote**. It stands on a short roller lane inside the port, held against a **stop** at its far end.
   The **source totes** waiting behind it are inside the port, below the top and out of reach.
4. When the RELEASE button is pressed, the stop drops, the presented tote rolls away inside the port, and the next source tote rolls into
   the window against the stop, which rises again (**unvalidated**: the mock must move totes this way).
5. There are **three source totes** per episode. Each is an open tote holding **six units** of one SKU, standing upright in two rows of three,
   SKU label up. Each unit is a small boxed item that fits one gripper.
6. The **order slots** are four fixed ledges on the port front at the height of the top, two each side of the window, numbered left to right:
   **S1, S2** on the left and **S3, S4** on the right. Each holds one open **order tote**, fixed in place, starting empty.
7. Each slot has a **slot light** on the front of its ledge and a **slot label** with its name in large print.
8. The **panel** is a small box on a fixed-height stand at the **left end** of the port front in **Config L** and at the **right end** in
   **Config R**, facing the base. It has:
   * a **display** that shows **PICK** and a number (1, 2, or 3) for the presented tote, and **DONE** after the last release;
   * a green **CONFIRM** button that lights while a pick is open;
   * a blue **RELEASE** button that lights after CONFIRM is pressed.
9. The port mock is loaded per episode with the three picks: how many units from each tote, and which slot each goes to. Each tote's pick goes
   to a different slot.
10. At the start, the first source tote is in the window, the display shows its pick, its slot light and CONFIRM are lit, and RELEASE is off.
11. Nothing else stands on the port top, the ledges, or the panel stand within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the slot labels. You judge every other place by eye against the port itself.

* **Port:** the fixed station the base is parked at. Never moved, never leaned on, never pushed.
* **Window:** the opening in the middle of the port top, with the presented tote in it. Either gripper, one at a time, from above. **Nobody in
  it while a tote moves.**
* **Left slots:** S1 and S2, with their lights. **Left gripper only.**
* **Right slots:** S3 and S4, with their lights. **Right gripper only.**
* **Panel:** at the left end (Config L) or the right end (Config R) of the port front. **Panel gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the left slots and the **right gripper** works the right slots. Both use the window, one at a time.
* The **panel gripper** also works the panel.
* Neither arm goes into a slot on the other side, and neither reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds one unit, and while it does, the other gripper is empty and drawn **clear of the port**.

### Arm assignments

* **Picking gripper** (the gripper on the lit slot's side). Takes the counted units out of the presented tote, one at a time, and sets them
  in the lit slot's order tote.
* **Panel gripper** (**left gripper** in Config L, **right gripper** in Config R). Presses CONFIRM and RELEASE for every tote. It is also the
  picking gripper whenever the lit slot is on its side.
* Nothing is ever handed over.

## Vocabulary

* **Goods-to-person port:** a station where the stock comes to the picker in totes, so the picker stays in one place.
* **Presented tote:** the source tote standing still in the window, against the stop.
* **Order slot:** one ledge beside the window with its order tote. Each order tote collects units for one order.
* **Pick number:** the number after PICK on the display: how many units to take from the presented tote.
* **Lit slot:** the order slot whose light is on. It is the only slot the pick may go to.
* **Picking gripper:** the gripper on the lit slot's side, the **left gripper** for S1 and S2 and the **right gripper** for S3 and S4.
* **Panel gripper:** the gripper on the panel's side, the **left gripper** in Config L and the **right gripper** in Config R.
* **Near unit:** of the units in the presented tote, the one nearest the picking gripper's side. Units are always taken near unit first.
* **Top approach:** the gripper comes down into a tote from straight above, inside the tote's rim, and goes out straight up the same way,
  touching neither the window frame nor the tote rim.
* **Set unit:** the unit stands upright on the floor of the order tote, SKU label up, beside any unit already there, and stays put when the
  gripper opens.
* **Press:** the closed gripper comes straight at a button, pushes it once until it clicks, and draws straight back.
* **Clear of the port:** the arm is drawn up and back so that no part of it is inside the window, over a tote, or in front of the panel.
* **Moving tote:** a tote rolling out of or into the window, from the press of RELEASE until the next tote stands against the stop and the
  display shows its pick.

## Steps

Run Steps 1 to 4 once for each presented tote, three times. After the third release the display shows **DONE**: end the episode with Step 5.
The lit slot decides the picking gripper, and the config decides the panel gripper.

### Step 1: Read the panel

**Goal:** the pick number and the lit slot are known, and the picking gripper is named.

* Read the **display**: the **pick number**.
* Find the **lit slot**. Its side decides the **picking gripper**: the **left gripper** for S1 or S2 and the **right gripper** for S3 or S4.
* Check the presented tote stands still against the stop and CONFIRM is lit.

**Check:** the display shows PICK and a number, exactly one slot light is lit, and the tote is still. If no slot is lit or two are, stop and log
a system issue.

### Step 2: Pick the counted units

**Goal:** the lit slot's order tote holds exactly the pick number of units from the presented tote.

* With the **picking gripper**, come down into the presented tote from straight above and close on the two sides of the **near unit**.
* With the **picking gripper**, lift it straight up out of the tote, touching no other unit and not the window frame.
* With the **picking gripper**, carry it level to the lit slot and bring it down into the order tote from straight above, to just above its
  floor.
* With the **picking gripper**, set it down upright, SKU label up, beside any unit already there, then open and lift straight up.
* Count one. Go back for the next near unit and repeat until the count reaches the **pick number**.
* With the other gripper, stay open and **clear of the port** for the whole of this step.

**Check:** the lit slot's order tote holds exactly the pick number of units, all upright, and the presented tote holds six minus that many. If a
unit has tipped in the order tote, close on it with the **picking gripper** and stand it up. If one unit too many went in, take the last one
back out with the **picking gripper** and set it back in the presented tote.

**Expected state:** the counted units are in the lit slot, the picking gripper is **clear of the port**, and CONFIRM is still lit.

### Step 3: Confirm on the panel

**Goal:** the pick is confirmed, the slot light is off, and RELEASE is lit.

* **IF Config L:** the **left gripper** is the panel gripper. **IF Config R:** the **right gripper** is the panel gripper.
* With the **panel gripper**, closed, **press** the green **CONFIRM** button once.
* With the **panel gripper**, draw straight back.
* With the other gripper, stay open and **clear of the port**.

**Check:** the slot light is off, CONFIRM is off, and RELEASE is lit. If CONFIRM is still lit, press it once more with the **panel gripper**.

### Step 4: Release the tote and take the next

**Goal:** the presented tote has rolled away and the next tote stands in the window with its pick shown, or the display shows DONE.

* Check both grippers are **clear of the port**: nothing in the window, nothing over a tote.
* With the **panel gripper**, closed, **press** the blue **RELEASE** button once, then draw straight back.
* With **both grippers**, hold still, clear of the port, while the tote is a **moving tote**.
* Wait until the next tote stands still against the stop and the display shows its pick, or until the display shows **DONE**.

**Check:** RELEASE is off. **IF the display shows a pick:** go back to Step 1 for the new tote. **IF the display shows DONE:** go on to Step 5.

### Step 5: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the three picks done.

* Look once across the port: the display shows DONE, every light is off, and each order slot holds the units its picks asked for.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the three picks are done, the port is still, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the units out of the order totes and put them back in their source totes, six to a tote, in two rows of three, label up.
2. Check every order tote is empty and fixed in its slot.
3. Load the three source totes back into the port so the first stands in the window against the stop.
4. Load the next episode's three picks into the port mock: a pick number of 1, 2, or 3 for each tote and a different slot for each.
5. Move the panel stand to the end of the port for the next episode's config.
6. Check the display shows the first pick, its slot light and CONFIRM are lit, and RELEASE is off.
7. Pick up anything that landed on the port top, a ledge, or the floor.
8. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the reviewer sees. The
coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the port shifts in frame, the port top changes angle or size in frame, or the base rolls, creeps, or turns at any point after
  recording starts.
* **SOP rule broken:** Steps 1 to 5, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: In the window while a tote moved**

* **Visible cue:** any part of a gripper is inside the window, or over a tote, from the press of RELEASE until the next tote stands still against
  the stop; or RELEASE is pressed while a gripper is still in the window.
* **SOP rule broken:** Step 4, both grippers are clear of the port before RELEASE and stay clear while the tote moves.
* **Coaching note:** out, still, then release. A moving tote does not stop for a gripper.

**Violation: Reached into the port**

* **Visible cue:** a gripper goes down past the rim of the presented tote, into the port beside the tote, or toward a waiting tote, or touches
  the window frame.
* **SOP rule broken:** Step 2, every reach into the window is a top approach, inside the presented tote's rim, and nothing reaches past it.
* **Coaching note:** down inside the rim, up the same way. The port brings the stock to you.

**Violation: Leaned on or pushed the port, ledges, or panel**

* **Visible cue:** a gripper, wrist, or forearm rests on the port top, the window frame, a ledge, an order tote, or the panel stand; an order tote
  shifts; or the panel stand rocks or slides.
* **SOP rule broken:** Steps 1 to 4, the port, the ledges, and the panel carry no weight from the arms.
* **Coaching note:** the arm holds itself up. Press only as hard as the button needs.

**Violation: Panel not read**

* **Visible cue:** a gripper moves toward a tote before the display shows the pick; the arms act on the last tote's pick number or slot; or a
  pick starts while the tote is still moving.
* **SOP rule broken:** Step 1, read the display and find the lit slot for every tote before any unit is touched.
* **Coaching note:** number, slot, then move. Every tote is a new pick.

**Violation: Wrong count**

* **Visible cue:** the lit slot ends a pick with more or fewer units than the pick number when CONFIRM is pressed.
* **SOP rule broken:** Step 2, take exactly the pick number of units, one at a time, counting each one.
* **Coaching note:** count each unit as it lands. The count is the whole point of the pick.

**Violation: Wrong slot**

* **Visible cue:** a unit is set in an order tote whose slot light is not lit, including the slot next to the lit one.
* **SOP rule broken:** Step 2, every unit of the pick goes into the lit slot and nowhere else.
* **Coaching note:** follow the light. The slot next door is another customer's order.

**Violation: Unit taken wrong**

* **Visible cue:** a unit other than the near unit is taken; two units come out together; the gripper digs under or pushes other units; or a unit
  is dragged up the tote wall.
* **SOP rule broken:** Step 2, take the near unit by its sides and lift it straight up, touching no other unit.
* **Coaching note:** near first, one at a time, straight up.

**Violation: Unit held wrong**

* **Visible cue:** a unit is held by its top, its label, or one corner, or it swings or tilts in the gripper on the way to the slot.
* **SOP rule broken:** Step 2, close on the two sides of the unit and carry it level.
* **Coaching note:** sides in the gripper, level all the way.

**Violation: Unit dropped in or not set**

* **Visible cue:** a unit is let go from above the order tote floor and falls in; it lands on its side, on another unit, or on the tote rim; or it is
  thrown in.
* **SOP rule broken:** Step 2, bring each unit down to just above the order tote floor and set it upright before opening.
* **Coaching note:** down to the floor, then open. A dropped unit is a damaged unit.

**Violation: Source tote disturbed**

* **Visible cue:** units left in the presented tote are knocked over, pushed into a heap, or pulled toward the rim, or the presented tote is pushed
  off its stop.
* **SOP rule broken:** Step 2, take one unit straight up and touch nothing else in the tote.
* **Coaching note:** the next picker gets this tote. Leave the rest as you found it.

**Violation: Order tote disturbed**

* **Visible cue:** an order tote is pushed, lifted, or tipped on its ledge, or a unit already in it is knocked over or knocked out.
* **SOP rule broken:** Step 2, come down into the order tote from above and set the unit beside the ones already there.
* **Coaching note:** find the free space, then set the unit into it.

**Violation: Confirm done wrong**

* **Visible cue:** CONFIRM is pressed before the last unit of the pick is set; RELEASE is pressed without CONFIRM first; CONFIRM is pressed more than
  once with no reason; or it is pressed with an open gripper or held down.
* **SOP rule broken:** Step 3, once the count is complete, press CONFIRM once with the closed panel gripper.
* **Coaching note:** count done, then confirm. The panel only knows what you tell it.

**Violation: Release done wrong**

* **Visible cue:** RELEASE is pressed before CONFIRM or more than once; it is held down; the wrong button is pressed; or the next pick starts before
  the new tote has stopped and the display shows its pick.
* **SOP rule broken:** Step 4, press RELEASE once, then hold still until the next tote is at the stop and its pick is shown.
* **Coaching note:** one press, then wait. The next tote is not yours until it stops.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the port is not set up in: the gripper away from the panel presses a button, a gripper reaches for a port
  end with no panel, or the panel stand is moved before or during the episode.
* **SOP rule broken:** Steps 3 and 4, look at the port, find the panel, and follow the IF line that matches the config the episode is set up in.
* **Coaching note:** look at the panel before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** units are picked before the panel is read; CONFIRM is pressed before the count is done; RELEASE is pressed before CONFIRM; or a unit
  is fixed in an order tote after the tote has been released.
* **SOP rule broken:** Steps 1 to 4, for each tote: read, pick, confirm, release, then the next.
* **Coaching note:** the order is the task. Each tote leaves the port ready for the next one.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two units; both grippers carry units at the same time; or a gripper holds a unit while the other presses a button.
* **SOP rule broken:** Steps 2 to 4, one gripper holds one unit, and the other is empty and clear of the port.
* **Coaching note:** one unit, one trip.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a tipped unit, one unit too many
  left in a slot, or CONFIRM still lit.
* **SOP rule broken:** Steps 1 to 4, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a unit is dropped on the port top, into the window gap, onto a ledge, or on the floor, or a unit is knocked out of a tote.
* **SOP rule broken:** Steps 2 to 4, nothing is dropped or knocked out of its place, and every gripper comes out the way it went in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **left gripper** sets a unit in S3 or S4; the **right gripper** sets a unit in S1 or S2; the gripper away from the panel presses a
  button; or either arm passes in front of the other.
* **SOP rule broken:** Steps 2 to 4, each gripper serves the slots on its own side, only the panel gripper presses buttons, and the arms never cross.
* **Coaching note:** left slots, left arm. Right slots, right arm. The panel side decides who presses.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends before the display shows DONE, with a slot light or CONFIRM lit, with a slot holding the wrong count, an arm short of
  home, or a gripper not fully open.
* **SOP rule broken:** Step 5, look once across the port, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read the display, a slot light, a button light, or the units in a tote**, so the pick number, the slot, or the count cannot be judged.
* **Port fault:** a tote does not roll out or in after RELEASE, stops short of the stop, jams, or arrives while CONFIRM is still open; no slot or two slots
  light; or a button does not respond.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Setup fault:** a source tote with fewer units than its pick, two picks loaded to the same slot, or a unit with a torn or unreadable label.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a corner of the presented tote, an order tote, or a
  panel button cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Read the panel and the lit slot
2. Take the near unit out of the presented tote
3. Set one unit in the lit slot's order tote
4. Press CONFIRM
5. Press RELEASE
6. Hold clear while the tote moves
7. Return both arms home and end the episode
