# Assemble a Four-Gear Train SOP (1x Episode: 1 Gear Train)

One episode builds one four-gear train. The table begins with the **baseplate** on the assembly spot,
just right of the center of the table, carrying four bare upright shafts in a row. A gear tray with four
numbered gears sits in the start zone for the episode's config, and a cap tray with four retaining caps
sits at the right.

The order never changes: seat all four gears on their shafts in number order, mesh the teeth left to
right, fit the four caps, then spin-test the train and correct any bind. No gear goes on before the gear
to its left is on its shaft. No cap goes on until all four gears sit flat down on the plate. The episode
does not end until gear 1 drives all four gears through a full turn.

The right gripper carries and seats every gear, rocks each gear down into mesh, fits all four caps,
drives the spin test, and makes the bind correction. The left gripper presses the baseplate flat on the
table by its left edge and holds it there for the whole episode. The left gripper stays on the left edge
of the plate and never reaches across it. The right gripper works the plate, the gear tray, and the cap
tray.

The table is set up in one of three ways. Only the gear tray moves; the baseplate, the cap tray, and the
clear left side are in the same place in all three.

* **Config M:** the gear tray is at the front-center, directly in front of the assembly spot.
* **Config R1:** the gear tray is at the front-right.
* **Config R2:** the gear tray is at the back-right, behind the cap tray.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line
that matches.

What stays constant across all sessions:

* **Start position:** the gear tray starts at the front-center (**Config M**), the front-right
  (**Config R1**) or the back-right (**Config R2**). One config per episode, chosen before recording and
  never changed mid-episode.
* **Same-side rule:** all three start zones lie on the right gripper's side of the table, so the **right
  gripper** takes every gear from the tray in every config. No arm reaches across the table, and the left
  gripper never leaves the plate's left edge to fetch a gear. Nothing is handed over.
* **Fixed roles:** everything else is the same in all three configs — the left gripper holds the
  baseplate down, the right gripper seats, rocks, caps, spin-tests, and corrects, and the caps always come
  from the cap tray at the right.
* **Order:** gears 1 to 4 in number order, mesh left to right, caps 1 to 4, then the spin test.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the baseplate with all four shafts, the gear tray in the
   start zone for this episode's config, and the cap tray at the right.
3. The baseplate is visible from above, so all four shafts, all four gears, and the mark on each gear
   can be seen.
4. Both arms are at home with grippers open.
5. The table is bare apart from the baseplate, the gear tray, the cap tray, and robot hardware.
6. The right arm reaches all four shafts, the cap tray, and every cell of the gear tray in its start zone
   — front-center (Config M), front-right (Config R1), or back-right (Config R2) — without stretching. The
   left arm reaches the left edge of the baseplate without stretching.

### Materials checklist

1. One **baseplate** lies on the **assembly spot**, just right of the center of the table, square to
   the front edge and flat on the table.
2. The baseplate carries four **shafts** standing upright in one row running left to right. **Shaft 1**
   is the leftmost and **shaft 4** is the rightmost. Each shaft is bare, clean, and straight.
3. One **gear tray** sits in the start zone for this episode's config, holding four **gears**, one per
   **cell**. Cells 1, 2, 3, and 4 run left to right and each gear carries its **number label** and its
   **mark** facing up.
   * **Config M:** front-center, directly in front of the assembly spot
   * **Config R1:** front-right
   * **Config R2:** back-right, behind the cap tray
4. One **cap tray** sits at the right of the assembly spot, holding four **retaining caps** lying
   opening-down. The four caps are the same and any cap fits any shaft.
5. Every gear tooth is clean and unchipped, and every shaft top is clean and free of burrs.
6. Keep the left side of the table clear. The left gripper works from there onto the plate.
7. Before collection, confirm by hand that each gear slides down its shaft to the plate without being
   forced, that each pair of neighbours meshes when the teeth are lined up, that each cap presses onto a
   shaft top and holds its gear on while the gear still turns, and that turning gear 1 turns all four
   gears.

### Workspace layout

- **Assembly spot:** just right of the center of the table — the baseplate stays here all episode
- **Gear tray start zone:** front-center, in front of the assembly spot (Config M), front-right
  (Config R1), or back-right, behind the cap tray (Config R2) — gear tray with four numbered gears
- **Right supply zone:** cap tray with four retaining caps
- **Left side:** kept clear, so the left gripper can come in onto the plate's left edge

### Arm assignments

- **Left gripper:** presses the baseplate flat against the table by its left edge and holds it there
  through every step, so the plate cannot slide or lift while the right gripper works. It does this in
  every config and never fetches a gear.
- **Right gripper:** takes every gear from the tray in its start zone — reaching forward in Config M, to
  the front-right in Config R1, and back past the cap tray in Config R2 — carries and seats all four gears in
  order, rocks each gear down into mesh, fits all four retaining caps, drives the spin test on gear 1, and
  makes the bind correction.

## Vocabulary

- **Baseplate:** the flat plate the gears are built on. It stays on the assembly spot for the whole
  episode and is never lifted.
- **Shaft:** one of the four upright posts on the baseplate that a gear slides onto. Shaft 1 is leftmost,
  shaft 4 is rightmost.
- **Shaft top:** the free upper end of a shaft, above the gear, where the retaining cap presses on.
- **Gear:** one of the four toothed wheels. Gear 1 goes on shaft 1, gear 2 on shaft 2, and so on.
- **Start zone:** where the gear tray sits at the start of the episode — front-center (**Config M**),
  front-right (**Config R1**), or back-right (**Config R2**). One per episode, chosen before recording and
  never changed mid-episode.
- **Tooth:** one of the raised points around the edge of a gear.
- **Gap:** the space between two teeth on a gear. A tooth of one gear drops into a gap of its neighbour.
- **Mark:** the painted line on the top face of each gear. It shows at a glance whether that gear is
  turning.
- **Neighbour:** the gear on the next shaft to the left or the right. Gear 2's neighbours are gear 1 and
  gear 3.
- **Riding high:** the gear went down its shaft but stopped short, because its teeth landed tip to tip
  on its neighbour's teeth instead of dropping into the gaps. A gear riding high sits above the plate and
  looks taller than the others.
- **Gear seated:** the gear is all the way down its shaft, its underside touches the baseplate, and it
  sits level, not tilted on the shaft.
- **Meshed:** the teeth of the two neighbouring gears sit in each other's gaps, and both gears are
  seated flat on the plate.
- **Rock:** turn a gear a small amount one way, then the other way, with a light hand, so its teeth can
  find the gaps of its neighbour and the gear drops down.
- **Cap:** one of the four retaining caps that press onto a shaft top and hold a gear on the shaft.
- **Cap seated:** the cap sits level and all the way down on the shaft top, does not lift off when the
  right gripper lets go, and the gear below it still turns.
- **Turns freely:** the gear moves when its neighbour moves, with no scraping and no need to push hard.
- **Bind:** the train will not turn. Either gear 1 will not go round any further, or gear 1 turns while
  one of the other gears' marks does not move.
- **Full turn:** gear 1 has gone all the way around, so its mark comes back to where it started.

## Steps

Run Steps 1–5 in order on the one gear train, then end the episode with Step 6. Only the gear pick in
Step 2 depends on where the gear tray is: the **right gripper** reaches forward to it in Config M, to the
front-right in Config R1, and back past the cap tray in Config R2. Every other line is the same in all three
configs.

### Step 1: Hold the baseplate down

**Goal:** the baseplate is pinned flat on the assembly spot and stays there for the rest of the episode.

- With the **left gripper**, press down on the **left edge** of the baseplate and hold it against the
  table.
- Keep the **left gripper** there through Steps 2, 3, 4, and 5. Release only in Step 6.

**Check:** the baseplate is flat on the table, square to the front edge, and does not slide when the
left gripper presses. If the plate is crooked, straighten it with the left gripper first, then press it
down.

### Step 2: Seat the four gears in order

**Goal:** all four gears are on their own shafts, in number order, each lowered straight down.

- Carry one gear at a time, straight from its cell to its shaft. Do not set a gear on the table or on
  the plate, and do not carry two at once.
- Lower each gear straight down the shaft, keeping it level. Do not drop it, and do not tilt it onto the
  shaft.
- A gear may stop short and ride high on its neighbour's teeth. That is fine here — leave it and go on.
  Step 3 brings it down.
- Do not press or twist a gear that stops. Let go and move to the next gear.

#### 2.1 Gears 1 and 2

Look where the gear tray is before reaching for gear 1.

- **IF the gear tray is at the front-center (Config M):** with the **right gripper**, reach forward past
  the plate's front edge, take **gear 1** by its rim from cell 1, lift it straight up, and carry it back
  over the plate to **shaft 1**.
- **IF the gear tray is at the front-right (Config R1):** with the **right gripper**, take **gear 1** by
  its rim from cell 1, lift it straight up, and carry it left and back to **shaft 1**.
- **IF the gear tray is at the back-right (Config R2):** with the **right gripper**, reach back past the
  cap tray, take **gear 1** by its rim from cell 1, lift it straight up, and carry it forward and left,
  clear of the cap tray, to **shaft 1**.

Then, in all three:

- Hold **gear 1** level over **shaft 1** and lower it straight down until it stops.
- With the **right gripper**, seat **gear 2** on **shaft 2** the same way, from the same tray.

#### 2.2 Gears 3 and 4

- With the **right gripper**, seat **gear 3** on **shaft 3** the same way.
- With the **right gripper**, seat **gear 4** on **shaft 4** the same way.

**Expected state:** four gears on four shafts, numbers matching, gear tray empty. Some gears may be
riding high.

**Check:** each shaft carries one gear, the numbers match, no gear is tilted on its shaft, and no gear is
lying on the plate or the table. If a gear went on the wrong shaft, lift it straight up with the right
gripper and lower it onto its own shaft. If a gear is tilted, lift it straight up and lower it again
level.

### Step 3: Mesh the teeth, left to right

**Goal:** all three pairs are meshed and all four gears are seated flat on the plate.

- With the **left gripper**, keep pressing the baseplate down.
- Work the pairs in this order: gear 1 with gear 2, then gear 2 with gear 3, then gear 3 with gear 4.
- For each pair, with the **right gripper**, pinch the rim of the gear that is riding high and **rock**
  it until its teeth drop into its neighbour's gaps and the gear settles onto the plate.
- If neither gear of a pair is riding high, rock the right-hand gear of that pair a small amount anyway,
  to confirm both gears turn together.
- Rock with a light hand only. Do not turn a gear hard against a stop, and do not press a gear down the
  shaft to force it.
- Do not go on to the next pair until the current pair is meshed.

**Expected state:** all four gears sit flat on the baseplate at the same height, and turning any one gear
turns its neighbours.

**Check:** every gear is seated, every neighbouring pair is meshed, and no gear is riding high. If a gear
still rides high after rocking, lift it straight up off its shaft with the right gripper, turn it a small
amount in the air, and lower it back down, then rock it again.

### Step 4: Fit the four retaining caps

**Goal:** all four shaft tops carry a seated cap, and all four gears still turn freely.

- With the **left gripper**, keep pressing the baseplate down.
- Fit the caps in order: shaft 1, then shaft 2, then shaft 3, then shaft 4.
- With the **right gripper**, take one cap from the cap tray, hold it level over the shaft top, lower it
  straight down, and press it on until it stops.
- Press onto the shaft top only. Stop pressing as soon as the cap stops — do not push the cap down onto
  the gear.
- Carry one cap at a time. Do not set a cap on the plate or the table on the way.
- Release each cap before starting the next one.

**Expected state:** four caps on four shaft tops, cap tray empty, all four gears still flat on the plate.

**Check:** each cap is seated level and does not lift off, no cap is pressing on the gear below it, and
no gear was pushed out of mesh while its cap went on. If a cap sits crooked or lifts off, lower it
straight down and press it on again. If a cap was pressed onto its gear, pull the cap straight up with
the right gripper and refit it, stopping at the shaft top.

### Step 5: Spin-test the train and correct any bind

**Goal:** gear 1 drives all four gears through a full turn with nothing binding.

#### 5.1 Spin-test

- With the **left gripper**, keep pressing the baseplate down.
- With the **right gripper**, close the gripper and set its tip against one **tooth** of **gear 1**.
- Push that tooth sideways along the plate to drive gear 1 around. Lift the tip clear, set it on the next
  tooth, and push again.
- Keep pushing until gear 1 has made a **full turn**, so its mark comes back to where it started.
- While gear 1 turns, watch the **marks** on gears 2, 3, and 4. All three marks must move.
- Drive from gear 1 only. Do not drive the train from gear 2, 3, or 4, and do not grab a gear body and
  twist it.
- If gear 1 makes a full turn and all four marks moved, the train is good — skip 5.2 and go to Step 6.
- If gear 1 will not go any further, or one mark does not move, there is a **bind** — go to 5.2.

**Check:** gear 1 made a full turn, all four marks moved, all four caps are still seated, and the
baseplate is still on the assembly spot.

#### 5.2 Correct the bind

- Name the gear that binds: the first gear whose mark did not move, or the gear where gear 1 stops.
- With the **right gripper**, pull that gear's **cap** straight up off its shaft top and set it back in
  the cap tray.
- With the **right gripper**, lift that gear straight up off its shaft, turn it a small amount in the
  air, and lower it straight back down the shaft.
- With the **right gripper**, **rock** it until it meshes with both of its neighbours and sits flat on
  the plate.
- With the **right gripper**, take a cap from the cap tray and fit it on that shaft top as in Step 4.
- Never take a gear off while its cap is still on, and never pry a cap off sideways.
- Run 5.1 again from the start.
- If the same gear binds after two corrections, stop, end the episode at Step 6, and log the plate for a
  station check.

**Check:** the corrected gear is seated, meshed, and capped, and 5.1 then runs clean. If it does not,
count the correction and follow the two-correction rule above.

### Step 6: End the episode

**Goal:** recording ends with the four-gear train built and spin-tested.

1. Confirm all four gears are on their own shafts, seated flat and meshed, all four caps are seated, the
   gear tray and cap tray are empty, and the baseplate is still square on the assembly spot.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

1. With recording off, pull the four caps off the shaft tops by hand and put them back in the cap tray,
   opening-down.
2. Lift the four gears off their shafts and put each one back in its own numbered cell in the gear tray,
   number label and mark facing up. Set the tray in the start zone for the next episode's config —
   front-center, in front of the assembly spot (Config M), front-right (Config R1), or back-right, behind
   the cap tray (Config R2).
3. Set the baseplate square on the assembly spot, flat against the table.
4. Wipe any grit off the shafts and the gear teeth.
5. Inspect the parts. Replace a gear if a tooth is chipped, worn round, or bent. Replace a shaft if it is
   bent or burred at the top. Replace a cap if it no longer grips the shaft top or no longer holds its
   gear on. Replace the baseplate if a shaft is loose in it.
6. Run both Setup checklists before the next episode.

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

**Note on the start position:** the violations below were written for Config R1 (gear tray at the
front-right). The pickup and arm-role cues will be rewritten later to cover all three start positions; they
are left as they are for now. Until then, anything that does not match the episode's config goes under
**Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the gear tray is not
  in the start zone for the config; the left gripper leaves the plate to reach for a gear, or a gripper
  reaches across the table for one; or the wrong IF line is followed.
- **SOP rule broken:** the start position and the same-side rule (the right gripper takes every gear from
  the tray in its start zone in every config; no arm reaches across the table; the IF line followed is the
  one for the config on the table).
- **Coaching note:** look where the gear tray is before the first reach, then follow that config's IF line
  through Step 2.

**Violation: Baseplate not held**
- **Visible cue:** the left gripper is off the left edge of the baseplate while the right gripper seats,
  rocks, caps, or spin-tests, and the plate slides, lifts, or is chased across the spot.
- **SOP rule broken:** Step 1 (the left gripper presses the baseplate down by its left edge and holds it
  there through Steps 2–5).
- **Coaching note:** left gripper on the plate first, and leave it there until the episode ends.

**Violation: Baseplate moved off the assembly spot**
- **Visible cue:** the baseplate is lifted, turned, dragged, or ends the episode out of square with the
  front edge.
- **SOP rule broken:** Steps 1–5 (the baseplate stays flat and square on the assembly spot for the whole
  episode and is never lifted).
- **Coaching note:** bring the gear to the plate; never move the plate to the gear.

**Violation: Gears seated out of order**
- **Visible cue:** a gear goes on its shaft before a lower-numbered gear is on, for example gear 3 seated
  before gear 2.
- **SOP rule broken:** Step 2 (seat gear 1, then 2, then 3, then 4).
- **Coaching note:** work left to right in number order, one gear at a time.

**Violation: Gear on the wrong shaft**
- **Visible cue:** a gear's number does not match its shaft, two gears end up on one shaft, or a shaft is
  left bare.
- **SOP rule broken:** Step 2 (gear 1 on shaft 1 through gear 4 on shaft 4).
- **Coaching note:** read the number on the gear before you lower it.

**Violation: Gear dropped or released above the shaft**
- **Visible cue:** the right gripper opens above the shaft and the gear falls onto it, bounces, or lands
  off the shaft.
- **SOP rule broken:** Step 2 (lower each gear straight down the shaft and release it only once it stops).
- **Coaching note:** go all the way down the shaft before you open the gripper.

**Violation: Gear tilted on its shaft**
- **Visible cue:** a gear is lowered at an angle, or is left cocked on its shaft with one side high and
  one side low.
- **SOP rule broken:** Step 2 (keep each gear level going down the shaft, and do not tilt it onto the
  shaft).
- **Coaching note:** hold it flat over the shaft, then straight down.

**Violation: Gear mishandled on the way in**
- **Visible cue:** a gear is set on the table or on the plate on the way, two gears are carried at once,
  or a gear is picked up by its teeth instead of its rim.
- **SOP rule broken:** Step 2 (carry one gear at a time by its rim, straight from its cell to its shaft).
- **Coaching note:** one gear, by the rim, straight in.

**Violation: Gear forced onto the shaft**
- **Visible cue:** a gear stops part way down and the right gripper presses it, twists it hard, or works
  it down instead of letting go and moving on.
- **SOP rule broken:** Step 2 (do not press or twist a gear that stops; leave it riding high and go on to
  the next gear).
- **Coaching note:** a gear that stops is riding high, not stuck. Let go and mesh it in Step 3.

**Violation: Mesh step skipped**
- **Visible cue:** caps go on, or the spin test starts, while a gear is still riding high and sits above
  the others.
- **SOP rule broken:** Step 3 (all three pairs are meshed and all four gears sit flat on the plate before
  Step 4).
- **Coaching note:** look across the tops of the gears. They all sit at one height before any cap goes on.

**Violation: Pairs meshed out of order**
- **Visible cue:** the right gripper rocks gears 3 and 4 together before gears 1 and 2 or gears 2 and 3
  are meshed, or it jumps between pairs.
- **SOP rule broken:** Step 3 (mesh gear 1 with gear 2, then gear 2 with gear 3, then gear 3 with gear 4,
  finishing each pair before starting the next).
- **Coaching note:** left pair first and work right, one pair at a time.

**Violation: Gear forced instead of rocked**
- **Visible cue:** the right gripper turns a gear hard against a stop, presses a gear down its shaft, or
  the teeth grind or click loudly instead of the gear settling.
- **SOP rule broken:** Step 3 (rock the gear with a light hand so the teeth find the gaps).
- **Coaching note:** small turns each way and a light hand. The gear drops on its own.

**Violation: Caps fitted before the gears are meshed down**
- **Visible cue:** a cap goes onto a shaft top while any gear is still riding high or any pair is unmeshed.
- **SOP rule broken:** Steps 3 and 4 (all four gears are seated and meshed before the first cap goes on).
- **Coaching note:** mesh everything first, then cap.

**Violation: Caps fitted out of order**
- **Visible cue:** a cap goes on shaft 3 or shaft 4 before shafts 1 and 2 are capped.
- **SOP rule broken:** Step 4 (fit the caps on shaft 1, then 2, then 3, then 4).
- **Coaching note:** cap left to right, same as the gears went on.

**Violation: Cap not seated**
- **Visible cue:** a cap sits crooked, stands proud of the shaft top, lifts off when the right gripper
  lets go, or is left off a shaft entirely.
- **SOP rule broken:** Step 4 (lower each cap straight down and press it on until it stops, level and all
  the way down).
- **Coaching note:** straight down, press until it stops, then check it holds.

**Violation: Cap pressed down onto the gear**
- **Visible cue:** the right gripper keeps pressing after the cap stops, and the gear below is clamped and
  no longer turns when its neighbour turns.
- **SOP rule broken:** Step 4 (press onto the shaft top only and stop as soon as the cap stops; the gear
  below still turns freely).
- **Coaching note:** the cap holds the gear on, it does not hold the gear still. Stop at the shaft top.

**Violation: Cap mishandled**
- **Visible cue:** a cap is set on the plate or the table on the way, two caps are carried at once, or a
  cap is dropped and left where it fell.
- **SOP rule broken:** Step 4 (carry one cap at a time straight from the cap tray to the shaft top).
- **Coaching note:** one cap, straight from the tray to the shaft.

**Violation: Gear knocked out of mesh while capping**
- **Visible cue:** a gear lifts, turns, or rides up while its cap or a neighbour's cap goes on, and the
  step moves on anyway.
- **SOP rule broken:** Step 4 (no gear is pushed out of mesh while its cap goes on).
- **Coaching note:** press straight down on the shaft top so nothing shifts underneath.

**Violation: Spin test skipped or cut short**
- **Visible cue:** the episode ends without the right gripper driving gear 1, or gear 1 is nudged only
  part way and its mark never returns to where it started.
- **SOP rule broken:** Step 5.1 (drive gear 1 a full turn, until its mark comes back to where it started).
- **Coaching note:** a full turn of gear 1, every episode, before the ending.

**Violation: Spin test driven from the wrong gear or the wrong way**
- **Visible cue:** the right gripper drives the train from gear 2, 3, or 4, or grabs a gear body and
  twists it instead of pushing tooth by tooth on gear 1.
- **SOP rule broken:** Step 5.1 (set the closed gripper tip against a tooth of gear 1 and push it
  sideways, tooth by tooth; drive from gear 1 only).
- **Coaching note:** gear 1 only, tip on a tooth, push sideways.

**Violation: Bind left uncorrected**
- **Visible cue:** gear 1 stops, or one of the marks does not move, and the episode goes to the ending
  without a correction.
- **SOP rule broken:** Step 5.2 (a bind is corrected before the episode ends).
- **Coaching note:** watch all four marks. If one stays still, that gear comes off and goes back on.

**Violation: Bind corrected the wrong way**
- **Visible cue:** the right gripper forces the train round, pries a cap off sideways, or lifts a gear
  while its cap is still on.
- **SOP rule broken:** Step 5.2 (pull the cap straight up off the shaft top first, then lift the gear
  straight up; never force the train and never pry a cap sideways).
- **Coaching note:** cap off straight up, gear off straight up, turn it, back down, rock, re-cap.

**Violation: Correction not re-tested**
- **Visible cue:** a gear is reseated and re-capped, and the episode ends with no fresh full turn of
  gear 1.
- **SOP rule broken:** Step 5.2 (run 5.1 again from the start after every correction).
- **Coaching note:** every fix earns another full turn of gear 1.

**Violation: Wrong arm used**
- **Visible cue:** an action assigned to one gripper is done by the other, including the left gripper
  seating a gear, rocking a gear, fitting a cap, or driving the spin test, or the right gripper holding
  the baseplate down.
- **SOP rule broken:** Steps 1–5 (the right gripper seats the gears, rocks them into mesh, fits the caps,
  drives the spin test, and corrects a bind; the left gripper presses the baseplate down).
- **Coaching note:** right gripper does all the work on the plate, left gripper only holds it down.

**Violation: Part or supply knocked over**
- **Visible cue:** a gear, a cap, the gear tray, or the cap tray is dropped, tipped, pushed off its spot,
  or spilled onto the table or the floor.
- **SOP rule broken:** Steps 2–5 (keep the gears, caps, and both trays on their spots through the build).
- **Coaching note:** work slower and lower over the table, and keep carries short.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before the spin test passes, an arm is not home, a gripper is closed,
  or an arm does something else after homing.
- **SOP rule broken:** Step 6 (confirm the end state, return both arms home with grippers open as their
  final action, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than
tagging them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- A gear has a chipped or malformed tooth, so a correctly seated pair still binds.
- A shaft is bent or loose in the baseplate, so a correctly lowered gear cannot sit flat.
- A cap will not grip its shaft top, or grips so deep that it always touches the gear.
- The shafts are spaced wrong for the gears, so a pair cannot mesh however it is seated.

## Annotation subtasks (from SOP)

1. Press the baseplate flat and hold it with the left gripper
2. Seat gear 1 on shaft 1 and gear 2 on shaft 2
3. Seat gear 3 on shaft 3 and gear 4 on shaft 4
4. Mesh gear 1 with gear 2, then gear 2 with gear 3, then gear 3 with gear 4
5. Fit the retaining caps on shafts 1, 2, 3, and 4 in order
6. Drive gear 1 a full turn and watch all four marks
7. Correct a bind: uncap, lift, reseat, re-mesh, re-cap, and re-test
8. Confirm the end state, return both arms home, and end the episode
