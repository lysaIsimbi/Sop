# Mount a PCB on Standoffs SOP (1x Board)

One episode mounts one board. Work the four phases in this fixed order: **thread the four standoffs
into the plate, seat the board on the standoffs, drive the four screws, mate the two header plugs.**
The four positions, the two headers, the order of the phases, and every fixture but the board rest never
vary.

**This is a single-arm task.** Only the **right arm** works. The **left arm stays at home with its
gripper open for the whole episode** and touches nothing. Because there is no second gripper to hold
or steady anything, the fixtures do that job: the **base plate** is heavy and non-slip and stands on
its mark all episode, so every turn and every push goes straight down into the table instead of
shoving the plate sideways; the **standoff nest** and the **screw nest** hold each part upright so a
magnetic bit picks it straight up; the **cradle bar** holds each driver upright so the right gripper
lifts it already vertical; and once the board is on the standoffs, the standoffs carry the board, so
the screws and the plugs are pushed straight down and nothing is ever held. Nothing is held in the
air while something else is done to it.

The four **positions** are numbered on the plate: **1** back-left, **2** back-right, **3**
front-right, **4** front-left. Standoffs go in the order **1, 2, 3, 4**. Screws go in **diagonal
order: 1, 3, 2, 4**, so the board is pulled down evenly. The board goes on with its **key dot** at
the back-left, which puts **H1** and **H2** where the steps expect them.

The table is set up in one of three ways. Only the board, on its rest, moves; the base plate, the
standoff nest, the screw nest, the plug tray, and the cradle bar are in the same place in all three.

* **Config M1:** the board rest is at the front center, in front of the plate.
* **Config M2:** the board rest is at the back center, behind the plate.
* **Config R:** the board rest is at the far right, right of the screw nest, between the standoff nest
  and the cradle bar.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line
that matches.

What stays constant across all sessions:

* **Start position:** the board starts on its rest at the front center (**Config M1**), the back center
  (**Config M2**), or the far right (**Config R**). One config per episode, chosen before recording and
  never changed mid-episode.
* **Same-side rule:** this is a single-arm task, so the **right gripper** takes the board in all three
  configs and the config changes only the direction it reaches. No zone is left of the table's center
  line, because the left arm is parked and the right arm never leans across the center line. Nothing is
  handed over.
* **Fixed roles:** everything else is the same in all three configs — the four positions, the standoff
  order 1, 2, 3, 4, the diagonal screw order 1, 3, 2, 4, the key dot at the back-left, P1 into H1 then
  P2 into H2, and every fixture but the board rest on its usual mark.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** single_arm

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the standoff nest across the back right, the screw
   nest right of the plate, the base plate on its mark just right of the table's center line, the
   board rest in the zone for this episode's config, the plug tray in front of the plate, the cradle
   bar at the front right, and both arms.
3. The base plate is visible from above, so all four position numbers and all four tapped holes can
   be seen.
4. The base plate is visible from the front, so the gap under a standoff shoulder and the gap under
   the board can be seen.
5. The board is visible from above on its rest, so the key dot, the two grip zones, the four mounting
   holes, and both headers can be seen.
6. Both arms are at home with grippers open.
7. The table is bare apart from the base plate, the standoff nest, the screw nest, the board rest,
   the plug tray, the cradle bar, and robot hardware.
8. The right arm reaches all four holes in the plate, all four standoff nest holes, all four screw
   nest holes, both cradles, the board rest in its config zone (front center in Config M1, back center
   in Config M2, far right in Config R), and both plug slots without stretching and without leaning
   across the table's center line.
9. The left arm is at home, gripper open, and stays there.

### Materials checklist

1. One **base plate**, a flat metal plate with four **tapped holes**, one near each corner. The
   position number **1**, **2**, **3**, **4** is printed on the plate beside each hole and readable
   from above.
2. The base plate stands on the **assembly mark**, a taped outline just right of the table's center
   line, square to the front edge and flat on the table. It is heavy with a non-slip underside, so a
   standoff can be run down and a plug pushed in without the plate sliding or lifting. It is never
   gripped.
3. The plate is narrow enough that position 1, at its back-left corner, still sits right of the
   table's center line, so the right arm reaches all four holes without leaning across the table.
4. All four tapped holes are empty, clean, and undamaged at the start.
5. **Four hex standoffs**, all the same. Each is a metal pillar with six flat sides, a threaded
   **stud** on its bottom end and a threaded hole in its top end.
6. The four standoffs stand in the **standoff nest** across the back right, one per hole, **stud
   down, hex up**. The nest holes are numbered 1 to 4, left to right.
7. The standoff nest is a heavy block, so a standoff can be pulled straight up out of it without the
   block moving or tipping.
8. **Four machine screws**, all the same, with cross-head tops. They stand in the **screw nest**
   right of the plate, one per hole, **shank down, head up**, so each head stands proud of the block.
   The nest holes are numbered 1 to 4, left to right. The block is heavy and does not move when a
   screw is pulled out of it.
9. **Two electric drivers** stand upright in the **cradle bar** at the front right, each in its own V
   cradle: the **standoff driver** in the left cradle, the **screw driver** in the right cradle.
10. The **standoff driver** carries a **magnetic hex socket** that fits the flats of a standoff. The
    **screw driver** carries a **magnetic cross bit** that fits the screw heads. Neither bit is
    changed during an episode.
11. Both drivers are set to **forward, low speed, and the validated clutch setting** before the
    episode. Each has a broad **trigger paddle** on its body, set so the right gripper runs the
    driver by closing a little more once it is holding it.
12. The cradle bar is heavy and non-slip, and each V cradle holds its driver upright with the bit
    pointing down, so the right gripper closes on the driver body and lifts it out already vertical.
13. One **board**, a printed circuit board about the size of a postcard, with four **mounting holes**
    that line up with the four plate holes, a white **key dot** printed at one corner, and two
    **headers** standing on its top face.
14. **H1** is a **two-pin power header**, red, standing close to position 2. **H2** is a **four-pin
    signal header**, white, standing close to position 3. Both are shrouded, both openings face up,
    and each has a **notch** in the front wall of its shroud.
15. The board lies on the **board rest**, top face up, key dot at its back-left corner. Both mounting
    holes and both headers are clear of parts on the rest. The rest stands in the zone for this
    episode's config:
    - **Config M1:** front center, in front of the plate.
    - **Config M2:** back center, behind the plate.
    - **Config R:** far right, right of the screw nest, between the standoff nest and the cradle bar.
16. The board rest holds the board on two low rails, so both **grip zones** stand clear of the rest
    and the right gripper can close on them. The rest is heavy and does not move when the board is
    lifted off it.
17. Each **grip zone** is a bare strip marked at the middle of the board's left edge and the middle
    of its right edge, with no part standing on it.
18. **Two plugs** lie in the **plug tray**, in front of the plate and left of the cradle bar, in two
    numbered slots:
    slot 1 holds **P1**, the red two-pin plug; slot 2 holds **P2**, the white four-pin plug. Each is
    on a short lead with a plain cut end and each has a **key ridge** on one face.
19. Both plugs are straight on their leads, with no bent pin and no cracked shell. The plug tray is
    heavy and non-slip, so a plug can be lifted out without the tray moving.
20. Before collection, confirm by hand that:
    - each standoff runs down its plate hole with finger pressure, without force;
    - a standoff can be run fully down without the plate sliding or lifting;
    - the board drops over all four standoffs with the key dot at the back-left, and will not sit
      flat with the key dot anywhere else;
    - each screw runs down its standoff top by hand and stops solid;
    - each plug drops into its shroud one way only, and stops if the key ridge is turned the wrong
      way;
    - a mated plug holds a light pull.

### Workspace layout

Everything below is a fixed area of the table, judged by eye against the table edges, the taped
outline, and the fixtures standing on it. The areas sit in a short arc, all inside the right arm's
reach. Only the board rest has more than one place.

- **Back right, standoff nest:** four numbered holes, standoffs standing stud down, hex up.
- **Just right of center, assembly mark:** one taped outline. The base plate stands here and does
  not move.
- **Right of the plate, screw nest:** four numbered holes, screws standing head up.
- **Board rest, start zone:** the board on its rails, top face up, key dot at the back-left. The rest
  stands at the front center in front of the plate (**Config M1**), at the back center behind the
  plate (**Config M2**), or at the far right, right of the screw nest (**Config R**).
- **In front of the plate, left of the cradle bar, plug tray:** slot 1 holds P1, slot 2 holds P2.
- **Front right, cradle bar:** the standoff driver in the left cradle, the screw driver in the right
  cradle.

### Arm assignment

- **Right gripper, all of the work:** lifts each driver out of its cradle and runs it, picks each
  standoff onto the socket and runs it down, lifts the board off its rest and lowers it onto the
  standoffs, picks each screw onto the bit and drives it, and pushes both plugs into their headers. It
  takes the board from the front center in Config M1, from the back center in Config M2, and from the
  far right in Config R.
- **Left arm, parked:** stays at home with its gripper open from the start of recording to the end.
  It holds nothing, steadies nothing, and reaches for nothing.

## Vocabulary

- **Assembly mark:** the taped outline just right of the table's center line where the base plate
  stands. The plate stays inside it for the whole episode. A correctly placed plate shows a thin band
  of tape all the way around its edge.
- **Square:** the front edge of the base plate lines up with the front edge of the table, so neither
  end of the plate sits nearer the front.
- **Base plate:** the heavy metal plate with the four tapped holes. Its underside is non-slip, so it
  holds itself still while a standoff is run down or a plug is pushed in. It is never gripped and
  never lifted.
- **Position number:** the number printed on the plate beside each hole: **1** back-left, **2**
  back-right, **3** front-right, **4** front-left.
- **Diagonal order:** position 1, then the position across the plate from it, 3, then position 2,
  then the position across from it, 4. Written out: **1, 3, 2, 4**. Screws are driven in this order
  so the board is pulled down evenly.
- **Standoff:** a metal pillar with six flat sides. Its bottom end carries a threaded **stud** that
  goes into a plate hole. Its top end has a threaded hole that takes a screw.
- **Shoulder:** the flat bottom face of the standoff's six-sided body, the face that lands on the
  plate when the standoff is fully down.
- **Shoulder flat:** seen from the front, the shoulder sits on the plate with no gap showing under it
  anywhere around the standoff.
- **Standing straight:** seen from the front, the standoff looks upright against the plate, and its
  six-sided body is not leaning to either side.
- **Standoff nest:** the heavy block at the back right holding the four standoffs upright, stud down,
  hex up, ready for the socket to come down over them.
- **Screw nest:** the heavy block right of the plate holding the four screws upright, shank down,
  head up, so a head stands proud of the block.
- **Cradle bar:** the heavy holder at the front right with two V cradles, one per driver. A cradle
  holds its driver upright with the bit pointing down.
- **Driver vertical:** the bit points straight down and the driver body looks upright against the
  plate, not tilted.
- **Trigger paddle:** the broad pad on the driver's body. Once the right gripper is holding the
  driver, closing a little more presses the paddle and runs the bit. Opening a little stops it.
- **Held on the bit:** the standoff or the screw hangs from the magnet on its own, straight, with
  the right gripper clear of it and the driver lifted off the nest.
- **Clutch release:** the driver's clutch lets go and the bit stops turning the part even though the
  driver is still running. This is the signal to stop the driver.
- **Cross-threaded:** the standoff or the screw is turning while leaning, so it bites at an angle
  instead of running down straight. It goes stiff early and stands crooked.
- **Board:** the printed circuit board that is mounted. Its top face carries the parts and the two
  headers. Its bottom face is bare where it lands on the standoffs.
- **Key dot:** the white dot printed at one corner of the board. It goes at the **back-left**, over
  position 1.
- **Start zone:** where the board rest stands at the start of the episode — front center, in front of
  the plate (**Config M1**), back center, behind the plate (**Config M2**), or far right, right of the
  screw nest (**Config R**). One per episode, chosen before recording and never changed mid-episode.
- **Grip zone:** the bare strip marked at the middle of the board's left edge and the middle of its
  right edge. These two strips are the only places the right gripper closes on the board.
- **Mounting hole:** one of the four holes near the corners of the board. Each one drops over one
  standoff top.
- **Board seated:** all four standoff tops show through the four mounting holes, the board lies flat
  on all four shoulders, and it does not rock when the gripper opens.
- **Rocking:** the board tips down at one corner and lifts at another when it is released, which
  means one mounting hole is not down on its standoff.
- **Header:** one of the two shrouded connectors standing on the board's top face. **H1** is the red
  two-pin power header near position 2. **H2** is the white four-pin signal header near position 3.
- **Notch:** the cut in the front wall of a header shroud. It is what makes the plug go in one way
  only.
- **Key ridge:** the raised rib on one face of a plug. It faces the **front edge** and drops into the
  notch when the plug goes in.
- **Front edge:** the edge of the table nearest the collector. Both plugs are mated with their key
  ridge pointing this way.
- **Straight down:** the part comes down in line with what it goes into and does not lean, tilt, or
  come in from the side.
- **Fully seated plug:** the plug has gone as far into its shroud as it goes, with no gap showing
  between the bottom of the plug and the shroud face anywhere around it, and it stays there when the
  right gripper opens.
- **Light pull:** the right gripper takes the lead just above the plug and pulls straight up once,
  gently. A fully seated plug does not lift or come loose.
- **Stable placement:** the item stays still for 2 seconds after release and does not rock, roll,
  tip, or slide.
- **Parked arm:** the left arm, at home with its gripper open. It does not move during the episode.

## Steps

Only Step 2 depends on where the board rest stands: the **right gripper** takes the board from the front
center in Config M1, from the back center in Config M2, or from the far right in Config R, and carries
it to the plate from that side. Every other line in every step is the same in all three configs.

### Step 1: Thread the four standoffs into the plate

**Goal:** four standoffs stand straight in the four plate holes, each with its shoulder flat on the
plate.

Work the positions in this fixed order: **1, 2, 3, 4.** Hold the standoff driver in the **right
gripper** for the whole step. Do not put it back in its cradle between standoffs. Do not grip, lift,
or push the base plate at any point.

#### 1.1 Pick up the standoff driver

- With the **right gripper**, close on the body of the standoff driver in the left cradle, with a
  finger over the trigger paddle.
- Lift it straight up out of the cradle, keeping the bit pointing down.
- Do not press the trigger paddle yet.

**Check:** the driver is held vertical, the socket points straight down, and the socket is empty. If
the driver is leaning in the gripper, lower it back into its cradle, open the **right gripper**, and
pick it up again.

#### 1.2 Load one standoff onto the socket

- Move the driver over the standoff nest hole with the same number as the position being worked.
- Lower the driver straight down until the socket goes over the standoff's six flat sides and the
  magnet holds it.
- Lift the driver straight up until the standoff is clear of the nest.

**Check:** the standoff hangs from the socket, straight, stud pointing down. If it hangs crooked or
falls off, lower it back into its nest hole and pick it up again.

#### 1.3 Run the standoff down into its hole

- Move the driver over the plate hole with that position number, keeping the driver vertical.
- Lower the driver straight down until the stud enters the hole.
- Press the trigger paddle at low speed and run the standoff down.
- Stop the driver as soon as the clutch releases.
- Lift the driver straight up so the socket comes off the standoff.

**Check:** the standoff stands straight in its hole with its shoulder flat on the plate, and the
socket is now empty. If a gap shows under the shoulder, lower the socket back over the standoff and
run it down once more. If the standoff went stiff early and stands crooked, run the driver in reverse
to back it all the way out, stand it in its nest hole, and start that position again.

**Expected state:** the position just worked holds one standoff, standing straight, shoulder flat.
The base plate is still inside its mark.

**Repeat 1.2 and 1.3** for position 2, then position 3, then position 4. Finish one position before
starting the next.

#### 1.4 Put the standoff driver back

- With the **right gripper**, carry the driver back to the left cradle.
- Lower it straight into the cradle, bit down, and release it when it is stable.

**Check:** all four standoffs stand straight with their shoulders flat, and the driver stands upright
in its left cradle. The standoff nest is empty.

### Step 2: Seat the board on the standoffs

**Goal:** the board sits flat on all four standoffs, key dot at the back-left, not rocking.

Look where the board rest is before reaching for the board.

- **IF the board rest is at the front center (Config M1):** with the **right gripper**, close on the
  board at its two grip zones, one jaw on each, lift it straight up off its rest, flat and level, and
  carry it straight back over the plate.
- **IF the board rest is at the back center (Config M2):** with the **right gripper**, close on the
  board at its two grip zones, one jaw on each, lift it straight up off its rest, flat and level, and
  carry it straight forward over the plate.
- **IF the board rest is at the far right (Config R):** with the **right gripper**, close on the board
  at its two grip zones, one jaw on each, lift it straight up off its rest, flat and level, and carry it
  left over the screw nest and over the plate, high enough to clear the screw heads.

Then, in all three:

- Do not close on the top face, on a header, or on any part.
- Do not tilt the board and do not pass it low over the standoff tops.
- Turn the board over the plate until the key dot is at the back-left, over position 1.
- Line up the four mounting holes with the four standoff tops.
- Lower the board straight down until all four standoff tops come through the mounting holes and the
  board lands on the four shoulders.
- Release the board and lift the gripper clear.

**Check:** all four standoff tops show through the four mounting holes, the key dot is at the
back-left, and the board lies flat and does not rock. If the board rocks, or a standoff top does not
show through its hole, close the **right gripper** on the grip zones again, lift the board straight
up clear of the standoffs, and lower it back down. Do not slide the board across the standoff tops
and do not press it down.

**Expected state:** the board sits on the four standoffs with H1 near position 2 and H2 near position
3, both header openings facing up. The board rest is bare. The base plate is still inside its mark.

### Step 3: Drive the four screws

**Goal:** four screws are driven down into the four standoff tops, each head flat on the board, with
the board still lying flat.

Work the positions in **diagonal order: 1, 3, 2, 4.** Hold the screw driver in the **right gripper**
for the whole step. Do not put it back in its cradle between screws. Do not hold, press, or steady
the board with the gripper at any point. The standoffs carry it.

#### 3.1 Pick up the screw driver

- With the **right gripper**, close on the body of the screw driver in the right cradle, with a
  finger over the trigger paddle.
- Lift it straight up out of the cradle, keeping the bit pointing down.
- Do not press the trigger paddle yet.

**Check:** the driver is held vertical, the cross bit points straight down, and the bit is empty. If
the driver is leaning in the gripper, lower it back into its cradle, open the **right gripper**, and
pick it up again.

#### 3.2 Load one screw onto the bit

- Move the driver over the screw nest hole with the same number as the position being worked.
- Lower the driver straight down onto the screw head until the magnet holds it.
- Lift the driver straight up until the screw is clear of the nest.

**Check:** the screw hangs from the bit, straight, shank pointing down. If it hangs crooked or falls
off, stand it back in its nest hole and pick it up again.

#### 3.3 Drive the screw

- Move the driver over the mounting hole at that position, keeping the driver vertical.
- Lower the driver straight down until the screw tip enters the mounting hole and meets the standoff
  top.
- Press the trigger paddle at low speed and drive the screw down.
- Stop the driver as soon as the clutch releases.
- Lift the driver straight up so the bit comes off the screw head.

**Check:** the screw head sits flat on the board with no gap under it and no tilt, the board still
lies flat, and the bit is now empty. If a gap shows under the head, lower the bit back onto the screw
and drive once more. If the screw went stiff early and stands crooked, run the driver in reverse to
back it all the way out, stand it in its nest hole, and start that position again.

**Expected state:** the position just worked holds one driven screw. The board still lies flat on all
four standoffs and has not turned.

**Repeat 3.2 and 3.3** for position 3, then position 2, then position 4. Finish one position before
starting the next.

#### 3.4 Put the screw driver back

- With the **right gripper**, carry the driver back to the right cradle.
- Lower it straight into the cradle, bit down, and release it when it is stable.

**Check:** four screws are driven, one at each position, every head flat on the board, and the driver
stands upright in its right cradle. The screw nest is empty.

### Step 4: Mate the two header plugs

**Goal:** both plugs are fully seated in their own headers, key ridge toward the front edge, and both
hold a light pull.

Mate them in this fixed order: **P1 into H1, then P2 into H2.** Do not grip, lift, or push the board
or the base plate.

#### 4.1 Mate P1 into H1

- With the **right gripper**, close on the body of P1 in plug tray slot 1. Do not close on its lead.
- Lift it straight up out of the slot.
- Carry it over H1, the red two-pin header near position 2. Do not pass it over H2.
- Turn the plug until its key ridge faces the front edge, in line with the notch in the front wall of
  the shroud.
- Lower it straight down into the shroud and push down until the bottom of the plug sits on the
  shroud face all the way around.
- Release the plug and lift the gripper clear.

**Check:** the plug is fully seated, with no gap showing between the bottom of the plug and the
shroud face anywhere around it. Then give it a light pull: with the **right gripper**, take the lead
just above the plug and pull straight up once, gently, then release. The plug does not lift. If a gap
shows, or if the plug lifts on the pull, close the **right gripper** on the plug body and push
straight down again. If the plug will not go down, lift it clear, turn the key ridge to the front
edge, and lower it again. Do not push a leaning plug.

#### 4.2 Mate P2 into H2

- With the **right gripper**, close on the body of P2 in plug tray slot 2. Do not close on its lead.
- Lift it straight up out of the slot.
- Carry it over H2, the white four-pin header near position 3. Do not pass it over H1.
- Turn the plug until its key ridge faces the front edge, in line with the notch in the front wall of
  the shroud.
- Lower it straight down into the shroud and push down until the bottom of the plug sits on the
  shroud face all the way around.
- Release the plug and lift the gripper clear.

**Check:** the plug is fully seated, with no gap showing between the bottom of the plug and the
shroud face anywhere around it. Then give it a light pull the same way. The plug does not lift. If a
gap shows, or if the plug lifts on the pull, close the **right gripper** on the plug body and push
straight down again. If the plug will not go down, lift it clear, turn the key ridge to the front
edge, and lower it again.

**Expected state:** both plugs stand fully seated in their own headers, key ridges toward the front
edge, both leads lying clear of the screws. The plug tray is empty.

### Step 5: End the episode

**Goal:** recording ends with the board mounted and both headers connected.

1. Confirm the end state:
   - four standoffs stand straight in positions 1 to 4, each with its shoulder flat on the plate;
   - the board sits flat on all four standoffs with its key dot at the back-left, not rocking;
   - four screws are driven, one at each position, every head flat on the board;
   - P1 is fully seated in H1 and P2 is fully seated in H2, both key ridges toward the front edge;
   - the standoff nest, the screw nest, and the plug tray are all empty;
   - both drivers stand upright in their own cradles;
   - the base plate is still inside its mark and the board rest is bare;
   - no standoff, screw, or plug is loose on the table.
2. Return the right arm home with its gripper open. The left arm is already home. Homing is the last
   thing the arm does.
3. Stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Pull P2 out of H2, then P1 out of H1. Lay P1 in plug tray slot 1 and P2 in slot 2.
2. Set the screw driver to reverse and back the four screws out in the order 4, 2, 3, 1. Stand each
   screw head up in its own screw nest hole.
3. Stand the board rest in the start zone for the next episode's config — front center (Config M1),
   back center (Config M2), or far right (Config R). Lift the board off the standoffs and lay it on the
   board rest, top face up, key dot at the back-left, both grip zones clear of the rails.
4. Set the standoff driver to reverse and back the four standoffs out in the order 4, 3, 2, 1. Stand
   each standoff stud down, hex up, in its own standoff nest hole.
5. Return both drivers to forward, low speed, and the validated clutch setting, and stand each one
   upright in its own cradle.
6. Wipe the plate holes, the standoff studs, the standoff tops, the screws, and both bits clean and
   dry.
7. Stand the base plate inside its mark, square to the front edge, with a thin band of tape showing
   all the way around it.
8. Clear away anything loose on the table.
9. Check the assembly mark and re-tape it if it is lifting, torn, or unreadable.
10. Inspect the plate holes, standoffs, screws, board, headers, plugs, both bits, and every fixture
    for damage. Replace damaged items.
11. Run both Setup checklists again.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

- the **start timestamp** in the video;
- the **violation name** from the list below; and
- the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an
annotation label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain several violations; tag each
one separately. Retain the episode in training data with its violation tags. Do not delete a recorded
episode solely because it contains a violation.

### Violations

**Note on the start position:** the violations below were written for Config M1 (board rest at the front
center, in front of the plate). The pickup and arm-role cues will be rewritten later to cover all three
start positions; they are left as they are for now. Until then, anything that does not match the
episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

- **Visible cue:** what the operator does does not match the config on the table — the board rest is
  not in the start zone for the config; the right gripper reaches across the table's center line for
  the board, or the left arm reaches for it; or the wrong IF line is followed.
- **SOP rule broken:** the start position and the same-side rule (the board rest stands at the front
  center, the back center, or the far right for the whole episode; the right gripper takes the board
  from that zone and no arm reaches across the table; the IF line followed is the one for the config
  on the table).
- **Coaching note:** look where the board rest is before the first reach, then follow that config's IF
  line through Step 2.

**Violation: Wrong phase order**

- **Visible cue:** the board goes on before all four standoffs are in, a screw is driven before the
  board is seated, a plug is mated before all four screws are driven, or a standoff is added after
  the board is on the plate.
- **SOP rule broken:** Steps 1 to 4, work the four phases in the fixed order: all four standoffs,
  then the board, then all four screws, then the two plugs.
- **Coaching note:** finish each phase and its check before starting the next one.

**Violation: Wrong standoff order**

- **Visible cue:** a standoff is run down at a higher-numbered position while a lower-numbered
  position is still empty, for example position 3 before position 2.
- **SOP rule broken:** Step 1, the standoffs go in the order 1, 2, 3, 4.
- **Coaching note:** read the number printed beside the hole before lowering the socket, whichever
  hole is nearest.

**Violation: Wrong screw order**

- **Visible cue:** the four screws are driven in any order other than 1, 3, 2, 4. Most often that is
  straight around the plate, 1, 2, 3, 4.
- **SOP rule broken:** Step 3, the screws are driven in diagonal order 1, 3, 2, 4.
- **Coaching note:** after each screw, go to the position across the plate. Straight around pulls the
  board down crooked.

**Violation: Driver picked up or held wrong**

- **Visible cue:** the right gripper drags a driver out of its cradle sideways, holds it leaning so
  the bit is not pointing straight down, closes on the bit end instead of the body, presses the
  trigger paddle before the bit is over a part, or puts a driver back in its cradle part way through
  its phase.
- **SOP rule broken:** Steps 1.1, 1.4, 3.1 and 3.4 (lift the driver straight up out of its cradle,
  hold it vertical, keep it in the gripper for the whole phase, and cradle it only at the end).
- **Coaching note:** straight up out of the V, bit down, and it stays in the gripper until that phase
  is finished.

**Violation: Part not held on the bit before the driver moves**

- **Visible cue:** a driver moves toward the plate with an empty socket or bit; or a standoff or
  screw hangs crooked, swings loose, or falls off on the way across.
- **SOP rule broken:** Steps 1.2 and 3.2 (lower the driver straight down onto the part, let the
  magnet take it, lift it clear of the nest, and confirm it hangs straight).
- **Coaching note:** look at the part hanging on the bit before moving. If it hangs crooked, put it
  back and pick it up again.

**Violation: Part started crooked or forced**

- **Visible cue:** a standoff or a screw is turning while leaning, goes stiff early, stops moving
  down, or the bit slips and keeps turning, and the driver keeps running.
- **SOP rule broken:** Steps 1.3 and 3.3 (keep the driver vertical, enter the hole straight down, and
  back a crooked part all the way out instead of driving it).
- **Coaching note:** stop the driver the moment it goes stiff or the part leans. Reverse it out, then
  start that position again.

**Violation: Standoff not fully down**

- **Visible cue:** the episode moves on with a gap showing under a standoff shoulder, or with a
  standoff standing crooked in its hole.
- **SOP rule broken:** Step 1.3 (run the standoff down until its shoulder is flat on the plate, and
  run it again if a gap shows).
- **Coaching note:** look at the shoulder from the front after every standoff, not from above.

**Violation: Driver kept running past the clutch**

- **Visible cue:** the clutch releases and the trigger paddle stays pressed, so the bit keeps
  slipping on a standoff or a screw head; or the board visibly bends under a screw as it is driven.
- **SOP rule broken:** Steps 1.3 and 3.3 (stop the driver as soon as the clutch releases).
- **Coaching note:** the clutch is the signal to stop. Nothing is gained by holding on.

**Violation: Board gripped wrong**

- **Visible cue:** the right gripper closes on the board's top face, on a header, on a part, on a
  corner, or anywhere other than the two marked grip zones.
- **SOP rule broken:** Step 2, close on the board at its two grip zones, one jaw on each.
- **Coaching note:** the two bare strips at the middle of the side edges, every time. Nothing else on
  the board is a handle.

**Violation: Board put on the wrong way round**

- **Visible cue:** the board is lowered onto the standoffs with the key dot anywhere but the
  back-left, so H1 and H2 end up away from the positions the steps name.
- **SOP rule broken:** Step 2, the board goes on with its key dot at the back-left, over position 1.
- **Coaching note:** turn the board over the plate and check the dot before lowering it.

**Violation: Board lowered or moved wrong**

- **Visible cue:** the board is dropped onto the standoffs from height, lowered tilted, slid or
  dragged across the standoff tops, pushed sideways to line up the holes, or carried low enough to
  clip a standoff top.
- **SOP rule broken:** Step 2 (line the four mounting holes up over the standoff tops, then lower the
  board straight down, flat and level).
- **Coaching note:** line it up in the air first, then come straight down. Never slide it into place.

**Violation: Board not seated**

- **Visible cue:** the episode moves on to Step 3 with the board rocking, with a standoff top not
  showing through its mounting hole, or with the board sitting on top of a standoff instead of over
  it.
- **SOP rule broken:** Step 2 (all four standoff tops show through the mounting holes and the board
  lies flat and does not rock before a screw is driven).
- **Coaching note:** open the gripper and look. A rocking board means one hole missed its standoff.

**Violation: Board held or pressed while screws are driven**

- **Visible cue:** the right gripper presses down on the board, holds an edge, or leans the driver
  body against the board while a screw is driven.
- **SOP rule broken:** Step 3, the standoffs carry the board. The gripper holds the driver and
  nothing else.
- **Coaching note:** if the board seems to need holding down, it is not seated. Go back and reseat
  it, do not press it.

**Violation: Screw head not flat**

- **Visible cue:** the episode moves on with a gap showing under a screw head, or with a screw head
  sitting tilted on the board.
- **SOP rule broken:** Step 3.3 (drive until the head sits flat on the board with no gap and no
  tilt).
- **Coaching note:** look along the board after every screw. A tilted head means the screw went in
  crooked.

**Violation: Wrong plug in a header**

- **Visible cue:** the red two-pin plug is pushed at the white four-pin header, or the white four-pin
  plug is pushed at the red two-pin header; or P2 is mated before P1.
- **SOP rule broken:** Step 4, P1 goes into H1 first, then P2 goes into H2.
- **Coaching note:** match the color and the pin count before lifting the plug out of its slot.

**Violation: Plug turned the wrong way**

- **Visible cue:** a plug is lowered or pushed with its key ridge facing the back, the left, or the
  right instead of the front edge, or is forced onto a shroud it will not enter.
- **SOP rule broken:** Steps 4.1 and 4.2 (turn the plug so its key ridge faces the front edge, in
  line with the notch in the front wall).
- **Coaching note:** ridge to the front, then down. If it will not go, lift it clear and turn it, do
  not push harder.

**Violation: Plug pushed in wrong**

- **Visible cue:** a plug is brought in from the side, lowered leaning, rocked from end to end, or
  the right gripper closes on the lead instead of the plug body to push it.
- **SOP rule broken:** Steps 4.1 and 4.2 (hold the plug by its body and push it straight down into
  the shroud).
- **Coaching note:** hold the body, come straight down, one push.

**Violation: Plug not fully seated**

- **Visible cue:** the episode moves on with a gap showing between the bottom of a plug and its
  shroud face, or a plug lifts on the light pull and is left as it is.
- **SOP rule broken:** Steps 4.1 and 4.2 (push until the plug sits on the shroud face all the way
  around, and push again if it lifts on the light pull).
- **Coaching note:** look all the way around the plug, then pull once. Both, every time.

**Violation: Fixture moved**

- **Visible cue:** the base plate shifts off its taped mark, or is gripped, lifted, or pushed; or the
  standoff nest, the screw nest, the plug tray, the board rest, or the cradle bar is pushed, dragged,
  or knocked out of place.
- **SOP rule broken:** Steps 1 to 4, the base plate stays inside its mark and every fixture stays
  where it is. None of them is ever gripped or pushed.
- **Coaching note:** come down onto a hole or a nest from straight above, and do not lean the gripper
  or the driver body against a fixture.

**Violation: Parked arm moved**

- **Visible cue:** the left arm leaves home, its gripper closes, or it reaches toward, holds, or
  steadies anything at any point in the episode.
- **SOP rule broken:** Steps 1 to 5, this is a single-arm task. The left arm stays at home with its
  gripper open from the start of recording to the end.
- **Coaching note:** the fixtures do the holding. If a step feels like it needs a second gripper,
  stop and report the fixture, do not use the left arm.

**Violation: Item dropped or knocked over**

- **Visible cue:** a standoff, screw, plug, board, or driver falls from the right gripper onto the
  table or the floor; a standoff is knocked over in its nest; a driver is knocked out of its cradle;
  or a dropped item is left where it fell.
- **SOP rule broken:** Steps 1 to 4 (lift each item clear, carry it on the path its step names, and
  release it only when it is stable).
- **Coaching note:** lift higher over the plate and the nests, and slow the carry near a fixture.

**Violation: Finished work disturbed later**

- **Visible cue:** a seated standoff is turned, knocked, or backed out during a later step; a driven
  screw is bumped or re-driven for no reason; the seated board is turned or lifted after Step 2; or a
  mated plug is pulled part way out while the other one is worked.
- **SOP rule broken:** Steps 2 to 5, once a standoff, the board, a screw, or a plug is in place it
  stays there, untouched, for the rest of the episode.
- **Coaching note:** route the arm around the finished corners and around a mated plug once a phase
  is done.

**Violation: Check skipped**

- **Visible cue:** the right arm moves straight on with no look at the step's end state: no look at
  the part hanging on the bit, no look at the shoulder after a standoff, no look under the board
  after seating it, no look under a screw head, or no light pull after a plug.
- **SOP rule broken:** Steps 1 to 4, each step's check is done before the next step starts.
- **Coaching note:** every step ends with a look, and the fix happens in that step, not later.

**Violation: Wrong episode ending**

- **Visible cue:** the episode ends with a standoff crooked or not fully down, the board rocking or
  the wrong way round, a screw missing or not flat, a plug unmated or part seated, a nest or tray not
  empty, a driver out of its cradle, or a loose part on the table; or the right arm is away from
  home, a gripper is closed, or an arm makes a correction after homing.
- **SOP rule broken:** Step 5 (confirm the end state, return the right arm home with its gripper
  open, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arm does.

### Non-violation failures

Failures that are not caused by how the task was run do not go in the violation set. Log them as
system issues, discard the episode, and do not use them for coaching.

- **Recording stopped or paused during the episode** (recording system).
- **Camera dropped frames or lost feed** (capture system).
- **Hardware fault on an arm:** gripper failure, drift, collision caused by controller error, or
  motor error.
- **Driver fault:** a driver that will not run, a clutch that does not release, a magnet that will
  not hold a sound part, or a bit that is worn round.
- **Defective item:** a stripped plate hole, a standoff with a damaged stud or top, a screw with a
  chewed head, a board with an out-of-place mounting hole or a cracked header shroud, a plug with a
  bent pin or cracked shell, a fixture that slides on its own, or a taped outline that lifts off the
  table during the episode. Replace before the next episode.

## Annotation subtasks (from SOP)

1. Pick up the standoff driver from its cradle
2. Load one standoff onto the socket
3. Run one standoff down into its plate hole
4. Cradle the standoff driver
5. Lift the board off its rest and lower it onto the standoffs
6. Pick up the screw driver from its cradle
7. Load one screw onto the bit
8. Drive one screw into its standoff top
9. Cradle the screw driver
10. Mate one plug into its header
11. Light-pull one mated plug
12. Return the right arm home and end the episode
