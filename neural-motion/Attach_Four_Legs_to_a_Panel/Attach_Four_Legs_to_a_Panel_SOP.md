# Attach Four Legs to a Panel SOP (Bracket-Mounted)

This SOP covers attaching four legs to a single flat panel using a two-arm robot system. Both arms are
used throughout: the grippers cooperate to position the brackets, start the screws by hand, drive them to
seat, flip the panel, wobble-test it and shim it, with the left and right grippers taking the specific
roles called out in each step. The task runs from a bare panel in its start zone to a legged panel standing
at the back-right.

The table is set up in one of three ways. Only the panel moves; the parts tray, the driver, the working area
and the output zone are in the same place in all three.

- **Config L:** the panel is at the back-left.
- **Config M:** the panel is at the front-center, in front of the working area.
- **Config R:** the panel is at the front-right.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

- **Start position:** the panel starts at the back-left (**Config L**), the front-center (**Config M**) or
  the front-right (**Config R**). One config per episode, chosen before recording and never changed
  mid-episode.
- **Same-side rule:** the gripper on the panel's side picks it — the left gripper in Config L and M, the
  right gripper in Config R. No arm reaches across the table.
- **Fixed roles:** the parts tray at the front-left, the driver at the right edge and the output zone at the
  back-right do not move, and the right gripper handles every bracket, screw, leg and shim and the driver
  while the left gripper holds, in every config.
- **Working position:** the panel is always moved to the centre of the table before any bracket is
  positioned.
- **Panel target:** the panel must lie flat, **face down, with all four layout marks visible**, before
  any bracket is positioned.
- **Corner order:** the four corners are always worked in the same order: near-left, far-left, far-right,
  near-right.
- **Fastening order:** at each bracket every screw is started by hand first, then the screws are driven
  to seat in a diagonal order.
- **Test before output:** the panel is always flipped and wobble-tested in the working area before it is
  moved to the output zone. Shims are added only after a failed wobble-test.

## Setup

Go through both checklists before starting the episode.

### Hardware checklist

- Cameras are on and recording
- Env camera frame includes the front and back edges of the table and is centered on the table's
    midpoint
- Both arms are at the home position with grippers open
- Table surface is clear of any objects other than the panel(s) and the parts tray

### Materials checklist

- Panel(s) to be legged are placed in the start zone for this episode's config, face down, with the four
    layout marks visible, and the other two start zones are clear:
    - **Config L:** back-left
    - **Config M:** front-center, in front of the working area
    - **Config R:** front-right, clear of the driver at the right edge
- The parts tray is at the **front-left** and holds 4 brackets, 16 screws, 4 legs and 4 shims per
    panel
- The driver is at the **right edge**, bit fitted and matched to the screw head
- Center of the table is clear (working area for positioning, fastening, flipping and wobble-testing)
- Back-right of the table is clear (output location for the legged panel / row)

## Workspace layout

- **Start zone**: bare panel(s), face down (input) — back-left (**Config L**), front-center (**Config M**)
  or front-right (**Config R**)
- **Center** : working area (position, hand-start, drive, flip, wobble-test, shim)
- **Front-left**: parts tray (brackets, screws, legs, shims)
- **Right edge**: driver
- **Back-right**: legged panel / row of legged panels (output)

## Vocabulary

These are the terms used in this SOP. Operators and annotators must use this language consistently. One
term per concept, used throughout.

### Panel anatomy

- **Panel:** a single flat rectangular top that four legs are attached to.
- **Face:** the finished side of the panel. It points down during fastening.
- **Underside:** the side of the panel opposite the face. The brackets go here.
- **Panel edge:** one of the four sides of the panel.
- **Mounting corner:** one of the four corners of the underside that takes a bracket.
- **Layout mark:** the printed L-shaped line at a mounting corner that the bracket is aligned to.
- **Near-left corner:** the mounting corner closest to the operator on the left. Work starts here.
- **Far-left corner:** the mounting corner farthest from the operator on the left.
- **Far-right corner:** the mounting corner farthest from the operator on the right.
- **Near-right corner:** the mounting corner closest to the operator on the right. Work ends here.

### Hardware anatomy

- **Bracket:** the flat metal plate that holds one leg to one mounting corner.
- **Screw hole:** one of the four holes in a bracket that takes a screw.
- **Boss:** the threaded socket at the center of a bracket that the leg screws into.
- **Screw:** one of the four fasteners that hold one bracket to the panel.
- **Screw head:** the top of a screw, the part the driver bit sits in.
- **Driver:** the tool that drives a screw.
- **Leg:** a single leg with a threaded stud at its top end.
- **Stud:** the threaded rod at the top of a leg that turns into the boss.
- **Foot:** the bottom end of a leg that rests on the table.
- **Shim:** a thin pad placed under one foot to remove wobble.
- **Seated:** a screw head sits flat against the bracket with no gap.
- **Proud:** a screw head stands above the bracket with a visible gap.
- **Cross-threaded:** a screw or stud that has entered its thread at an angle and binds.
- **Finger-tight:** turned in by hand until it stops, with no driver used.
- **Wobble:** movement of a foot off the table when a corner of the panel is pressed.
- **Short leg:** the leg whose foot lifts off the table during the wobble-test.

### Workspace zones

- **Start zone:** where the bare panel(s) lie at the start of the episode — back-left (**Config L**),
  front-center (**Config M**) or front-right (**Config R**).
- **Working area:** the center of the table where positioning, fastening, flipping, wobble-testing and
  shimming happen.
- **Front-left tray:** the parts tray holding the brackets, screws, legs and shims.
- **Right edge:** the rest position for the driver.
- **Back-right edge:** output zone where the legged panel is placed at the back-right of the table.
- **Home position:** the default resting pose for each arm: gripper open and clear of the table.

### Actions

- **Pick:** move one panel to the working area.
- **Square:** set the panel flat and face down with the layout marks visible and the panel edges parallel
  to the table edges.
- **Position:** set a bracket on a mounting corner, aligned to the layout mark.
- **Hand-start:** turn a screw into a screw hole by hand until it is finger-tight.
- **Drive:** turn a screw with the driver until the screw head is seated.
- **Thread:** turn a leg stud into a boss until the leg stops.
- **Flip:** turn the panel over so it stands on its four feet.
- **Wobble-test:** press each corner of the panel in turn and watch the four feet.
- **Shim:** place one shim under a short leg.
- **Stage:** place the legged panel in the output zone (batch sessions place them in a row).

## Steps

Only Step 1 depends on where the panel starts: in Config L and M the **left gripper** takes the panel from the
start zone; in Config R the **right gripper** takes it. Every other line is the same in all three configs.

### Step 1: Move a panel to the working area

**Goal:** one panel lies in the working area, ready to be squared.

Look where the panel is before reaching for it.

- **IF the panel is at the back-left (Config L):** with the **left gripper**, grasp one panel from the
  back-left pile at the middle of its left edge.
- **IF the panel is at the front-center (Config M):** with the **left gripper**, grasp one panel from the
  front-center pile at the middle of its left edge.
- **IF the panel is at the front-right (Config R):** with the **right gripper**, grasp one panel from the
  front-right pile at the middle of its right edge.

Then, in all three:

- Lift it clear of the table and carry it to the center; do not drag or slide it.
- Set it down flat and release.

### Step 2: Square the panel face down

**Goal:** the panel lies flat and face down in the center of the table, with all four layout marks
visible and the underside clear.

#### 2.1 Check which side is up

- If the underside is up and the four layout marks are visible → continue to 2.2.
- If the face is up → with the left gripper grasp the middle of the left edge and with the right gripper
  grasp the middle of the right edge, lift the panel 5 cm clear of the table, turn it over in one smooth
  motion, and set it down face down.

#### 2.2 Square the panel to the table

- With both grippers, move the panel until its center is within 5 cm of the center of the table.
- Turn the panel until each panel edge is parallel to the table edge it faces, within 5°.

#### 2.3 Clear the underside

- With the right gripper, sweep any loose screw, shim or debris off the underside and into the parts
  tray.
- Confirm the panel sits flat on the table with no rock at any corner.

#### 2.4 Confirm the layout marks

- Confirm one layout mark is visible at each of the four mounting corners.
- If a layout mark is hidden or unreadable → stop the episode and report a defective panel.

### Step 3: Position the four brackets

**Goal:** one bracket sits flat on each mounting corner, aligned to its layout mark within 2 mm, with the
boss pointing up.

#### 3.1 Stage the brackets

- With the right gripper, take four brackets from the parts tray and set them on the underside of the
  panel, one beside each mounting corner.

#### 3.2 Position the first bracket

- With the left gripper, hold the panel against the table at the near-left corner.
- With the right gripper, set one bracket on the near-left corner with the boss pointing up.
- Slide the bracket until its two outer edges sit on the two lines of the layout mark, within 2 mm.
- Press the bracket flat and confirm all four screw holes show bare panel through them.
- If the bracket rocks on the panel → lift it, clear what is under it, and position it again.

#### 3.3 Position the remaining three brackets

- Repeat 3.2 at the far-left corner, then the far-right corner, then the near-right corner.
- Confirm four brackets are positioned and every boss points up.

**Warning:** All four brackets must sit flat and within 2 mm of their layout marks before any screw is
started. A bracket moved after its screws are driven leaves open holes in the panel.

### Step 4: Start every screw by hand

**Goal:** all four screws at a bracket stand finger-tight and square in their screw holes, with no driver
used.

#### 4.1 Hand-start the first screw

- With the left gripper, hold the bracket flat against the near-left corner.
- With the right gripper, take one screw from the parts tray and set its tip in one screw hole.
- Turn the screw clockwise by hand until it stops, and keep the screw square to the panel while turning.
- If the screw binds in the first two turns → turn it anti-clockwise until it lifts out, then set it in
  the hole again square and turn it in.

#### 4.2 Hand-start the other three screws

- Repeat 4.1 for the other three screw holes in the same bracket.
- Confirm all four screws are finger-tight and no screw is turned with the driver.

#### 4.3 Hand-start the remaining brackets

- Repeat 4.1 and 4.2 at the far-left corner, then the far-right corner, then the near-right corner.
- Confirm 16 screws stand finger-tight and every bracket still sits within 2 mm of its layout mark.

### Step 5: Drive the screws to seat

**Goal:** all 16 screw heads are seated flat against their brackets, with no proud screw and no stripped
screw.

#### 5.1 Drive the first bracket

- With the right gripper, take the driver from the right edge and seat the bit in one screw head at the
  near-left corner.
- With the left gripper, hold the panel against the table.
- Drive that screw until its screw head sits flat against the bracket, then stop.
- Drive the screw diagonally opposite it next, then the remaining two screws in the same diagonal order.
- If the driver bit slips out of a screw head → stop, re-seat the bit square in the screw head, and drive
  again.

#### 5.2 Drive the remaining three brackets

- Repeat 5.1 at the far-left corner, then the far-right corner, then the near-right corner.

#### 5.3 Confirm every screw is seated

- Run the right gripper across all 16 screw heads and confirm each one sits flat against its bracket with
  no gap.
- If a screw head is proud → drive that screw until it seats.
- With the right gripper, return the driver to the right edge.

### Step 6: Thread a leg into each bracket

**Goal:** four legs stand square to the panel, each threaded into its boss until the leg stops.

- With the right gripper, take one leg from the parts tray and set its stud in the boss at the near-left
  corner.
- With the left gripper, hold the panel against the table.
- Turn the leg clockwise until it stops and the top of the leg sits flat against the bracket.
- If the stud binds in the first two turns → turn the leg anti-clockwise until the stud lifts out, then
  set it in the boss again square and turn it in.
- Repeat at the far-left corner, then the far-right corner, then the near-right corner.
- Confirm each leg stands within 5° of square to the panel.

**Warning:** All 16 screws must be seated and all four legs threaded to a stop before the panel is
flipped. A panel flipped on unseated screws drops a bracket.

### Step 7: Flip the panel onto its legs

**Goal:** the panel stands on its four feet in the center of the table, face up.

- With the left gripper, grasp the middle of the left edge and with the right gripper, grasp the middle
  of the right edge.
- Lift the panel 10 cm clear of the table.
- Turn the panel over in one smooth motion so the four feet point down.
- Lower it until all four feet touch the table, then release both grippers.
- If the panel lands on an edge or a leg folds under → lift it clear, turn it over again, and set it down
  on all four feet.

### Step 8: Wobble-test the panel

**Goal:** the panel is confirmed either steady on all four feet or wobbling at one named short leg.

- With the right gripper, press down on the near-left corner of the face with a steady press, and watch
  all four feet.
- Repeat the press at the far-left corner, then the far-right corner, then the near-right corner.
- Keep the other gripper clear of the panel during each press.
- If no foot lifts off the table on any of the four presses → the panel is steady, skip to Step 10.
- If a foot lifts off the table → name that leg the short leg and continue to Step 9.

### Step 9: Shim the short leg

**Goal:** the short leg rests on the table on one or two shims and the panel passes the wobble-test.

#### 9.1 Insert one shim

- With the left gripper, press down on the corner diagonally opposite the short leg so the short leg
  lifts.
- With the right gripper, take one shim from the parts tray and slide it under the foot of the short leg.
- Release the left gripper and confirm the foot rests on the shim.

#### 9.2 Re-test

- Repeat Step 8 on all four corners.
- If no foot lifts → continue to Step 10.
- If the same foot still lifts → add one more shim under the same foot, up to two shims total, then
  repeat Step 8.
- If a different foot lifts → take the shims out and return to Step 8.
- If the panel still wobbles with two shims under one leg → stop the episode and report a defective leg.

**Warning:** The panel must stand on all four feet with no foot lifting on any of the four presses before
it leaves the working area.

### Step 10: Move the legged panel to the back-right edge

**Goal:** the legged panel stands in the designated back-right output zone.

- With the left gripper, grasp the middle of the left edge and with the right gripper, grasp the middle
  of the right edge.
- Lift the panel clear of the table and carry it back and to the right into the output location at the
  back-right of the table.
- Set it down on all four feet and release both grippers.
- Batch sessions only: set it beside the panels already there, all faces up, within 10-20 cm and not
  touching. Never set a panel on top of another panel.

### Step 11: Return to home and end the episode

- With the right gripper, return the driver to the right edge and any unused parts to the parts tray at
  the front-left.
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

**Note on the start position:** the violations below were written for Config L (panel starts at the
back-left). The pickup and arm-role cues will be rewritten later to cover all three start positions; they
are left as they are for now. Until then, anything that does not match the episode's config goes under
**Config misaligned**.

**Violation: Config misaligned.**

- **Visible cue:** what the operator does does not match the config on the table — the panel is not in the
  start zone for the config; a gripper reaches across the table for the panel; or the wrong IF line is
  followed.
- **SOP rule broken:** the start position and the same-side rule (the left gripper picks the panel in Config
  L and M, the right gripper in Config R; no arm reaches across the table; the IF line followed is the one
  for the config on the table).
- **Coaching note:** look where the panel is before the first reach, then follow that config's IF line in
  Step 1.

**Violation: Wrong pickup.**

- **Visible cue:** the panel is started from the center or the right instead of the back-left pile (input
  pile), it is set down outside the center working area, or the panel is dragged or slid across the table
  instead of being picked up (lifted clear of the surface) and carried.
- **SOP rule broken:** Step 1 (pick from the back-left pile and place it in the center working area).
  Pick means lift and carry, not drag.
- **Coaching note:** always start each panel from the back-left pile and bring it to the center before
  squaring it. Lift the panel clear of the table and carry it. Do not drag or slide it across the
  surface.

**Violation: Picked more than one panel at once.**

- **Visible cue:** two or more panels are lifted or moved from the input pile in a single pick.
- **SOP rule broken:** Step 1 (move one panel).
- **Coaching note:** pick exactly one panel per episode.

**Violation: Positioning while the panel is face up (square skipped).**

- **Visible cue:** a bracket is set on the face of the panel, or brackets are positioned while the panel
  is face up, without completing the turn-over and squaring in Step 2.
- **SOP rule broken:** Step 2 (square the panel flat and face down with the four layout marks visible
  before any bracket is positioned).
- **Coaching note:** never position a bracket on the face. Turn the panel face down and square it first,
  then check all four layout marks.

**Violation: Panel not squared to the table.**

- **Visible cue:** positioning starts with the panel center more than 5 cm off the center of the table,
  or a panel edge more than 5° out of parallel with the table edge it faces.
- **SOP rule broken:** Step 2.2 (center within 5 cm, panel edges parallel within 5°).
- **Coaching note:** center and square the panel before the first bracket goes on; a skewed panel puts
  every bracket off its mark.

**Violation: Debris left under a bracket.**

- **Visible cue:** a bracket is positioned over a loose screw, shim or piece of debris, or the bracket
  visibly rocks on the panel instead of sitting flat.
- **SOP rule broken:** Step 2.3 and Step 3.2 (clear the underside, and the bracket sits flat).
- **Coaching note:** sweep the underside into the parts tray before positioning, and press each bracket
  flat to confirm it does not rock.

**Violation: Bracket off its layout mark.**

- **Visible cue:** a bracket sits more than 2 mm off the lines of its layout mark, is turned away from
  the corner, or overhangs a panel edge.
- **SOP rule broken:** Step 3.2 (bracket outer edges on the layout mark lines, within 2 mm).
- **Coaching note:** set each bracket on the layout mark and slide it until both outer edges sit on the
  lines before starting a screw.

**Violation: Bracket boss pointing down.**

- **Visible cue:** a bracket is positioned with the boss against the panel instead of pointing up, so no
  leg can be threaded into it.
- **SOP rule broken:** Step 3.2 (set the bracket with the boss pointing up).
- **Coaching note:** check the boss points up before the first screw goes in; the boss is the leg socket.

**Violation: Screw hole not clear at positioning.**

- **Visible cue:** a screw hole in a positioned bracket does not show bare panel through it, so a screw
  is started into an obstructed hole.
- **SOP rule broken:** Step 3.2 (all four screw holes show bare panel through them).
- **Coaching note:** sight through all four screw holes after pressing the bracket flat.

**Violation: Screw driven without a hand-start.**

- **Visible cue:** the driver is used on a screw that was never turned in by hand, or the driver touches
  a screw head before all four screws at that bracket stand finger-tight.
- **SOP rule broken:** Step 4 (hand-start every screw at a bracket before any screw is driven) and the
  fastening order.
- **Coaching note:** start every screw by hand until it stops, then pick up the driver. The hand-start is
  what catches a crossed thread.

**Violation: Cross-threaded screw.**

- **Visible cue:** a screw enters its screw hole at a visible angle, binds in the first two turns, and is
  turned further instead of being backed out and re-set square.
- **SOP rule broken:** Step 4.1 (keep the screw square, and back it out if it binds in the first two
  turns).
- **Coaching note:** back a binding screw all the way out and set it square in the hole again. Never
  force a screw that binds early.

**Violation: Wrong drive order at a bracket.**

- **Visible cue:** the four screws at a bracket are driven around the bracket in sequence instead of in
  the diagonal order, so the bracket pulls to one side.
- **SOP rule broken:** Step 5.1 (drive one screw, then the screw diagonally opposite, then the remaining
  two in the same diagonal order).
- **Coaching note:** drive across the bracket, not around it, so the bracket pulls down flat.

**Violation: Screw left proud.**

- **Visible cue:** at the end of Step 5 a screw head stands above its bracket with a visible gap, or the
  bracket lifts at that screw.
- **SOP rule broken:** Step 5.3 (all 16 screw heads seated flat against their brackets).
- **Coaching note:** check all 16 screw heads at the end of Step 5 and drive any proud screw until it
  seats.

**Violation: Screw overdriven.**

- **Visible cue:** the driver keeps turning after the screw head is flat against the bracket, the screw
  head sinks into the bracket, or the screw spins without pulling down.
- **SOP rule broken:** Step 5.1 (drive until the screw head sits flat against the bracket, then stop).
- **Coaching note:** stop the driver the moment the screw head sits flat. An overdriven screw strips the
  panel and the panel is scrapped.

**Violation: Bracket moved after its screws are driven.**

- **Visible cue:** a bracket is repositioned, or its screws are backed out and re-driven in new holes,
  after Step 5 has seated that bracket.
- **SOP rule broken:** Step 3 Warning (all four brackets positioned within 2 mm before any screw is
  started).
- **Coaching note:** get the bracket on its layout mark before the first screw. A moved bracket leaves
  open holes in the panel.

**Violation: Fewer than four brackets or four legs attached.**

- **Visible cue:** the panel is flipped, wobble-tested or moved to the output zone with a mounting corner
  that carries no bracket, a bracket that carries no leg, or a bracket missing one or more of its four
  screws.
- **SOP rule broken:** Steps 3, 4, 5 and 6 (four brackets, 16 screws, four legs).
- **Coaching note:** count four brackets, 16 seated screws and four legs before the flip.

**Violation: Wrong corner order.**

- **Visible cue:** the corners are worked in an order other than near-left, far-left, far-right,
  near-right at positioning, hand-starting, driving or threading.
- **SOP rule broken:** The corner order (near-left, far-left, far-right, near-right) and Steps 3.3, 4.3,
  5.2 and 6.
- **Coaching note:** work the same four corners in the same order every time so the episodes match.

**Violation: Leg not threaded to a stop.**

- **Visible cue:** a leg stands with a visible gap between the top of the leg and its bracket, turns
  loosely by hand after Step 6, or is more than 5° out of square to the panel.
- **SOP rule broken:** Step 6 (turn the leg until it stops and the top of the leg sits flat against the
  bracket, within 5° of square).
- **Coaching note:** turn each leg until it stops and sits flat, then check it stands square to the
  panel.

**Violation: Cross-threaded leg stud.**

- **Visible cue:** a leg stud enters the boss at a visible angle, binds in the first two turns, and is
  turned further instead of being backed out and re-set square.
- **SOP rule broken:** Step 6 (back the leg out if the stud binds in the first two turns, then set it
  square).
- **Coaching note:** back a binding leg all the way out and set the stud square in the boss again.

**Violation: Panel flipped before the fastening is complete.**

- **Visible cue:** the flip in Step 7 starts while a screw is proud, a screw is missing, or a leg is not
  threaded to a stop.
- **SOP rule broken:** Step 6 Warning (all 16 screws seated and all four legs threaded to a stop before
  the flip).
- **Coaching note:** complete and check the fastening before the flip. A panel flipped on unseated screws
  drops a bracket.

**Violation: Panel flipped by sliding or with one gripper.**

- **Visible cue:** the panel is rolled over on the table, pushed off a table edge, or turned over with a
  single gripper instead of being lifted 10 cm clear with both grippers.
- **SOP rule broken:** Step 7 (grasp both edge middles, lift 10 cm clear, and turn the panel over in one
  smooth motion).
- **Coaching note:** lift the panel clear with both grippers before turning it over. Do not slide or roll
  it on the table.

**Violation: Panel set down on fewer than four feet.**

- **Visible cue:** at the end of Step 7 the panel rests on an edge, on a folded leg, or on the face,
  instead of on all four feet.
- **SOP rule broken:** Step 7 (lower the panel until all four feet touch the table).
- **Coaching note:** lower the panel level and confirm all four feet touch before releasing.

**Violation: Wobble-test skipped.**

- **Visible cue:** the panel goes from the flip straight to the output zone with no press on any corner.
- **SOP rule broken:** Step 8 (press each of the four corners in turn and watch the four feet).
- **Coaching note:** always wobble-test in the working area. An untested panel can reach the output zone
  wobbling.

**Violation: Incomplete or wrong wobble-test.**

- **Visible cue:** fewer than four corners are pressed, the panel is lifted or rocked side to side
  instead of pressed down, or the second gripper stays on the panel during a press.
- **SOP rule broken:** Step 8 (press all four corners in turn, one gripper only, other gripper clear).
- **Coaching note:** press down on each of the four corners in turn with one gripper and keep the other
  gripper clear.

**Violation: Shim added without a failed wobble-test.**

- **Visible cue:** a shim is placed under a foot when no foot lifted during Step 8, or a shim is placed
  before Step 8 is run.
- **SOP rule broken:** Step 9 and the test-before-output rule (shims only after a failed wobble-test).
- **Coaching note:** shim only the leg that lifted, and only after the wobble-test shows it lifting.

**Violation: Shim under the wrong leg.**

- **Visible cue:** the shim goes under a foot other than the one that lifted during Step 8.
- **SOP rule broken:** Step 9.1 (slide the shim under the foot of the short leg).
- **Coaching note:** name the short leg from the test before shimming, then shim that foot only.

**Violation: Over-shimmed.**

- **Visible cue:** more than two shims are placed under one leg, or shims are placed under more than one
  leg.
- **SOP rule broken:** Step 9.2 (up to two shims total under one leg, then report a defective leg).
- **Coaching note:** stop at two shims under one leg. Beyond that the leg is defective, not
  under-shimmed.

**Violation: Wobble left unresolved.**

- **Visible cue:** the panel is moved to the output zone while a foot still lifts on one of the four
  presses.
- **SOP rule broken:** Step 9 Warning (no foot lifts on any of the four presses before the panel leaves
  the working area).
- **Coaching note:** re-test after every shim and only move the panel once no foot lifts.

**Violation: Legged panel placement off zone.**

- **Visible cue:** in Step 10 the panel is left in the center instead of being moved to the back-right
  output zone, is set down face down, or is released at the back-right but ends up noticeably off from
  the designated zone, without falling or requiring further correction.
- **SOP rule broken:** Step 10 (carry the panel back and to the right into the back-right output zone and
  set it down on all four feet).
- **Coaching note:** move the legged panel to the back-right output zone. Do not leave it in the center
  and aim the release point more precisely; set it down on all four feet in the corner.

**Violation: Wrong batch placement (batch sessions).**

- **Visible cue:** in Step 10 the new panel is set on top of an earlier panel, is set down touching it,
  is more than 10-20 cm away, or is set down face down while the others are face up.
- **SOP rule broken:** Step 10 (batch sessions: alongside, all faces up, within 10-20 cm, not touching).
- **Coaching note:** lay the finished panels out in a row, all faces up; do not stack them.

**Violation: Driver or parts left out of place.**

- **Visible cue:** at the end of Step 11 the driver is not at the right edge, or unused brackets, screws,
  legs or shims are left on the table instead of in the parts tray.
- **SOP rule broken:** Step 11 (return the driver to the right edge and unused parts to the parts tray).
- **Coaching note:** clear the driver and the loose parts before homing the arms.

**Violation: Wrong arm used for an action.**

- **Visible cue:** any step that specifies the left gripper or the right gripper is performed with the
  opposite gripper.
- **SOP rule broken:** any step that specifies a gripper, including Steps 1, 2.1, 2.3, 3.1, 3.2, 4.1,
  5.1, 6, 7, 9.1, 10 and 11.
- **Coaching note:** operator confusion about left vs right roles. Walk through the SOP step by step with
  the operator.

**Violation: Re-grip on a pick or grasp.**

- **Visible cue:** the operator closes on the panel, a bracket, a screw, a leg or a shim, finds the grip
  off, opens, and re-grips before lifting more than two times.
- **SOP rule broken:** Steps 1/3.1/4.1/6/9.1 (grasp securely, e.g., the middle of an edge, the body of a
  bracket, or the head of a screw).
- **Coaching note:** approach angle off. Practice the from-above approach so the first grip catches the
  right point.

**Violation: Repeated fiddling with a bracket, a screw or a shim.**

- **Visible cue:** the operator makes many small adjustments (more than about two) to settle a bracket on
  its layout mark, a bit in a screw head, or a shim under a foot, rather than settling it in one or two
  corrections.
- **SOP rule broken:** the positioning/fastening/shimming sub-steps (settle in one or two small
  adjustments).
- **Coaching note:** grip or approach is off, forcing repeated correction. Tighten the approach so each
  bracket and shim lands close to target.

**Violation: Arms not fully at home position at episode end.**

- **Visible cue:** in the final frame, both arms are close to the home position but not exactly at it
  (gripper not fully open, or arm position visibly off home).
- **SOP rule broken:** Step 11 (return to home position with grippers open).
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
- **Defective panel:** Cause: a warped, split or unmarked panel, or a layout mark that cannot be read,
  through no fault of the operator. Replace before the next episode.
- **Defective bracket or screw:** Cause: a bent bracket, a stripped boss, or a screw with a damaged screw
  head. Replace before the next episode.
- **Defective leg:** Cause: a bent leg, a damaged stud, or a leg short enough that two shims do not
  remove the wobble. Replace before the next episode.
- **Defective driver:** Cause: a worn bit, a bit that does not match the screw head, or a driver that
  will not turn. Replace before the next episode.

## After each episode: repeat or reset

- **Batch sessions (e.g., 4x):** if fewer than the target number are legged, return to Step 1 with the
  next panel. Once the target number is legged and placed at the back-right, reset the workspace before
  the next session.
- Clear the working area and re-run the Setup checklist before the next session.

### After the episode: reset the workspace

This part is not recorded. It is just how you reset the table for the next episode.

- With recording off, take the legged panel(s) from the back-right to the working area.
- Take out any shims, turn each leg out of its boss, back out all 16 screws, and take each bracket off
  the panel.
- Set the bare panel(s) in the start zone for the next episode's config — back-left (Config L),
  front-center (Config M) or front-right (Config R) — face down, with the four layout marks visible, leaving
  the other two zones clear.
- Return the brackets, screws, legs and shims to the parts tray at the front-left, and the driver to the
  right edge.
- Discard any stripped screw and any panel with a stripped hole.
- Confirm the table surface is clear of any objects other than the panel(s) and the parts tray in their
  designated zones.
- Go through the Setup checklist again before starting the next episode.

**Warning:** The table must be clear except for the panel(s) in the start zone, the parts tray at the
front-left, and the driver at the right edge.

## Annotation subtasks

1. Move one panel from the input area to the center working area
2. Square the panel (flat, face down, layout marks visible, underside clear)
3. Position the four brackets on the layout marks
4. Start every screw by hand at all four brackets
5. Drive the 16 screws to seat in a diagonal order
6. Thread a leg into each bracket
7. Flip the panel onto its legs
8. Wobble-test all four corners
9. Shim the short leg if the panel wobbles
10. Move the legged panel to the back-right output area
11. Return the driver and the parts, and home the arms
