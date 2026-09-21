# Sort Salvaged Parts into Graded Bins SOP

One episode empties one salvage tray. The tray is already sitting in its start zone when recording
starts, holding seven mixed parts pulled from a teardown: screws, connectors, and fine
parts, some of them damaged. Every part is graded where it lies, lifted once, and released into the
bin that matches it. When the tray is bare, four count chips go onto the tally card, one for each
bin. The tray is empty, the four bins hold the sorted parts, and four chips sit on the card when the
episode ends.

The order never changes: screws, then connectors, then fine parts, then the tally. The tally is
never started while a part is still in the tray.

The left arm supports and the right arm works. The right gripper does all the sorting and works the
tweezers. The left gripper works the chip rack and the tally card. Neither arm crosses the middle of
the desk to take the other's zones.

Every part is graded over the tray before it is lifted. A part is never carried out of the tray and
then sent to a different bin, and a part that has landed in the bin it was graded for is never taken
back out.

Fine parts are only ever taken with the tweezers. Screws and connectors are only ever taken by the
bare gripper. One part moves at a time. The tray is never tipped, raked, shaken, or dragged to move
parts, and no part is ever released above the rim of a bin.

The desk is set up in one of three ways. Only the salvage tray moves; the bin row, the tweezer stand,
the tally card, and the chip rack are in the same place in all three.

* **Config M1:** the tray is at the middle of the desk, immediately left of the bin row.
* **Config M2:** the tray is at the back-center, behind the middle of the desk.
* **Config R:** the tray is at the back-right, behind the bin row.

Where a step depends on the setup it says so on an **IF** line — look at the desk and follow the line
that matches.

What stays constant across all sessions:

* **Start position:** the tray starts at the middle of the desk (**Config M1**), the back-center
  (**Config M2**), or the back-right (**Config R**). One config per episode, chosen before recording and
  never changed mid-episode.
* **Same-side rule:** all three start zones are on the right arm's side, so the **right gripper** takes
  every part in every config. No left zone is used, because the left gripper never takes a part: the
  bins, the tweezer stand, and the tweezers are the right arm's, and a fine part moves only with the
  tweezers. No arm reaches across the desk, and nothing is handed over.
* **Fixed roles:** everything else is the same in all three configs — the right gripper sorts and works
  the tweezers, the left gripper works the chip rack and the tally card, and the bins, the tweezer
  stand, the tally card, and the chip rack stay where they are.

## Setup

Complete both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole desk: the salvage tray in the start zone for this episode's
   config, the bin row on the right, the tweezer stand at the front right, and the tally card and chip
   rack at the front left.
3. The inside of the salvage tray is in frame from above, with all seven parts and the bare tray
   floor visible.
4. The mouth of all four bins is in frame from above, so a part can be seen going in below the rim.
5. The tweezer tips are in frame whenever the tweezers are in the gripper.
6. Both arms are at home with grippers open.
7. The desk is clear of anything but the zones listed below.
8. The right gripper reaches every corner of the salvage tray in the start zone for this episode's
   config (Config M1, M2, or R), the tweezer stand, and the mouth of all four bins, including the
   reject bin at the far right, without the arm leaning out.
9. The left gripper reaches all four chip lanes and all four card slots without reaching a joint
   limit.
10. The travel from the tray to the bin row is bare and level, and neither gripper enters the other
    arm's zones.

### Materials checklist

1. One **salvage tray** already resting in the printed outline for this episode's config, on a mat
   that keeps it from sliding, with the other two outlines bare. Nothing else stands on the desk
   except the zones below.
   * **Config M1:** the middle of the desk, immediately left of the bin row
   * **Config M2:** the back-center, behind the middle of the desk
   * **Config R:** the back-right, behind the bin row
2. The tray is shallow and open, with walls low enough that a gripper clears them on the way in and
   out, and its floor is bare except for the parts.
3. **Seven parts** lie loose in the tray in one layer, none touching and none overlapping: three
   screws, two connectors, and two fine parts.
4. The **screws** are pan head machine screws about a thumb joint long, lying flat, each long enough
   for the bare gripper to close across the shank.
5. The **connectors** are two pin plastic housings, lying flat with the pins to one side, each with
   a body wide enough for the bare gripper to close across.
6. The **fine parts** are flat washers lying flat on the tray floor, too small and too thin for the
   bare gripper to close on, and taken only with the tweezers.
7. At least one and no more than three of the seven parts are visibly damaged. Damage is obvious
   from above: a bent shank or a chewed head on a screw, a bent pin or a snapped latch on a
   connector, a cracked washer or one bent out of flat.
8. **Four bins** stand in one row immediately right of the tray, at the same depth, each in its
   printed outline with its printed label facing the front edge. Left to right: **SCREWS**,
   **CONNECTORS**, **FINE PARTS**, **REJECT**. Each bin is empty, wide at the mouth, and deep enough
   that a part released just inside the rim stays in.
9. One pair of **tweezers** lying in the tweezer stand at the front right, arms up and tips angled
   down toward the desk. The tips are flat, meet cleanly, and spring apart on their own.
10. One **tally card** at the front left, carrying four printed rows in the order SCREWS,
    CONNECTORS, FINE PARTS, REJECT, each row with one empty slot and a readable label.
11. The **chip rack** at the front left corner, with four labeled lanes in that same order, each
    lane holding four chips standing in notches and numbered 0 to 3 on their top faces.

### Workspace layout

* **Salvage tray:** the start zone — the middle of the desk (**Config M1**), the back-center
  (**Config M2**), or the back-right (**Config R**). The seven parts start here and it is bare when
  the episode ends. The tray itself never moves.
* **Bin row:** four bins in one straight line at the middle depth, immediately right of the Config M1
  outline, so every carry is a short level move and no gripper passes over another bin.
* **Tweezer stand:** the front right, between the middle of the desk and the front edge, clear of the
  bin row. The tweezers rest here before Step 3 and again at the end of it.
* **Tally card:** the front left, between the chip rack and the middle of the desk.
* **Chip rack:** the front left corner, outboard of the tally card.

The right arm's zones are the salvage tray (in all three configs), the bin row, and the tweezer stand.
The left arm's zones are the tally card and the chip rack. Nothing is shared, and neither arm reaches past the middle of
the desk at any point in the episode.

## Vocabulary

* **Arm assignment:** the right arm sorts every part, from whichever start zone the tray is in, and
  works the tweezers. The left arm counts the bins and works the chip rack and the tally card, and
  never reaches for the tray in any config. Neither arm takes the other's job, and the two never work
  at the same time.
* **Start zone:** where the salvage tray sits for the whole episode — the middle of the desk
  (**Config M1**), the back-center (**Config M2**), or the back-right (**Config R**). One per episode,
  chosen before recording and never changed mid-episode.
* **Screw:** a pan head machine screw. Taken by the bare gripper closing across the shank, never
  across the head.
* **Connector:** a two pin plastic housing. Taken by the bare gripper closing across the body, never
  on the pins.
* **Fine part:** a flat washer. Taken only with the tweezers, by pinching across its rim.
* **Damaged:** a part carrying a visibly bent, snapped, cracked, or stripped feature that is obvious
  from above without turning the part over. A part that merely looks scuffed, dull, or dirty is not
  damaged.
* **Grade:** deciding, while the part is still lying in the tray, which bin it goes to. A damaged
  part is graded REJECT whatever its type. Every other part is graded to the bin matching its type.
* **Bin mouth:** the open top of a bin, inside its rim. A part is released here and nowhere else.
* **Release point:** inside a bin mouth below the rim, or over a card slot with the chip already
  resting. A gripper opens nowhere else.
* **Bare grip:** the right gripper closing directly on a screw or a connector, with no tool in hand.
* **Tweezer grip:** the right gripper closed across the flat of the two tweezer arms near their
  middle, tips angled down. The gripper takes this hold once and keeps it for the whole of Step 3.
* **Pinch:** closing the right gripper the rest of the way so the tweezer tips meet on the part.
* **Spring open:** easing the right gripper open a little so the tips part and let the part go. The
  tweezer grip itself is not released.
* **Lift:** taking a part, a chip, or the tweezers straight down onto its grasp, closing, and
  raising it straight up until there is daylight under it, before anything moves sideways.
* **Set down:** carrying the thing level to its spot, lowering it straight down until it is resting,
  and releasing once it is resting.
* **Settled:** the chip or the tray stays put for 2 seconds after the gripper lifts clear, with
  nothing rocking, sliding, or falling over.
* **Empty tray:** the tray floor bare, with no part left in it and none caught against a wall or a
  corner.
* **Count chip:** one numbered chip from the chip rack, taken by closing across its two side faces
  with the number on top and lifting it straight up out of its notch.
* **Lane:** one labeled column of the chip rack. A chip for a row is only ever taken from the lane
  whose label matches that row.
* **Card slot:** the printed slot at the end of a tally card row. One chip rests in it, number face
  up and readable from above.

## Steps

Steps 1 to 4 are one tray. The parts are already in the tray, so the episode starts with the first
screw, not with a fetch.

Only the reach into the tray and the carry to the bin in Steps 1, 2, and 3.2 depend on the config: the
**right gripper** takes every part in all three, from the middle of the desk in Config M1, the
back-center in Config M2, or the back-right in Config R. Every other line is the same in all three
configs.

### Step 1: Sort the screws

**Goal:** all three screws out of the tray and resting in their bins, with only the connectors and
the fine parts left on the tray floor.

Look where the tray is before the first reach.

* Look over the tray and take the **screw nearest the front edge** first.
* **Grade it where it lies:** a bent shank, a chewed head, or a stripped thread sends it to
  **REJECT**. Anything else goes to **SCREWS**.
* **IF the tray is at the middle of the desk (Config M1):** the **right gripper** comes straight down
  onto the screw, closes across the **shank**, lifts it straight up until there is daylight under it,
  and carries it level a short way **sideways to the right** to the graded bin.
* **IF the tray is at the back-center (Config M2):** the **right gripper** comes straight down onto
  the screw, closes across the **shank**, lifts it straight up until there is daylight under it, and
  carries it level **behind the bin row and then forward** over the graded bin, never over another bin.
* **IF the tray is at the back-right (Config R):** the **right gripper** comes straight down onto the
  screw, closes across the **shank**, lifts it straight up until there is daylight under it, and
  carries it level a short way **forward** to the graded bin.

Then, in all three:

* Lower the gripper **inside the bin mouth below the rim**, and open.
* Lift the gripper straight up out of the bin.
* Work the remaining screws the same way, taking the one nearest the front edge each time.

The bin is decided before the lift, so a part is never carried out of the tray and then sent
somewhere else. Close on one part at a time, and never on a screw that is lying against another
part.

**Check:** no screw is left in the tray, each screw lies inside the bin it was graded for below the
rim, the connectors and fine parts are still lying where they started, no part was knocked out of
the tray, and the tray is still seated in its outline. If a screw lands on the desk, on a bin rim, or
in the wrong bin, lift it from where it landed and place it in the correct bin, then carry on.

### Step 2: Sort the connectors

**Goal:** both connectors out of the tray and resting in their bins, with only the fine parts left on
the tray floor.

* Take the **connector nearest the front edge** first.
* **Grade it where it lies:** a bent pin, a snapped latch, or a cracked housing sends it to
  **REJECT**. Anything else goes to **CONNECTORS**.
* The **right gripper** comes straight down onto the connector, closes across the **body** clear of
  the pins, and lifts it straight up.
* **IF Config M1:** carry it level sideways to the right to the graded bin. **IF Config M2:** carry it
  level behind the bin row and then forward over the graded bin, never over another bin. **IF Config
  R:** carry it level forward to the graded bin.
* Lower the gripper **inside the bin mouth below the rim**, and open.
* Lift the gripper straight up out of the bin, then work the second connector the same way.

Never close on the pins and never drag a connector across the tray floor to get a better hold. If the
first hold does not take, open, set it back down flat, and close again.

**Check:** no connector is left in the tray, each connector lies inside the bin it was graded for
below the rim, no pin was bent by the gripper, the two fine parts are still lying flat where they
started, and the tray is still seated in its outline. If a connector lands outside its bin or in the
wrong bin, lift it from where it landed and place it in the correct bin.

### Step 3: Tweeze the fine parts

**Goal:** both fine parts out of the tray and resting in their bins, the tray bare, and the tweezers
back in their stand.

**3.1 Take the tweezers**

* The **right gripper** comes down onto the flat of the two **tweezer arms** near their middle,
  closes into the **tweezer grip**, and lifts them straight up out of the stand, tips angled down.
* Carry them level to the tray without turning them.

**3.2 Move each fine part**

* Take the **fine part nearest the front edge** first, and **grade it where it lies:** cracked or
  bent out of flat sends it to **REJECT**. Anything else goes to **FINE PARTS**.
* Bring the tips down to the tray floor on either side of the part's rim, then **pinch** until the
  part is held between the tips.
* Lift straight up. **IF Config M1:** carry level sideways to the right to the graded bin. **IF Config
  M2:** carry level behind the bin row and then forward over the graded bin, never over another bin.
  **IF Config R:** carry level forward to the graded bin.
* Lower the tips **inside the bin mouth below the rim**, and **spring open**.
* Lift the tweezers straight up out of the bin, then work the second fine part the same way.

The tweezer grip is taken once and held for the whole step. Never take a fine part with the bare
gripper, and never take a screw or a connector with the tweezers.

**3.3 Return the tweezers**

* Carry the tweezers level to the **tweezer stand**, lower them until they are resting in the
  cradle with the arms up and the tips angled down, and open the gripper.
* The right gripper lifts clear.

**Check:** the tray is bare with nothing caught in a corner, both fine parts lie inside the bins they
were graded for below the rim, no part was flicked out of the tray, and the tweezers rest in the
stand tips down with the tips undamaged. If a fine part slips from the tips, take it again with the
tweezers from where it landed. It is never picked up by the bare gripper.

### Step 4: Tally the bins

**Goal:** four count chips resting in the four card slots, each matching what is in its bin.

* Count what is in the **SCREWS** bin.
* The **left gripper** closes across the side faces of the chip carrying that number in the
  **SCREWS lane**, lifts it straight up out of its notch, carries it level to the **SCREWS row**,
  lowers it flat into the slot until it is resting, and releases.
* The left gripper lifts clear.
* Do the same for **CONNECTORS**, then **FINE PARTS**, then **REJECT**, in that order, always taking
  the chip from the lane whose label matches the row.

Count the bin before going to the rack. Take each chip straight up out of its notch and leave the
chips beside it standing.

**Check:** four chips rest flat in the four card slots, settled, number face up and readable from
above, each matching the count in the bin named on its row; each chip came from its own lane; and no
other chip has been knocked over or lifted out of the rack. If a wrong chip went down, lift it
clear, stand it back in its own notch, and place the right one.

### Step 5: End the episode

* Confirm the salvage tray is bare and still seated in its outline, each of the four bins holds only
  the parts graded for it, the tweezers lie in their stand with the tips angled down, and four chips
  rest in the four card slots matching the bins.
* Return both arms home, clear of the tray and the bin row, then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Empty all four bins back into a stock box and confirm each bin is bare, upright, and still seated
   in its printed outline with its label readable.
2. Lift the four chips out of the card slots and stand each one back in its own notch in its own
   lane, number up, with every lane holding chips 0 to 3 in number order.
3. Seat the salvage tray on its mat in the printed outline for the next episode's config — the middle
   of the desk (Config M1), the back-center (Config M2), or the back-right (Config R) — leaving the
   other two outlines bare, then lay seven parts in it in one layer, none touching and none
   overlapping: three screws, two connectors, and two fine parts.
4. Vary which parts are damaged and how many between episodes rather than running the same mix every
   time. At least one and no more than three of the seven are damaged, so no bin count ever goes
   above 3.
5. Check the tweezers: tips flat, meeting cleanly, springing apart on their own, and not bent. Lay
   them in the stand with the arms up and the tips angled down.
6. Replace anything damaged: a tray that is cracked or will not sit in its outline, a bin that will
   not stand upright or whose label is unreadable, a chip whose number cannot be read, tweezers that
   will not hold a washer, or a card whose printed rows have worn away.
7. Wipe the desk and confirm the salvage tray, the four bins, the tweezer stand, the tally card, and
   the chip rack have not shifted and that every printed outline and label is readable.
8. Run both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The
visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation
label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not
delete it just because a rule was broken.

### Violations

**Note on the start position:** the violations below were written for Config M1 (the tray at the
middle of the desk, immediately left of the bin row). The pickup and arm-role cues will be rewritten
later to cover all three start positions; they are left as they are for now. Until then, anything that
does not match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the operator does does not match the config on the desk — the tray is not in
  the start zone for the config; a gripper reaches across the desk for the tray; or the wrong IF line
  is followed.
* **SOP rule broken:** the start position and the same-side rule (the tray sits in one of the three
  start zones for the whole episode, the right gripper takes every part from it in every config, no
  arm reaches across the desk; the IF line followed is the one for the config on the desk).
* **Coaching note:** look where the tray is before the first reach, then follow that config's IF lines
  through Steps 1 to 3.

**Violation: Wrong order**

* **Visible cue:** a connector is moved while a screw is still in the tray, a fine part is moved
  while a connector is still in the tray, the tweezers are taken before the tray holds only fine
  parts, or a chip goes onto the card while any part is still in the tray.
* **SOP rule broken:** Steps 1 to 4, the order never changes: screws, then connectors, then fine
  parts, then the tally.
* **Coaching note:** clear the class you are on before you start the next one.

**Violation: Arms swapped roles**

* **Visible cue:** the left gripper takes a part or the tweezers, the right gripper takes a chip or
  reaches the tally card, or either arm crosses the middle of the desk.
* **SOP rule broken:** Steps 1 to 4, the right arm sorts and works the tweezers and the left arm
  works the chip rack and the tally card.
* **Coaching note:** right sorts, left tallies. Stay on your own side.

**Violation: Bin chosen in the air**

* **Visible cue:** a part is lifted and then carried along the bin row while the arm hesitates, is
  taken toward one bin and then swung to another, or is held over the row before it goes down.
* **SOP rule broken:** Steps 1 to 3, grade the part where it lies and go straight to that bin.
* **Coaching note:** look, decide, then lift. The carry is a straight line.

**Violation: Part in the wrong type bin**

* **Visible cue:** a screw lands in the connectors bin, a connector lands in the screws bin, a fine
  part lands in either, or any good part lands in a bin that does not carry its name.
* **SOP rule broken:** Steps 1 to 3, every part that is not damaged goes to the bin matching its
  type.
* **Coaching note:** read the bin label before the gripper goes down.

**Violation: Grade ignored**

* **Visible cue:** a part with a bent shank, chewed head, bent pin, snapped latch, cracked housing,
  or cracked washer lands in a type bin, or an undamaged part lands in the reject bin.
* **SOP rule broken:** Steps 1 to 3, a damaged part goes to REJECT whatever its type, and everything
  else goes to its type bin.
* **Coaching note:** damage beats type. Check the part before you decide the bin.

**Violation: Fine part taken by the bare gripper**

* **Visible cue:** the bare gripper closes on a washer, scrapes one along the tray floor, or picks
  one up after it slips from the tweezer tips.
* **SOP rule broken:** Step 3, a fine part is only ever taken with the tweezers.
* **Coaching note:** if it is a washer, it is a tweezer job, including on the retry.

**Violation: Screw or connector taken with the tweezers**

* **Visible cue:** the tweezers are used on a screw or a connector, or the tweezers are taken from
  the stand while screws or connectors are still in the tray.
* **SOP rule broken:** Steps 1 to 3, screws and connectors are taken by the bare gripper and the
  tweezers come out only once the tray holds fine parts alone.
* **Coaching note:** the tool comes out last and only for the small stuff.

**Violation: Tweezers mishandled**

* **Visible cue:** the gripper closes on the tweezer tips instead of the flat of the arms, the tips
  are dragged across the tray floor or a bin rim, the tweezer hold is taken again in the air, or the
  tweezers are dropped, left on the desk, or left in the gripper at the end of the step.
* **SOP rule broken:** Step 3, the tweezer grip is taken once across the flat of the arms, held for
  the whole step, and the tweezers are set down resting in the stand tips down.
* **Coaching note:** grip the arms, keep the hold, put the tool back.

**Violation: Two parts moved at once**

* **Visible cue:** the gripper or the tweezers close on two parts together, or a second part comes
  up stuck to the one being lifted and is carried to a bin with it.
* **SOP rule broken:** Steps 1 to 3, one part moves at a time.
* **Coaching note:** one part, one carry. Set the passenger back down.

**Violation: Part released above the rim**

* **Visible cue:** a gripper or the tweezers open above a bin and the part falls the rest of the
  way, bounces off the rim, or lands outside the bin.
* **SOP rule broken:** Steps 1 to 3, lower inside the bin mouth below the rim before opening.
* **Coaching note:** go in over the rim before you let go.

**Violation: Part taken back out of a bin**

* **Visible cue:** a part that landed in the bin it was graded for is lifted out again, moved to
  another bin, or the contents of a bin are stirred or rearranged.
* **SOP rule broken:** Steps 1 to 3, a part that has landed in the bin it was graded for stays
  there; only a part that landed outside its bin or in the wrong bin is lifted again.
* **Coaching note:** once it is in the right bin it is finished. Leave it alone.

**Violation: Parts raked, tipped, or shaken**

* **Visible cue:** the tray is tipped, lifted, or shaken to move parts, or a gripper sweeps, drags,
  or rakes parts across the tray floor instead of lifting them one at a time.
* **SOP rule broken:** Steps 1 to 3, every part leaves the tray by being lifted straight up.
* **Coaching note:** lift each one out. The tray stays flat and still.

**Violation: Salvage tray moved**

* **Visible cue:** the tray slides, turns, or lifts out of its printed outline, or a gripper strikes
  a tray wall hard enough to shift it.
* **SOP rule broken:** Steps 1 to 3, the tray stays seated in its outline for the whole episode.
* **Coaching note:** clear the wall on the way in and on the way out.

**Violation: Tally started before the tray is empty**

* **Visible cue:** the left gripper goes to the chip rack while a part is still lying in the tray,
  or a chip is on the card before Step 3 is finished.
* **SOP rule broken:** Step 4, the tally starts only once the tray is bare.
* **Coaching note:** empty tray first, then count.

**Violation: Chip taken from the wrong lane**

* **Visible cue:** the chip placed in a row came from a lane carrying a different label, or chips
  are moved between lanes.
* **SOP rule broken:** Step 4, a row's chip comes only from the lane whose label matches that row.
* **Coaching note:** match the label to the label, then lift.

**Violation: Wrong count chip**

* **Visible cue:** the chip in a card slot does not match the number of parts in the bin named on
  that row, or a chip is lifted from the rack before the bin has been looked at.
* **SOP rule broken:** Step 4, count the bin first and place the chip that matches it.
* **Coaching note:** count the bin, then go to the rack. Never the other way round.

**Violation: Chip mishandled**

* **Visible cue:** a chip lands off its slot, number face down or sideways, is dragged out of its
  notch rather than lifted straight up, is nudged or patted into the slot after it lands, or the
  chips beside it are knocked over or lifted out of the rack.
* **SOP rule broken:** Step 4, the chip is lifted straight up out of its notch and lowered flat into
  the slot, number up, with the chips beside it left standing.
* **Coaching note:** straight up, straight down, number showing.

**Violation: Gripper released over the wrong place**

* **Visible cue:** a gripper opens over the tray, over the desk, over a bin rim, over the chip rack,
  or over open space, and what it held lands anywhere but inside a bin mouth or in a card slot.
* **SOP rule broken:** Steps 1 to 4, a gripper opens inside a bin mouth below the rim or over a card
  slot with the chip already resting, and nowhere else.
* **Coaching note:** know where it lands before you open the gripper.

**Violation: Regripped in the air**

* **Visible cue:** a gripper shifts, rolls, or seats its hold again on a part, a chip, or the
  tweezers without setting it down first.
* **SOP rule broken:** Steps 1 to 4, set a held item down before taking a new hold.
* **Coaching note:** put it down before you take a new hold.

**Violation: Item dropped, collided, or knocked something over**

* **Visible cue:** a part, a chip, or the tweezers fall onto the desk or the floor; a bin, the
  tweezer stand, the tally card, or the chip rack is struck and shifts or tips; or the two arms
  strike each other.
* **SOP rule broken:** Steps 1 to 4, keep a clear travel path and release only after a settled
  placement.
* **Coaching note:** check the path and the landing spot before you move.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a part still in the tray, a card slot empty, the tweezers
  out of their stand, or an arm away from home, or recording stops before both arms are home.
* **SOP rule broken:** Step 5, confirm the bare tray, the four bins, the tweezers, and the four
  chips, return both arms home, then stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the
episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Defective tweezers:** tips bent apart, tips that will not meet, or a pair that will not spring
  open on its own. Replace the tweezers before the next episode.
* **A part that cannot be lifted at all:** stuck to the tray floor, or too small for the tweezer
  tips to close on.
* **A part that belongs to none of the three classes,** or one whose class cannot be told from
  above. Restock the tray before the next episode.
* **More than three parts of one class or more than three damaged parts in the tray,** so a bin
  count cannot be shown on a chip. Restock the tray before the next episode.
* **Defective bin:** cracked, will not stand upright, its label unreadable, or so shallow that a
  part released below the rim bounces out.
* **Chip missing from a lane, will not stand in its notch, or its number is unreadable.**
* **Tally card slot torn, or a printed row label worn away.**
* **The salvage tray, a bin, the tweezer stand, the tally card, or the chip rack shifts out of
  place** during the episode.

## Annotation subtasks (from SOP)

1. Grade a screw in the tray and place it in its bin
2. Grade a connector in the tray and place it in its bin
3. Send a damaged part to the reject bin
4. Take the tweezers from the stand
5. Tweeze a fine part into its bin
6. Return the tweezers to the stand
7. Place one count chip in a tally card row
8. Confirm the bins and the tally card and end the episode
