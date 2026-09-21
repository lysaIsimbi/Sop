# Assemble a Printed Gearbox Kit SOP (1x Episode: 1 Gearbox)

One episode builds one printed gearbox from a kit of printed parts. The table begins with the **frame
left half** on the **build spot**, just right of the center of the table, and the **frame right half**
lying on the **right stage** beside it. An axle tray and a gear tray sit side by side in the **supply
zone**, the crank lies on the crank rest at the back-right, and the **diagram card** lies face up at the
back-left.

The order never changes: join the two frame halves, press the three axles into their holes, drop the
three gears onto their axles the way the diagram card shows, mesh the teeth left to right, press the
crank onto the top of axle A, then turn the crank a full turn and correct any bind. No axle goes in
before the frame seam is closed. No gear goes on before all three axles stand seated. The crank does not
go on until all three gears sit flat on the frame. The episode does not end until the crank has driven a
full turn with all three marks moving.

The right gripper slides the frame halves together, presses in every axle, seats every gear, rocks each
gear into mesh, fits the crank, drives the function test, and makes the bind correction. The left gripper
presses the frame left half flat on the table by its left edge and holds it there for the whole episode.
The left gripper stays on the left edge of the frame and never reaches across it. The right gripper works
the frame, the crank rest, and (Config M and R) both trays.

The table is set up in one of three ways. Only the two trays move; the frame halves, the crank rest, and the
diagram card are in the same place in all three.

* **Config L:** the trays are at the front-left.
* **Config M:** the trays are at the front-center, in front of the build spot.
* **Config R:** the trays are at the front-right.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the trays start at the front-left (**Config L**), the front-center (**Config M**) or
  the front-right (**Config R**). One config per episode, chosen before recording and never changed
  mid-episode.
* **Same-side rule:** the gripper on the trays' side takes each axle and gear from its cell — the left
  gripper in Config L, the right gripper in Config M and R. The front-center is directly in front of the
  build spot, where the right gripper already works. No arm reaches across the table.
* **Hand-over rule:** in Config L the right gripper cannot reach the front-left past the left gripper, so
  the left gripper lifts off the frame, takes the part, and **hands it over** to the right gripper above the
  build spot: the left gripper holds the part still, the right gripper closes on the opposite side of it, and
  only then does the left gripper open, lift clear, and go back onto the frame's left edge. Nothing is handed
  over in Config M or R.
* **Fixed roles:** the frame left half stays on the build spot, the frame right half on the right stage, the
  crank on its rest, and the diagram card at the back-left in every config. The left gripper holds the frame
  down whenever the right gripper works on it, and the right gripper does every join, press, seat, rock,
  crank fit, and test in every config.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: both frame halves, the axle tray and the gear tray in
   the supply zone for this episode's config, the crank on its rest at the back-right, and the diagram card
   at the back-left.
3. The build spot is visible from above, so all three holes, all three axles, the mark on each gear, and
   the seam between the frame halves can be seen.
4. Both arms are at home with grippers open.
5. The table is bare apart from the two frame halves, the axle tray, the gear tray, the crank, the
   diagram card, and robot hardware.
6. The right arm reaches the build spot, the right stage, the crank rest, and (Config M and R) both trays.
   The left arm reaches the left edge of the frame left half and (Config L) both trays at the front-left
   without stretching.

### Materials checklist

1. One **frame left half** lies on the **build spot**, just right of the center of the table, square to
   the front edge and flat on the table. It carries **hole A** on the left and **hole B** in the middle,
   and a **slot** along its right edge.
2. One **frame right half** lies on the **right stage**, directly right of the build spot, flat and
   square, with its **tongue** pointing left toward the slot. It carries **hole C**.
3. One **axle tray** sits in the supply zone with three cells labelled **A**, **B**, and **C**. Cell A
   holds the **long axle**. Cells B and C hold the two **short axles**, which are the same as each other.
   * **Config L:** front-left, clear of the left gripper's path onto the frame
   * **Config M:** front-center, directly in front of the build spot
   * **Config R:** front-right
4. One **gear tray** sits beside the axle tray in the same zone, with three cells labelled **A**, **B**,
   and **C**. **Gear A** and **gear C** are the small gears. **Gear B** is the large gear. Each gear lies
   with its letter and its **mark** facing up.
5. One **crank** lies flat on the **crank rest** at the back-right, socket down and **handle** standing up.
6. One **diagram card** lies face up at the **back-left**, showing which gear goes on which axle. Neither
   gripper ever touches it.
7. Every gear tooth is clean and unchipped, every axle is straight, and every hole is clean and free of
   stringing from the print.
8. Keep the left side of the table clear apart from the trays in Config L. The left gripper works from there
   onto the frame.
9. Before collection, confirm by hand that the tongue slides into the slot and clicks home, that each axle
   presses into its hole without being forced, that each gear slides down its axle to the frame, that
   neighbouring gears mesh when the teeth are lined up, that the crank socket drops onto the flats of axle
   A, and that turning the crank turns all three gears.

### Workspace layout

- **Build spot:** just right of the center of the table — the frame left half stays here all episode
- **Right stage:** directly right of the build spot — the frame right half waits here
- **Supply zone:** axle tray and gear tray side by side, three lettered cells each — front-left (Config L),
  front-center in front of the build spot (Config M), or front-right (Config R)
- **Back-right:** crank rest, with the crank lying socket down
- **Back-left:** diagram card, face up and never touched
- **Left side:** kept clear apart from the trays in Config L, so the left gripper can come in onto the frame's
  left edge

### Arm assignments

- **Left gripper:** presses the frame left half flat against the table by its left edge and holds it there
  through every step, so the frame cannot slide or lift while the right gripper works. In Config L it also
  takes each axle and gear from the front-left and hands it over to the right gripper above the build spot,
  then goes back onto the frame edge.
- **Right gripper:** slides the frame right half home, presses in all three axles, seats all three gears in
  diagram order, rocks each gear into mesh, fits the crank, drives the function test, and makes the bind
  correction. Takes each axle and gear from its cell itself in Config M and R, and from the left gripper in
  Config L.

## Vocabulary

- **Supply zone:** where the axle tray and the gear tray sit at the start of the episode — front-left
  (**Config L**), front-center (**Config M**), or front-right (**Config R**). One per episode, chosen before
  recording and never changed mid-episode.
- **Hand over:** the left gripper holds an axle or gear still above the build spot, the right gripper closes
  on the opposite side of the part, and only then does the left gripper open and lift clear. Config L only,
  because the right gripper cannot reach the front-left past the left gripper.
- **Frame left half:** the printed plate with hole A and hole B. It stays on the build spot for the whole
  episode and is never lifted.
- **Frame right half:** the printed plate with hole C. It slides left into the frame left half.
- **Tongue:** the flat printed tab on the left edge of the frame right half.
- **Slot:** the matching printed groove along the right edge of the frame left half. The tongue slides
  into it.
- **Seam:** the join line between the two frame halves once the tongue is in the slot.
- **Clicked home:** the tongue is all the way into the slot, the seam is closed with no gap along its
  length, and the right half does not slide back when the right gripper lets go.
- **Frame:** the two halves once they are clicked home. From then on they are treated as one part.
- **Hole:** one of the three printed holes an axle presses into. Hole A is on the left, hole B is in the
  middle, hole C is on the right, past the seam.
- **Axle:** one of the three printed pegs that stand upright in the holes. Each axle has a **step**
  partway up. Below the step it is thin and grips the hole. Above the step it is the smooth part the gear
  turns on.
- **Long axle:** the taller axle. It goes in hole A and stands up above gear A so the crank can go on it.
- **Short axle:** either of the two shorter axles. They go in holes B and C and are the same as each other.
- **Axle seated:** the axle's step sits down flat on the frame, the axle stands straight up, and it does
  not lean or lift when the right gripper lets go.
- **Flats:** the two flat faces on the top of the long axle. The crank socket only goes on when it lines
  up with them.
- **Gear:** one of the three toothed wheels. Gear A goes on axle A, gear B on axle B, gear C on axle C.
- **Tooth:** one of the raised points around the edge of a gear.
- **Gap:** the space between two teeth on a gear. A tooth of one gear drops into a gap of its neighbour.
- **Mark:** the painted line on the top face of each gear. It shows at a glance whether that gear is
  turning.
- **Neighbour:** the gear on the next axle to the left or the right. Gear B's neighbours are gear A and
  gear C.
- **Riding high:** the gear went down its axle but stopped short, because its teeth landed tip to tip on
  its neighbour's teeth instead of dropping into the gaps. A gear riding high sits above the frame and
  looks taller than the others.
- **Gear seated:** the gear is all the way down its axle, its underside touches the frame, and it sits
  level, not tilted on the axle.
- **Meshed:** the teeth of the two neighbouring gears sit in each other's gaps, and both gears are seated
  flat on the frame.
- **Rock:** turn a gear a small amount one way, then the other way, with a light hand, so its teeth can
  find the gaps of its neighbour and the gear drops down.
- **Crank:** the printed arm that drives the gearbox. One end is a square **socket** that goes on the
  flats of axle A. The other end carries the **handle**.
- **Handle:** the peg standing up from the free end of the crank. The right gripper pushes it around to
  drive the gearbox.
- **Crank seated:** the socket is all the way down on the flats, the crank sits level, and it does not
  lift off when the right gripper lets go.
- **Turns freely:** the gear moves when its neighbour moves, with no scraping and no need to push hard.
- **Bind:** the gearbox will not turn. Either the crank will not go round any further, or the crank turns
  while one of the gears' marks does not move.
- **Full turn:** the crank has gone all the way around, so the handle comes back to where it started.

## Steps

Run Steps 1–6 in order on the one gearbox, then end the episode with Step 7. Steps 2 and 3 depend on where
the trays are: in Config M and R the **right gripper** takes each axle and gear from its cell itself; in
Config L the **left gripper** takes it from the front-left and **hands it over** to the right gripper above
the build spot, then goes back onto the frame. Every other line is the same in all three configs.

### Step 1: Join the frame and hold it down

**Goal:** the two frame halves are clicked home on the build spot and the frame is pinned flat for the
rest of the episode.

#### 1.1 Hold the left half

- With the **left gripper**, press down on the **left edge** of the frame left half and hold it against
  the table.
- Keep the **left gripper** there through Steps 2, 3, 4, 5, and 6. Release only in Step 7.
- **IF Config L:** the left gripper lifts off only to fetch an axle or gear in Steps 2 and 3, and is back on
  the left edge before the right gripper lowers the part.

**Check:** the frame left half is flat on the table, square to the front edge, and does not slide when the
left gripper presses. If it is crooked, straighten it with the left gripper first, then press it down.

#### 1.2 Slide the right half home

- With the **right gripper**, take the **frame right half** by its **right edge**.
- Slide it **left along the table** until the **tongue** enters the **slot**, then keep pushing until it
  **clicks home**.
- Keep it flat on the table the whole way. Do not lift it, and do not lower it onto the slot from above.
- Push straight left. Do not twist it into the slot.
- Let go and look at the **seam**.

**Expected state:** one frame on the build spot, seam closed along its whole length, three holes in a row
running left to right, and the right stage empty.

**Check:** the seam is closed with no gap, the frame is flat on the table, and the right half does not
slide back when the right gripper lets go. If a gap shows, push the right half left again with the right
gripper until it clicks. If the tongue rides up on top of the slot, pull it straight back right, set it
flat, and slide it in again.

### Step 2: Press in the three axles

**Goal:** all three axles stand seated in their own holes, straight up, in order.

- Fit the axles in order: hole A, then hole B, then hole C. Look where the trays are before reaching for the
  first axle.
- **IF the trays are at the front-left (Config L):** the **left gripper** lifts off the frame, takes the axle
  by its **lower part** below the step, carries it straight up and level to above the **build spot**, and
  holds it still. The **right gripper** closes on the **upper part**; the **left gripper** opens, lifts
  clear, and goes back onto the frame's left edge.
- **IF the trays are at the front-center (Config M):** the **right gripper** takes the axle by its **upper
  part** from its cell, straight back from the tray to the build spot.
- **IF the trays are at the front-right (Config R):** the **right gripper** takes the axle by its **upper
  part** from its cell and carries it left to the build spot.

Then, in all three:

- With the **right gripper**, one axle at a time, hold the axle straight up over its hole, lower it in, and
  press straight down until the **step** stops on the frame.
- The **long axle** goes in **hole A**. A **short axle** goes in **hole B** and the other in **hole C**.
- Press straight down only. Do not lever the axle, do not twist it in, and do not push it in at an angle.
- Carry one axle at a time, straight from its cell to its hole. Do not rest an axle on the frame or the
  table on the way.
- If an axle will not go down with a steady press, pull it straight back up, look at the hole, and lower
  it in again straight.

**Expected state:** three axles standing upright in a row, the tall one on the left, axle tray empty.

**Check:** each axle's step sits flat on the frame, each axle stands straight up, none leans or lifts when
the right gripper lets go, and the long axle is the one in hole A. If an axle stands proud or leans, pull
it straight up with the right gripper and press it in again straight. If the long axle went into the wrong
hole, pull it straight up and swap it with the axle in hole A.

### Step 3: Seat the three gears per the diagram

**Goal:** all three gears are on their own axles, in order, each lowered straight down.

- Read the **diagram card** at the back-left before each gear. Gear A goes on axle A, gear B on axle B,
  gear C on axle C. Neither gripper touches the card.
- **IF Config M or R:** the **right gripper** takes each gear by its rim from its cell. **IF Config L:** the
  **left gripper** lifts off the frame, takes the gear by its rim from its cell, and holds it still above the
  build spot; the **right gripper** closes on the rim opposite; the **left gripper** opens, lifts clear, and
  goes back onto the frame's left edge.
- Carry one gear at a time by its **rim**, straight from its cell to its axle. Do not set a gear on the
  frame or the table, and do not carry two at once.
- Lower each gear straight down the axle, keeping it level. Do not drop it, and do not tilt it onto the
  axle.
- A gear may stop short and ride high on its neighbour's teeth. That is fine here — leave it and go on.
  Step 4 brings it down.
- Do not press or twist a gear that stops. Let go and move to the next gear.

#### 3.1 Gears A and B

- With the **right gripper**, holding **gear A** by its rim, bring it level over **axle A** and lower it
  straight down until it stops.
- With the **right gripper**, seat **gear B** on **axle B** the same way.

#### 3.2 Gear C

- With the **right gripper**, seat **gear C** on **axle C** the same way.

**Expected state:** three gears on three axles, letters matching the diagram, gear tray empty, and the top
of the long axle still standing clear above gear A. Some gears may be riding high.

**Check:** each axle carries one gear, the letters match the diagram, no gear is tilted on its axle, and no
gear is lying on the frame or the table. If a gear went on the wrong axle, lift it straight up with the
right gripper and lower it onto its own axle. If a gear is tilted, lift it straight up and lower it again
level.

### Step 4: Mesh the teeth, left to right

**Goal:** both pairs are meshed and all three gears are seated flat on the frame.

- With the **left gripper**, keep pressing the frame down.
- Work the pairs in this order: gear A with gear B, then gear B with gear C.
- For each pair, with the **right gripper**, pinch the rim of the gear that is riding high and **rock** it
  until its teeth drop into its neighbour's gaps and the gear settles onto the frame.
- If neither gear of a pair is riding high, rock the right-hand gear of that pair a small amount anyway, to
  confirm both gears turn together.
- Rock with a light hand only. Do not turn a gear hard against a stop, and do not press a gear down the
  axle to force it.
- Do not go on to the second pair until the first pair is meshed.

**Expected state:** all three gears sit flat on the frame at the same height, and turning any one gear
turns its neighbours.

**Check:** every gear is seated, both neighbouring pairs are meshed, no gear is riding high, and the seam
is still closed. If a gear still rides high after rocking, lift it straight up off its axle with the right
gripper, turn it a small amount in the air, and lower it back down, then rock it again. If the seam has
opened, push the right half left with the right gripper until it clicks home, then mesh gear B with gear C
again.

### Step 5: Fit the crank

**Goal:** the crank is seated on the flats at the top of axle A, and all three gears still turn freely.

- With the **left gripper**, keep pressing the frame down.
- With the **right gripper**, take the **crank** from the crank rest by its **arm**, socket down.
- Hold it level over the top of **axle A** and lower it until the socket touches the **flats**.
- Turn the crank a small amount one way, then the other, until the socket lines up with the flats and
  drops on.
- Press straight down until the crank stops.
- Press onto the axle top only. Stop pressing as soon as the crank stops — do not push the crank down onto
  gear A.
- Do not force the crank on at an angle, and do not press it on across the corners of the flats.

**Expected state:** the crank sits level across the top of axle A, its handle stands up clear of the gears,
the crank rest is empty, and all three gears are still flat on the frame.

**Check:** the crank is seated level, it does not lift off when the right gripper lets go, it is not
pressing on gear A, axle A is still seated with its step flat on the frame, and gear A still turns when
gear B turns. If the crank sits crooked or lifts off, pull it straight up, line it up with the flats, and
press it on again. If the crank was pressed down onto gear A, pull it straight up and refit it, stopping
at the axle top. If axle A lifted in its hole, pull the crank off, press the axle back down until its step
sits flat, and fit the crank again.

### Step 6: Function-test the rotation and correct any bind

**Goal:** the crank drives all three gears through a full turn with nothing binding.

#### 6.1 Function test

- With the **left gripper**, keep pressing the frame down.
- With the **right gripper**, close the gripper and set its tip against the **handle**.
- Push the handle around the circle. Lift the tip clear, set it back on the handle further round, and push
  again.
- Keep pushing until the crank has made a **full turn**, so the handle comes back to where it started.
- While the crank turns, watch the **marks** on gears A, B, and C. All three marks must move.
- Drive from the handle only. Do not push a gear to turn the gearbox, and do not grab the crank arm and
  twist it.
- If the crank makes a full turn and all three marks moved, the gearbox is good — skip 6.2 and go to
  Step 7.
- If the crank will not go any further, or one mark does not move, there is a **bind** — go to 6.2.

**Check:** the crank made a full turn, all three marks moved, the crank is still seated, all three axles
are still seated, the seam is still closed, and the frame is still on the build spot.

#### 6.2 Correct the bind

- Name the gear that binds: the first gear whose mark did not move, or the gear where the crank stops.
- If the binding gear is **gear A**, first pull the **crank** straight up off axle A with the **right
  gripper** and set it back on the crank rest.
- With the **right gripper**, lift the binding gear straight up off its axle, turn it a small amount in the
  air, and lower it straight back down the axle.
- With the **right gripper**, **rock** it until it meshes with its neighbour or neighbours and sits flat on
  the frame.
- If the crank came off, fit it again as in Step 5.
- Never lift gear A while the crank is still on, and never pry the crank off sideways.
- Never force the crank round against a stop.
- Run 6.1 again from the start.
- If the same gear binds after two corrections, stop, end the episode at Step 7, and log the kit for a
  station check.

**Check:** the corrected gear is seated and meshed, the crank is seated, and 6.1 then runs clean. If it
does not, count the correction and follow the two-correction rule above.

### Step 7: End the episode

**Goal:** recording ends with the gearbox built and function-tested.

1. Confirm the seam is closed, all three axles are seated, all three gears are on their own axles and
   seated flat and meshed, the crank is seated on axle A, both trays and the crank rest are empty, and the
   frame is still square on the build spot.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

1. With recording off, pull the crank straight off axle A by hand and lay it back on the crank rest, socket
   down and handle up.
2. Lift the three gears off their axles and put each one back in its own lettered cell in the gear tray,
   letter and mark facing up.
3. Pull the three axles straight up out of their holes and put each one back in its own lettered cell in
   the axle tray, with the long axle in cell A.
4. Pull the frame halves apart by sliding the right half right, and set it on the right stage, flat and
   square, tongue pointing left. Set the frame left half square on the build spot, flat against the table.
   Set both trays side by side for the next episode's config — front-left (Config L), front-center in front
   of the build spot (Config M), or front-right (Config R).
5. Wipe any grit off the axles, the holes, and the gear teeth, and pick off any print stringing.
6. Inspect the parts. Replace a gear if a tooth is chipped, worn round, or bent. Replace an axle if it is
   bent, or if it no longer grips its hole. Replace a frame half if the tongue or slot no longer clicks
   home, or if a hole has gone loose. Replace the crank if the socket no longer holds on the flats.
7. Run both Setup checklists before the next episode.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

- the **start timestamp** in the video;
- the **violation name** from the list below; and
- the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation
label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain multiple violations; tag each
separately. Retain the episode in training data with its violation tags. Do not delete a recorded episode
solely because it contains a violation.

### Violations

**Note on the start position:** the violations below were written for Config R (trays at the front-right).
The pickup and arm-role cues will be rewritten later to cover all three start positions; they are left as
they are for now. Until then, anything that does not match the episode's config goes under
**Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the trays are not in the
  supply zone for the config; a gripper reaches across the table for an axle or gear; in Config L the left
  gripper carries a part to its hole or axle itself, or the right gripper reaches to the front-left for one,
  instead of a hand-over above the build spot; or the wrong IF line is followed.
- **SOP rule broken:** the start position, the same-side rule, and the hand-over rule (the right gripper
  takes each axle and gear from its cell in Config M and R; in Config L the left gripper takes it and hands
  it over to the right gripper above the build spot; no arm reaches across the table; the IF line followed
  is the one for the config on the table).
- **Coaching note:** look where the trays are before the first reach, then follow that config's IF lines
  through Steps 2 and 3.

**Violation: Frame not held**
- **Visible cue:** the left gripper is off the left edge of the frame while the right gripper joins,
  presses in an axle, seats a gear, rocks, cranks, or tests, and the frame slides, lifts, or is chased
  across the spot.
- **SOP rule broken:** Step 1.1 (the left gripper presses the frame down by its left edge and holds it
  there through Steps 2–6).
- **Coaching note:** left gripper on the frame first, and leave it there until the episode ends.

**Violation: Frame seam left open**
- **Visible cue:** a gap shows along the seam and the episode moves on to the axles, or the right half
  slides back out later and is not pushed home again.
- **SOP rule broken:** Steps 1.2 and 2 (the right half is clicked home with the seam closed before the
  first axle goes in, and the seam stays closed).
- **Coaching note:** let go and look at the seam. A gap there is a gearbox that will not mesh.

**Violation: Frame right half lifted or twisted in**
- **Visible cue:** the right gripper picks the right half up off the table, lowers it onto the slot from
  above, or turns it into the slot instead of pushing it straight left.
- **SOP rule broken:** Step 1.2 (keep the right half flat on the table and push it straight left into the
  slot).
- **Coaching note:** flat on the table, straight left, until it clicks.

**Violation: Frame moved off the build spot**
- **Visible cue:** the frame left half is lifted, turned, dragged, or ends the episode out of square with
  the front edge.
- **SOP rule broken:** Steps 1–6 (the frame left half stays flat and square on the build spot for the
  whole episode and is never lifted).
- **Coaching note:** bring the part to the frame; never move the frame to the part.

**Violation: Axle in the wrong hole or out of order**
- **Visible cue:** the long axle ends up in hole B or hole C, a short axle is in hole A, a hole is left
  bare, or an axle goes into hole B or hole C before hole A is filled.
- **SOP rule broken:** Step 2 (fit hole A, then B, then C, with the long axle in hole A and a short axle in
  each of holes B and C).
- **Coaching note:** long axle first, in hole A, then work right.

**Violation: Axle not seated**
- **Visible cue:** an axle stands proud with its step off the frame, leans over, or lifts back up when the
  right gripper lets go, or axle A rises out of its hole while the crank goes on, and the step moves on
  anyway.
- **SOP rule broken:** Steps 2 and 5 (press each axle straight down until its step stops flat on the frame
  and it stands straight up, and axle A is still seated with its step flat after the crank goes on).
- **Coaching note:** press until the step lands, then let go and watch whether it stays. Press the crank on
  straight down in line with the axle so nothing shifts underneath.

**Violation: Axle forced in**
- **Visible cue:** the right gripper levers an axle, twists it into the hole, pushes it in at an angle, or
  works a stuck axle instead of pulling it back out.
- **SOP rule broken:** Step 2 (press straight down only; if it will not go, pull it straight back up and
  lower it in again straight).
- **Coaching note:** straight down or straight back out. Never lever an axle.

**Violation: Axle or gear mishandled on the way in**
- **Visible cue:** an axle or gear is rested on the frame or the table on the way, two are carried at once,
  or a gear is picked up by its teeth instead of its rim.
- **SOP rule broken:** Steps 2 and 3 (carry one part at a time, straight from its cell to its place, gears
  by the rim).
- **Coaching note:** one part, straight in, no stops on the way.

**Violation: Gear on the wrong axle or out of order**
- **Visible cue:** a gear's letter does not match its axle, the large gear sits on axle A or axle C, two
  gears end up on one axle, or gear C goes on before gear A or gear B.
- **SOP rule broken:** Step 3 (gear A on axle A, gear B on axle B, gear C on axle C, seated in that order,
  as the diagram card shows).
- **Coaching note:** check the letter against the diagram before you lower each gear.

**Violation: Gear dropped or tilted onto the axle**
- **Visible cue:** the right gripper opens above the axle and the gear falls onto it, bounces, or lands off
  the axle; or a gear goes down at an angle and is left cocked on its axle with one side high and one side
  low.
- **SOP rule broken:** Step 3 (hold each gear level over its axle, lower it straight down, and release it
  only once it stops).
- **Coaching note:** flat over the axle, straight down, and all the way before you open the gripper.

**Violation: Gear forced onto the axle**
- **Visible cue:** a gear stops part way down and the right gripper presses it, twists it hard, or works it
  down instead of letting go and moving on.
- **SOP rule broken:** Step 3 (do not press or twist a gear that stops; leave it riding high and go on).
- **Coaching note:** a gear that stops is riding high, not stuck. Let go and mesh it in Step 4.

**Violation: Mesh step skipped**
- **Visible cue:** the crank goes on, or the function test starts, while a gear is still riding high and
  sits above the others.
- **SOP rule broken:** Step 4 (both pairs are meshed and all three gears sit flat on the frame before
  Step 5).
- **Coaching note:** look across the tops of the gears. They all sit at one height before the crank goes on.

**Violation: Pairs meshed out of order**
- **Visible cue:** the right gripper rocks gears B and C together before gears A and B are meshed, or it
  jumps between the two pairs.
- **SOP rule broken:** Step 4 (mesh gear A with gear B, then gear B with gear C, finishing the first pair
  before starting the second).
- **Coaching note:** left pair first, then the right pair, one at a time.

**Violation: Gear forced instead of rocked**
- **Visible cue:** the right gripper turns a gear hard against a stop, presses a gear down its axle, or the
  teeth grind or click loudly instead of the gear settling.
- **SOP rule broken:** Step 4 (rock the gear with a light hand so the teeth find the gaps).
- **Coaching note:** small turns each way and a light hand. The gear drops on its own.

**Violation: Crank not seated or forced on**
- **Visible cue:** the crank sits crooked, stands proud of the axle top, lifts off when the right gripper
  lets go, is pressed on across the corners of the flats, or is pushed on at an angle instead of being
  turned until it drops.
- **SOP rule broken:** Step 5 (lower the socket onto the flats, turn it a small amount each way until it
  drops on, then press straight down until it stops).
- **Coaching note:** let it find the flats. Turn a little, then straight down.

**Violation: Crank pressed down onto gear A**
- **Visible cue:** the right gripper keeps pressing after the crank stops, and gear A is clamped and no
  longer turns when gear B turns.
- **SOP rule broken:** Step 5 (press onto the axle top only and stop as soon as the crank stops; gear A
  still turns freely).
- **Coaching note:** the crank drives the axle, it does not hold the gear still. Stop at the axle top.

**Violation: Function test skipped or cut short**
- **Visible cue:** the episode ends without the right gripper driving the crank, or the crank is nudged
  only part way and the handle never returns to where it started.
- **SOP rule broken:** Step 6.1 (drive the crank a full turn, until the handle comes back to where it
  started).
- **Coaching note:** a full turn of the crank, every episode, before the ending.

**Violation: Test driven from the wrong place**
- **Visible cue:** the right gripper pushes a gear to turn the gearbox, or grabs the crank arm and twists it
  instead of pushing the handle round.
- **SOP rule broken:** Step 6.1 (set the closed gripper tip against the handle and push it around; drive
  from the handle only).
- **Coaching note:** handle only, tip against it, push it round.

**Violation: Bind left uncorrected**
- **Visible cue:** the crank stops, or one of the marks does not move, and the episode goes to the ending
  without a correction.
- **SOP rule broken:** Step 6.2 (a bind is corrected before the episode ends).
- **Coaching note:** watch all three marks. If one stays still, that gear comes off and goes back on.

**Violation: Bind corrected the wrong way**
- **Visible cue:** the right gripper forces the crank round against a stop, pries the crank off sideways,
  or lifts gear A while the crank is still on.
- **SOP rule broken:** Step 6.2 (pull the crank straight up first when gear A binds, then lift the gear
  straight up; never force the crank and never pry it off sideways).
- **Coaching note:** crank off straight up, gear off straight up, turn it, back down, rock, re-fit.

**Violation: Correction not re-tested**
- **Visible cue:** a gear is reseated and the crank is back on, and the episode ends with no fresh full turn
  of the crank.
- **SOP rule broken:** Step 6.2 (run 6.1 again from the start after every correction).
- **Coaching note:** every fix earns another full turn of the crank.

**Violation: Diagram card touched or covered**
- **Visible cue:** a gripper moves, slides, or knocks the diagram card, or a part or an arm is parked on
  top of it so its face cannot be seen.
- **SOP rule broken:** Step 3 (read the diagram card at the back-left; neither gripper touches it).
- **Coaching note:** the card is for reading only. Keep both grippers and every part off it.

**Violation: Wrong arm used**
- **Visible cue:** an action assigned to one gripper is done by the other, including the left gripper
  sliding the frame half, pressing in an axle, seating or rocking a gear, fitting the crank, or driving the
  test, or the right gripper holding the frame down.
- **SOP rule broken:** Steps 1–6 (the right gripper joins the frame, presses in the axles, seats and rocks
  the gears, fits the crank, drives the test, and corrects a bind; the left gripper presses the frame down).
- **Coaching note:** right gripper does all the work on the frame, left gripper only holds it down.

**Violation: Part or supply knocked over**
- **Visible cue:** an axle, a gear, the crank, the axle tray, or the gear tray is dropped, tipped, pushed
  off its spot, or spilled onto the table or the floor.
- **SOP rule broken:** Steps 2–6 (keep the axles, gears, crank, and both trays on their spots through the
  build).
- **Coaching note:** work slower and lower over the table, and keep carries short.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before the function test passes, an arm is not home, a gripper is closed,
  or an arm does something else after homing.
- **SOP rule broken:** Step 7 (confirm the end state, return both arms home with grippers open as their
  final action, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than
tagging them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- A gear has a chipped or malformed tooth, so a correctly seated pair still binds.
- An axle is bent, or its hole has printed loose, so a correctly pressed axle cannot stand straight.
- The tongue or slot has printed out of size, so the seam will not close however it is pushed.
- The holes are spaced wrong for the gears, so a pair cannot mesh however it is seated.
- The crank socket has printed too wide, so it will not hold on the flats.

## Annotation subtasks (from SOP)

1. Press the frame left half flat and hold it with the left gripper
2. Slide the frame right half left until the seam clicks home
3. Hand an axle or gear from the left gripper to the right gripper above the build spot (Config L)
4. Press the long axle into hole A and the short axles into holes B and C
5. Seat gear A on axle A and gear B on axle B
6. Seat gear C on axle C
7. Mesh gear A with gear B, then gear B with gear C
8. Fit the crank onto the flats at the top of axle A
9. Drive the crank a full turn and watch all three marks
10. Correct a bind: uncrank, lift, reseat, re-mesh, re-fit, and re-test
11. Confirm the end state, return both arms home, and end the episode
