# Exchange Totes with an AMR SOP (1x Episode: one exchange, in situ)

One episode exchanges one tote with a docked AMR, at the transfer station where the AMR docks. An AMR is a small mobile robot that
carries a tote on its top. The base is **passive**: it has no drive of its own, so it is pushed by hand to the front of the station and
locked there, and nothing is carried away to a table. Everything the episode touches is already at the station when recording starts:
the docked AMR mock with a full tote on its top, the empty tote on the station bench, and the panel with its scanner.

The episode runs these four actions in this order and no other: **lift the full tote off the AMR mock top, seat the empty tote on it,
scan both totes, dispatch the AMR at the panel.** The AMR is only touched while it is docked and still, and nothing is over it when it is
sent away.

The station is worked **as found**. The **AMR mock** stands docked in the **dock bay** in the middle of the station, the panel's **DOCKED**
lamp lit, with a **full tote** seated in the **tote nest** on its top. The **empty tote** stands on the bench on one side of the bay, and the
**FULL spot** on the bench on the other side is bare. The episode ends with the full tote on the FULL spot, the empty tote seated on the AMR,
both scanned, and the AMR dispatched.

**This is an in-situ task, and three things follow from that.** First, **the AMR moves**: it is touched only while the DOCKED lamp is lit and
it stands still against its dock stop, and both grippers are clear of it from the press of DISPATCH on. Second, the **AMR, the bench, and the
panel are never leaned on and never pushed**: no gripper, wrist, or forearm rests on the AMR, its nest, the bench, or the panel, and the AMR is
never shoved off its dock. Third, **each tote goes straight to its place and nowhere else**: the full tote from the AMR to the FULL spot, the
empty tote from the bench to the AMR, never set down in between.

The station is set up in one of two ways. The **FULL spot** and the **empty tote** swap sides. The dock bay, the AMR, and the panel are in the
same place in both.

* **Config L:** the FULL spot is on the **left** bench and the empty tote stands on the **right** bench.
* **Config R:** the FULL spot is on the **right** bench and the empty tote stands on the **left** bench.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says so on an **IF**
line. Look at the station and follow the line that matches.

What stays constant across all sessions:

* **Two-gripper tote rule:** every tote is lifted, carried, and set down by **both grippers together**: the **left gripper** on the tote's left
  end and the **right gripper** on its right end.
* **Panel-side rule:** the gripper on the FULL spot's side does both scans and presses DISPATCH. It is called the **panel gripper**: the **left
  gripper** in Config L and the **right gripper** in Config R.
* **Docked-only rule:** the AMR is touched only while the DOCKED lamp is lit and the AMR stands still.

Nothing is ever handed over. **The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches
over, under, around, or past the other. Nothing is moved two at a time: the grippers carry one tote together, or one gripper holds the scanner
while the other is empty and clear of the AMR.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or repositioned once
recording starts. It is parked once, before recording, and does not move again until the episode is over.

1. Push the base by hand up to the front of the station and stop it **square to it**, so the bench edge runs straight across the frame of the
   camera.
2. Stop it **centered on the dock bay**, so the middle of the base is in line with the middle of the tote nest.
3. Stop it **close enough** that both grippers reach the end walls of a tote in the nest, on the left bench spot, and on the right bench spot
   without either arm extending, and **far enough** that neither arm, wrist, nor any part of the base touches the bench, the panel, or the AMR
   while both arms work.
4. Check the **two-gripper carry**: with a tote in the nest, the **left gripper** on its left end and the **right gripper** on its right end can lift
   it clear of the nest guides and carry it level to each bench spot and back, without either arm extending and without the arms crossing.
5. Check the **panel** for the config this episode runs: the **panel gripper** reaches the scanner holster, the DISPATCH button, and the front
   label of a tote on the FULL spot and in the nest.
6. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
7. If any of lines 1 to 5 fails, push the base to a new park by hand and start again at line 1. Do not work a station the arms cannot reach
   comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the station hard enough to shift it, nothing touches
it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the dock bay and its frame includes both bench spots, the whole AMR top with its nest, the dock stop, and
   the panel with its lamps, button, and scanner.
3. The camera reads the **tote label** on the front of each tote, wherever it stands.
4. The camera sees which panel lamps are lit, and whether the AMR is still, at every moment.
5. The camera sees into the full tote well enough to see if its contents shift.
6. Both arms are at home with grippers open.
7. Both arms reach the ends of a tote in the nest and on both bench spots without extending to a joint limit.
8. The panel arm for this config reaches the holster, the button, and both tote labels without extending to a joint limit.
9. The two arms do not collide, and neither arm passes in front of the other.
10. If a place cannot be reached, re-park the base by the Base positioning steps until lines 7 to 9 hold.

### Materials checklist

1. The **transfer station** stands where it lives, fixed to the floor. It is not moved, not leaned on, and not pushed at any point. It is a bench
   at about waist height with a **dock bay**, a gap one AMR wide, in the middle, open at the back. Nothing is above the bench or the bay.
2. The **AMR mock** is a low wheeled unit that backs into the bay from behind and stands against a **dock stop** at the front of the bay. Its flat top is
   level with the bench. On its top is a **tote nest**: four low corner guides that hold a tote square.
3. The AMR stands still, brakes on, while it is docked. When dispatched, it drives out of the back of the bay (**unvalidated**: a passive mock is
   drawn out from the back by a helper off camera when the DISPATCHED lamp lights).
4. Two bench spots flank the bay, one each side, each one tote in size. The **FULL spot** is a painted outline marked **FULL** on the **left** bench in
   **Config L** and on the **right** bench in **Config R**. The other bench's spot holds the **empty tote**.
5. The two **totes** are the same size, light when empty, with a stiff rim along each **end wall** that one gripper can close on, and a **tote label**
   with a barcode on the middle of the long side facing the base. Each tote lies with its long sides running left to right.
6. The **full tote** is seated in the nest at the start and holds a few light items that fill it about half way, loose. Loaded, it is light enough for
   the two grippers to lift together.
7. The **panel** is fixed on the front edge of the dock bay, below the level of the AMR top, facing the base. It has:
   * an amber **DOCKED** lamp, lit while the AMR stands on its dock;
   * a **FULL TOTE** lamp and an **EMPTY TOTE** lamp, which light green when that tote's label is scanned in the right place;
   * a **DISPATCH** button, which lights green only when both tote lamps are green, and a **DISPATCHED** lamp;
   * a **scanner holster** holding a handheld **scanner**, window out.
8. The scanner reads a barcode by itself when held about a hand in front of it. It lights the FULL TOTE lamp for the full tote's label, and the
   EMPTY TOTE lamp for the empty tote's label (**unvalidated**: the mock must know which label is which).
9. At the start, DOCKED is lit, both tote lamps and DISPATCH are off, and the scanner is in its holster.
10. Nothing else stands on the bench, the AMR, or the panel within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the FULL spot and the empty tote's spot. You judge every other place by eye against the station
itself.

* **Transfer station:** the fixed bench the base is parked at. Never moved, never leaned on, never pushed.
* **Dock bay and AMR:** in the middle, the AMR top with its tote nest level with the bench. Both grippers together, only while DOCKED is lit.
* **FULL spot:** on the left bench (Config L) or the right bench (Config R). Where the full tote goes.
* **Empty tote spot:** on the other bench. Where the empty tote starts.
* **Panel:** on the front edge of the dock bay, below the AMR top. **Panel gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* During a tote carry, the **left gripper** holds the tote's left end and the **right gripper** its right end, and they move together.
* The **panel gripper** also works the scanner and the DISPATCH button, alone.
* Neither arm reaches over, under, around, or past the other.
* Only one thing is moved at a time: one tote by both grippers, or the scanner by the panel gripper while the other gripper is empty and drawn **clear
  of the AMR**.

### Arm assignments

* **Both grippers.** Lift the full tote off the AMR and set it on the FULL spot, then lift the empty tote and seat it on the AMR.
* **Panel gripper** (**left gripper** in Config L, **right gripper** in Config R). Scans the full tote, then the empty tote, and presses DISPATCH.
* **Other gripper.** Stays open and clear of the AMR while the panel gripper scans and dispatches.
* Nothing is handed over.

## Vocabulary

* **AMR:** autonomous mobile robot, a small robot that drives totes around the building. Here it is a mock.
* **Docked:** the AMR stands against the dock stop, still, with the DOCKED lamp lit.
* **Tote nest:** the four corner guides on the AMR top that hold a tote square.
* **End grip:** each gripper closes on the rim of one end wall, at its middle: the **left gripper** on the left end and the **right gripper** on the right
  end.
* **Two-gripper lift:** with both end grips closed, both grippers rise together, at the same speed, keeping the tote level.
* **Clear of the nest:** the tote's bottom is above the tops of the corner guides.
* **Seated tote:** the tote sits flat in the nest, inside all four corner guides, long sides left to right, label facing the base, and does not rock.
* **Set tote:** the tote stands flat inside its bench spot, square, label facing the base.
* **Scan:** the panel gripper takes the scanner out of its holster by its handle, holds its window about a hand in front of a tote label, still, until the
  tote's lamp lights green, and stands the scanner back in its holster.
* **Press:** the closed gripper comes straight at the button, pushes it once until it clicks, and draws straight back.
* **Clear of the AMR:** the arm is drawn up and back so that no part of it is over the AMR, the nest, or the dock bay.

## Steps

Run Steps 1 to 5 in order, and end the episode with Step 6. The config decides where the full tote goes, where the empty tote comes from, and which
gripper is the panel gripper. Nothing else changes between configs.

### Step 1: Check the AMR is docked

**Goal:** the AMR is known to be docked and still before anything touches it.

* Look at the panel: the **DOCKED** lamp is lit.
* Look at the AMR: it stands against the dock stop, still, with the full tote seated in its nest.
* **IF DOCKED is not lit or the AMR is moving:** keep both grippers clear of the AMR and wait until it is docked and still.

**Check:** DOCKED is lit, the AMR is still, and both grippers are clear of it.

### Step 2: Lift the full tote off the AMR

**Goal:** the full tote is **set** on the FULL spot and the nest is empty.

* With the **left gripper**, come down to the full tote's **left end** and close on the middle of its rim. With the **right gripper**, come down to its **right
  end** and close on the middle of its rim.
* With **both grippers** together, lift the tote straight up, level, until it is **clear of the nest**.
* **IF Config L:** with **both grippers** together, carry the tote level to the left, to above the FULL spot on the left bench. **IF Config R:** with **both
  grippers** together, carry it level to the right, to above the FULL spot on the right bench.
* With **both grippers** together, bring it straight down onto the FULL spot, flat, square, label facing the base.
* With **both grippers**, open together and lift straight up.

**Check:** the full tote is **set** on the FULL spot, its contents have not shifted out of it, and the nest is empty. If the tote sits across the outline, close
both end grips again and set it straight.

### Step 3: Seat the empty tote on the AMR

**Goal:** the empty tote is **seated** in the nest.

* Look at the panel again: DOCKED is still lit and the AMR is still.
* With the **left gripper**, close on the middle of the empty tote's **left end** rim. With the **right gripper**, close on the middle of its **right end** rim.
* With **both grippers** together, lift it straight up just clear of the bench.
* **IF Config L:** with **both grippers** together, carry it level from the right bench to above the nest. **IF Config R:** with **both grippers** together,
  carry it level from the left bench to above the nest.
* With **both grippers** together, turn it square to the nest, label facing the base, and lower it straight down inside the four corner guides until it sits flat.
* With **both grippers**, open together and lift straight up and **clear of the AMR**.

**Check:** the empty tote is **seated**: inside all four guides, flat, not rocking. If a corner rests on a guide, close both end grips again, lift just clear, and
lower it straight down once more.

### Step 4: Scan both totes

**Goal:** the FULL TOTE and EMPTY TOTE lamps are both green.

#### 4.1 Scan the full tote

* **IF Config L:** the **left gripper** is the panel gripper. **IF Config R:** the **right gripper** is the panel gripper.
* With the **panel gripper**, close on the handle of the **scanner** and lift it straight up out of its holster.
* With the **panel gripper**, hold its window about a hand in front of the **full tote's label** on the FULL spot, still, until the **FULL TOTE** lamp lights green.
* With the other gripper, stay open and **clear of the AMR**.

**Check:** the FULL TOTE lamp is green. If it does not light, hold the scanner still in front of the label once more with the **panel gripper**.

#### 4.2 Scan the empty tote

* With the **panel gripper**, bring the scanner level to about a hand in front of the **empty tote's label** on the AMR, keeping it off the tote and the AMR, and
  hold still until the **EMPTY TOTE** lamp lights green.
* With the **panel gripper**, stand the scanner back in its holster, window out, open, and draw back.

**Check:** both tote lamps are green, DISPATCH is lit, and the scanner stands in its holster, window out.

### Step 5: Dispatch the AMR

**Goal:** DISPATCH is pressed with both grippers clear, and the AMR has left the bay.

* Check both grippers are **clear of the AMR**.
* With the **panel gripper**, closed, **press** the green **DISPATCH** button once, then draw straight back.
* With **both grippers**, hold still and clear while the AMR leaves the bay.

**Check:** DISPATCHED is lit, DOCKED is out, and the bay is empty. If DISPATCH does not light DISPATCHED, check both tote lamps are green and press it once more with
the **panel gripper**.

### Step 6: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the exchange done.

* Look once across the station: the full tote stands on the FULL spot, the empty tote's spot is bare, the AMR has left with the empty tote, and the scanner is in its
  holster.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the exchange is done, the AMR has left, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Bring the AMR back into the bay against its dock stop, brakes on, with the empty tote still on it, and check DOCKED lights.
2. Take the empty tote off the AMR and stand the full tote back in the nest, seated, label facing the base, contents loose inside.
3. Stand the empty tote on the empty tote's spot for the next config.
4. Swap the FULL outline and the empty tote's spot to the sides for the next episode's config.
5. Reset the panel: tote lamps, DISPATCH, and DISPATCHED off, scanner in its holster.
6. Pick up anything that landed on the bench, the AMR, or the floor.
7. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the reviewer sees. The coaching note is
for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the station shifts in frame, the bench edge changes angle or size in frame, or the base rolls, creeps, or turns at any point after recording
  starts.
* **SOP rule broken:** Steps 1 to 6, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Worked an AMR that was not docked**

* **Visible cue:** a gripper touches the AMR, its nest, or a tote on it while DOCKED is out or the AMR is moving.
* **SOP rule broken:** Steps 1 and 3, the AMR is touched only while DOCKED is lit and it stands still.
* **Coaching note:** lamp first, AMR second. A robot that is not docked can move.

**Violation: Touched the leaving AMR**

* **Visible cue:** a gripper is over the AMR or the bay, or touches the AMR or its tote, from the press of DISPATCH until the AMR has left.
* **SOP rule broken:** Step 5, both grippers are clear of the AMR before DISPATCH and stay clear while it leaves.
* **Coaching note:** hands clear, then dispatch, then stay clear.

**Violation: Leaned on or pushed the AMR, bench, or panel**

* **Visible cue:** a gripper, wrist, or forearm rests on the AMR, its nest, the bench, or the panel; or the AMR is shoved against or off its dock stop.
* **SOP rule broken:** Steps 1 to 5, the AMR, the bench, and the panel carry no weight from the arms.
* **Coaching note:** the arm holds itself up. The AMR stays exactly where it docked.

**Violation: Tote lifted wrong**

* **Visible cue:** a tote is lifted by one gripper, by a corner, by a long side, or by its label; or both grippers close on the same end.
* **SOP rule broken:** Steps 2 and 3, the left gripper takes the left end rim and the right gripper the right end rim, at the middle, before any lift.
* **Coaching note:** one end each, middle of the rim, then lift together.

**Violation: Grippers out of step**

* **Visible cue:** one end rises, falls, or moves sideways before the other, so the tote tilts or swings in the carry.
* **SOP rule broken:** Steps 2 and 3, both grippers lift, carry, and lower together, keeping the tote level.
* **Coaching note:** two hands, one tote, one speed. A tilted tote spills.

**Violation: Tote dragged**

* **Visible cue:** a tote is slid across the AMR top, a guide, the bench, or the gap of the bay instead of being lifted clear first.
* **SOP rule broken:** Steps 2 and 3, lift the tote clear of the nest or the bench before carrying it.
* **Coaching note:** up first, then across.

**Violation: Contents disturbed**

* **Visible cue:** items in the full tote slide over the rim, fall out, or are thrown against a wall of the tote by a jerk in the lift or the set-down.
* **SOP rule broken:** Step 2, lift, carry, and set the full tote down level and smooth.
* **Coaching note:** smooth and level. What is in the tote is someone's order.

**Violation: Full tote set wrong**

* **Visible cue:** the full tote is set down anywhere but the FULL spot, across its outline, crooked, hanging over the bench edge, or with its label facing away.
* **SOP rule broken:** Step 2, set the full tote flat and square inside the FULL spot, label facing the base.
* **Coaching note:** inside the lines, square, label out.

**Violation: Empty tote not seated**

* **Visible cue:** the empty tote rests on a corner guide, rocks, sits crooked in the nest, or faces its label away; or it is dropped into the nest.
* **SOP rule broken:** Step 3, lower the empty tote straight down inside all four guides until it sits flat.
* **Coaching note:** square above the nest, then straight down. A tote on a guide falls off in the first turn.

**Violation: Scan skipped or done out of turn**

* **Visible cue:** a tote is not scanned; a tote is scanned before it is in its place; the empty tote is scanned before the full tote; or the arms move on before the
  lamp lights green.
* **SOP rule broken:** Step 4, with both totes in place, scan the full tote, then the empty tote, each until its lamp lights green.
* **Coaching note:** tote in place, scan, green. Both lamps before the button.

**Violation: Scanner handled wrong**

* **Visible cue:** the scanner is held by its window, dropped, laid on the bench, the AMR, or a tote, pressed against a label, left out of its holster, or held while
  the gripper does anything else.
* **SOP rule broken:** Step 4, the panel gripper takes the scanner by its handle, scans a hand from the label, and stands it back in its holster window out.
* **Coaching note:** holster to label and back to the holster. It lives in the holster.

**Violation: Dispatch done wrong**

* **Visible cue:** DISPATCH is pressed before both tote lamps are green, while a gripper is over the AMR, more than once with no reason, held down, or with an open
  gripper.
* **SOP rule broken:** Step 5, with both lamps green and both grippers clear, press DISPATCH once with the closed panel gripper.
* **Coaching note:** two green lamps, hands clear, one press.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the station is not set up in: the full tote goes to the empty tote's side, the empty tote is looked for on the FULL side, the
  gripper away from the FULL spot scans or presses DISPATCH, or a spot is moved before or during the episode.
* **SOP rule broken:** Steps 2 to 5, look at the station, find the FULL spot, and follow the IF line that matches the config the episode is set up in.
* **Coaching note:** find FULL before the arms move. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** the empty tote is lifted before the full tote is off the AMR; a scan is made before both totes are in place; or DISPATCH is pressed before both scans.
* **SOP rule broken:** Steps 1 to 5, check docked, lift the full tote off, seat the empty tote, scan both, then dispatch.
* **Coaching note:** the order is the task. Off, on, scan, send.

**Violation: More than one thing moved at a time**

* **Visible cue:** both totes are moved at the same time, a tote is carried with one gripper while the other works, or the scanner is held during a tote move.
* **SOP rule broken:** Steps 2 to 5, both grippers carry one tote together, or the panel gripper holds the scanner while the other gripper is clear.
* **Coaching note:** one tote with two hands, or the scanner with one. Never both.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a tote across the FULL outline, a corner on a guide,
  a lamp not green, or DISPATCHED not lit.
* **SOP rule broken:** Steps 1 to 5, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a tote or the scanner is dropped on the bench, the AMR, or the floor; a tote is knocked off the AMR or the bench; or an item falls out of a tote.
* **SOP rule broken:** Steps 2 to 5, nothing is dropped or knocked out of its place, and every gripper lifts clear the way it came in.
* **Coaching note:** check the path and the landing place before the arms move.

**Violation: Wrong arm used**

* **Visible cue:** the right gripper takes a tote's left end or the left gripper its right end; the gripper away from the FULL spot scans or presses DISPATCH; or either
  arm passes in front of the other.
* **SOP rule broken:** Steps 2 to 5, each gripper takes its own end of a tote, only the panel gripper scans and dispatches, and the arms never cross.
* **Coaching note:** left end, left arm. Right end, right arm. The FULL side runs the panel.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with the AMR still docked, a tote lamp not green, the full tote off the FULL spot, the scanner out of its holster, an arm short of
  home, or a gripper not fully open.
* **SOP rule broken:** Step 6, look once across the station, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a tote label, a panel lamp, or whether the AMR is moving**, so the scans, the dispatch, or the docking cannot be judged.
* **AMR fault:** the AMR does not stand still while DOCKED is lit, does not leave after DISPATCHED lights, or leaves before DISPATCH is pressed.
* **Panel or scanner fault:** a lamp does not light on a correctly held label, lights for the wrong tote, or DISPATCH does not respond with both lamps green.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a tote end, a bench spot, the holster, or the button cannot be
  reached without extending or folding the arm, or the full tote is too heavy for the two-gripper lift.

## Annotation subtasks (from SOP)

1. Check the DOCKED lamp and the AMR
2. Close both end grips on a tote
3. Lift the full tote clear of the nest with both grippers
4. Set the full tote on the FULL spot
5. Carry the empty tote to the AMR with both grippers
6. Seat the empty tote in the nest
7. Take the scanner from its holster
8. Scan one tote label
9. Stand the scanner back in its holster
10. Press DISPATCH
11. Hold clear while the AMR leaves
12. Return both arms home and end the episode
