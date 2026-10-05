# Run a Drill Press Sequence SOP (1x Part: clamp, align, three holes, deburr, unclamp, in situ)

One episode takes one blank part through the drill press where the press is bolted to its bench. Clamp
the blank in the fixture. Line up mark 1 under the bit and drill hole 1. Do the same for mark 2 and mark
3. Clean the top of the three holes with the deburr tool. Open the clamps. Put the part in the finished
tray. Then get the fixture ready for the next part. The episode ends when the part lies in the finished
tray, the fixture is empty, clean, and back at its start stop, the press is switched off, and the chuck
is still. Never split one part into two episodes, and never start a second part in the same episode.

The base is **passive**: it has no drive of its own, so it is pushed by hand up to the bench in front of
the drill press and locked there, and nothing is carried away to another table. Everything the episode
touches is already there when recording starts: the drill press bolted to the bench, the fixture on the
drill table, the blank tray with flat blanks in it, the tool stand with the deburr tool and the chip
brush, the chip tray, and the finished tray.

The press is worked **as found**. It starts switched off, with the bit fitted, the chuck still, and the
bit at its top stop. The fixture starts empty, clean, and locked at its start stop. The blank is a flat
bar with three marks along its top face. Each mark has a small dent punched in its middle and a number
next to it: 1, 2, and 3. The episode ends with the fixture empty and back at the start stop, ready for
the next part.

**This is an in-situ task, and four things follow from that.** First, **the drill press stays bolted
down**: nothing pushes, pulls, lifts, or leans on the press head, the column, the drill table, or the
bench. Second, **nothing comes near a turning bit**: while the chuck turns, no gripper, wrist, or tool is
inside the chuck guard or under the head, and the only gripper near the press is the right gripper on
the feed handle. Third, **the clamps hold the part, never a gripper**: while the chuck turns, both
clamps are closed, the fixture is locked, and no gripper touches the part or the fixture. Fourth, **the
bit only goes down on a mark**: the tip sits in the dent before the press is switched on. If it does
not, the fixture is moved and locked again first. The press is never switched on to see what happens.

A hole cannot be undone. A hole drilled off its mark, or in the wrong place, makes the part a reject. It
is not drilled again. It is not filled. It goes in the finished tray like any other part, and it is
reported.

**The bench is set up in one of two ways.** The drill press, the fixture, the blank tray, the tool
stand, and the chip tray never move. Only the finished tray does.

* **Config L:** the finished tray stands on the **left**, in front of the blank tray.
* **Config R:** the finished tray stands on the **right** of the press, past the feed handle.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on
the setup it says so on an **IF** line. Look at the bench and follow the line that matches.

**Fixed arm roles:** the **left gripper is the part gripper**. It takes the blank, clamps it, moves and
locks the fixture, deburrs, opens the clamps, and takes the part out. The **right gripper is the press
gripper**, because the feed handle is on the right side of the head. It works the ON and OFF buttons and
the feed handle, and it lowers the bit to find each mark. **Tray-side rule:** the finished part goes into
the tray with the gripper on the tray's side. In Config L the left gripper does it. In Config R the left
gripper sets the part down on the set-down spot, and the right gripper takes it from there. Nothing is
passed from one gripper to the other in the air.

Each gripper holds one thing at a time.

The order never changes: **clamp; for each of marks 1, 2, 3: find the mark, lock, drill; then deburr all
three; then open the clamps; then the tray; then the fixture back to its start stop.**

## Setup

Complete the base positioning and all the checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never
steered, pushed, or moved once recording starts. It is parked once, before recording, and does not move
again until the episode is over.

1. Push the base by hand up to the bench and stop it **square to the front edge of the bench**, so the
   front edge runs straight across the frame and neither end sits nearer than the other.
2. Stop it **in the middle of the drill table**, so the left end and the right end of the fixture rail
   are the same distance from the middle of the base.
3. Stop it **close enough** that the **left gripper** reaches both clamp levers and the fixture lock
   lever at both ends of the rail without the arm stretching out, and **far enough** that no arm, wrist,
   or part of the base touches the bench front, the drill table, or the column while both arms work.
4. Check the **feed handle**: with the base parked, the **right gripper** closes on the feed handle knob
   and turns the handle down until the bit tip reaches the fixture, and back up to its top stop, without
   stretching out.
5. Check the **buttons**: the **right gripper** reaches the green ON button and the red OFF paddle on the
   front of the head without passing under the chuck.
6. Check the **bench**: the **left gripper** reaches the top blank in the blank tray, the tool stand, the
   chip tray, the set-down spot, and the finished tray in Config L. The **right gripper** reaches the
   set-down spot and the finished tray in Config R. All without stretching out and without knocking
   anything over.
7. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
8. If any of lines 1 to 6 fails, push the base to a new park by hand and start again at line 1. Do not
   work a bench the arms cannot reach easily.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the bench
or the press hard enough to shift it, nothing and nobody touches it, and it is never moved mid-task. A
base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is in the middle of the drill table, and its frame shows the chuck with its
   guard, the bit, the whole fixture and its rail, both clamps, the fixture lock lever, the feed handle,
   the ON button and OFF paddle, the blank tray, the tool stand, the chip tray, the set-down spot, and the
   finished tray.
3. The camera reads the bit tip over the part, so whether the tip sits in the dent of a mark is readable.
4. The camera reads the chuck, so whether it is turning or still is readable.
5. The camera reads the clamp levers and the fixture lock lever, so whether each is up (open) or down
   (closed) is readable.
6. The camera reads the numbers on the blank, so which mark is under the bit is readable.
7. Both arms are at home with grippers open.
8. The **left arm** reaches the top blank, both clamp levers, the fixture lock lever at both ends of the
   rail, the tool stand, the chip tray, the set-down spot, and the finished tray in Config L, without
   reaching a joint limit.
9. The **right arm** reaches the ON button, the OFF paddle, the feed handle knob through its whole turn,
   the set-down spot, and the finished tray in Config R, without reaching a joint limit.
10. The two arms do not collide when the right gripper holds the feed handle and the left gripper works
    the fixture lock lever.
11. A **person stands at the red stop button** on the wall beside the bench for the whole episode, hands
    off the bench. They press it only if an arm or a tool goes near a turning bit.
12. If a place cannot be reached, park the base again by the Base positioning steps until lines 8 to
    10 hold.

### Materials checklist

1. The **drill press** is a small bench drill press, bolted to the bench in the middle. It is powered.
   Nothing moves it, leans on it, or stands anything on it.
2. The **ON button** is green and the **OFF paddle** is red. Both sit on the front of the head, above and
   to the right of the chuck. The OFF paddle stops the motor with one light press.
3. The **chuck** holds the bit. It has a clear **chuck guard** round it that comes down to just above the
   bit tip. The guard stays closed. The **chuck key is not in the chuck**. It hangs on its hook on the
   column.
4. The **bit** is a sharp 6 mm drill bit, fitted before the episode. It is not changed during the
   episode.
5. The **feed handle** is a three-spoke handle on the **right side** of the head. One spoke has a **knob**
   on its end. Turning the knob down brings the bit down. A spring brings it back up. The **depth stop**
   is set so the bit goes just through the part and 2 mm into the backer, and then stops hard. Nothing
   changes the depth stop during the episode.
6. The **drill table** sits under the head. The **fixture rail** is fixed along the back of the drill
   table, from left to right. It has a **start stop** at its left end.
7. The **fixture** is a flat steel plate that slides left and right along the rail. It has:
   * a **back fence** along its back edge and a **left end stop**. A blank pushed back against the fence
     and left against the end stop sits in the same place every time.
   * a **backer**: a strip of wood under the blank, so the bit goes into wood and not into steel.
   * two **clamps**, one at each end of the blank. Each clamp has a **lever**. Push the lever down to
     press the blank flat. Pull it up to let go.
   * a **lock lever** at its front left corner. Push it down to lock the fixture to the rail. Pull it up
     to let the fixture slide.
8. The **blank** is a flat aluminium bar, 120 mm long, 30 mm wide, and 5 mm thick. Its **top face** has
   three marks along its middle line, 30 mm apart. Each mark is a small cross with a **dent** punched in
   its middle, and a number next to it: 1 on the left, 2 in the middle, 3 on the right.
9. The **blank tray** is a flat tray on the **left** of the press. Blanks lie in it in a stack, top face
   up, with mark 1 on the left. The top blank is the one taken.
10. The **tool stand** is a small block with two upright holes, beside the blank tray. The **deburr tool**
    stands in one hole, handle up. The **chip brush** stands in the other, handle up.
11. The **deburr tool** has a handle and a small hooked blade on its tip. The blade turns freely. It
    shaves off the rough ring of metal left round the top of a hole.
12. The **chip brush** is a small stiff brush with a handle.
13. The **chip tray** is a shallow tray hooked on the front edge of the drill table, under the fixture.
    Chips are brushed forward off the fixture into it.
14. The **set-down spot** is the clear bench directly in front of the drill press base.
15. The **finished tray** is a flat tray with soft pockets, one part to a pocket. It has at least one
    empty pocket. It stands **on the left, in front of the blank tray, in Config L**, and **on the right
    of the press, past the feed handle, in Config R**.
16. At the start the fixture is empty, clean, and locked with its left end against the start stop. Both
    clamp levers are up. The bit is at its top stop. The chuck is still. No chips lie on the fixture, the
    drill table, or the bench.

### Workspace layout

Nothing is taped out. Every place below is judged by eye from the bench and the press themselves.

* **Drill press:** the middle of the bench. Head above, chuck and bit pointing down, drill table below,
  feed handle on the right side, ON button and OFF paddle on the front of the head. Never moved.
  * **Under the head:** the space inside the chuck guard and below it, down to the fixture. No gripper
    goes here while the chuck turns.
  * **Fixture rail and start stop:** along the back of the drill table. The fixture starts and ends at
    the start stop, at the left end.
* **Blank tray:** left of the press. Blanks start here. Only the top blank is taken.
* **Tool stand:** beside the blank tray. The deburr tool and the chip brush start and end here.
* **Chip tray:** on the front edge of the drill table. Chips end here.
* **Set-down spot:** the bench in front of the drill press base. Used in Config R only.
* **Finished tray:** left, in front of the blank tray, in Config L. Right of the press in Config R.

### Arm assignments

* **The left gripper is the part gripper.** It takes the blank, lays it in the fixture, closes and
  opens both clamps, unlocks, slides, and locks the fixture, deburrs, brushes the chips, and takes the
  part out. In Config L it puts the part in the finished tray.
* **The right gripper is the press gripper.** It presses ON and OFF, and it turns the feed handle by the
  knob, and only by the knob. In Config R it takes the part from the set-down spot and puts it in the
  finished tray.
* A part that must change gripper is set down flat on the set-down spot by one gripper, let go, and taken
  up by the other. Nothing is passed in the air.
* Each gripper holds one thing at a time. While the chuck turns, the left gripper holds nothing and waits
  back and clear.

## Vocabulary

* **In situ:** the press is worked where it is bolted. Nothing is carried away to another table, and
  nothing about the bench is changed for the task.
* **Passive base:** the base has no drive. It is pushed by hand to its park before recording, locked
  there, and it does not move at all during the episode.
* **Config:** which side the finished tray stands on. It is set before recording and never changes
  mid-episode.
* **Top stop:** the bit is all the way up. The feed handle is at rest.
* **Depth stop:** the bit is all the way down. The feed handle will not turn further.
* **Running:** the ON button has been pressed and the chuck is turning.
* **Still:** the chuck has stopped turning. It is not slowing. It has stopped.
* **Clamped:** the blank lies flat on the backer, against the back fence and the left end stop, and both
  clamp levers are down.
* **Locked:** the fixture lock lever is down, and the fixture does not slide when pushed gently.
* **Find the mark:** with the chuck still, the right gripper turns the feed handle down until the bit tip
  is just above the blank, so the camera can see where the tip will land.
* **On the mark:** the bit tip, lowered with the chuck still, drops into the dent of the mark without
  the blank moving.
* **Feed:** the right gripper turns the feed handle down slow and smooth, all the way to the depth stop,
  then lets it come back up to the top stop under control.
* **Drilled through:** the hole goes right through the blank, and the bit has touched the backer.
* **Burr:** the thin, rough ring of metal left round the top of a hole.
* **Deburred:** the deburr tool blade has gone round the top of the hole two full turns, and no rough
  ring is left.
* **Back and clear:** the arm is drawn back so that no part of it is under the head, inside the chuck
  guard, or over the fixture.
* **Waits clear:** the gripper is not working. It is back and clear, still in the frame, holding nothing.
* **Set-down:** the part is laid flat on the set-down spot, top face up, and the gripper opens, so the
  other gripper can take it.
* **Low carry:** the blank, the part, or a tool is carried close over the bench and level. It never goes
  under the head.
* **Seated in the pocket:** the part lies top face up in one finished tray pocket, inside the pocket
  walls, and does not rock.

### Handling standard

* Each gripper holds one thing at a time. Nothing is passed from one gripper to the other in the air.
* The blank and the part are held by their two long sides, never by a marked spot or a hole.
* The feed handle is held only by the right gripper, only by the knob.
* The deburr tool and the chip brush are held only by the handle, never by the blade or the bristles.
* While the chuck turns: both clamps down, fixture locked, left gripper back and clear, holding nothing.
* Nothing rests on the press, the drill table, or the bench. No gripper, wrist, or forearm leans on them,
  and no push is ever hard enough to move the fixture when it is locked.

## Steps

Step 6 depends on the config: the part goes into the finished tray with the gripper on the tray's side.
Every other step is the same in both.

### Step 1: Clamp the blank in the fixture

**Goal:** one blank lies clamped in the fixture, top face up, with mark 1 on the left.

#### 1.1 Take the top blank

* With the **left gripper**, close on the top blank in the blank tray by its two long sides, near the
  middle.
* With the **left gripper**, lift it just off the blank under it. Do not lift two blanks.

**Check:** one blank hangs flat in the **left gripper**, top face up, with the numbers showing and mark 1
on the left. If two blanks came up, the left gripper puts them back and takes one.

#### 1.2 Lay it in the fixture

* With the **left gripper**, carry the blank in a low carry to the fixture. Keep it below the chuck
  guard. Do not carry it under the bit.
* With the **left gripper**, lay it flat on the backer, top face up, mark 1 on the left.
* With the **left gripper**, push it back against the back fence and left against the left end stop.
  Then open the gripper.

**Check:** the blank lies flat on the backer, touching the back fence along its whole length and
touching the left end stop. Mark 1 is on the left. If it is upside down or turned, the left gripper takes
it out, turns it the right way over the blank tray, and lays it in again.

#### 1.3 Close the clamps

* With the **left gripper**, push the left clamp lever down until it stops.
* With the **left gripper**, push the right clamp lever down until it stops.

**Check:** the blank is clamped. Both levers are down, and the blank does not move when the left gripper
pushes one end of it gently. If a lever is not all the way down, the left gripper pushes it down again.

**Expected state:** the blank is clamped in the fixture, top face up, mark 1 on the left. The fixture is
locked at its start stop. Both grippers are back and clear.

### Step 2: Drill hole 1

**Goal:** hole 1 is drilled through on mark 1, and the chuck is still.

#### 2.1 Find mark 1

* With the **right gripper**, close on the feed handle knob.
* With the **right gripper**, turn the handle down, slow, until the bit tip is just above the blank, and
  hold it there.

#### 2.2 Line up and lock

* With the **left gripper**, pull the fixture lock lever up.
* With the **left gripper**, slide the fixture to the right along the rail until mark 1 sits right under the bit tip.
* With the **left gripper**, push the lock lever down.
* With the **right gripper**, turn the handle down a little more, until the tip drops into the dent.

**Check:** the tip is on the mark. It sits in the dent of mark 1 and the blank did not move. If the tip
lands beside the dent, the right gripper lifts the tip just clear, and the left gripper unlocks, slides,
and locks again.

#### 2.3 Raise the bit and switch on

* With the **right gripper**, let the handle come back up, under control, to the top stop. Then open the
  gripper.
* The **left gripper** draws back and clear, holding nothing, and waits there.
* With the **right gripper**, press the green ON button once. Wait 2 seconds for the chuck to reach full
  speed.

**Check:** the chuck is running. Both clamp levers and the lock lever are down. The left gripper is back
and clear. If any of these is not true, the right gripper presses the OFF paddle, waits for the chuck to
be still, and the fault is fixed first.

#### 2.4 Drill

* With the **right gripper**, close on the feed handle knob.
* With the **right gripper**, feed: turn the handle down, slow and smooth, until it stops at the depth
  stop.
* With the **right gripper**, let the handle come back up, under control, to the top stop. Keep the
  gripper on the knob all the way.

**Check:** the handle reached the depth stop, and the bit is back at the top stop. If the handle stopped
short, the right gripper feeds again to the depth stop.

#### 2.5 Switch off

* With the **right gripper**, open on the knob and move to the OFF paddle, keeping below the head and
  outside the chuck guard.
* With the **right gripper**, press the red OFF paddle once.
* Wait until the chuck is still.

**Expected state:** hole 1 is drilled through on mark 1. The chuck is still, and the bit is at its top
stop. The fixture is locked. Both grippers are back and clear.

### Step 3: Drill hole 2

**Goal:** hole 2 is drilled through on mark 2, and the chuck is still.

#### 3.1 Find mark 2

* With the **right gripper**, close on the feed handle knob.
* With the **right gripper**, turn the handle down, slow, until the bit tip is just above the blank, and
  hold it there.

#### 3.2 Line up and lock

* With the **left gripper**, pull the fixture lock lever up.
* With the **left gripper**, slide the fixture to the left along the rail until mark 2 sits right under
  the bit tip.
* With the **left gripper**, push the lock lever down.
* With the **right gripper**, turn the handle down a little more, until the tip drops into the dent.

**Check:** the tip is on the mark. It sits in the dent of mark 2, not in hole 1, and the blank did not
move. If the tip lands beside the dent, the right gripper lifts the tip just clear, and the left gripper
unlocks, slides, and locks again.

#### 3.3 Raise the bit and switch on

* With the **right gripper**, let the handle come back up, under control, to the top stop. Then open the
  gripper.
* The **left gripper** draws back and clear, holding nothing, and waits there.
* With the **right gripper**, press the green ON button once. Wait 2 seconds.

**Check:** the chuck is running. Both clamp levers and the lock lever are down. The left gripper is back
and clear. If not, the right gripper presses OFF, waits for the chuck to be still, and the fault is fixed
first.

#### 3.4 Drill

* With the **right gripper**, close on the feed handle knob.
* With the **right gripper**, feed to the depth stop, slow and smooth.
* With the **right gripper**, let the handle come back up, under control, to the top stop.

**Check:** the handle reached the depth stop, and the bit is back at the top stop. If it stopped short,
the right gripper feeds again.

#### 3.5 Switch off

* With the **right gripper**, open on the knob and press the red OFF paddle once.
* Wait until the chuck is still.

**Expected state:** holes 1 and 2 are drilled through. The chuck is still, and the bit is at its top
stop. The fixture is locked. Both grippers are back and clear.

### Step 4: Drill hole 3

**Goal:** hole 3 is drilled through on mark 3, and the chuck is still.

#### 4.1 Find mark 3

* With the **right gripper**, close on the feed handle knob.
* With the **right gripper**, turn the handle down, slow, until the bit tip is just above the blank, and
  hold it there.

#### 4.2 Line up and lock

* With the **left gripper**, pull the fixture lock lever up.
* With the **left gripper**, slide the fixture to the left along the rail until mark 3 sits right under
  the bit tip.
* With the **left gripper**, push the lock lever down.
* With the **right gripper**, turn the handle down a little more, until the tip drops into the dent.

**Check:** the tip is on the mark. It sits in the dent of mark 3 and the blank did not move. If the tip
lands beside the dent, the right gripper lifts the tip just clear, and the left gripper unlocks, slides,
and locks again.

#### 4.3 Raise the bit and switch on

* With the **right gripper**, let the handle come back up, under control, to the top stop. Then open the
  gripper.
* The **left gripper** draws back and clear, holding nothing, and waits there.
* With the **right gripper**, press the green ON button once. Wait 2 seconds.

**Check:** the chuck is running. Both clamp levers and the lock lever are down. The left gripper is back
and clear. If not, the right gripper presses OFF, waits for the chuck to be still, and the fault is fixed
first.

#### 4.4 Drill

* With the **right gripper**, close on the feed handle knob.
* With the **right gripper**, feed to the depth stop, slow and smooth.
* With the **right gripper**, let the handle come back up, under control, to the top stop.

**Check:** the handle reached the depth stop, and the bit is back at the top stop. If it stopped short,
the right gripper feeds again.

#### 4.5 Switch off

* With the **right gripper**, open on the knob and press the red OFF paddle once.
* Wait until the chuck is still.
* The **right gripper** draws back and waits clear of the press.

**Expected state:** all three holes are drilled through, one on each mark. The chuck is still, and the
bit is at its top stop. The part is still clamped. Both grippers are back and clear.

### Step 5: Deburr the three holes

**Goal:** the top of each of the three holes is deburred, with the part still clamped and the chuck
still.

#### 5.1 Brush the chips off the part

* With the **left gripper**, take the chip brush from the tool stand by its handle.
* With the **left gripper**, brush the chips off the top of the part, forward, off the fixture and into
  the chip tray. Keep the brush below the chuck guard.
* With the **left gripper**, stand the brush back in its hole in the tool stand, handle up.

**Check:** the top of the part is clear of chips, and all three holes can be seen.

#### 5.2 Take the deburr tool

* With the **left gripper**, take the deburr tool from the tool stand by its handle, blade down.
* With the **left gripper**, carry it in a low carry to the fixture.

#### 5.3 Deburr hole 1

* With the **left gripper**, set the blade tip into the top of hole 1, tool straight up.
* With the **left gripper**, turn the tool two full turns clockwise, pressing lightly down.
* With the **left gripper**, lift the tool straight up out of the hole.

**Check:** the top of hole 1 is deburred. The rough ring is gone and a thin bright edge shows all round.
If a rough spot is left, the left gripper sets the blade in again and turns one more full turn.

#### 5.4 Deburr hole 2

* With the **left gripper**, set the blade tip into the top of hole 2, tool straight up.
* With the **left gripper**, turn the tool two full turns clockwise, pressing lightly down.
* With the **left gripper**, lift the tool straight up out of the hole.

#### 5.5 Deburr hole 3

* With the **left gripper**, set the blade tip into the top of hole 3, tool straight up.
* With the **left gripper**, turn the tool two full turns clockwise, pressing lightly down.
* With the **left gripper**, lift the tool straight up out of the hole.

#### 5.6 Put the deburr tool back

* With the **left gripper**, carry the tool in a low carry to the tool stand and stand it in its hole,
  handle up.
* With the **left gripper**, open and draw back.

**Expected state:** all three holes are deburred. The part is still clamped. The deburr tool and the chip
brush stand in the tool stand. The chuck is still. Both grippers are back and clear.

### Step 6: Unclamp the part and put it in the finished tray

**Goal:** the finished part lies in one empty pocket of the finished tray, top face up.

#### 6.1 Open the clamps

* With the **left gripper**, pull the right clamp lever up until it stops.
* With the **left gripper**, pull the left clamp lever up until it stops.

**Check:** both levers are up and the part lies loose on the backer.

#### 6.2 Take the part out

* With the **left gripper**, close on the part by its two long sides, near the middle.
* With the **left gripper**, lift it straight up off the backer, then draw it forward, out from under
  the head, in a low carry.

#### 6.3 Put it in the tray

* **IF Config L:** with the **left gripper**, carry the part in a low carry to the finished tray, bring it
  over the nearest empty pocket, and lower it straight down into the pocket, top face up. Then open and
  draw back.
* **IF Config R:** with the **left gripper**, make a set-down on the set-down spot, then draw back and
  clear. With the **right gripper**, close on the part by its two long sides, lift it, carry it in a low
  carry to the finished tray, bring it over the nearest empty pocket, and lower it straight down into the
  pocket, top face up. Then open and draw back.

**Check:** the part is seated in the pocket. It lies inside the pocket walls, top face up, and does not
rock. If it sits on a pocket wall, the gripper that placed it lifts it and puts it down again.

**Expected state:** the part lies in a finished tray pocket. The fixture is empty. Both grippers are back
and clear.

### Step 7: Get the fixture ready for the next part

**Goal:** the fixture is empty, free of chips, and locked at its start stop.

#### 7.1 Brush the fixture

* With the **left gripper**, take the chip brush from the tool stand by its handle.
* With the **left gripper**, brush the chips off the backer and the fixture plate, forward, into the chip
  tray. Keep the brush below the chuck guard.
* With the **left gripper**, stand the brush back in its hole in the tool stand, handle up.

**Check:** no chips lie on the backer, the fixture plate, or along the back fence and end stop.

#### 7.2 Slide it back to the start stop

* With the **left gripper**, pull the fixture lock lever up.
* With the **left gripper**, slide the fixture to the left along the rail until its left end touches the
  start stop.
* With the **left gripper**, push the lock lever down. Then open and draw back.

**Check:** the fixture touches the start stop and is locked. Both clamp levers are up.

**Expected state:** the fixture is empty, clean, and locked at its start stop, ready for the next part.
Both grippers are back and clear.

### Step 8: End the episode

**Goal:** the bench is ready for the next part, and both arms are safely home.

* Look once across the bench: the part lies in the finished tray, the fixture is empty, clean, and
  locked at its start stop, the tools stand in the tool stand, the chuck is still, and the bit is at its
  top stop.
* Return both arms home.
* Stop recording.

**Check:** both arms are at home with grippers open, and the base has not moved.

**Expected state:** the part is in the finished tray, the fixture is ready for the next part, and both
arms are home.

## After the episode: reset the workspace

This reset is not recorded. The base stays parked and locked through the reset, and is only pushed away
by hand once the bench is set for the next episode.

1. Check the press is switched off and the chuck is still. Check the chuck key hangs on its hook, not in
   the chuck.
2. Check the bit is sharp and straight, and fitted tight. Change it if it is blunt, chipped, or bent.
3. Check the depth stop has not moved: the bit goes just through a blank and 2 mm into the backer.
4. Check the backer: if the three bit marks in it are deep or torn, turn it or change it.
5. Check the fixture is empty, free of chips, locked at its start stop, with both clamp levers up.
6. Check the blank tray has at least one blank in it, top face up, mark 1 on the left. Add blanks if it
   is empty.
7. Check the top blank: its three marks, dents, and numbers are clear. Change it if it is bent or marked
   wrong.
8. Check the deburr tool blade turns freely and is sharp, and stands in the tool stand with the chip
   brush.
9. Empty the chip tray if it is more than half full.
10. Take the parts out of the finished tray if it has no empty pocket. Stand the finished tray where the
    next episode's config puts it: on the left, in front of the blank tray, for Config L, or on the right
    of the press, past the feed handle, for Config R.
11. Check the press is still bolted tight and does not rock.
12. Check the base is still square, in the middle, and locked, and push it firmly once by hand to confirm
    it does not roll. If it has moved, park it again by the Base positioning steps.
13. Run the Setup checklists again.

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

**Violation: Config misaligned**

* **Visible cue:** the finished tray is not where the config puts it; the left gripper reaches across the
  press to a tray on the right; the part is set down on the set-down spot in Config L, or carried to the
  right tray with no set-down in Config R; or the wrong IF line is followed in Step 6.3.
* **SOP rule broken:** Step 6.3, the tray-side rule. The gripper on the tray's side puts the part in the
  tray, and a part that changes gripper is set down on the set-down spot.
* **Coaching note:** look where the finished tray stands before the first blank is taken.

**Violation: Base moved during the episode**

* **Visible cue:** the bench shifts in the frame, the press changes angle in the frame, or the base rolls,
  creeps, or turns at any time after recording starts.
* **SOP rule broken:** Base positioning, the base is parked and locked before recording and does not move
  at all during the episode.
* **Coaching note:** park it, lock it, push-test it. If the park is wrong, fix it before recording, never
  during.

**Violation: Gripper near a turning bit**

* **Visible cue:** while the chuck is running or still slowing, a gripper, wrist, or tool goes inside the
  chuck guard or under the head, or the left gripper is not back and clear.
* **SOP rule broken:** Steps 2.3 to 2.5, 3.3 to 3.5, and 4.3 to 4.5, while the chuck turns, the only
  gripper near the press is the right gripper on the feed handle knob, and the left gripper waits back
  and clear.
* **Coaching note:** if the chuck is turning, the left arm is out. No exceptions.

**Violation: Drilled unclamped or unlocked**

* **Visible cue:** the chuck runs or the bit goes down into the part while a clamp lever is up, the lock
  lever is up, or a gripper holds the part or the fixture.
* **SOP rule broken:** Steps 1.3, 2.2, 3.2, 4.2, and the checks in 2.3, 3.3, and 4.3, both clamps down and
  the fixture locked before ON, and the clamps hold the part, never a gripper.
* **Coaching note:** three levers down before the green button. The clamps hold it, not the arm.

**Violation: Switched on with the bit down**

* **Visible cue:** the ON button is pressed while the bit tip is in the dent or touching the part, or
  while the right gripper is still holding the handle down.
* **SOP rule broken:** Steps 2.3, 3.3, and 4.3, let the bit back up to the top stop, then press ON.
* **Coaching note:** find the mark, go back up, then switch on. The bit starts in the air.

**Violation: Drilled off the mark**

* **Visible cue:** the bit comes down with the tip beside the dent, or the finished hole is clearly off its
  cross.
* **SOP rule broken:** Steps 2.2, 3.2, and 4.2, the tip sits in the dent before the press is switched on.
* **Coaching note:** the tip must drop into the dent. If it lands beside it, unlock, slide, lock, and look
  again.

**Violation: Wrong hole drilled**

* **Visible cue:** the holes are not drilled in the order 1, 2, 3; a mark is skipped; a hole is drilled
  twice; or a hole is drilled where there is no mark.
* **SOP rule broken:** Steps 2, 3, and 4, mark 1, then mark 2, then mark 3, one hole on each.
* **Coaching note:** read the number under the tip before locking.

**Violation: Feed forced or let go**

* **Visible cue:** the handle is turned down fast or in jerks, pushed past the depth stop, or let go so it
  springs back up on its own.
* **SOP rule broken:** Steps 2.4, 3.4, and 4.4, feed slow and smooth to the depth stop, then let the
  handle back up under control, with the gripper on the knob all the way.
* **Coaching note:** slow down, slow up. The bit does the cutting, not the arm.

**Violation: Hole not drilled through**

* **Visible cue:** the handle stops short of the depth stop and is not fed again, so a hole does not go
  right through.
* **SOP rule broken:** Steps 2.4, 3.4, and 4.4, feed all the way to the depth stop.
* **Coaching note:** to the stop every time. Almost through is not a hole.

**Violation: Worked before the chuck was still**

* **Visible cue:** a gripper unlocks the fixture, touches the part, the fixture, or a tool, or goes under
  the head while the chuck is still slowing after OFF, or the press is left running after a hole.
* **SOP rule broken:** Steps 2.5, 3.5, and 4.5, press OFF after every hole and wait until the chuck is
  still.
* **Coaching note:** slowing is not still. Watch the chuck stop.

**Violation: Hole not deburred**

* **Visible cue:** a hole is skipped at the deburr, the tool turns less than two full turns, or a rough
  ring is still visible and not retried.
* **SOP rule broken:** Steps 5.3, 5.4, and 5.5, two full turns in the top of every hole.
* **Coaching note:** three holes, two turns each. Look for the bright edge.

**Violation: Deburred wrong**

* **Visible cue:** the tool is held on a slant, turned the wrong way, pressed hard enough to dig a deep
  cone, dragged across the part, or used while the part is unclamped or the chuck is running.
* **SOP rule broken:** Step 5, tool straight up, clockwise, light press, part clamped, chuck still.
* **Coaching note:** straight, light, two turns. The blade shaves; it does not dig.

**Violation: Blank not seated in the fixture**

* **Visible cue:** the blank is clamped away from the back fence or the left end stop, lying on a chip, on
  a slant, or with a clamp lever not all the way down.
* **SOP rule broken:** Steps 1.2 and 1.3, lay the blank flat, push it back against the fence and left
  against the end stop, then push both clamp levers all the way down.
* **Coaching note:** fence, end stop, two levers. Push it home before it is clamped.

**Violation: Blank laid wrong way**

* **Visible cue:** the blank goes into the fixture upside down, with the numbers facing down, or turned so
  mark 3 is on the left.
* **SOP rule broken:** Step 1.2, top face up, mark 1 on the left.
* **Coaching note:** numbers up, 1 on the left. If the number cannot be read, the mark cannot be found.

**Violation: Two blanks taken**

* **Visible cue:** two blanks come up out of the blank tray together, or two blanks go into the fixture.
* **SOP rule broken:** Step 1.1, take the top blank and only the top blank.
* **Coaching note:** one blank, one episode. If two come up, put both back and take one.

**Violation: Fixture forced or knocked**

* **Visible cue:** the fixture is pushed while locked, shoved hard enough to bang the start stop, lifted
  off the rail, or a lever is hit instead of pushed or pulled.
* **SOP rule broken:** Steps 2.2, 3.2, 4.2, and 7.2, unlock, slide gently, lock.
* **Coaching note:** lever up before it moves, lever down after. It slides; it is not pushed hard.

**Violation: Held by the wrong part**

* **Visible cue:** a gripper closes on the blank or the part over a mark or a hole, on the feed handle by
  a spoke instead of the knob, on the deburr tool by its blade, or on the chip brush by its bristles.
* **SOP rule broken:** Handling standard and Steps 1.1, 2.1, 5.1, 5.2, and 6.2, long sides on the part,
  knob on the handle, handle on the tools.
* **Coaching note:** sides, knob, handle.

**Violation: Wrong arm used**

* **Visible cue:** the right gripper takes a blank, works a clamp or the lock lever, deburrs, or brushes,
  or the left gripper presses ON or OFF or turns the feed handle.
* **SOP rule broken:** Arm assignments and Steps 1 to 7, the left gripper is the part gripper, the right
  gripper is the press gripper.
* **Coaching note:** left hand on the part and the fixture, right hand on the press.

**Violation: Carried under the head or passed in the air**

* **Visible cue:** the blank, the part, or a tool is carried under the bit or high over the bench, or the
  part goes from one gripper to the other in the air instead of by a set-down.
* **SOP rule broken:** Steps 1.2, 5.2, 6.2, and 6.3, every carry is low and level, never under the bit, and
  a part changes gripper only by a set-down.
* **Coaching note:** low and in from the front, and down on the set-down spot before the other hand takes
  it.

**Violation: Part not seated in the pocket**

* **Visible cue:** the part ends up on a pocket wall, across two pockets, face down, rocking, or on top of
  another part.
* **SOP rule broken:** Step 6.3, lower the part straight down into one empty pocket, top face up.
* **Coaching note:** straight down into one pocket. Watch it settle before letting go.

**Violation: Fixture not ready for the next part**

* **Visible cue:** the episode ends with chips on the fixture or the backer, the fixture away from the
  start stop, the lock lever up, a clamp lever down, or a tool left out of the tool stand.
* **SOP rule broken:** Steps 5.6 and 7, brush the fixture clean, slide it back to the start stop, lock it,
  and stand the tools back in the tool stand.
* **Coaching note:** the next part starts where this one ended. Leave it clean and at the stop.

**Violation: Done in the wrong order**

* **Visible cue:** a hole is drilled before the blank is clamped, the deburr starts before all three holes
  are drilled, the clamps open before the deburr, or the fixture is slid back before the part is out.
* **SOP rule broken:** Steps 1 to 7, clamp, three holes, deburr, unclamp, tray, fixture back.
* **Coaching note:** the order is the task. Skipping ahead is not faster, it is a lost episode.

**Violation: Something dropped or knocked over**

* **Visible cue:** the blank, the part, the deburr tool, or the chip brush slips out of a gripper and
  falls, or the blank tray, the tool stand, the chip tray, or the finished tray is knocked by an arm going
  past.
* **SOP rule broken:** Steps 1 to 7, one thing moves at a time, and each one is put down under control.
* **Coaching note:** close all the way before lifting, and put it down before letting go.

**Violation: Failed check not retried**

* **Visible cue:** a check in a step clearly fails and the episode carries on with no retry: the tip lands
  beside the dent, a clamp lever is not all the way down, the handle stops short, a rough ring is left,
  or the part rocks in the pocket.
* **SOP rule broken:** Steps 1 to 7, do the retry written under each failed check before moving on.
* **Coaching note:** fix it where it happened.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with the chuck turning, the part still in the fixture, or an arm away
  from home, or the arms go home before the look across the bench.
* **SOP rule broken:** Step 8, look once across the bench, return both arms home, then stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode,
and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot see the bit tip over the mark, the chuck, or the levers**, so nobody can tell if the tip
  was on the mark, if the chuck was still, or if the part was clamped.
* **Red stop button pressed by the standby person** for a reason not caused by the arms.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake that lets go on its own, or a caster that sticks so the base cannot be parked
  square.
* **Bad object:** a blank that arrives bent, with a mark missing, a dent missing, or numbers wrong; a bit
  that is blunt, bent, or loose in the chuck; a deburr tool whose blade does not turn; a backer too torn to
  hold the blank flat. Replace it before the next episode.
* **Press fault:** a motor that does not start or stop on one press, a feed handle that sticks, a depth
  stop that slips, a fixture that slides while locked, a clamp that does not hold, or a press that rocks
  on its bolts.
* **Reach fault:** a place turns out to be too far for its arm with the base parked correctly.

## Annotation subtasks (from SOP)

1. Take the top blank from the blank tray
2. Lay the blank in the fixture against the fence and end stop
3. Close both clamps
4. Find mark 1, line up, and lock the fixture
5. Raise the bit and switch on
6. Drill hole 1 and switch off
7. Find mark 2, line up, and lock the fixture
8. Raise the bit and switch on
9. Drill hole 2 and switch off
10. Find mark 3, line up, and lock the fixture
11. Raise the bit and switch on
12. Drill hole 3 and switch off
13. Brush the chips off the part
14. Take the deburr tool
15. Deburr hole 1
16. Deburr hole 2
17. Deburr hole 3
18. Put the deburr tool back
19. Open both clamps and take the part out
20. Set the part down on the set-down spot (Config R only)
21. Put the part in the finished tray
22. Brush the fixture clean
23. Slide the fixture back to the start stop and lock it
24. Return both arms home and end the episode
