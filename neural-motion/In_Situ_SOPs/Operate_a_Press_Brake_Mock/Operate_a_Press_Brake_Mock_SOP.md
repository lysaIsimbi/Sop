# Operate a Press Brake Mock SOP (1x Episode: one sheet, three bends, in situ)

One episode bends one sheet on the press brake mock at the bench where the mock is bolted. Put the sheet
against the back stops. Cycle the press. Turn the part. Do this three times, for three bends. Then gauge
the three angles. Put the part in the finished tray. The episode ends when the part lies in the finished
tray or in the reject bin, the gauge is back on the gauge mat, and the press is up. Never split one sheet
into two episodes.

The base is **passive**: it has no drive of its own, so it is pushed by hand up to the bench in front of
the press brake mock and locked there, and nothing is carried away to another table. Everything the
episode touches is already there when recording starts: the press brake mock bolted to the bench, the
blank tray with flat sheets in it, the finished tray, the reject bin, and the angle gauge on the gauge
mat.

The press is worked **as found**. It starts up, with nothing in it. The sheet is a flat blank with three
bend lines drawn across it. Each line has a number on it: 1, 2, and 3. The episode ends with the press up
and empty, ready for the next sheet.

**This is an in-situ task, and four things follow from that.** First, **the press brake mock stays
bolted down**: nothing pushes, pulls, lifts, or leans on the press body or the bench. Second, **the lever
only goes down and up**: it is pulled down until it stops, and lifted back up until it stops. It is never
twisted, jerked, or let drop. Third, **nothing is in the gap while the press moves, except the sheet**:
no gripper, wrist, or tool ever goes under the punch. The sheet is held by its front edge, in front of
the die, and nowhere else. Fourth, **the sheet is bent on its line, and nowhere else**: the line sits over
the die groove before the press comes down. If the line is off, it is fixed before the cycle. The press
is never cycled to see what happens.

A bend cannot be undone. A part bent off its line, or bent on the wrong line, or bent the wrong way up,
is a reject. It is not bent again. It is not flattened. It goes in the reject bin and is reported.

**The bench is set up in one of three ways.** The press, the lever, the blank tray, the finished tray,
and the reject bin never move. Only the gauge mat, with the gauge on it, does.

* **Config L:** the gauge mat lies on the **left**, in front of the blank tray.
* **Config M:** the gauge mat lies in the **middle**, on the turn spot directly in front of the die. The
  half turns are made on the mat.
* **Config R:** the gauge mat lies on the **right**, in front of the finished tray.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on
the setup it says so on an **IF** line. Look at the bench and follow the line that matches.

**Fixed arm roles:** the **left gripper is the sheet gripper**. It takes the sheet from the blank tray on
its side, lays it on the die, holds it against the stops through every cycle, and makes the turns. The
**right gripper is the lever gripper**, because the lever is on the right side of the press, and it puts
the part in the finished tray or the reject bin on its side. **Mat-side rule:** the gripper on the gauge
mat's side works the gauge. When the part must go from one gripper's side to the other, it is **set
down on the turn spot** and taken up by the other gripper. Nothing is ever passed from one gripper to
the other in the air.

Each gripper holds one thing at a time. The sheet is never in the air while the lever moves.

The order never changes: **sheet against the stops; cycle; turn; sheet against the stops; cycle; turn;
sheet against the stops; cycle; then gauge all three angles; then tray or bin.**

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
2. Stop it **centered on the press brake mock**, so the blank tray on the left and the finished tray on
   the right are the same distance from the middle of the base.
3. Stop it **close enough** that the **left gripper**, holding the sheet by its front edge, pushes the
   sheet back until it touches both back stops without the arm extending, and **far enough** that no
   arm, wrist, or part of the base touches the bench front, the press body, or the lever while both arms
   work.
4. Check the **lever**: with the base parked, the **right gripper** closes on the lever knob and pulls
   the lever all the way down and lifts it all the way up without extending.
5. Check the **stops**: the **left gripper**, holding a sheet by its front edge, pushes the sheet back
   until it touches both back stops and holds it there without extending. The gripper stays in front of
   the die the whole time.
6. Check the **bench**: the **left gripper** reaches the top sheet in the blank tray and the turn spot,
   the **right gripper** reaches the turn spot, the finished tray, and the reject bin, and the gripper on
   the gauge mat's side reaches the gauge where this config puts it, all without extending and without
   knocking anything over.
7. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
8. If any of lines 1 to 6 fails, push the base to a new park by hand and start again at line 1. Do not
   work a bench the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the bench
or the press hard enough to shift it, nothing and nobody touches it, and it is never repositioned
mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the press brake mock and its frame includes the whole press,
   the punch, the die, both back stops, the lever, the blank tray, the turn spot, the gauge mat with the
   gauge, the finished tray, and the reject bin.
3. The camera reads the die from the front, so the sheet lying on the die and the bend line over the die
   groove are readable.
4. The camera reads the back stops, so whether the sheet touches both stops or only one is readable.
5. The camera reads the punch and the lever, so whether the press is up or down is readable.
6. The camera reads the gauge mat from above, so the part on the mat and the gauge held in each bend are
   readable.
7. The camera reads the finished tray pockets, so where the part lands is readable.
8. Both arms are at home with grippers open.
9. The **left arm** reaches the top sheet in the blank tray, the front edge of a sheet on the die, the
   turn spot, and the gauge mat in Config L, without extending to a joint limit.
10. The **right arm** reaches the lever knob, the turn spot, the finished tray, the reject bin, and the
    gauge mat in Config M and R, without extending to a joint limit.
11. The two arms do not collide when the left gripper holds the sheet on the die and the right gripper
    works the lever.
12. If a place cannot be reached, re-park the base by the Base positioning steps until lines 9 to 11
    hold.

### Materials checklist

1. The **press brake mock** is a small hand press made for practice. It bends thin sheet with a lever. It
   has no motor and no foot pedal. Nothing is powered.
2. The **press body** is bolted to the bench in the middle. Nothing moves it, leans on it, or stands
   anything on it.
3. The **die** is the bottom block. It has one **groove** along its top, running left to right. The sheet
   lies on the die with its bend line over the groove.
4. The **punch** is the top blade. It comes straight down into the groove when the lever is pulled, and
   goes straight up when the lever is lifted. It stops hard at the top and at the bottom.
5. The **gap** is the space between the punch and the die. Only the sheet is ever in it.
6. The **back stops** are two fingers behind the die. They stand at the same distance from the groove. A
   sheet pushed back until it touches both fingers has its line over the groove. Nothing moves the stops
   during the episode.
7. The **lever** is a bar with a **knob** on its end, on the **right side** of the press. Pull the knob
   down until it stops to bend. Lift the knob up until it stops to open the press.
8. The lever moves easily by hand. Test it by hand during setup. If it sticks, stop and fix the press.
   Nothing forces it during the episode.
9. The **sheet** is one flat blank of thin, soft sheet. It has a **top face** with three bend lines drawn
   across it. Each line has a number next to it: 1, 2, and 3. Line 1 is near one end. Line 2 is near the
   other end. Line 3 is between line 1 and the middle.
10. The sheet bends at 90 degrees on each line. The press is set to 90 degrees and stays there. Nothing
    changes the press setting during the episode.
11. The finished part is a **C**: a flat bottom, a wall at each end, and a short lip on top of one wall
    that points in.
12. The **blank tray** is a flat tray on the **left** of the press. Flat sheets lie in it in a stack, top
    face up, with line 1 toward the back. The top sheet is the one taken.
13. The **turn spot** is the clear bench directly in front of the die. The part is laid here flat for
    every half turn and for every set-down between grippers. In Config M the gauge mat lies on it.
14. The **gauge** is a small metal square. Its two edges meet at 90 degrees. It is set into a bend to
    check the angle.
15. The **gauge mat** is a rubber mat on the bench. The gauge lies on it. The part is laid on it to be
    gauged. Nothing else is on it. It lies at the spot this episode's config puts it: **in front of the
    blank tray on the left in Config L**, **on the turn spot in the middle in Config M**, **in front of
    the finished tray on the right in Config R**.
16. The **finished tray** is a flat tray with soft pockets on the **right** of the press. Each pocket holds
    one part, bottom down. It has at least one empty pocket.
17. The **reject bin** is an open bin behind the finished tray. A part with a bad bend goes in it.
18. The bench top is clean and clear at the start. No sheet, part, or scrap lies on it, on the die, on
    the turn spot, or on the gauge mat.

### Workspace layout

Nothing is marked or taped out. Every place below is judged by eye from the bench and the press
themselves.

* **Press brake mock:** the middle of the bench. Die at the front, back stops behind it, punch above,
  lever on the right side. Never moved.
  * **Die and groove:** where the sheet lies for every bend. The bend line sits over the groove.
  * **Back stops:** the two fingers behind the die. The sheet is pushed back until it touches both.
  * **Front edge zone:** the strip of sheet that sticks out in front of the die. This is the only place
    the left gripper ever holds the sheet while it is on the die.
  * **Lever and knob:** on the right side of the press. The right gripper on the knob, and only on the
    knob.
* **Turn spot:** directly in front of the die. Half turns and set-downs happen here.
* **Blank tray:** left of the press. Flat sheets start here. Only the top sheet is taken.
* **Gauge mat:** left in front of the blank tray in Config L, on the turn spot in Config M, right in
  front of the finished tray in Config R. The gauge starts and ends here. The part is laid here to be
  gauged.
* **Finished tray:** right of the press. Good parts go here, one to a pocket, bottom down.
* **Reject bin:** behind the finished tray. A part with a bad bend goes here.

### Arm assignments

* **The left gripper is the sheet gripper.** It takes the top sheet from the blank tray, lays it on the
  die, pushes it against the stops, holds it through every cycle, pulls it out, makes both half turns,
  and lays the part on the turn spot or, in Config L and M, on the gauge mat.
* **The right gripper is the lever gripper.** It cycles the press by the knob, and only by the knob, and
  it puts the part in the finished tray or the reject bin.
* **The gauge is worked by the gripper on the gauge mat's side:** the left gripper in Config L, the right
  gripper in Config M and R.
* A part that must change gripper is set down flat on the turn spot by one gripper, let go, and taken up
  by the other. Nothing is passed in the air.
* Each gripper holds one thing at a time. The gauge is never in a gripper while the lever moves.

## Vocabulary

* **In situ:** the press is worked where it is bolted. Nothing is carried away to another table, and
  nothing about the bench is rearranged for the task.
* **Passive base:** the base has no drive. It is pushed by hand to its park before recording, locked
  there, and it does not move at all during the episode.
* **Config:** which of the three gauge mat spots this episode uses. It is set before recording and never
  changes mid-episode.
* **Press up:** the punch is at its top stop. The gap is open. The lever is all the way up.
* **Press down:** the punch is at its bottom stop, in the groove. The lever is all the way down.
* **Cycle:** the right gripper pulls the lever down until it stops, holds it there for 1 second, then
  lifts it up until it stops. One cycle makes one bend.
* **Against the stops:** the back edge of the sheet touches both back stops at the same time. Not one.
  Both.
* **On the line:** the numbered bend line lies right over the die groove, straight, from side to side.
* **Front edge grip:** the left gripper closes on the sheet in the middle of its front edge, top and
  bottom, flat, in front of the die. After a bend, the front edge is the flat bottom just behind the
  wall that now stands at the front, never the wall itself.
* **Half turn:** the sheet stays flat on the turn spot and is turned around, end for end, so the end that
  was at the front is now at the back. The top face stays up. The sheet is never flipped over.
* **Top face up:** the face with the numbers on it points at the ceiling.
* **Low carry:** the sheet or the part is carried close over the bench and level. It never goes over the
  press.
* **Set-down:** the part is laid flat on the turn spot, top face up, and the gripper opens, so the other
  gripper can take it by its front edge.
* **Wall:** the part of the sheet that stands up after a bend.
* **Lip:** the short wall made by bend 3. It points in, over the bottom of the part.
* **Gauged:** the gauge is set into the inside of a bend, with one edge flat on the bottom and the other
  edge flat on the wall, and held still for 2 seconds in front of the camera.
* **Good bend:** the gauge sits flat on both faces with no gap showing on either edge.
* **Bad bend:** a gap shows between the gauge and the bottom or between the gauge and the wall, or the
  bend is not on its line, or the bend is the wrong way up.
* **Seated in the pocket:** the part sits bottom down in one finished tray pocket, inside the pocket
  walls, and does not rock.
* **Reset:** the press is up and empty, the gauge lies on the gauge mat, and both grippers are open and
  clear.
* **Back and clear:** the arm is drawn back so that no part of it is over the press, the gauge mat, or
  the trays.

### Handling standard

* Each gripper holds one thing at a time. Nothing is passed from one gripper to the other in the air.
* The sheet is held only by the left gripper, only by its front edge, and only in front of the die while
  it is on the die. No gripper ever goes under the punch.
* The lever is held only by the right gripper, only by the knob.
* The gauge is held only by its outside corner, only by the gripper on the mat's side.
* Every carry is a low carry. Nothing crosses the press.
* Nothing rests on the press or the bench. No gripper, wrist, or forearm leans on the press body, the
  punch, the back stops, or the bench, and no push is ever hard enough to move a stop.

## Steps

Steps 5 and 6 depend on the config: the gripper on the gauge mat's side works the gauge, and the part is
set down on the turn spot when it must cross from one gripper to the other. Every other step is the same
in all three.

### Step 1: Take a sheet to the press

**Goal:** the flat sheet lies on the die, top face up, with line 1 at the back.

#### 1.1 Take the top sheet

* The **left gripper** closes on the top sheet in the blank tray, in the middle of its front edge, in a
  front edge grip.
* Lift it just off the sheet under it. Do not lift two sheets.

**Check:** one sheet hangs flat in the **left gripper**, top face up, with the numbers showing. If two
sheets came up, put them back and take one.

#### 1.2 Lay it on the die

* The **left gripper** carries the sheet to the press in a low carry. Do not carry it over the press.
* Slide it in from the front, flat, over the die, with line 1 toward the back stops.
* Keep the gripper closed on the front edge. Keep the gripper in front of the die.

**Check:** the sheet lies flat on the die, top face up, with line 1 at the back. The **left gripper** is
in front of the die, not under the punch. If the sheet is upside down, the left gripper takes it back to
the blank tray, turns it over there, and takes it again.

**Expected state:** the sheet lies flat on the die with line 1 toward the back. The **left gripper**
holds its front edge. The press is up.

### Step 2: Bend 1

**Goal:** the sheet is bent at 90 degrees on line 1, and the press is up.

#### 2.1 Push the sheet against the stops

* The **left gripper** pushes the sheet straight back, flat on the die, until its back edge touches both
  back stops.
* Push gently. Do not lift the sheet. Do not turn it.
* Keep the gripper closed and keep pushing lightly, so the sheet stays against the stops.

**Check:** the sheet is against the stops, both of them. Line 1 is on the line, over the groove,
straight from side to side. If only one stop is touched, the left gripper eases off and pushes again,
square. If the line is off the groove, stop and report it. Do not cycle.

#### 2.2 Cycle the press

* The **right gripper** closes on the lever knob.
* Pull the lever down, slow and smooth, until it stops. Hold it there for 1 second.
* Lift the lever up, slow and smooth, until it stops.
* The **left gripper** keeps the hold on the sheet the whole time. The sheet does not move until the
  press is up.

**Check:** the press is up. The sheet has a wall standing up at the back, on line 1. The left gripper
never went under the punch. If the lever stopped short of the bottom, the right gripper pulls it down
again until it stops, then lifts it up.

#### 2.3 Let go of the lever

* The **right gripper** opens on the knob and draws back from the lever.

**Expected state:** the sheet has one wall, at the back. The press is up. The **left gripper** still holds
the front edge. The **right gripper** is back and clear.

### Step 3: Turn the part and bend 2

**Goal:** the sheet is bent at 90 degrees on line 2, and the press is up.

#### 3.1 Take the part out

* The **left gripper** pulls the part straight forward, flat, out of the press, until the wall is clear
  of the punch.
* Lay it flat on the turn spot and open the gripper.

#### 3.2 Half turn

* The **left gripper** closes on the part again by the back edge, now free, and turns it flat on the turn
  spot, a half turn, end for end.
* Do not flip it over. The top face stays up.

**Check:** line 2 is now at the back, and wall 1 is at the front, pointing up. The numbers still face up.
If the part is upside down, the left gripper turns it back over and turns it again, flat.

#### 3.3 Lay it on the die

* The **left gripper** closes on the part in a front edge grip, on the flat bottom just behind wall 1. Do
  not close on the wall.
* Slide it in from the front, flat, over the die, with line 2 toward the back stops.
* Keep the gripper in front of the die.

#### 3.4 Push against the stops

* The **left gripper** pushes the part straight back, flat, until its back edge touches both back stops.
* Keep the gripper closed and keep pushing lightly.

**Check:** the part is against the stops, both of them. Line 2 is on the line, over the groove. If only
one stop is touched, the left gripper eases off and pushes again, square. If the line is off the groove,
stop and report it. Do not cycle.

#### 3.5 Cycle the press

* The **right gripper** closes on the lever knob.
* Pull the lever down, slow and smooth, until it stops. Hold it there for 1 second.
* Lift the lever up, slow and smooth, until it stops.
* The **left gripper** keeps the hold on the part the whole time.

**Check:** the press is up. The part now has two walls, one at each end, both pointing up. If the lever
stopped short of the bottom, the right gripper pulls it down again until it stops, then lifts it up.

#### 3.6 Let go of the lever

* The **right gripper** opens on the knob and draws back from the lever.

**Expected state:** the part has two walls. The press is up. The **left gripper** still holds the front
edge. The **right gripper** is back and clear.

### Step 4: Turn the part and bend 3

**Goal:** the sheet is bent at 90 degrees on line 3, and the press is up.

#### 4.1 Take the part out

* The **left gripper** pulls the part straight forward, flat, out of the press, until wall 2 is clear of
  the punch.
* Lay it flat on the turn spot and open the gripper.

#### 4.2 Half turn

* The **left gripper** closes on the part again and turns it flat on the turn spot, a half turn, end for
  end.
* Do not flip it over. The top face stays up.

**Check:** wall 1 is now at the back and wall 2 is at the front. Line 3 lies between wall 1 and the
middle. If the part is upside down, the left gripper turns it back over and turns it again, flat.

#### 4.3 Lay it on the die

* The **left gripper** closes on the part in a front edge grip, on the flat bottom just behind wall 2. Do
  not close on the wall.
* Slide it in from the front, flat, over the die, with wall 1 toward the back stops.
* Keep the gripper in front of the die.

#### 4.4 Push against the stops

* The **left gripper** pushes the part straight back, flat, until wall 1 touches both back stops.
* Keep the gripper closed and keep pushing lightly.

**Check:** the part is against the stops, both of them. Line 3 is on the line, over the groove. If only
one stop is touched, the left gripper eases off and pushes again, square. If the line is off the groove,
stop and report it. Do not cycle.

#### 4.5 Cycle the press

* The **right gripper** closes on the lever knob.
* Pull the lever down, slow and smooth, until it stops. Hold it there for 1 second.
* Lift the lever up, slow and smooth, until it stops.
* The **left gripper** keeps the hold on the part the whole time.

**Check:** the press is up. The part is now a C: a flat bottom, two walls, and a lip on top of wall 1
that points in. If the lever stopped short of the bottom, the right gripper pulls it down again until it
stops, then lifts it up.

#### 4.6 Let go of the lever and take the part out

* The **right gripper** opens on the knob and draws back from the lever.
* The **left gripper** pulls the part straight forward, flat, out of the press, until the lip is clear of
  the punch.

**Expected state:** the part is a C with three bends. The press is up and empty. The **left gripper**
holds the part by its front edge. The **right gripper** is back and clear.

### Step 5: Gauge the three angles

**Goal:** the gauge has been shown in each of the three bends in front of the camera, and each bend is
known to be good or bad.

#### 5.1 Lay the part on the gauge mat

* **IF Config L:** the **left gripper** carries the part in a low carry to the gauge mat on the left and
  lays it down on the mat, bottom down, with the open side toward the camera. Then it opens and draws
  back.
* **IF Config M:** the **left gripper** lays the part down on the gauge mat on the turn spot, bottom
  down, with the open side toward the camera. Then it opens and draws back.
* **IF Config R:** the **left gripper** makes a set-down on the turn spot and comes back and clear. The
  **right gripper** takes the part by its front edge, carries it in a low carry to the gauge mat on the
  right, and lays it down on the mat, bottom down, with the open side toward the camera. Then it opens
  and draws back.

Do not carry the part over the press.

**Check:** the part sits flat on the mat, bottom down, and does not rock. If it rocks, the gripper that
laid it takes it by its front edge, lifts it, and puts it down again.

#### 5.2 Pick up the gauge

* **IF Config L:** the **left gripper** is the gauge gripper.
* **IF Config M or R:** the **right gripper** is the gauge gripper.

Then, in all three:

* The **gauge gripper** closes on the gauge by its outside corner and lifts it just off the mat.

#### 5.3 Gauge bend 1

* The **gauge gripper** sets the gauge into the inside of bend 1. One edge flat on the bottom. The other
  edge flat on wall 1.
* Hold it still for 2 seconds in front of the camera.

**Check:** the bend is gauged. Both gauge edges against the part are readable. If the gauge is on the
outside of the bend, the gauge gripper lifts it and sets it on the inside.

#### 5.4 Gauge bend 2

* The **gauge gripper** lifts the gauge and sets it into the inside of bend 2. One edge flat on the
  bottom. The other edge flat on wall 2.
* Hold it still for 2 seconds in front of the camera.

#### 5.5 Gauge bend 3

* The **gauge gripper** lifts the gauge and sets it into the inside of bend 3. One edge flat on wall 1.
  The other edge flat on the lip.
* Hold it still for 2 seconds in front of the camera.

#### 5.6 Put the gauge back

* The **gauge gripper** lifts the gauge off the part and lays it flat on the gauge mat where it started,
  away from the part.
* Open the gripper and draw it back.

#### 5.7 Decide good or bad

* If all three bends are good bends, the part is good. Go to Step 6.
* If any bend is a bad bend, the part is a reject. **IF Config L:** the **left gripper** takes the part
  by its front edge, carries it to the turn spot in a low carry, and makes a set-down. **Then, and in
  Config M and R directly:** the **right gripper** takes the part by its front edge, carries it in a low
  carry to the reject bin, opens over the bin, and lets it drop in. Then go to Step 7.
* Do not bend a bad part again. Do not push a bad bend by hand to fix it.

**Expected state:** the part is either on the gauge mat, ready for the tray, or in the reject bin. The
gauge lies on the mat. Both grippers are back and clear.

### Step 6: Put the part in the finished tray

**Goal:** the part sits bottom down in one empty tray pocket.

#### 6.1 Bring it to the right gripper

* **IF Config L:** the **left gripper** closes on the part in a front edge grip, lifts it just off the
  mat, carries it to the turn spot in a low carry, and makes a set-down. The **right gripper** then takes
  it by its front edge and lifts it just off the turn spot.
* **IF Config M or R:** the **right gripper** closes on the part in a front edge grip and lifts it just
  off the mat.

#### 6.2 Carry it to the tray

* The **right gripper** carries the part in a low carry to the finished tray. Do not carry it over the
  press.
* Bring it over the nearest empty pocket.

#### 6.3 Lower it into the pocket

* The **right gripper** lowers the part straight down into the pocket, bottom down.
* Open the gripper and draw it back.

**Check:** the part is seated in the pocket. It sits inside the pocket walls, bottom down, and does not
rock. If it sits on the pocket wall, or on its side, the right gripper takes it by its front edge, lifts
it, and puts it down again.

**Expected state:** the part sits in a tray pocket. The gauge lies on the mat. The press is up and empty.
Both grippers are back and clear.

### Step 7: Check the press and end the episode

**Goal:** the press is up and empty, the part is away, and both arms are safely home.

* Confirm the press is up and the gap is empty, and the back stops stand where they started.
* Confirm the part sits bottom down in one finished tray pocket, or is in the reject bin.
* Confirm the gauge lies flat on the gauge mat, and no sheet or part lies on the bench, on the turn spot,
  or on the die.
* Confirm the base has not moved: it is still square to the bench and still locked.
* Return both arms home, then stop recording.

## After the episode: reset the workspace

This reset is not recorded. The base stays parked and locked through the reset, and is only pushed away
by hand once the bench is set for the next episode.

1. Check the press is up by hand. Lift the lever to its top stop if it is not.
2. Check the gap is empty. Take out any part or scrap by hand.
3. Check the back stops: both stand at the same distance from the groove and do not wobble. Set them
   again if one moved.
4. Check the blank tray has at least one flat sheet in it, top face up, with line 1 toward the back. Add
   sheets if it is empty.
5. Check the top sheet: its three lines are clear and numbered, and it lies flat. Change it if it is bent,
   marked wrong, or has no numbers.
6. Check the finished tray has at least one empty pocket. Change the tray if it is full.
7. Empty the reject bin if it is more than half full.
8. Check the gauge: its edges are clean and straight. Lay the gauge mat at the spot the next episode's
   config puts it, in front of the blank tray for Config L, on the turn spot for Config M, in front of the
   finished tray for Config R, and lay the gauge flat on it, away from the front edge of the mat.
9. Check the lever: it goes all the way down and all the way up by hand with no catch.
10. Check the press body is still bolted tight and does not rock.
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

**Note on the gauge mat:** the violations below were written for Config L (gauge mat on the left, gauge
worked by the left gripper, part set down on the turn spot for the right gripper). The arm-role cues in
them will be rewritten later to cover all three configs; they are left as they are for now. Until then,
anything that does not match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the grippers do does not match the config on the bench. A gripper reaches across
  the press for the gauge or the mat; the gauge is worked by the gripper on the other side; the part is
  set down on the turn spot when the config does not call for it, or carried across without a set-down
  when it does; the gauge mat is not where that config puts it; or the wrong IF line is followed in
  Step 5 or 6.
* **SOP rule broken:** Steps 5.1, 5.2, 5.7, and 6.1, the mat-side rule. The gripper on the gauge mat's side
  works the gauge, a part that changes gripper is set down on the turn spot, and the IF line followed is
  the one for the config on the bench.
* **Coaching note:** look where the gauge mat lies before the first sheet is taken, then follow that
  config's IF lines through Steps 5 and 6.

**Violation: Base moved during the episode**

* **Visible cue:** the bench shifts in the frame, the press changes angle in the frame, or the base rolls,
  creeps, or turns at any time after recording starts.
* **SOP rule broken:** Step 7 and the Base positioning rule it confirms, the base is parked and locked
  before recording and does not move at all during the episode.
* **Coaching note:** park it, lock it, push-test it. If the park is wrong, fix it before recording, never
  during.

**Violation: Gripper under the punch**

* **Visible cue:** a gripper, wrist, or forearm goes into the gap between the punch and the die at any
  time, or the left gripper holds the sheet so close to the die that it is under the punch when the
  lever moves.
* **SOP rule broken:** Steps 2.2, 3.5, and 4.5, only the sheet is ever in the gap, and the left gripper
  holds the front edge, in front of the die.
* **Coaching note:** front edge only. If the punch could touch the gripper, the gripper is in the wrong
  place.

**Violation: Cycled without a hold**

* **Visible cue:** the lever goes down while no gripper holds the sheet, the left gripper lets go of the
  sheet before the press is all the way up, or the sheet is pulled or turned while the punch is down.
* **SOP rule broken:** Steps 2.2, 3.5, and 4.5, keep the hold on the sheet from before the press starts
  down until after it is all the way up.
* **Coaching note:** hold first, cycle second, hold until it is up. A sheet that moves under the punch is
  a reject.

**Violation: Cycled off the stops**

* **Visible cue:** the lever goes down while the sheet touches only one back stop, or neither, the sheet
  is not straight on the die, or the bend line is clearly off the groove.
* **SOP rule broken:** Steps 2.1, 3.4, and 4.4, push the sheet against both stops, check the line is on
  the groove, and only then cycle.
* **Coaching note:** both stops, then look at the line, then cycle. Never cycle to see what happens.

**Violation: Bent on the wrong line**

* **Visible cue:** bend 1 is made on line 2 or line 3, a bend is made where there is no line, or a line
  is bent twice.
* **SOP rule broken:** Steps 2, 3, and 4, line 1, then line 2, then line 3, one bend per line.
* **Coaching note:** read the number before pushing it back. The stops set the place, but the line is
  chosen when the sheet is laid on the die.

**Violation: Wrong turn**

* **Visible cue:** the part is flipped over between bends, so the numbers face down, it is turned a
  quarter turn instead of a half turn, or it goes back in the press with no turn at all.
* **SOP rule broken:** Steps 3.2 and 4.2, between bends the part gets a half turn, flat, end for end, and
  it is never flipped over.
* **Coaching note:** end for end, numbers up. Two half turns, and nothing else.

**Violation: Lever forced or dropped**

* **Visible cue:** the lever is jerked, twisted, pulled sideways, or let go so it drops on its own, or it
  is pushed past its stop.
* **SOP rule broken:** Steps 2.2, 3.5, and 4.5, pull the lever down slow and smooth until it stops, hold
  for 1 second, then lift it up slow and smooth until it stops.
* **Coaching note:** slow down, hold, slow up. The stops do the stopping, not the arm.

**Violation: Press not cycled all the way**

* **Visible cue:** the lever stops short of the bottom, so the bend is not finished, or the lever is left
  part way up, so the press is not up when the sheet is pulled out.
* **SOP rule broken:** Steps 2.2, 3.5, and 4.5, down until it stops, then up until it stops.
* **Coaching note:** to the stop both ways. Almost down is not bent, and almost up is not open.

**Violation: Press body touched or leaned on**

* **Visible cue:** a gripper, wrist, or forearm rests on the press body, the punch, the back stops, or the
  bench, or a back stop is pushed or knocked out of place.
* **SOP rule broken:** Steps 1 to 7, nothing pushes, pulls, lifts, or leans on the press body or the
  bench, and nothing moves the stops.
* **Coaching note:** the arm holds itself up. If something moves when it is touched, it was touched too
  hard.

**Violation: Held by the wrong part**

* **Visible cue:** a gripper closes on the sheet by a side edge, by a wall, or by the lip instead of the
  front edge, on the lever bar instead of the knob, or on the gauge by its edge instead of its corner.
* **SOP rule broken:** Steps 1.1, 2.2, 3.3, 4.3, 5.2, and 6.1, front edge on the sheet, knob on the lever,
  corner on the gauge.
* **Coaching note:** front edge, knob, corner. Three things, three grips.

**Violation: Wrong arm used**

* **Visible cue:** the right gripper takes a sheet from the blank tray, holds the sheet on the die, or
  makes a half turn, or the left gripper takes the lever knob, the finished tray, or the reject bin.
* **SOP rule broken:** Steps 1 to 6, the left gripper is the sheet gripper, the right gripper is the lever
  gripper and puts the part in the tray or the bin.
* **Coaching note:** left hand on the sheet, right hand on the lever. It never changes.

**Violation: Two sheets taken**

* **Visible cue:** two sheets come up out of the blank tray together, or two sheets go onto the die.
* **SOP rule broken:** Step 1.1, take the top sheet and only the top sheet.
* **Coaching note:** one sheet, one episode. If two come up, put them both back and start again.

**Violation: Sheet laid down wrong**

* **Visible cue:** the sheet goes onto the die upside down, with the numbers face down, with line 2 or
  line 3 at the back on the first bend, or on a slant across the die.
* **SOP rule broken:** Step 1.2, lay the sheet flat, top face up, with line 1 toward the back stops.
* **Coaching note:** numbers up, 1 to the back. If the number cannot be read, the line cannot be bent.

**Violation: Carried over the press or passed in the air**

* **Visible cue:** the sheet, the part, or the gauge crosses over the press, a thing is carried high
  instead of low and level, or the part goes from one gripper to the other in the air instead of by a
  set-down on the turn spot.
* **SOP rule broken:** Steps 1.2, 5.1, 5.7, and 6.1, every carry is low and level, never crosses the press,
  and a part changes gripper only by a set-down.
* **Coaching note:** low and around, and down on the turn spot before the other hand takes it.

**Violation: Bend not gauged**

* **Visible cue:** the part goes from the press to the tray with no stop at the gauge mat, one of the
  three bends is skipped, the gauge is set on the outside of a bend, held for less than 2 seconds, or
  turned away from the camera.
* **SOP rule broken:** Steps 5.3, 5.4, and 5.5, set the gauge into the inside of each bend and hold it still
  for 2 seconds in front of the camera.
* **Coaching note:** three bends, three gauges, two seconds each. If the camera did not see the gauge,
  nobody checked the angle.

**Violation: Wrong call on the part**

* **Visible cue:** a part with a gap at the gauge, or a bend off its line, goes into the finished tray, or
  a part with three good bends goes into the reject bin.
* **SOP rule broken:** Step 5.7, three good bends to the tray, any bad bend to the reject bin.
* **Coaching note:** no gap, in the tray. Any gap, in the bin. There is no in between.

**Violation: Bad part bent again**

* **Visible cue:** a part goes back into the press after the gauge, or a gripper pushes on a wall or the
  lip to change the angle by hand.
* **SOP rule broken:** Step 5.7, do not bend a bad part again, do not push a bad bend to fix it.
* **Coaching note:** a bend cannot be undone. A bad bend is a reject, not a retry.

**Violation: Gauge put back wrong**

* **Visible cue:** the gauge is left on the part, on the bench, off the mat, or in the press, or it is
  dropped onto the mat.
* **SOP rule broken:** Step 5.6, lay the gauge flat on the gauge mat where it started.
* **Coaching note:** back where it was. The next episode starts from there.

**Violation: Part not seated in the pocket**

* **Visible cue:** the part ends up on a pocket wall, across two pockets, on its side, rocking, or on top
  of another part.
* **SOP rule broken:** Step 6.3, lower the part straight down into one empty pocket, bottom down, so it
  sits flat.
* **Coaching note:** straight down into one pocket, bottom down. Watch it settle before letting go.

**Violation: Press left with something in it**

* **Visible cue:** the episode ends with the part, a sheet, or scrap still on the die or in the gap.
* **SOP rule broken:** Step 7, the press ends up and empty.
* **Coaching note:** look in the gap before going home. Empty means nothing on the die.

**Violation: Done in the wrong order**

* **Visible cue:** the lever goes down before the sheet is against the stops, the part goes to the tray
  before it is gauged, bend 2 is made before bend 1, bend 3 before bend 2, or the gauge comes out before
  the third bend.
* **SOP rule broken:** Steps 1 to 6, stops, cycle, turn, three times, then gauge, then tray or bin, one
  thing at a time.
* **Coaching note:** the order is the task. Skipping a step is not faster, it is a lost episode.

**Violation: Something dropped or knocked over**

* **Visible cue:** the sheet, the part, or the gauge slips out of a gripper and falls on the bench or the
  floor, or the blank tray, the finished tray, or the reject bin is knocked over by an arm going past.
* **SOP rule broken:** Steps 1 to 6, one thing moves at a time, and each one is put down under control.
* **Coaching note:** close all the way before lifting, and put it down before letting go.

**Violation: Failed check not retried**

* **Visible cue:** a check in a step clearly fails and the episode carries on with no retry: the sheet
  touches one stop, the lever stops short, the gauge is on the outside of a bend, or the part rocks in
  the pocket.
* **SOP rule broken:** Steps 1 to 6, do the retry written under each failed check before moving on.
* **Coaching note:** a check is only worth doing if the retry is done. Fix it where it happened.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with the press down, a part in the gap, the part not in the tray or
  the bin, the gauge off the mat, or an arm away from home.
* **SOP rule broken:** Step 7 (confirm the press, the back stops, the part, the gauge, the bench, and the
  locked base; return both arms home; then stop recording).
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode,
and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot see the die, the back stops, the lever, or the gauge on the part**, so nobody can tell
  if the sheet was against the stops, if the press cycled, or if a bend was good.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake that releases on its own, or a caster that seizes so the base cannot be parked
  square.
* **Defective object:** a sheet that arrives already bent, with no lines or no numbers, with lines drawn
  in the wrong place, or that cracks at a bend made on its line against both stops; a gauge with a bent
  or chipped edge, or whose edges are not at 90 degrees; a tray with pockets too small or too big for
  the part, or that slides on the bench under a correct set down. Replace it before the next episode.
* **Press fault:** a lever that sticks or binds, a punch that does not reach its top or bottom stop, a
  press set to the wrong angle, a back stop that moves on its own, or a press body that rocks on its
  bolts.
* **Reach fault:** a place turns out to be too far for its arm with the base parked correctly, so the top
  sheet, the front edge on the die, the lever knob, the gauge, the turn spot, the finished tray, or the
  reject bin cannot be reached without extending the arm to a limit.

## Annotation subtasks (from SOP)

1. Take the top sheet from the blank tray
2. Lay the sheet on the die
3. Push the sheet against the back stops
4. Pull the lever down and lift it up (bend 1)
5. Take the part out and give it a half turn
6. Lay the part on the die and push it against the back stops
7. Pull the lever down and lift it up (bend 2)
8. Take the part out and give it a half turn
9. Lay the part on the die and push it against the back stops
10. Pull the lever down and lift it up (bend 3)
11. Take the part out of the press
12. Lay the part on the gauge mat
13. Pick up the gauge
14. Gauge bend 1
15. Gauge bend 2
16. Gauge bend 3
17. Put the gauge back on the gauge mat
18. Set the part down on the turn spot for the right gripper (Config L only)
19. Put the part in the finished tray or the reject bin
20. Return both arms home and end the episode
