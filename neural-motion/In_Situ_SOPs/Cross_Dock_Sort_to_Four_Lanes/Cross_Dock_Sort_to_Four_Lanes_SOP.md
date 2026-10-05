# Cross-Dock Sort to Four Lanes SOP (1x Episode: ten parcels, in situ)

One episode sorts ten inbound parcels onto four lane pallets and tallies each lane, at the cross-dock sort bench where the lanes live.
The base is **passive**: it has no drive of its own, so it is pushed by hand to the front of the bench and locked there, and nothing is
carried away to a table. Everything the episode touches is already at the bench when recording starts: the infeed cart with its ten
parcels, the four empty lane pallets, the scanner with its lane display, and the tally card with its marker.

The episode runs these four actions in this order and no other: **scan each parcel, route it to one of four lane pallets, stack it
squarely, tally the lane counts.** Each parcel is scanned before it moves toward a lane, because the scan is what names its lane. The
tally comes last, once all ten parcels are stacked.

The bench is worked **as found**. The **infeed cart** stands braked against one end of the bench with **ten parcels** standing on its top
deck in a row. The four **lane pallets** are empty. The episode ends with every parcel stacked squarely on the pallet of the lane the
scanner named, the infeed deck bare, and the tally card showing each lane's count.

**The scanner decides the lane.** A parcel is held up to the scanner, and the **lane display** shows **LANE 1**, **2**, **3**, or **4**.
That is the only thing that says where the parcel goes. How many parcels each lane gets changes from episode to episode, so each lane's count
is only known by counting its stack at the end.

**This is an in-situ task, and three things follow from that.** First, **the lanes are stacks that grow**: every parcel is set straight
down on top of the stack below, and nothing is ever pushed or slid across a stack. Second, the **bench, the pallets, and the cart are never
leaned on and never pushed**: no gripper, wrist, or forearm rests on the bench, a pallet, a stack, the scanner post, or the cart. Third,
**each parcel goes from the cart to its lane and nowhere else**: nothing is set down on the bench top, another lane, or the floor on the way.

The bench is set up in one of two ways. Only the **infeed cart** moves. The lanes, the scanner, and the tally card are in the same place in
both.

* **Config L:** the infeed cart stands against the **left end** of the bench.
* **Config R:** the infeed cart stands against the **right end** of the bench.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says so on an **IF**
line. Look at the bench and follow the line that matches. Which lane each parcel goes to also changes per episode, but it is not a config:
the scan shows it.

What stays constant across all sessions:

* **Lane-side rule:** the **left gripper** stacks **Lane 1** and **Lane 2** and the **right gripper** stacks **Lane 3** and **Lane 4**.
* **Cart-side rule:** the gripper on the cart's side takes every parcel off the cart, scans it, and fills in the tally. It is called the
  **cart gripper**: the **left gripper** in Config L and the **right gripper** in Config R.
* **Hand-over rule:** when a scanned parcel's lane is on the side away from the cart, the cart gripper **hands it over** to the other gripper
  at the **hand-over point**. No arm reaches across the bench.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches over, under, around, or past
the other. Nothing is moved two at a time: one gripper holds one parcel, and the other gripper is empty, taking a hand-over, or clear of the
lanes.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or repositioned once
recording starts. It is parked once, before recording, and does not move again until the episode is over.

1. Push the base by hand up to the front of the bench and stop it **square to it**, so the bench edge runs straight across the frame of the
   camera.
2. Stop it **centered on the scanner post**, so the middle of the base is in line with the post.
3. Stop it **close enough** that both grippers reach the back lane pallets and the top of a four-high stack on them without either arm
   extending, and **far enough** that neither arm, wrist, nor any part of the base touches the bench, a pallet, or the cart while both arms
   work.
4. Check the **left side**: the **left gripper** reaches Lane 1 and Lane 2, from the pallet up to four parcels high, and the hand-over point,
   all without extending.
5. Check the **right side**: the **right gripper** reaches Lane 3 and Lane 4, from the pallet up to four parcels high, and the hand-over point,
   all without extending.
6. Check the **cart** for the config this episode runs: the **cart gripper** reaches every parcel on the cart deck, the scanner window, the
   tally card, and the marker clip.
7. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
8. If any of lines 1 to 6 fails, push the base to a new park by hand and start again at line 1. Do not work a bench the arms cannot reach
   comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the bench hard enough to shift it, nothing touches
it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the scanner post and its frame includes all four lane pallets up to four parcels high, the lane signs,
   the scanner and its display, the tally card, and the cart with its parcels.
3. The camera reads the **lane display** after every scan and the **lane sign** on every pallet.
4. The camera reads the **shipping label** on the front of every parcel, so which parcel went to which lane is readable.
5. The camera reads the **tally card** well enough to see which boxes are ticked.
6. Both arms are at home with grippers open.
7. The **left arm** reaches Lanes 1 and 2 up to four high and the hand-over point without extending to a joint limit.
8. The **right arm** reaches Lanes 3 and 4 up to four high and the hand-over point without extending to a joint limit.
9. The cart arm for this config reaches the whole cart deck, the scanner window, the tally card, and the marker without extending to a joint limit.
10. A parcel carried to a back lane passes above a four-high stack on the front lane on that side.
11. The two arms do not collide, and neither arm passes in front of the other.
12. If a place cannot be reached, re-park the base by the Base positioning steps until lines 7 to 11 hold.

### Materials checklist

1. The **sort bench** stands where it lives, fixed to the floor. It is not moved, not leaned on, and not pushed at any point. Its top is at about
   waist height and nothing is above it.
2. A **scanner post** stands fixed at the back of the bench in the middle. Near its top is the **scanner**, window facing the base, and above it the
   **lane display**. The scanner reads a barcode by itself when it is held about a hand in front of its window, beeps, and shows the parcel's lane
   on the display (**unvalidated**: the mock must know each parcel's lane).
3. The four **lane pallets** are small mock pallets fixed on the bench top, each exactly one parcel in size, each with a **lane sign** on the bench
   in front of it. Two stand left of the post and two right of it:
   * **Lane 1** at the back left, **Lane 2** at the front left;
   * **Lane 3** at the front right, **Lane 4** at the back right.
4. Every lane pallet starts empty.
5. The **hand-over point** is in the middle of the bench, in front of the scanner post, a little above the bench top.
6. The **tally card** sits in a fixed holder on the front of the scanner post, below the scanner, facing out, with the **marker** standing point
   down in a clip beside it. The card has four lines, **LANE 1** to **LANE 4**, each with a row of **tick boxes** numbered **0 to 6**. The card
   is fresh: no box is ticked.
7. The **infeed cart** is a flat-top cart standing braked against the **left end** of the bench in **Config L** and against the **right end** in
   **Config R**, its deck at about bench height.
8. On its deck stand **ten parcels** in one row, running away from the bench, each clear of the next. All ten are closed cartons of the same
   footprint and height, light enough for one gripper to hold by its sides, each with a **shipping label** with a barcode on one long side, facing
   the base.
9. How many parcels belong to each lane changes per episode. Each lane gets between one and four, and the four counts add up to ten.
10. Nothing else stands on the bench or the cart within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the lane signs. You judge every other place by eye against the bench itself.

* **Sort bench:** the fixed bench the base is parked at. Never moved, never leaned on, never pushed.
* **Left lanes:** Lane 1 (back left) and Lane 2 (front left). **Left gripper only.**
* **Right lanes:** Lane 3 (front right) and Lane 4 (back right). **Right gripper only.**
* **Scanner post:** at the back middle, with the scanner, the lane display, the tally card, and the marker. **Cart gripper only.**
* **Hand-over point:** in the middle, in front of the post.
* **Infeed cart:** braked against the left end (Config L) or the right end (Config R) of the bench. **Cart gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works Lanes 1 and 2 and the **right gripper** works Lanes 3 and 4. The **cart gripper** also works the cart, the scanner,
  and the tally.
* The two arms meet only at the **hand-over point**.
* Neither arm goes into a lane on the other side, and neither reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds one parcel or the marker, and while it does, the other gripper is empty, taking a hand-over,
  or drawn **clear of the lanes**.

### Arm assignments

* **Cart gripper** (**left gripper** in Config L, **right gripper** in Config R). Takes every parcel off the cart, scans it, stacks the parcels for
  its own side's lanes, hands over the parcels for the other side, and ticks the tally.
* **Other gripper.** Takes each hand-over and stacks the parcel on its lane.
* **Stacking gripper** (the gripper of the named lane's side). Sets the parcel on its lane's stack.
* Only parcels are handed over. The marker is never handed over.

## Vocabulary

* **Cross-dock:** a place where inbound freight is sorted straight onto outbound lanes without going into storage.
* **Lane:** one lane pallet and the stack on it. Each lane is one outbound route.
* **Next parcel:** of the parcels still on the cart, the one nearest the bench.
* **Scan:** the cart gripper holds the parcel's shipping label about a hand in front of the scanner window, still, until it beeps and the lane display
  shows a lane. The scanner is never touched.
* **Named lane:** the lane the display shows after the scan. It is the only place the parcel may go.
* **Stacking gripper:** the gripper of the named lane's side, the **left gripper** for Lanes 1 and 2 and the **right gripper** for Lanes 3 and 4.
* **Stacked squarely:** the parcel sits flat on the pallet or on the parcel below it, its edges in line with the edges below on all four sides, its
  shipping label facing the base, and it stays put when the gripper opens.
* **Hand over:** the cart gripper brings the scanned parcel to the hand-over point and holds it still for a **half-second hold**. The other gripper then
  closes on the far side of it. Only after the other gripper is closed does the cart gripper open and draw back.
* **Lane count:** the number of parcels in a lane's stack.
* **Tick:** one mark with the marker inside a tick box: a short stroke down and to the right, then a longer stroke up and to the right, without lifting.
* **Clear of the lanes:** the arm is drawn up and back so that no part of it is over a lane, the hand-over point, or the cart.

## Steps

Run Steps 1 and 2 once for each of the ten parcels, then Step 3 once, and end the episode with Step 4. Each parcel is scanned and stacked before the
next is taken. The named lane decides the stacking gripper, and the config decides the cart gripper and the hand-overs.

### Step 1: Take and scan the next parcel

**Goal:** the cart gripper holds the next parcel and the lane display shows its lane.

* **IF Config L:** the **left gripper** is the cart gripper. **IF Config R:** the **right gripper** is the cart gripper.
* With the **cart gripper**, come down from above and close on the two long sides of the **next parcel**, near its middle, keeping clear of its shipping label.
* With the **cart gripper**, lift it straight up just clear of the deck, touching no other parcel.
* With the **cart gripper**, carry it level to the scanner and hold its shipping label about a hand in front of the window, still, until it beeps and the
  display shows a lane.
* Read the **named lane**. Its side decides the **stacking gripper**.
* With the other gripper, stay open and **clear of the lanes** unless it is waiting at the hand-over point.

**Check:** the display shows one lane, the scanner has not moved, and the parcels left on the cart still stand. If the display shows no lane, hold the
label in front of the window once more with the **cart gripper**. If it still shows none, stop and log a system issue.

### Step 2: Route and stack the parcel

**Goal:** the parcel is **stacked squarely** on its named lane.

#### 2.1 Bring the parcel to its lane

* **IF the named lane is on the cart gripper's side:** the cart gripper is the stacking gripper. With the **cart gripper**, carry the parcel level to above
  the named lane.
* **IF the named lane is on the other side:** with the **cart gripper**, carry the parcel to the **hand-over point** and hold it still for a **half-second
  hold**. With the **stacking gripper**, close on the far side of the parcel. With the **cart gripper**, open and draw back **clear of the lanes**. With the
  **stacking gripper**, carry the parcel level to above the named lane.
* **IF the named lane is a back lane (Lane 1 or Lane 4):** with the **stacking gripper**, carry the parcel above the top of the front lane's stack on that side,
  never through or against it.

**Check:** the **stacking gripper** holds the parcel level, label facing the base, above the named lane.

#### 2.2 Stack the parcel

* With the **stacking gripper**, line the parcel's edges up with the pallet, or with the top parcel of the stack, from above.
* With the **stacking gripper**, bring it straight down until it sits flat, shipping label facing the base, then open and lift straight up.
* With the **stacking gripper**, do not let it go from above the stack, do not slide it across the parcel below, and do not press down on the stack.
* With the **stacking gripper**, draw up and **clear of the lanes**.

**Check:** the parcel is **stacked squarely** and the parcels below it have not moved. If it hangs over an edge or sits crooked, close on its sides with the
**stacking gripper**, lift it just clear, and set it straight down again.

**Expected state:** the parcel is on its lane, and both grippers are clear. **IF a parcel is still on the cart:** go back to Step 1. **IF the cart deck is bare:**
go on to Step 3.

### Step 3: Tally the lane counts

**Goal:** each of the four lines of the tally card carries one tick in the box of its lane's count, and the marker is back in its clip.

* Count the parcels in each lane's stack, Lane 1 to Lane 4. The four counts add up to ten.
* With the **cart gripper**, close on the **barrel** of the marker, not on its point, and lift it straight up out of its clip.
* With the **cart gripper**, bring the marker point level to the **LANE 1** line, to the box numbered with Lane 1's count, draw one **tick**, and draw the point
  straight back off the card.
* With the **cart gripper**, tick the **LANE 2**, **LANE 3**, and **LANE 4** lines the same way, top to bottom. Press only hard enough to leave a mark.
* With the **cart gripper**, stand the marker back in its clip, point down, then open and draw back.
* With the other gripper, stay open and **clear of the lanes** for the whole of this step.

**Check:** each line carries **one tick**, in the box of that lane's count, and the four ticked numbers add up to ten. If a tick has run outside its box, leave it.
Do not draw over it and do not draw a second tick on that line.

### Step 4: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the sort done.

* Look once across the bench: the cart deck is bare, every lane stands square with labels facing the base, and the tally card has one tick per lane.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the sort is done and tallied, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the parcels off the lanes, top down, and stand them back on the cart deck in one row, clear of each other, labels facing the base.
2. Load the next episode's lane for each parcel into the scanner mock, one to four parcels per lane, ten in all.
3. Take the ticked tally card out of its holder and put in a fresh one. Check the marker still marks.
4. Move the cart to the end of the bench for the next episode's config and brake it.
5. Check every lane pallet is empty and every lane sign is readable.
6. Pick up anything that landed on the bench, the cart, or the floor.
7. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the reviewer sees. The coaching note is for
retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the bench shifts in frame, the bench edge changes angle or size in frame, or the base rolls, creeps, or turns at any point after recording starts.
* **SOP rule broken:** Steps 1 to 4, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Leaned on or pushed the bench, a stack, or the cart**

* **Visible cue:** a gripper, wrist, or forearm rests on the bench, a pallet, a stack, the scanner post, or the cart, or a stack or the cart shifts.
* **SOP rule broken:** Steps 1 to 3, the bench, the lanes, and the cart carry no weight from the arms.
* **Coaching note:** the arm holds itself up. A stack is set on, never pressed on.

**Violation: Parcel taken wrong**

* **Visible cue:** a parcel other than the next parcel is taken; two parcels come off together; or a parcel is dragged across the deck or knocks the one beside it.
* **SOP rule broken:** Step 1, take the next parcel by its long sides and lift it straight up, touching no other parcel.
* **Coaching note:** nearest first, one at a time, straight up.

**Violation: Parcel held wrong**

* **Visible cue:** a parcel is held by its top, one corner, or its label; its label is covered at the scanner; or it tilts or swings in the gripper.
* **SOP rule broken:** Steps 1 and 2.1, close on the two long sides near the middle, keep the label free, and carry the parcel level.
* **Coaching note:** long sides, middle, level, label free.

**Violation: Scan skipped or done out of turn**

* **Visible cue:** a parcel is stacked or handed over without a scan, or before the display shows its lane; or the next parcel is taken before the last one is stacked.
* **SOP rule broken:** Step 1, scan each parcel and read its lane before it moves toward any lane.
* **Coaching note:** scan, read, then move. The lane comes from the scanner, not a guess.

**Violation: Scanner handled or knocked**

* **Visible cue:** a parcel or gripper bumps the scanner window or the display, or the scanner post is knocked.
* **SOP rule broken:** Step 1, hold the label a hand in front of the window; the scanner is never touched.
* **Coaching note:** bring the label to the scanner and stop a hand short.

**Violation: Wrong lane**

* **Visible cue:** a parcel is stacked on a lane other than the one the display named, including the other lane on the same side.
* **SOP rule broken:** Steps 2.1 and 2.2, each parcel goes on its named lane and nowhere else.
* **Coaching note:** read the display, find the lane sign, match them before the parcel goes down.

**Violation: Not stacked squarely**

* **Visible cue:** a parcel hangs over an edge of the pallet or the parcel below, sits crooked, stands on its side or end, or has its label facing away from the base.
* **SOP rule broken:** Step 2.2, line the edges up from above and set the parcel flat, label facing the base.
* **Coaching note:** edges in line on all four sides. A crooked parcel makes the whole lane lean.

**Violation: Parcel dropped onto the stack**

* **Visible cue:** a parcel is let go from above the stack and falls onto it, or bounces or slides after landing.
* **SOP rule broken:** Step 2.2, bring each parcel straight down until it sits flat before opening.
* **Coaching note:** down onto the stack, then open.

**Violation: Stack disturbed**

* **Visible cue:** setting a parcel shoves, slides, or tips a parcel below it; a parcel is slid across the top of a stack; or a stack is pressed down.
* **SOP rule broken:** Step 2.2, set each parcel straight down, and do not slide it or press on the stack.
* **Coaching note:** straight down only. The parcels below are already stacked.

**Violation: Carried through a front stack**

* **Visible cue:** a parcel on its way to Lane 1 or Lane 4 hits, scrapes, or pushes the stack on Lane 2 or Lane 3.
* **SOP rule broken:** Step 2.1, carry a parcel for a back lane above the front lane's stack.
* **Coaching note:** up and over, never through.

**Violation: Hand-over done wrong**

* **Visible cue:** the cart gripper opens before the stacking gripper has closed; the parcel is still moving when the stacking gripper closes, with no half-second hold;
  the hand-over happens away from the hand-over point; a parcel for the cart's own side is handed over; or a parcel is handed over before its scan.
* **SOP rule broken:** Step 2.1, hand over only parcels for the other side, after the scan, at the hand-over point, held still, and open only after the other gripper
  has closed.
* **Coaching note:** scan, stop, hold still, let the other gripper take it, then open.

**Violation: Wrong tally**

* **Visible cue:** a lane's tick is in a box that does not match the number of parcels on that lane, or the four ticked numbers do not add up to ten.
* **SOP rule broken:** Step 3, count each lane's stack and tick the box of that count.
* **Coaching note:** count the stack, then find the number. Tick what is there.

**Violation: Tally filled in wrong**

* **Visible cue:** a line is skipped or ticked twice; lines are ticked out of top-to-bottom order; the tally starts before the cart is bare; a tick is drawn over; or any
  other mark is made on the card.
* **SOP rule broken:** Step 3, once all ten parcels are stacked, tick each lane's line once, Lane 1 to Lane 4.
* **Coaching note:** sort first, then tally, one tick per lane.

**Violation: Marker handled wrong**

* **Visible cue:** the marker is held by its point, pressed hard enough to bend its tip or push the card, laid on the bench, dropped, or not stood back in its clip point down.
* **SOP rule broken:** Step 3, hold the marker by its barrel and stand it back in its clip, point down.
* **Coaching note:** barrel in the gripper, light on the card, back in the clip.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the bench is not set up in: the gripper away from the cart takes a parcel off the cart, scans, or ticks the tally; a gripper reaches
  for a cart end that is empty; or the cart is moved before or during the episode.
* **SOP rule broken:** Steps 1, 2.1, and 3, look at the bench, find the cart, and follow the IF line that matches the config the episode is set up in.
* **Coaching note:** look at the cart before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** a parcel moves toward a lane before its scan; the next parcel is taken before the last one is stacked; or the tally starts before all ten are stacked.
* **SOP rule broken:** Steps 1 to 3, for each parcel: take, scan, route, stack; then tally.
* **Coaching note:** one parcel start to finish, then the next. The tally is last.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two parcels; both grippers carry different parcels at the same time outside a hand-over; or a gripper holds a parcel or the marker while
  the other works instead of being clear of the lanes.
* **SOP rule broken:** Steps 1 to 3, one gripper holds one thing, and the other is empty, taking a hand-over, or clear of the lanes.
* **Coaching note:** one parcel, one trip.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: no lane shown, a parcel hanging over an edge, or a tally
  that does not add up to ten.
* **SOP rule broken:** Steps 1 to 3, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a parcel or the marker is dropped on the bench, the cart, or the floor; a stack is knocked over; or a parcel on the cart is knocked over.
* **SOP rule broken:** Steps 1 to 3, nothing is dropped or knocked out of its place, and every gripper lifts clear the way it came in.
* **Coaching note:** check the path and the landing place before the arm moves.

**Violation: Wrong arm used**

* **Visible cue:** the **left gripper** stacks on Lane 3 or Lane 4; the **right gripper** stacks on Lane 1 or Lane 2; the gripper away from the cart touches the cart, the scanner, or the
  marker; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 3, each gripper stacks its own side's lanes, only the cart gripper works the cart, scanner, and tally, and the arms never cross.
* **Coaching note:** left lanes, left arm. Right lanes, right arm. The cart side scans and tallies.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a parcel on the cart or on the wrong lane, a stack not square, a lane not tallied, the marker out of its clip, an arm short of home, or a
  gripper not fully open.
* **SOP rule broken:** Step 4, look once across the bench, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read the lane display, a lane sign, a shipping label, or the tally card**, so which parcel went where or what was tallied cannot be judged.
* **Scanner fault:** no lane shown on a correctly held label, or the display shows a lane the mock was not loaded with.
* **Setup fault:** a lane loaded with more than four parcels or none, counts that do not add up to ten, or a torn or unreadable shipping label.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a lane, the top of a four-high stack, the scanner, the hand-over point, or the tally
  card cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Take the next parcel off the cart
2. Scan one parcel and read its lane
3. Hand one parcel over at the hand-over point
4. Carry a parcel over a front stack
5. Stack one parcel squarely on its lane
6. Count the four lane stacks
7. Take the marker from its clip
8. Tick one lane count
9. Stand the marker back in its clip
10. Return both arms home and end the episode
