# Build a Multipack on a Tray SOP

One episode builds one multipack. The empty tray is already on the build spot, three units stand in
the unit lane, one overwrap sleeve stands on the sleeve spot with its open end facing the tray, and
one label lies on the label pad. The three units go onto the tray in printed order, the sleeve is
drawn over them along the table, the sleeve is seated down and squared on the tray, one label is
pressed onto the sleeve top panel, and the finished multipack is set on the stack at the front of the
table.

The order never changes: load, sleeve, seat and square, label, stack. The sleeve does not move before
all three units are on the tray, the sleeve is not squared before it is seated, the label does not go
on before the sleeve is seated and squared, and the multipack is not lifted to the stack before the
label is pressed.

The right gripper draws the sleeve on, seats and squares it, presses the label, and loads the units in
Config R. The left gripper holds the tray down while the sleeve comes on, holds the pack while the label
is pressed, squares the sleeve back only in the one case named in Step 3, takes the left end of the tray
for the stack lift, and loads the units in Config L and M. Every zone the right gripper works from is on
the right or at the center, the left gripper works only at the center, the front center, and the front
left, and nothing is folded, turned, or regripped in the air.

The table is set up in one of three ways. Only the unit lane moves; the tray on the build spot, the
sleeve spot, the label pad, and the stack spot are in the same place in all three.

* **Config L:** the unit lane is at the front left, left of the stack spot.
* **Config M:** the unit lane is at the center of the table, directly in front of the build spot and
  behind the stack spot.
* **Config R:** the unit lane is at the front right, left of the label pad.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line
that matches.

What stays constant across all sessions:

* **Start position:** the unit lane is at the front left (**Config L**), the center (**Config M**), or
  the front right (**Config R**). One config per episode, chosen before recording and never changed
  mid-episode.
* **Same-side rule:** the gripper on the unit lane's side loads the three units — the left gripper in
  Config L and M, the right gripper in Config R. No arm reaches across the table.
* **Fixed roles:** everything else is the same in all three configs — the right gripper draws the sleeve
  on, seats and squares it, and presses the label; the left gripper holds the tray during the draw and
  the press and squares the sleeve back only in the case named in Step 3.2; both grippers take the tray
  ends for the stack lift.

## Setup

Complete both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the build spot at the back center, the sleeve spot
   to its right, the unit lane in the zone for this episode's config, the label pad at the front right
   corner, and the stack spot at the front center.
3. The build spot is visible from above, so all three position outlines on the tray, the sleeve draw,
   the label patch, and the label press can be seen. The near window of the sleeve is visible from the
   front edge.
4. Both arms are at home with grippers open.
5. The table is bare apart from the tray, the three units, the sleeve, the label pad, and whatever
   multipacks are already on the stack spot.
6. The right arm reaches the sleeve spot, the label pad, the whole build spot, the right half of the
   stack spot, and (Config R) the unit lane at the front right. The left arm reaches the left end of the
   build spot, the left half of the stack spot, and (Config L and M) the unit lane and the whole build
   spot. Neither arm needs the other's zones.

### Materials checklist

1. One empty **tray** sits square on the **build spot** at the back center of the table, its long
   edges running left to right and clear table around it. Its floor carries three printed **position
   outlines** in one row, numbered 1, 2, and 3 from left to right.
2. Three **units** stand upright in the **unit lane**, one per **cell**. The cells are numbered 1, 2,
   and 3 from left to right, matching the position outlines. Every unit stands on its base with its
   **face label** toward the front edge. The lane sits in the zone for this episode's config and the
   other two zones are bare:
   * **Config L:** front left, left of the stack spot
   * **Config M:** center of the table, in front of the build spot and behind the stack spot
   * **Config R:** front right, left of the label pad
3. The three units are the same size and shape, each one fits inside its position outline with clear
   space around it, and each is light enough and narrow enough for one gripper to lift from above.
4. One **overwrap sleeve** stands on the **sleeve spot** to the right of the build spot, in line with
   it, with its open end facing the tray. The sleeve stands taller than a unit and its two walls sit
   wider apart than the tray, so it passes over the units and down around the outside of the tray.
5. The sleeve carries one cut **window** in its near wall, so all three unit faces are visible from
   the front edge once the sleeve is on, and one printed **label patch** on its top panel.
6. One **liner square** is taped flat on the **label pad** at the front right corner, carrying one
   **label** printed face up. The label's near edge is already lifted free of the liner, so a gripper
   takes the lifted edge and the label comes away on a straight lift.
7. The **stack spot** at the front center carries a printed **stack outline**. Multipacks finished in
   earlier episodes stay stacked on it as they are, squared and label face up.
8. Which face label the units carry varies between episodes. The count stays at three units, one
   sleeve, and one label.
9. The build spot, the stack spot, and the table around them are clear and dry.

### Workspace layout

* **Build spot:** back center, where the tray sits and every load, draw, seat, square, and press
  happens.
* **Sleeve spot:** right of the build spot and in line with it, one sleeve standing with its open end
  facing the tray.
* **Unit lane:** three numbered cells in one row, 1, 2, and 3 from left to right — front left, left of
  the stack spot (**Config L**), the center of the table between the build spot and the stack spot
  (**Config M**), or front right, left of the label pad (**Config R**). One per episode; the lane is
  empty when the episode ends.
* **Label pad:** front right corner, one liner square taped flat with one label on it, near edge
  lifted free.
* **Stack spot:** front center, printed stack outline, holding the multipacks finished so far.

The sleeve and the label are staged on the right; the unit lane is on the side of the gripper that
loads it. The build spot and the stack spot sit at the center, where both arms reach without stretching.

## Vocabulary

* **Arm assignment:** the right gripper lifts every unit out of the unit lane in Config R, draws the
  sleeve on, seats it, squares it left, takes the label off the liner, presses it, and takes the right
  end of the tray for the stack lift. The left gripper lifts every unit out of the unit lane in Config L
  and M, holds the tray down during the draw, holds the pack during the label press, squares the sleeve
  back in the one case named in Step 3.2, and takes the left end of the tray for the stack lift. Neither
  gripper takes over the other's work.
* **Tray:** the open tray on the build spot. Its **ends** are the short left and right sides that stay
  outside the sleeve once the sleeve is on, and they are the only grip points for the stack lift.
* **Position outline:** one printed shape on the tray floor, numbered 1 to 3 from left to right. Unit
  N goes into position N and nowhere else.
* **Unit:** one product going into the multipack. It stands on its base with its **face label** toward
  the front edge, in the cell and on the tray alike.
* **Unit lane:** the row of three numbered cells the units start in — front left (**Config L**), the
  center of the table in front of the build spot (**Config M**), or front right (**Config R**). One per
  episode, chosen before recording and never changed mid-episode.
* **Overwrap sleeve:** the card cover on the sleeve spot. It has a **top panel**, a **near wall**, and
  a **far wall**, it is open at both ends and open at the bottom, and it comes on by being drawn along
  the table, never lifted over the units.
* **Window:** the cut opening in the near wall of the sleeve. All three unit faces show through it
  once the sleeve is seated.
* **Seated:** both sleeve walls are down flat against the outside of the tray walls with their bottom
  edges level with the bottom of the tray, so the sleeve comes up with the tray when the tray is
  lifted.
* **Squared:** the sleeve runs straight along the tray with its open ends parallel to the tray ends
  and the same length of tray showing at each end.
* **Multipack:** the tray, the three units, and the seated and squared sleeve, once the label is
  pressed. It is handled as one thing from Step 5 on.
* **Label:** the one printed label on the liner square. It is taken by its lifted near edge, carried
  with the adhesive face down, and pressed once onto the label patch.
* **Flat hold:** a gripper closed and resting on the tray or on a sleeve wall to keep the pack from
  sliding while the other gripper works. It goes on before the work starts and comes off after the
  working gripper is clear.
* **Lift:** coming straight down onto the grasp point, closing, and raising straight up until there is
  daylight under the thing, before anything moves sideways.
* **Lower on:** carrying level over the target, lowering straight down until the thing is resting, and
  releasing once it is resting. Nothing is dropped from height.
* **Settled:** the thing stays put for 2 seconds after the gripper lifts clear, with nothing sliding,
  toppling, or hanging over an edge.
* **Release point:** inside the position outline the unit is going into, on the label patch, or on the
  stack spot. A gripper opens nowhere else.

## Steps

Steps 1 to 5 build the multipack in one pass, in that order. Only the pick in Step 1 and the carry in
Step 5.2 depend on the config: the gripper on the lane's side loads the units — the **left gripper** in
Config L and M, the **right gripper** in Config R — and in Config M the multipack passes over the empty
lane on its way to the stack. Every other line is the same in all three configs. Step 6 ends the episode
once the multipack is on the stack.

### Step 1: Load the three units onto the tray

**Goal:** all three units standing upright inside their matching position outlines, face labels toward
the front edge.

Look where the unit lane is before reaching for the first unit.

* **IF the unit lane is at the front left (Config L):** the **left gripper** closes on the unit in
  **cell 1** across its narrow sides, lifts it straight up, carries it level back and to the right,
  behind the stack spot, to the tray, lowers it into **position 1** until it is resting on the tray
  floor, and releases.
* **IF the unit lane is at the center, in front of the build spot (Config M):** the **left gripper**
  closes on the unit in **cell 1** across its narrow sides, lifts it straight up, carries it level
  straight back to the tray, lowers it into **position 1** until it is resting on the tray floor, and
  releases.
* **IF the unit lane is at the front right (Config R):** the **right gripper** closes on the unit in
  **cell 1** across its narrow sides, lifts it straight up, carries it level over the tray, lowers it
  into **position 1** until it is resting on the tray floor, and releases.

Then, in all three:

* Do the same for the units in cells 2 and 3, in that order, with the same gripper. Unit N always goes
  into position N.
* Take one unit per trip and finish it before the next one comes out of the lane.
* Carry each unit the way it stood in its cell, face label toward the front edge. Nothing is turned in
  the air.
* The other gripper stays clear of the build spot for the whole step.

**Check:** all three cells are empty, all three units stand upright inside their matching position
outlines with their face labels toward the front edge, no unit leans on another or on a tray wall, and
no unit hangs outside its outline. If a unit lands outside its outline, leans, or has turned, lift it
clear and lower it again.

### Step 2: Draw the sleeve over the loaded tray

**Goal:** the sleeve drawn along the table until it stands over all three units with its walls down
around the tray.

* The **left gripper** takes a **flat hold** on the **left end** of the tray and keeps it for the whole
  draw, so the tray stays on the build spot as the sleeve comes on.
* The **right gripper** closes on the **top panel** of the sleeve at its right edge, draws it straight
  left along the table so it passes over the three units and its two walls straddle the tray, and keeps
  drawing until the sleeve stands roughly over the middle of the tray with tray showing at both ends.
* The **right gripper** releases once the sleeve is over the tray, and the **left gripper** keeps its
  flat hold into Step 3.

The sleeve is drawn along the table in one motion. Never lift the sleeve off the table and lower it
over the units, and never draw it back to the right once it is on.

**Check:** the sleeve stands over all three units, its two walls sit outside the tray walls, tray shows
at both ends, and no unit has been knocked over or dragged out of its outline. If a unit has moved,
draw the sleeve back off to the right, stand the unit in its outline again, and draw the sleeve on
again.

### Step 3: Seat the sleeve and square it on the tray

**Goal:** the sleeve seated down on the tray and squared, with the same length of tray showing at each
end.

The left gripper keeps its flat hold on the left end of the tray for both substeps unless it is the
gripper doing the squaring.

#### 3.1 Seat the sleeve down

* The **right gripper** closes and presses down on the middle of the **top panel** for 2 seconds, so
  both walls settle fully down against the outside of the tray walls, then lifts straight off.

**Expected state:** both sleeve walls are down flat against the tray walls with their bottom edges
level with the bottom of the tray, and all three unit faces show through the window.

#### 3.2 Square the sleeve on the tray

* If more tray shows at the **left end** than at the right, the sleeve sits too far right: the **right
  gripper** presses flat against the sleeve's right end and slides it left until the same length of
  tray shows at each end.
* If more tray shows at the **right end** than at the left, the sleeve sits too far left: the **left
  gripper** releases its flat hold, presses flat against the sleeve's left end, and slides it right
  until the same length of tray shows at each end. The **right gripper** takes a flat hold on the right
  end of the tray while this happens.
* If the sleeve already shows the same length of tray at each end, neither gripper touches it.
* Both grippers come clear once the sleeve is square.

The sleeve is squared by pressing an end along the tray. Never lift the sleeve to place it again and
never lift the tray to shake it square.

**Check:** both sleeve walls are down flat against the outside of the tray walls with their bottom
edges level with the bottom of the tray, the sleeve runs straight along the tray, the same length of
tray shows at each end, all three unit faces show through the window, and no unit has toppled. If a
wall is still standing proud of the tray, press the top panel down again.

### Step 4: Label the multipack

**Goal:** one label pressed down flat inside the label patch on the sleeve top panel.

* The **left gripper** takes a **flat hold** on the **left end** of the tray and keeps it for the whole
  press.
* The **right gripper** closes on the lifted near edge of the **label**, lifts it straight up off the
  liner square, carries it level to the build spot with the adhesive face down, lowers it onto the
  **label patch** with its printed face up and its long edges running left to right, presses it down
  for 2 seconds, and lifts straight off.
* The **left gripper** releases the flat hold once the right gripper is clear.

One label, one press, inside the patch and nowhere else. The label is laid down once. Do not lift a
stuck label to place it again, because the adhesive loses its hold on a second try.

**Check:** the label lies flat inside the label patch, printed face up, pressed down across its whole
width with no corner lifting, and the sleeve is still seated and square. If a corner lifts, press along
it again.

### Step 5: Stack the multipack

**Goal:** the finished multipack resting on the stack spot, squared with the pack below it, label face
up and window toward the front edge.

#### 5.1 Lift the multipack

* The **left gripper** closes on the **left end** of the tray and the **right gripper** closes on the
  **right end**. Both grippers close before either arm lifts.
* Both arms lift the multipack straight up together until there is daylight under the tray, keeping it
  level.

#### 5.2 Set it on the stack

* **IF Config M:** the empty unit lane lies between the build spot and the stack spot; both arms lift
  the multipack high enough to clear it before carrying it forward. **IF Config L or R:** the path to
  the stack spot is bare table.
* Both arms carry the multipack level toward the front edge to the **stack spot** and lower it straight
  down onto the pack already on the stack, or onto the printed stack outline if the stack is empty,
  until it is resting.
* Both grippers release together once it is resting, then both arms lift clear.

The multipack is carried level on the two tray ends and set down in the orientation it was built in.
Never carry it by the sleeve, never tilt it, and never slide it into place after it is down.

**Check:** the multipack rests on the stack with its edges flush with the pack below it or inside the
stack outline, label face up, window toward the front edge, the sleeve still seated and square, all
three units still upright, and the stack standing straight with nothing overhanging. If the pack lands
off square, lift it clear with both grippers and lower it again.

### Step 6: Confirm the multipack and end the episode

* Confirm the multipack stands squared on the stack with its label face up and the packs stacked in
  earlier episodes untouched, and confirm the three cells of the unit lane are empty, the sleeve spot
  is empty, the liner square is bare, and the build spot and the table are otherwise clear.
* Return both arms home, clear of the stack spot and the build spot, then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Leave the finished multipack on the stack. When the stack reaches three multipacks, lift them off
   and break each one down as below, then clear the stack spot back to a bare stack outline.
2. To break a multipack down: draw the sleeve off the tray to the right and stand it on the sleeve
   spot with its open end facing the build spot.
3. Take the used label off the top panel and discard it. Labels are single use.
4. Lift the three units out and stand each one back in its cell in the unit lane, on its base with the
   face label toward the front edge, with the lane set for the next episode's config — front left
   (Config L), the center in front of the build spot (Config M), or front right (Config R) — and the
   other two zones bare.
5. Set the empty tray back on the build spot, square, long edges running left to right, with clear
   table around it.
6. Check the sleeve for a crushed wall, a torn window, or a wall that will not stand wide enough to
   pass over the tray. Swap in a fresh sleeve if it will not stand open on its own.
7. Lift the near edge of a fresh label free of the liner square and leave it on the label pad, printed
   face up. Confirm the liner square is still taped flat.
8. Change which face label the units carry between episodes rather than running the same one every
   time. The count stays at three units, one sleeve, and one label.
9. Wipe the table around the build spot and the stack spot and confirm the surface is clean and dry. A
   dusty table lets the tray slide under a flat hold.
10. Run both Setup checklists again.

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

**Note on the start position:** the violations below were written for Config R (unit lane at the front
right, loaded by the right gripper). The pickup and arm-role cues will be rewritten later to cover all
three start positions; they are left as they are for now. Until then, anything that does not match the
episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the operator does does not match the config on the table — the unit lane is not
  in the zone for the config; a gripper reaches across the table for a unit; or the wrong IF line is
  followed.
* **SOP rule broken:** the start position and the same-side rule (the left gripper loads the units in
  Config L and M, the right gripper in Config R; no arm reaches across the table; the IF line followed
  is the one for the config on the table).
* **Coaching note:** look where the unit lane is before the first reach, then follow that config's IF
  lines through Steps 1 and 5.

**Violation: Wrong order**

* **Visible cue:** the sleeve moves before all three units are on the tray, the sleeve is squared
  before it is seated down, the label goes on before the sleeve is seated and squared, or the multipack
  is lifted to the stack before the label is pressed.
* **SOP rule broken:** Steps 1 to 5, the order never changes: load, sleeve, seat and square, label,
  stack.
* **Coaching note:** load, sleeve, seat and square, label, stack. Finish the step you are in before you
  start the next one.

**Violation: Units loaded out of order**

* **Visible cue:** the units leave the lane in an order other than 1, 2, 3, so a gripper carries a unit
  over a unit already standing on the tray.
* **SOP rule broken:** Step 1, take the units in printed order 1 to 3 and put unit N into position N.
* **Coaching note:** count up from one. Nothing travels over a unit already standing.

**Violation: Unit in the wrong position or outside its outline**

* **Visible cue:** a unit is released on a position outline whose number does not match its cell, or it
  is released overhanging its outline, leaning on a neighbouring unit, or resting on a tray wall, and
  the next unit is picked anyway.
* **SOP rule broken:** Step 1, unit N goes into position N and nowhere else, standing upright inside
  its outline, and a bad landing is corrected by lifting it clear and lowering it again.
* **Coaching note:** each unit gets its own outline, flat on its base. Fix it before the next trip.

**Violation: Unit face turned**

* **Visible cue:** a unit lands with its face label toward a side wall or away from the front edge, or
  it is turned between the lift and the set down.
* **SOP rule broken:** Step 1, carry each unit the way it stood in its cell, face label toward the
  front edge.
* **Coaching note:** the face is set in the cell. Carry it straight across and put it down that way.

**Violation: More than one unit handled at once**

* **Visible cue:** two units are carried in one trip, a unit is moved while another is still in the
  other gripper, or the lane is emptied in a sweep.
* **SOP rule broken:** Step 1, take one unit per trip and finish it before the next one comes out.
* **Coaching note:** one unit, one position, one trip.

**Violation: Arms swapped roles**

* **Visible cue:** the left gripper takes a unit out of the lane, draws the sleeve on, seats it, or
  takes the label off the liner; or the right gripper is the one holding the tray down while the sleeve
  is drawn on.
* **SOP rule broken:** Steps 1 to 5, the right gripper loads the units, draws the sleeve on, seats and
  squares it, and presses the label; the left gripper holds the tray and the pack, and squares the
  sleeve back only in the case named in Step 3.2.
* **Coaching note:** the right arm does the work, the left arm holds. Neither reaches into the other's
  zones.

**Violation: Tray not held during the draw**

* **Visible cue:** the left gripper is off the tray while the sleeve is drawn on, or the tray slides
  off the build spot, turns, or is pushed along with the sleeve.
* **SOP rule broken:** Step 2, the left gripper takes a flat hold on the left end of the tray and keeps
  it for the whole draw.
* **Coaching note:** anchor the tray first. The sleeve moves, the tray does not.

**Violation: Sleeve lifted over the units**

* **Visible cue:** the sleeve leaves the table and is carried over the units and lowered onto them,
  instead of being drawn along the table onto the tray.
* **SOP rule broken:** Step 2, the sleeve is drawn straight left along the table and is never lifted
  off the table and lowered over the units.
* **Coaching note:** keep it on the table and push it on. Nothing goes over the top.

**Violation: Sleeve drawn back off the tray**

* **Visible cue:** the sleeve is drawn back to the right after it is on, or it is worked on and off the
  tray more than once, with no unit having been knocked over.
* **SOP rule broken:** Step 2, the sleeve is drawn on in one motion and is not drawn back to the right
  once it is on, except to stand a knocked unit up again.
* **Coaching note:** one draw, all the way on. Only a toppled unit buys a second try.

**Violation: Unit knocked over by the sleeve and left**

* **Visible cue:** a unit topples, turns, or is dragged out of its outline as the sleeve comes over,
  and the seat or the label goes ahead anyway.
* **SOP rule broken:** Step 2, a unit that has moved is corrected by drawing the sleeve back off,
  standing the unit in its outline again, and drawing the sleeve on again.
* **Coaching note:** look through the window before you press. A leaning unit does not get sealed in.

**Violation: Sleeve not seated**

* **Visible cue:** a sleeve wall stands proud of the tray wall, a bottom edge sits high above the
  bottom of the tray, or the top panel is never pressed down, and the label goes on anyway.
* **SOP rule broken:** Step 3.1, press the middle of the top panel down for 2 seconds so both walls
  settle fully down against the outside of the tray walls.
* **Coaching note:** press the middle, hold two, then look along both walls.

**Violation: Sleeve left off square**

* **Visible cue:** the sleeve sits with clearly more tray showing at one end than the other, or cocked
  across the tray, and the label goes on anyway.
* **SOP rule broken:** Step 3.2, the sleeve runs straight along the tray with the same length of tray
  showing at each end.
* **Coaching note:** check both ends against each other, then press the end that is long.

**Violation: Sleeve squared by lifting**

* **Visible cue:** the sleeve is lifted off the tray to place it again, or the tray is lifted or shaken
  to settle the sleeve, instead of an end being pressed along the tray.
* **SOP rule broken:** Step 3.2, the sleeve is squared by pressing an end along the tray, never by
  lifting the sleeve or the tray.
* **Coaching note:** it slides square on the table. Nothing comes up off the build spot yet.

**Violation: Label pressed off the patch**

* **Visible cue:** the label lands outside the printed label patch, across a sleeve edge, on a sleeve
  wall, on the tray, or on the table, or more than one label goes down.
* **SOP rule broken:** Step 4, one label pressed down inside the label patch on the sleeve top panel
  and nowhere else.
* **Coaching note:** find the patch first, then bring the label down on it.

**Violation: Label not pressed, or laid down twice**

* **Visible cue:** the label touches the patch and comes away at once, is pressed at one corner only,
  lifts at a corner afterwards, or is peeled back off the sleeve and laid down a second time.
* **SOP rule broken:** Step 4, press the label down for 2 seconds, lift straight off, and lay it down
  once without lifting a stuck label to place it again.
* **Coaching note:** down, hold two, straight up. The adhesive will not hold a second try.

**Violation: Pack not steadied during the label press**

* **Visible cue:** the left gripper is off the tray while the label is pressed, or the pack slides,
  turns, or lifts with the label on the way out.
* **SOP rule broken:** Step 4, the left gripper takes a flat hold on the left end of the tray and keeps
  it for the whole press.
* **Coaching note:** the flat hold goes on before the label touches and comes off after the gripper is
  clear.

**Violation: Multipack lifted with one gripper or by the sleeve**

* **Visible cue:** one arm lifts the multipack on its own, one gripper closes and lifts before the
  other has closed, or a gripper takes hold of the sleeve, the top panel, or a unit to lift the pack.
* **SOP rule broken:** Step 5.1, both grippers close on the two tray ends before either arm lifts, and
  the tray ends are the only grip points.
* **Coaching note:** both ends, both closed, then up together.

**Violation: Multipack tilted or released one gripper at a time**

* **Visible cue:** the pack tips out of level during the carry, a unit shifts or topples inside the
  sleeve, or one gripper opens while the other is still holding the pack.
* **SOP rule broken:** Step 5, carry the multipack level on the two tray ends and release both grippers
  together once it is resting.
* **Coaching note:** keep it flat all the way across, and let go with both at the same time.

**Violation: Multipack stacked off square**

* **Visible cue:** the pack lands overhanging the pack below it, turned across the stack, outside the
  stack outline, label face down, or window facing away from the front edge, and it is left there.
* **SOP rule broken:** Step 5.2, the multipack rests with its edges flush with the pack below or inside
  the stack outline, label face up and window toward the front edge, and a pack that lands off square
  is lifted clear with both grippers and lowered again.
* **Coaching note:** line it up with the pack below before you lower. Fix it with a lift, not a shove.

**Violation: Turned in the air**

* **Visible cue:** a unit, the label, or the multipack is rotated or flipped between the lift and the
  set down, so it lands facing a different way than it was carried.
* **SOP rule broken:** Steps 1, 4, and 5, nothing is turned in the air; the orientation it was staged
  in is the orientation it lands in.
* **Coaching note:** the wrist does not have the range to turn it in transit.

**Violation: Dragged instead of lifted**

* **Visible cue:** a unit, the label, or the multipack slides along the lane, the liner, or the table
  still touching it, with no daylight under it in transit. The sleeve draw in Step 2 and the square
  press in Step 3.2 are not this.
* **SOP rule broken:** Steps 1, 4, and 5, lift straight up until there is daylight before moving
  sideways.
* **Coaching note:** the lift is its own motion, not the start of the carry.

**Violation: Dropped onto the tray or pressed down**

* **Visible cue:** a gripper opens above the tray or above the stack and the thing falls into place, or
  a unit is pressed or patted down after it is resting in its outline.
* **SOP rule broken:** Steps 1 and 5, lower the thing until it is resting and release once it is
  resting.
* **Coaching note:** take it all the way down, then let go. Leave it how it lands.

**Violation: Regripped in the air**

* **Visible cue:** a gripper shifts, rolls, or seats its hold again on a unit, the sleeve, the label, or
  the multipack without setting it down first.
* **SOP rule broken:** Steps 1 to 5, set it down before taking a new hold.
* **Coaching note:** put it down before you take a new hold.

**Violation: Gripper released over the wrong place**

* **Visible cue:** a gripper opens over the unit lane, over the label pad, over the sleeve spot, over a
  tray wall, over a unit, or over open table.
* **SOP rule broken:** Steps 1 to 5, a gripper opens inside the position outline the unit is going into,
  on the label patch, or on the stack spot, and nowhere else.
* **Coaching note:** know where it lands before you open the gripper.

**Violation: Placement corrected by shoving**

* **Visible cue:** a gripper nudges, pats, or slides a unit, the label, or the stacked multipack into
  position after releasing it, instead of lifting it clear and placing it again. The prescribed square
  press in Step 3.2 is not this.
* **SOP rule broken:** Steps 1, 4, and 5, correct a bad placement by lifting the thing clear and placing
  it again.
* **Coaching note:** lift it and lay it again, or leave it alone.

**Violation: Dropped, collided, or knocked something over**

* **Visible cue:** a unit, the sleeve, the label, or the multipack falls to the table or the floor short
  of its spot, the tray is struck and shifts off the build spot, the unit lane is knocked out of place,
  the stack is toppled or shifted off its outline, the liner square is torn off the table, or the two
  arms strike each other.
* **SOP rule broken:** Steps 1 to 5, keep each thing on a clear travel path and release only after a
  settled placement.
* **Coaching note:** check the path and the landing spot before you move.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a unit still in the lane, the sleeve still on the sleeve spot
  or not seated, the label still on the liner, the multipack still on the build spot, a pack from an
  earlier episode moved, an arm away from home, or an arm still over the stack spot or the build spot.
* **SOP rule broken:** Step 6, confirm the stacked multipack and the empty lane, sleeve spot, liner, and
  build spot; return both arms home clear of the scene; then stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode,
and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Defective unit:** a unit that breaks, leaks, or will not stand on its base, or a face label that
  cannot be read once it is in its cell. Replace it before the next episode.
* **Unit does not fit its outline:** the printed outline is smaller than the unit, or two neighbouring
  outlines are too close for both units to stand clear. Reprint the tray floor before the next episode.
* **Sleeve fault:** a sleeve whose walls have collapsed inward so it will not pass over the tray, one
  too tight to draw on under a steady push, one too loose to stay on the tray when the tray is lifted,
  or one with a torn window. Swap in a fresh sleeve before the next episode.
* **Defective label:** a label whose near edge will not stay lifted off the liner, that tears on the
  lift, or whose adhesive will not take hold under a correct press because it has gone dead or picked
  up lint. Swap in a fresh label before the next episode.
* **Liner square lifts** off the table with the label because its tape has failed. Tape it flat again
  before the next episode.
* **Tray fault:** a warped tray floor that will not let three units stand, a tray too wide for the
  sleeve, or a tray end that has torn away so there is no grip point for the stack lift. Replace the
  tray before the next episode.
* **Stack fault:** a pack from an earlier episode that has sagged or gone off square, so a new pack will
  not sit flush on it. Clear the stack before the next episode.
* **Tray or multipack slides** under a correct flat hold because the table is dusty or slick. Wipe the
  table before the next episode.

## Annotation subtasks (from SOP)

1. Place one unit into its matching position outline on the tray
2. Draw the overwrap sleeve over the loaded tray
3. Seat the sleeve down on the tray
4. Square the sleeve along the tray
5. Take one label off the liner square
6. Press the label onto the sleeve top panel
7. Lift the multipack by both tray ends
8. Set the multipack on the stack
9. Return both arms home and end the episode
