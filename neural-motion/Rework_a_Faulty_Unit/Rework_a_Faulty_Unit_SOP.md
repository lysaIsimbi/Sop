# Rework a Faulty Unit SOP (Open, Swap, Reseat, Close, Retest, Relabel)

This SOP covers reworking one faulty unit using a two-arm robot system: the enclosure is opened, the
component named on the fault tag is swapped for a good one, every connector in the unit is reseated, the
enclosure is closed to torque, the unit is retested at the test station, and it is relabelled as
reworked. Both arms are used throughout: the grippers cooperate to hold the unit, back out the screws,
unmate and mate connectors and drive the lid down, with the left and right grippers taking the specific
roles called out in each step. The task runs from a tagged faulty unit in the start zone to a closed,
retested and relabelled unit in the output zone.

The table is set up in one of three ways. Only the faulty unit moves; the parts tray, the quarantine tray,
the torque driver, the label sheet, the test station and the working area are in the same place in all
three.

- **Config L:** the faulty unit is at the back-left.
- **Config M:** the faulty unit is at the front-centre, in front of the working area.
- **Config R:** the faulty unit is at the back-right, so the reworked unit is staged at the back-left
  instead.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

- **Start position:** the faulty unit starts at the back-left (**Config L**), the front-centre
  (**Config M**) or the back-right (**Config R**). One config per episode, chosen before recording and never
  changed mid-episode.
- **Same-side rule:** the gripper on the unit's side picks it — the left gripper in Config L and M, the
  right gripper in Config R. No arm reaches across the table.
- **Fixed roles:** once the unit is in the working area every gripper role in Steps 2 to 8 is the same in
  all three configs. The output zone is the back-right, except in Config R where it is the back-left.
- **One unit at a time:** exactly one unit is open on the table at any moment. The unit in hand is
  closed, retested and relabelled before the next one is picked.
- **Working position:** the unit is always moved to the centre of the table before the lid is opened, and
  it keeps its **front panel facing the operator** through every later step.
- **De-energised first:** the unit is powered down and unplugged from the test dock before the first
  screw is touched, and it is not reconnected until the enclosure is closed.
- **The fault tag governs:** only the component named on the **fault tag** is swapped. No other component
  is removed, resoldered, reworked or substituted.
- **Reseat means every connector:** every connector inside the unit is unmated and re-mated, not only the
  ones on the swapped component.
- **Screws live in the screw cup:** the four lid screws go straight into the screw cup when they come out
  and come straight back from it when the lid goes on. Screws are never set loose on the table or inside
  the enclosure.
- **Cross pattern:** the four screws are always worked in the same cross order: near-left, far-right,
  far-left, near-right, loosened in reverse on opening and torqued in a seating pass then a final pass on
  closing.
- **Retest before relabel:** the rework label goes on only after the test station has shown a **pass**
  for that unit. A unit that fails retest is quarantined, never relabelled.
- **The removed part is quarantined:** the faulty component goes straight into the quarantine tray. It
  never returns to the parts tray or into another unit.

## Setup

Go through both checklists before starting the episode.

### Hardware checklist

- Cameras are on and recording
- Env camera frame includes the front and back edges of the table and is centered on the table's
    midpoint
- Env camera frame includes the test station dock and both its pass and fail lamps
- Both arms are at the home position with grippers open
- Both arms are bonded to the ESD mat and the mat is connected to the bench ground point
- Table surface is clear of any objects other than the faulty unit(s) and the trays

### Materials checklist

- Faulty unit(s) to be reworked are placed in the start zone for this episode's config, lid up, front
    panel toward the operator, one unit per rework
    - **Config L:** back-left
    - **Config M:** front-centre, in front of the working area, between the two trays
    - **Config R:** back-right, clear of the torque driver
- Every unit carries a legible **fault tag** naming one flagged component by reference designator,
    and the unit is powered down and unplugged
- The parts tray is at the **front-left** and holds one replacement component in its ESD bag, the
    empty screw cup, and two spare screws
- The replacement component's part number matches the flagged component on the fault tag
- The quarantine tray is at the **front-right**, empty, with its reject bag open
- The torque driver is at the right edge with the hex bit fitted, and it matches the screw heads
- The label sheet is at the right edge, next to the torque driver, with rework labels face up
- The test station is at the back-center, powered on, dock empty, both lamps dark
- Center of the table is clear (working area for opening, swapping, reseating and closing)
- The output zone is clear (reworked unit / row): back-right (Config L and M) or back-left (Config R)

## Workspace layout

- **Start zone**: tagged faulty unit(s) (input) — back-left (Config L), front-centre (Config M) or
  back-right (Config R)
- **Center**: working area (open, swap, reseat, close)
- **Front-left**: parts tray (replacement component, screw cup, spare screws)
- **Front-right**: quarantine tray (the removed faulty component)
- **Right edge**: torque driver and rework label sheet
- **Back-center**: test station (retest dock, pass lamp, fail lamp)
- **Output zone**: reworked unit / row of reworked units (output) — back-right in Config L and M,
  back-left in Config R

## Vocabulary

These are the terms used in this SOP. Operators and annotators must use this language consistently. One
term per concept, used throughout.

### Unit anatomy

- **Unit:** one assembled product in its enclosure, the thing being reworked.
- **Faulty unit:** a unit that has failed test and carries a fault tag naming one component.
- **Reworked unit:** a unit that has been swapped, reseated, closed, retested to a pass and relabelled.
- **Enclosure:** the base and lid together, the shell that closes around the unit.
- **Base:** the lower half of the enclosure that holds the board and the components.
- **Lid:** the flat cover that closes the base and carries no wiring of its own.
- **Sealing face:** the flat rim on top of the base wall that the lid presses against.
- **Front panel:** the outside wall of the base that faces the operator. Labels go here.
- **Label zone:** the flat rectangle on the front panel that a label is aimed at.
- **Serial label:** the printed unit serial already on the front panel. It always stays on.
- **Fault tag:** the card tied to a faulty unit naming the one flagged component and the failure.
- **Screw boss:** one of the four threaded posts at the corners of the base.
- **Clearance hole:** one of the four holes at the corners of the lid that a screw passes through.
- **Near-left corner:** the screw boss closest to the operator on the left. Torque starts here.
- **Far-left corner:** the screw boss farthest from the operator on the left.
- **Far-right corner:** the screw boss farthest from the operator on the right.
- **Near-right corner:** the screw boss closest to the operator on the right. Torque ends here.
- **Lid gap:** the visible slot between the underside of the lid and the sealing face.

### Component anatomy

- **Component:** one replaceable module inside the base, held on a mount and wired by connectors.
- **Flagged component:** the one component named on the fault tag. It is the only part swapped.
- **Replacement component:** the good component from the parts tray that goes in its place.
- **Removed component:** the flagged component once it is out of the unit. It is quarantined.
- **Reference designator:** the printed code on the board that names a component position, such as U4.
- **Part number:** the printed code on a component that says which part it is.
- **Mount:** the clip, bracket or pair of standoffs that holds a component down in the base.
- **Standoff:** a threaded or snap post the component sits on, holding it clear of the board.
- **Retaining clip:** the sprung tab that latches a component onto its mount.
- **Seated component:** a component sitting flat on its mount with its clip latched and no rock.

### Connector anatomy

- **Connector:** one mating pair inside the unit: a plug on the harness and a header on the board.
- **Plug:** the moving half of a connector, on the end of a harness.
- **Header:** the fixed half of a connector, mounted on the board or on a component.
- **Latch:** the sprung tab on a plug that locks it to its header. It is pressed to unmate.
- **Key:** the moulded rib and slot that let a plug enter its header one way only.
- **Mated:** plug and header pushed together.
- **Fully seated:** mated all the way home, latch closed, with no gap showing between the two bodies.
- **Partially mated:** plug started into its header but not home, usually with the latch still open.
- **Click:** the sound and small release felt as a latch closes at full seat.
- **Harness:** the bundle of wires running between connectors inside the unit.
- **Service loop:** the slack left in a harness so a connector can be reached without tension.
- **Pinched harness:** a wire trapped between the lid and the sealing face when the enclosure closes.
- **Connector list:** the fixed order in which the unit's connectors are reseated, printed on the fault
  tag.

### Hardware and tool anatomy

- **Screw:** one of the four corner fasteners that hold the lid to the base.
- **Screw head:** the socketed top of a screw, the part the hex bit sits in.
- **Screw cup:** the small cup in the parts tray that holds the four screws while the unit is open.
- **Torque driver:** the tool that turns a screw to a set torque and clicks when it reaches it.
- **Hex bit:** the tip fitted to the torque driver that matches the screw head.
- **Seating pass:** the first pass over all four screws at half the final torque setting.
- **Final pass:** the second pass over all four screws at the full torque setting.
- **Hand-start:** a screw turned in by hand two to three turns, head still standing proud.
- **Cross-threaded:** a screw that has entered its boss at an angle and binds.
- **Cross pattern:** the corner order near-left, far-right, far-left, near-right.

### Test and label anatomy

- **Test station:** the fixture at the back-center that powers a unit and calls a pass or a fail.
- **Dock:** the cradle on the test station that a unit is lowered into for retest.
- **Test lead:** the flying lead on the station that plugs into the unit's front panel port.
- **Pass lamp:** the green lamp on the station, lit only when the unit has passed.
- **Fail lamp:** the red lamp on the station, lit when the unit has failed.
- **Retest:** the test run on a unit after rework, the one that decides pass or quarantine.
- **Rework label:** the printed sticker that marks a unit as reworked. It goes below the serial label.
- **Quarantine tray:** the front-right tray holding removed faulty components and failed units.

### Workspace zones

- **Start zone:** where the tagged faulty units lie at the start of the episode — back-left (**Config L**),
  front-centre (**Config M**) or back-right (**Config R**). One per episode, chosen before recording and
  never changed mid-episode.
- **Working area:** the center of the table where opening, swapping, reseating and closing happen.
- **Front-left tray:** the parts tray holding the replacement component, the screw cup and the spares.
- **Front-right tray:** the quarantine tray for removed components and failed units.
- **Right edge:** the rest position for the torque driver and the label sheet.
- **Back-center station:** the test station with its dock, test lead and pass and fail lamps.
- **Output zone:** where the reworked unit is placed — the back-right of the table, or the back-left in
  Config R.
- **Home position:** the default resting pose for each arm: gripper open and clear of the table.

### Actions

- **Pick:** lift one unit clear of the start zone and carry it to the working area.
- **Open:** back the four screws out and lift the lid straight off the base.
- **Unmate:** press a latch and draw a plug straight out of its header.
- **Mate:** push a plug straight into its header until the latch clicks and it is fully seated.
- **Reseat:** unmate a connector and mate it again to a full seat.
- **Swap:** take the flagged component out and put the replacement component in its place.
- **Quarantine:** place the removed component, or a failed unit, in the front-right tray.
- **Close:** place the lid, hand-start all four screws and torque them in the cross pattern.
- **Retest:** dock the unit at the test station, run the test, and read the pass or fail lamp.
- **Relabel:** apply one rework label to the label zone below the serial label.
- **Stage:** place the reworked unit in the output zone (batch sessions place them in a row).

## Steps

Steps 1 and 9 depend on where the faulty unit starts: in Config L and M the **left gripper** picks it from
the back-left or the front-centre; in Config R the **right gripper** picks it from the back-right and the
reworked unit is staged at the back-left. Every other line, Steps 2 to 8 and Step 10, is the same in all
three configs.

### Step 1: Move the faulty unit to the working area

**Goal:** one tagged, de-energised unit sits in the working area, front panel toward the operator.

Look where the faulty unit is before reaching for it.

- **IF the unit is at the back-left (Config L):** with the **left gripper**, grasp one unit at the middle of
  its left wall, lift it clear of the table and carry it forward and right to the center.
- **IF the unit is at the front-centre (Config M):** with the **left gripper**, grasp one unit at the middle
  of its left wall, lift it clear of the table and carry it straight back to the center.
- **IF the unit is at the back-right (Config R):** with the **right gripper**, grasp one unit at the middle
  of its right wall, lift it clear of the table and carry it forward and left to the center.

Then, in all three:

- Do not drag or slide the unit; it is carried clear of the table.
- Set it down flat, lid up, with the front panel facing the operator, and release.
- With the right gripper, turn the **fault tag** face up and read it. Confirm it names one **flagged
  component** by reference designator and carries a **connector list**.
- Confirm the unit is powered down and that no cable runs from its front panel to the test station or to
  any supply.
- If the fault tag is missing, unreadable, or names more than one component, return the unit to the
  start zone and report it. Do not open an untagged unit.

### Step 2: Open the enclosure

**Goal:** the lid is off and set aside, all four screws are in the screw cup, and nothing has fallen
inside.

#### 2.1 Back out the four screws

- With the left gripper, hold the base down at the middle of its near wall so the unit cannot turn while
  the screws come out.
- With the right gripper, take the torque driver from the right edge and back the four screws out in the
  reverse cross order: near-right, far-left, far-right, near-left.
- Back each screw out until it turns free, then lift it straight up out of its clearance hole with the
  driver bit or the right gripper.
- Carry each screw to the **screw cup** in the parts tray and release it there before starting the next
  screw. Screws are never set down on the table or laid on the lid.
- Return the torque driver to the right edge once all four screws are out.

#### 2.2 Lift the lid

- Confirm all four clearance holes are empty before the lid is touched.
- With both grippers, grasp the lid at its left and right edges and lift it **straight up**, clear of the
  sealing face.
- Do not slide, twist or pry the lid off. If the lid does not lift, set it back down and check for a
  screw still in place.
- Set the lid down to the left of the unit in the working area, outside face down, and release.
- Look into the open base and confirm nothing fell in: no screw, no debris, no tool. Remove anything
  found before going on.

### Step 3: Remove the flagged component

**Goal:** the component named on the fault tag is out of the unit and in the quarantine tray, and nothing
else has moved.

#### 3.1 Confirm the component against the fault tag

- Read the **reference designator** printed on the board beside each component and find the one named on
  the fault tag.
- With the right gripper, point to that component and hold it in the camera view long enough for the
  designator and the tag to be read together.
- If the designator on the board and the designator on the tag do not match, stop. Close the unit per
  Step 6 and report a tag mismatch. Never swap a component the tag does not name.

#### 3.2 Unmate the component's connectors

- With the left gripper, hold the component body down; with the right gripper, press the **latch** on
  each plug wired to it and draw the plug **straight out** of its header.
- Pull on the plug body only. Never draw a connector out by its wires, its harness or its service loop.
- Lay each freed plug over the near wall of the base so its header stays visible and reachable.

#### 3.3 Release the mount and lift the component out

- With the right gripper, press the **retaining clip** aside until it clears the component, and hold it
  clear.
- With the left gripper, lift the component **straight up** off its standoffs, keeping it level so it
  does not catch a neighbouring part.
- Carry the removed component to the **quarantine tray** at the front-right, set it in the reject bag,
  and release.
- The removed component never goes back in the parts tray, never goes back in a unit, and is not set down
  anywhere else on the table.

### Step 4: Fit the replacement component

**Goal:** the replacement component sits fully seated on its mount, clip latched, in the same position
and orientation as the part that came out.

#### 4.1 Verify the replacement

- With the right gripper, take the replacement component from its ESD bag in the parts tray and hold it
  in view.
- Read its **part number** and confirm it matches the part number called on the fault tag. If it does not
  match, return it to the tray and report a wrong part; do not fit it.
- Confirm the replacement has no bent pin, no cracked body and no loose header.

#### 4.2 Seat and secure it

- Carry the replacement to the open base and line it up over its standoffs in the **same orientation**
  the removed component had.
- With the left gripper, lower it straight down until it sits flat on the standoffs. Do not slide it in
  sideways under the clip.
- With the right gripper, release the **retaining clip** so it snaps over the component, then press the
  component down once at its centre.
- Confirm the component does not rock, sits flat on both standoffs, and that its headers face the same
  way as the plugs laid over the near wall.

### Step 5: Reseat every connector in the unit

**Goal:** every connector on the connector list has been unmated and mated again to a full seat, and the
harness is clear of the sealing face.

#### 5.1 Work the connector list in order

- Read the **connector list** on the fault tag and work it from the first entry to the last. Every
  connector on the list is reseated, not only the ones on the swapped component.
- Reseat one connector at a time and finish it before touching the next, so only one plug is ever out of
  its header.

#### 5.2 Unmate and mate each connector

- With the left gripper, hold the header or the board down beside the connector so the board does not
  lift.
- With the right gripper, press the **latch** and draw the plug straight out until it is fully clear of
  the header.
- Line the plug up with its header so the **key** rib meets the key slot, then push it straight in until
  the latch **clicks** and the two bodies meet with no gap.
- If the plug does not enter freely, lift it clear and re-aim. Never force a plug past its key or into a
  header it does not match.
- Tug the plug once, gently, by its body. If it moves at all, it is **partially mated**: draw it out and
  mate it again.

#### 5.3 Dress the harness

- Lay every harness back down inside the base with its **service loop** slack, not stretched across a
  component.
- Push every wire down below the level of the **sealing face** all the way round the base.
- Confirm no wire crosses the sealing face and no plug stands proud of the base walls.

### Step 6: Close the enclosure

**Goal:** the lid is down flat with no harness pinched, and all four screws are torqued in the cross
pattern.

- Before the lid goes on, sweep the open base once with the camera view: no tool, no screw, no cut wire,
  no debris inside.
- With both grippers, grasp the lid at its left and right edges and lower it **straight down** onto the
  sealing face, outside face up, with its clearance holes over the four screw bosses.
- Do not slide the lid into place across the sealing face; a slid lid drags wires under its edge.
- Look all the way round the **lid gap** and confirm no wire is trapped and the gap is even.
- With the right gripper, bring the four screws back one at a time from the **screw cup** and
  **hand-start** each one two to three turns, head still proud.
- All four screws are hand-started before the torque driver touches the first one.
- With the right gripper, take the torque driver and run the **seating pass** at half torque in the cross
  order: near-left, far-right, far-left, near-right.
- Run the **final pass** at full torque in the same cross order, one click per screw.
- Confirm all four heads are down on the lid, the lid gap is closed and even, and the unit does not rock.
- Return the torque driver to the right edge.

### Step 7: Retest the unit

**Goal:** the unit has been run at the test station and a pass or a fail has been read from the lamps.

- With the left gripper, carry the closed unit to the **test station** at the back-center and lower it
  into the **dock**, front panel toward the operator.
- With the right gripper, take the **test lead** and mate it to the front panel port until it clicks and
  is fully seated.
- With the right gripper, press the start control on the station and hold both arms clear of the unit
  while the test runs.
- Read the lamps once the test ends: **pass lamp** green, or **fail lamp** red.
- **On a pass:** unmate the test lead by its body, return it to the station, lift the unit out of the
  dock and carry it back to the working area for Step 8.
- **On a fail:** unmate the test lead, lift the unit out, place it in the **quarantine tray** at the
  front-right with its fault tag still attached, and report the failed retest. The unit is not opened
  again, not retested again and not relabelled.
- A unit is retested once. Repeating the test to get a different lamp is not permitted.

### Step 8: Relabel the unit as reworked

**Goal:** one rework label is applied to the label zone below the serial label, square and readable.

- This step is reached only after the **pass lamp** has been read in Step 7.
- With the left gripper, hold the unit down at the middle of its near wall, front panel toward the
  operator.
- With the right gripper, lift one **rework label** from the label sheet at the right edge by its edge.
- Place the label in the **label zone** below the existing **serial label**, square to the bottom edge of
  the front panel, and press it down once across its face.
- The **serial label stays on**. The rework label never covers the serial, never overlaps it, and no
  existing label is peeled off.
- With the right gripper, pull the **fault tag** off the unit and place it in the quarantine tray with
  the removed component.
- Confirm the rework label is flat, unwrinkled, inside the label zone, and that the serial is still fully
  readable.

### Step 9: Move the reworked unit to the output zone

**Goal:** the reworked unit rests in the designated output zone.

- With the left gripper, grasp the unit at the middle of its left wall and lift it clear of the table.
- **IF Config L or M:** carry it to the back-right. **IF Config R:** carry it to the back-left, which is
  empty because the units started at the back-right.
- Set it down flat, lid up, front panel toward the operator, and release.
- In batch sessions, place each reworked unit in a row from left to right with its neighbours, not
  stacked.
- Confirm the working area holds no screw, no plug, no tool and no debris before the next unit is picked.
- Return to Step 1 while the start zone still holds tagged faulty units.

### Step 10: Return to home and end the episode

- Confirm the torque driver is at the right edge, the screw cup is empty, and the test station dock is
  empty with both lamps dark.
- Move both arms back to the home position with grippers open.
- End data collection.

## SOP violations

These are the things the operator can do that break (violate) the SOP. This list feeds the violation set
and is what reviewers look for using the side-by-side review tool.

### How to record a violation in review

For each violation you spot in a recorded episode, record:

- The **start timestamp** of the violation in the video.
- The **violation name** from the list below.
- The **SOP rule broken** (the step number from the list below).

The **visible cue** is what you actually see in the video. The **coaching note** is for retraining the
operator after the review; it is not what the annotator labels.

### Episode handling

Any SOP violation is flagged (or tagged) with the timestamp and violation name. Rather than being
discarded, the episode is retained in the training data and tagged with the violation. No flagged episode
is deleted. This matches the goal of capturing realistic operator variance in training.

### Violations

**Note on the start position:** the violations below were written for Config L (unit starts at the
back-left, reworked unit staged at the back-right). The pickup and arm-role cues will be rewritten later to
cover all three start positions; they are left as they are for now. Until then, anything that does not match
the episode's config goes under **Config misaligned**.

**Violation: Config misaligned.**

- **Visible cue:** what the operator does does not match the config on the table — the faulty unit is not
  in the start zone for the config; a gripper reaches across the table for the unit; the reworked unit is
  staged at the back-right in Config R or at the back-left in Config L or M; or the wrong IF line is
  followed.
- **SOP rule broken:** the start position and the same-side rule (the left gripper picks the unit in Config
  L and M, the right gripper in Config R; no arm reaches across the table; the IF line followed is the one
  for the config on the table).
- **Coaching note:** look where the faulty unit is before the first reach, then follow that config's IF
  lines through Steps 1 and 9.

**Violation: Wrong pickup.**

- **Visible cue:** the unit is started from the center, the quarantine tray or the output row instead of
  the back-left input zone, it is placed outside the center working area, it is set down with the front
  panel turned away from the operator, or the unit is dragged or slid across the table instead of being
  picked up (lifted clear of the surface) and carried.
- **SOP rule broken:** Step 1 (pick from the back-left, carry to the center, set down front panel toward
  the operator). Pick means lift and carry, not drag.
- **Coaching note:** always start each unit from the back-left and bring it to the center before opening
  it. Lift it clear of the table and carry it. Do not drag or slide it across the surface.

**Violation: Fault tag not read.**

- **Visible cue:** the operator starts backing screws out without ever turning the fault tag face up and
  holding it in view, or opens a unit whose tag is missing or unreadable.
- **SOP rule broken:** Step 1 (read the fault tag and confirm it names one flagged component before
  opening).
- **Coaching note:** read the tag first, every time. The tag is what says which component may be touched;
  without it the rework has no scope.

**Violation: Unit opened while still connected or powered.**

- **Visible cue:** a cable still runs from the unit's front panel to the test station or a supply when
  the first screw is backed out.
- **SOP rule broken:** Step 1 (the unit is de-energised and unplugged before the first screw is touched).
- **Coaching note:** unplug and confirm dark before opening. Working into a live unit risks the operator,
  the board and the replacement part.

**Violation: More than one unit open at a time.**

- **Visible cue:** a second unit is picked from the back-left, or a second lid comes off, while the first
  unit is still open in the working area.
- **SOP rule broken:** Step 1 and Step 9 (one unit at a time; close, retest and relabel before the next
  pick).
- **Coaching note:** finish the unit in hand completely before reaching back to the input zone. Two open
  units mix screws, plugs and components between them.

**Violation: Screws removed out of pattern.**

- **Visible cue:** the four lid screws are backed out in an order other than the reverse cross order
  near-right, far-left, far-right, near-left.
- **SOP rule broken:** Step 2.1 (back the screws out in the reverse cross order).
- **Coaching note:** call the corner order out loud as each screw comes out. Backing a lid off from one
  side loads the last screw and the sealing face.

**Violation: Screws not put in the screw cup.**

- **Visible cue:** a screw is set down on the table, laid on the lid, left in the open base or held while
  another screw is worked, instead of being carried to the screw cup in the parts tray.
- **SOP rule broken:** Step 2.1 (carry each screw to the screw cup and release it there before starting
  the next).
- **Coaching note:** one screw, one trip to the cup. Loose screws roll into the open base and end up
  closed inside the unit.

**Violation: Lid pried, slid or twisted off.**

- **Visible cue:** the lid is levered, rocked or dragged sideways across the sealing face rather than
  being lifted straight up, or it is lifted with a screw still in a clearance hole.
- **SOP rule broken:** Step 2.2 (confirm all four holes are empty, then lift the lid straight up).
- **Coaching note:** check all four holes first, then lift straight up with both grippers. Prying marks
  the sealing face and a slid lid drags wires under its edge.

**Violation: Debris left inside the open base.**

- **Visible cue:** a screw, a cut wire, a tool or other debris is visible inside the base after the lid
  comes off and the operator carries on without removing it.
- **SOP rule broken:** Step 2.2 (look into the open base and remove anything found before going on).
- **Coaching note:** sweep the inside of the base with the camera view right after the lid lifts.
  Anything left in there gets closed inside the unit.

**Violation: Wrong component swapped.**

- **Visible cue:** the component removed from the base is not the one named on the fault tag: a different
  reference designator, or a neighbouring part pulled instead.
- **SOP rule broken:** Step 3.1 (read the designator on the board and match it to the tag before anything
  is removed).
- **Coaching note:** point to the designator and hold it in view beside the tag before touching the clip.
  A wrong swap leaves the real fault in the unit and scraps a good part.

**Violation: Extra component removed or reworked.**

- **Visible cue:** a second component is unclipped, lifted, swapped or resoldered in addition to the
  flagged one, or a connector is cut or a wire re-routed.
- **SOP rule broken:** Step 3 (only the component named on the fault tag is swapped).
- **Coaching note:** the tag defines the whole scope of the rework. Anything beyond it is a new change
  with no test history behind it.

**Violation: Connector pulled by the wires.**

- **Visible cue:** a plug is drawn out by its harness, its service loop or a single wire rather than by
  the plug body, or the latch is not pressed before the pull.
- **SOP rule broken:** Steps 3.2 and 5.2 (press the latch, pull the plug body straight out).
- **Coaching note:** press the latch, grip the plug body, pull straight. Pulling on wires backs pins out
  of the housing where the damage will not be visible.

**Violation: Removed component not quarantined.**

- **Visible cue:** the removed faulty component is set down on the table, put back in the parts tray,
  left in the working area, or refitted into a unit instead of going into the quarantine tray.
- **SOP rule broken:** Step 3.3 (carry the removed component to the front-right quarantine tray and
  release it in the reject bag).
- **Coaching note:** the removed part goes to quarantine on the same move that lifts it out. A faulty
  part loose on the bench will be fitted to something eventually.

**Violation: Replacement not verified.**

- **Visible cue:** the replacement component is fitted without its part number ever being held in view
  and matched against the fault tag, or is fitted despite a visible bent pin or cracked body.
- **SOP rule broken:** Step 4.1 (read the part number and confirm it matches the tag before fitting).
- **Coaching note:** hold the part number in view before it goes in the base. A mismatched replacement
  fails retest and sends the unit round again.

**Violation: Replacement fitted wrong or left unseated.**

- **Visible cue:** the replacement sits at the wrong orientation, sits proud of a standoff, rocks when
  pressed, is slid sideways under the clip, or is left with the retaining clip not latched over it.
- **SOP rule broken:** Step 4.2 (lower straight down onto the standoffs in the same orientation, latch
  the clip, confirm no rock).
- **Coaching note:** match the orientation the old part had, lower straight down, latch the clip, then
  press once and check for rock.

**Violation: Connector reseat skipped.**

- **Visible cue:** only the swapped component's connectors are reseated, or one or more entries on the
  connector list are never unmated at all before the lid goes back on.
- **SOP rule broken:** Step 5.1 (every connector on the connector list is reseated, not only the ones on
  the swapped component).
- **Coaching note:** work the list top to bottom and tick each entry. A connector that was never reseated
  is the most common repeat failure after rework.

**Violation: Connector left partially mated.**

- **Visible cue:** a plug is left standing off its header with a visible gap, the latch open, or it moves
  when tugged and the operator moves on.
- **SOP rule broken:** Step 5.2 (push in until the latch clicks and the bodies meet with no gap, then
  tug-check).
- **Coaching note:** listen for the click and tug-check every connector. A partial mate reads as
  intermittent, not as a hard fail, and gets shipped.

**Violation: Connector forced or mis-keyed.**

- **Visible cue:** a plug is pushed into a header it does not match, forced past its key rib, or entered
  at an angle and worked in rather than being lifted clear and re-aimed.
- **SOP rule broken:** Step 5.2 (line the key rib to the key slot, push straight in; lift clear and
  re-aim if it does not enter freely).
- **Coaching note:** if it does not go in freely it is the wrong header or the wrong angle. Forcing bends
  pins and splits housings.

**Violation: More than one connector unmated at once.**

- **Visible cue:** two or more plugs are out of their headers at the same time during the reseat pass.
- **SOP rule broken:** Step 5.1 (reseat one connector at a time and finish it before touching the next).
- **Coaching note:** one connector out, one connector back. Several plugs loose at once is how they get
  swapped between headers.

**Violation: Harness pinched under the lid.**

- **Visible cue:** a wire is visible in the lid gap, trapped between the lid and the sealing face, or a
  harness is left stretched across a component or standing above the sealing face when the lid comes
  down.
- **SOP rule broken:** Steps 5.3 and 6 (push every wire below the sealing face, then check the lid gap
  all the way round).
- **Coaching note:** dress the harness down before the lid, then walk the lid gap all the way round
  before hand-starting a screw.

**Violation: Torque started before all four screws were hand-started.**

- **Visible cue:** the torque driver touches the first screw while one or more clearance holes are still
  empty.
- **SOP rule broken:** Step 6 (all four screws are hand-started before the torque driver touches the
  first one).
- **Coaching note:** hand-start all four first. Torquing one corner while another is empty pulls the lid
  over and cocks the remaining holes off their bosses.

**Violation: Cross pattern or two-pass torque not followed.**

- **Visible cue:** the four screws are torqued in an order other than near-left, far-right, far-left,
  near-right, or the seating pass is skipped and the screws go straight to full torque.
- **SOP rule broken:** Step 6 (seating pass at half torque, then final pass at full torque, both in the
  cross order).
- **Coaching note:** call the corner order out loud on both passes. Skipping the seating pass draws the
  lid down unevenly and opens the gap at the far corner.

**Violation: Retest skipped.**

- **Visible cue:** the unit is relabelled, staged at the back-right, or returned to the input zone
  without ever being docked at the test station and read.
- **SOP rule broken:** Step 7 (dock the unit, run the test, read the lamps) and Step 8 (relabel only
  after a pass).
- **Coaching note:** no unit leaves the working area without a lamp being read. An unretested rework is
  an untested unit with a label saying otherwise.

**Violation: Failed unit relabelled or staged.**

- **Visible cue:** the fail lamp is lit and the operator still applies a rework label, places the unit in
  the back-right output row, or reopens the unit for a second swap.
- **SOP rule broken:** Step 7 (a failed unit goes to the quarantine tray with its fault tag attached, and
  is not relabelled or reopened) and Step 8.
- **Coaching note:** a fail ends the episode for that unit. It goes to quarantine tagged, for someone
  with the test history to look at.

**Violation: Unit retested more than once.**

- **Visible cue:** the test is started again on the same unit after a fail, or repeated after a pass, to
  get a second reading.
- **SOP rule broken:** Step 7 (a unit is retested once).
- **Coaching note:** one retest, one result. Re-running a marginal unit until it passes hides the fault
  instead of finding it.

**Violation: Rework label misplaced.**

- **Visible cue:** the rework label is applied outside the label zone, crooked to the bottom edge,
  wrinkled, hanging over a panel edge, or applied to the lid instead of the front panel.
- **SOP rule broken:** Step 8 (apply the label in the label zone below the serial, square to the bottom
  edge, pressed flat).
- **Coaching note:** line the label to the bottom edge of the front panel and press once across its face.
  A crooked or lifting label will not scan.

**Violation: Serial label covered or removed.**

- **Visible cue:** the rework label overlaps or covers the existing serial label, or the serial label is
  peeled off the unit.
- **SOP rule broken:** Step 8 (the serial label stays on; the rework label goes below it and never covers
  it).
- **Coaching note:** the serial is how the unit's history is found. Cover it and the rework record has
  nothing to attach to.

**Violation: Fault tag left on a passed unit.**

- **Visible cue:** a unit that passed retest is relabelled and staged at the back-right with its fault
  tag still tied to it.
- **SOP rule broken:** Step 8 (pull the fault tag and place it in the quarantine tray with the removed
  component).
- **Coaching note:** the tag comes off as part of relabelling. A tagged unit in the output row reads as
  faulty to everyone downstream.

**Violation: Working area not cleared before the next unit.**

- **Visible cue:** the next unit is picked while a screw, a plug, a lid, the old component or debris is
  still sitting in the center working area.
- **SOP rule broken:** Step 9 (the working area holds no screw, plug, tool or debris before the next
  pick).
- **Coaching note:** finish the unit in hand, including its screws and its old part, before reaching back
  to the input zone.

**Violation: Wrong arm used for an action.**

- **Visible cue:** any step that specifies the left gripper or the right gripper is performed with the
  opposite gripper.
- **SOP rule broken:** any step that specifies a gripper, including Steps 1, 2, 3, 4, 5, 6, 7, 8 and 9.
- **Coaching note:** operator confusion about left vs right roles. Walk through the SOP step by step with
  the operator.

**Violation: Re-grip on a pick or grasp.**

- **Visible cue:** the operator closes on a unit, a lid, a screw, a plug or a component, finds the grip
  off, opens, and re-grips before lifting more than two times.
- **SOP rule broken:** Steps 1/2.2/3.3/4.2/5.2/9 (grasp securely at the middle of the body).
- **Coaching note:** approach angle off. Practice the from-above approach so the first grip catches the
  middle of the body.

**Violation: Repeated fiddling with a connector, a screw or the label.**

- **Visible cue:** the operator makes many small adjustments (more than about two) to seat a plug, start
  a screw, settle the lid or square the label, rather than settling it in one or two corrections.
- **SOP rule broken:** the mate, hand-start and label sub-steps (settle in one or two small adjustments).
- **Coaching note:** grip or approach is off, forcing repeated correction. Tighten the approach so each
  mate and each placement lands close to target.

**Violation: Arms not fully at home position at episode end.**

- **Visible cue:** in the final frame, both arms are close to the home position but not exactly at it
  (gripper not fully open, or arm position visibly off home).
- **SOP rule broken:** Step 10 (return to home position with grippers open).
- **Coaching note:** complete the home motion explicitly before ending recording.

### Non-violation failures

These are episode failures that are not the operator's fault and do not go in the violation set. They are
recorded as system issues, the episode is discarded/deleted, and the episode does not become a coaching
point for the operator.

- **Recording stopped or paused mid-episode:** Cause: software or hardware issue with the recording
  system.
- **Camera dropped frames or lost feed during the episode:** Cause: camera or capture system issue.
- **Hardware fault on the robot arm:** Cause: gripper malfunction, arm position drift, or motor error
  during the episode.
- **Test station did not run or gave no reading:** Cause: station power, dock or software fault, or
  neither lamp lights at the end of the run. Service the station before the next episode.
- **Replacement component faulty out of the bag:** Cause: a correctly verified, correctly fitted
  replacement that is dead on arrival. The retest fail is a parts issue, not an operator issue.
- **Screw or boss thread stripped:** Cause: a screw that spins without drawing down, or a boss whose
  thread has failed, under a normal hand-start. Replace the screw from the spares or set the enclosure
  aside.
- **Enclosure cracked or sealing face damaged:** Cause: a base or lid that splits or deforms under a
  normal grasp or a normal torque pass. Set the unit aside before the next episode.
- **Connector housing broken on arrival:** Cause: a latch, header or plug already snapped before the unit
  was opened, so it cannot be reseated to a full seat.
- **Fault tag missing or illegible:** Cause: a tag that is absent, torn or unreadable, so the flagged
  component cannot be identified. Re-tag before the next episode.
- **Label sheet empty or unreadable:** Cause: no rework labels left on the sheet, or labels printed blank
  or smeared. Re-stock before the next episode.

## After each episode: repeat or reset

- **Batch sessions (e.g., 4x):** if fewer than the target number of units are reworked, reset the
  workspace and return to Step 1 with the next unit. Once the target number is reworked, reset the
  workspace before the next session.
- Clear the working area and re-run the Setup checklist before the next session.

### After the episode: reset the workspace

This part is not recorded. It is just how you reset the table for the next episode.

- With recording off, bring each reworked unit back from the output zone to the working area, one at a
  time.
- Peel the rework label off the front panel and leave the serial label in place.
- Open the enclosure, take the replacement component back out, and refit the original flagged component
  on its mount.
- Re-mate every connector on the connector list to a full seat, close the lid and torque the four screws
  in the cross pattern.
- Tie a fresh **fault tag** to the unit naming the same flagged component and the same connector list.
- Move every unit back to the start zone for the next episode's config — back-left (Config L),
  front-centre (Config M), or back-right (Config R) — so it once again holds tagged faulty units, lid up,
  front panels toward the operator, and the other two zones are empty.
- Return the replacement component to its ESD bag in the parts tray and empty the screw cup back to four
  screws.
- Empty the quarantine tray, fit a fresh reject bag, and return it empty to the front-right.
- Return the torque driver and the label sheet to the right edge, hex bit fitted and labels face up.
- Clear the test station dock, return the test lead to its rest position, and confirm both lamps are
  dark.
- Wipe the working area dry and confirm it is clear of screws, plugs, components and debris.
- Confirm the table surface is clear of any objects other than the faulty units and the trays.
- Go through both Setup checklists again before starting the next episode.

**Warning:** The table must be clear except for the tagged faulty unit(s) in the start zone, the parts
tray at the front-left, the quarantine tray at the front-right, the driver and label sheet at the right
edge, and the test station at the back-center.

## Annotation subtasks

1. Move one tagged faulty unit from the start zone to the center working area
2. Read the fault tag (flagged component and connector list)
3. Open the enclosure (four screws out in reverse cross order, screws to the screw cup, lid lifted
   straight up)
4. Remove the flagged component (unmate its connectors, release the clip, lift it out)
5. Quarantine the removed component in the front-right tray
6. Verify and fit the replacement component (part number checked, seated, clip latched)
7. Reseat every connector on the connector list to a full seat
8. Dress the harness clear of the sealing face
9. Close the enclosure (lid down, four screws hand-started, seating pass, final pass)
10. Retest the unit at the test station and read the pass or fail lamp
11. Relabel the unit as reworked and remove the fault tag
12. Stage the reworked unit in the output zone
13. Home the arms
