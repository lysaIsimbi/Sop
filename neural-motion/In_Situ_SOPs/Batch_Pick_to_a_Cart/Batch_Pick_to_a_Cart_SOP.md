# Batch-Pick to a Cart SOP (1x Episode: one six-line batch, in situ)

One episode picks one six-line batch for four orders into one pick cart, at the shelf bays where the stock lives. The base is
**passive**: it has no drive of its own, so it is pushed by hand to the front of the bays and locked there, and it never moves. The
**cart** is what travels: it runs on a short track in front of the bays, and the arms push it from stop to stop. Everything the episode
touches is already there when recording starts: the stocked bins, the cart at its START stop with its empty order slots, its scanner, and
its pick list.

The episode runs these four actions in this order and no other: **push the cart along the bays, pick to the partitioned slots by order,
scan each item, park the cart at the pack handoff.** Each item is scanned straight after it comes out of its bin, before it goes into its
slot. The cart never moves while an item or a gripper is over a bin or a slot.

The bays are worked **as found**. The **pick cart** stands on its track at the **START** stop at one end, with its **slot tray** divided into
four empty **order slots**, A, B, C, and D. Each of the eight bins holds three units of one SKU. The **pick list** sits in its clip on the cart.
The episode ends with each picked item in the slot its line names, every pick scanned green, and the cart standing at the **PACK** stop at the
other end, its brake on.

**The pick list sets the order.** It is printed in walk order: the lines for the first bay the cart reaches come first, then the lines for the
second bay. Each line names a **bin**, the item's **SKU**, the **order slot** it goes to, and the quantity, which is always one. Which bins and
which slots change from episode to episode, so the list is read every time and never worked from memory.

**This is an in-situ task, and three things follow from that.** First, **each shelf level has a shelf directly above it**, so **every reach into
a bin is from the front, straight in, level**, over the cart. Second, the **shelving, the track, and the cart are never leaned on**: the cart is
pushed only by its end handle, and nothing rests on a shelf, an upright, a bin, the track, or the slot tray. Third, **each item goes from its bin
to its slot and nowhere else**: nothing is set down on a shelf edge, the cart deck outside the tray, the track, or the floor on the way.

The bays are set up in one of two ways. Only the **direction of the walk** changes. The bays, the bins, and the track are in the same place in
both, and the START and PACK signs swap ends.

* **Config L:** the pack handoff is at the **left end**. The cart starts at the right end and walks **right to left**: Bay 2 first, then Bay 1.
* **Config R:** the pack handoff is at the **right end**. The cart starts at the left end and walks **left to right**: Bay 1 first, then Bay 2.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says so on an **IF** line.
Look at the PACK sign and follow the line that matches.

What stays constant across all sessions:

* **Bay rule:** the **left gripper** picks from **Bay 1** and the **right gripper** from **Bay 2**. The gripper that picks an item scans it and
  sets it in its slot.
* **Push rule:** the gripper at the end the cart comes from pushes the cart every time, by the handle on that end, and sets the brake at PACK. It is
  called the **pushing gripper**: the **right gripper** in Config L and the **left gripper** in Config R.
* **Still-cart rule:** the cart moves only when both grippers are empty and out of every bin and slot, and nothing is picked until the cart stands
  at its stop.

Nothing is ever handed over. **The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches
over, under, around, or past the other. Nothing is moved two at a time: one gripper holds one item or pushes the cart, and the other gripper is
empty and clear of the bays.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or repositioned once
recording starts. It is parked once, before recording, and does not move again until the episode is over.

1. Push the base by hand up to the front of the track deck and stop it **square to the bays**, so the track and the shelf edges run straight across
   the frame of the camera.
2. Stop it **centered on the bays**, so the middle of the base is in line with the middle upright between Bay 1 and Bay 2.
3. Stop it **close enough** that both grippers reach over the cart into the back of a bin straight in and level without either arm extending, and
   **far enough** that neither arm, wrist, nor any part of the base touches the deck, the track, the cart, or the shelving while both arms work.
4. Check the **left side**: with the cart at STOP 1, the **left gripper** reaches all four Bay 1 bins over it, every order slot, and the cart
   scanner, all without extending.
5. Check the **right side**: with the cart at STOP 2, the **right gripper** reaches all four Bay 2 bins over it, every order slot, and the cart
   scanner, all without extending.
6. Check the **push** for the config this episode runs: the **pushing gripper** reaches the cart's trailing handle at every stop, START to PACK, and
   the brake lever at PACK.
7. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
8. If any of lines 1 to 6 fails, push the base to a new park by hand and start again at line 1. Do not work bays the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Only the cart moves. Nothing moves the base: no arm leans on the shelving or the cart hard
enough to shift it, nothing touches it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the middle upright and its frame includes both bays, the whole track from end stop to end stop with all four
   stop lines and signs, and the cart with its slot tray, scanner, and pick list.
3. The camera reads every **bin label**, the **SKU label** on the front unit of every bin, and the **slot letters** on the tray.
4. The camera reads the **pick list** in its clip well enough to follow its lines.
5. The camera sees the **scanner light**, and sees the cart's leading end against each stop line.
6. Both arms are at home with grippers open.
7. The **left arm** reaches all of Bay 1 and the tray with the cart at STOP 1, and the **right arm** all of Bay 2 and the tray with the cart at STOP 2,
   without extending to a joint limit.
8. The pushing arm for this config reaches the trailing handle at every stop and the brake lever at PACK without extending to a joint limit.
9. Both grippers come into every bin **from the front and level**, over the cart, and neither wrist nor forearm touches the shelf above or the cart.
10. The two arms do not collide, and neither arm passes in front of the other.
11. If a place cannot be reached, re-park the base by the Base positioning steps until lines 7 to 10 hold.

### Materials checklist

1. The **shelving** stands where it lives, fixed to the wall or the floor. It is not moved, not leaned on, and not pushed at any point. It has two
   bays side by side, **Bay 1** on the left and **Bay 2** on the right, with a **middle upright** between them.
2. Each bay has **two levels**, each with a shelf directly above it, and each level holds **two fixed open-front bins**. That makes eight bins,
   named by bay, level, and slot, left to right: **1-A1, 1-A2, 1-B1, 1-B2** in Bay 1 and **2-A1, 2-A2, 2-B1, 2-B2** in Bay 2. Each bin has a
   **bin label** on the shelf edge right below it.
3. Each bin holds **three units of one SKU** in a row from front to back, standing upright, SKU label up and facing out. Every unit is a small boxed
   item that fits one gripper. No two bins hold the same SKU.
4. The **track deck** is a raised deck in front of the shelving, between the base and the bins, with a straight two-rail **track** running left to
   right along it. Its surface is below the bottom level of bins, so the arms reach over a cart on the track into every bin.
5. The track has an **end block** at each end and four painted **stop lines** across it, left to right: the left end, **STOP 1** in front of Bay 1,
   **STOP 2** in front of Bay 2, and the right end. A sign reading **START** stands at one end and a sign reading **PACK** at the other:
   * **Config L:** PACK at the left end, START at the right end;
   * **Config R:** PACK at the right end, START at the left end.
6. The **pick cart** is a short, low wheeled cart that runs on the track. It has an upright **handle** at each end, a **brake lever** on its deck
   beside the handle at each end (down is on, up is off), and on its deck:
   * the **slot tray**: an open tray divided by fixed walls into four **order slots** in a row along the cart, **A, B, C, D**, left to right, each
     with its letter in large print on its front wall and room for two units standing;
   * the **cart scanner**: fixed on a short post at the back middle of the cart, window facing the base. It reads a barcode by itself when the
     barcode is held about a hand in front of its window: a **green** light and one beep if the SKU is the one the current line names, a **red**
     light and a buzz if it is not;
   * the **pick list** in a clip on the scanner post, facing the camera.
7. At the start, the cart stands at the **START** end, its end against the end block, brakes off, every slot empty.
8. The **pick list** has a section for each bay, the first bay of the walk first. Each section has **three lines**. Each line reads bin, SKU, slot,
   quantity 1. The six lines use at least three different slots, and no slot gets more than two items.
9. The cart rolls freely along the track with a light push and stops when the push stops.
10. Nothing else stands on the deck, the track, or the cart within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the stop lines, the end signs, the bin labels, and the slot letters.

* **Shelving:** the fixed bays behind the track. Never moved, never leaned on, never pushed.
* **Bay 1:** the left bay, four bins. **Left gripper only.**
* **Bay 2:** the right bay, four bins. **Right gripper only.**
* **Track deck:** in front of the shelving, with the track, the four stop lines, the end blocks, and the START and PACK signs.
* **Pick cart:** on the track, with the slot tray, the cart scanner, and the pick list. Its tray and scanner are used by the gripper picking at its
  bay; its trailing handle and brake by the **pushing gripper** only.

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** picks Bay 1 and the **right gripper** picks Bay 2. The **pushing gripper** also pushes the cart and sets the brake.
* Neither arm goes into a bin in the other bay, and neither reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds one item or pushes the cart, and while it does, the other gripper is empty and drawn **clear of
  the bays**.

### Arm assignments

* **Pushing gripper** (**right gripper** in Config L, **left gripper** in Config R). Pushes the cart from each stop to the next by the handle at the
  end it comes from, picks its own bay's lines, and sets the brake at PACK.
* **Other gripper.** Picks its own bay's lines.
* **Picking gripper** (the gripper of the current line's bay). Takes the unit, scans it, and sets it in its slot.
* Nothing is handed over.

## Vocabulary

* **Batch pick:** picking the items of several orders in one walk, sorting them into one slot per order as you go.
* **Pick list:** the card in the clip on the cart. It is read top to bottom, in walk order.
* **Current line:** the top line not yet picked, scanned green, and set in its slot.
* **Order slot:** one section of the slot tray, holding one order's items. It is named by the letter on its front wall.
* **Walk:** the cart's trip along the track, START to PACK, stopping at each bay.
* **At the stop:** the cart's leading end is on the stop line, the cart square on the track, still.
* **Trailing handle:** the handle at the end of the cart the cart is moving away from.
* **Push:** the pushing gripper closes on the trailing handle and moves the cart along the track, slowly and evenly, keeping it on the rails, until
  its leading end is on the next stop line, then opens and draws back.
* **Front unit:** the unit nearest the front of its bin. It is the only unit ever taken.
* **Front approach:** the gripper comes in and goes out of a bin level and from the front, over the cart, and never comes down into a bin from above.
* **Scan:** straight after the unit comes out of its bin, the picking gripper holds its SKU label about a hand in front of the cart scanner window,
  still, until the light shows. The scanner is never touched.
* **Set item:** the item stands upright on the floor of its order slot, SKU label up, beside any item already there, and stays put when the gripper
  opens.
* **Parked:** the cart stands at the PACK end, its end against the end block, square on the track, with the brake lever at that end pushed down.
* **Clear of the bays:** the arm is drawn back so that no part of it is over the cart or in front of a bin.

## Steps

Run Steps 1 to 5 in order, and end the episode with Step 6. Steps 1 and 3 push the cart, Steps 2 and 4 pick one bay each, and Step 5 parks the cart.
The config decides the walk direction and the pushing gripper, and so which bay is first.

### Step 1: Push the cart to the first bay

**Goal:** the cart stands **at the stop** in front of the first bay of the walk.

* **IF Config L:** the **right gripper** is the pushing gripper and the first stop is **STOP 2** (Bay 2). **IF Config R:** the **left gripper** is the
  pushing gripper and the first stop is **STOP 1** (Bay 1).
* With the other gripper, stay open and **clear of the bays**.
* With the **pushing gripper**, close on the **trailing handle** and **push** the cart along the track until its leading end is on the first stop line.
* With the **pushing gripper**, open and draw back **clear of the bays**.

**Check:** the cart is **at the stop**, square on the track, and the slot tray and pick list have not shifted. If it stopped short or ran past, close on
the trailing handle with the **pushing gripper** and move it onto the line.

### Step 2: Pick the first bay's lines

**Goal:** the three lines of the first bay are each picked, scanned green, and **set** in their slots.

Run 2.1 to 2.4 for each line of the first bay's section, top to bottom.

#### 2.1 Read the current line

* Read the **current line** on the pick list: its bin, SKU, and slot.
* Find the bin whose **bin label** matches it, and check the SKU label on its front unit. Find the slot letter on the tray.
* The line's bay decides the **picking gripper**: the **left gripper** for Bay 1 and the **right gripper** for Bay 2.

**Check:** one bin matches the line and its front unit carries the line's SKU. If no bin matches, stop and log a system issue.

#### 2.2 Take the front unit

* With the **picking gripper**, come level into the bin from the front, over the cart, just above the bin floor, and close on the two sides of the
  **front unit**.
* With the **picking gripper**, lift it just clear of the bin floor and draw it straight out to the front, level, touching no other unit.
* With the other gripper, stay open and **clear of the bays**.

**Check:** the picking gripper holds one unit by its sides, and the units left in the bin still stand in their row.

#### 2.3 Scan the unit

* With the **picking gripper**, hold the unit's SKU label about a hand in front of the cart scanner window, still, until the light shows.
* **IF green:** go on to 2.4.
* **IF red:** with the **picking gripper**, set the unit back at the front of its bin, SKU label up and out, then draw straight out. Read the line
  again and go back to 2.1.

**Check:** the scan was green, the unit never touched the scanner, and the cart has not moved.

#### 2.4 Set the unit in its slot

* With the **picking gripper**, carry the unit level to above the order slot the line names.
* With the **picking gripper**, bring it straight down to just above the slot floor and set it down upright, SKU label up, beside any item already
  there.
* With the **picking gripper**, open and lift straight up and **clear of the bays**.

**Check:** the unit is **set** in its slot. If it has tipped, close on it with the **picking gripper** and stand it up in the same slot.

**Expected state:** the first bay's three items are in their slots, each scanned green, and both grippers are clear.

### Step 3: Push the cart to the second bay

**Goal:** the cart stands **at the stop** in front of the second bay of the walk.

* Check both grippers are empty and **clear of the bays**.
* **IF Config L:** the next stop is **STOP 1** (Bay 1). **IF Config R:** the next stop is **STOP 2** (Bay 2).
* With the **pushing gripper**, close on the **trailing handle** and **push** the cart until its leading end is on that stop line, slowly enough that no
  item in the tray tips.
* With the **pushing gripper**, open and draw back **clear of the bays**.

**Check:** the cart is **at the stop** and every item in the tray still stands. If an item has tipped, stand it up in its slot with the gripper on its
side of the cart.

### Step 4: Pick the second bay's lines

**Goal:** the three lines of the second bay are each picked, scanned green, and **set** in their slots.

* Run 2.1 to 2.4 for each line of the second bay's section, top to bottom, with the **picking gripper** for that bay.

**Check:** all six items are in their slots, each in the slot its line names, each scanned green, and every line on the list is done.

### Step 5: Park the cart at the pack handoff

**Goal:** the cart is **parked** at PACK.

* Check both grippers are empty and **clear of the bays**.
* With the **pushing gripper**, close on the **trailing handle** and **push** the cart slowly until its leading end touches the **end block** at the PACK
  end.
* With the **pushing gripper**, open, then close again and push the **brake lever** at the trailing end straight down until it clicks.
* With the **pushing gripper**, draw back **clear of the bays**.

**Check:** the cart is **parked**: against the PACK end block, square, brake down, every item still standing in its slot. If the cart is short of the block,
lift the brake with the **pushing gripper**, push the cart on, and set the brake again.

### Step 6: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the batch picked and parked.

* Look once across the bays and the cart: every line's item stands in its slot, and the cart is parked at PACK with its brake down.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the batch is picked and at the pack handoff, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take each item out of the slot tray and stand it back at the front of the bin its SKU belongs to, so every bin holds three units in an upright row.
2. Lift the brake and roll the cart to the START end for the next episode's config. Swap the START and PACK signs if the config changes.
3. Put a new pick list in the clip, printed in that config's walk order, with lines and slots changed.
4. Check the cart rolls freely, the scanner still lights, and every slot is empty.
5. Pick up anything that landed on a shelf, the deck, the track, or the floor.
6. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the reviewer sees. The coaching note is for
retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the shelving shifts in frame, the track changes angle or size in frame, or the base rolls, creeps, or turns at any point after recording starts.
* **SOP rule broken:** Steps 1 to 6, the base is parked and locked before recording and stays still. Only the cart moves.
* **Coaching note:** park it, lock it, push-test it, then start recording. The cart walks, the base does not.

**Violation: Approached from above or fouled the shelf**

* **Visible cue:** a gripper comes down into a bin from above instead of coming in level from the front, or a wrist, forearm, or unit knocks the shelf above a bin or
  rests on the cart on the way in.
* **SOP rule broken:** Step 2.2, every reach into a bin is a front approach, level, over the cart, straight in and straight out.
* **Coaching note:** over the cart, level into the bin, out the same way.

**Violation: Leaned on the shelving, track, or cart**

* **Visible cue:** a gripper, wrist, or forearm rests on a shelf, an upright, a bin, the track, the deck, or the slot tray, or a bin shifts.
* **SOP rule broken:** Steps 1 to 5, the shelving, the track, and the cart carry no weight from the arms, and the cart is moved only by its handle.
* **Coaching note:** the arm holds itself up. The handle is the only place to push.

**Violation: Cart pushed wrong**

* **Visible cue:** the cart is pushed by the slot tray, a slot wall, the scanner post, or an item; it is pulled instead of pushed; it is jerked, so items tip; it
  comes off a rail; or it is lifted.
* **SOP rule broken:** Steps 1, 3, and 5, push the cart by its trailing handle, slowly and evenly, keeping it on the rails.
* **Coaching note:** trailing handle, slow and even. The orders ride in that tray.

**Violation: Picked away from the stop**

* **Visible cue:** a unit is picked while the cart stands short of or past its stop line, or before the cart is still.
* **SOP rule broken:** Steps 1 and 3, the cart stands at the stop in front of the bay before any pick from that bay.
* **Coaching note:** park on the line, then pick. A cart off its stop puts the slots out of reach.

**Violation: Cart moved during a pick**

* **Visible cue:** the cart is pushed while a gripper holds an item, is in a bin, or is over the tray; or the cart is knocked along the track by a pick.
* **SOP rule broken:** Steps 1, 3, and 5, the cart moves only when both grippers are empty and clear of every bin and slot.
* **Coaching note:** hands empty and out, then push.

**Violation: Pick list not followed**

* **Visible cue:** a line is skipped, lines are taken out of top-to-bottom order, a line of the second bay is picked at the first, or a bin is reached into that is
  not on the current line.
* **SOP rule broken:** Steps 2.1 and 4, read the list top to bottom in walk order, one current line at a time.
* **Coaching note:** read the line, then move. The list is the walk.

**Violation: Wrong bin**

* **Visible cue:** a unit is taken from a bin other than the one the current line names.
* **SOP rule broken:** Step 2.1, find the bin whose label matches the line before the arm goes in.
* **Coaching note:** match the label under the bin to the line. Bins that look alike are not the same bin.

**Violation: Wrong quantity**

* **Visible cue:** a gripper comes out of a bin with two units, or a line ends with no unit or two units in the tray.
* **SOP rule broken:** Steps 2.2 to 2.4, every line is quantity one: one unit out, one unit in.
* **Coaching note:** one line, one unit.

**Violation: Unit taken or held wrong**

* **Visible cue:** a unit other than the front unit is taken; units left in the bin are knocked or dragged; or a unit is held by its top, label, or one corner, or with
  its SKU label covered at the scanner.
* **SOP rule broken:** Step 2.2, close on the sides of the front unit, lift it just clear, and draw it straight out.
* **Coaching note:** front unit, sides in the gripper, label free.

**Violation: Scan skipped or done out of turn**

* **Visible cue:** a unit goes into a slot without a scan, or before the green light; or the next line is read before the last unit is set.
* **SOP rule broken:** Step 2.3, scan each unit straight after it leaves its bin, and wait for green before it goes to its slot.
* **Coaching note:** pick, scan, green, then the slot.

**Violation: Red scan ignored**

* **Visible cue:** a red light and buzz is followed by the unit going into a slot, or the same unit is held up again and again until the operator moves on.
* **SOP rule broken:** Step 2.3, on red, set the unit back at the front of its bin, read the line again, and pick again.
* **Coaching note:** red means the wrong thing is in the gripper. Fix the pick, not the scan.

**Violation: Scanner handled or knocked**

* **Visible cue:** a unit or gripper bumps the cart scanner or its post, the post is used to push the cart, or the pick list is knocked out of its clip.
* **SOP rule broken:** Step 2.3, hold the unit a hand in front of the scanner window; the scanner is never touched.
* **Coaching note:** bring the label to the scanner and stop a hand short.

**Violation: Wrong slot**

* **Visible cue:** a unit is set in a slot other than the one its line names, including the slot next to it.
* **SOP rule broken:** Step 2.4, each unit goes into the order slot its line names.
* **Coaching note:** read the slot letter on the line, find it on the tray, then set. The slot next door is another order.

**Violation: Unit dropped in or not set**

* **Visible cue:** a unit is let go from above the slot floor and falls in, lies on its side, rests on a slot wall, or stands on another item.
* **SOP rule broken:** Step 2.4, bring each unit straight down to just above the slot floor and set it upright before opening.
* **Coaching note:** down to the floor, then open.

**Violation: Cart not parked**

* **Visible cue:** the episode ends with the cart short of the PACK end block, crooked on the track, at the START end, or with its brake up; or the brake is pushed
  at the wrong end.
* **SOP rule broken:** Step 5, push the cart against the PACK end block and push the brake lever at the trailing end down until it clicks.
* **Coaching note:** block, then brake. A cart that rolls is not handed off.

**Violation: Config misaligned**

* **Visible cue:** the cart is pushed the wrong way along the track; the second bay is picked first; the gripper at the leading end pushes or brakes; or a sign is moved
  before or during the episode.
* **SOP rule broken:** Steps 1, 3, and 5, look at the PACK sign and follow the IF line that matches the config the episode is set up in.
* **Coaching note:** find PACK before the cart moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** a unit is picked before the cart reaches its bay; the cart leaves a bay before all its lines are done; or the cart is parked before all six lines are done.
* **SOP rule broken:** Steps 1 to 5, push to the first bay, pick it, push to the second, pick it, then park.
* **Coaching note:** the order is the task. Each bay is finished before the cart moves on.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two units; both grippers carry units at the same time; or the cart is pushed by one gripper while the other holds a unit.
* **SOP rule broken:** Steps 1 to 5, one gripper holds one item or pushes the cart, and the other is empty and clear of the bays.
* **Coaching note:** one thing, one move.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a cart off its stop line, a tipped item in the tray, or
  a brake left up.
* **SOP rule broken:** Steps 1 to 5, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a unit is dropped on the cart deck, the track, a shelf, or the floor; an item in the tray is knocked out of its slot; or a unit in a bin is knocked over.
* **SOP rule broken:** Steps 2 to 5, nothing is dropped or knocked out of its place, and every gripper comes out the way it went in.
* **Coaching note:** check the path and the landing place before the arm moves.

**Violation: Wrong arm used**

* **Visible cue:** the **left gripper** goes into a Bay 2 bin; the **right gripper** goes into a Bay 1 bin; the gripper at the leading end pushes the cart; or either arm passes
  in front of the other.
* **SOP rule broken:** Steps 1 to 5, each gripper picks its own bay, only the pushing gripper pushes and brakes, and the arms never cross.
* **Coaching note:** Bay 1, left arm. Bay 2, right arm. The trailing side pushes.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a line not picked, an item in the wrong slot, a pick not scanned green, the cart not parked, an arm short of home, or a gripper not
  fully open.
* **SOP rule broken:** Step 6, look once across the bays and the cart, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a bin label, an SKU label, a slot letter, the pick list, the scanner light, or the cart against a stop line**, so the picks, the slots, or the stops
  cannot be judged.
* **Scanner fault:** no light on a correctly held label, a green on a wrong SKU, or a red on the right one.
* **Cart or track fault:** the cart binds, will not roll with a light push, rolls on its own, comes off a rail by itself, or its brake will not hold.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **List or stock fault:** a line with no matching bin, a bin holding the wrong SKU, or a list not printed in the walk order of the config.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a bin, a slot, the scanner, a handle, or the brake cannot be reached without
  extending or folding the arm.

## Annotation subtasks (from SOP)

1. Push the cart to a stop line by its trailing handle
2. Read one pick-list line
3. Take the front unit out of a bin, over the cart
4. Scan one unit at the cart scanner
5. Set one unit back in its bin after a red scan
6. Set one unit in its order slot
7. Push the cart against the PACK end block
8. Push the brake lever down
9. Return both arms home and end the episode
