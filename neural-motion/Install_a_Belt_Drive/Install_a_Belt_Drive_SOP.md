# Install a Belt Drive SOP (1x Episode: 1 Belt Drive)

One episode installs one belt onto one two-pulley drive. The table begins with the **drive plate** on the
assembly spot, just right of the center of the table. The plate carries a fixed **drive pulley** at the
back-right and a **tension pulley** on the **tensioner arm** at the front-left. The arm starts released, so
the two pulleys sit close together and the belt goes on slack. A **belt tray** with one belt stands in the
**start zone** for the episode's config.

The order never changes: route the belt over the drive pulley first and the tension pulley second, seat it
in both grooves, lever the tensioner arm to its stop, align the tracking at both pulleys, spin-test the
drive, then lock the tensioner screw. Nothing is levered until the belt is seated in both grooves. The lock
screw is not turned until the spin test passes. The episode does not end until the lever is released and the
tensioner arm holds on its own.

The right gripper carries the belt, routes it over both pulleys, seats it in the grooves, corrects the
tracking, drives the spin test, and turns the lock screw. The left gripper presses the drive plate flat
against the table while the belt goes on, then holds the tensioner lever at the stop until the screw is
locked. The left gripper stays on the left of the plate and never reaches across it. The right gripper works
the plate, the belt tray, and the lock screw.

The table is set up in one of three ways. Only the belt tray moves; the drive plate, both pulleys, the
tensioner arm, and the lock screw are in the same place in all three.

* **Config M:** the belt tray is at the front-center, in front of the assembly spot.
* **Config R1:** the belt tray is at the front-right.
* **Config R2:** the belt tray is at the back-right, behind and to the right of the plate.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the belt tray stands at the front-center (**Config M**), the front-right
  (**Config R1**), or the back-right (**Config R2**). One config per episode, chosen before recording and
  never changed mid-episode.
* **Same-side rule:** the **right gripper** takes the belt from the tray in all three configs. The left side
  of the table is never a start zone, because the left gripper is on the plate's left edge while the belt
  goes on and cannot leave it to fetch the belt. No arm reaches across the table.
* **Fixed roles:** everything else is the same in all three configs — the left gripper holds the plate, then
  the lever; the right gripper routes, seats, tracks, spin-tests, and locks; and the order is route, seat,
  lever, align, spin-test, lock.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the drive plate with both pulleys, the tensioner arm and
   its lever, the lock screw, and the belt tray in the start zone for this episode's config.
3. The drive plate is visible from above, so both pulley grooves, both flanges of each pulley, the mark on
   each pulley, and the belt stripe can be seen.
4. Both arms are at home with grippers open.
5. The table is bare apart from the drive plate, the belt tray, and robot hardware.
6. The right arm reaches the belt tray in all three start zones (front-center, front-right, back-right), both
   pulleys, and the lock screw without stretching. The left arm reaches the left edge of the drive plate and
   the lever without stretching.

### Materials checklist

1. One **drive plate** lies on the **assembly spot**, just right of the center of the table, square to the
   front edge and flat on the table.
2. The **drive pulley** is fixed at the back-right of the plate. It carries a **drive knob** standing up on
   its top face and a painted **mark** on its top face.
3. The **tensioner arm** pivots at the back-left corner of the plate. The **tension pulley** sits on the
   arm and carries its own painted **mark**. The arm's free end is the **lever**, which sticks out to the
   front-left.
4. The tensioner arm starts **released**: the lever is back at its loose position, the two pulleys sit at
   their closest, and there is slack in the belt path.
5. The **lock screw** is a wing-head screw in the arm's curved **slot**, where the arm crosses the middle of
   the plate. It starts **loose**, backed off far enough that the arm swings freely by hand.
6. One **belt** lies flat in the **belt tray**, untwisted, with its painted **stripe** facing up. The tray
   stands in the start zone for this episode's config, clear of the plate:
   * **Config M:** front-center, in front of the assembly spot
   * **Config R1:** front-right
   * **Config R2:** back-right, behind and to the right of the plate
7. Both pulley grooves are clean and dry, both flanges are unchipped, and the belt has no cracks or frayed
   edges.
8. Keep the left side of the table clear. The left gripper works from there onto the plate and the lever.
9. Before collection, confirm by hand that the belt drops over both pulleys with the arm released, that
   levering the arm to its stop makes the belt taut with no sag, that the lock screw holds the arm at the
   stop when the lever is let go, and that pushing the drive knob turns the drive pulley and the belt turns
   the tension pulley with it.

### Workspace layout

- **Assembly spot:** just right of the center of the table — the drive plate stays here all episode
- **Back-right of the plate:** the fixed drive pulley with its drive knob
- **Front-left of the plate:** the tensioner arm, the tension pulley, and the lever
- **Middle of the plate:** the lock screw in the arm's slot
- **Start zone:** the belt tray with one belt — front-center (Config M), front-right (Config R1), or
  back-right (Config R2), one per episode
- **Left side:** kept clear, so the left gripper can come in onto the plate's left edge and the lever

### Arm assignments

- **Left gripper:** presses the drive plate flat against the table by its left edge while the belt is routed
  and seated, then pushes the tensioner lever to the stop and holds it there until the lock screw is closed,
  so the arm cannot spring back and the plate cannot slide. It never fetches the belt, in any config.
- **Right gripper:** carries the belt from the tray in all three configs, routes it over the drive pulley
  then the tension pulley,
  seats it in both grooves, corrects the tracking, drives the spin test on the drive knob, and turns the
  lock screw closed.

## Vocabulary

- **Drive plate:** the flat plate the belt drive is built on. It stays on the assembly spot for the whole
  episode and is never lifted.
- **Drive pulley:** the wheel fixed at the back-right of the plate. It is the wheel the spin test drives.
- **Tension pulley:** the wheel carried on the tensioner arm at the front-left of the plate. It moves when
  the arm moves.
- **Groove:** the channel around the outside of a pulley that the belt runs in.
- **Flange:** the raised rim on each side of a groove. The flanges keep the belt from walking off.
- **Belt:** the rubber loop that runs around both pulleys.
- **Start zone:** where the belt tray stands at the start of the episode — front-center (**Config M**),
  front-right (**Config R1**), or back-right (**Config R2**). One per episode, chosen before recording and
  never changed mid-episode.
- **Stripe:** the painted line running all the way around the outside face of the belt. If any part of the
  stripe faces in toward the pulley, the belt is twisted.
- **Span:** either of the two straight runs of belt between the two pulleys.
- **Tensioner arm:** the arm that carries the tension pulley and pivots at the back-left corner of the plate.
- **Lever:** the free end of the tensioner arm, sticking out to the front-left. Pushing it toward the front
  edge swings the tension pulley away from the drive pulley and tightens the belt.
- **Released:** the lever is back at its loose position, so the belt path is slack and the belt lifts on and
  off by hand.
- **Stop:** the post at the front-left of the plate that the tensioner arm comes up against. The arm can go
  no further once it touches the stop.
- **Lock screw:** the wing-head screw in the arm's slot. Turned closed, it holds the arm where it is.
- **Wing:** the flat head of the lock screw that the right gripper pinches to turn it.
- **Belt seated:** the belt sits down inside the groove, all the way round, with no part of it up on a
  flange and no part of it above the groove.
- **Centered:** the belt sits in the groove with a strip of bare groove showing on both sides, between the
  belt edge and each flange.
- **Riding a flange:** one edge of the belt is up against or climbing onto a flange, and no bare groove
  shows on that side.
- **Tracking:** where the belt sits across the width of each groove. Tracking is good when the belt is
  centered at both pulleys.
- **Taut:** both spans are straight with no sag in them.
- **Turns with it:** the tension pulley's mark moves whenever the drive pulley's mark moves.
- **Slip:** the drive pulley turns but the tension pulley's mark stops or falls behind.
- **Bind:** the drive pulley will not turn any further when the drive knob is pushed.
- **Full turn:** the drive pulley has gone all the way around, so its mark comes back to where it started.
- **Locked:** the lock screw has been turned closed until it stops, and the tensioner arm stays at the stop
  after the left gripper lets go of the lever.

## Steps

Run Steps 1–7 in order on the one belt drive, then end the episode with Step 8. Only the pick in 2.1 depends
on the config: the **right gripper** takes the belt from the tray at the front-center (Config M), the
front-right (Config R1), or the back-right (Config R2). Every other line is the same in all three configs.

### Step 1: Hold the drive plate down

**Goal:** the drive plate is pinned flat on the assembly spot and cannot slide while the belt goes on.

- With the **left gripper**, press down on the **left edge** of the drive plate and hold it against the
  table.
- Keep the **left gripper** there through Steps 2 and 3.

**Check:** the plate is flat on the table, square to the front edge, and does not slide when the left
gripper presses. If the plate is crooked, straighten it with the left gripper first, then press it down.

**Expected state:** the plate is held, the tensioner arm is released, and the lock screw is loose.

### Step 2: Route the belt over the two pulleys

**Goal:** the belt hangs over both pulleys, flat and untwisted, with the arm still released.

- With the **left gripper**, keep pressing the drive plate down.
- Carry the belt in one go, straight from the tray to the plate. Do not set it down on the plate or the
  table on the way.
- Hold the belt by its outside face only. Do not hook the gripper tip inside the loop.
- Leave the tensioner arm released for the whole step. Do not push the lever yet.
- Drop the belt over each pulley. Do not stretch it, roll it, or work it over a flange.

#### 2.1 Over the drive pulley

- **IF the belt tray is at the front-center (Config M):** with the **right gripper**, pinch the belt by its
  outside face, lift it out of the tray in front of the plate, and hold it flat above the plate.
- **IF the belt tray is at the front-right (Config R1):** with the **right gripper**, pinch the belt by its
  outside face, lift it out of the tray, and hold it flat above the plate.
- **IF the belt tray is at the back-right (Config R2):** with the **right gripper**, pinch the belt by its
  outside face, lift it out of the tray behind the plate, and bring it forward flat above the plate.

Then, in all three:

- With the **right gripper**, lower the belt so the far side of the loop drops over the **drive pulley** and
  sits on its groove.

#### 2.2 Over the tension pulley

- With the **right gripper**, take the near side of the loop and lay it over the **tension pulley**.
- Let go once the belt rests on both pulleys.

**Expected state:** the belt hangs slack around both pulleys, the belt tray is empty, and the tensioner arm
is still released.

**Check:** the belt is on both pulleys, the **stripe** shows all the way round on the outside face, and the
belt is not caught under a pulley or trapped against the plate. If the stripe disappears anywhere, the belt
is twisted: with the right gripper, lift the belt off the tension pulley, untwist it flat, and lay it back
on.

### Step 3: Seat the belt in both grooves

**Goal:** the belt sits down inside both grooves, all the way round, while the belt is still slack.

- With the **left gripper**, keep pressing the drive plate down.
- With the **right gripper**, close the gripper and run its tip along the top of the belt where the belt
  meets the **drive pulley**, pressing the belt down into the groove.
- With the **right gripper**, do the same where the belt meets the **tension pulley**.
- Press the belt down only. Do not pull the belt sideways and do not pry under it with the tip.

**Expected state:** the belt is seated in both grooves, both spans are still slack, and the arm is still
released.

**Check:** the belt is down in both grooves with no part of it up on a flange, and both spans run straight
from one pulley to the other. If a part of the belt sits on a flange or above the groove, press it down
again with the right gripper. If it will not drop in, lift the belt off that pulley with the right gripper
and lay it back on.

### Step 4: Lever the tensioner to the stop and hold it

**Goal:** the tensioner arm is at its stop, the belt is taut, and the left gripper holds it there.

- With the **left gripper**, let go of the plate edge and take the **lever**.
- With the **left gripper**, push the lever toward the **front edge** in one steady move until the tensioner
  arm comes up against the **stop**.
- Push until the arm touches the stop, then stop pushing. Do not force the arm against the stop and do not
  jerk the lever.
- Keep the **left gripper** on the lever, holding the arm at the stop, through Steps 5, 6, and 7.
- Do not let the lever spring back at any point in Steps 5, 6, or 7.

**Expected state:** the tensioner arm is against the stop, both spans are **taut** with no sag, and the left
gripper is holding the lever.

**Check:** the arm is touching the stop, both spans are taut, and the belt is still in both grooves. If a
span still sags, the arm is short of the stop: with the left gripper, push the lever a little further until
the arm touches. If the belt came out of a groove while the lever moved, ease the lever back to released
with the left gripper, reseat the belt with the right gripper as in Step 3, then lever again.

### Step 5: Align the tracking at both pulleys

**Goal:** the belt is centered in the groove at both pulleys, with the arm still at the stop.

- With the **left gripper**, keep holding the lever at the stop.
- Look at the **drive pulley** first, then the **tension pulley**. Check both, every episode.
- At each pulley, look for a strip of bare groove on both sides of the belt.
- If the belt is **riding a flange**, use the **right gripper**: close the gripper and push the edge of the
  belt sideways, away from that flange, at the point where the belt leaves the pulley, until a strip of bare
  groove shows on that side.
- Push on the edge of the belt only. Do not pry the tip under the belt and do not pull the belt up off the
  pulley while it is taut.
- If the belt will not move sideways, ease the lever back to released with the **left gripper**, reseat the
  belt with the **right gripper** as in Step 3, then lever to the stop again as in Step 4 and look again.

**Expected state:** the belt is centered at both pulleys, the arm is still at the stop, and both spans are
still taut.

**Check:** bare groove shows on both sides of the belt at the drive pulley and at the tension pulley. If it
does not at either pulley, correct that pulley before going on to Step 6.

### Step 6: Spin-test the drive

**Goal:** the drive pulley makes two full turns, the tension pulley turns with it, and the belt stays
centered.

- With the **left gripper**, keep holding the lever at the stop.
- With the **right gripper**, close the gripper and set its tip against the **drive knob**.
- Push the knob sideways to drive the drive pulley around. Lift the tip clear, set it back on the knob, and
  push again.
- Keep pushing until the drive pulley has made **two full turns**, so its mark comes back to where it
  started twice.
- While the drive pulley turns, watch the **mark** on the tension pulley. It must move every time the drive
  pulley moves.
- While the drive pulley turns, watch the belt at both pulleys. It must stay centered.
- Drive from the drive knob only. Do not push on the belt, do not turn the tension pulley, and do not grab a
  pulley rim and twist it.
- If the drive pulley makes both turns, the tension pulley turns with it, and the belt stays centered, go to
  Step 7.
- If the tension pulley's mark stops or falls behind, there is **slip**. If the drive pulley will not go any
  further, there is **bind**. If the belt walks onto a flange, the tracking is off. In all three cases, go
  back to Step 5, correct the belt, then run Step 6 again from the start.
- If the same fault comes back after two corrections, stop, end the episode at Step 8 with the screw left as
  it is, and log the plate for a station check.

**Check:** the drive pulley made two full turns, the tension pulley's mark moved with it every time, the
belt is still centered at both pulleys, and the arm is still at the stop.

### Step 7: Lock the tensioner screw

**Goal:** the lock screw is closed and the tensioner arm holds at the stop on its own.

- With the **left gripper**, keep holding the lever at the stop until this step says to let go.
- With the **right gripper**, pinch the **wing** of the lock screw and turn it **clockwise** a quarter turn.
- Open the **right gripper**, take the wing again at the start of a fresh quarter turn, and turn again.
- Repeat these quarter turns until the screw stops turning. Do not turn more than a quarter turn in one grip
  and do not keep forcing the screw once it stops.
- With the **left gripper**, let go of the lever and move the left gripper clear of the plate.
- Watch the tensioner arm as the lever is released. It must stay against the stop.

**Expected state:** the lock screw is closed, the arm sits against the stop with nothing holding the lever,
both spans are taut, and the belt is centered at both pulleys.

**Check:** the arm did not move when the left gripper let go, and the belt is still centered at both
pulleys. If the arm sprang back, take the lever again with the left gripper, push the arm back to the stop,
and turn the screw closed again with the right gripper as above.

### Step 8: End the episode

**Goal:** recording ends with the belt installed, tensioned, tracked, spin-tested, and locked.

1. Confirm the belt is seated and centered at both pulleys, both spans are taut, the tensioner arm is at the
   stop with the lock screw closed, the belt tray is empty, and the drive plate is still square on the
   assembly spot.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

1. With recording off, back the lock screw off by hand until the tensioner arm swings freely.
2. Ease the tensioner arm back to released, so the two pulleys sit at their closest.
3. Lift the belt off the tension pulley, then off the drive pulley, and lay it flat in the belt tray with its
   stripe facing up and no twist in it. Stand the tray in the start zone for the next episode's config —
   front-center (Config M), front-right (Config R1), or back-right (Config R2).
4. Set the drive plate square on the assembly spot, flat against the table.
5. Wipe grit, dust, and rubber crumbs out of both pulley grooves.
6. Inspect the parts. Replace the belt if it is cracked, frayed, glazed, or stretched so far that levering to
   the stop no longer makes it taut. Replace a pulley if a flange is chipped or the groove is worn. Replace
   the lock screw if its thread no longer holds the arm. Tighten the pivot or the stop if either is loose in
   the plate.
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

**Note on the start position:** the violations below were written for Config R1 (belt tray at the
front-right). The pickup and arm-role cues will be rewritten later to cover all three start positions; they
are left as they are for now. Until then, anything that does not match the episode's config goes under
**Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the belt tray is not in
  the start zone for the config; the left gripper leaves the plate to fetch the belt, or a gripper reaches
  across the table for it; or the wrong IF line is followed.
- **SOP rule broken:** the start position and the same-side rule (the right gripper takes the belt from the
  tray in all three configs, the left gripper stays on the plate's left edge, and no arm reaches across the
  table; the IF line followed is the one for the config on the table).
- **Coaching note:** look where the belt tray is before the first reach, then follow that config's IF line
  in Step 2.

**Violation: Drive plate not held**
- **Visible cue:** the left gripper is off the left edge of the drive plate while the right gripper routes or
  seats the belt, and the plate slides, lifts, or is chased across the spot.
- **SOP rule broken:** Step 1 (the left gripper presses the drive plate down by its left edge and holds it
  there through Steps 2 and 3).
- **Coaching note:** left gripper on the plate first, and leave it there until the lever needs it.

**Violation: Drive plate moved off the assembly spot**
- **Visible cue:** the drive plate is lifted, turned, dragged, or ends the episode out of square with the
  front edge.
- **SOP rule broken:** Steps 1–7 (the drive plate stays flat and square on the assembly spot for the whole
  episode and is never lifted).
- **Coaching note:** bring the belt to the plate; never move the plate to the belt.

**Violation: Belt mishandled on the way in**
- **Visible cue:** the belt is set down on the plate or the table on the way from the tray, is picked up by
  its inside face, or the gripper tip is hooked inside the loop to carry it.
- **SOP rule broken:** Step 2 (carry the belt in one go, straight from the tray to the plate, held by its
  outside face).
- **Coaching note:** one lift, outside face, straight to the plate.

**Violation: Belt routed in the wrong order**
- **Visible cue:** the belt goes over the tension pulley before it is over the drive pulley.
- **SOP rule broken:** Step 2 (drive pulley first in 2.1, tension pulley second in 2.2).
- **Coaching note:** far pulley first, then lay the near side over the tension pulley.

**Violation: Belt stretched or forced onto a pulley**
- **Visible cue:** the belt is pulled hard, rolled over a flange, or worked on with the gripper tip under it,
  instead of being dropped over the pulley; or the lever has already been pushed and the belt is forced onto
  a tensioned pulley.
- **SOP rule broken:** Step 2 (leave the arm released and drop the belt over each pulley without stretching,
  rolling, or working it over a flange).
- **Coaching note:** slack first, then the belt drops on. If it needs force, the arm is not released.

**Violation: Belt left twisted**
- **Visible cue:** the stripe on the belt disappears somewhere around the loop, or the belt shows a visible
  half-turn in a span, and the episode goes on anyway.
- **SOP rule broken:** Step 2 (the stripe shows all the way round on the outside face before Step 3).
- **Coaching note:** follow the stripe all the way round with your eye before you seat it.

**Violation: Belt not seated in a groove**
- **Visible cue:** part of the belt sits on a flange or above the groove at either pulley, and the step moves
  on.
- **SOP rule broken:** Step 3 (the right gripper presses the belt down into the groove at both pulleys, with
  no part of it up on a flange).
- **Coaching note:** press it down at both pulleys and look all the way round before you touch the lever.

**Violation: Tensioner levered before the belt is seated**
- **Visible cue:** the left gripper pushes the lever while part of the belt is still on a flange, above a
  groove, or twisted.
- **SOP rule broken:** Steps 3 and 4 (the belt is seated in both grooves before the lever is pushed).
- **Coaching note:** seat first, lever second. Tension on an unseated belt only jams it worse.

**Violation: Tensioner arm not at the stop, or forced past it**
- **Visible cue:** the arm is left short of the stop with sag still showing in a span; or the left gripper
  jerks the lever, or keeps pushing and straining after the arm has met the stop.
- **SOP rule broken:** Step 4 (push the lever in one steady move until the arm touches the stop, then stop
  pushing).
- **Coaching note:** one steady push to the stop, no jerk, no extra strain.

**Violation: Lever released before the screw is locked**
- **Visible cue:** the left gripper lets go of the lever, or drifts off it, during Step 5, 6, or the screw
  turns, and the arm springs back off the stop.
- **SOP rule broken:** Steps 4 and 7 (the left gripper holds the lever at the stop through Steps 5, 6, and 7,
  and lets go only after the screw stops turning).
- **Coaching note:** the left gripper stays on the lever until the screw is closed.

**Violation: Tracking check skipped**
- **Visible cue:** the spin test starts with no look at the belt in the grooves after the lever was pushed.
- **SOP rule broken:** Step 5 (check the tracking at both pulleys after levering, every episode).
- **Coaching note:** every lever pull moves the belt. Look before you spin.

**Violation: Tracking checked at only one pulley**
- **Visible cue:** the belt is checked or corrected at one pulley only, and the other pulley is never looked
  at before the spin test.
- **SOP rule broken:** Step 5 (look at the drive pulley first, then the tension pulley; check both).
- **Coaching note:** two pulleys, two looks. Name them out loud as you check them.

**Violation: Belt left riding a flange**
- **Visible cue:** at either pulley the belt is up against or climbing a flange, with no bare groove on that
  side, and the episode goes on to the spin test or the ending.
- **SOP rule broken:** Step 5 (the belt is centered at both pulleys, with bare groove showing on both sides,
  before Step 6).
- **Coaching note:** bare groove on both sides at both pulleys, or it is not aligned yet.

**Violation: Tracking corrected the wrong way**
- **Visible cue:** the right gripper pries its tip under the taut belt, pulls the belt up off a pulley while
  it is taut, or reseats the belt without the left gripper easing the lever back first.
- **SOP rule broken:** Step 5 (push sideways on the edge of the belt only; to reseat, ease the lever back to
  released first, then reseat and lever again).
- **Coaching note:** push the edge sideways. If it will not move, take the tension off before you touch the
  belt.

**Violation: Spin test skipped or cut short**
- **Visible cue:** the episode ends without the right gripper driving the drive knob, or the drive pulley's
  mark comes back to its start fewer than two times.
- **SOP rule broken:** Step 6 (drive the drive pulley two full turns, so its mark comes back to where it
  started twice).
- **Coaching note:** two full turns of the drive pulley, every episode, before the screw.

**Violation: Spin test driven from the wrong place**
- **Visible cue:** the right gripper pushes on the belt, turns the tension pulley, or grabs a pulley rim and
  twists it instead of pushing the drive knob sideways.
- **SOP rule broken:** Step 6 (set the closed gripper tip against the drive knob and push it sideways; drive
  from the drive knob only).
- **Coaching note:** knob only, tip on the knob, push sideways.

**Violation: Slip or bind ignored**
- **Visible cue:** the tension pulley's mark stops or falls behind, the drive pulley will not turn further,
  or the belt walks onto a flange during the spin test, and the episode moves on to the screw or the ending.
- **SOP rule broken:** Step 6 (on slip, bind, or a belt walking onto a flange, go back to Step 5, correct the
  belt, and run Step 6 again from the start).
- **Coaching note:** watch the tension pulley's mark, not just the drive pulley. If it stalls, fix and retest.

**Violation: Correction not re-tested**
- **Visible cue:** the belt is recentered or reseated after a slip, bind, or flange climb, and the episode
  goes to the screw with no fresh pair of full turns.
- **SOP rule broken:** Step 6 (run Step 6 again from the start after every correction).
- **Coaching note:** every fix earns two more full turns.

**Violation: Lock screw left loose**
- **Visible cue:** the episode ends with the wing never turned, or turned only part way, and the screw still
  stands off the arm.
- **SOP rule broken:** Step 7 (turn the screw clockwise in quarter turns until it stops turning).
- **Coaching note:** quarter turn, re-grip, again, until it stops.

**Violation: Lock screw turned the wrong way or forced**
- **Visible cue:** the right gripper turns the wing counter-clockwise, twists more than a quarter turn in one
  grip, or keeps forcing the screw after it has stopped.
- **SOP rule broken:** Step 7 (clockwise, a quarter turn per grip, and stop once the screw stops).
- **Coaching note:** clockwise, small bites, let go and re-grip. Stop when it stops.

**Violation: Lock not confirmed**
- **Visible cue:** the left gripper never lets go of the lever before the arms are sent home, or it lets go
  and nothing watches the arm, so the episode ends without showing the arm holds on its own.
- **SOP rule broken:** Step 7 (the left gripper lets go of the lever, moves clear, and the arm is seen to
  stay against the stop).
- **Coaching note:** let the lever go and watch the arm. A lock you did not see hold is not a lock.

**Violation: Work done out of order**
- **Visible cue:** the steps run out of sequence, for example the screw is locked before the spin test, the
  spin test runs before the tracking is checked, or the lever is pushed before the belt is on both pulleys.
- **SOP rule broken:** Steps 2–7 (route, seat, lever, align, spin-test, lock, in that order).
- **Coaching note:** the order is the task. Say the next step's name before you move.

**Violation: Wrong arm used**
- **Visible cue:** an action assigned to one gripper is done by the other, including the left gripper routing
  or seating the belt, correcting the tracking, driving the spin test, or turning the lock screw, or the right
  gripper pushing or holding the lever.
- **SOP rule broken:** Steps 1–7 (the right gripper routes and seats the belt, corrects the tracking, drives
  the spin test, and turns the lock screw; the left gripper holds the plate, then the lever).
- **Coaching note:** right gripper does the belt and the screw, left gripper holds the plate and the lever.

**Violation: Belt or supply knocked off its spot**
- **Visible cue:** the belt is dropped on the plate, the table, or the floor, or the belt tray is tipped,
  pushed off its spot, or spilled.
- **SOP rule broken:** Steps 2–7 (keep the belt and the belt tray on their spots through the install).
- **Coaching note:** work slower and lower over the table, and keep the carry short.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before the lock is confirmed, an arm is not home, a gripper is closed, or
  an arm does something else after homing.
- **SOP rule broken:** Step 8 (confirm the end state, return both arms home with grippers open as their final
  action, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than
tagging them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- The belt is stretched, cracked, or glazed, so a correctly levered arm still leaves it slack or slipping.
- A pulley is loose on its shaft, or its groove is worn, so a correctly seated belt cannot stay centered.
- A flange is chipped or burred, so the belt climbs off however it is seated.
- The lock screw's thread is stripped, so a fully turned screw does not hold the arm at the stop.
- The tensioner pivot or the stop is loose in the plate, so the arm moves after the screw is closed.

## Annotation subtasks (from SOP)

1. Press the drive plate flat and hold it with the left gripper
2. Carry the belt from the tray and drop it over the drive pulley
3. Lay the belt over the tension pulley
4. Seat the belt in both pulley grooves
5. Push the lever to the stop and hold the tensioner arm there
6. Check and center the belt at the drive pulley and the tension pulley
7. Drive the drive knob two full turns and watch the tension pulley's mark
8. Turn the lock screw closed in quarter turns
9. Release the lever and confirm the arm holds at the stop
10. Confirm the end state, return both arms home, and end the episode
