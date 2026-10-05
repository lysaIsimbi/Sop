# Load the Washing Machine SOP (1x Load, in situ)

One episode loads one empty washing machine where it is installed and starts it: the door is opened, the
garments go from the hamper into the drum one at a time, the pockets of every pair of shorts are checked
on the way, the door is closed, the dial is set, and the machine is started. The base is **passive**: it
has no drive of its own, so it is pushed by hand up to the machine and locked there. Everything the
episode touches is already at the machine when recording starts.

The washing machine is worked **as found**. The drum is empty, the door is **almost closed** (not
latched), and the dial points at OFF. The garments lie loose in the hamper at one end of the low
table in front of the machine. The pocket dish stands on the table between the hamper and the middle.

**This is an in-situ task, and three things follow from that.** First, the drum is deep and the arms
cannot reach its back, so **no gripper reaches deep into the drum. A garment is laid just inside the
mouth and let go there.** Second, **the machine and the table are never leaned on and never pushed**: no
gripper, wrist, or forearm rests on the door, the mouth rim, the control panel, or the table, and the
only pushes in this SOP are the door being swung open and closed and the Start button being pressed.
Third, **nothing is thrown**: every garment and the tissue are held over the place they go and let go
there.

The order never changes: **open the door, then all the garments (pockets checked on the way), then close
the door, then the dial, then Start.** The door is shut before the dial is touched, and the dial is set
before Start is pressed.

The station is set up in one of two ways. Only the **hamper** and the **pocket dish** move. The machine,
the table, the dial, and the Start button are the same in both.

* **Config L:** the hamper stands at the **left** end of the table. The pocket dish stands between it
  and the check spot.
* **Config R:** the hamper stands at the **right** end of the table. The pocket dish stands between it
  and the check spot.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on
the setup it says so on an **IF** line. Look at the table and follow the line that matches. Who does
what is the same in both configs:

* **Garment rule:** the **right gripper** takes each garment out of the hamper and lays every garment in
  the drum. In Config L, if the hamper is too far for the right gripper, the **left gripper** takes the
  garment out and hands it to the right gripper at the check spot.
* **Pocket rule:** for a pair of shorts, the **right gripper** holds the waistband at the check spot and
  the **left gripper** pulls each pocket open. If the left gripper cannot get at a pocket, the arms
  **exchange**: the left gripper takes the waistband and the right gripper pulls that pocket open.
* **Door rule:** the **right gripper** swings the door open, and later, closed, pushes the door round and
  presses it shut.
* **Panel rule:** the **left gripper** turns the dial, and presses Start with the gripper closed.

The machine is powered but its water tap is shut off, so the cycle starts dry. The cycle is cancelled
during the reset.

## Setup

Complete the base positioning and all the checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never
steered, pushed, or moved once recording starts. It is parked once, before recording, and does not move
again until the episode is over.

1. Push the base by hand up to the near edge of the table and stop it **square to the front of the
   machine**, so the front of the machine runs straight across the frame and neither end of the table
   sits nearer than the other.
2. Stop it **in the middle of the drum mouth**, so the left rim and the right rim of the mouth are the
   same distance out from the middle of the base.
3. Stop it **close enough** that each gripper reaches through the mouth to just past the rubber ring
   without the arm stretching out.
4. Check the **door's swing**: open it by hand to the left, wider than a right angle. Open, it is clear
   of the left arm, the left side of the base, and the left arm's path to the mouth, and its bottom edge
   is higher than the hamper rim. Shut it again before recording.
5. Check the **hamper** at both ends: the **right gripper** reaches the bottom of the hamper and every
   part of its open top without stretching out with the hamper at the right end (Config R). With the
   hamper at the left end (Config L), note whether the **right gripper** reaches it without stretching
   out. If it does not, the **left gripper** must reach it, and the garments are handed over (Step 2.1).
6. Check the **check spot**: both grippers reach the space above the middle of the table, in front of
   the mouth, without stretching out.
7. Check the **pocket dish** at both of its spots: both grippers reach over it from above without
   stretching out.
8. Check the **door, the dial, and Start**: the **right gripper** reaches the door's free edge when the
   door is almost closed, the door's inner face near the free edge and near the hinge, and the door's
   front face at its free edge. The **left gripper** reaches the dial and the Start button. Neither arm
   stretches out.
9. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
10. If any of lines 1 to 8 fails, push the base to a new park by hand and start again at line 1. Do not
    work a station the arms cannot reach easily.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the machine
or the table hard enough to shift it, nothing and nobody touches it, and it is never moved mid-task. A
base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is in the middle of the drum mouth, and its frame shows the door, both shut and
   swung open to the left, the whole mouth with its rubber ring, the front of the drum floor, the control
   panel with the dial and Start, and the whole table with the hamper and the pocket dish.
3. The camera reads the front of the drum floor through the mouth, so a garment lying on the rubber ring
   can be told from one lying inside.
4. The camera reads the check spot, so the inside of a pocket that is pulled open is visible and a
   tissue in it can be seen.
5. The camera reads the dial, so its turn can be seen from the base.
6. The camera reads the door front while it is shut, so a gap along the door edge, or cloth
   caught in it, is visible.
7. Both arms are at home with grippers open.
8. The **right arm** reaches the hamper at the right end, the check spot, the pocket dish, the mouth,
   the door's free edge when the door is almost closed, the door's inner face, and the door's front
   face at its free edge, without reaching a joint limit.
9. The **left arm** reaches the hamper at the left end, the pocket dish at both of its spots, the check
   spot, the mouth, the dial, and the Start button, without reaching a joint limit.
10. The two arms do not collide over the check spot, at the mouth, at the door, or at the dial, and the
    open door is clear of both arms' paths.
11. If a place cannot be reached, park the base again by the Base positioning steps until lines 8 to
    10 hold.

### Materials checklist

1. The **washing machine** is a front-loading machine standing where it is installed, on a pedestal, so
   the bottom of the drum mouth sits about level with the arms. It is not moved, not leaned on, and not
   pushed at any point. It is powered, its water tap is shut off, and the dial points at **OFF**.
2. The **door** is hinged on the **left** of the machine. At the start it is **almost closed**: pushed
   nearly shut but not latched, with a gap of about a finger's length at the free edge. Swung open to the
   left, wider than a right angle, it stays there on its own. It shuts with a latch, and a shut door sits
   flush with the front of the machine all round.
3. The **drum** is empty, dry, and still. The **rubber ring** round the inside of the mouth is clean and
   has nothing caught in it.
4. The **dial** sits on the control panel above the mouth, right of the middle. It clicks from one
   program to the next.
   The **Start** button sits beside it, under the dial's right side.
5. The **table** is low and stands on the floor in front of the machine, below the door opening, between
   the machine and the base. It does not move when something is set on it or taken off it.
6. The **hamper** is a low, open-top laundry basket. Its rim is lower than the bottom edge of the open
   door, so the door swings clear over it. It stands at the **left** end of the table in **Config L**
   and at the **right** end in **Config R**.
7. The **garments** lie loose in the hamper: cotton t-shirts, hand towels, and pairs of cotton
   **shorts**, all dry, none rolled, knotted, or tucked into another. Each pair of shorts has two open
   front **pockets** and lies with part of its waistband showing.
8. One folded **tissue** sits in **one** front pocket of the shorts, chosen at the reset. The other
   pockets are empty.
9. The **pocket dish** is a small open dish, empty. It stands on the table between the hamper and the
   check spot.
10. The **check spot**, the part of the table in the middle, in front of the mouth, is clear.
11. The floor around the table and the base is clear and dry.

### Workspace layout

* **Washing machine:** straight ahead of the parked base, on its pedestal, drum mouth about level with
  the arms.
  * **Mouth:** the round door opening, with the **rubber ring** round its inside. The **bottom rim** is
    the lower edge of the opening.
  * **Drum floor:** the bottom of the drum. Only its front is within reach.
  * **Door:** hinged on the left, almost closed at the start. It opens to the left, wider than a right
    angle.
  * **Control panel:** above the mouth. The **dial** is right of the middle and **Start** is under its
    right side.
* **Table:** low, in front of the machine under the door opening, between the machine and the base.
  * **Hamper:** at the left end (Config L) or the right end (Config R).
  * **Pocket dish:** between the hamper and the check spot.
  * **Check spot:** the middle of the table, in front of the mouth. Shorts are held above it for the
    pocket check. Nothing is set down on it.

### Arm assignments

* **The right gripper owns the garments.** It takes each garment out of the hamper, holds a pair of
  shorts by the waistband at the check spot, and lays every garment just inside the mouth.
* **The left gripper works the pockets.** It pulls the pockets open and drops the tissue in the pocket
  dish when it finds it. It takes a garment out of the hamper only in Config L when the hamper is too
  far for the right gripper, and then hands it straight to the right gripper. It never lays a garment
  in the drum.
* **Exchange arms only when needed.** If the left gripper cannot get at a pocket, the left gripper takes
  the waistband and the right gripper pulls that pocket open and drops the tissue in the pocket dish if
  it finds it. The right gripper then takes the waistband back.
* **The right gripper swings the door open, and later, closed, pushes it round and presses it shut. The
  left gripper turns the dial and presses Start with the gripper closed.**
* A garment is let go only just inside the mouth, or at a hand-over once the other gripper holds it. The
  tissue is let go only over the pocket dish. Never open a gripper over open space, over the table, or
  over the floor while it holds something.

## Vocabulary

* **In situ:** the machine is worked where it is installed. Nothing is taken away from it, and nothing
  about the laundry area is moved around for the task.
* **Passive base:** the base has no drive. It is pushed by hand to its park before recording, locked
  there, and it does not move at all during the episode.
* **Config:** the end of the table the hamper stands at. **Config L:** hamper left. **Config R:** hamper
  right. The pocket dish always stands between the hamper and the check spot.
* **Drum:** the round chamber inside the machine where the laundry goes. The **drum floor** is its
  bottom.
* **Mouth:** the round door opening at the front of the drum. The **bottom rim** is its lower edge.
* **Rubber ring:** the soft ring round the inside of the mouth. Cloth left lying on it gets caught in the
  door.
* **Garment:** one piece of the laundry: a t-shirt, a hand towel, or a pair of shorts.
* **Top garment:** the garment lying highest in the hamper, the one with nothing on top of it.
* **Waistband:** the band round the top of a pair of shorts. Shorts are always held by it.
* **Pocket:** one of the two open front pockets on a pair of shorts. Its **opening** is the slit at the
  top where a hand goes in. Its **front edge** is the side of the opening nearer the base.
* **Check spot:** the space above the middle of the table, in front of the mouth, where a pair of shorts
  is held for the pocket check.
* **Hand-over:** one gripper pinches the garment (the waistband, for shorts) beside the other gripper,
  both hold still for half a second, then the first gripper lets go.
* **Exchange arms:** the left gripper takes the waistband from the right gripper by a hand-over, so the
  right gripper is free to work a pocket the left gripper cannot get at. The right gripper takes the
  waistband back the same way after.
* **Pull open:** a gripper pinches the front edge of a pocket opening and draws it toward the base, a
  finger's length, so the inside of the pocket shows. **Unvalidated:** whether the camera sees the
  bottom of the pocket.
* **Tissue:** the folded paper tissue left in one pocket. It goes in the pocket dish, never in the drum.
* **Lay in:** the right gripper carries the garment through the mouth until the gripper is just past the
  rubber ring, lowers it onto the front of the drum floor or onto the laundry already there, and opens.
* **Inside the drum:** the whole garment lies past the rubber ring. No part lies on the ring or hangs out
  of the mouth.
* **Door inner face:** the side of the door that faces the mouth when the door stands open.
* **Door front face:** the outer side of the door. Its **free edge** is the edge away from the hinge,
  where the latch is.
* **Almost closed:** the door is pushed nearly shut but not latched. A gap of about a finger's length
  shows at the free edge.
* **Round:** the door has swung from standing open to hanging in front of the mouth, touching or nearly
  touching the front of the machine, but not yet latched.
* **Shut:** the door is latched, sits flush with the front of the machine all round, no gap or cloth
  shows along its edge, and it does not spring back when the right gripper comes off.
* **Click:** one step of the dial from one program to the next. The dial stops at each click.
* **Resting:** the thing has stopped moving and stays still for 2 seconds after the gripper opens.
* **Clear of:** not touching. A gap shows between the two things.

### Handling standard

* Move exactly one garment at a time.
* Take the top garment every time. Never dig under one garment for another.
* Every pair of shorts has both pockets checked at the check spot before it goes in the drum. T-shirts
  and hand towels go straight to the drum.
* No gripper reaches deep into the drum. Garments are laid just past the rubber ring and let go there.
* The tissue goes only in the pocket dish.
* The door is opened in Step 1, before anything else is touched. After that it is touched only in
  Step 3, once both grippers are empty and out of the mouth.
* The dial is touched only in Step 4, once the door is shut. Start is touched only in Step 5, once the
  dial is set.
* Nothing rests on the machine or the table. No gripper, wrist, or forearm leans on the door, the mouth
  rim, the control panel, or the table.

## Steps

### Step 1: Open the door

**Goal:** the door stands open to the left, wider than a right angle, and stays there on its own.

* With the **right gripper**, come to the gap at the door's **free edge** and pinch the edge.
* With the **right gripper**, draw the door round to the left, steadily, until it points straight out at
  the base.
* With the **right gripper**, let go of the edge.
* With the **right gripper** closed, touch the door's **inner face** near the free edge and push it on
  to the left until it stands open wider than a right angle.
* With the **right gripper**, draw straight back off the door.
* The **left gripper** waits clear of the door.

**Check:** the door stands open to the left, wider than a right angle, stays there on its own, and is
clear of both arms' paths to the mouth. If it swings back, the **right gripper** pushes it open again.

**Expected state:** the door stands open to the left, the drum is empty, the garments are in the
hamper, and both grippers are empty and clear of the door.

### Step 2: Move the garments from the hamper into the drum

**Goal:** the hamper is empty, all the garments lie inside the drum, and both pockets of each pair of
shorts were checked on the way, with the tissue in the pocket dish.

Work one garment at a time, top garment first. Do 2.1, then 2.2 only if the garment is a pair of shorts,
then 2.3.

#### 2.1 Take the top garment out of the hamper

* **IF Config R:** the hamper is at the right end of the table, and the **right gripper** takes the
  garment. **IF Config L:** the hamper is at the left end. The **right gripper** takes the garment if it
  reaches the hamper without stretching out. If it does not, the **left gripper** takes it and hands it
  over (last bullet).
* With the **right gripper**, come down over the hamper and pinch the top garment by the part on top.
  If the top garment is a pair of shorts, pinch it by the waistband.
* With the **right gripper**, lift the garment straight up until it hangs clear of the hamper rim and
  of the other garments.
* If a second garment comes up caught on it, with the **right gripper** lower both back into the hamper,
  let go, and pinch the top garment again.
* The **left gripper** waits clear of the hamper.
* **IF Config L and the hamper is too far for the right gripper:** with the **left gripper**, take the
  top garment the same way, by the waistband for shorts, and carry it to the **check spot**. With the
  **right gripper**, pinch the garment (the waistband, for shorts) beside the left gripper. Both
  grippers hold still for half a second. With the **left gripper**, let go.

**Check:** one garment hangs from the right gripper, clear of the hamper. The rest are still in the
hamper.

#### 2.2 Check both pockets (shorts only)

* With the **right gripper**, carry the shorts by the waistband to the **check spot**, hanging, front
  toward the base. If the back faces the base, turn them round with the wrist.
* With the **right gripper**, hold the shorts still at the check spot until both pockets are done.
* With the **left gripper**, **pull open** one pocket: pinch the front edge of its opening and draw it
  toward the base, a finger's length. Hold it open for 1 second so the camera sees inside.
* If the tissue shows, with the **left gripper** let go of the edge, pinch the tissue through the
  opening, and draw it straight out. Carry it to the **pocket dish**, hold it over the dish, and open.
* If the pocket is empty, with the **left gripper** let go of the edge.
* With the **left gripper**, do the same for the other pocket.
* **IF the left gripper cannot get at a pocket, exchange arms:** with the **left gripper**, pinch the
  waistband beside the right gripper. Both grippers hold still for half a second. With the **right
  gripper**, let go of the waistband. With the **left gripper**, hold the shorts still. With the **right
  gripper**, pull that pocket open the same way, and if the tissue shows, draw it out and open over the
  pocket dish.
* When both pockets are done, if the **left gripper** holds the shorts, with the **right gripper** take
  the waistband back the same way: pinch beside it, both hold still for half a second, and with the
  **left gripper** let go.

**Check:** both pockets were pulled open and looked into, the tissue, if it was in these shorts, is in
the pocket dish, and the **right gripper** holds the shorts by the waistband. If the tissue fell on the
table, the gripper that dropped it picks it up and drops it in the pocket dish. If the tissue fell in the
hamper or on the floor, leave it there and carry on.

#### 2.3 Lay the garment in the drum

* With the **right gripper**, carry the garment, hanging, up to the mouth.
* With the **right gripper**, **lay in** the garment: carry it through the mouth until the gripper is
  just past the rubber ring, bring it down onto the front of the drum floor or onto the laundry already
  there, and open.
* With the **right gripper**, draw straight back out of the mouth.
* The **left gripper** waits clear of the mouth.

**Check:** the garment lies **inside the drum**. If any part lies on the rubber ring or hangs out of the
mouth, the **right gripper** pinches that part and pushes it past the ring, then draws back out. If the
laundry at the front has built up to the rubber ring, the **right gripper**, closed, pushes it back a
hand's length into the drum and draws back out. A garment that has fallen on the table is picked up by
any part with the **right gripper** and laid in again. A garment that has fallen on the floor is left
where it is.

Go back to 2.1 for the next garment until the hamper is empty.

**Check:** look into the hamper. It is empty. Look at the pocket dish. The tissue is in it. If a garment
is left in the hamper, go back to 2.1 for it. If the tissue is not in the dish, carry on. Never go into the
drum after it.

**Expected state:** the hamper is empty, the garments lie inside the drum, the tissue is in the pocket
dish, the door still stands open to the left, and both grippers are empty and out of the mouth.

### Step 3: Close the door

**Goal:** the door is **shut** and flush with the front of the machine, with no cloth caught in it.

#### 3.1 Push the door round

* Check first that both grippers are empty and out of the mouth, and that no garment lies on the rubber
  ring.
* With the **right gripper** closed, touch the door's **inner face** near the hinge.
* With the **right gripper**, push steadily, so the door swings **round** toward the mouth in one smooth
  move. Do not push fast and do not let the door swing on its own.
* With the **right gripper**, stop when the door hangs in front of the mouth, touching or nearly
  touching the front of the machine.
* The **left gripper** waits clear of the door.

**Check:** the door hangs in front of the mouth and no cloth shows between the door and the machine. If
cloth is caught, the **right gripper** opens, pinches the free edge, draws the door back open, and lets
go. Then the **right gripper** pushes the cloth past the rubber ring, draws back out, and, closed,
pushes the door round again.

#### 3.2 Press the door shut

* With the **right gripper** closed, press the door's **front face** flat at the **free edge**, straight
  back toward the machine.
* With the **right gripper**, press until the latch holds. Hold the press for 2 seconds.
* With the **right gripper**, press straight back only. Do not slam it, do not press at an angle, do not
  press on the door glass, and do not press hard enough to move the machine.
* With the **right gripper**, draw straight back off the door. It waits clear of the machine until the
  episode ends.

**Check:** the door is **shut**: flush all round, no gap or cloth along its edge, and it does not spring
back when the **right gripper** comes off. If it springs back or a gap shows, the **right gripper**,
closed, presses it once more at the free edge.

**Expected state:** the door is shut with the garments behind it, the dial still points at OFF, and both
grippers are clear of the machine.

### Step 4: Set the dial

**Goal:** the dial is set on a program.

* With the **left gripper**, come to the dial from the front and close on the knob across its two sides.
* With the **left gripper**, turn the knob **clockwise** off OFF onto a program.
* With the **left gripper**, open and draw straight back off the dial.
* The **right gripper** waits clear of the control panel.

**Check:** the dial is off OFF and sits at a click, not between two. If it does not, the **left
gripper** closes on the knob again and turns it onto a program.

**Expected state:** the dial is set, the door is shut, and Start has not been pressed.

### Step 5: Press Start

**Goal:** the machine has started.

* With the **left gripper** closed, come to the **Start** button from the front.
* With the **left gripper**, press it straight in until it clicks. Hold for 1 second.
* With the **left gripper**, draw straight back off the button.
* The **right gripper** waits clear of the control panel.

**Check:** the machine has started. If it has not, the **left gripper**, closed, presses Start once
more.

**Expected state:** the machine is running with the door locked, the hamper is empty, and the
tissue is in the pocket dish.

### Step 6: End the episode

**Goal:** the load is done and both arms are safely home.

* Look once across the station: door shut and locked, dial set, hamper empty, tissue in the pocket
  dish, base still locked in place.
* With **both grippers**, return home.
* Stop recording.

**Check:** both arms are at home with grippers open.

**Expected state:** the machine is running with the load inside, and both arms are at home.

## After the episode: reset the workspace

This reset is not recorded. The base stays parked and locked through the reset, and is only pushed away
by hand once the station is set for the next episode.

1. Cancel the cycle, turn the dial back to OFF, and wait for the door lock to let go.
2. Open the door to the left and take the garments out of the drum. Check the drum and the rubber
   ring are dry and clear.
3. Push the door almost closed: nearly shut, not latched, with a gap of about a finger's length at the
   free edge.
4. Put the tissue back, folded, in **one** front pocket of the shorts. Change which pocket from one
   episode to the next.
5. Put all the garments back loose in the hamper, none rolled, knotted, or tucked into another, with part
   of each pair of shorts' waistband showing. Change which garment is on top from one episode to the
   next.
6. Set the hamper at the left end (Config L) or the right end (Config R) of the table for the next
   episode's config, and the pocket dish between it and the check spot. Change the config from one
   episode to the next. Empty the pocket dish. Check the check spot is clear.
7. Replace any garment that is torn or damp, and any tissue that is torn.
8. Check the door stands open on its own and latches when pressed, the dial still clicks, and the
   table has not moved.
9. Check the base is still square, in the middle, and locked, and push it firmly once by hand to check it
   does not roll. If it has moved, park it again by the Base positioning steps.
10. Run the Setup checklists again.

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

* **Visible cue:** the work does not match the config the episode is set up in: the garments are taken
  from the wrong end of the table, the tissue is dropped where the pocket dish would stand in the other
  config, or the hamper or the pocket dish is moved during the episode.
* **SOP rule broken:** the config set before recording and the IF line in Step 2.1.
* **Coaching note:** look at where the hamper is before you move. It stays there for the whole episode.

**Violation: Base moved during the episode**

* **Visible cue:** the base rolls, creeps, or turns after recording starts, the mouth shifts in the frame,
  or an arm pushes off the machine or the table hard enough to move the base.
* **SOP rule broken:** Base positioning, the base is parked and locked before recording and does not move
  at all during the episode.
* **Coaching note:** park it, lock it, push-test it. If the park is wrong, fix it before recording, never
  during.

**Violation: Machine or table leaned on or pushed**

* **Visible cue:** a gripper, wrist, or forearm rests on the mouth rim, the door, the control panel, or
  the table; an arm pushes off any of them; or the table or the machine visibly shifts.
* **SOP rule broken:** Steps 1 to 5, nothing rests on the machine or the table, and the only pushes are
  the door being swung open and closed and Start being pressed.
* **Coaching note:** nothing at the station holds an arm up. Take the weight on the arm.

**Violation: Work order broken**

* **Visible cue:** the work does not run open the door, then all the garments, then close the door, then
  the dial, then Start. For example a garment is taken out of the hamper before the door is open, the
  door is pushed round while a garment is still in the hamper, or the dial is turned while the door is
  open.
* **SOP rule broken:** Steps 1 to 5, the order is open the door, garments, close the door, dial, Start.
* **Coaching note:** say the next stage out loud before you reach for anything. The order never changes.

**Violation: Garment handled by the left gripper**

* **Visible cue:** the left gripper takes a garment out of the hamper in Config R, or in Config L when
  the right gripper reaches the hamper; carries a garment to the mouth; or lays a garment in the drum.
* **SOP rule broken:** Garment rule and Steps 2.1 and 2.3, the right gripper takes every garment out of
  the hamper, except in Config L when the hamper is too far for it, and lays every garment in the drum.
* **Coaching note:** the right hand is the laundry hand. The left hand works the pockets.

**Violation: More than one garment moved at a time**

* **Visible cue:** two garments go to the check spot or into the drum together, or a caught second
  garment is carried on instead of being lowered back into the hamper.
* **SOP rule broken:** Step 2.1, move exactly one garment at a time, and lower both back if a second comes
  up with it.
* **Coaching note:** one garment hanging, nothing else. If two come up, put them back and try again.

**Violation: Garment dug out instead of taken from the top**

* **Visible cue:** a gripper takes a garment that is not the top garment, pushes one garment aside
  to get at another, or takes a pair of shorts by a leg instead of the waistband.
* **SOP rule broken:** Step 2.1, take the top garment first, and take shorts by the waistband.
* **Coaching note:** the one on top is the one you take. Shorts by the waistband, so the pockets hang
  right.

**Violation: Shorts put in the drum without a pocket check**

* **Visible cue:** a pair of shorts goes into the drum without going to the check spot, or with only one
  pocket pulled open, or the tissue goes into the drum inside a pocket.
* **SOP rule broken:** Step 2.2, every pair of shorts has both pockets pulled open and looked into before
  it goes in the drum.
* **Coaching note:** every pair, both pockets, every time. A tissue in the wash covers the whole load in
  paper.

**Violation: Garment dropped at a hand-over**

* **Visible cue:** one gripper lets go of a garment before the other gripper holds it, or without the
  half-second still hold, and the garment drops or slips down to the table.
* **SOP rule broken:** Steps 2.1 and 2.2, the taking gripper pinches the garment beside the other, both
  hold still for half a second, then the first gripper lets go.
* **Coaching note:** both hands on, count half a second, then let go.

**Violation: Pocket not held open long enough to see inside**

* **Visible cue:** a gripper pulls a pocket open and lets go at once, pulls it open less than a finger's
  length, or pulls it open facing away from the camera, so the inside never shows.
* **SOP rule broken:** Step 2.2, pull the front edge a finger's length toward the base and hold it open
  for 1 second.
* **Coaching note:** open it toward the camera and count one. The camera has to see the bottom.

**Violation: Shorts not held still at the check spot**

* **Visible cue:** the gripper holding the waistband swings, moves, or lets the shorts sag onto the table
  while the other gripper works a pocket, holds them away from the check spot, or holds them back toward
  the base.
* **SOP rule broken:** Step 2.2, the holding gripper keeps the shorts still, hanging, front toward the
  base, at the check spot until both pockets are done.
* **Coaching note:** the holding hand is a hook. It does not move until the other hand is done.

**Violation: Tissue not put in the pocket dish**

* **Visible cue:** the tissue is let go over the drum, the hamper, the table, or the floor, is left
  hanging half out of the pocket, or falls on the way and is not picked up and put in the dish.
* **SOP rule broken:** Step 2.2, draw the tissue straight out, carry it to the pocket dish, and open over
  the dish.
* **Coaching note:** pocket, then dish, nowhere in between.

**Violation: Garment reached deep into the drum or thrown in**

* **Visible cue:** the right gripper reaches past the front of the drum floor, opens before it is past the
  rubber ring so the garment is flung in, or pushes garments to the back of the drum with the arm.
* **SOP rule broken:** Step 2.3, lay in the garment just past the rubber ring, bring it down, and open.
* **Coaching note:** just past the ring, down, open, out. The drum does the rest.

**Violation: Garment left on the rubber ring**

* **Visible cue:** the right gripper draws out while part of a garment still lies on the rubber ring or
  hangs out of the mouth, and it is not pushed in before the next garment.
* **SOP rule broken:** Step 2.3, check the garment lies inside the drum, and push any part on the ring past
  it.
* **Coaching note:** look at the ring every time you come out. Cloth on the ring is cloth in the door.

**Violation: Hamper not checked empty**

* **Visible cue:** a gripper goes for the door while a garment is still in the hamper, or a garment
  is left out of the drum when the door is pushed round.
* **SOP rule broken:** Step 2, look into the hamper and check it is empty before moving to Step 3.
* **Coaching note:** look in the hamper before you touch the door. All in the drum, none in the hamper.

**Violation: Door opened wrongly**

* **Visible cue:** the left gripper swings the door open, the door is yanked or pulled at an angle,
  flung open so it swings on its own and hits the machine side, or left standing less than a right angle
  open when the garment work starts.
* **SOP rule broken:** Step 1, the right gripper draws the free edge round and pushes the inner face
  until the door stands open wider than a right angle.
* **Coaching note:** right hand walks it open, slow the whole way.

**Violation: Door touched early or pushed with the mouth blocked**

* **Visible cue:** a gripper takes hold of the door or pushes it during Step 2, or the right gripper
  pushes the door round while a gripper is still in the mouth or cloth lies on the rubber ring.
* **SOP rule broken:** Step 3.1, the door is touched only once both grippers are empty and out of the
  mouth and nothing lies on the ring.
* **Coaching note:** hands out, ring clear, then the door.

**Violation: Door pushed round wrongly**

* **Visible cue:** the left gripper pushes the door round, the right gripper pushes it open instead of
  closed, the door is pushed fast, let swing on its own, or hits the machine.
* **SOP rule broken:** Step 3.1, the right gripper, closed, on the inner face near the hinge pushes the
  door round steadily in one smooth move and stops it in front of the mouth.
* **Coaching note:** right hand closed, slow and steady. A fast door bounces open.

**Violation: Door not pressed shut**

* **Visible cue:** the episode goes on with the door open or not latched, a gap or cloth shows along its
  edge, the door springs back when the right gripper comes off, or the press is made with the gripper
  open, at an angle, on the door glass, or by the left gripper.
* **SOP rule broken:** Step 3.2, the right gripper, closed, presses the door's front face flat and
  straight back at the free edge, holds the press for 2 seconds, and the door sits flush with the latch
  holding.
* **Coaching note:** flat face, straight back, hold two seconds, then look before you move away.

**Violation: Dial turned wrongly or not set**

* **Visible cue:** the dial is turned by the right gripper, turned counterclockwise from OFF, pulled or
  pushed instead of turned, or left on OFF or between two clicks.
* **SOP rule broken:** Step 4, the left gripper turns the knob clockwise off OFF onto a program.
* **Coaching note:** turn it, then look that it sits on a program.

**Violation: Start pressed wrongly or not pressed**

* **Visible cue:** Start is pressed before the dial is set, pressed by the right gripper,
  pressed with the gripper open, pressed at an angle or hit, pressed more than twice, or never pressed,
  or another button is pressed.
* **SOP rule broken:** Step 5, the left gripper, closed, presses Start straight in once the dial is set,
  holds for 1 second, and presses once more only if the machine has not started.
* **Coaching note:** dial first, then one straight press with a closed gripper. Check it started.

**Violation: Idle gripper in the way**

* **Visible cue:** the gripper not working hangs over the hamper, the check spot, the mouth, the door, or
  the control panel while the other gripper works there, or the two grippers touch.
* **SOP rule broken:** Steps 1 to 5, the gripper not named in a bullet waits clear of the work.
* **Coaching note:** if your hand is not working, it is out of the way.

**Violation: Correction made without looking at the check**

* **Visible cue:** a step's check is skipped: the episode moves on with the door not open wide, a garment
  on the rubber ring, a pocket not looked into, the tissue on the table, the door not latched, or the
  dial between clicks, and nothing is fixed.
* **SOP rule broken:** Steps 1, 2.2, 2.3, 3.2, and 4, each check is looked at before the next stage
  begins, and a bad result is fixed the way the step says.
* **Coaching note:** look at it before you reach for the next thing. Fix it now, not at the end.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a garment still in the hamper, the door open, the dial not
  set, the machine not started, or an arm away from home.
* **SOP rule broken:** Step 6, look once across the station, return both arms home, then stop recording.
* **Coaching note:** one look, then home. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode,
and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake that lets go on its own, or a wheel that sticks so the base cannot be parked
  straight.
* **Bad object:** a torn or damp garment, a pocket sewn shut, or a torn tissue. Replace it before the
  next episode.
* **Machine or station fault:** a door that will not stay open on its own, or will not latch under a flat
  press, a dial that does not click, a machine that does not start with a correct press, or a table that
  slides under a correct set-down.

## Annotation subtasks (from SOP)

1. Swing the door open with the right gripper
2. Take the top garment out of the hamper
3. Hand a garment between the grippers
4. Pull a pocket open and look inside
5. Exchange arms for a pocket the left gripper cannot get at
6. Take the tissue out and drop it in the pocket dish
7. Lay one garment in the drum with the right gripper
8. Push the door round with the right gripper closed
9. Press the door shut with the right gripper closed
10. Set the dial with the left gripper
11. Press Start with the left gripper closed
12. Return both arms home and end the episode
