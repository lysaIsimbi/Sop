# Extract a Part from an Injection Mold Mock SOP (1x Episode: one part, one mold, in situ)

One episode takes one part out of the mold mock at the bench where the mock is bolted. Open the mold.
Take the part out. Cut the gate off. Look at the gate. Put the part in the tray. Close the mold and set
it up for the next part. The episode ends when the part lies in the tray or in the reject bin, the runner
is in the scrap cup, the cutters are back where they started, and the mold is shut. Never split one part
into two episodes.

The base is **passive**: it has no drive of its own, so it is pushed by hand up to the bench in front of
the mold mock and locked there, and nothing is carried away to another table. Everything the episode
touches is already there when recording starts: the mold mock bolted to the bench, the tool mat in front
of it, the cutters, the tray, the scrap cup, and the reject bin.

The mold is worked **as found**. It starts shut, with a part inside. The part is a molded plastic part
with its runner still on it. The moving half slides on two guide bars. The episode ends with the mold shut
and empty, ready for the next part to be loaded in the reset.

**This is an in-situ task, and four things follow from that.** First, **the mold mock stays bolted
down**: nothing pushes, pulls, lifts, or leans on the fixed half or the bench. Second, **the moving half
only slides on its bars**: it is pulled open by its handle until it stops, and pushed shut by its handle
until it stops. It is never twisted, lifted, or jerked. Third, **the part face is never touched**: the
face is the smooth, shiny side of the part. The part is lifted out of the mold by its runner, and after
the cut it is held by its edges. Fourth, **the cutters only cut the gate**: they never touch the mold, the
tray, or the face of the part.

Scrap goes in the scrap cup and nowhere else. The runner cut off goes in the scrap cup. A bit of plastic
left on the bench, in the mold, or on the floor is a loose bit. It is not chased. It is reported.

**The bench is set up in one of three ways.** The mold, the tool mat, and the handle never move. Only the
cutters and the output group, the tray with the scrap cup beside it and the reject bin behind it, do.

* **Config L:** the cutters lie on the bench to the **left** of the tool mat. The tray, the scrap cup,
  and the reject bin stand to the **right**.
* **Config M:** the cutters lie on the **front edge of the tool mat**, in the middle. The tray, the scrap
  cup, and the reject bin stand to the **right**.
* **Config R:** the cutters lie on the bench to the **right** of the tool mat. The tray, the scrap cup,
  and the reject bin stand to the **left**.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on
the setup it says so on an **IF** line. Look at the bench and follow the line that matches.

**Tool-side rule:** the gripper on the cutters' side is the **cutter gripper**: the left gripper in
Config L, the right gripper in Config M and R. It is the only gripper that touches the cutters. The other
gripper is the **hold gripper**: it lifts the part out of the mold, lays it on the mat, and holds it still
while the gate is cut. The gripper on the tray's side is the **output gripper**: the right gripper in
Config L and M, the left gripper in Config R. It puts the runner in the scrap cup, shows the gate to the
camera, and puts the part in the tray or the bin. No arm reaches across the mold or the mat for a tool,
a cup, or a tray.

The **right gripper always works the handle**, because the handle stands at the front of the mold in the
middle and is taken only while nothing else is held. Each gripper holds one thing at a time. Nothing is
passed from one gripper to the other. The part is never in the air while the cutters move.

The order never changes: **open the mold; take the part out; cut the gate off; look at the gate; put the
part in the tray; close the mold and reset it.**

## Setup

Complete the base positioning and all the checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never
steered, nudged, or repositioned once recording starts. It is parked once, before recording, and does
not move again until the episode is over.

1. Push the base by hand up to the bench and stop it **square to the front edge of the bench**, so the
   front edge runs straight across the frame and neither end sits nearer than the other.
2. Stop it **centered on the mold mock**, so the cutters' side and the tray's side are the same distance
   from the middle of the base.
3. Stop it **close enough** that the hold gripper reaches the runner in the open cavity without the arm
   extending, and **far enough** that no arm, wrist, or part of the base touches the bench front, the
   mold, or the guide bars while both arms work.
4. Check the **pull**: with the base parked, the **right gripper** closes on the mold handle and slides
   the moving half all the way open and all the way shut without extending.
5. Check the **cavity**: the hold gripper reaches the runner in the open cavity, lifts the part straight
   up, and clears the mold without extending.
6. Check the **bench**: the cutter gripper reaches the cutters where this config puts them, both grippers
   reach the middle of the tool mat, and the output gripper reaches the tray, the scrap cup, and the
   reject bin, all without extending and without knocking anything over.
7. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
8. If any of lines 1 to 6 fails, push the base to a new park by hand and start again at line 1. Do not
   work a bench the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the bench
or the mold hard enough to shift it, nothing and nobody touches it, and it is never repositioned
mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the mold mock and its frame includes the whole mold, both
   halves, the guide bars, the handle, the tool mat with the cut point, the cutters, the tray, the scrap
   cup, and the reject bin.
3. The camera reads the parting line from the front, so whether the mold is open or shut is readable.
4. The camera reads into the cavity when the mold is open, so the part in it and an empty cavity are
   readable.
5. The camera reads the tool mat from above, so the part lying on it and the cutters on the gate are
   readable.
6. The camera reads the gate on the part when it is held up at the inspection point, so the cut is
   readable.
7. The camera reads the tray pockets, so where the part lands and which way its face points are
   readable.
8. Both arms are at home with grippers open.
9. The **right arm** reaches the mold handle, the runner in the open cavity, and the middle of the tool
   mat without extending to a joint limit.
10. The **left arm** reaches the runner in the open cavity and the middle of the tool mat without
    extending to a joint limit.
11. The cutter gripper reaches the cutters, and the output gripper reaches the tray, the scrap cup, and
    the reject bin, without extending.
12. The two arms do not collide when one holds the part still on the mat and the other holds the cutters.
13. If a place cannot be reached, re-park the base by the Base positioning steps until lines 9 to 12
    hold.

### Materials checklist

1. The **mold mock** is a two half mold made for practice. It does not heat up. Nothing is molded in it.
   A part is put in it by hand before each episode.
2. The **fixed half** is bolted to the bench. Nothing moves it, leans on it, or stands anything on it.
3. The **moving half** slides on two **guide bars**. It has a **handle** on its front, in the middle. It
   stops hard at the open end and at the shut end.
4. The moving half slides easily. Test it by hand during setup. If it sticks, stop and fix the bars.
   Nothing forces it during the episode.
5. The **cavity** is the hollow in the fixed half. The part sits in it. When the mold opens, the part
   stays in the cavity of the fixed half.
6. The **part** is one molded plastic part. It has a smooth **face** that must not be scratched, and a
   **runner** stuck to one edge.
7. The runner is a plastic stick about as long as a finger. It is what the part is lifted by.
8. The **gate** is the thin neck where the runner joins the part. It is the spot that is cut.
9. The part sits loose in the cavity. It lifts out with no pull. Test it by hand during setup. If it
   sticks, change the part.
10. The **tool mat** is a rubber mat on the bench directly in front of the mold, centered on the base.
    The part is laid on it for the cut. Nothing else lies on it, except the cutters in Config M.
11. The **cutters** are flush cutters with two handles and a small flat jaw. They lie with the handles
    toward the front and the jaw pointing to the back, at the spot this episode's config puts them: on
    the bench **left of the mat in Config L**, on the **front edge of the mat in Config M**, on the bench
    **right of the mat in Config R**.
12. The cutters are sharp and close all the way. Test them on a scrap runner during setup.
13. The **tray** is a flat tray with soft pockets. Each pocket holds one part face up. It stands on the
    bench beside the mat with at least one empty pocket, on the **right in Config L and M** and on the
    **left in Config R**.
14. The **scrap cup** is an open cup standing next to the tray, on the tray's side. The cut runner goes
    in it.
15. The **reject bin** is an open bin standing behind the tray, on the tray's side. A part with a bad gate
    goes in it.
16. The bench top is clean and clear at the start. No loose bits of plastic lie on it, in the cavity, or
    on the tool mat.

### Workspace layout

Nothing is marked or taped out. Every place below is judged by eye from the bench and the mold
themselves.

* **Mold mock:** the middle of the bench. Fixed half at the back, moving half at the front, handle
  facing the front. Never moved.
  * **Cavity:** the hollow in the fixed half. The part starts here and leaves here once.
  * **Open end:** where the moving half stops when the mold is pulled open.
  * **Shut end:** where the moving half stops when the mold is pushed shut.
* **Tool mat:** directly in front of the mold, centered. The part is laid here for the cut.
  * **Cut point:** the middle of the tool mat. The part lies here face up while the gate is cut, so the
    runner falls on the mat and not in the mold.
  * **Inspection point:** the air above the tool mat, in front of the camera, where the gate is held up
    to be looked at.
* **Cutters:** left of the mat in Config L, on the front edge of the mat in Config M, right of the mat in
  Config R. They start and end there.
* **Output group:** on the right in Config L and M, on the left in Config R.
  * **Tray:** beside the mat. Good parts go here, one to a pocket, face up.
  * **Scrap cup:** next to the tray. The cut runner goes here.
  * **Reject bin:** behind the tray. A part with a bad gate goes here.

### Arm assignments

* **The right gripper owns the handle.** It opens the mold in Step 1 and shuts it in Step 6, and it holds
  nothing else while it does.
* **The hold gripper** lifts the part out of the cavity by its runner, lays it on the cut point, and
  presses on its edge while the gate is cut: the right gripper in Config L, the left gripper in Config M
  and R.
* **The cutter gripper** picks the cutters up, cuts the gate, and puts the cutters back: the left gripper
  in Config L, the right gripper in Config M and R.
* **The output gripper** drops the runner in the scrap cup, picks the part up by its edges, shows the gate
  to the camera, and puts the part in the tray or the reject bin: the right gripper in Config L and M,
  the left gripper in Config R.
* Each gripper holds one thing at a time. Nothing is passed from one gripper to the other. The cutters
  are never in a gripper while the part is in the air.

## Vocabulary

* **In situ:** the mold is worked where it is bolted. Nothing is carried away to another table, and
  nothing about the bench is rearranged for the task.
* **Passive base:** the base has no drive. It is pushed by hand to its park before recording, locked
  there, and it does not move at all during the episode.
* **Config:** which of the three bench layouts this episode uses. It is set before recording and never
  changes mid-episode.
* **Cutter gripper:** the gripper on the cutters' side. Left in Config L, right in Config M and R.
* **Hold gripper:** the gripper that is not the cutter gripper. Right in Config L, left in Config M and R.
* **Output gripper:** the gripper on the tray's side. Right in Config L and M, left in Config R.
* **Parting line:** the gap between the two mold halves. It shows when the mold opens.
* **Open all the way:** the moving half stands at its open end stop. It does not move when pulled more.
* **Shut all the way:** the moving half stands at its shut end stop. The parting line is closed. No gap
  shows.
* **Runner grip:** the gripper closes on the runner in its middle, not on the gate and not on the part.
* **Edge grip:** the gripper closes on the part by two edges, with nothing touching the face.
* **Straight lift:** the part goes straight up out of the cavity, held by its runner, with no tilt and no
  drag along the cavity wall.
* **Low carry:** the part, the runner, or the cutters are carried close over the bench and level. Nothing
  ever goes over the mold.
* **Face up:** the smooth face of the part points at the ceiling.
* **Hold:** the hold gripper closed and pressed on the edge of the part, so the part does not slide or
  spin on the mat. A hold never lifts or moves the part.
* **Flush cut:** the cutters close right at the gate, with the flat side of the jaw against the part
  edge, so no stub sticks out.
* **Gate stub:** the small bit of the gate left on the part after the cut.
* **Good gate:** the stub is flat with the part edge or smaller than a grain of rice, and the part edge
  has no tear and no hole.
* **Bad gate:** the stub sticks out longer than a grain of rice, or the cut tore into the part, or there
  is a hole at the gate.
* **Seated in the pocket:** the part lies flat in one tray pocket, inside the pocket walls, face up, and
  does not rock.
* **Loose bit:** a piece of plastic that lands anywhere but in the scrap cup. It is not chased. It is
  reported.
* **Reset:** the mold is shut all the way, the cutters lie where they started, the mat is clear, and
  both grippers are open and clear.
* **Back and clear:** the arm is drawn back so that no part of it is over the mold, the mat, or the tray.

### Handling standard

* Each gripper holds one thing at a time. Nothing is passed from one gripper to the other.
* The handle is held only by the right gripper, only in the middle, and only while nothing else is held.
* The part is held only by its runner out of the mold and only by its edges after the cut. The face is
  never touched.
* The cutters are held only by their two handles, only by the cutter gripper, and only while the part
  lies held on the mat.
* Every carry is a low carry. Nothing crosses the open mold.
* Nothing rests on the mold or the bench. No gripper, wrist, or forearm leans on the fixed half, the
  guide bars, or the bench, and no push is ever hard enough to move the mold.

## Steps

Steps 2, 3, and 4 depend on the config: the hold gripper takes the part out and holds it, the cutter
gripper works the cutters, and the output gripper takes the runner and the part away. Every other step
is the same in all three.

### Step 1: Open the mold

**Goal:** the moving half stands at its open end, and the part sits in the cavity of the fixed half.

#### 1.1 Take the handle

* The **right gripper** closes on the mold handle in the middle.
* Do not touch the guide bars, the fixed half, or the parting line.

**Check:** the **right gripper** holds the handle square and nothing else is touched. If the grip is off
the middle, open it and take the handle again.

#### 1.2 Slide it open

* The **right gripper** pulls the handle straight toward the front, slow and level, along the guide bars.
* Do not twist it. Do not lift it. Do not jerk it.
* Pull until the moving half stops at the open end.

**Check:** the mold is open all the way. The parting line is a wide gap. The part sits in the cavity of
the fixed half. If the part came out stuck to the moving half, stop and report it.

#### 1.3 Let go of the handle

* The **right gripper** opens and draws back from the handle.

**Expected state:** the mold stands open. The part sits in the cavity. Both grippers are back and clear.

### Step 2: Take the part out

**Goal:** the part lies face up on the cut point, with its runner pointing away from the cutters.

#### 2.1 Take the runner

* **IF Config L:** the **right gripper** is the hold gripper.
* **IF Config M or R:** the **left gripper** is the hold gripper.

Then, in all three:

* The **hold gripper** comes straight down over the cavity and closes on the runner in the middle. Do
  not close on the gate. Do not close on the part.

**Check:** it is a runner grip. The hold gripper holds only the runner. If it holds the part or the gate,
open it and take the runner again.

#### 2.2 Lift it straight up

* The **hold gripper** lifts the part straight up out of the cavity in a straight lift.
* Do not tilt it. Do not drag it along the cavity wall. Do not scrape it on the moving half.
* Lift until the part is clear of the mold.

**Check:** the part hangs from its runner, clear of the mold. The cavity is empty. If the part catches,
the hold gripper lowers it back into the cavity and lifts again, slower.

#### 2.3 Lay it on the tool mat

* The **hold gripper** carries the part to the tool mat in a low carry. Do not carry it over the tray.
* Lower it straight down onto the cut point, face up, with the runner pointing away from the cutters.
* Open the gripper and draw it back.

**Check:** the part lies flat on the mat, face up, and does not rock. The runner lies flat on the mat. If
the part is face down, the hold gripper takes the runner again, lifts it, turns it, and lays it down
again.

**Expected state:** the part lies face up on the cut point. The cavity is empty. The mold is still open.
The cutters have not moved.

### Step 3: Cut the gate off

**Goal:** the runner is cut off at the gate with a flush cut, the runner is in the scrap cup, and the
cutters are back where they started.

#### 3.1 Hold the part still

* The **hold gripper** closes and presses down on the edge of the part, on the side away from the runner.
* Press just hard enough that the part cannot slide or spin. Do not press on the face.

**Check:** it is a hold. The part does not move when pushed a little. The hold gripper is on the edge, not
the face.

#### 3.2 Pick up the cutters

* **IF Config L:** the **left gripper** is the cutter gripper.
* **IF Config M or R:** the **right gripper** is the cutter gripper.

Then, in all three:

* The **cutter gripper** closes on the cutters by their two handles and lifts them just off the surface
  they lie on.

**Check:** the cutters hang jaw down, closed, with both handles in the cutter gripper. If the grip is on
the jaw, put them down and take them again.

#### 3.3 Set the jaw on the gate

* The **cutter gripper** opens the cutters and brings the jaw down to the gate.
* Lay the flat side of the jaw against the edge of the part, so the gate is between the blades.
* Do not touch the part face with the jaw. Do not put the runner in the jaw.

**Check:** the jaw sits on the gate, flat against the part edge, with nothing else between the blades. If
the jaw is on the runner instead of the gate, open it and set it again.

#### 3.4 Make the cut

* The **cutter gripper** closes the cutters all the way in one squeeze.
* The **hold gripper** keeps the hold on the part while the cut is made.

**Check:** it is a flush cut. The runner lies loose on the mat. The part did not move. If the runner is
still joined by a thread of plastic, set the jaw on the thread and cut again.

#### 3.5 Put the cutters back

* The **cutter gripper** lifts the cutters just off the part and carries them in a low carry to where
  they started.
* Lay them down with the handles toward the front and the jaw pointing to the back.
* Open the gripper and draw it back.

**Check:** the cutters lie closed where they started. If they lie on the part or off their spot, the
cutter gripper takes them again and lays them down again.

#### 3.6 Put the runner in the scrap cup

* The **hold gripper** opens its hold and comes back and clear.
* **IF Config L or M:** the **right gripper** is the output gripper.
* **IF Config R:** the **left gripper** is the output gripper.

Then, in all three:

* The **output gripper** closes on the loose runner, lifts it just off the mat, and carries it to the
  scrap cup in a low carry.
* Open the gripper over the cup so the runner drops in.

**Check:** the runner is in the scrap cup. Nothing lies on the mat except the part, and the cutters in
Config M. If the runner fell on the bench, leave it and report it.

**Expected state:** the part lies face up on the mat with a gate stub. The runner is in the scrap cup.
The cutters are back where they started. Both grippers are back and clear.

### Step 4: Look at the gate

**Goal:** the gate stub has been shown to the camera and is known to be good or bad.

#### 4.1 Pick the part up by its edges

* The **output gripper** closes on the part by two edges in an edge grip. Do not touch the face.
* Lift it just off the mat.

**Check:** the part hangs level in the output gripper. Nothing touches the face. If the grip is on the
face, put the part down and take it again.

#### 4.2 Hold the gate up to the camera

* The **output gripper** lifts the part to the inspection point above the mat.
* Turn it so the gate stub faces the camera. Hold it still for 2 seconds.

**Check:** the gate stub is in the frame and in focus. The stub, the part edge next to it, and any tear
or hole are readable.

#### 4.3 Decide good or bad

* If the stub is flat or smaller than a grain of rice, and the edge has no tear and no hole, it is a good
  gate. Go to Step 5.
* If the stub sticks out longer than a grain of rice, or the edge is torn, or there is a hole, it is a
  bad gate. The **output gripper** carries the part in a low carry to the reject bin, opens over the bin,
  and lets it drop in. Then go to Step 6.
* Do not cut a bad gate again. Do not trim the stub.

**Expected state:** the part is either in the output gripper, ready for the tray, or in the reject bin.
The mat holds nothing but the cutters in Config M.

### Step 5: Put the part in the tray

**Goal:** the part lies face up in one empty tray pocket.

#### 5.1 Carry it to the tray

* The **output gripper** carries the part in a low carry to the tray. Do not carry it over the mold.
* Bring it over the nearest empty pocket.

#### 5.2 Lower it into the pocket

* The **output gripper** lowers the part straight down into the pocket, face up.
* Open the gripper and draw it back.

**Check:** the part is seated in the pocket. It lies flat, inside the pocket walls, face up, and does not
rock. If it sits on the pocket wall, or face down, the output gripper takes it by its edges, lifts it,
and puts it down again.

**Expected state:** the part lies in a tray pocket. The mat is clear but for the cutters in Config M. The
mold is still open and empty.

### Step 6: Close the mold and reset it

**Goal:** the mold is shut all the way, and the workspace is ready for the next part.

#### 6.1 Take the handle

* The **right gripper** closes on the mold handle in the middle.
* Do not touch the guide bars, the fixed half, or the parting line.

#### 6.2 Slide it shut

* Look into the cavity first. It must be empty.
* The **right gripper** pushes the handle straight toward the back, slow and level, along the guide bars.
* Do not twist it. Do not lift it. Do not slam it.
* Push until the moving half stops at the shut end.

**Check:** the mold is shut all the way. The parting line is closed and no gap shows. If a gap shows, the
right gripper pulls the moving half open a little and pushes it shut again. If it will not shut, stop
and report it.

#### 6.3 Let go and check the bench

* The **right gripper** opens and draws back from the handle.
* Look at the cutters. They lie closed where they started, handles to the front. Nothing else lies on the
  mat.
* Look at the bench. No loose bits lie on it.

**Check:** the workspace is reset. The mold is shut, the cutters are in place, and the mat is clear. If
the cutters are out of place, the cutter gripper takes them by their handles and lays them down again.

**Expected state:** the mold is shut and empty. The part is in the tray or in the reject bin. The runner
is in the scrap cup. The cutters are where they started. Both grippers are back and clear.

### Step 7: End the episode

**Goal:** the part is out and away, the mold is reset, and both arms are safely home.

* Confirm the mold is shut all the way, with no gap at the parting line, and the cavity is empty.
* Confirm the part lies face up in one tray pocket, or is in the reject bin.
* Confirm the runner is in the scrap cup and the cutters lie closed where they started, handles to the
  front.
* Confirm no loose bits lie on the bench, and the base has not moved: it is still square to the bench
  and still locked.
* Return both arms home, then stop recording.

## After the episode: reset the workspace

This reset is not recorded. The base stays parked and locked through the reset, and is only pushed away
by hand once the bench is set for the next episode.

1. Pull the moving half open by hand.
2. Put a new part in the cavity by hand, with its runner on the side away from the cutters for the next
   episode's config. Press it in so it sits flat.
3. Lift the part out by hand once and put it back, to check it comes out with no pull. Change the part if
   it sticks.
4. Push the moving half shut by hand until it stops.
5. Empty the scrap cup if it is more than half full.
6. Pick up any loose bits from the bench, the mat, the cavity, and the floor.
7. Check the cutters: they close all the way and cut a scrap runner clean. Change them if they crush
   instead of cut. Lay them closed, handles to the front, jaw to the back, at the spot the next episode's
   config puts them: left of the mat for Config L, on the front edge of the mat for Config M, right of
   the mat for Config R.
8. Stand the tray, the scrap cup, and the reject bin on the side the next episode's config puts them, the
   right for Config L and M, the left for Config R, with the scrap cup next to the tray and the bin
   behind it. Check the tray has at least one empty pocket. Change the tray if it is full.
9. Check the guide bars: the moving half slides open and shut by hand with no catch.
10. Check the fixed half is still bolted tight and does not rock.
11. Check the base is still square, centered, and locked, and push it firmly once by hand to confirm it
    does not roll. If it has moved, park it again by the Base positioning steps.
12. Run the Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The
visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation
label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete
it just because a rule was broken.

### Violations

**Note on the tool side:** the violations below were written for Config L (cutters on the left worked by
the left gripper, tray on the right, the right gripper holding the part and taking it away). The arm-role
cues in them will be rewritten later to cover all three configs; they are left as they are for now.
Until then, anything that does not match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the grippers do does not match the config on the bench. A gripper reaches across
  the mat for the cutters, the scrap cup, or the tray; the cutters are worked by the gripper on the
  other side; the part is held by the cutter gripper; the cutters or the output group are not where
  that config puts them; or the wrong IF line is followed in Step 2, 3, or 4.
* **SOP rule broken:** Steps 2.1, 3.2, and 3.6, the tool-side rule. The gripper on the cutters' side
  works the cutters, the other holds the part, the gripper on the tray's side takes the runner and the
  part away, and the IF line followed is the one for the config on the bench.
* **Coaching note:** look where the cutters and the tray are before the mold is opened, then follow that
  config's IF lines through Steps 2 to 5.

**Violation: Base moved during the episode**

* **Visible cue:** the bench shifts in the frame, the mold changes angle in the frame, or the base rolls,
  creeps, or turns at any time after recording starts.
* **SOP rule broken:** Step 7 and the Base positioning rule it confirms, the base is parked and locked
  before recording and does not move at all during the episode.
* **Coaching note:** park it, lock it, push-test it. If the park is wrong, fix it before recording, never
  during.

**Violation: Mold half forced or lifted**

* **Visible cue:** the moving half is twisted, lifted off the guide bars, jerked, or slammed, or the
  handle is pulled sideways.
* **SOP rule broken:** Steps 1.2 and 6.2, slide the moving half straight along its bars, slow and level,
  until it stops.
* **Coaching note:** the bars are the road. Straight along, until the stop, and no harder than that.

**Violation: Fixed half touched or leaned on**

* **Visible cue:** a gripper, wrist, or forearm rests on the fixed half, the guide bars, or the bench, or
  the fixed half rocks.
* **SOP rule broken:** Steps 1 to 6, nothing pushes, pulls, lifts, or leans on the fixed half or the
  bench.
* **Coaching note:** the arm holds itself up. If something moves when it is touched, it was touched too
  hard.

**Violation: Held by the wrong part**

* **Visible cue:** a gripper closes on the part face when lifting it out of the mold, on the gate instead
  of the runner, or on the cutters by the jaw, or the left gripper takes the handle.
* **SOP rule broken:** Steps 1.1, 2.1, 3.2, 4.1, and 6.1, the right gripper takes the handle in the
  middle, the part is lifted by the runner and held by the edges, and the cutters are taken by their
  handles.
* **Coaching note:** runner out of the mold, edges after the cut, handles on the cutters, right hand on
  the handle. The face is never touched.

**Violation: Part dragged out of the cavity**

* **Visible cue:** the part tilts, scrapes along the cavity wall, or catches on the moving half on the
  way out.
* **SOP rule broken:** Step 2.2, lift the part straight up out of the cavity.
* **Coaching note:** straight up first. Nothing moves sideways until the part is clear of the mold.

**Violation: Carried over the mold or the tray**

* **Visible cue:** the part, the runner, or the cutters cross over the open mold, the part crosses over
  the tray before Step 5, or a thing is carried high instead of low and level.
* **SOP rule broken:** Steps 2.3, 3.6, 4.3, and 5.1, every carry is low and level and never crosses the
  mold.
* **Coaching note:** low and around. Nothing crosses the open mold.

**Violation: Part laid down wrong**

* **Visible cue:** the part is laid on the mat face down, off the cut point, or with the runner under it,
  or it is dropped instead of lowered.
* **SOP rule broken:** Step 2.3, lay the part face up on the cut point, with the runner flat and pointing
  away from the cutters.
* **Coaching note:** face up, runner out. A part that cannot be seen cannot be cut.

**Violation: Cut without a hold**

* **Visible cue:** the cutters close on the gate while no gripper holds the part still, or the part spins
  or slides on the mat during the cut.
* **SOP rule broken:** Steps 3.1 and 3.4, hold the part still by its edge before and during the cut.
* **Coaching note:** hold first, cut second. A part that moves under the blades gets a torn gate.

**Violation: Cut in the wrong place**

* **Visible cue:** the cutters close on the runner away from the gate, leaving a long stub, or the jaw is
  set on the part edge so the blades bite into the part.
* **SOP rule broken:** Steps 3.3 and 3.4, set the flat side of the jaw against the part edge with the gate
  between the blades, and cut once.
* **Coaching note:** flat side to the part, gate between the blades. Not the runner, not the part.

**Violation: Cutters touched the wrong thing**

* **Visible cue:** the cutter jaw touches the part face, the mold, the tray, or the bench, or the cutters
  are moved while the part is in the air.
* **SOP rule broken:** Steps 3.2 to 3.5, the cutters only cut the gate, and only while the part lies held
  on the mat.
* **Coaching note:** the cutters have one job. The part is on the mat when they come out and on the mat
  when they go back.

**Violation: Cutters put back wrong**

* **Visible cue:** the cutters are laid on the part, off their spot, open, or with the jaw to the front,
  or they are dropped onto the mat or the bench.
* **SOP rule broken:** Step 3.5, lay the cutters closed where they started, handles to the front and jaw
  to the back.
* **Coaching note:** back where they were, the same way round. The next episode starts from there.

**Violation: Runner not put in the scrap cup**

* **Visible cue:** the cut runner is left on the mat, on the bench, in the mold, or dropped on the floor,
  or it is dropped into the tray or the reject bin.
* **SOP rule broken:** Step 3.6, the runner goes in the scrap cup and nowhere else.
* **Coaching note:** scrap has one home. Pick it up before the part comes off the mat.

**Violation: Gate not shown to the camera**

* **Visible cue:** the part goes from the mat to the tray with no stop at the inspection point, the gate
  stub is turned away from the camera, or the hold is shorter than 2 seconds.
* **SOP rule broken:** Step 4.2, hold the gate stub up to the camera, still, for 2 seconds.
* **Coaching note:** if the camera did not see the gate, nobody checked it.

**Violation: Wrong call on the gate**

* **Visible cue:** a part with a long stub, a tear, or a hole goes into the tray, or a part with a good
  gate goes into the reject bin.
* **SOP rule broken:** Step 4.3, good gate to the tray, bad gate to the reject bin.
* **Coaching note:** rice grain rule. Flat or smaller goes to the tray. Longer, torn, or holed goes to the
  bin.

**Violation: Bad gate trimmed**

* **Visible cue:** the cutters come back out after the inspection, and a second cut is made on the stub.
* **SOP rule broken:** Step 4.3, do not cut a bad gate again, do not trim the stub.
* **Coaching note:** one cut per part. A bad cut is a reject, not a retry.

**Violation: Part not seated in the pocket**

* **Visible cue:** the part ends up on a pocket wall, across two pockets, face down, rocking, or on top of
  another part.
* **SOP rule broken:** Step 5.2, lower the part straight down into one empty pocket, face up, so it lies
  flat.
* **Coaching note:** straight down into one pocket, face up. Watch it settle before letting go.

**Violation: Mold shut on something**

* **Visible cue:** the moving half is pushed shut while the part, the runner, or a loose bit is still in
  the cavity or on the parting line.
* **SOP rule broken:** Step 6.2, look into the cavity first, it must be empty before the mold shuts.
* **Coaching note:** look, then shut. A mold shut on plastic is a damaged mold.

**Violation: Mold not shut all the way**

* **Visible cue:** the episode ends with a gap at the parting line, or the moving half stopped short of
  the shut end.
* **SOP rule broken:** Step 6.2, push until the moving half stops at the shut end and no gap shows.
* **Coaching note:** to the stop, then look for the gap. Almost shut is open.

**Violation: Done in the wrong order**

* **Visible cue:** the cutters come out before the part is on the mat, the part goes to the tray before
  the gate is shown to the camera, or the mold is shut before the part is in the tray or the bin.
* **SOP rule broken:** Steps 1 to 6, open, take out, cut, look, tray, close, one thing at a time.
* **Coaching note:** the order is the task. Skipping a step is not faster, it is a lost episode.

**Violation: Something dropped or knocked over**

* **Visible cue:** the part, the runner, or the cutters slip out of a gripper and fall on the bench or the
  floor, or the scrap cup, the tray, or the reject bin is knocked over by an arm going past.
* **SOP rule broken:** Steps 1 to 6, one thing moves at a time, and each one is put down under control.
* **Coaching note:** close all the way before lifting, and put it down before letting go.

**Violation: Loose bit chased**

* **Visible cue:** a gripper goes after a bit of plastic on the bench, in the mold, or on the floor during
  the episode.
* **SOP rule broken:** Steps 1 to 6, a loose bit is not chased, it is reported.
* **Coaching note:** leave it, tag it, keep going. Clean up is not on camera.

**Violation: Failed check not retried**

* **Visible cue:** a check in a step clearly fails and the episode carries on with no retry: the part lies
  face down on the mat, the jaw is on the runner, or the part rocks in the pocket.
* **SOP rule broken:** Steps 1 to 6, do the retry written under each failed check before moving on.
* **Coaching note:** a check is only worth doing if the retry is done. Fix it where it happened.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with the mold open, the cavity not empty, the part not in the tray or
  the bin, the runner not in the cup, the cutters off their spot, or an arm away from home.
* **SOP rule broken:** Step 7 (confirm the mold, the cavity, the part, the scrap cup, the cutters, the
  bench, and the locked base; return both arms home; then stop recording).
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode,
and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot see the cavity, the gate stub, or the parting line**, so nobody can tell if the part
  came out clean, if the cut was good, or if the mold shut.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake that releases on its own, or a caster that seizes so the base cannot be parked
  square.
* **Defective object:** a part that sticks in the cavity under a correct straight lift, has no runner,
  has a runner that snaps off in a correct grip, or arrives already cracked or scratched; cutters that
  crush instead of cut, will not close all the way, come apart, or are too big to fit on the gate; a
  tray with pockets too small or too big for the part, or that slides on the bench under a correct set
  down. Replace it before the next episode.
* **Mold fault:** a moving half that sticks or binds on its bars, a stop that does not stop, a handle
  that comes loose, or a fixed half that rocks on its bolts.
* **Reach fault:** a place turns out to be too far for its arm with the base parked correctly, so the
  handle, the runner in the cavity, the cutters, the tray, the scrap cup, or the reject bin cannot be
  reached without extending the arm to a limit.

## Annotation subtasks (from SOP)

1. Take the mold handle and slide the mold open
2. Take the runner in the cavity
3. Lift the part straight out of the cavity
4. Lay the part face up on the cut point
5. Hold the part still on the mat
6. Pick up the cutters
7. Cut the gate
8. Put the cutters back
9. Put the runner in the scrap cup
10. Pick the part up by its edges
11. Hold the gate up to the camera
12. Put the part in the tray or the reject bin
13. Take the mold handle and slide the mold shut
14. Return both arms home and end the episode
