# Pack a Single-Order Carton SOP (1x Episode: 3 Items)

One episode packs one three-item order into one carton. Both grippers bring the right-size carton from the
back of the table to the center, and its four top flaps are opened. The base foam goes in flat, each of the
three order items goes into its own seat in the base foam, the pack slip goes on the items, and the top foam
goes over everything. The four flaps are closed, one tape strip is laid across the seam by both grippers
together, and the shipping label goes on the near half of the top. Then the episode ends.

The order never changes: carton to center, open, base foam, items, pack slip, top foam, close, tape, label.
Nothing goes into the carton until the base foam is flat in it. The pack slip goes in only after the last
item is in. The carton is not closed until the top foam is in. The label goes on only after the tape.

The flaps open and close in a fixed order. Open: far flap, near flap, left flap, right flap. Close: left
flap, right flap, far flap, near flap.

The right gripper does the primary work and the left gripper supports. The right gripper works the tape and
the shipping label. The left gripper works the order items and the pack slip. The foam belongs to whichever
gripper is on the dunnage stack's side. Each gripper opens and closes the flaps named for it in the Steps.
Both grippers move the carton together, and both grippers lay the tape together.

Adjustments are always optional. After the tape is laid and after the label is on, the grippers may make
adjustments. Adjustments are not steps. There is no set number of them, and making none is correct.

The table is set up in one of four ways. Only the dunnage stack moves, from one corner of the table to
another. The carton start spot, the pick spot, the label spot and the packing spot are in the same place in
all four.

* **Config L1:** the dunnage stack is in the front-left corner.
* **Config L2:** the dunnage stack is in the back-left corner.
* **Config R1:** the dunnage stack is in the front-right corner.
* **Config R2:** the dunnage stack is in the back-right corner.

Where a step depends on the setup it says so on an **IF** line: look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the dunnage stack starts in the front-left corner (**Config L1**), the back-left
  corner (**Config L2**), the front-right corner (**Config R1**) or the back-right corner (**Config R2**).
  One config per episode, chosen before recording and never changed mid-episode. The other three corners are
  bare.
* **Stack side:** the side of the table the dunnage stack is on: left in Config L1 and L2, right in Config
  R1 and R2. Everything that changes with the config follows the stack side, not the corner.
* **Foam owner:** the foam belongs to the gripper on the stack side, the **left gripper** in Config L1 and
  L2 and the **right gripper** in Config R1 and R2. That one gripper takes each pad off the stack and lays it
  in the carton, the base foam first and the top foam second.
* **Same-side rule:** no arm reaches across the table for a foam pad, and no foam pad ever changes hands.
* **Order:** the order of the work never changes with the config. Only which gripper works the foam
  changes.

## Setup

Complete both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole tabletop: the carton at the back center, the dunnage stack in the
   start place for this episode's config, the pick spot at the left center, the label spot at the right
   center, and the packing spot at the center.
3. The inside of the carton at the packing spot is in view, so the foam, the items and the pack slip can be
   seen going in.
4. The whole top of the carton at the packing spot is in view, so the tape and the label can be seen going
   on.
5. Both arms are at home with their grippers open.
6. The left arm reaches the carton's left wall at the back center, the pick spot, every flap of the carton at
   the packing spot, and, in Config L1 and L2, the dunnage stack in its corner, without extending to a joint
   limit or folding in on itself.
7. The right arm reaches the carton's right wall at the back center, the label spot, every flap of the carton
   at the packing spot, and, in Config R1 and R2, the dunnage stack in its corner, in the same way.
8. Nothing obstructs the paths from the back center to the packing spot, from the dunnage stack to the
   packing spot, from the pick spot to the packing spot, and from the label spot to the packing spot.

### Materials checklist

1. One carton stands at the back center. It is the right size for this order. Its bottom is already taped.
   Its four top flaps are folded in and lie closed but not taped.
2. The carton is empty.
3. The dunnage stack sits in the corner for this episode's config: the front-left corner (**Config L1**), the
   back-left corner (**Config L2**), the front-right corner (**Config R1**), or the back-right corner
   (**Config R2**). It holds one top foam pad on the bottom and one base foam pad on top of it, its three
   seats facing up. Each pad fits flat inside the carton. The other three corners are bare.
4. Exactly three order items lie on the pick spot at the left center, each one clear of the others.
5. The pack slip lies face up on the pick spot, clear of the items.
6. One tape strip lies sticky side down on the label spot at the right center. Both of its ends are folded
   back into grab tabs. It is long enough to run across the seam and down both side walls.
7. One shipping label, already peeled off its backing, lies sticky side down on the label spot, clear of the
   tape strip. One end is folded back into a grab tab.
8. The packing spot at the center of the table is clear.

### Workspace layout

* **Carton start spot:** back center. The carton stands here at the start of the episode.
* **Dunnage stack:** one corner of the table: front-left (**Config L1**), back-left (**Config L2**),
  front-right (**Config R1**), or back-right (**Config R2**). One per episode, clear of the pick spot and the
  label spot. The base foam and the top foam lie here until they go in, and the corner is bare when the
  episode ends.
* **Pick spot:** left center. The order items and the pack slip lie here until they go in.
* **Label spot:** right center. The tape strip and the shipping label lie here until they go on.
* **Packing spot:** the center of the table. All packing, closing, taping and labeling happen here. The
  carton ends the episode here.

## Vocabulary

### Arm assignments

* The **left gripper** owns the pick spot: every order item and the pack slip. It opens the far flap and the
  left flap. It closes the left flap, the far flap and the near flap. It holds the left end of the tape. It
  never touches the shipping label. It works the foam only in Config L1 and L2, where it takes each pad off
  the dunnage stack and lays it in the carton itself.
* The **right gripper** owns the label spot and the shipping label, and it owns the dunnage stack and both
  foam pads in Config R1 and R2, taking each pad off the stack and laying it in the carton itself. It opens
  the near flap and the right flap. It closes the right flap. It picks up the tape and holds the right end of it. It never touches the
  order items or the pack slip.
* **Shared moments:** both grippers carry the carton to the packing spot in Step 1 and both grippers lay the
  tape in Step 8. Either gripper, or both, may make adjustments to the tape and the label.

### Carton anatomy

* **Far flap:** the top flap hinged on the back wall, away from the front edge.
* **Near flap:** the top flap hinged on the front wall, nearest the front edge.
* **Left flap / right flap:** the top flaps hinged on the left wall and the right wall.
* **End flaps:** the far flap and the near flap. When closed they lie on top and meet at the seam.
* **Side flaps:** the left flap and the right flap. When closed they lie flat under the end flaps.
* **Seam:** the line where the closed far flap and near flap meet, running left to right across the top.
* **Near half:** the half of the closed top on the near flap, between the seam and the front wall.

### Packing materials

* **Stack side:** the side of the table the dunnage stack is on: left in Config L1 and L2, right in Config
  R1 and R2. The **stack-side gripper** is the gripper on that side.
* **Base foam:** the foam pad on top of the dunnage stack. It has three seats cut into its top face. It lies
  flat on the carton floor, seats facing up, under everything else.
* **Seat:** a hollow cut into the top of the base foam, shaped for one order item. There is one seat per
  item. The seats are spaced so that seated items never touch each other.
* **Seated:** the item rests in its own seat and touches no other item. It counts as seated even if it
  stands above the top of the foam, as long as it stays in its seat. It is not seated if it sits on the foam
  top between the seats or in another item's seat.
* **Top foam:** the foam pad at the bottom of the dunnage stack. It lies flat over the items and the pack
  slip.
* **Order items:** the three goods for this order, lying on the pick spot. Each one has its own seat in the
  base foam.
* **Pack slip:** the paper sheet listing the order. It lies face up on top of the items.
* **Tape strip:** the pre-cut strip of packing tape on the label spot, called the tape slip at the station.
  It has a grab tab at each end.
* **Shipping label:** the address label on the label spot, already peeled off its backing, with one grab tab.
* **Grab tab:** the folded-back, non-sticky end of the tape strip or the shipping label. It is the only part
  of either one a gripper picks up.

### Moves

* **Open out:** the gripper pinches a flap at the middle of its free edge, swings it up and out over its
  hinge, and lets it hang against the outside of its own wall. The opening is then clear of it.
* **Fold in:** the gripper pinches a flap at the middle of its free edge, swings it up and in over the
  opening until it lies flat and level, and releases.
* **Lower in:** the gripper carries the thing level over its spot, lowers it straight down until it is
  resting, and releases. Nothing is dropped from above.
* **Flat:** a foam pad lies level in the carton with no corner folded up and no edge riding up a wall.
* **Settled:** the thing stays put after the gripper lifts clear, with nothing rocking, sliding or tipping.

### Adjustments

* An adjustment is any small touch-up after the tape is laid or after the label is on: pressing the tape or
  label down, smoothing out a wrinkle or a bubble, pressing an end down onto a wall, or lifting a tab to
  straighten it and laying it down again.
* Adjustments are optional. They are not steps and not substeps. Make as many as needed, or none.
* Either gripper, or both, may adjust. An adjustment never lifts the tape or the label all the way off, never
  opens a flap, and never moves the carton.

## Steps

Steps 1 to 10 are one packing run. Every item and every foam pad is carried level and lowered in.

Steps 3 and 6 depend on which side the dunnage stack is on: the **stack-side gripper** takes each foam pad
off the stack and lays it in the carton, the **right gripper** in Config R1 and R2 and the **left gripper**
in Config L1 and L2. Every other step is the same in all four configs.

### Step 1: Bring the carton to the packing spot

**Goal:** the carton stands at the packing spot, square to the front edge, flaps still closed.

* The **left gripper** closes on the middle of the carton's left wall.
* The **right gripper** closes on the middle of the carton's right wall.
* Both grippers lift the carton straight up together until it clears the table.
* Both grippers carry it level toward the front edge to the packing spot.
* Both grippers lower it straight down until it is resting, then release together.

**Check:** the carton stands upright at the center of the table, square to the front edge, with its top flaps
still closed. If it is crooked, both grippers lift it and set it down again.

**Expected state:** the carton is at the packing spot. The carton start spot is empty.

### Step 2: Open the four top flaps

**Goal:** all four flaps hang open outside their walls and the opening is clear.

* The **left gripper** opens out the far flap.
* The **right gripper** opens out the near flap.
* The **left gripper** opens out the left flap.
* The **right gripper** opens out the right flap.

**Check:** all four flaps hang outside the carton and none springs back over the opening. If one springs
back, the gripper that opened it opens it out again.

**Expected state:** the carton is open and empty at the packing spot.

### Step 3: Lay the base foam

**Goal:** the base foam lies flat on the carton floor with its three seats facing up.

Look where the dunnage stack is before reaching for the base foam.

* **IF the stack is on the right (Config R1 or R2):** the **right gripper** closes on the middle of the near
  edge of the base foam on top of the stack, lifts it straight up off the top foam, carries it level from
  that corner to the packing spot, lowers it in onto the carton floor, seats facing up, and releases.
* **IF the stack is on the left (Config L1 or L2):** the **left gripper** closes on the middle of the near
  edge of the base foam on top of the stack, lifts it straight up off the top foam, carries it level from
  that corner to the packing spot, lowers it in onto the carton floor, seats facing up, and releases.

**Check:** the base foam is flat and its seats face up. If a corner is folded up or an edge rides up a wall,
the **stack-side gripper** lifts that edge and lowers it again. If the seats face down, the **stack-side
gripper** lifts the base foam out, turns it over, and lowers it in again.

**Expected state:** the base foam is flat in the carton with three empty seats. The top foam is alone on the
dunnage stack.

### Step 4: Place the three order items

**Goal:** each of the three order items is seated in its own seat in the base foam.

* The **left gripper** closes on the middle of one item on the pick spot.
* The **left gripper** lifts it straight up, carries it level over that item's seat, and lowers it straight
  down into the seat until it is seated. Then it releases.
* Repeat for the second item and then the third, one at a time, until the pick spot holds only the pack slip.

**Check:** each item is seated in its own seat and touches no other item. If an item is in the wrong seat or
sitting on the foam top, the **left gripper** lifts it and lowers it into its seat again.

**Expected state:** all three seats are filled, one item in each. The pick spot holds only the pack slip.

### Step 5: Insert the pack slip

**Goal:** the pack slip lies face up on top of the items.

* The **left gripper** pinches the pack slip at the middle of its near edge.
* The **left gripper** lifts it, carries it to the carton, lowers it face up onto the items, and releases.

**Check:** the pack slip is inside the carton, face up, and not hanging over a wall. If it is, the **left
gripper** lifts it and lays it again.

**Expected state:** the pick spot is empty. The pack slip lies on the items.

### Step 6: Lay the top foam

**Goal:** the top foam lies flat over the items and the pack slip.

Look where the dunnage stack is before reaching for the top foam. It is the same place as in Step 3.

* **IF the stack is on the right (Config R1 or R2):** the **right gripper** closes on the middle of the near
  edge of the top foam on the stack, lifts it, carries it level from that corner to the carton, lowers it in
  over the items and the pack slip, and releases.
* **IF the stack is on the left (Config L1 or L2):** the **left gripper** closes on the middle of the near
  edge of the top foam on the stack, lifts it, carries it level from that corner to the carton, lowers it in
  over the items and the pack slip, and releases.

**Check:** the top foam covers the items and the pack slip and lies below the top of the walls. If an edge
rides up a wall, the **stack-side gripper** lifts that edge and lowers it again.

**Expected state:** the dunnage stack is empty. The carton is full and ready to close.

### Step 7: Close the four top flaps

**Goal:** all four flaps are closed, the side flaps under the end flaps, and the end flaps meet at the seam.

* The **left gripper** folds in the left flap.
* The **right gripper** folds in the right flap.
* The **left gripper** folds in the far flap over the two side flaps.
* The **left gripper** folds in the near flap over the two side flaps until it meets the far flap at the
  seam.

**Check:** both side flaps lie under the end flaps, and the end flaps meet at the seam with no flap standing
up. If a flap stands up, the gripper that closed it folds it in again.

**Expected state:** the carton is closed but not taped.

### Step 8: Tape the seam

**Goal:** one tape strip runs along the seam from the left wall to the right wall, with its ends down the
side walls.

* The **right gripper** pinches the grab tab at one end of the tape strip on the label spot.
* The **right gripper** lifts that end until the strip peels off the label spot, and carries it above the
  carton.
* The **left gripper** comes in and pinches the grab tab at the other end of the tape strip.
* The **left gripper** holds the left end over the left side of the carton. The **right gripper** holds the
  right end over the right side. The strip hangs above the seam, sticky side down.
* Both grippers lower the strip together onto the seam, the **left gripper** at the left end and the **right
  gripper** at the right end.
* Both grippers bring the ends down onto the side walls and release.

**Optional adjustments:** either gripper, or both, may now press, smooth or straighten the tape. Make as many
adjustments as needed, or none.

**Check:** the tape covers the seam from the left wall to the right wall.

**Expected state:** the carton is closed and taped. The label spot holds only the shipping label.

### Step 9: Apply the shipping label

**Goal:** the shipping label is stuck flat on the near half of the carton top.

* The **right gripper** pinches the grab tab of the shipping label on the label spot.
* The **right gripper** lifts it, carries it above the near half of the carton top, lays it down sticky side
  down, and releases.

**Optional adjustments:** either gripper, or both, may now press, smooth or straighten the label. Make as
many adjustments as needed, or none.

**Check:** the label is on the near half of the top, fully on the carton, and not on the tape.

**Expected state:** the carton is packed, closed, taped and labeled at the packing spot. The label spot is
empty.

### Step 10: End the episode

**Goal:** the carton is packed, closed, taped and labeled, and both arms are safely home.

* Look over the packing spot once: the carton stands closed with the tape across the seam and the label on
  the near half of the top, and the pick spot, the dunnage stack and the label spot are all empty.
* Return both arms home with their grippers open, then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Peel the shipping label and the tape strip off the carton and throw them away.
2. Open the carton and take out the top foam, the pack slip, the items and the base foam.
3. Close the carton's four top flaps, without tape, and stand it at the back center.
4. Stack the top foam and then the base foam, seats facing up, on the dunnage stack in the corner for the
   next episode's config: the front-left corner (Config L1), the back-left corner (Config L2), the
   front-right corner (Config R1), or the back-right corner (Config R2). Leave the other three corners bare.
   Vary the config between episodes.
5. Lay the three order items on the pick spot, each clear of the others. Vary where each one lies between
   episodes.
6. Lay the pack slip face up on the pick spot, clear of the items.
7. Lay a new tape strip, sticky side down with both ends folded into grab tabs, on the label spot.
8. Lay a new shipping label, peeled off its backing, sticky side down with its grab tab, on the label spot,
   clear of the tape.
9. Replace the carton if a flap is torn or will not stay open or closed. Replace a foam pad if it is torn.
10. Clear the packing spot and run both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the start timestamp, violation name, and SOP rule broken. The visible cue is what
the reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it
just because a rule was broken.

### Violations

Adjustments to the tape and the label are optional and unlimited. Making any number of them, or none, is
never a violation.

**Note on the start position:** the violations below were written for Config R2 (the dunnage stack in the
back-right corner, the right gripper taking both pads off it). The pickup and arm-role cues will be rewritten
later to cover all four corners; they are left as they are for now. Until then, anything that does not match
the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**
* **Visible cue:** what the operator does does not match the config on the table: the dunnage stack is not in
  the corner for the config; a gripper reaches across the table for a foam pad; a foam pad is passed from one
  gripper to the other; the gripper that takes a pad off the stack is not the one that lays it in the carton;
  or the wrong IF line is followed.
* **SOP rule broken:** the start position and the same-side rule (the stack-side gripper takes each pad off
  the stack and lays it in the carton, the right gripper in Config R1 and R2 and the left gripper in Config
  L1 and L2; no arm reaches across the table; no pad changes hands; the IF line followed is the one for the
  config on the table).
* **Coaching note:** look which corner the dunnage stack is in before the first reach, then follow that
  side's IF lines in Steps 3 and 6.

**Violation: Carton moved by one gripper**
* **Visible cue:** only one gripper moves the carton to the packing spot, or the carton is dragged or pushed
  across the table instead of lifted and carried.
* **SOP rule broken:** Step 1, the left gripper on the left wall and the right gripper on the right wall lift
  the carton together, carry it level, and lower it at the packing spot.
* **Coaching note:** both walls, both hands, lift it clear of the table.

**Violation: Carton not at the packing spot**
* **Visible cue:** the packing starts with the carton off center, crooked to the front edge, or still at the
  back center.
* **SOP rule broken:** Step 1, the carton stands at the center of the table, square to the front edge, before
  any flap is opened.
* **Coaching note:** set it square in the center first. Everything after this happens there.

**Violation: Flaps opened out of order**
* **Visible cue:** the four flaps are opened in any order other than far, near, left, right.
* **SOP rule broken:** Step 2, open the far flap, then the near flap, then the left flap, then the
  right flap.
* **Coaching note:** far, near, left, right. Say the flap before you reach.

**Violation: Wrong gripper on a flap**
* **Visible cue:** a flap is opened or closed by the gripper not named for it: the right gripper opens the
  far or left flap, the left gripper opens the near or right flap, the right gripper closes the left, far or
  near flap, or the left gripper closes the right flap.
* **SOP rule broken:** Steps 2 and 7, the left gripper opens the far and left flaps and closes the left, far
  and near flaps; the right gripper opens the near and right flaps and closes the right flap.
* **Coaching note:** each flap has one owner. Check the step before you pinch.

**Violation: Packing into a partly open carton**
* **Visible cue:** the base foam goes in while a flap is still closed over the opening or has sprung back
  over it.
* **SOP rule broken:** Step 2, all four flaps hang open outside their walls before anything goes in.
* **Coaching note:** clear opening first. Reopen any flap that springs back.

**Violation: Base foam skipped or late**
* **Visible cue:** an item, the pack slip or the top foam goes into the carton before the base foam is flat
  on the floor, or no base foam goes in.
* **SOP rule broken:** Step 3, the base foam lies flat on the carton floor before anything else goes in.
* **Coaching note:** foam first, always. Nothing touches the carton floor but the base foam.

**Violation: Wrong foam pad used**
* **Visible cue:** the top foam goes in as the base, the base foam goes in with its seats facing down, both
  pads are lifted together, or the top foam is knocked off the stack while the base foam is taken off.
* **SOP rule broken:** Step 3, the right gripper lifts only the base foam off the top of the stack, leaves
  the top foam where it lies, and lays the base foam in with its seats facing up.
* **Coaching note:** the upper pad goes in first, and only that one.

**Violation: Foam pad not flat**
* **Visible cue:** a foam pad is left in the carton with a corner folded up or an edge riding up a wall, and
  the next step starts.
* **SOP rule broken:** Steps 3 and 6, each foam pad lies flat before the next thing goes in.
* **Coaching note:** look at every corner before you move on.

**Violation: Items placed by the wrong gripper**
* **Visible cue:** the right gripper touches an order item or the pack slip, or the left gripper touches a
  foam pad.
* **SOP rule broken:** Steps 3 to 6, the left gripper places every item and the pack slip; the right gripper
  places both foam pads.
* **Coaching note:** left hand for the order, right hand for the foam.

**Violation: More than one item moved at once**
* **Visible cue:** the left gripper lifts two items together, or picks up the next item before the one in its
  grip is resting on the base foam.
* **SOP rule broken:** Step 4, the left gripper places the items one at a time.
* **Coaching note:** one item per trip, all the way down.

**Violation: Item left out or placed wrong**
* **Visible cue:** fewer than three items are seated when the pack slip goes in, an item goes in another
  item's seat, two items share a seat, an item is left sitting on the foam top between the seats, or the
  items touch each other.
* **SOP rule broken:** Step 4, each of the three items is seated in its own seat before the pack slip goes
  in.
* **Coaching note:** one item, one seat. Look at the seat before you lower.

**Violation: Pack slip missing or out of order**
* **Visible cue:** the pack slip goes in before the last item, goes in face down or under an item, is left
  hanging over a wall, or is not put in at all.
* **SOP rule broken:** Step 5, the left gripper lays the pack slip face up on the items after the last item
  is in.
* **Coaching note:** items, then slip, face up on top.

**Violation: Top foam skipped or late**
* **Visible cue:** a flap is closed before the top foam is in, or the top foam goes in before the pack slip.
* **SOP rule broken:** Step 6, the right gripper lays the top foam over the items and the pack slip before
  any flap is closed.
* **Coaching note:** the slip goes under the foam, and the foam goes in before any flap moves.

**Violation: Flaps closed out of order**
* **Visible cue:** the four flaps are closed in any order other than left, right, far, near, or an end flap
  ends up under a side flap.
* **SOP rule broken:** Step 7, close the left flap, then the right flap, then the far flap, then
  the near flap.
* **Coaching note:** sides first, then far, then near. The end flaps always go on top.

**Violation: Tape picked up wrong**
* **Visible cue:** the left gripper picks the tape up first, one gripper lays the tape alone, or a gripper
  takes the strip anywhere but a grab tab.
* **SOP rule broken:** Step 8, the right gripper lifts the strip by the grab tab at one end, then
  the left gripper takes the grab tab at the other end.
* **Coaching note:** right picks it up, left comes in for the other end. Tabs only.

**Violation: Tape not laid together**
* **Visible cue:** one end of the strip is laid down while the other end is not held, the strip sticks to
  itself or to a gripper, or the strip is laid off the seam.
* **SOP rule broken:** Step 8, both grippers lower the strip onto the seam together and bring its ends down
  onto the side walls.
* **Coaching note:** hold it over the seam with both hands and lower it as one.

**Violation: Adjustment breaks the seal**
* **Visible cue:** while adjusting, a gripper pulls the tape or the label all the way off, opens a flap, or
  moves the carton.
* **SOP rule broken:** Steps 8 and 9, adjustments only press, smooth or straighten the tape and label.
* **Coaching note:** adjust in place. If it needs more than a touch-up, lift one tab and lay it again.

**Violation: Label out of order**
* **Visible cue:** the shipping label goes on before the tape is laid.
* **SOP rule broken:** Step 9, the shipping label goes on only after the tape is on the seam.
* **Coaching note:** tape, then label. Always.

**Violation: Label put on wrong**
* **Visible cue:** the left gripper brings the label, the label goes on the far half of the top, on a wall,
  or over the tape, or a gripper takes it anywhere but the grab tab.
* **SOP rule broken:** Step 9, the right gripper carries the label by its grab tab and lays it on the near
  half of the carton top.
* **Coaching note:** right hand, near half, clear of the tape.

**Violation: Dropped or knocked over**
* **Visible cue:** under command, an item, a foam pad, the pack slip, the tape or the label falls, or a
  gripper knocks the carton, the dunnage stack or an item on the pick spot, with no gripper failure, drift or
  controller fault visible.
* **SOP rule broken:** Steps 1 to 9, every item is carried level on a clear path and lowered until it is
  resting.
* **Coaching note:** watch the whole path, not just the target.

**Violation: Manipulation outside the camera frame**
* **Visible cue:** a flap, a foam pad, an item, the pack slip, the tape or the label is worked partly or
  wholly outside the environment camera frame.
* **SOP rule broken:** Steps 1 to 9, every manipulation happens inside the camera frame.
* **Coaching note:** the work has drifted outside the framed area. Set the spots back to their setup
  positions.

**Violation: Wrong episode ending**
* **Visible cue:** the episode ends with a flap open, the tape or label missing, something left on the pick
  spot, the dunnage stack or the label spot, an arm away from home, or a gripper not fully open.
* **SOP rule broken:** Step 10, confirm the closed, taped and labeled carton and the empty spots, then return
  both arms home with grippers open and stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and
never use them for coaching.

* Recording stopped or paused during the episode (recording system).
* Camera dropped frames or lost its feed (capture system).
* Hardware fault on an arm: gripper failure, drift, controller caused collision, or motor error.
* A spot sits outside an arm's comfortable reach, so the arm stalls at a joint limit or has to fold in on
  itself to work it. Move the spot and run the Setup checklists again.
* Defective object: a torn flap, a flap that will not stay open, a torn foam pad, a tape strip or label that
  will not peel off the label spot, or a carton too small for the order. Replace it before the next episode.
* Wrong setup at episode start: the pick spot does not hold exactly three items, a spot is missing its
  materials, the carton is already open, or a foam pad is in the wrong place on the stack. Reset error, not a
  violation.

## Annotation subtasks (from SOP)

1. Carry the carton from the back center to the packing spot with both grippers
2. Open the far flap
3. Open the near flap
4. Open the left flap
5. Open the right flap
6. Lay the base foam flat in the carton
7. Seat one order item in its seat in the base foam
8. Lay the pack slip on the items
9. Lay the top foam over the items and pack slip
10. Close the left flap
11. Close the right flap
12. Close the far flap
13. Close the near flap
14. Pick up the tape strip by one end with the right gripper
15. Take the other end of the tape strip with the left gripper
16. Lay the tape strip on the seam with both grippers
17. Adjust the tape (optional)
18. Lay the shipping label on the near half of the top
19. Adjust the label (optional)
20. Return both arms home and end the episode
