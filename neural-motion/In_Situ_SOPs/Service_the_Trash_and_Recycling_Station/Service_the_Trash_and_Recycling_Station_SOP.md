# Service the Trash and Recycling Station SOP (1x Episode: one station, in situ)

One episode services one trash and recycling station, at the place where it stands. The base is **passive**:
it has no drive of its own, so it is pushed by hand to the front of the station and locked there, and nothing
is carried away to a table. Everything the episode touches is already at the station when recording starts:
the two bins in their bays with a full liner in each, the mixed tray, the two stream trays, the two liner
boxes, the cloth, and the collection cart standing beside the station.

The episode runs these five actions in this order and no other: **tie and lift the full liners, sort the
mixed items into the correct streams, fit new liners, wipe the lids, seat the bins.** Each one is a step, and
the steps run in that order.

The station is worked **as found**. It is the station at the end of a day: both bins stand in their bays with
their lids shut, each liner is full, and a tray of mixed items that people left on top has not been sorted.
There are **two streams**. The **TRASH** bin stands in the left bay and takes a black liner. The **RECYCLING**
bin stands in the right bay and takes a clear liner. The episode ends with both full liners tied and lying
on the collection cart, every mixed item in the stream tray of its own stream, a new liner of the right color
fitted in each bin, both lids shut and wiped, and both bins seated in their bays.

**This is an in-situ task, and three things follow from that.** First, the **worktop runs directly above
both bays**, so **a bin is never worked while it stands in its bay**. Each bin is drawn straight out to the
front, level, before its lid is opened, and pushed straight back in at the end. No gripper comes down into
a bay from above. Second, the **station is never leaned on and never pushed**: no gripper, wrist, or forearm
rests on the worktop, the cabinet, a bin, or the cart, and no push is ever hard enough to shift the cabinet,
a tray, or the cart. Third, **a bin is never lifted**: it slides along the plinth on its base, drawn out and
pushed back, and is never lifted, tipped, or turned.

The station is set up in one of two ways. Only the **collection cart** moves. The bins, the bays, the trays,
the liner boxes, and the cloth are in the same place in both.

* **Config L:** the collection cart stands against the **left end** of the station.
* **Config R:** the collection cart stands against the **right end** of the station.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the
setup it says so on an **IF** line. Look at the station and follow the line that matches.

What stays constant across all sessions:

* **Cart-side rule:** the gripper on the cart's side lifts both full liners and lays them on the cart. That is
  the **left gripper** in Config L and the **right gripper** in Config R. While it lifts, the other gripper
  holds the bin down. No liner is handed over.
* **Stream-side rule:** each stream has its own side. The **left gripper** does everything for the TRASH
  stream: its bin, its lid, its tray, its liners. The **right gripper** does everything for the RECYCLING
  stream. Tying a liner and fitting a liner take both grippers, each working its own half of the bin.
* **Fixed roles:** the **right gripper** wipes both lids with the one cloth, and the **left gripper** is clear
  of the station for the wipe. The five actions run in the same order in both configs.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm
reaches over, under, around, or past the other. Nothing is moved two at a time: one gripper holds one thing,
and the other gripper is empty, holding a bin down, or clear of the station.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never
steered, nudged, or repositioned once recording starts. It is parked once, before recording, and does not
move again until the episode is over.

1. Push the base by hand up to the station and stop it **square to the front of the cabinet**, so the fronts
   of the two bins run straight across the frame of the camera.
2. Stop it **centered on the station**, so the middle of the base is in line with the divider between the two
   bays.
3. Stop it **far enough** back that both bins can be drawn all the way out to their **draw line** without
   touching the base, and **close enough** that both grippers reach the inside of a drawn-out bin and the
   front of the worktop without either arm extending.
4. Check the **height band**: with both bins drawn out to the draw line and their lids open, both grippers come
   down into either bin from above without a wrist or forearm touching a rim, an open lid, or the front edge of
   the worktop, and both grippers reach the floor of either bin.
5. Check the **left side**: the **left gripper** reaches the TRASH bin handle, the whole of the TRASH bin, the
   left half of the RECYCLING bin, the TRASH lid, the TRASH liner box, the TRASH tray, and the mixed tray, all
   without extending.
6. Check the **right side**: the **right gripper** reaches the RECYCLING bin handle, the whole of the RECYCLING
   bin, the right half of the TRASH bin, both lids, the RECYCLING liner box, the RECYCLING tray, the mixed tray,
   and the cloth home, all without extending.
7. Check the **cart** for the config this episode runs: in **Config L** the **left gripper** reaches the whole
   cart bed; in **Config R** the **right gripper** reaches the whole cart bed. The cart gripper carries a liner
   from above either bin to the cart bed without passing in front of the other arm.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not work a
   station the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the station hard
enough to shift it, nothing touches it by hand, and it is never repositioned mid-task. A base that moves after
recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the station and its frame includes the whole of it: both bays, the
   plinth out to both draw lines, both bins drawn out with lids open, the worktop with both liner boxes, all three
   trays, the cloth home, and the collection cart.
3. The camera reads the **inside of a drawn-out bin**, so whether a liner is tied, lifted clear, or fitted down
   to the floor of the bin is readable.
4. The camera reads the **inside of all three trays**, so which tray each mixed item went into is readable.
5. The camera reads the **top of both lids** well enough to see the dirt on them before and after the wipe.
6. The camera reads the **draw lines** and the **front of the cabinet**, so whether a bin is drawn out to its
   line and whether it is seated are readable.
7. Both arms are at home with grippers open.
8. The **left arm** reaches the TRASH bin, the left half of the RECYCLING bin, the TRASH lid, the TRASH liner
   box, the TRASH tray, and the mixed tray without extending to a joint limit.
9. The **right arm** reaches the RECYCLING bin, the right half of the TRASH bin, both lids, the RECYCLING liner
   box, the RECYCLING tray, the mixed tray, and the cloth home without extending to a joint limit.
10. The cart arm for this config reaches the whole cart bed without extending to a joint limit.
11. Neither gripper touches the worktop above a bay while a bin is in its bay, and neither wrist nor forearm
    touches the front edge of the worktop while a gripper works inside a drawn-out bin.
12. The two arms do not collide, and neither arm passes in front of the other.
13. If a place cannot be reached, re-park the base by the Base positioning steps until lines 8 to 12 hold.

### Materials checklist

1. The **station** is a fixed cabinet standing where it lives, braced to the wall or the floor. It is not moved,
   not leaned on, and not pushed at any point.
2. The cabinet has **two bays** side by side, open at the front, standing on a raised **plinth** that carries
   on out in front of them. The **TRASH bay** is on the left and the **RECYCLING bay** is on the right. Each bay
   carries its stream name on the cabinet front above it.
3. The **worktop** is the flat top of the cabinet, directly above both bays. It is high enough that a drawn-out
   bin can open its lid under open air, and low enough that nothing can be lifted over it from a bay.
4. The **plinth** in front of each bay carries a **draw line**, a taped line across it. A bin drawn out until the
   back of the bin is on its draw line stands clear of the worktop.
5. Each bay has a **stop** at its back. A bin pushed in until it meets the stop is flush with the front of the
   cabinet.
6. The **TRASH bin** stands in the left bay and the **RECYCLING bin** in the right bay, each pushed in to its
   stop. They are the same size: square, open at the top, with a **front handle** on the face toward the base.
   Each bin slides along the plinth on its base without catching.
7. Each bin has a **lid** hinged along its back edge. The lid opens by tipping back until it rests upright
   against its **lid stop**, clear of the back rim, and shuts flat on the rim. Each lid has a **front lip** to
   take it by. Both lids start shut.
8. Each bin holds a **full liner**: a drawstring liner filled with light waste to about a hand below the rim,
   its hem turned over the rim all round, and its two **drawstring loops** showing at the left and right sides of
   the rim. The TRASH liner is black and the RECYCLING liner is clear. Each full liner weighs no more than
   1.5 kg and holds nothing sharp and nothing wet.
9. The **mixed tray** is a shallow open tray on the worktop at its **middle**. It holds the **mixed items**: at
   least one item of each stream, each lying clear of the others. How many there are varies per episode.
10. Each mixed item is plainly one stream or the other by the **stream test** in Vocabulary, is empty and dry,
    and can be picked up in one grip.
11. The **TRASH tray** is an open tray on the worktop to the left of the mixed tray, marked TRASH. The
    **RECYCLING tray** is an open tray on the worktop to the right of the mixed tray, marked RECYCLING. Both start
    empty.
12. The **TRASH liner box** stands on the worktop at its **left end** and holds black liners. The **RECYCLING
    liner box** stands on the worktop at its **right end** and holds clear liners. In each box, the top liner
    stands up out of the slot by a hand, folded flat, so a gripper can take it without reaching into the box.
13. There is **one cloth**. It lies folded flat on the **cloth home**, a marked spot on the worktop at its
    front-right corner, in front of the RECYCLING liner box.
14. The cloth is damp and wrung out, so it picks dirt up and does not drip.
15. There are spots of dried dirt on the top of both lids, spread over the whole lid, so whether a lid has been
    wiped is readable from the front.
16. The **collection cart** is a low flat cart, its bed at about the height of the bin rims, with its wheels
    braked. It stands against the **left end** of the station in **Config L** and against the **right end** in
    **Config R**, and its bed starts empty.
17. Nothing else stands anywhere at the station within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the draw lines, the tray names, and the cloth home. You judge
every other place by eye against the cabinet itself.

* **Station:** the fixed cabinet the base is parked at. It is never moved, never leaned on, and never pushed.
* **Worktop:** the flat top of the cabinet, directly above both bays. Left to right it carries the TRASH liner
  box, the TRASH tray, the mixed tray, the RECYCLING tray, and the RECYCLING liner box, with the cloth home at the
  front-right corner.
* **TRASH bay / TRASH bin:** the left bay and the bin that lives in it, with its lid. **Left gripper**, except
  for the right half of the bin when tying or fitting a liner and the right gripper's wipe of its lid.
* **RECYCLING bay / RECYCLING bin:** the right bay and the bin that lives in it, with its lid. **Right gripper**,
  except for the left half of the bin when tying or fitting a liner.
* **Plinth and draw lines:** the raised floor the bins slide on, with one taped draw line in front of each bay.
* **Mixed tray:** the middle of the worktop. Both grippers take from it, each only the items of its own stream.
* **TRASH tray:** left of the mixed tray. **Left gripper only.**
* **RECYCLING tray:** right of the mixed tray. **Right gripper only.**
* **TRASH liner box:** left end of the worktop, black liners. **Left gripper takes the liner.**
* **RECYCLING liner box:** right end of the worktop, clear liners. **Right gripper takes the liner.**
* **Cloth home:** the marked spot at the front-right corner of the worktop. **Right gripper only.**
* **Collection cart:** the low braked cart against the left end (Config L) or the right end (Config R) of the
  station. **Cart gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the TRASH side: the TRASH bin, its lid, the TRASH tray, and the TRASH liner box,
  and in Config L the cart.
* The **right gripper** works the RECYCLING side: the RECYCLING bin, its lid, the RECYCLING tray, the RECYCLING
  liner box, and the cloth, and in Config R the cart.
* Both grippers work inside one bin together only to tie a liner, to hold a bin down while the cart gripper
  lifts, and to fit a liner. Then the **left gripper** works the left half of that bin and the **right gripper**
  works the right half.
* The **right gripper** goes over the TRASH lid for one reason only: the **wipe**, while the left gripper is drawn
  clear of the station.
* Neither arm reaches over, under, around, or past the other, and neither reaches across the front of the other
  arm's body.
* Only one thing is moved at a time. A gripper holds one thing, and while it does, the other gripper is empty,
  holding a bin down, or drawn **clear of the station**.

### Arm assignments

* **Left gripper.** Draws the TRASH bin out and pushes it back, opens and shuts its lid, sorts every TRASH item
  into the TRASH tray, and takes the black liner out of its box. Holds the left loop and works the left half of
  the bin when tying and fitting a liner. In **Config L**, lifts both full liners onto the cart.
* **Right gripper.** Draws the RECYCLING bin out and pushes it back, opens and shuts its lid, sorts every
  RECYCLING item into the RECYCLING tray, and takes the clear liner out of its box. Holds the right loop, draws
  the knot, and works the right half of the bin when tying and fitting a liner. Wipes both lids with the one
  cloth. In **Config R**, lifts both full liners onto the cart.
* Nothing is handed between grippers, and only one thing is moved at a time.

## Vocabulary

* **Stream:** one of the two kinds of waste the station takes. **TRASH** (black liner, left) and **RECYCLING**
  (clear liner, right).
* **Stream test:** an empty drink can, an empty plastic bottle, or clean dry paper or card is **RECYCLING**.
  Everything else is **TRASH**, for example a food wrapper, a used tissue, a paper cup, or a crisp packet. No other
  test is applied.
* **Stream side:** the side a stream lives on. The **left gripper** does the TRASH stream and the **right gripper**
  does the RECYCLING stream.
* **Cart gripper:** the gripper on the cart's side. The **left gripper** in Config L and the **right gripper** in
  Config R. The other gripper is the **holding gripper** while a liner is lifted.
* **Drawn out:** the bin has slid straight forward along the plinth until the back of the bin is on its draw line,
  square to the cabinet, clear of the worktop.
* **Seated:** the bin has slid straight back into its bay until it meets the stop, and its front is flush with the
  front of the cabinet.
* **Open / shut lid:** an open lid rests upright against its lid stop. A shut lid lies flat on the rim all the way
  round.
* **Loops:** the two drawstring loops of a liner, one at the left side of the rim and one at the right.
* **Neck:** the top of a liner once the loops are drawn up and its mouth is closed.
* **Tied:** the neck is closed tight and the loops hold one knot on it, pulled tight, so nothing can fall out
  when the liner is lifted.
* **Hold down:** the holding gripper closes on the rim of the bin at its own side and presses it flat on the
  plinth, so the bin does not rise or slide while the liner comes out.
* **Fitted:** the new liner stands open in the bin, down to the floor of the bin, not twisted, not torn, with its
  hem turned over the rim all the way round and both loops showing at the left and right sides.
* **Set down:** the thing is lowered until it rests on the floor of the tray or on what is already there, and only
  then does the gripper open. Nothing is let go from above.
* **Pass:** one wipe. The gripper lays the cloth flat on the lid, presses it down, draws it straight in one line
  from the back edge of the lid to the front edge without lifting, and stops.
* **Clear of the station:** the arm is drawn back so that no part of it is over a bin, a lid, the worktop, or the
  cart.

## Steps

Run Steps 1 to 5 in order, and end the episode with Step 6. The five steps are the five actions of the task, in
the task's own order: **tie and lift the full liners, sort the mixed items, fit new liners, wipe the lids, seat the
bins.** Only Step 1.4 depends on the config. Every other step is the same in both.

### Step 1: Tie and lift the full liners

**Goal:** both bins are drawn out with their lids open, and both full liners are tied and lying on the collection
cart.

#### 1.1 Draw out the bins

* Draw out the TRASH bin first, then the RECYCLING bin.
* With the **left gripper**, close on the front handle of the TRASH bin and draw it straight forward along the
  plinth, level, without lifting it, until the back of the bin is on its draw line. Open the gripper and draw it
  back.
* With the **right gripper**, close on the front handle of the RECYCLING bin and draw it straight forward along the
  plinth, level, without lifting it, until the back of the bin is on its draw line. Open the gripper and draw it
  back.
* With either gripper, keep the bin square to the cabinet and do not pull it past its draw line.

**Check:** both bins are **drawn out**, square, backs on their draw lines, nothing spilled. If a bin stands crooked,
short of its line, or past it, close on its handle with the gripper on its side and slide it straight to its line.

#### 1.2 Open the lids

* With the **left gripper**, close on the front lip of the TRASH lid and tip it up and back, slowly, until it rests
  upright against its lid stop. Open the gripper and draw it back.
* With the **right gripper**, close on the front lip of the RECYCLING lid and tip it up and back, slowly, until it
  rests upright against its lid stop. Open the gripper and draw it back.
* With either gripper, do not let a lid fall back or drop onto its stop.

**Check:** both lids rest upright on their stops and stay there with the grippers off them.

#### 1.3 Tie the full liners

Tie the TRASH liner first, then the RECYCLING liner. Both grippers work the same bin.

* With the **left gripper**, close on the left loop. With the **right gripper**, close on the right loop.
* With **both grippers**, draw the loops straight up together, level, until the hem comes off the rim and the mouth
  of the liner is closed tight into a **neck** above the waste.
* With the **left gripper**, hold the left loop still, up and a little to the left of the neck.
* With the **right gripper**, carry the right loop over the front of the left loop, down behind it, and back up
  through the gap between the left loop and the neck, to the right side. This is one knot, the same first cross as
  tying a shoe.
* With **both grippers**, pull the loops apart, the **left gripper** to the left and the **right gripper** to the
  right, until the knot is tight on the neck.
* With **both grippers**, keep the liner inside the bin while tying. Do not lift it off the floor of the bin.

**Check:** the liner is **tied**: the neck is closed and the knot sits tight on it. If the knot is loose or has
slipped off, open it with the **right gripper**, draw the loops up again with **both grippers**, and tie again.

#### 1.4 Lift the full liners onto the cart

Lift the TRASH liner first, then the RECYCLING liner, each straight after it is tied.

* **IF Config L:** the **left gripper** is the cart gripper and the **right gripper** holds the bin down.
* **IF Config R:** the **right gripper** is the cart gripper and the **left gripper** holds the bin down.
* Then, in both: with the **holding gripper**, let go of its loop, close on the rim of the bin at its own side,
  and **hold it down**.
* With the **cart gripper**, let go of its loop and close on the **knot**.
* With the **cart gripper**, lift the liner straight up, slowly, until its bottom is clear of the rim.
* With the **holding gripper**, keep the bin flat on the plinth until the liner is clear, then open and draw it
  **clear of the station**.
* With the **cart gripper**, carry the liner level to the cart, bottom clear of the rims, the lids, and the
  worktop, and lower it until it rests on the cart bed: the first liner at the far end of the bed, the second
  beside it, nearer the station. Open the gripper and draw it back.
* With the **cart gripper**, do not drag the liner over the rim, swing it, or let it go from above the bed.

**Check:** each full liner lies on the cart bed, tied, whole, and nothing has fallen out of it. The bin it came out
of is still on its draw line and holds nothing. If a liner lies half off the bed, close on its knot with the **cart
gripper** and set it down again.

**Expected state:** both bins are drawn out and empty, their lids open. Both full liners lie tied on the cart. The
mixed items are still in the mixed tray.

### Step 2: Sort the mixed items

**Goal:** every mixed item is **set down** in the stream tray of its own stream, and the mixed tray holds nothing.

* Work one item at a time. Take the item nearest the front of the mixed tray first and work back.
* Apply the **stream test** in Vocabulary to the item before any gripper moves.
* **For a TRASH item:** with the **left gripper**, close on the item at its widest point and lift it straight up out
  of the mixed tray. With the **left gripper**, carry it level to the **TRASH tray** and **set it down** there. Open
  the gripper and draw it back.
* **For a RECYCLING item:** with the **right gripper**, close on the item at its widest point and lift it straight
  up out of the mixed tray. With the **right gripper**, carry it level to the **RECYCLING tray** and **set it down**
  there. Open the gripper and draw it back.
* With the gripper that is not carrying, stay open and out of the mixed tray until the carrying gripper has drawn
  back.
* With either gripper, carry one item at a time, lift it clear of the tray before the carry, and do not slide it
  across the worktop or let it go over the bins.
* Repeat for the next item until the mixed tray is empty, then draw both grippers **clear of the station**.

**Check:** after each one, the item lies inside the tray of its own stream and nothing has bounced out. If an item
went into the wrong tray, lift it out with the gripper on that tray's side, set it back in the mixed tray, and sort it
again with the gripper of its own stream. Look into the mixed tray once more: if an item is left, sort it before
Step 3.

**Expected state:** the mixed tray is empty. The TRASH tray holds only TRASH items and the RECYCLING tray holds only
RECYCLING items. Both bins are still drawn out, empty, lids open.

### Step 3: Fit new liners

**Goal:** a new liner of the right color is **fitted** in each bin: black in TRASH, clear in RECYCLING.

Fit the TRASH bin first, then the RECYCLING bin. Both grippers work the same bin.

#### 3.1 Take the liner out of its box

* **For the TRASH bin:** with the **left gripper**, close on the top black liner where it stands up out of the TRASH
  liner box and draw it straight up until it comes free.
* **For the RECYCLING bin:** with the **right gripper**, close on the top clear liner where it stands up out of the
  RECYCLING liner box and draw it straight up until it comes free.
* With the gripper holding the liner, carry it level to above the middle of its bin and let it hang.
* With the gripper that is not holding the liner, stay open and clear of the liner box.

**Check:** one liner hangs from the gripper, the right color for this bin. If two came out together, lay the second
back on its box with the same gripper.

#### 3.2 Open the liner into the bin

* With the **left gripper**, close on the left loop of the new liner. With the **right gripper**, close on the right
  loop. The gripper that brought the liner out lets go of it only after both loops are held.
* With **both grippers**, draw the loops apart until the mouth of the liner opens.
* With **both grippers**, bring the liner straight down into the bin, bottom first, until the bottom of the liner
  touches the floor of the bin.

**Check:** the mouth is open and the liner hangs straight down inside the bin, not twisted.

#### 3.3 Turn the hem over the rim

* With the **left gripper**, turn the hem over the left side of the rim, then over the left half of the back rim,
  then over the left half of the front rim.
* With the **right gripper**, turn the hem over the right side of the rim, then over the right half of the back rim,
  then over the right half of the front rim.
* With either gripper, leave the loop on its side showing outside the rim.
* With the **gripper on the stream side**, press the middle of the liner down once to the floor of the bin, then draw
  both grippers **clear of the station**.

**Check:** the liner is **fitted**. If a stretch of hem is off the rim, turn it over again with the gripper on that
side. If the liner is torn, take it out with **both grippers**, lay it on the worktop beside its liner box, and fit a
new one from 3.1.

**Expected state:** a black liner is fitted in the TRASH bin and a clear liner in the RECYCLING bin. Both lids are
still open.

### Step 4: Wipe the lids

**Goal:** both lids are shut and wiped, and the cloth is back on the cloth home.

#### 4.1 Shut the lids

* With the **left gripper**, close on the front lip of the TRASH lid and tip it forward and down, slowly, until it
  lies flat on the rim. Open the gripper and draw it **clear of the station**.
* With the **right gripper**, close on the front lip of the RECYCLING lid and tip it forward and down, slowly, until it
  lies flat on the rim. Open the gripper and draw it back.
* With either gripper, do not let a lid drop onto the rim.

**Check:** both lids lie flat, shut all the way round, and the hem of each liner is trapped under its lid.

#### 4.2 Wipe the lids

The **right gripper** does the whole wipe: the RECYCLING lid first, then the TRASH lid. The **left gripper** stays
open and **clear of the station** for all of this.

* With the **right gripper**, close on the middle of the **cloth** and lift it straight up off the **cloth home**.
* With the **right gripper**, lay the cloth flat on the RECYCLING lid along its left third and draw it in one **pass**
  from the back edge of the lid to the front edge.
* With the **right gripper**, lift the cloth just off the lid, carry it back to the back edge, and draw a second pass
  along the middle third, then a third pass along the right third.
* With the **right gripper**, carry the cloth just off the lids to the TRASH lid and wipe it the same way: three
  passes, left third, middle third, right third, each from the back edge to the front edge.
* With the **right gripper**, press only as hard as the wipe needs. Do not push a lid open, and do not push a bin
  along the plinth.

**Check:** each lid shows no dirt, the three passes have covered it from edge to edge, and no dirt has gone into a
tray. If a line of dirt is left, wipe that line again with the **right gripper**.

#### 4.3 Put the cloth back

* With the **right gripper**, carry the cloth just off the lids back to the **cloth home** and lay it flat there, then
  open the gripper and draw it **clear of the station**.

**Check:** the cloth lies flat on the cloth home, and neither gripper holds anything.

**Expected state:** both lids are shut and clean, the cloth is on the cloth home, and both bins still stand on their
draw lines.

### Step 5: Seat the bins

**Goal:** both bins are **seated** in their bays.

* Seat the TRASH bin first, then the RECYCLING bin.
* With the **left gripper**, close on the front handle of the TRASH bin and push it straight back along the plinth,
  level, without lifting it, until it meets the stop. Open the gripper and draw it back.
* With the **right gripper**, close on the front handle of the RECYCLING bin and push it straight back along the
  plinth, level, without lifting it, until it meets the stop. Open the gripper and draw it back.
* With either gripper, keep the bin square to the bay so it does not catch on the cabinet, and do not push it hard
  enough to knock the stop.

**Check:** each bin is **seated**: its front is flush with the front of the cabinet and its lid is still shut. If a bin
stands proud or crooked, close on its handle with the gripper on its side, draw it out a little, and push it straight
in again.

**Expected state:** both bins are seated with lids shut, both arms are clear of the station, and the plinth in front of
the bays is empty.

### Step 6: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the station serviced.

* Look once across the station: both full liners lie tied on the cart, every mixed item is in its stream tray, a new
  liner of the right color is fitted in each bin, both lids are shut and clean, the cloth is on its home, and both bins
  are seated.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the station is serviced and still, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the new liners out of both bins and fold them back into their liner boxes, or throw them away if they have
   stretched or torn.
2. Take both full liners off the cart, untie them, and put them back in their bins, the black one in TRASH and the
   clear one in RECYCLING, hem turned over the rim, loops at the sides.
3. Check each full liner is still whole, holds nothing sharp or wet, and weighs no more than 1.5 kg.
4. Tip every item from both stream trays back into the mixed tray, each clear of the others. Vary how many and which
   items between episodes, keeping at least one of each stream.
5. Stand the top liner of each box up out of its slot by a hand.
6. Spread fresh spots of dirt over the top of both lids and let them dry.
7. Rinse the cloth, wring it out, and lay it folded flat on the cloth home. Replace it when it has stopped picking dirt up.
8. Shut both lids and push both bins in to their stops.
9. Move the collection cart to the end of the station for the next episode's config, bed empty, wheels braked.
10. Check both lids tip open to their stops and shut flat, both bins slide freely, and both draw lines are still readable.
11. Pick up anything that landed on the plinth, the worktop, or the floor.
12. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what
the reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a
rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the cabinet shifts in frame, the bins change angle or size in frame, or the base rolls, creeps, or turns
  at any point after recording starts.
* **SOP rule broken:** Steps 1 to 6, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Worked a bin in its bay or fouled the worktop**

* **Visible cue:** a gripper opens a lid, reaches into a bin, or takes a liner while the bin still stands in its bay; or a
  gripper, wrist, forearm, or liner knocks, scrapes, or rests on the front edge of the worktop.
* **SOP rule broken:** Steps 1.1 to 1.4, each bin is drawn out to its draw line before its lid is opened, and nothing
  comes down into a bay from above.
* **Coaching note:** out first, then open. There is no way into a bin under the worktop.

**Violation: Leaned on or pushed the station**

* **Visible cue:** a gripper, wrist, or forearm rests on the worktop, the cabinet, a bin, or the cart; the cabinet, a tray,
  a liner box, or the cart rocks, slides, or shifts; or the wipe presses a lid open or a bin along the plinth.
* **SOP rule broken:** Steps 1 to 5, the station carries no weight and nothing on it is pushed out of place.
* **Coaching note:** the arm holds itself up. Press only as hard as the work needs.

**Violation: Bin lifted, tipped, or not drawn to its line**

* **Visible cue:** a bin leaves the plinth, tips, or turns; a bin is drawn out crooked, short of its draw line, or past
  it; or a bin is drawn or pushed by its rim or its lid instead of its front handle.
* **SOP rule broken:** Steps 1.1 and 5, each bin slides straight along the plinth by its front handle, to its draw line and
  back to its stop.
* **Coaching note:** handle, straight, level. A bin never leaves the floor.

**Violation: Lid let fall**

* **Visible cue:** a lid drops back onto its stop, drops shut onto the rim, bounces, or is opened or shut by any part but
  its front lip; or a lid is left open at the end of Step 4.1.
* **SOP rule broken:** Steps 1.2 and 4.1, each lid is tipped slowly by its front lip, open to its stop and shut flat on
  the rim.
* **Coaching note:** hold the lip all the way. A dropped lid is a pinched finger at a real station.

**Violation: Liner not tied**

* **Visible cue:** a full liner is lifted with its neck open, with no knot, or with a knot so loose that it slips off;
  waste falls out of the neck; or the liner is lifted off the floor of the bin while it is being tied.
* **SOP rule broken:** Step 1.3, draw the loops up to close the neck, tie one knot, and pull it tight before the liner is
  lifted.
* **Coaching note:** closed, knotted, tight, and only then lift. An open liner spills on the way to the cart.

**Violation: Liner lifted wrong**

* **Visible cue:** a full liner is lifted by its body or by one loop instead of the knot; the bin rises, slides, or tips
  with the liner because nothing holds it down; the liner is dragged over the rim; the liner swings; or the liner tears.
* **SOP rule broken:** Step 1.4, the holding gripper holds the bin down while the cart gripper lifts the liner straight up
  by its knot until it is clear of the rim.
* **Coaching note:** hold the bin, lift the knot, straight up and slow.

**Violation: Full liner not laid on the cart**

* **Visible cue:** a full liner is dropped or let go from above the cart bed; it is laid on the floor, the plinth, the
  worktop, or a lid instead of the cart; it hangs half off the bed; or it is left in its bin.
* **SOP rule broken:** Step 1.4, the cart gripper lowers each full liner until it rests on the cart bed, then opens.
* **Coaching note:** down to the bed, then let go. The cart is the only place a full liner goes.

**Violation: Item sorted into the wrong stream**

* **Visible cue:** a RECYCLING item goes into the TRASH tray or a TRASH item into the RECYCLING tray; an item goes into a
  bin, a liner box, or back into the mixed tray without being sorted; or a wrong item is seen and left where it landed.
* **SOP rule broken:** Step 2, apply the stream test to each item and set it down in the tray of its own stream.
* **Coaching note:** read the item, then move. Can, bottle, or clean paper is RECYCLING. Everything else is TRASH.

**Violation: Item dropped into a tray or left in the mixed tray**

* **Visible cue:** an item is let go from above a tray and falls in, bounces out, or is thrown; an item is slid across the
  worktop instead of lifted; an item is carried over a bin; or the mixed tray still holds an item at the end of Step 2.
* **SOP rule broken:** Step 2, each item is lifted, carried, and set down in its tray, until the mixed tray is empty.
* **Coaching note:** set it down, do not drop it. An item that bounces out is a sort that did not happen.

**Violation: Wrong liner in a bin**

* **Visible cue:** a clear liner is fitted in the TRASH bin or a black liner in the RECYCLING bin, a liner is taken from
  the other stream's box, or two liners are fitted in one bin.
* **SOP rule broken:** Step 3.1, each bin takes one liner of its own color, from its own liner box.
* **Coaching note:** black for TRASH, clear for RECYCLING. The color is how the next person knows the stream.

**Violation: Liner not fitted**

* **Visible cue:** the liner does not reach the floor of the bin; it is twisted; a stretch of hem is not over the rim; a
  loop is tucked inside the bin; the liner is torn and left in; or the lid is shut on a liner with its hem off the rim.
* **SOP rule broken:** Steps 3.2 and 3.3, open the liner, bring it down to the floor of the bin, and turn the hem over the
  rim all the way round with the loops showing.
* **Coaching note:** down to the floor, hem over all the way round. A liner that falls in is a bin someone has to empty by hand.

**Violation: Wipe pattern wrong**

* **Visible cue:** a lid gets fewer or more than three passes; a pass runs from front to back; the cloth lifts partway
  through a pass; the lids are wiped in the wrong order; or part of a lid is never covered.
* **SOP rule broken:** Step 4.2, wipe the RECYCLING lid then the TRASH lid, each with three passes, left, middle, right,
  each from the back edge to the front edge without lifting.
* **Coaching note:** three passes per lid, back to front. Count them as you go.

**Violation: Dirt wiped into a tray or off the lid**

* **Visible cue:** a pass carries dirt off the front edge of a lid onto the plinth or the floor, or wipes dirt into a stream
  tray, a liner box, or the gap under a lid.
* **SOP rule broken:** Step 4.2, each pass stops at the front edge so the cloth keeps the dirt.
* **Coaching note:** the cloth holds the dirt. Anything that goes over the edge, someone else has to sweep.

**Violation: Cloth not put back on the cloth home**

* **Visible cue:** the cloth is left on a lid, in a tray, on the worktop, on the cart, or still in the gripper at the end of
  the episode, or it is left bunched instead of flat.
* **SOP rule broken:** Step 4.3, the **right gripper** lays the cloth flat on the cloth home before Step 5.
* **Coaching note:** same spot, flat, every time.

**Violation: Bin not seated**

* **Visible cue:** a bin stands proud of the cabinet front, sits crooked in its bay, catches on the cabinet, or is still on its
  draw line at the end; or a bin is pushed in with its lid open.
* **SOP rule broken:** Step 5, each bin is pushed straight back by its front handle until it meets the stop and is flush with
  the front of the cabinet.
* **Coaching note:** square it up, one straight push, all the way in.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the station is not set up in: the wrong gripper lifts a full liner, the lifting arm
  carries a liner to the end of the station where the cart is not, or the cart is moved before or during the episode.
* **SOP rule broken:** Step 1.4, look at the station, find the cart, and follow the IF line that matches the config the episode
  is set up in.
* **Coaching note:** look at the cart before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** a lid is opened before both bins are drawn out; the RECYCLING bin is serviced before the TRASH bin in any
  step other than the wipe; a liner is lifted before it is tied; a mixed item is touched before both full liners are on the cart; a new liner goes
  in before the mixed tray is empty; a lid is shut before both new liners are fitted; the cloth touches a lid before both lids
  are shut; a bin is pushed in before the cloth is back on its home; or the mixed items are taken out of front-to-back order.
* **SOP rule broken:** Steps 1 to 5, tie and lift the full liners, sort the mixed items, fit new liners, wipe the lids, then
  seat the bins.
* **Coaching note:** the order is the task. Each step leaves the station ready for the next one.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two mixed items, two liners, or a liner and an item together; both grippers carry
  different things at the same time; or a gripper works while the other holds something instead of being open, holding a
  bin down, or clear of the station.
* **SOP rule broken:** Steps 1 to 5, one gripper holds one thing, and while it does the other gripper is empty, holding a bin
  down, or clear of the station.
* **Coaching note:** one thing, one trip. Two at once is what ends up on the floor.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a bin
  crooked or off its line, a loose knot, a liner half off the cart, an item in the wrong tray, two liners drawn out, a stretch
  of hem off the rim, a torn liner left in, a line of dirt left on a lid, or a bin standing proud.
* **SOP rule broken:** Steps 1.1 to 5, run each check and correct what it finds by the retry written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a mixed item, a liner, or the cloth is dropped on the plinth, the worktop, or the floor; a tray or a liner
  box is knocked over or out of place; a lid is knocked shut or open; waste spills out of a full liner; or an arm knocks an item
  out of a tray.
* **SOP rule broken:** Steps 1 to 5, nothing is dropped or knocked out of its place, and every gripper comes out the way it
  went in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **right gripper** touches a TRASH item, the TRASH tray, the TRASH liner box, the TRASH bin handle, or the
  TRASH lid outside the wipe; the **left gripper** touches a RECYCLING item, the RECYCLING tray, the RECYCLING liner box, the
  RECYCLING bin handle, the RECYCLING lid, or the cloth; the gripper that is not the cart gripper lifts a liner or touches the
  cart; the **left gripper** is over the station while the right gripper wipes; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 5, each gripper does its own stream, the cart gripper does the cart, the **right gripper**
  does the whole wipe, and the arms never cross.
* **Coaching note:** left arm is TRASH, right arm is RECYCLING, and the cart side decides who lifts.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a full liner off the cart, an item in the mixed tray, a bin without a fitted liner, a
  lid open or dirty, the cloth off its home, a bin not seated, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 6, look once across the station, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for
coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read the inside of a bin, a tray, a lid top, or a draw line**, so whether a liner was tied or fitted, which tray an
  item went into, whether a lid came clean, or whether a bin was drawn out or seated cannot be judged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Faulty station:** a bin that sticks on the plinth, a lid hinge that will not hold the lid on its stop, a stop that has come
  loose, or a cart whose brake will not hold.
* **Faulty liner:** a drawstring that snaps or pulls out of its hem when drawn gently, or a new liner that comes out of the box
  already torn.
* **Consumables out:** no liners of one color, no damp cloth, or no dirt on a lid at the start.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a bin handle, the floor of a
  drawn-out bin, a lid, a tray, a liner box, the cloth home, or the cart bed cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Draw one bin out to its draw line
2. Open one lid
3. Draw up the loops of one full liner
4. Tie the knot on one full liner
5. Lift one full liner out of its bin
6. Lay one full liner on the cart
7. Sort one mixed item into its stream tray
8. Take one new liner out of its box
9. Open one new liner into its bin
10. Turn the hem over the rim of one bin
11. Shut one lid
12. Take the cloth off the cloth home
13. Wipe one pass across a lid
14. Lay the cloth back on the cloth home
15. Push one bin back into its bay
16. Return both arms home and end the episode
