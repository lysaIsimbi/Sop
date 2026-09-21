# Restock the Refrigerator SOP (1x Restock)

One episode restocks one countertop refrigerator. It runs from a cabinet holding six older items with
the new stock waiting outside it, to a cabinet holding all thirteen items with every older item
standing in front of the new one behind it, and the door pressed fully shut.

The order never changes: **load the produce drawer, load the three shelf zones, load the two door
bins, then close the door.** The drawer is loaded and shut before anything goes on the shelf, so
nothing is ever carried over an open drawer, and the door bins are loaded last so nothing is carried
over the loaded shelf.

**Every place in the cabinet is loaded the same way: rotate first, then fill.** The older item already
in that place is drawn forward to the front, and the new item goes in behind it. New stock never goes
in front of older stock, anywhere, and no older item is ever taken out of the cabinet.

Arm roles are fixed and never swap. The **right gripper is the stock gripper**: it takes every item
off the stock tray on the right, loads the three shelf zones and the two door bins, and presses the
door fully shut at the end. The **left gripper is the drawer and door gripper**: it opens the produce
drawer, loads the two produce packs staged on the left, pushes the drawer shut, and swings the door
round at the end. The stock tray is never on the left of the table and the produce never on the right,
and neither arm reaches into the other's side.

The door is hinged on the left of the cabinet. It stands open against the **door post** for the whole
of the loading, so its two bins face the front right where the right gripper works them, and the
cabinet mouth stays clear.

The table is set up in one of three ways. Only the stock tray moves; the cabinet, the door post, the open
door, and the produce staging are in the same place in all three.

* **Config M:** the stock tray is at the front-center, against the front table edge in front of the cabinet
  mouth.
* **Config R1:** the stock tray is at the front-right.
* **Config R2:** the stock tray is at the back-right, beside the cabinet.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the stock tray starts at the front-center (**Config M**), the front-right
  (**Config R1**) or the back-right (**Config R2**). One config per episode, chosen before recording and never
  changed mid-episode. There is no left config: the door post with the open door on it takes the back-left,
  the produce staging takes the front-left, and the tray belongs to the right gripper.
* **Same-side rule:** the **right gripper** takes every item off the stock tray in all three configs — the
  front-center is on its side by convention — and the **left gripper** takes both produce packs from the
  front-left. No arm reaches across the table.
* **Fixed roles:** everything else is the same in all three configs — the produce staging, the drawer, the
  shelf zones, the door bins, the door post, and which gripper works each of them.

## Setup

Complete both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the cabinet and its frame includes the cabinet mouth, the
   shelf and all three zone labels, the produce drawer both shut and pulled open, the door open on the
   post with both bins, the stock tray in its place for this episode's config, the produce staging, and the
   front table edge.
3. The camera reads the shelf from the front, so which zone an item stands in, whether it stands
   upright, and whether anything sticks out past the shelf front lip are all readable.
4. The camera reads both door bins from above, so what is in each bin and where in the bin it stands
   are readable.
5. The camera reads the shut door from the front, so daylight along the seal is readable.
6. Both arms are at home with grippers open.
7. The cabinet is steady on the table and does not slide when the drawer is pulled open or the door is
   pressed shut.
8. The right arm reaches every item on the stock tray in its place for this episode's config (front-center
   in Config M, front-right in Config R1, back-right in Config R2), all three shelf zones from the front, and
   both door bins from above, without extending to a joint limit. It reaches neither the produce staging nor
   the drawer.
9. The left arm reaches the drawer handle, the whole drawer floor when the drawer is open, both produce
   packs on the produce staging, and the door's free edge through its whole swing, without extending to
   a joint limit. It reaches neither the stock tray nor the shelf.
10. Each arm comes onto the shelf straight in from the front and comes onto the door bins straight down
    from above, without its wrist or forearm touching the shelf above, the cabinet mouth, or the door.
11. The two arms do not collide at the cabinet, and the open door is clear of the right arm's path to
    the shelf.
12. If a zone cannot be reached, move it toward the arm that cannot reach it until lines 8 to 11 hold.

### Materials checklist

1. The **cabinet** is a countertop refrigerator standing on the table at the back center, squared to the
   back table edge, its mouth facing the front. It is heavy enough that it does not move when the drawer
   is pulled or the door is pressed shut.
2. The cabinet holds one **shelf** across its upper half and one **produce drawer** filling its lower
   half. There is nothing else inside it.
3. The **shelf** is level, dry, and split into three **zones** side by side, each named by a label on the
   shelf front edge, left to right: **DAIRY** (blue), **JARS** (green), **TUBS** (yellow).
4. Each zone is wide enough for two items to stand side by side without touching, and deep enough for
   two items to stand one behind the other with clear space between them.
5. There is clear space above the shelf, so an item stands in a zone without touching the cabinet roof.
6. **One older item stands at the back of each zone**, upright, label to the front: an older carton in
   DAIRY, an older jar in JARS, an older tub in TUBS. Nothing else is on the shelf.
7. The **produce drawer** pulls straight out toward the front to a stop and does not come free of the
   cabinet. It slides when pulled by its handle and does not need to be lifted.
8. The drawer floor is long enough front to back for three produce packs to lie flat in one row, and no
   wider than one pack, so there is one row and no choice of lane.
9. **One older produce pack lies flat at the back of the drawer** at the start. The drawer is shut.
10. The **door** is hinged on the cabinet's left front edge. It swings open to the left and it is standing
    open against the **door post** at the start of the episode.
11. The **door post** is a heavy fixed block at the back left of the table. The open door rests its outer
    face against it and stands steady there, with its inner face and both bins facing the front right.
12. The door carries two open topped bins on its inner face: the **tall bin** above and the **short bin**
    below. Both are open above along their whole length and are loaded straight down from above.
13. **One older bottle stands in the tall bin** and **one older small jar stands in the short bin**, each
    against the door face at the back of its bin. Both bins are otherwise empty.
14. The door shuts with a latch that holds it closed, and its seal runs all round the mouth. A correctly
    shut door shows no daylight along the seal and does not spring back open.
15. The **stock tray** sits on the table in the place for this episode's config, and the other two places
    are bare. It holds five new items standing upright in one row, none touching another, each label facing
    the front edge, in this order left to right: the **carton** (blue label), the **jar** (green label), the
    **tub** (yellow label), the **bottle**, the **small jar**.
    * **Config M:** front-center, against the front table edge, with clear table between it and the drawer
      when the drawer stands open at its stop
    * **Config R1:** front-right
    * **Config R2:** back-right, beside the cabinet, not touching it
16. Each new shelf item's label color matches its zone label: blue to DAIRY, green to JARS, yellow to
    TUBS. The bottle fits the tall bin only and the small jar fits the short bin only.
17. Every item on the stock tray stands on its own base unaided, is closed and dry, and is held by one
    gripper without its contents spilling.
18. The **produce staging** is the clear table at the front left. It holds the **two new produce packs**
    lying flat side by side, not touching, and nothing else.
19. Each produce pack is a sealed rigid pack that lies flat on one face, keeps its shape when gripped, and
    is short enough to lie in the drawer with clear space above it when the drawer is shut.
20. The table is clean, dry, and bare apart from the cabinet, the door post, the stock tray and its five
    items, and the two produce packs on the produce staging.

### Workspace layout

* **Cabinet:** the countertop refrigerator at the back center. It is never lifted, never turned, and never
  pushed out of its place.
* **Cabinet mouth:** the open front of the cabinet. Every gripper going to the shelf passes through it
  straight in from the front.
* **Shelf:** the one shelf in the cabinet, split into the three zones. All shelf work happens here.
* **Zones:** **DAIRY** at the left end of the shelf, **JARS** in the middle, **TUBS** at the right end. Each
  carries its own label on the shelf front edge. **Right gripper only.**
* **Shelf front lip:** the front edge of the shelf. Nothing may stick out past it, or the door will not shut.
* **Produce drawer:** the drawer filling the lower half of the cabinet. **Left gripper only.**
* **Door:** the cabinet door, hinged on the left, standing open against the door post for all the loading.
* **Door post:** the heavy fixed block at the back left of the table that the open door rests against. It is
  never moved.
* **Tall bin** and **short bin:** the two open topped bins on the door's inner face, the tall one above the
  short one. **Right gripper only.**
* **Stock tray:** the tray holding the five new items at episode start — front-center (**Config M**),
  front-right (**Config R1**), or back-right (**Config R2**). Empty at episode end. **Right gripper only.**
* **Produce staging:** the clear table at the front left holding the two new produce packs at episode start.
  Empty at episode end. **Left gripper only.**

### Arm assignments

* **Right gripper — the stock gripper.** Takes each item off the stock tray in all three configs, draws the
  older item forward in each shelf zone and each door bin, stands each new item in behind it, and presses the
  door fully shut at the end. In Config R2 it brings each item forward past the cabinet's right side and round
  to the front of the cabinet, never over the cabinet roof. It never touches the drawer, the produce, or the
  door post.
* **Left gripper — the drawer and door gripper.** Pulls the produce drawer open, draws the older produce
  pack forward, lays the two new produce packs in behind it, pushes the drawer shut, and swings the door off
  the post and round to the cabinet at the end. In Config M it carries each produce pack round the left of
  the stock tray, not over it. It never touches the shelf, a door bin, or the stock tray.
* Nothing is handed between grippers, and only one arm moves an object at a time.

## Vocabulary

* **Older stock:** anything already inside the cabinet when recording starts — the older carton, jar, tub,
  bottle, small jar, and produce pack. Older stock is never taken out of the cabinet.
* **New stock:** the seven items outside the cabinet when recording starts — the five on the stock tray and
  the two produce packs on the produce staging. All seven go in during the episode.
* **Stock tray place:** where the stock tray stands at the start of the episode — front-center (**Config M**),
  front-right (**Config R1**), or back-right (**Config R2**). One per episode, chosen before recording and
  never changed mid-episode.
* **Rotate forward:** draw the older item in that place toward the front of that place, so it stands in front
  of everything that goes in after it. It is done before any new item goes into that place.
* **Behind:** further from the front of that place. On the shelf, behind means nearer the back of the zone. In
  the drawer, behind means nearer the back of the drawer. In a door bin, behind means nearer the door face.
* **Front of the zone:** the part of the zone just inside the shelf front lip. An item drawn forward stands
  there, with nothing sticking out past the lip.
* **Outer rail:** the front wall of a door bin, the one away from the door face. An older bin item is drawn
  forward until it stands against the outer rail.
* **Stands on its own:** after the gripper moves clear, the item stays upright for 2 seconds and does not
  rock, lean, slide, or fall.
* **Upright and square:** the item stands on its own base with its label facing the front of the cabinet, not
  leaning, not lying on its side, and not turned to face a side wall.
* **Clear space:** the two items in a place do not touch each other, and the gap between them is visible from
  the front.
* **Shut flush:** the drawer face sits level with the cabinet front, with no part of it standing out.
* **Sealed:** the door face meets the cabinet all round, no daylight shows anywhere along the seal, the latch
  holds, and the door does not spring back when the gripper comes off.
* **Overhang the lip:** any part of an item sticks out past the shelf front lip into the doorway.

## Steps

Only Steps 1.3, 2.2, and 3.1 depend on where the stock tray is: the **right gripper** takes every item off
the tray in all three configs, but the path it carries the item along changes, and in Config M the **left
gripper** keeps the produce packs clear of the tray. Every other line is the same in all three configs.

### Step 1: Load the produce drawer

**Goal:** the older produce pack lies at the front of the drawer with the two new packs flat behind it, and
the drawer is shut flush.

#### 1.1 Pull the drawer open

* With the **left gripper**, close on the drawer handle at its left end.
* Draw the drawer straight out toward the front until it meets its stop. Do not jerk it, and do not pull
  after it has stopped.
* Do not lift the drawer, and do not let the cabinet slide forward with it.
* Open the **left gripper** and draw it clear of the drawer.

**Check:** the drawer stands open at its stop, the cabinet has not moved, and the whole drawer floor is
visible. If the cabinet moved, put it back square to the back table edge before going on.

#### 1.2 Rotate the older produce forward

* With the **left gripper** closed, come in from the front and set it against the back edge of the older
  produce pack.
* Push the pack forward along the drawer floor until it lies against the drawer front wall.
* Keep it flat the whole way. Do not lift it, and do not take it out of the drawer.

**Check:** the older pack lies flat against the drawer front wall, with clear drawer floor behind it. If it
turned as it slid, square it with the closed **left gripper** against its edges.

#### 1.3 Lay the two new packs in behind it

* With the **left gripper**, pick up the produce pack nearer the front table edge from the produce staging.
* Carry it level to the drawer and lay it flat on the drawer floor behind the older pack, with clear space
  between them. **IF Config M:** carry it round the left of the stock tray, not over it.
* Open the **left gripper** and draw it straight up clear of the drawer.
* Do the same with the second produce pack, laying it flat behind the first new pack.
* Lay every pack flat. Never stack one pack on another, and never stand a pack on edge.

**Check:** three packs lie flat in one row, older pack at the front, both new packs behind it, none stacked
and none standing above the drawer rim. If a pack sits on top of another, lift it with the **left gripper**
and lay it flat behind.

#### 1.4 Push the drawer shut

* With the **left gripper** closed, press the drawer face at its left end and push it straight back until it
  is shut flush.
* Push until the drawer stops. Do not push hard enough to move the cabinet.
* Draw the **left gripper** back clear of the cabinet. It stays clear until Step 4.

**Check:** the drawer is shut flush, nothing is caught in it, and the cabinet still stands square to the back
table edge. If the drawer stops short, pull it open with the **left gripper**, lay the packs flat again, and
shut it once more.

**Expected state:** drawer shut with three packs in it, produce staging empty, shelf still holding the three
older items only, door still open on the post.

### Step 2: Load the three shelf zones

**Goal:** each zone holds its older item at the front and its new item behind it, all standing upright and
square, with nothing overhanging the shelf front lip.

Work the zones in this fixed order: **DAIRY, then JARS, then TUBS** — the far zone first, so the **right
gripper** never reaches over an item it has just stood down. Run Steps 2.1 and 2.2 once per zone, three times.

#### 2.1 Rotate the older item forward

* With the **right gripper** closed, come in through the cabinet mouth from the front, level, and set it
  against the back of the older item in that zone.
* Draw the item forward along the shelf until it stands at the front of the zone, just inside the shelf front
  lip.
* Keep it standing the whole way. Do not lift it, do not tip it, and do not take it out of the cabinet.
* Draw the **right gripper** straight out of the cabinet mouth.

**Check:** the older item stands upright and square at the front of the zone, nothing sticks out past the shelf
front lip, and there is clear shelf behind it. If it leans, stand it up with the **right gripper**. If it stands
out past the lip, press it back with the closed **right gripper**.

#### 2.2 Stand the new item in behind it

Look where the stock tray is before reaching for the item.

* **IF the stock tray is at the front-center (Config M):** with the **right gripper**, close on the item for
  that zone on the stock tray — the carton for DAIRY, the jar for JARS, the tub for TUBS — gripping it around
  its body, not by its lid or cap. Lift it level and carry it straight back to the cabinet mouth.
* **IF the stock tray is at the front-right (Config R1):** with the **right gripper**, close on the item for
  that zone the same way. Lift it level and carry it left to the front of the cabinet mouth.
* **IF the stock tray is at the back-right (Config R2):** with the **right gripper**, close on the item for
  that zone the same way. Lift it level, bring it forward past the cabinet's right side, and round to the
  front of the cabinet mouth. Never carry it over the cabinet roof.

Then, in all three:

* Take it in through the cabinet mouth from the front. Do not carry it over the shelf items already standing
  and do not carry it over the door.
* Stand it down on the shelf behind the older item, upright and square, its label facing the front, with clear
  space between the two.
* Open the **right gripper** and draw it straight out of the cabinet mouth.

**Check after each zone:** two items stand in the zone, older at the front and new behind, both upright and
square, both labels facing the front, clear space between them, and nothing overhanging the shelf front lip. If
the new item leans or touches the older one, take it back up with the **right gripper** and stand it down again.
If it went into the wrong zone, take it up with the **right gripper** and stand it in the zone whose label color
matches it.

**Expected state after the third zone:** six items on the shelf, two in each zone, older in front of new in all
three, stock tray holding the bottle and the small jar only.

### Step 3: Load the two door bins

**Goal:** each door bin holds its older item against the outer rail with its new item behind it, and both items
stand on their own.

The door rests on the door post and stays there for the whole step. Work the **tall bin first, then the short
bin**, so the **right gripper** never reaches over an item it has just stood down.

#### 3.1 Load the tall bin

* With the **right gripper** closed, come straight down into the tall bin and set it against the back of the
  older bottle.
* Draw the bottle forward until it stands against the outer rail. Keep it standing, and do not lift it out.
* Draw the **right gripper** straight up out of the bin.
* With the **right gripper**, close on the new bottle on the stock tray around its body, lift it level, and carry
  it over to the bin. **IF Config M or R1:** carry it across the front of the cabinet to the bin. **IF Config R2:**
  bring it forward past the cabinet's right side and across the front of the cabinet to the bin, never over the
  cabinet roof.
* Lower it straight down into the bin behind the older bottle, stand it on the bin floor, and only then open the
  **right gripper**. Never drop or throw an item into a bin.
* Draw the **right gripper** straight up clear of the bin.

**Check:** both bottles stand upright in the tall bin, older against the outer rail and new behind it, clear space
between them, and the door still rests against the door post. If the door has moved off the post, stop and re-seat
it against the post with the **right gripper** before going on.

#### 3.2 Load the short bin

* Run the same motions as Step 3.1 with the **right gripper**, using the older small jar and the new small jar in
  the short bin: draw the older jar forward to the outer rail, then stand the new jar down behind it.
* Keep the gripper clear of the tall bin above it on the way in and out.

**Check:** both jars stand upright in the short bin, older against the outer rail and new behind it, clear space
between them, and the stock tray is empty.

**Expected state:** thirteen items in the cabinet, the stock tray and the produce staging both empty, the door still
open on the post.

### Step 4: Close the door fully

**Goal:** the door is shut and sealed, with no daylight along the seal and no spring back.

#### 4.1 Swing the door round

* Check first that both arms are clear of the cabinet mouth and that nothing sticks out past the shelf front lip.
* With the **left gripper**, close on the door's free edge at about its middle height.
* Swing the door away from the door post and round toward the cabinet in one smooth move. Do not swing it fast, and
  do not let it hit the cabinet.
* Stop when the door has come round in front of the cabinet mouth and its free edge is near the middle of the cabinet
  front.
* Open the **left gripper** and draw it back clear of the door.

**Check:** the door hangs in front of the cabinet mouth, nothing is caught between the door and the cabinet, and no
item has been knocked over. If an item was knocked over, swing the door open again with the **left gripper** and stand
the item up with the **right gripper** before going on.

#### 4.2 Press the door home

* With the **right gripper** closed, press the door's front face flat, at the free edge side, straight back toward the
  cabinet.
* Press until the door meets the cabinet all round and the latch holds. Hold the press for 2 seconds.
* Press straight back only. Do not slam the door, and do not press hard enough to move the cabinet.
* Draw the **right gripper** straight back off the door.

**Check:** the door is sealed — it meets the cabinet all round, no daylight shows anywhere along the seal, and the door
does not spring back when the **right gripper** comes off. If daylight shows or the door springs back, press it home
once more with the **right gripper**. If it still will not seal, swing it open with the **left gripper** and look for an
item overhanging the shelf front lip or standing proud of a bin.

**Expected state:** door shut and sealed, cabinet square to the back table edge, stock tray empty, produce staging
empty, door post still in its place.

### Step 5: End the episode

* Confirm the door: shut and sealed, no daylight along the seal, and no spring back.
* Confirm the table: the stock tray is empty, the produce staging is empty, and nothing is left on the table but the
  cabinet, the door post, and the tray.
* Confirm the cabinet: still square to the back table edge, and the door post still in its place.
* Confirm nothing is on the floor or lying on the table beside the cabinet.
* Correct any failed check before ending.
* Return both arms home with grippers open, then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Swing the door open by hand and rest it against the door post, outer face on the post, bins facing the front right.
2. Take the new carton, jar, and tub out of the shelf zones and stand them back on the stock tray in their row order,
   labels facing the front edge. Set the tray in the place for the next episode's config — front-center
   (Config M), front-right (Config R1), or back-right (Config R2).
3. Leave the older carton, jar, and tub on the shelf and slide each one back to the back of its own zone, upright and
   square, label facing the front.
4. Take the new bottle out of the tall bin and the new small jar out of the short bin, and stand them back on the stock
   tray in their row order.
5. Slide the older bottle and the older small jar back against the door face at the back of their own bins.
6. Pull the drawer open, take the two new produce packs out, and lay them flat side by side on the produce staging, not
   touching.
7. Push the older produce pack back to the back of the drawer, lying flat, and shut the drawer flush.
8. Wipe up any spill in the cabinet, on the shelf, in a bin, or in the drawer, and dry it.
9. Replace an item that leaks, that no longer stands on its own base, or whose lid or cap has come loose.
10. Replace a produce pack that has lost its shape or split.
11. Check the door still latches and seals when it is pushed shut by hand, and that it does not spring back.
12. Check the drawer still slides to its stop and shuts flush, and that the cabinet still stands square to the back table
    edge and does not slide.
13. Run both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what
the reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a
rule was broken.

### Violations

**Note on the start position:** the violations below were written for Config R1 (stock tray at the front-right).
The pickup and arm-role cues will be rewritten later to cover all three start positions; they are left as they
are for now. Until then, anything that does not match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the operator does does not match the config on the table — the stock tray is not in the
  place for the config; a gripper reaches across the table for a stock item or a produce pack; in Config R2 an
  item is carried over the cabinet roof; or the wrong IF line is followed.
* **SOP rule broken:** the start position and the same-side rule (the **right gripper** takes every item off the
  stock tray wherever it stands, the **left gripper** takes the produce from the front-left, no arm reaches
  across the table; the IF line followed is the one for the config on the table).
* **Coaching note:** look where the stock tray is before the first reach, then follow that config's IF lines
  through Steps 1.3, 2.2, and 3.1.

**Violation: Wrong loading order**

* **Visible cue:** the shelf or a door bin is loaded before the drawer is shut, the door bins are loaded before all three
  zones are done, the zones are not worked DAIRY, JARS, TUBS, the short bin is loaded before the tall bin, or a place is
  skipped and come back to.
* **SOP rule broken:** Steps 1 to 3, load the drawer and shut it, then the three zones left to right, then the tall bin and
  the short bin.
* **Coaching note:** drawer, shelf, bins, door. Far side first every time, so nothing is carried over what has just been
  stood down.

**Violation: Drawer opened or shut wrong**

* **Visible cue:** the **left gripper** jerks the drawer, keeps pulling after it has met its stop, lifts the drawer, drags
  the cabinet forward with it, or shuts the drawer without it sitting flush with the cabinet front.
* **SOP rule broken:** Steps 1.1 and 1.4, draw the drawer straight out to its stop and push it straight back until it is
  shut flush, without moving the cabinet.
* **Coaching note:** straight out to the stop, straight back to flush, and let go of the handle before the push.

**Violation: Older stock not rotated forward**

* **Visible cue:** a new item goes into a zone, a bin, or the drawer while the older item there is still at the back, or the
  older item is only part way forward and is left there.
* **SOP rule broken:** Steps 1.2, 2.1, 3.1, and 3.2, draw the older item forward to the front of its place before any new
  item goes in behind it.
* **Coaching note:** rotate first, then fill. Every place gets the old one moved before the new one arrives.

**Violation: New stock put in front of older stock**

* **Visible cue:** a new item ends up nearer the front of a zone, a bin, or the drawer than the older item of that place.
* **SOP rule broken:** Steps 1.3, 2.2, 3.1, and 3.2, the new item is stood down behind the older item every time.
* **Coaching note:** the older item is always the one you see first from the front. If the new one is in front, it is wrong.

**Violation: Older stock lifted or taken out**

* **Visible cue:** an older item is lifted off the shelf, out of a bin, or out of the drawer, is carried in the air, or is set
  down outside the cabinet.
* **SOP rule broken:** Steps 1.2, 2.1, 3.1, and 3.2, older stock is pushed or drawn along the surface it stands on and never
  leaves the cabinet.
* **Coaching note:** slide it, do not lift it. Nothing that starts in the cabinet comes out.

**Violation: Produce stacked or laid wrong**

* **Visible cue:** a produce pack is laid on top of another, stood on edge, laid across the row instead of along it, or left
  standing above the drawer rim.
* **SOP rule broken:** Step 1.3, lay every pack flat on the drawer floor in one row, none stacked.
* **Coaching note:** flat, in the row, one behind the other. A stacked pack blocks the drawer from shutting.

**Violation: Item put in the wrong zone**

* **Visible cue:** the **right gripper** stands an item down in a zone whose label color does not match the item's label, or
  the bottle or small jar is stood on the shelf.
* **SOP rule broken:** Step 2.2, the carton goes in DAIRY, the jar in JARS, the tub in TUBS, matched by label color.
* **Coaching note:** read the item label and the zone label before the arm goes in. Colors match, always.

**Violation: Item not stood upright and square**

* **Visible cue:** an item in a zone or a bin leans, lies on its side, stands turned so its label faces a side wall or the back,
  touches its neighbour, or rocks after the gripper moves clear.
* **SOP rule broken:** Steps 2.2, 3.1, and 3.2, stand every item on its own base, label facing the front, with clear space
  between the two items in that place.
* **Coaching note:** stand it down, watch it settle, then let go. Labels face the front so the next restock can read them.

**Violation: Item left overhanging the shelf front lip**

* **Visible cue:** an item on the shelf sticks out past the shelf front lip into the doorway when the **right gripper** moves on,
  or the door meets an item when it swings round.
* **SOP rule broken:** Steps 2.1 and 2.2, every item stands inside the shelf front lip, with nothing sticking out past it.
* **Coaching note:** an item over the lip is a door that will not shut. Press it back before you move on.

**Violation: Item gripped by its lid or cap**

* **Visible cue:** the **right gripper** closes on a carton flap, a jar lid, a tub lid, or a bottle cap instead of around the
  item's body, or a lid comes loose or lifts off as the item is carried.
* **SOP rule broken:** Step 2.2, close around the item's body, not on its lid or cap.
* **Coaching note:** grip the body low, where the item is solid. A lid is not a handle.

**Violation: Item carried over the loaded shelf or the open door**

* **Visible cue:** the **right gripper** carries an item over the items already standing on the shelf, over the open door, or
  over an open drawer, instead of going in level through the cabinet mouth or straight down into a bin.
* **SOP rule broken:** Steps 2.2, 3.1, and 3.2, carry each item level to the cabinet, in through the mouth from the front, and
  straight down into a bin.
* **Coaching note:** in from the front for the shelf, down from above for the bins, and never over something already placed.

**Violation: Item dropped into a bin**

* **Visible cue:** the **right gripper** opens above the bin and the item falls in, the item bounces or topples on landing, or it
  is thrown at the bin.
* **SOP rule broken:** Steps 3.1 and 3.2, lower the item until it stands on the bin floor, then open the gripper.
* **Coaching note:** stand it down, then let go. A dropped bottle knocks the door off the post.

**Violation: Door moved off the post during loading**

* **Visible cue:** the door swings, slides off the door post, or is knocked by an arm while the shelf or the bins are being
  loaded, or the door post is pushed out of its place.
* **SOP rule broken:** Steps 2 and 3, the door rests against the door post for the whole of the loading and the post is never
  moved.
* **Coaching note:** work the bins from straight above and the shelf from straight in front, and nothing pushes the door.

**Violation: Door swung round with an item still held or an arm still inside**

* **Visible cue:** the **left gripper** swings the door while the **right gripper** is still inside the cabinet mouth or is still
  holding an item, or the door catches an arm or an item as it comes round.
* **SOP rule broken:** Step 4.1, check both arms are clear of the cabinet mouth before the door is swung.
* **Coaching note:** everything out and empty first, then swing. The door does not wait for a hand.

**Violation: Door swung by the wrong gripper or slammed**

* **Visible cue:** the **right gripper** swings the door round, the **left gripper** grips it somewhere other than its free edge,
  or the door is swung fast enough to bang against the cabinet.
* **SOP rule broken:** Step 4.1, the **left gripper** closes on the door's free edge and swings it round in one smooth move.
* **Coaching note:** left gripper, free edge, smooth swing. A slammed door topples what you just stood up.

**Violation: Door not pressed fully home**

* **Visible cue:** daylight shows along the seal after the **right gripper** comes off, the door springs back open, the latch does
  not hold, or the press is released before 2 seconds.
* **SOP rule broken:** Step 4.2, press the door's front face straight back until it meets the cabinet all round and the latch
  holds, and hold the press for 2 seconds.
* **Coaching note:** press flat, hold two seconds, then watch it before you move away. A door left ajar is a failed restock.

**Violation: Door pressed wrong or cabinet moved**

* **Visible cue:** the **right gripper** presses the door at an angle, presses on its edge or a bin, or presses hard enough that the
  cabinet slides or turns out of square with the back table edge.
* **SOP rule broken:** Step 4.2, press the front face flat and straight back at the free edge side, without moving the cabinet.
* **Coaching note:** flat face, straight back, stop when it latches.

**Violation: More than one item moved at once**

* **Visible cue:** a gripper carries two items together, or two items move at the same time on the shelf, in a bin, or in the drawer.
* **SOP rule broken:** Steps 1 to 3, one item at a time, and only one arm moves an object at a time.
* **Coaching note:** one item, one place, one motion. Two at a time is how items go in the wrong zone.

**Violation: New stock left outside the cabinet**

* **Visible cue:** the episode moves on to Step 4 with an item still on the stock tray or a produce pack still on the produce staging.
* **SOP rule broken:** Steps 1 to 3, all seven new items go into the cabinet — two produce packs, three shelf items, two bin items.
* **Coaching note:** read the tray and the staging before the door swings. Both are empty when the loading is done.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected — a leaning item,
  a wrong zone, an item over the lip, a stacked pack, a drawer not flush, or a door showing daylight.
* **SOP rule broken:** Steps 1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 3.1, 3.2, 4.1, and 4.2, run each check and correct what it finds by the
  retry written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped, toppled, or knocked over**

* **Visible cue:** an item is dropped on the table or the floor, an item already standing is toppled by an arm or by the door, the drawer
  contents shift when it shuts, or the stock tray is knocked out of its place.
* **SOP rule broken:** Steps 1 to 4, nothing is dropped, toppled, or knocked out of its place, and every gripper leaves the cabinet
  straight out to the front or straight up.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **right gripper** touches the drawer, a produce pack, or the door post; the **left gripper** touches the shelf, a
  door bin, or the stock tray; or an item is handed from one gripper to the other.
* **SOP rule broken:** Steps 1 to 4, the **left gripper** works the drawer, the produce, and the door swing, the **right gripper** works
  the stock tray, the shelf, the bins, and the door press, and nothing changes hands.
* **Coaching note:** left arm low and left, right arm high and right. Nothing crosses.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with the door open or showing daylight, an item still on the stock tray or the produce staging, the
  drawer standing open, an item leaning or in the wrong zone, the cabinet out of square, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 5, confirm the door, the table, the cabinet, and the floor, then return both arms home with grippers open and
  stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a zone label, a bin, or the door seal**, so which zone an item went into or whether the door shut cannot be judged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Faulty door:** a door whose latch will not hold, whose seal will not close under a correct press, or that swings shut on its own off
  the door post.
* **Faulty drawer:** a drawer that jams, that will not run to its stop, that comes free of the cabinet, or that will not shut flush when
  correctly loaded.
* **Cabinet will not stay put:** a cabinet that slides or turns on the table under a correct drawer pull or a correct door press.
* **Door post will not hold:** a post that slides under the weight of the open door.
* **Defective item:** one that leaks, that will not stand on its own base, whose lid or cap comes off in a correct grip, or that slips out
  of a correct grip.
* **Defective produce pack:** one that has split, lost its shape, or will not lie flat on the drawer floor.
* **Zone too small:** a zone that will not hold its two items standing one behind the other with clear space between them.
* **Bin too small:** a bin that will not hold its two items standing side by side, or that is too shallow for the bottle to stand in it.
* **A place turns out to sit outside its arm's comfortable reach**, so the stock tray, a zone, a bin, the drawer, the produce staging, or the
  door's free edge cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Pull the produce drawer open
2. Slide the older produce pack forward in the drawer
3. Lay one new produce pack flat in the drawer
4. Push the produce drawer shut
5. Slide the older item forward in one shelf zone
6. Pick one item off the stock tray
7. Stand one new item down behind the older item in its zone
8. Slide the older bin item forward to the outer rail
9. Stand one new item down in a door bin
10. Swing the door round to the cabinet
11. Press the door home until it seals
12. Return both arms home and end the episode
