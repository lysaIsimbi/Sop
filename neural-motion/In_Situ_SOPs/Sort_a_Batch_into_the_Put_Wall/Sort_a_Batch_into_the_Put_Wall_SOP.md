# Sort a Batch into the Put-Wall SOP (1x Episode: one batch of ten items, in situ)

One episode sorts one batch tote of ten items into the order cubbies of a put-wall, at the put-wall where the cubbies live. The
base is **passive**: it has no drive of its own, so it is pushed by hand to the front of the put-wall and locked there, and nothing
is carried away to a table. Everything the episode touches is already at the put-wall when recording starts: the batch cart with its
tote of items, the six cubbies with their lamps, order cards, and flags, and the scanner in its holster.

The episode runs these four actions in this order and no other: **sort the batch-picked items into the order cubbies, scan each one,
flip the full-order flags, clear the tote.** Each item is scanned before it is sorted, because the scan is what lights its cubby.
Each item is put, confirmed, and its order checked for full before the next item is taken.

The put-wall is worked **as found**. The **batch tote** stands on the top deck of the batch cart, braked against one end of the
put-wall, holding **ten items** picked together for **six orders**. Each cubby belongs to one order and starts empty, its lamp off,
its flag down. The episode ends with every item in its order's cubby, every lamp off, every flag flipped up to **FULL**, and the empty
tote on the cart's lower deck.

**The put-wall decides where each item goes.** An item is held up to the scanner, and the lamp on its order's cubby lights. That lamp
is the only thing that says where the item goes. The **order card** on each cubby says how many items the order needs. When the cubby
holds that many, the order is full and its flag is flipped.

**This is an in-situ task, and three things follow from that.** First, **each row of cubbies has another row or the top of the wall
directly above it**, so **every reach into a cubby is from the front, straight in, level**. No gripper comes down into a cubby from
above. Second, the **put-wall and the cart are never leaned on and never pushed**: no gripper, wrist, or forearm rests on a cubby, an
upright, or the cart. Third, **each item goes from the tote to its lit cubby and nowhere else**: nothing is set down on a cubby lip,
another cubby, the cart deck, or the floor on the way.

The put-wall is set up in one of two ways. Only the **batch cart** moves. The cubbies, the lamps, the flags, and the scanner are in the
same place in both.

* **Config L:** the batch cart stands against the **left end** of the put-wall.
* **Config R:** the batch cart stands against the **right end** of the put-wall.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says so on an
**IF** line. Look at the put-wall and follow the line that matches. Which items the tote holds and which order each belongs to also
change from episode to episode, but they are not a config: the scan shows them.

What stays constant across all sessions:

* **Column rule:** the **left gripper** puts into the **left column** (A1, B1, C1) and the **right gripper** into the **right column**
  (A2, B2, C2). The gripper that puts an item confirms it and flips that cubby's flag.
* **Cart-side rule:** the gripper on the cart's side takes every item out of the tote, scans it, and clears the tote. That is the **left
  gripper** in Config L and the **right gripper** in Config R. It is called the **cart gripper**.
* **Hand-over rule:** when an item's lit cubby is in the column away from the cart, the cart gripper scans it and then **hands it over**
  to the other gripper at the **hand-over point**. No arm reaches across the put-wall.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches over, under, around,
or past the other. Nothing is moved two at a time: one gripper holds one item, and the other gripper is empty, taking a hand-over, or
clear of the put-wall.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or repositioned
once recording starts. It is parked once, before recording, and does not move again until the episode is over.

1. Push the base by hand up to the put-wall and stop it **square to its front**, so the cubby rows run straight across the frame of the
   camera.
2. Stop it **centered on the put-wall**, so the middle of the base is in line with the middle upright between the two columns.
3. Stop it **close enough** that both grippers reach the back of a cubby straight in and level without either arm extending, and **far
   enough** that neither arm, wrist, nor any part of the base touches the put-wall or the cart while both arms work.
4. Check the **height band**: both grippers come level into every cubby on rows A, B, and C without a wrist or forearm touching the cubby
   roof above it.
5. Check the **left side**: the **left gripper** reaches the back of A1, B1, and C1, each one's lamp button and flag, and the hand-over
   point, all without extending.
6. Check the **right side**: the **right gripper** reaches the back of A2, B2, and C2, each one's lamp button and flag, and the hand-over
   point, all without extending.
7. Check the **cart** for the config this episode runs: the **cart gripper** reaches every item in the tote, the scanner window, the
   hand-over point, and the cart's lower deck.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not work a put-wall the arms cannot
   reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the put-wall hard enough to shift it,
nothing touches it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the middle upright and its frame includes all six cubbies with their lamps, order cards, and
   flags, the scanner and its light, and the cart with the tote and the lower deck.
3. The camera reads every **cubby label**, every **order card**, and the **item label** on every item, so which item went into which
   cubby is readable.
4. The camera sees every **cubby lamp** and every **flag**, so which lamp is lit and which flags are up is readable at every moment.
5. The camera sees into the tote well enough to count the items left in it.
6. Both arms are at home with grippers open.
7. The **left arm** reaches all of the left column, its lamps and flags, and the hand-over point without extending to a joint limit.
8. The **right arm** reaches all of the right column, its lamps and flags, and the hand-over point without extending to a joint limit.
9. The cart arm for this config reaches the whole tote, the scanner window, and the lower deck without extending to a joint limit.
10. Both grippers come in and go out of every cubby **from the front and level**, and neither wrist nor forearm touches the cubby roof on
    the way in or out.
11. The two arms do not collide, and neither arm passes in front of the other.
12. If a place cannot be reached, re-park the base by the Base positioning steps until lines 7 to 11 hold.

### Materials checklist

1. The **put-wall** stands where it lives, fixed to the wall or the floor. It is not moved, not leaned on, and not pushed at any point.
2. It is a grid of **six open-front cubbies** in **three rows** and **two columns**: **A1, A2** in the top row, **B1, B2** in the middle
   row, **C1, C2** in the bottom row, numbered left to right. A **middle upright** splits the left column from the right column. Each
   cubby has a roof: the floor of the cubby above it, or the top of the wall.
3. Each cubby is big enough for three items standing side by side on its floor. Each has a **cubby label** on its front lip with its
   name in large print.
4. Each cubby has a **lamp** on its front lip, left of the label: a small light with a push button in it. After a scan it lights on the
   cubby the item belongs to. Pressing it turns it off (**unvalidated**: the mock must link the scanner to the lamps).
5. Each cubby has an **order card** in a holder on its front lip, right of the label, saying how many items its order needs: **1**, **2**,
   or **3**. The six cards add up to ten.
6. Each cubby has a **flag** hinged at the top of its front, on the right: a small paddle that hangs down showing **OPEN** and, pushed up
   until it clicks, stands up showing **FULL** in red. Every flag starts down.
7. Every cubby starts empty, its lamp off, its flag down.
8. The **scanner** stands fixed in its **holster** on the middle upright between row B and row C, window facing out. It stays in its
   holster for the whole episode. It reads a barcode by itself when the barcode is held about a hand in front of its window, beeps, and
   lights the lamp of the item's cubby.
9. The **batch cart** is a two-deck cart standing braked against the **left end** of the put-wall in **Config L** and against the **right
   end** in **Config R**, its top deck at about the height of row C.
10. On its top deck stands the **batch tote**, an open tote holding **ten items** standing upright in two rows, clear of each other, item
    label up. Every item is small enough for one gripper, with its barcode and item label on its top face. Which items, and which order
    each belongs to, change per episode.
11. The cart's **lower deck** is empty. It is where the empty tote goes.
12. Nothing else stands on the put-wall or the cart within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the cubby labels. You judge every other place by eye against the put-wall itself.

* **Put-wall:** the fixed wall the base is parked at. Never moved, never leaned on, never pushed.
* **Left column:** A1, B1, C1, with their lamps and flags. **Left gripper only.**
* **Right column:** A2, B2, C2, with their lamps and flags. **Right gripper only.**
* **Scanner:** fixed in its holster on the middle upright. **Cart gripper only.**
* **Hand-over point:** in front of the middle upright, a hand out from the front of row B.
* **Batch cart:** braked against the left end (Config L) or the right end (Config R) of the put-wall: batch tote on the top deck, empty
  lower deck. **Cart gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the left column and the **right gripper** works the right column. The **cart gripper** also works the cart
  and the scanner.
* The two arms meet only at the **hand-over point**.
* Neither arm goes into a cubby in the other column, and neither reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds one item, and while it does, the other gripper is empty, taking a hand-over, or drawn
  **clear of the put-wall**.

### Arm assignments

* **Cart gripper** (**left gripper** in Config L, **right gripper** in Config R). Takes every item out of the tote, scans it, puts the items
  for its own column, hands over the items for the other column, and moves the empty tote to the lower deck.
* **Other gripper.** Takes each hand-over and puts the item in its lit cubby.
* **Putting gripper** (the gripper of the lit cubby's column). Puts the item, presses the lamp off, and flips the flag when the order is
  full.
* Only items are handed over. The tote is never handed over, and the scanner never leaves its holster.

## Vocabulary

* **Put-wall:** a wall of cubbies, one per order, that a batch of items is sorted into.
* **Batch tote:** the tote of items picked together for several orders at once.
* **Order cubby:** one cubby, holding the items of one order.
* **Next item:** of the items still in the tote, the one nearest the put-wall. If two are as near, the one nearer the middle upright.
* **Scan:** the cart gripper holds the item's barcode about a hand in front of the scanner window, still, until it beeps and a lamp lights.
  The scanner is never touched.
* **Lit cubby:** the cubby whose lamp came on after the scan. It is the only place the item may go.
* **Putting gripper:** the gripper of the lit cubby's column, the **left gripper** for A1, B1, C1 and the **right gripper** for A2, B2, C2.
* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down into a cubby from above.
* **Put item:** the item stands on the cubby floor, upright, item label up, back against the back wall of the cubby, beside any item
  already there and not on top of it, and stays put when the gripper opens.
* **Confirm:** after the put, the putting gripper presses the lit lamp's button once, straight in, until the lamp goes off.
* **Full order:** the number of items in the cubby equals the number on its order card.
* **Flip the flag:** the putting gripper pushes the flag paddle up from below until it clicks and stands up, showing FULL.
* **Hand over:** the cart gripper brings the scanned item to the hand-over point and holds it still for a **half-second hold**. The other
  gripper then closes on the far side of it. Only after the other gripper is closed does the cart gripper open and draw back.
* **Clear of the put-wall:** the arm is drawn back so that no part of it is in front of a cubby, the scanner, or the cart.

## Steps

Run Steps 1 to 3 once for each of the ten items, then Step 4 once, and end the episode with Step 5. Each item is scanned, put, confirmed,
and checked for a full order before the next item is taken. The column of the lit cubby decides the putting gripper, and the config decides
the cart gripper and the hand-overs.

### Step 1: Take and scan the next item

**Goal:** the cart gripper holds the next item and its cubby's lamp is lit.

#### 1.1 Take the next item

* **IF Config L:** the **left gripper** is the cart gripper. **IF Config R:** the **right gripper** is the cart gripper.
* Find the **next item** in the tote.
* With the **cart gripper**, close on the two sides of the next item and lift it straight up out of the tote, touching no other item.
* With the other gripper, stay open and **clear of the put-wall**.

**Check:** the cart gripper holds one item by its sides, barcode up, and the items left in the tote still stand.

#### 1.2 Scan the item

* With the **cart gripper**, carry the item level to the scanner and turn it so its barcode faces the window, about a hand in front of it.
* With the **cart gripper**, hold still until the scanner beeps and a lamp lights.
* Read which cubby is lit, and which column it is in. That column decides the **putting gripper**.

**Check:** exactly one lamp is lit and the scanner still stands in its holster. If no lamp lights, hold the barcode in front of the window
once more with the **cart gripper**. If it still does not light, stop and log a system issue.

**Expected state:** one item is scanned and held, and one lamp is lit.

### Step 2: Put the item in its lit cubby

**Goal:** the item is a **put item** in the lit cubby, and the lamp is off.

#### 2.1 Bring the item to the lit cubby

* **IF the lit cubby is in the cart gripper's own column:** the cart gripper is the putting gripper. With the **cart gripper**, carry the
  item level to the front of the lit cubby.
* **IF the lit cubby is in the other column:** with the **cart gripper**, carry the item to the **hand-over point** and hold it still for a
  **half-second hold**. With the **putting gripper**, close on the far side of the item. With the **cart gripper**, open and draw back
  **clear of the put-wall**. With the **putting gripper**, carry the item level to the front of the lit cubby.

**Check:** the **putting gripper** holds the item by its sides, label up, in front of the lit cubby.

#### 2.2 Put the item

* With the **putting gripper**, bring the item level into the lit cubby from the front, just above its floor.
* With the **putting gripper**, set it down on the cubby floor against the back wall, beside any item already there and touching none,
  upright, item label up.
* With the **putting gripper**, open and draw straight out to the front, level.
* With the **putting gripper**, do not let the item go from above the cubby floor, do not set it on another item, and do not push the items
  already there.

**Check:** the item is a **put item**, and every item already in the cubby still stands where it was. If it has tipped, close on it with the
**putting gripper** and stand it up in its place.

#### 2.3 Confirm the put

* With the **putting gripper**, close, bring it level to the lit lamp, and press its button once, straight in, until the lamp goes off.
* With the **putting gripper**, draw straight back.

**Check:** every lamp on the put-wall is off.

**Expected state:** the item is in its cubby, confirmed, and no lamp is lit.

### Step 3: Flip the flag if the order is full

**Goal:** a cubby whose order is full shows FULL.

* Count the items in the cubby just put into and read its **order card**.
* **IF the count is smaller than the order card:** the order is not full. Leave the flag down and go back to Step 1 for the next item.
* **IF the count equals the order card:** with the **putting gripper**, closed, come level to the underside of the cubby's **flag** and push
  it straight up until it clicks and stands up, showing FULL. Draw the gripper straight back and **clear of the put-wall**.

**Check:** the flag of every full order stands up showing FULL, and the flag of every order that is not yet full hangs down. If a flag has not
clicked up, push it up again with the **putting gripper**.

**Expected state:** the put-wall shows which orders are full. When the tote is empty, all six flags are up.

### Step 4: Clear the tote

**Goal:** the empty batch tote stands on the cart's lower deck, and the top deck is bare.

* Look into the tote: it is empty.
* With the **cart gripper**, close on the rim of the tote at the side nearest the put-wall and lift it just clear of the top deck.
* With the **cart gripper**, bring it straight down and in onto the **lower deck**, set it flat, then open and draw back **clear of the
  put-wall**.
* With the other gripper, stay open and **clear of the put-wall** for the whole of this step.

**Check:** the tote sits flat on the lower deck and the top deck is bare. If the tote rests half off the lower deck, push it straight in with
the **cart gripper**.

**Expected state:** the batch is sorted, every order is flagged full, and the tote is cleared.

### Step 5: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the batch sorted.

* Look once across the put-wall and the cart: each cubby holds as many items as its order card says, every lamp is off, every flag is up,
  and the tote is on the lower deck.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the batch is sorted and still, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take every item out of the cubbies and stand them back in the batch tote, in two rows, clear of each other, label up.
2. Push every flag back down to OPEN and check every lamp is off.
3. Set up the next batch: change which item belongs to which order in the scanner mock, and put the matching order cards in the holders.
   The cards add up to ten.
4. Stand the tote back on the top deck and check the lower deck is empty.
5. Move the cart to the end of the put-wall for the next episode's config and brake it.
6. Check every label is readable and the scanner still beeps and lights lamps.
7. Pick up anything that landed on a cubby lip, the cart, or the floor.
8. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the reviewer sees.
The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the put-wall shifts in frame, the cubby rows change angle or size in frame, or the base rolls, creeps, or turns at any
  point after recording starts.
* **SOP rule broken:** Steps 1 to 5, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Approached from above or fouled the cubby roof**

* **Visible cue:** a gripper comes down into a cubby from above instead of coming in level from the front, or a wrist, forearm, or item
  knocks, scrapes, or rests on the roof of a cubby.
* **SOP rule broken:** Step 2.2, every reach into a cubby is a front approach, level, straight in and straight out.
* **Coaching note:** straight in from the front, straight out the same way.

**Violation: Leaned on or pushed the put-wall or cart**

* **Visible cue:** a gripper, wrist, or forearm rests on a cubby, an upright, or the cart; the put-wall or the cart rocks or moves; or a lamp
  or flag is pressed hard enough to shake the wall.
* **SOP rule broken:** Steps 1 to 4, the put-wall and the cart carry no weight from the arms.
* **Coaching note:** the arm holds itself up. Press only as hard as the button or flag needs.

**Violation: Item taken wrong**

* **Visible cue:** an item other than the next item is taken; two items come out together; the gripper digs under or pushes other items;
  or an item is dragged up the tote wall.
* **SOP rule broken:** Step 1.1, take the next item by its sides and lift it straight up, touching no other item.
* **Coaching note:** nearest first, one at a time, straight up.

**Violation: Item held wrong**

* **Visible cue:** an item is held by its top, its label, or one corner, or held so its barcode is covered at the scanner.
* **SOP rule broken:** Steps 1.1 and 1.2, close on the two sides of the item and keep its barcode free.
* **Coaching note:** sides in the gripper, barcode free for the scanner.

**Violation: Scan skipped or done out of turn**

* **Visible cue:** an item is put without a scan; an item is handed over before it is scanned; an item is put while a lamp from an earlier
  item is still lit; or the next item is taken before the lamp is confirmed off.
* **SOP rule broken:** Steps 1.2 and 2.3, scan each item before it moves toward a cubby, and confirm its lamp off before the next item.
* **Coaching note:** scan, look at the lamp, then move. One lit lamp at a time.

**Violation: Scanner handled or knocked**

* **Visible cue:** a gripper takes the scanner out of its holster, an item or gripper bumps the scanner window, or the scanner is turned or
  knocked in its holster.
* **SOP rule broken:** Step 1.2, hold the item a hand in front of the scanner window; the scanner stays in its holster and is never touched.
* **Coaching note:** bring the barcode to the scanner and stop a hand short.

**Violation: Wrong cubby**

* **Visible cue:** an item is put into a cubby whose lamp is not lit, including the cubby next to it or the one above or below it.
* **SOP rule broken:** Steps 2.1 and 2.2, the item goes into the lit cubby and nowhere else.
* **Coaching note:** follow the light, not the order card and not a guess.

**Violation: Item dropped in or not put**

* **Visible cue:** an item is let go from above the cubby floor and falls in; it lies on its side, stands on another item, rests on the lip,
  or stands short of the back wall; or it blocks the lamp or the flag.
* **SOP rule broken:** Step 2.2, set each item down on the cubby floor, against the back wall, upright, label up, before opening.
* **Coaching note:** down to the floor, back to the wall, then open.

**Violation: Cubby items disturbed**

* **Visible cue:** putting an item pushes, tips, or shoves an item already in the cubby, or an item is knocked out of a cubby.
* **SOP rule broken:** Step 2.2, set the new item beside the items already there, touching none, and do not push them.
* **Coaching note:** find the free space first, then set the item into it.

**Violation: Put not confirmed**

* **Visible cue:** the lamp is left lit after the put; a lamp other than the lit one is pressed; the lamp is pressed before the item is in the
  cubby; or the lamp is pressed several times or with an open gripper.
* **SOP rule broken:** Step 2.3, after the put, press the lit lamp's button once, straight in, with the closed putting gripper.
* **Coaching note:** put, then press. The lamp going off is the record of the put.

**Violation: Hand-over done wrong**

* **Visible cue:** the cart gripper opens before the putting gripper has closed; the item is still moving when the putting gripper closes,
  with no half-second hold; the hand-over happens away from the hand-over point; or an item for the cart's own column is handed over.
* **SOP rule broken:** Step 2.1, hand over only items for the other column, after the scan, at the hand-over point, held still, and open only
  after the putting gripper has closed.
* **Coaching note:** scan, stop, hold still, let the putting gripper take it, then open.

**Violation: Flag not flipped**

* **Visible cue:** a cubby holds as many items as its order card says and its flag is still down when the next item is taken, or at the end.
* **SOP rule broken:** Step 3, count the items against the order card after every put, and flip the flag as soon as the order is full.
* **Coaching note:** after every put, count and compare. Full means flag up, right now.

**Violation: Flag flipped wrong**

* **Visible cue:** a flag is flipped up on a cubby that is not full; the wrong cubby's flag is flipped; a flag is left half up; or a flag
  that is up is pushed back down.
* **SOP rule broken:** Step 3, flip a flag only when its order is full, push it up until it clicks, and never lower it.
* **Coaching note:** count first. A FULL flag sends the order on, so it must be true.

**Violation: Tote not cleared**

* **Visible cue:** the tote is moved while an item is still in it; it is dropped, set on the floor, or left on the top deck; or it rests half off
  the lower deck at the end.
* **SOP rule broken:** Step 4, once the tote is empty, the cart gripper sets it flat on the lower deck.
* **Coaching note:** empty first, then down to the lower deck. A bare top deck is the signal the batch is done.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the put-wall is not set up in: the gripper away from the cart takes an item out of the tote or scans,
  a gripper reaches for a cart end that is empty, or the cart is moved before or during the episode.
* **SOP rule broken:** Steps 1.1, 2.1, and 4, look at the put-wall, find the cart, and follow the IF line that matches the config the episode is
  set up in.
* **Coaching note:** look at the cart before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** the next item is taken before the last one is confirmed and its order checked; a flag is flipped before its last item is
  confirmed; or the tote is moved before all ten items are sorted.
* **SOP rule broken:** Steps 1 to 4, for each item: take, scan, put, confirm, check for full; then clear the tote.
* **Coaching note:** one item start to finish, then the next. The order is the task.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two items; both grippers carry different items at the same time outside a hand-over; or a gripper holds an
  item while the other works instead of being clear of the put-wall.
* **SOP rule broken:** Steps 1 to 4, one gripper holds one item, and the other is empty, taking a hand-over, or clear of the put-wall.
* **Coaching note:** one item, one trip.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a tipped item, a lamp still
  lit, a flag not clicked up, or a tote half off the lower deck.
* **SOP rule broken:** Steps 1.1 to 4, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** an item or the tote is dropped on the cart, a cubby lip, or the floor, or an item in the tote is knocked over.
* **SOP rule broken:** Steps 1 to 4, nothing is dropped or knocked out of its place, and every gripper comes out the way it went in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **left gripper** goes into A2, B2, or C2 or touches their lamps or flags; the **right gripper** does the same in the left
  column; the gripper away from the cart touches the tote or the cart; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 4, each gripper works its own column, only the cart gripper works the cart and the scanner, and the arms never
  cross.
* **Coaching note:** left column, left arm. Right column, right arm. The cart side decides who scans.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with an item in the tote or the wrong cubby, a lamp lit, a flag down, the tote on the top deck, an arm short
  of home, or a gripper not fully open.
* **SOP rule broken:** Step 5, look once across the put-wall and the cart, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a cubby label, an order card, an item label, a lamp, or a flag**, so which item went where, which lamp lit, or which flag
  is up cannot be judged.
* **Put-wall fault:** no lamp lights on a correctly held barcode, two lamps light at once, a lamp will not turn off when pressed, or a flag will
  not click up or stay up.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Batch fault:** the order cards do not add up to ten, the items in the tote do not match the orders, or a barcode is torn or unreadable.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so the back of a cubby, a lamp, a flag, the
  scanner, the hand-over point, or the lower deck cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Take the next item out of the tote
2. Scan one item at the scanner
3. Hand one item over at the hand-over point
4. Put one item in its lit cubby
5. Press a lamp off to confirm the put
6. Flip one flag up to FULL
7. Set the empty tote on the lower deck
8. Return both arms home and end the episode
