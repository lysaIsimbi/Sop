# Press-Fit Four Bushings SOP (4x)

This SOP covers press-fitting a bushing into the bore of a part using a two-arm robot system and a hand
arbor press, repeated for four parts in one episode. Both arms are used throughout: the grippers
cooperate to seat the part, align the bushing to the bore, drive the press lever, and check the result
with a straightedge, with the left and right grippers taking the specific roles called out in each step.
The task runs from four unpressed parts in the start zone and four loose bushings at the back-left of the
table to four pressed parts at the back-right.

The table is set up in one of three ways. Only the parts move; the bushings, the press and the output zone
are in the same place in all three.

- **Config L:** the parts are at the back-left, beside the bushings.
- **Config M:** the parts are at the front-center, in front of the press station.
- **Config R:** the parts are at the front-right, and the straightedge rest is at the front-left.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

- **Start position:** the parts start at the back-left (**Config L**), the front-center (**Config M**) or
  the front-right (**Config R**). One config per episode, chosen before recording and never changed
  mid-episode.
- **Same-side rule:** the gripper on the parts' side takes each part — the left gripper in Config L and M,
  the right gripper in Config R. The gripper on the straightedge side fetches, lays and returns the
  straightedge, and the other gripper holds the part down. No arm reaches across the table for a part or
  for the straightedge.
- **Fixed roles:** the bushings stay at the back-left, the press stays at the center, and every pressed
  part goes to the back-right with the right gripper, in all three configs.
- **Working position:** the part is always moved to the press station at the centre of the table before
  any bushing is aligned or pressed.
- **Align target:** every bushing must start in the bore mouth **chamfer down, square to the bore axis,
  and centred**, before the ram is brought down.
- **Cycle order:** align the bushing to the bore, press with the hand arbor, verify flush with the
  straightedge, then move to the next part. One bushing per part, four parts per episode.
- **Pass condition:** a part is only staged as finished once the straightedge shows the bushing face
  flush with the bore face, with no visible gap or rock.

## Setup

Go through both checklists before starting the episode.

### Hardware checklist

- Cameras are on and recording
- Env camera frame includes the front and back edges of the table and is centered on the table's
    midpoint
- Both arms are at the home position with grippers open
- Table surface is clear of any objects other than the press, the straightedge and the parts

### Materials checklist

- Four parts to be pressed are placed in the start zone for this episode's config, bore up, not touching
    each other, and the other two zones are empty:
    - **Config L:** back-left, beside the bushings
    - **Config M:** front-center, in front of the press station
    - **Config R:** front-right, where the straightedge rest normally is
- Four bushings are placed at the **back-left** of the table beside the parts, chamfer up
- Hand arbor press is at the **center** of the table with the ram fully raised and the bed clear
- Straightedge is at the **front-right** of the table on its rest (Config L and M); **IF Config R**, the
    rest and the straightedge are at the **front-left**
- Back-right of the table is clear (output location for the pressed parts)

## Workspace layout

- **Start zone**: unpressed parts (input) — back-left (Config L), front-center (Config M) or front-right
  (Config R)
- **Back-left**: loose bushings (input)
- **Center**: press station (align + press + verify)
- **Front-right**: straightedge rest (Config L and M)
- **IF Config R:** the straightedge rest is at the **front-left** instead
- **Back-right**: pressed parts (output)

## Vocabulary

These are the terms used in this SOP. Operators and annotators must use this language consistently. One
term per concept, used throughout.

### Part and bushing anatomy

- **Part:** a single workpiece with one through-bore that receives one bushing.
- **Bore:** the hole in the part that the bushing is pressed into.
- **Bore mouth:** the top opening of the bore, where the bushing starts.
- **Bore face:** the flat surface of the part surrounding the bore mouth.
- **Bushing:** the cylindrical sleeve pressed into the bore.
- **Chamfer:** the bevelled lead-in edge at one end of the bushing; the chamfer always goes down, into
  the bore.
- **Bushing face:** the flat end of the bushing opposite the chamfer; this is the end the ram drives.
- **Flush:** the bushing face is level with the bore face, with no step either way.
- **Proud:** the bushing face stands above the bore face (not pressed far enough).
- **Sunk:** the bushing face sits below the bore face (pressed too far).
- **Cocked:** the bushing is tilted, so its axis is not parallel to the bore axis.
- **Seated:** the bushing has stopped moving under the ram and is fully home in the bore.

### Tooling

- **Hand arbor press:** the lever-operated press at the center of the table.
- **Press bed:** the flat table of the press that the part sits on.
- **Ram:** the vertical shaft of the press that travels down onto the bushing.
- **Press pad:** the flat face on the bottom of the ram that contacts the bushing face.
- **Lever:** the arm that drives the ram down and back up.
- **Arbor path:** the vertical space between the press pad and the part, which the ram travels through.
- **Straightedge:** the flat steel edge used to check whether the bushing is flush.
- **Straightedge rest:** the marked spot where the straightedge lives — at the front-right of the table in
  Config L and M, at the front-left in Config R.
- **Straightedge side:** the side of the table holding the straightedge rest — the right in Config L and M,
  the left in Config R. The gripper on that side handles the straightedge.

### Workspace zones

- **Start zone:** where the parts lie at the start of the episode — back-left (**Config L**), front-center
  (**Config M**) or front-right (**Config R**). One per episode, chosen before recording and never changed
  mid-episode.
- **Back-left edge:** input zone holding the loose bushings, and the unpressed parts in Config L.
- **Press station:** the center of the table where aligning, pressing and verifying happen.
- **Back-right edge:** output zone where each pressed part is placed at the back-right of the table.
- **Home position:** the default resting pose for each arm: gripper open and clear of the table.

### Actions

- **Pick:** move one part, or one bushing, to the press station.
- **Align:** start the bushing in the bore mouth chamfer down, square and centred.
- **Press:** drive the lever down in one continuous stroke until the bushing is seated.
- **Verify:** lay the straightedge across the bore and check the bushing is flush.
- **Stage:** place the finished part in the output zone (batch sessions place them in a row).
- **Next part:** return to Step 1 with the next unpressed part until four parts are done.

## Steps

Step 1 depends on where the parts are: in Config L and M the **left gripper** takes each part from the start
zone; in Config R the **right gripper** takes it from the front-right. Steps 4.1, 4.2 and 4.6 depend on the
straightedge side: in Config L and M the **right gripper** handles the straightedge from the front-right and
the left gripper holds the part down; in Config R the **left gripper** handles it from the front-left and
the right gripper holds the part down. Every other line is the same in all three configs.

### Step 1: Move a part to the working area

**Goal:** one part sits on the press bed, ready for a bushing to be aligned.

Look where the parts are before reaching for the first one.

- **IF the parts are at the back-left (Config L):** with the **left gripper**, grasp one part from the
  back-left pile by its outside edge, lift it clear of the table and carry it forward and to the right, to
  the press station.
- **IF the parts are at the front-center (Config M):** with the **left gripper**, grasp one part by its
  outside edge, lift it clear of the table and carry it straight back to the press station.
- **IF the parts are at the front-right (Config R):** with the **right gripper**, grasp one part by its
  outside edge, lift it clear of the table and carry it back and to the left, to the press station.

Then, in all three:

- Move it to the press bed at the center of the table and set it down bore up.

### Step 2: Align the bushing to the bore

**Goal:** the bushing stands in the bore mouth chamfer down, square to the bore axis and centred, with
both grippers clear of the arbor path.

#### 2.1 Seat the part on the press bed

- With the right gripper, press the part flat onto the press bed so it sits fully down with no rock, and
  the bore face is horizontal.
- Slide the part until the bore is directly under the press pad, then release.

#### 2.2 Find and pick up a bushing

- With the right gripper, grasp one bushing from the back-left by its outside diameter; if no bushing is
  clear of the others, rotate/reorient anti-clockwise until one comes free, then grasp it.
- Raise it clear of the input pile and carry it to the press station.

#### 2.3 Check orientation - chamfer down

- If the chamfer points down (toward the bore) → continue to 2.4.
- If the chamfer points up → hand the bushing to the left gripper, regrip it from the opposite end with
  the right gripper, and turn it 180° so the chamfer faces the bore and the bushing face is up.

#### 2.4 Start the bushing in the bore mouth

- Lower the bushing until the chamfer rests in the bore mouth, then release slowly.
- Do not push the bushing in by gripper force; it only needs to stand in the mouth so the ram can take it
  from there.

#### 2.5 Check alignment - square to the bore

- If the bushing stands square, with its face level and parallel to the bore face → continue to 2.6.
- If the bushing is cocked → with the left gripper, grasp it by the outside diameter, lift it clear of
  the mouth, reset it straight down into the mouth and release. If it cocks again → return to 2.1 and
  re-seat the part.

#### 2.6 Check alignment - centred in the bore

- Confirm the bushing is centred in the bore mouth, with an even ring of bore face visible all the way
  around it and no part of the chamfer sitting on the bore face.
- Make small adjustments to centre it; if it will not centre, lift it out and restart from 2.4.

#### 2.7 Clear the arbor path

- Move both grippers off the part and out of the vertical space between the press pad and the bushing.
- Confirm nothing but the bushing is under the press pad before the stroke begins.

### Step 3: Press the bushing with the hand arbor

**Goal:** the bushing is driven fully into the bore in one continuous stroke and is seated.

#### 3.1 Take the lever

- With the right gripper, grasp the press lever at its handle end.
- With the left gripper, hold the part down against the press bed, clear of the bore.

#### 3.2 Bring the press pad to contact

- Pull the lever down slowly until the press pad just touches the bushing face, then stop and confirm the
  bushing is still square and centred.
- If the bushing shifted or cocked at contact → raise the ram and return to 2.4.

#### 3.3 Press in one continuous stroke

- Drive the lever down in one smooth, continuous stroke until the bushing stops moving and the lever
  comes up hard against its stop.
- Do not pump the lever, release part way, or drive the bushing in a series of short strokes.

#### 3.4 Raise the ram and clear

- Return the lever until the ram is fully raised and the press pad is clear of the bushing.
- Release the lever with the right gripper and release the part with the left gripper.

**Warning:** The bushing should now be seated in the bore with its face at the bore face, ready to be
checked with the straightedge.

### Step 4: Verify flush with the straightedge

**Goal:** the bushing face is confirmed flush with the bore face, with no gap and no rock.

#### 4.1 Fetch the straightedge

- **IF Config L or M:** with the **right gripper**, grasp the straightedge from its rest at the front-right
  of the table. **IF Config R:** with the **left gripper**, grasp it from its rest at the front-left.
- Carry it to the press station and hold it over the part.

#### 4.2 Lay it across the bore

- Lay the straightedge flat across the bore so it spans the bushing face and lands on the bore face on
  both sides of the bore.
- **IF Config L or M:** with the **left gripper**, hold the part down so it cannot lift or rock while the
  straightedge is on it. **IF Config R:** the **right gripper** holds the part down.

#### 4.3 Read the result

- If the straightedge lies flat with no gap and does not rock → the bushing is flush; continue to 4.5.
- If the straightedge rocks on the bushing face, or lifts off the bore face → the bushing is proud.
- If a gap shows over the bushing face while the straightedge sits on the bore face → the bushing is
  sunk.

#### 4.4 Correct a proud bushing

- If proud → return the straightedge to its rest, then repeat Step 3 with a further continuous stroke
  until the bushing seats, and check again from 4.1.
- If sunk or still not flush after one further stroke → stop, flag the part, and set it aside at the
  front-left of the table rather than staging it as finished.

#### 4.5 Check a second position

- Turn the straightedge about 90° and lay it across the bore again in the second direction, then read it
  the same way.
- Both positions must read flush before the part is staged.

#### 4.6 Return the straightedge

- **IF Config L or M:** lift the straightedge clear of the part and place it back on its rest at the
  front-right of the table. **IF Config R:** place it back on its rest at the front-left.
- Release the gripper. The straightedge never stays on the part or on the press bed.

### Step 5: Move the pressed part to the back-right edge

**Goal:** the finished part rests in the designated back-right output zone.

- With the right gripper, grasp the pressed part by its outside edge.
- Move it back and to the right into the output location at the back-right of the table and set it down
  bore up.
- Place it alongside the parts already there, bores all facing up, within 10-20 cm and not touching.
- Release the gripper.

### Step 6: Next part (repeat to four)

**Goal:** all four parts are pressed, verified and staged in the output row.

- If fewer than four parts have been pressed → return to Step 1 with the next part and the next bushing.
- Do not start the next part until the current part is verified flush and staged at the back-right.
- Once four parts are pressed, verified and staged → continue to Step 7.

### Step 7: Return to home and end the episode

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

**Note on the start position:** the violations below were written for Config L (parts start at the
back-left beside the bushings, straightedge rest at the front-right). The pickup and arm-role cues will be
rewritten later to cover all three start positions; they are left as they are for now. Until then,
anything that does not match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned.**

- **Visible cue:** what the operator does does not match the config on the table — the parts are not in
  the start zone for the config; a gripper reaches across the table for a part or for the straightedge;
  the straightedge rest is not on the side that config puts it; or the wrong IF line is followed.
- **SOP rule broken:** the start position and the same-side rule (the left gripper takes each part in
  Config L and M and the right gripper in Config R; the gripper on the straightedge side fetches, lays and
  returns the straightedge while the other gripper holds the part down; the IF line followed is the one
  for the config on the table).
- **Coaching note:** look where the parts and the straightedge are before the first reach, then follow
  that config's IF lines through Steps 1, 4.1, 4.2 and 4.6.

**Violation: Wrong pickup.**

- **Visible cue:** a part or a bushing is started from the center or right instead of the back-left input
  zone, it is placed outside the press station, or it is dragged or slid across the table instead of
  being picked up (lifted clear of the surface) and carried.
- **SOP rule broken:** Steps 1 and 2.2 (pick from the back-left input zone and bring it to the press
  station). Pick means lift and carry, not drag.
- **Coaching note:** always start each part and each bushing from the back-left and bring it to the
  center before aligning. Lift it clear of the table and carry it. Do not drag or slide it across the
  surface.

**Violation: Picked more than one part or bushing at once.**

- **Visible cue:** two or more parts, or two or more bushings, are lifted/moved from the input zone in a
  single pick.
- **SOP rule broken:** Steps 1 and 2.2 (move one part, and one bushing, per cycle).
- **Coaching note:** pick exactly one part and one bushing per press cycle.

**Violation: Part not seated flat or not under the ram.**

- **Visible cue:** the press stroke starts while the part rocks on the press bed, sits on a chip or on
  another part, or the bore is visibly not under the press pad.
- **SOP rule broken:** Step 2.1 (press the part flat onto the bed with no rock and slide the bore under
  the press pad).
- **Coaching note:** seat the part flat and line the bore up under the press pad before any bushing goes
  in. A rocking part presses the bushing in cocked.

**Violation: Bushing installed backwards (chamfer up).**

- **Visible cue:** the bushing is started in the bore mouth with the chamfer facing up and the flat face
  down, so the ram drives the chamfer.
- **SOP rule broken:** Align target and Step 2.3 (chamfer down, into the bore; bushing face up).
- **Coaching note:** the chamfer is the lead-in and always goes down into the bore. Check the end
  orientation before releasing the bushing into the mouth.

**Violation: Bushing not correctly found before grasping.**

- **Visible cue:** the operator fails to find and grasp a bushing: the grip closes on empty table, on the
  part, or on two bushings at once; or, when no bushing is clear of the others, the operator reorients
  clockwise (or in an arbitrary back-and-forth direction) instead of anti-clockwise to free one.
- **SOP rule broken:** Step 2.2 (grasp one bushing by its outside diameter; if none is clear,
  rotate/reorient anti-clockwise until one comes free, then grasp it).
- **Coaching note:** grasp one bushing on its outside diameter, confirm it is actually in view and clear
  before closing the gripper. If none is free, reorient anti-clockwise (a consistent search direction)
  until one comes loose, then grasp it.

**Violation: Pressing while the bushing is not aligned (align skipped).**

- **Visible cue:** the ram is brought down while the bushing is cocked, sitting on the bore face rather
  than in the mouth, or resting on top of the bore instead of started in it, without completing the
  alignment checks in Step 2.
- **SOP rule broken:** Step 2 (square to the bore axis and centred in the bore mouth before the ram comes
  down).
- **Coaching note:** never go straight to the press. Start the bushing in the mouth square and centred
  first; a cocked start shaves the bore and jams the bushing.

**Violation: Bushing not centred in the bore mouth.**

- **Visible cue:** the bushing sits off to one side, with the ring of visible bore face uneven around it
  or part of the chamfer resting on the bore face when the stroke starts.
- **SOP rule broken:** Step 2.6 (centred, with an even ring of bore face visible all the way around).
- **Coaching note:** centre the bushing before the stroke; an off-centre start presses in crooked and
  cannot be corrected afterwards.

**Violation: Bushing pushed in by gripper instead of the press.**

- **Visible cue:** the operator drives the bushing down into the bore with gripper force during Step 2
  rather than only standing it in the mouth for the ram.
- **SOP rule broken:** Step 2.4 (rest the chamfer in the mouth and release; do not push it in by gripper
  force).
- **Coaching note:** the ram does the pressing. The gripper only starts the bushing in the mouth.

**Violation: Grippers not clear of the arbor path at the stroke.**

- **Visible cue:** at the start of the stroke a gripper, or the fingers, are still over the bushing or in
  the vertical space between the press pad and the part.
- **SOP rule broken:** Step 2.7 (both grippers off the part and out of the arbor path before the stroke
  begins).
- **Coaching note:** clear both grippers out of the arbor path and confirm only the bushing is under the
  press pad before pulling the lever.

**Violation: Stroke not continuous (pumped or part-stroked).**

- **Visible cue:** the lever is pumped, released part way and re-taken, or the bushing is driven in a
  series of short strokes rather than one smooth continuous stroke.
- **SOP rule broken:** Step 3.3 (one smooth, continuous stroke until the bushing stops moving).
- **Coaching note:** one continuous stroke to the stop. Pumping the lever steps the bushing in and leaves
  it cocked or proud.

**Violation: Contact not checked before the full stroke.**

- **Visible cue:** the lever is driven straight through without pausing at press-pad contact to confirm
  the bushing is still square and centred.
- **SOP rule broken:** Step 3.2 (pull down slowly to contact, stop, and confirm square and centred).
- **Coaching note:** stop at contact and look before committing the stroke. This is the last chance to
  catch a shifted bushing.

**Violation: Press stopped early - bushing left proud.**

- **Visible cue:** the stroke is released before the bushing stops moving or before the lever reaches its
  stop, leaving the bushing face standing above the bore face.
- **SOP rule broken:** Step 3.3 (drive until the bushing stops moving and the lever comes up against its
  stop).
- **Coaching note:** carry the stroke all the way to the lever stop; do not stop on feel part way down.

**Violation: Over-pressed - bushing driven below flush.**

- **Visible cue:** the bushing face ends up below the bore face after the stroke, or the operator adds
  further strokes to a bushing that already read flush.
- **SOP rule broken:** Pass condition and Step 4.4 (flush, no step either way; only re-press a proud
  bushing).
- **Coaching note:** stop at the lever stop and verify before adding force. A sunk bushing cannot be
  brought back out; flag the part instead.

**Violation: Ram not raised and cleared after the press.**

- **Visible cue:** the ram is left down on the bushing, or the straightedge check is attempted with the
  press pad still over the bore.
- **SOP rule broken:** Step 3.4 (return the lever until the ram is fully raised and the pad is clear).
- **Coaching note:** raise the ram fully and clear the pad before checking the part.

**Violation: Flush check skipped.**

- **Visible cue:** the part is moved to the output zone, or the next part is started, without the
  straightedge being laid across the bore at all.
- **SOP rule broken:** Step 4 and Pass condition (verify flush with the straightedge before staging).
- **Coaching note:** every part gets the straightedge before it is staged. No part is finished on a
  visual guess.

**Violation: Straightedge used incorrectly.**

- **Visible cue:** the straightedge is laid so it does not span the bushing face and land on the bore
  face on both sides, it is held above the surface instead of resting on it, the part is not held down so
  it rocks under the check, or only one position is read instead of two.
- **SOP rule broken:** Steps 4.2 and 4.5 (lay it flat across the bore, hold the part down, read two
  positions about 90° apart).
- **Coaching note:** rest the straightedge flat across the bore, hold the part still, and read it in two
  directions before calling it flush.

**Violation: Proud bushing not corrected.**

- **Visible cue:** the straightedge reads proud or rocks in Step 4.3 and the operator stages the part
  anyway, without the further stroke in Step 4.4.
- **SOP rule broken:** Step 4.4 (re-press a proud bushing and check again).
- **Coaching note:** a proud reading means one more continuous stroke and a fresh check, not a pass.

**Violation: Straightedge not returned to its rest.**

- **Visible cue:** at the end of the cycle the straightedge is left on the part, on the press bed, or
  anywhere other than its rest at the front-right of the table.
- **SOP rule broken:** Step 4.6 (place the straightedge back on its rest and release).
- **Coaching note:** the straightedge lives on its rest. Return it every cycle so the bed stays clear for
  the next part.

**Violation: Wrong cycle order.**

- **Visible cue:** the operator presses before aligning, verifies before pressing, or stages the part
  before the flush check is complete.
- **SOP rule broken:** Cycle order (align, press, verify, next part): Step 2 must precede Step 3, Step 3
  must precede Step 4, and Step 4 must precede Step 5.
- **Coaching note:** hold the cycle order every time: align, press, verify, then next part. Out-of-order
  cycles put unverified parts in the output row.

**Violation: Next part started before the current one is staged.**

- **Visible cue:** a second part or bushing is brought to the press station while the current part is
  still on the press bed or has not yet been moved to the back-right.
- **SOP rule broken:** Step 6 (do not start the next part until the current part is verified flush and
  staged).
- **Coaching note:** finish one part completely, stage it, then fetch the next. Two parts at the station
  confuse the pairing.

**Violation: Pressed part placement off zone.**

- **Visible cue:** in Step 5 the part is moved with the left gripper, is left on the press bed instead of
  being moved to the back-right output zone, is set down bore-down, or is released at the back-right but
  ends up noticeably off from the designated zone, without falling or requiring further correction.
- **SOP rule broken:** Step 5 (grasp the part with the right gripper and move it back and to the right
  into the back-right output zone, bore up).
- **Coaching note:** move the pressed part to the back-right output zone with the right gripper. Do not
  leave it on the bed and aim the release point more precisely; set it down bore up in the corner.

**Violation: Wrong batch placement.**

- **Visible cue:** in Step 5 the new part is stacked on top of an earlier part, is set down touching it,
  is more than 10-20 cm away, or is set bore-down while the others sit bore up.
- **SOP rule broken:** Step 5 (alongside, bores up, within 10-20 cm, not touching).
- **Coaching note:** lay the finished parts out in a row bore up; do not pile them.

**Violation: Fewer or more than four parts pressed.**

- **Visible cue:** the episode ends with fewer than four parts pressed and staged, or a fifth part is
  started after four are done.
- **SOP rule broken:** Step 6 (repeat to exactly four parts, one bushing each).
- **Coaching note:** count the output row before homing: exactly four pressed parts per episode.

**Violation: Wrong arm used for an action.**

- **Visible cue:** any step that specifies the left gripper or the right gripper is performed with the
  opposite gripper.
- **SOP rule broken:** any step that specifies a gripper, including Steps 1, 2.1, 2.2, 2.5, 3.1, 4.1, 4.2
  and 5.
- **Coaching note:** operator confusion about left vs right roles. Walk through the SOP step by step with
  the operator.

**Violation: Re-grip on a pick or grasp.**

- **Visible cue:** the operator closes on a part, a bushing, the lever or the straightedge, finds the
  grip off, opens, and re-grips before lifting more than two times.
- **SOP rule broken:** Steps 1/2.2/3.1/4.1 (grasp securely, e.g., the outside edge, the outside diameter,
  the handle end).
- **Coaching note:** approach angle off. Practice the from-above approach so the first grip catches the
  right point.

**Violation: Repeated fiddling with the part or the bushing.**

- **Visible cue:** the operator makes many small adjustments (more than about two) to settle the part on
  the bed, the bushing in the mouth, or the straightedge on the bore, rather than settling it in one or
  two corrections.
- **SOP rule broken:** the align/press/verify sub-steps (settle in one or two small adjustments).
- **Coaching note:** grip or approach is off, forcing repeated correction. Tighten the approach so the
  part and the bushing land close to target.

**Violation: Arms not fully at home position at episode end.**

- **Visible cue:** in the final frame, both arms are close to the home position but not exactly at it
  (gripper not fully open, or arm position visibly off home).
- **SOP rule broken:** Step 7 (return to home position with grippers open).
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
- **Press fault:** Cause: the ram binds or sticks, the lever slips its stop, or the press walks on the
  table during the stroke, through no fault of the operator.
- **Defective part or bushing:** Cause: a burred, undersize or oversize bore, a damaged or out-of-round
  bushing, or a bushing that cannot seat flush in any orientation, through no fault of the operator.
  Replace before the next episode.

## After each episode: repeat or reset

- **Batch sessions (e.g., 4x):** the four parts are pressed within the single episode. Once all four are
  verified flush and staged in the output row, reset the workspace before the next session.
- Clear the press station and re-run the Setup checklist before the next session.

### After the episode: reset the workspace

This part is not recorded. It is just how you reset the table for the next episode.

- With recording off, move the four pressed parts from the back-right to the start zone for the next
  episode's config — back-left (Config L), front-center (Config M) or front-right (Config R) — leaving the
  other two zones empty.
- Press each bushing back out of its bore on the arbor press using the removal support, then set the
  bushings at the back-left chamfer up, matching the initial setup state.
- Set any part flagged in Step 4.4 aside for inspection; do not return it to the input pile.
- Return the ram to fully raised and the straightedge to its rest — at the front-right, or at the
  front-left if the next episode is Config R. If the config changes to or from Config R, move the rest to
  the other side.
- Confirm the table surface is clear of any objects other than the press, the straightedge and the parts
  and bushings in their designated zones.
- Go through the Setup checklist again before starting the next episode.

**Warning:** The table must be clear except for the press at the center, the straightedge on its rest,
the bushings at the back-left and the parts in the start zone for the next episode's config.

## Annotation subtasks

1. Move one part from the input area to the press station
2. Seat the part flat on the press bed with the bore under the ram
3. Pick one bushing and orient it chamfer down
4. Align the bushing square and centred in the bore mouth
5. Press the bushing with the hand arbor in one continuous stroke
6. Verify the bushing is flush with the straightedge in two positions
7. Return the straightedge to its rest
8. Move the pressed part to the back-right output area
9. Repeat for the next part until four are pressed
10. Home the arms
