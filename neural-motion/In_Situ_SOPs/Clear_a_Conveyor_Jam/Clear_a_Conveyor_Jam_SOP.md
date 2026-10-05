# Clear a Conveyor Jam SOP (1x Episode: one jam, in situ)

One episode clears one jam on a conveyor line, at the conveyor where the jam happened. The base is **passive**: it has no drive of
its own, so it is pushed by hand to the front of the conveyor and locked there, and nothing is carried away to a table. Everything the
episode touches is already at the conveyor when recording starts: the running belt with its jammed and waiting cartons, the mock HMI
panel, and the fault log card with its marker.

The episode runs these five actions in this order and no other: **stop the line at the mock HMI, clear the wedged cartons, square the
remaining flow, restart, log the fault.** No carton is touched until the belt has stopped, and nothing is over the belt when it starts
again.

The conveyor is worked **as found**. When recording starts, the belt is **running** and the HMI's amber **JAM** lamp is flashing. At the
**jam point** in the middle of the conveyor, the **lead carton** has turned across the lane and wedged between the guide rails, and the
**riding carton** has run into it and ridden up with one corner on its back edge. The belt slides on under them. Upstream, two more
cartons, the **waiting cartons**, sit crooked on the stopped flow. The episode ends with the line running again, all four cartons carried
away square and spaced, and the four lines of the fault log ticked.

**This is an in-situ task, and three things follow from that.** First, **the belt is live**: nothing touches the belt, a carton on it, or
a guide rail while the belt is moving, before the STOP or after the START. Second, the **conveyor and the HMI are never leaned on and
never pushed**: no gripper, wrist, or forearm rests on the frame, a guide rail, or the HMI. Third, **every carton stays on the lane**: a
carton is freed, turned, and set back down in the lane, never lifted off the conveyor, set on a rail or the frame, or carried away.

The conveyor is set up in one of two ways. Only the **flow direction** changes. The jam point, the HMI, and the log card are in the same
place in both, and the jam is always built the same way, facing the flow.

* **Config L:** the belt runs **left to right**. Upstream is on the left and downstream on the right.
* **Config R:** the belt runs **right to left**. Upstream is on the right and downstream on the left.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says so on an **IF**
line. Look at the arrow on the conveyor frame and follow the line that matches.

What stays constant across all sessions:

* **Downstream rule:** the gripper at the downstream end presses every HMI button, frees the lead carton, and ticks the log. It is called
  the **downstream gripper**: the **right gripper** in Config L and the **left gripper** in Config R.
* **Upstream rule:** the gripper at the upstream end frees the riding carton and squares the waiting cartons. It is called the **upstream
  gripper**: the **left gripper** in Config L and the **right gripper** in Config R.
* **Live-belt rule:** before the STOP and after the START, both grippers stay off the belt, the cartons, and the rails.

Nothing is ever handed over. **The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm
reaches over, under, around, or past the other. Nothing is moved two at a time: one gripper holds or pushes one carton, and the other
gripper is empty and clear of the belt.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or repositioned once
recording starts. It is parked once, before recording, and does not move again until the episode is over.

1. Push the base by hand up to the front of the conveyor and stop it **square to it**, so the guide rails run straight across the frame of
   the camera.
2. Stop it **centered on the jam point**, so the middle of the base is in line with the jam mark on the conveyor frame.
3. Stop it **close enough** that both grippers reach the far guide rail without either arm extending, and **far enough** that neither arm,
   wrist, nor any part of the base touches the conveyor frame or the HMI while both arms work.
4. Check the **left side**: the **left gripper** reaches the lane from the jam point out to the left end of the reach zone, the HMI buttons,
   and the log card, all without extending.
5. Check the **right side**: the **right gripper** reaches the lane from the jam point out to the right end of the reach zone, the HMI
   buttons, and the log card, all without extending.
6. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
7. If any of lines 1 to 5 fails, push the base to a new park by hand and start again at line 1. Do not work a conveyor the arms cannot reach
   comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the conveyor hard enough to shift it, nothing
touches it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the jam point and its frame includes the whole reach zone of the lane, both guide rails, the four
   cartons, the flow arrow, the HMI with its lamps, and the log card.
3. The camera sees whether the belt is moving, and which HMI lamp is lit, at every moment.
4. The camera reads the **carton labels**, so which carton is which, and the order they leave in, is readable.
5. The camera reads the **log card** well enough to see which boxes are ticked.
6. Both arms are at home with grippers open.
7. Each arm reaches its half of the reach zone, the HMI, and the log card without extending to a joint limit.
8. Both grippers come down onto a carton and lift it clear of the rails without either wrist touching a rail.
9. The two arms do not collide, and neither arm passes in front of the other.
10. If a place cannot be reached, re-park the base by the Base positioning steps until lines 7 to 9 hold.

### Materials checklist

1. The **conveyor** is a short powered belt section fixed to the floor at about waist height, running across in front of the base. It is not
   moved, not leaned on, and not pushed at any point. Nothing is above it.
2. A **low guide rail** runs along each side of the belt, lower than half a carton's height. The space between them is the **lane**. It is a
   little wider than a carton is wide, and narrower than a carton is long.
3. A **flow arrow** on the front of the frame shows which way the belt runs: left to right in **Config L**, right to left in **Config R**.
4. A **jam mark** on the front of the frame, in the middle, marks the **jam point**. The part of the lane both arms can reach, a little more
   than two cartons each side of the jam point, is the **reach zone**.
5. There are **four cartons**, all the same size, light enough for one gripper to hold by its sides, each about twice as long as it is wide,
   each with a large-print **carton label** on top: **A**, **B**, **C**, **D**.
6. At the start (the **jam as found**):
   * **A**, the **lead carton**, is turned across the lane at the jam point, its two ends wedged against the two guide rails;
   * **B**, the **riding carton**, is right behind A on the upstream side, at a slant, with one front corner riding up on A's back edge;
   * **C** and **D**, the **waiting cartons**, are further upstream in that order, C nearer the jam, each crooked in the lane, touching each
     other or a rail.
7. The **belt** is running under the jammed cartons when recording starts. It does not move them.
8. The **mock HMI** is a panel fixed on the front of the conveyor frame, just below the belt, in the middle, facing the base. It has:
   * a red **STOP** button, a yellow **RESET** button, and a green **START** button;
   * three lamps: amber **JAM**, red **STOPPED**, green **RUNNING**.
9. The HMI works like this (**unvalidated**: the mock must behave this way). At the start, JAM flashes and the belt runs. STOP stops the belt and
   lights STOPPED, and JAM keeps flashing. RESET, with the belt stopped, puts JAM out. START, with JAM out, starts the belt and lights RUNNING.
   START does nothing while JAM is still lit.
10. The **fault log card** sits in a fixed **log holder** on the frame beside the HMI, facing out, with the **marker** standing point down in a
    clip beside it. The card has four lines, each with a **tick box** at its right end: **LINE STOPPED AT HMI**, **JAM CLEARED**, **FLOW
    SQUARED**, **LINE RESTARTED**. The card is fresh: no box is ticked.
11. There is a **catch tray** at each end of the section, out of reach. The belt carries cartons past the downstream end of the reach zone
    into the catch tray at that end.
12. Nothing else stands on the conveyor within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the flow arrow and the jam mark. You judge every other place by eye against the conveyor itself.

* **Conveyor:** the fixed belt section the base is parked at. Never moved, never leaned on, never pushed.
* **Jam point:** the lane at the jam mark, in the middle.
* **Upstream half:** the reach zone on the side the cartons come from. **Upstream gripper only.**
* **Downstream half:** the reach zone on the side the cartons go to, including the jam point itself. **Downstream gripper only.**
* **HMI and log card:** on the front of the frame in the middle, below the belt. **Downstream gripper only.**
* **Catch trays:** one past each end, out of reach. Cartons go to the one downstream, and a carton that reaches it is gone.

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **upstream gripper** works the upstream half of the lane. The **downstream gripper** works the jam point, the downstream half, the HMI, and
  the log.
* Neither arm reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds or pushes one carton, or holds the marker, and while it does, the other gripper is empty and
  drawn **clear of the belt**.

### Arm assignments

* **Downstream gripper** (**right gripper** in Config L, **left gripper** in Config R). Presses STOP, frees the lead carton A and sets it square,
  presses RESET and START, and ticks the log.
* **Upstream gripper** (**left gripper** in Config L, **right gripper** in Config R). Frees the riding carton B and sets it square, and squares and
  spaces the waiting cartons C and D.
* Nothing is handed over.

## Vocabulary

* **Jam:** cartons stuck on a running belt so they no longer move with it.
* **Mock HMI:** the button panel that runs the conveyor. HMI means the panel where a person talks to the machine.
* **Upstream / downstream:** the side the cartons come from, and the side they go to. The flow arrow shows which is which.
* **Lead carton (A):** the carton turned across the lane and wedged between the rails.
* **Riding carton (B):** the carton behind A, riding up on its back edge.
* **Waiting cartons (C, D):** the cartons further upstream, crooked but not wedged.
* **Live belt:** the belt from the start of recording until STOP, and again from START on. Nothing touches it, a carton on it, or a rail.
* **Press:** the closed gripper comes straight at a button, pushes it once until it clicks, and draws straight back.
* **Free:** lift a stuck carton straight up by its sides until its bottom is above the rails, without pulling it sideways, twisting it
  against a rail, or pushing it through the jam.
* **Square carton:** the carton lies flat on the belt, its length along the lane, in the middle of the lane, touching neither rail.
* **Gap:** the space between one carton and the next along the lane: one hand wide, about the width of a closed gripper.
* **Squared flow:** A, B, C, D in that order from downstream to upstream, each one square, with one gap between each and the next.
* **Nudge:** the closed gripper presses flat on the side of a carton on the stopped belt and slides it a short way, keeping it flat on the belt.
* **Clear of the belt:** the arm is drawn up and back so that no part of it is over the belt, a carton, or a rail.
* **Tick:** one mark with the marker inside a tick box: a short stroke down and to the right, then a longer stroke up and to the right, without
  lifting.

## Steps

Run Steps 1 to 5 in order, and end the episode with Step 6. The config decides which gripper is upstream and which is downstream. Nothing else
changes between configs.

### Step 1: Stop the line at the HMI

**Goal:** the belt has stopped and the STOPPED lamp is lit.

* **IF Config L:** the **right gripper** is the downstream gripper. **IF Config R:** the **left gripper** is the downstream gripper.
* Look at the conveyor: the belt is running and JAM is flashing. Keep both grippers off the belt, the cartons, and the rails.
* With the **downstream gripper**, closed, **press** the red **STOP** button once, then draw back.
* Watch the belt until it has stopped.
* With the upstream gripper, stay open and **clear of the belt**.

**Check:** the belt is still, STOPPED is lit, and JAM is still flashing. If the belt is still moving, press STOP once more with the **downstream
gripper**.

### Step 2: Clear the wedged cartons

**Goal:** A and B are freed and both lie **square** in the lane, A at the jam point and B one **gap** behind it.

#### 2.1 Free the riding carton

* **IF Config L:** the **left gripper** is the upstream gripper. **IF Config R:** the **right gripper** is the upstream gripper.
* With the **upstream gripper**, come down from above and close on the two long sides of **B**, near its middle.
* With the **upstream gripper**, lift B straight up until its corner is clear of A's back edge, then draw it straight back upstream, level, a
  little more than one gap.
* With the **upstream gripper**, turn it square to the lane, set it down flat in the middle of the lane, then open and lift straight up and
  **clear of the belt**.
* With the downstream gripper, stay open and **clear of the belt**.

**Check:** B lies **square**, flat on the belt, with space behind A, and A has not moved.

#### 2.2 Free the lead carton

* With the **downstream gripper**, come down from above and close on the two long sides of **A**, at its middle.
* With the **downstream gripper**, **free** A: lift it straight up until its bottom is above the rails.
* With the **downstream gripper**, turn it a quarter turn in the air, so its length runs along the lane.
* With the **downstream gripper**, set it down flat in the middle of the lane at the jam point, then open and lift straight up and **clear of the
  belt**.
* With the upstream gripper, stay open and **clear of the belt**.

**Check:** A lies **square** at the jam point, touching neither rail, and there is at least one gap between A and B. If B sits closer than one
gap, **nudge** it back upstream with the **upstream gripper**. If the gap is bigger, nudge B forward to one gap.

**Expected state:** the jam is cleared. A and B are square in the lane, one gap apart. C and D are still as found.

### Step 3: Square the remaining flow

**Goal:** C and D are **square** in the lane, in order behind B, each one gap from the carton ahead, so the flow is **squared**.

* With the **upstream gripper**, closed, **nudge** **C** until it lies square in the middle of the lane, one gap behind B.
* With the **upstream gripper**, closed, **nudge** **D** until it lies square in the middle of the lane, one gap behind C.
* With the **upstream gripper**, if a carton will not turn square by nudging, close on its sides, lift it just clear of the belt, turn it square,
  and set it down in its place.
* With the **upstream gripper**, draw up and **clear of the belt**.
* With the downstream gripper, stay open and **clear of the belt**.

**Check:** the flow is **squared**: A, B, C, D in that order, each square, one gap apart, none touching a rail. If a gap is wrong or a carton
touches a rail, nudge it with the gripper of its half.

### Step 4: Restart the line

**Goal:** the belt is running, RUNNING is lit, and all four cartons have gone down the lane square without catching.

* Check both grippers are **clear of the belt**.
* With the **downstream gripper**, closed, **press** the yellow **RESET** button once and draw back. JAM goes out.
* With the **downstream gripper**, closed, **press** the green **START** button once and draw back.
* With **both grippers**, hold still, clear of the belt, and watch every carton pass the jam point and run out to the downstream catch tray.
* **IF a carton catches on a rail or turns across the lane:** with the **downstream gripper**, press **STOP** at once, then go back to Step 2 for
  that carton.

**Check:** the belt is running, RUNNING is lit, JAM is out, and the reach zone is empty.

### Step 5: Log the fault

**Goal:** all four lines of the fault log carry **one tick** each, and the marker is back in its clip.

* With the **downstream gripper**, close on the **barrel** of the marker, not on its point, and lift it straight up out of its clip.
* With the **downstream gripper**, bring the marker point level to the first line's **tick box**, draw one **tick**, and draw the point straight
  back off the card.
* With the **downstream gripper**, tick the second, third, and fourth lines the same way, top to bottom. Press only hard enough to leave a mark.
* With the **downstream gripper**, stand the marker back in its clip, point down, then open and draw back.
* With the upstream gripper, stay open and **clear of the belt** for the whole of this step.

**Check:** each of the four lines carries **one tick**, inside its box, and the marker stands in its clip point down. If a tick has run outside its
box, leave it. Do not draw over it and do not draw a second tick in the same box.

### Step 6: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the line running.

* Look once across the conveyor: the belt is running with RUNNING lit, the reach zone is empty, and the log card has four ticks.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the jam is cleared and logged, the line is running, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Stop the belt at the HMI.
2. Take the four cartons out of the downstream catch tray.
3. Set the flow arrow for the next episode's config.
4. Build the jam as found, facing the flow: A across the lane wedged at the jam point, B at a slant riding on A's back edge, C and D crooked
   upstream.
5. Take the ticked log card out of its holder and put in a fresh one. Check the marker still marks.
6. Start the belt and set JAM flashing, so the belt runs under the jammed cartons without moving them.
7. Pick up anything that landed on the frame, a rail, or the floor.
8. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the reviewer sees. The
coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the conveyor shifts in frame, the rails change angle or size in frame, or the base rolls, creeps, or turns at any point after
  recording starts.
* **SOP rule broken:** Steps 1 to 6, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Touched the live belt**

* **Visible cue:** a gripper touches the belt, a carton, or a rail while the belt is moving: before the STOP has taken effect, or after START.
* **SOP rule broken:** Steps 1 and 4, nothing touches the belt, a carton on it, or a rail while the belt runs.
* **Coaching note:** stop first, then touch. A running belt does not care what it pulls in.

**Violation: Leaned on or pushed the conveyor or HMI**

* **Visible cue:** a gripper, wrist, or forearm rests on the frame, a rail, or the HMI panel, or the conveyor shakes.
* **SOP rule broken:** Steps 1 to 5, the conveyor and the HMI carry no weight from the arms.
* **Coaching note:** the arm holds itself up. Press only as hard as the button needs.

**Violation: STOP done wrong**

* **Visible cue:** a button other than STOP is pressed first; STOP is held down, pressed with an open gripper, or pressed again and again; or the
  arms move on before the belt has stopped.
* **SOP rule broken:** Step 1, press STOP once with the closed downstream gripper and watch the belt stop.
* **Coaching note:** one press, then watch it stop. The stop is only real when the belt is still.

**Violation: Cleared in the wrong order**

* **Visible cue:** A is freed while B is still riding on its back edge, or C or D is touched before A and B are both square.
* **SOP rule broken:** Step 2, free the riding carton first, then the lead carton, then square the rest.
* **Coaching note:** top of the pile first. Pull A out from under B and B falls.

**Violation: Wedged carton forced**

* **Visible cue:** a stuck carton is pulled sideways, twisted against a rail, dragged along a rail, pushed downstream through the jam, or levered on a
  rail, or a rail flexes.
* **SOP rule broken:** Step 2.2, free the carton by lifting it straight up by its sides until it is above the rails.
* **Coaching note:** straight up, not through. The rails are why it is stuck, so lift it clear of them.

**Violation: Carton held wrong**

* **Visible cue:** a carton is held by one corner, one end, its top flaps, or its label, or it swings or tilts in the gripper.
* **SOP rule broken:** Steps 2.1, 2.2, and 3, close on the two long sides of the carton near its middle.
* **Coaching note:** long sides, middle, level.

**Violation: Carton not set square**

* **Visible cue:** A is left across the lane or at a slant; a carton is set down touching a rail, off the middle of the lane, or on its side or end.
* **SOP rule broken:** Steps 2.1 and 2.2, set each freed carton flat, its length along the lane, in the middle, touching neither rail.
* **Coaching note:** length along the lane, middle, flat. A crooked carton is the next jam.

**Violation: Carton taken off the lane**

* **Visible cue:** a carton is set on a rail, the frame, the HMI, or the floor, lifted away from the conveyor, or set down outside the reach zone.
* **SOP rule broken:** Steps 2 and 3, every carton is freed, turned, and set back in the lane.
* **Coaching note:** the cartons stay in the flow. Clearing a jam is not removing cartons.

**Violation: Flow not squared**

* **Visible cue:** C or D is left crooked, touching a rail, or touching the carton ahead when START is pressed.
* **SOP rule broken:** Step 3, nudge C and then D square, each one gap behind the carton ahead.
* **Coaching note:** square the whole flow before it moves, not just the jam.

**Violation: Gaps wrong**

* **Visible cue:** two cartons touch, a gap is much wider than a hand, or the gaps are uneven when START is pressed.
* **SOP rule broken:** Steps 2.2 and 3, one gap, one hand wide, between each carton and the next.
* **Coaching note:** one hand between each. Touching cartons climb each other.

**Violation: Cartons out of order**

* **Visible cue:** the cartons leave in any order other than A, B, C, D, or a carton is moved past another.
* **SOP rule broken:** Steps 2 and 3, the cartons keep their order: A leading, then B, C, D.
* **Coaching note:** the line counts on the order. Nobody jumps the queue.

**Violation: Restart done wrong**

* **Visible cue:** START is pressed before RESET, before the flow is squared, or while a gripper is over the belt; or RESET or START is held or pressed
  more than once.
* **SOP rule broken:** Step 4, with both grippers clear, press RESET once, then START once.
* **Coaching note:** clear, reset, start. Hands out before the belt moves.

**Violation: Re-jam ignored**

* **Visible cue:** after START a carton catches or turns across the lane and the belt is left running, or a gripper reaches for it without pressing STOP
  first.
* **SOP rule broken:** Step 4, watch every carton out, and on a new jam press STOP at once and go back to Step 2.
* **Coaching note:** watch them all the way out. A new jam gets the same stop as the first.

**Violation: Log filled in wrong**

* **Visible cue:** a line is skipped or ticked twice; lines are ticked out of top-to-bottom order; the log is ticked before the restart; a tick is drawn
  over; or any other mark is made on the card.
* **SOP rule broken:** Step 5, after the line is running, tick each of the four lines once, top to bottom, inside its box.
* **Coaching note:** the log is the record. The work first, then one tick per line.

**Violation: Marker handled wrong**

* **Visible cue:** the marker is held by its point, pressed hard enough to bend its tip or push the card, laid on the frame, dropped, or not stood back in its
  clip point down.
* **SOP rule broken:** Step 5, hold the marker by its barrel and stand it back in its clip, point down.
* **Coaching note:** barrel in the gripper, light on the card, back in the clip.

**Violation: Config misaligned**

* **Visible cue:** the arms work the flow the wrong way round: the upstream gripper presses a button or frees A, the downstream gripper frees B or squares C
  and D, or cartons are spaced out toward the downstream side.
* **SOP rule broken:** Steps 1 to 3, look at the flow arrow and follow the IF line that matches the config the episode is set up in.
* **Coaching note:** read the arrow before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** a carton is touched before STOP; C or D is squared before A and B are free; START is pressed before the flow is squared; or the log is
  ticked before the restart.
* **SOP rule broken:** Steps 1 to 5, stop, clear, square, restart, then log.
* **Coaching note:** the order is the task, and the first step keeps you safe.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper moves two cartons at once; both grippers move cartons at the same time; or a gripper holds a carton or the marker while the
  other works instead of being clear of the belt.
* **SOP rule broken:** Steps 2 to 5, one gripper moves one thing, and the other is empty and clear of the belt.
* **Coaching note:** one carton, one move.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: the belt still moving after STOP, a
  carton touching a rail, a wrong gap, or JAM still lit when START is pressed.
* **SOP rule broken:** Steps 1 to 5, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a carton or the marker is dropped on the belt, a rail, the frame, or the floor; a carton is knocked onto its side or off the belt; or a
  carton is knocked out of its place in the flow.
* **SOP rule broken:** Steps 2 to 5, nothing is dropped or knocked out of its place, and every gripper lifts clear the way it came in.
* **Coaching note:** check the path and the landing place before the arm moves.

**Violation: Wrong arm used**

* **Visible cue:** the upstream gripper works the downstream half, the HMI, or the log; the downstream gripper works the upstream half; or either arm passes
  in front of the other.
* **SOP rule broken:** Steps 1 to 5, the downstream gripper runs the HMI, A, and the log, the upstream gripper runs B, C, and D, and the arms never cross.
* **Coaching note:** downstream runs the line, upstream runs the flow.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with the belt stopped, JAM lit, a carton still in the reach zone, a log line not ticked, the marker out of its clip, an arm
  short of home, or a gripper not fully open.
* **SOP rule broken:** Step 6, look once across the conveyor, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot see whether the belt is moving, which lamp is lit, the carton labels, or the log card**, so the stop, the order, or the log cannot be judged.
* **HMI or conveyor fault:** STOP does not stop the belt, RESET does not put JAM out, START does not start the belt, or the belt moves on its own.
* **Jam not built as found:** a carton missing, the cartons in the wrong order, or A not actually wedged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a carton, the far rail, a button, or the log card cannot
  be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Press STOP at the HMI
2. Lift the riding carton off the lead carton
3. Free the lead carton straight up
4. Turn the lead carton along the lane and set it down
5. Nudge one waiting carton square
6. Press RESET
7. Press START
8. Watch the cartons clear the reach zone
9. Take the marker from its clip
10. Tick one log line
11. Stand the marker back in its clip
12. Return both arms home and end the episode
