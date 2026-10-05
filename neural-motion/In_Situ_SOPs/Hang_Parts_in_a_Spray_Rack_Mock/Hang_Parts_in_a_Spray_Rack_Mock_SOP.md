# Hang Parts in a Spray Rack Mock SOP (1x Episode: one rack, in situ)

One episode hangs one load of parts on a spray rack mock and stages it at the booth, in the paint bay where the
rack lives. The base is **passive**: it has no drive of its own, so it is pushed by hand to the front of the rack
cart and locked there, and nothing is carried away to a table. Everything the episode touches is already in the
bay when recording starts: the rack cart on its track with the rack on it, the tray of parts on the cart, and the
booth mock at the right end of the track.

The episode runs these four actions in this order and no other: **hook the parts on the rack spindles with
spacing, rotate the rack, verify that no part is touching, stage the cart to the booth.** Each one is a step, and
the steps run in that order.

The bay is worked **as found**. The rack cart stands braked at its **load mark**, the rack is turned with its
spindles pointing at the base, and both spindles are empty. Six parts lie in the parts tray on the cart, each with
its wire hook already fitted. The episode ends with the six parts hanging three to a spindle, one in each notch, the
rack turned a quarter turn and locked with its spindles pointing at the booth, no part touching anything, and the
cart braked against the booth stop.

**Spacing is set by the notches.** Each spindle has three notches along its top. One part hangs in each notch, and
no notch is left empty or holds two parts. A part hung in its notch hangs a clear gap away from the parts beside it.

**This is an in-situ task, and three things follow from that.** First, the **booth is a wet paint zone**: no
gripper, wrist, or forearm ever goes into the booth or touches its walls. Only the cart goes in, and only as far as
the booth stop. Second, the **rack and the cart are never leaned on, lifted, or pushed out of turn**: the rack turns
only in Step 2, by its turn handle, and the cart moves only in Step 4, along its track, by its push bar. Third, **a
hung part hangs free**: once a part is in its notch, nothing touches it except to put right a part found touching
in Step 3.

The bay is set up in one of three ways. Only the **parts tray** moves. The cart, the rack, the track, and the booth
are in the same place in all three.

* **Config L:** the parts tray stands on the cart's lower deck at its **left end**.
* **Config M:** the parts tray stands on the cart's lower deck in its **middle**.
* **Config R:** the parts tray stands on the cart's lower deck at its **right end**.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup
it says so on an **IF** line. Look at the cart and follow the line that matches.

What stays constant across all sessions:

* **Tray-side rule:** one gripper hangs all six parts. That is the **left gripper** in Config L and the **right
  gripper** in Config M and R. It is called the **hanging gripper**. The other gripper stays clear of the rack for
  all of Step 1. Nothing is handed over.
* **Fixed roles:** the **left gripper** lifts the lock pin and works the cart brake. The **right gripper** turns the
  rack and puts right any part found touching. **Both grippers** push the cart. The four actions run in the same
  order in every config.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches
over, under, around, or past the other. Nothing is moved two at a time: one gripper holds one part, and the other
gripper is empty or clear of the rack.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered,
nudged, or repositioned once recording starts. It is parked once, before recording, and does not move again until
the episode is over.

1. Push the base by hand up to the front of the rack cart and stop it **square to the track**, so the track runs
   straight across the frame of the camera.
2. Stop it **centered on the cart's run**, so the middle of the base is in line with the point halfway between the
   load mark and the booth stop.
3. Stop it **close enough** that both grippers reach the push bar with the cart at the load mark and at the booth
   stop without either arm extending, and **far enough** that no part of either arm or the base touches the cart, the
   rack, or a spindle tip.
4. Check the **hanging reach**: with the cart at the load mark, the **left gripper** and the **right gripper** each
   reach every notch on both spindles from above, and each reaches the parts tray at its own end and in the middle.
5. Check the **rack reach**: the **left gripper** reaches the lock pin and the brake lever, and the **right gripper**
   reaches the turn handle through the whole quarter turn, all without extending.
6. Check the **booth**: with the cart at the booth stop, the **right gripper** reaches the push bar and the rows of
   hung parts from the front without going into the booth.
7. Check the **parts tray** for the config this episode runs: in **Config L** the **left gripper** reaches every part in
   the tray; in **Config M** and **Config R** the **right gripper** does.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not work a rack
   the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the cart hard enough to
shift the base, nothing touches it by hand, and it is never repositioned mid-task. A base that moves after recording
starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the cart's run and its frame includes the whole of it: the cart at the load
   mark, the rack and both spindles, the parts tray, the lock pin, the turn handle, the brake lever, the track, the
   booth mouth, and the booth stop.
3. The camera reads the **notches** on both spindles, so which notch each hook sits in is readable.
4. With the rack turned, the camera looks **along each row**, so the gap between every two hung parts is readable.
5. The camera reads the **load mark** and the **booth stop**, so where the cart stands is readable.
6. Both arms are at home with grippers open.
7. Each arm reaches every notch on both spindles from above without extending to a joint limit.
8. The **left arm** reaches the lock pin and the brake lever, and the **right arm** reaches the turn handle through its
   whole quarter turn, without extending to a joint limit.
9. Both arms reach the push bar with the cart at the load mark and at the booth stop without extending to a joint
   limit, and neither goes into the booth.
10. The two arms do not collide, and neither arm passes in front of the other.
11. If a place cannot be reached, re-park the base by the Base positioning steps until lines 7 to 10 hold.

### Materials checklist

1. The **paint bay** has a raised **deck** with a straight **track** on it: two guide rails that keep the cart's wheels
   in line. The track runs left to right across the front of the base.
2. The **load mark** is taped across the track at its left part. The cart starts with its left end on the load mark.
3. The **booth mock** is a fixed three-walled box at the right end of the track, open at the front and at its left
   side, with its roof high enough for the rack to roll in under it. It is not moved or touched at any point.
4. The **booth stop** is a bar fixed across the track inside the booth mouth. A cart rolled to it has its right end
   touching the stop and its rack inside the booth mouth.
5. The **rack cart** is a low two-deck cart with its wheels in the track. It rolls freely along the track and nowhere
   else. It starts at the load mark with its brake on.
6. The **push bar** runs along the front of the cart's top deck. The **brake lever** is at the left end of the push
   bar: down is braked, up is free.
7. The **rack** stands on a **turntable** in the middle of the cart's top deck. It is a flat upright frame with **two
   spindles**, an **upper spindle** and a **lower spindle**, one above the other on the frame's middle line. Each
   spindle is a straight rod standing out from the frame with a turned-up tip at its end.
8. Each spindle has **three notches** along its top, cut the same distance apart, so parts hung in two notches side by
   side hang a clear gap apart. The **inner notch** is the one nearest the frame and the **outer notch** is the one
   nearest the tip. The two spindles are far enough apart that a part hung on the upper spindle hangs a clear gap above
   the hooks on the lower spindle.
9. At the start the rack is turned so both spindles point **straight at the base**, and the **lock pin** holds the
   turntable there.
10. The **lock pin** stands up from the cart deck at the front edge of the turntable and sits in a hole in it. Lifted by
    its knob, it frees the turntable. Let go, it rides on the turntable's edge and drops into the next hole, a quarter
    turn on, with a click.
11. The **turn handle** stands up from the edge of the turntable at its front-right.
12. The **parts tray** is an open tray on the cart's lower deck, at the left end in **Config L**, in the middle in
    **Config M**, and at the right end in **Config R**.
13. There are **six parts**, all the same: flat, light, dry metal brackets with a hang hole at the top. Each one has a
    **wire hook** already fitted through its hang hole: a **shank** above the part and a **curl** at the top that sits
    in a notch. The parts lie flat in the tray, side by side, hooks up, none on top of another, no hook caught in
    another.
14. Nothing else stands on the cart, the track, or the deck within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the load mark and the notches. You judge every other place by eye
against the cart and the track.

* **Track:** the two rails on the deck the cart rolls along. Nothing but the cart's wheels touches it.
* **Load mark:** the taped line at the left part of the track where the cart starts.
* **Booth mock:** the three-walled box at the right end of the track. **No gripper, ever.**
* **Booth stop:** the bar across the track inside the booth mouth, where the cart ends.
* **Rack cart:** the two-deck cart on the track, with the push bar at the front and the brake lever at its left end.
* **Rack:** the upright frame on the turntable, with the upper and lower spindles.
* **Lock pin:** at the front edge of the turntable. **Left gripper only.**
* **Turn handle:** on the turntable edge at its front-right. **Right gripper only.**
* **Brake lever:** at the left end of the push bar. **Left gripper only.**
* **Parts tray:** on the cart's lower deck, at the left end, the middle, or the right end by config. **Hanging gripper
  only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **hanging gripper** works the parts tray and both spindles in Step 1. The other gripper is drawn **clear of the
  rack** until Step 1 is done.
* The **left gripper** works the lock pin and the brake lever. The **right gripper** works the turn handle and puts
  right any touching part.
* On the push bar the **left gripper** holds left of the **right gripper**.
* Neither arm goes into the booth, and neither reaches over, under, around, or past the other.
* Only one part is moved at a time.

### Arm assignments

* **Hanging gripper** (**left gripper** in Config L, **right gripper** in Config M and R). Takes each part out of the
  tray by its hook and hangs it in its notch, lower spindle first, inner notch first.
* **Left gripper.** Lifts the lock pin for the turn. Frees and sets the cart brake. Holds the left part of the push
  bar in Step 4.
* **Right gripper.** Turns the rack a quarter turn by its turn handle. Puts right any part found touching in Step 3.
  Holds the right part of the push bar in Step 4.
* Nothing is handed between grippers.

## Vocabulary

* **Hanging gripper:** the gripper on the parts tray's side: the **left gripper** in Config L, the **right gripper** in
  Config M and R.
* **Shank / curl:** the straight part of the wire hook just above the part, and the curled top of the hook that sits in
  a notch. A part is always held by its **shank**.
* **Notch:** one of the three cuts along the top of a spindle. Each notch takes one hook.
* **Inner / outer notch:** the notch nearest the frame / nearest the tip. The middle notch is between them.
* **Hung:** the curl of the hook sits down in its notch, the part hangs straight below the spindle with its flat face
  across the spindle, and it stays put when the gripper opens.
* **With spacing:** one part in each notch, every notch filled, no notch holding two.
* **Quarter turn:** the rack turns until its spindle tips, which pointed at the base, point to the right at the booth,
  and the lock pin drops into its hole with a click.
* **Touching:** a part is in contact with another part, the frame, the other spindle's hooks, the cart, or the booth.
* **Clear gap:** light shows between a part and everything beside it, all the way down its side, with the part hanging
  still.
* **Along the row:** looking from the front, down the length of a turned spindle, so every gap on it is in view.
* **Clear of the rack:** the arm is drawn back so no part of it is over the cart, beside a spindle, or near a hung part.

## Steps

Run Steps 1 to 4 in order, and end the episode with Step 5. The four steps are the four actions of the task, in the
task's own order: **hook the parts on the spindles with spacing, rotate the rack, verify none touching, stage the cart to
the booth.** Only Step 1 depends on the config. Every other step is the same in all three.

### Step 1: Hook the parts on the rack spindles with spacing

**Goal:** all six parts are **hung**, one in each notch: the lower spindle full first, then the upper spindle.

* **IF Config L:** the **left gripper** is the hanging gripper. Draw the **right gripper** clear of the rack.
* **IF Config M or Config R:** the **right gripper** is the hanging gripper. Draw the **left gripper** clear of the rack.
* Then, in all three: hang the **lower spindle** first, inner notch, middle notch, outer notch. Then hang the **upper
  spindle** the same way. Each part goes on the notch nearest the frame that is still empty, so the gripper never
  reaches past a hung part.
* With the **hanging gripper**, close on the **shank** of the hook of the part nearest the front of the tray, and lift
  the part straight up out of the tray until it hangs clear.
* With the **hanging gripper**, carry the part level to above its notch, the curl a little above the spindle, the part's
  flat face across the spindle.
* With the **hanging gripper**, bring the curl straight down over the spindle until it sits in the notch.
* With the **hanging gripper**, hold still for about half a second so the part stops swinging, then open and draw
  straight up and back.
* With the **hanging gripper**, do not hook the curl over the tip and slide it along the spindle, and do not push a hung
  part along the spindle.
* Repeat for the next part until all six are hung, then draw the **hanging gripper** clear of the rack.

**Check:** after each one, the part is **hung** in its own notch and hangs a clear gap from the part beside it. If the
curl sits between notches or on the tip, close on the shank with the **hanging gripper**, lift the curl just off the
spindle, and set it down in its notch. If two hooks sit in one notch, lift the outer one off and hang it in the next
empty notch.

**Expected state:** three parts hang on the lower spindle and three on the upper, one in each notch. The tray is empty.
The rack still points at the base and the cart is braked at the load mark.

### Step 2: Rotate the rack

**Goal:** the rack has turned a **quarter turn** and is locked, its spindle tips pointing at the booth, the parts hanging
still.

* With the **left gripper**, close on the knob of the **lock pin** and lift it straight up until the turntable is free.
* With the **right gripper**, close on the **turn handle** and push it slowly round toward the back, so the spindle tips
  swing to the right.
* With the **left gripper**, once the turntable has started to turn, let the lock pin down so it rides on the turntable
  edge, then open and draw the **left gripper** clear of the rack.
* With the **right gripper**, keep turning slowly and steadily until the lock pin drops into its hole with a click. Do not
  turn past it and do not turn back.
* With the **right gripper**, open and draw back, and wait for the parts to stop swinging.
* With either gripper, turn only by the turn handle. Do not turn the rack by the frame, a spindle, or a part.

**Check:** the lock pin is down in its hole, the spindle tips point straight at the booth, and the turntable does not move.
If the pin has not dropped, push the turn handle on with the **right gripper**, a little at a time, until it clicks.

**Expected state:** the rack is locked a quarter turn round. From the front you look along both rows. The cart is still
braked at the load mark.

### Step 3: Verify none touching

**Goal:** every part is looked at along its row and hangs with a **clear gap** all round.

* Wait until every part hangs still.
* Look **along the lower row**, from the frame out to the tip: between the frame and the inner part, and between each two
  parts, there is a clear gap. Each hook is still in its notch.
* Look **along the upper row** the same way.
* Look **between the rows**: no part on the upper spindle touches a hook or part on the lower spindle.
* Look at the ends: no part touches the cart deck or the turntable.
* If a part is **touching**, with the **right gripper**, close on the shank of that part's hook and hold it still for about
  half a second, then open and draw back. If it still touches, lift the curl just off the spindle with the **right
  gripper** and set it back down square in its notch.
* With the **right gripper**, touch no other hung part while putting one right.
* Hold the **left gripper** open and clear of the rack for the whole of this step.

**Check:** every gap on both rows and between them is clear, and every part hangs still in its notch. If one was put right,
look along both rows once more before Step 4.

**Expected state:** six parts hang still with a clear gap all round. Both grippers are clear of the rack.

### Step 4: Stage the cart to the booth

**Goal:** the cart has rolled along the track to the booth stop and is braked there, with no part touching.

* With the **left gripper**, close on the **brake lever** and lift it up to free the cart.
* With the **left gripper**, close on the push bar at its left part. With the **right gripper**, close on the push bar at
  its right part, right of the left gripper.
* With **both grippers**, push the cart slowly and steadily to the right along the track, in one move, without jerking or
  stopping.
* With **both grippers**, slow down as the cart nears the booth and let it come gently against the **booth stop**. Do not
  bump it into the stop.
* With **both grippers**, keep the arms outside the booth mouth. Only the cart goes in.
* With the **right gripper**, open and draw back. With the **left gripper**, press the brake lever down to brake the cart,
  then open and draw back.
* Wait for the parts to stop swinging.

**Check:** the cart's right end touches the booth stop, the brake is down, and the cart does not roll. Look along both rows
once more: no part is touching. If a part is touching, put it right with the **right gripper** from the front as in
Step 3, without going into the booth.

**Expected state:** the cart is braked at the booth stop, the rack is locked a quarter turn round inside the booth mouth,
and the six parts hang still with clear gaps.

### Step 5: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the rack staged.

* Look once along both rows: six parts hung one to a notch, none touching, the rack locked, and the cart braked at the
  booth stop.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the rack is staged at the booth, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Free the brake and roll the cart back along the track until its left end is on the load mark, then brake it.
2. Lift the lock pin and turn the rack back a quarter turn until both spindles point at the base and the pin clicks.
3. Take each part off its spindle by its shank and lay it flat in the parts tray, hook up, none on top of another.
4. Move the parts tray to the spot on the lower deck for the next episode's config.
5. Check every hook is straight, closed round its hang hole, and not caught in another. Replace a bent hook.
6. Check the notches are clean and the turntable turns freely and locks at both holes.
7. Check the cart rolls freely along the track and the brake holds.
8. Pick up anything that landed on the deck, the track, or the floor.
9. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the
reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule
was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the track shifts in frame, the cart or booth changes angle or size in frame without the cart being pushed,
  or the base rolls, creeps, or turns at any point after recording starts.
* **SOP rule broken:** Steps 1 to 5, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Reached into the booth**

* **Visible cue:** a gripper, wrist, or forearm goes past the booth mouth or touches a booth wall, the roof, or the booth stop.
* **SOP rule broken:** Steps 3 and 4, only the cart goes into the booth, and parts are put right from the front.
* **Coaching note:** the booth is wet paint. The cart goes in, the arm stays out.

**Violation: Leaned on or moved the rack or cart out of turn**

* **Visible cue:** a gripper, wrist, or forearm rests on the cart, the frame, or a spindle; the cart rolls in Steps 1 to 3; or
  the rack turns in Step 1, 3, or 4.
* **SOP rule broken:** Steps 1 to 4, the rack turns only in Step 2 and the cart moves only in Step 4.
* **Coaching note:** the arm holds itself up. The rack and the cart move only when the step says so.

**Violation: Part held wrong**

* **Visible cue:** the hanging gripper closes on the part's face, its edge, or the curl instead of the shank; a hook is bent in
  the gripper; or a part is dragged across the tray or the deck instead of lifted.
* **SOP rule broken:** Step 1, take each part by the shank of its hook and lift it straight up out of the tray.
* **Coaching note:** hold the shank. The curl is what goes in the notch, and the face is what gets painted.

**Violation: Hook not in its notch**

* **Visible cue:** a curl sits between notches, on the tip, or half out of a notch; a part hangs crooked; or a part falls off
  the spindle when the gripper opens.
* **SOP rule broken:** Step 1, bring the curl straight down over the spindle until it sits in its notch.
* **Coaching note:** straight down into the notch, hold half a second, then open.

**Violation: Spacing wrong**

* **Visible cue:** two hooks share a notch, a notch is left empty at the end of Step 1, or a part is hung with its flat face
  along the spindle instead of across it.
* **SOP rule broken:** Step 1, one part in each notch, every notch filled, each face across the spindle.
* **Coaching note:** one notch, one part. The notches are the spacing.

**Violation: Part slid along the spindle**

* **Visible cue:** a curl is hooked over the tip and slid along to its notch, or a hung part is pushed along the spindle to make
  room.
* **SOP rule broken:** Step 1, each part goes straight down into its own notch from above, and a hung part is not pushed.
* **Coaching note:** down, not along. Sliding knocks the parts already hung.

**Violation: Hung out of order**

* **Visible cue:** the upper spindle gets a part before the lower spindle is full, or an outer or middle notch is filled before the
  notches nearer the frame on that spindle, so the gripper reaches past or under a hung part.
* **SOP rule broken:** Step 1, lower spindle first, then upper, and on each spindle the inner notch first, out to the tip.
* **Coaching note:** fill from the frame out and from the bottom up, and nothing is ever in the way.

**Violation: Lock pin or turn done wrong**

* **Visible cue:** the rack is turned while the lock pin is still down; the pin is held up for the whole turn so it does not drop
  in; the rack is turned by the frame, a spindle, or a part instead of the turn handle; or the lock pin is lifted by the right
  gripper.
* **SOP rule broken:** Step 2, the **left gripper** lifts the pin and lets it ride, and the **right gripper** turns by the handle.
* **Coaching note:** pin up, start the turn, pin down, and let it find the hole.

**Violation: Rack turned the wrong way or the wrong amount**

* **Visible cue:** the spindle tips swing to the left; the rack stops short of the click or goes past it; or the rack is turned
  back after the click.
* **SOP rule broken:** Step 2, turn a quarter turn, tips to the right, until the pin clicks, and stop.
* **Coaching note:** tips toward the booth, one quarter, one click.

**Violation: Turned or pushed too fast**

* **Visible cue:** the rack or the cart is turned or pushed so fast, or stopped so hard, that the parts swing into each other or
  the frame; or the cart is bumped into the booth stop.
* **SOP rule broken:** Steps 2 and 4, turn and push slowly and steadily, and let the cart come gently against the stop.
* **Coaching note:** the turn and the push are slow on purpose. Swinging parts hit each other.

**Violation: Rows not looked along**

* **Visible cue:** Step 3 goes by without a look along both rows and between them; the look starts while the parts are still
  swinging; or the check after the cart reaches the booth is skipped.
* **SOP rule broken:** Steps 3 and 4, look along the lower row, the upper row, between the rows, and at the ends, with the parts
  still.
* **Coaching note:** still parts first, then look along every row. A touch you did not look for is a spray mark.

**Violation: Touching part left or put right wrong**

* **Visible cue:** the episode goes on with a part touching; a part is put right by the left gripper, by its face, or by pushing
  it along the spindle; or putting one part right knocks another.
* **SOP rule broken:** Step 3, the **right gripper** holds the touching part still by its shank, or re-seats its curl in its
  notch, touching nothing else.
* **Coaching note:** hold it still first. Most touches stop when the swing stops.

**Violation: Cart brake not freed or not set**

* **Visible cue:** the cart is pushed with the brake on, the brake is freed before Step 4, or the cart is left at the booth stop
  with the brake up.
* **SOP rule broken:** Step 4, the **left gripper** frees the brake just before the push and sets it once the cart is at the
  stop.
* **Coaching note:** brake up, push, brake down. A free cart rolls off the mark.

**Violation: Cart not staged at the booth stop**

* **Visible cue:** the cart stops short of the booth stop, is pushed by the rack, a spindle, or the cart side instead of the push
  bar, is pulled instead of pushed, or its wheels come out of the track.
* **SOP rule broken:** Step 4, both grippers push the cart by the push bar along the track until it rests against the booth stop.
* **Coaching note:** push bar only, one steady push, all the way to the stop.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the cart is not set up in: the wrong gripper hangs the parts, a gripper reaches for a
  tray spot that is empty, both grippers hang parts, or the tray is moved before or during the episode.
* **SOP rule broken:** Step 1, look at the cart, find the parts tray, and follow the IF line that matches the config the episode
  is set up in.
* **Coaching note:** look at the tray before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** the rack is turned before all six parts are hung; the cart brake is touched before the rows are looked along;
  the cart is pushed before the rack is locked; or a part is taken out of the tray after the turn.
* **SOP rule broken:** Steps 1 to 4, hook the parts with spacing, rotate the rack, verify none touching, then stage the cart.
* **Coaching note:** the order is the task. Each step leaves the rack ready for the next one.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two parts together, or the gripper that is not hanging comes near the rack in Step 1.
* **SOP rule broken:** Step 1, one part at a time, and the other gripper is clear of the rack.
* **Coaching note:** one part, one trip. Two hooks together tangle.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a curl off
  its notch, two hooks in one notch, a lock pin not in its hole, a part touching, or the cart short of the stop.
* **SOP rule broken:** Steps 1 to 4, run each check and correct what it finds by the retry written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked off**

* **Visible cue:** a part is dropped in the tray, on the deck, or on the floor; a hung part is knocked off its spindle; or a
  hook comes off its part.
* **SOP rule broken:** Steps 1 to 4, nothing is dropped or knocked out of its place, and every gripper comes out the way it went
  in.
* **Coaching note:** check the path before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the gripper that is not the hanging gripper touches a part or the tray in Step 1; the **right gripper** works
  the lock pin or the brake lever; the **left gripper** works the turn handle or puts a part right; one gripper pushes the cart
  alone; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 4, the hanging gripper hangs, the **left gripper** does the pin and the brake, the **right
  gripper** does the turn and the fixes, both push, and the arms never cross.
* **Coaching note:** each gripper has its own part of the task. Look at the config, then at the step.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a part off its notch, a part touching, the rack not locked, the cart short of the booth
  stop or unbraked, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 5, look once along both rows, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for
coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read the notches, the gaps along a row, the load mark, or the booth stop**, so which notch a hook sits in,
  whether a part touches, or where the cart stands cannot be judged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Faulty rack or cart:** a lock pin that sticks or will not drop, a turntable that binds, a cart that sticks on the track, or a
  cart brake that will not hold.
* **Faulty part:** a hook that arrives bent or open, or a part that comes off its hook when lifted gently by the shank.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a notch, the tray, the lock
  pin, the turn handle, the brake lever, or the push bar at the booth stop cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Lift one part out of the tray by its shank
2. Hang one part in its notch
3. Lift the lock pin
4. Turn the rack a quarter turn by its handle
5. Look along one row
6. Put one touching part right
7. Free the cart brake
8. Push the cart to the booth stop
9. Set the cart brake
10. Return both arms home and end the episode
