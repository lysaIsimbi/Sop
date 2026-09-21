# Assemble a Flat-Pack Drawer Box SOP (1x Episode: 1 Drawer Box)

One episode assembles one drawer box. The table begins with a flat cardboard blank lying on the
assembly spot just right of the center of the table, the sleeve behind it with its mouth facing the
front edge, a tray of six numbered items at the front-right, and the divider on its own spot.

The order never changes: fold the two long walls up, lock the right wall, lock the left wall, drop the
divider in, load six items, then slide the drawer into the sleeve. No divider goes in before all four
corner tabs are seated, no item goes in before the divider is flat on the bottom, and the drawer never
goes into the sleeve before all six pockets are filled.

The right gripper folds the far wall, the near wall, and the right wall, seats all four corner tabs,
lowers the divider in, loads all six items, and pushes the drawer into the sleeve. The left gripper
presses the blank flat, folds the left wall up and holds it in, steadies the drawer while the divider
and the items go in, and holds the sleeve down during the slide. The left gripper works from the left
side onto the drawer and never reaches past the drawer's left wall. The right gripper stays on the
drawer, the tray, the divider spot, and the sleeve.

The table is set up in one of three ways. Only the divider moves; the blank, the sleeve, and the item tray
are in the same place in all three.

* **Config L:** the divider is at the back-left, level with the sleeve.
* **Config M:** the divider is at the front-center, in front of the assembly spot.
* **Config R:** the divider is at the right of the assembly spot.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the divider starts at the back-left (**Config L**), the front-center (**Config M**)
  or the right of the assembly spot (**Config R**). One config per episode, chosen before recording and
  never changed mid-episode.
* **Same-side rule:** the gripper on the divider's side takes it — the left gripper in Config L and M, the
  right gripper in Config R. No arm reaches across the table.
* **Hand-over rule:** in Config L and M the left gripper never reaches over the drawer, so it **hands the
  divider over** to the right gripper just in front of the drawer's near wall: the left gripper holds the
  divider still, the right gripper closes on the opposite end of its long wall, and only then does the left
  gripper open. The right gripper lowers it in. Nothing is handed over in Config R.
* **Fixed roles:** the right gripper folds, seats, loads, and pushes; the left gripper presses, folds the
  left wall, steadies, and holds the sleeve. The fold order, the divider-before-items rule, the load order,
  and the sleeve slide are the same in all three configs.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the assembly spot, the sleeve behind it, the item
   tray at the front-right, and the divider spot for this episode's config.
3. The blank is visible from above, so all four score lines, all four corner tabs, and all four tab
   slots can be seen.
4. Both arms are at home with grippers open.
5. The table is bare apart from the blank, the sleeve, the item tray, the divider, and robot hardware.
6. The right arm reaches the item tray, the divider spot (Config R), the whole drawer, and the sleeve.
   The left arm reaches the drawer's left wall, the left side of the sleeve, and the divider spot (Config L
   and M) without stretching.

### Materials checklist

1. One flat **blank** lies on the **assembly spot**, just right of the center of the table. It lies
   square to the front edge with the face that becomes the inside of the drawer facing up, and all four
   walls unfolded flat on the table.
2. The blank carries a **tab slot** at each end of the far wall and each end of the near wall, and a
   **corner tab** at each end of the left wall and the right wall — four tabs and four slots in total.
   All eight are clear of tape, dust, and crushed cardboard.
3. One **sleeve** sits directly behind the assembly spot, away from the front edge, lying flat on the
   table. Its **mouth** faces the front edge and lines up square with the blank. Its far end is closed.
4. One **divider** lies flat on the **divider spot** with its pocket openings facing up and its long wall
   running left to right:
   * **Config L:** back-left, level with the sleeve
   * **Config M:** front-center, in front of the assembly spot
   * **Config R:** right of the assembly spot
5. One **item tray** sits at the front-right, holding six **items**, one per **cell**. The cells are
   numbered like the pockets: cells 1, 2, and 3 in the far row, left to right, and cells 4, 5, and 6 in
   the near row, left to right. Every item carries a **number label** facing up and readable from
   above.
6. Keep the left side of the table clear apart from the divider in Config L. The left gripper works from
   there onto the drawer.
7. Before collection, confirm by hand that each wall folds up on its score line, that all four tabs
   seat with a light press, that the divider drops to the bottom of the folded drawer without being
   forced, that each item sits in its pocket below the rim of the drawer, and that the loaded drawer
   slides into the sleeve with a light push.

### Workspace layout

- **Assembly spot:** just right of the center of the table — the blank is folded, filled, and pushed
  from here
- **Sleeve spot:** directly behind the assembly spot, mouth facing the front edge
- **Front-right supply zone:** item tray with six numbered items
- **Divider spot:** the divider, lying flat, pockets facing up — back-left (Config L), front-center in
  front of the assembly spot (Config M), or right of the assembly spot (Config R)
- **Left side:** kept clear, so the left gripper can come in onto the drawer; in Config L only the divider
  lies there, at the back-left

### Arm assignments

- **Left gripper:** presses the bottom panel flat during the first folds, folds the left wall up and
  holds it in while its tabs are seated, steadies the drawer by its left wall while the divider and the
  items go in, and holds the sleeve down flat during the slide. In Config L and M it also fetches the
  divider and hands it to the right gripper in front of the drawer.
- **Right gripper:** folds the far wall, the near wall, and the right wall, seats all four corner tabs,
  lifts the divider in (from the divider spot in Config R, from the hand-over in Config L and M), loads all
  six items in order, and pushes the drawer into the sleeve.

## Vocabulary

- **Blank:** the flat cut piece of cardboard that becomes the drawer. It starts lying flat on the
  assembly spot with the face that becomes the inside of the drawer facing up.
- **Score line:** a pressed line on the blank that shows where a wall folds. Every fold in this task is
  made on a score line.
- **Bottom panel:** the middle rectangle of the blank. It stays flat on the table and becomes the floor
  of the drawer.
- **Far wall:** the long wall on the side away from the front edge. It carries a tab slot at each end.
- **Near wall:** the long wall on the side nearest the front edge. It carries a tab slot at each end.
- **Left wall:** the short end wall on the left. It carries a corner tab at each end.
- **Right wall:** the short end wall on the right. It carries a corner tab at each end.
- **Corner tab:** a small flap on the end of the left wall or the right wall that slides into a tab
  slot and locks that corner. There are four.
- **Tab slot:** the cut opening at the end of the far wall or the near wall that a corner tab slides
  into.
- **Seated tab:** the tab is all the way through its slot, lies flat against the wall, and does not
  spring back out when the right gripper lets go.
- **Locked corner:** the two walls at that corner meet with no gap, and the tab there is seated.
- **Square drawer:** all four walls stand upright, all four corners are locked, and the bottom panel is
  still flat on the table.
- **Rim:** the top edges of the four standing walls.
- **Divider:** the cardboard insert that drops into the drawer and splits it into six pockets. It comes
  already put together as one stiff piece and is never taken apart.
- **Divider spot:** where the divider lies at the start of the episode — back-left (**Config L**),
  front-center (**Config M**), or right of the assembly spot (**Config R**). One per episode, chosen before
  recording and never changed mid-episode.
- **Hand over:** the left gripper holds the divider still, level, just in front of the drawer's near wall;
  the right gripper closes on the top edge of the long wall at the opposite end, and only then does the
  left gripper open and lift clear. Config L and M only, because the left gripper never reaches over the
  drawer.
- **Pocket:** one of the six spaces the divider makes inside the drawer. Pockets 1, 2, and 3 are the
  far row, left to right. Pockets 4, 5, and 6 are the near row, left to right.
- **Divider seated:** the divider rests flat on the bottom panel all the way around, its long wall runs
  left to right, and its short walls run front to back.
- **Item:** one of the six numbered objects in the item tray. Item 1 goes in pocket 1, item 2 in pocket
  2, and so on.
- **Item loaded:** the item rests on the drawer floor inside its own pocket, its number label faces up,
  and no part of it stands above the rim.
- **Sleeve:** the cardboard cover the finished drawer slides into. It is open at the mouth and closed at
  the far end.
- **Sleeve mouth:** the open end of the sleeve, facing the front edge.
- **Drawer fully in:** the drawer has slid in until it stops against the closed end, and its near edge
  is level with the edge of the sleeve mouth.

## Steps

Run Steps 1–6 in order on the one drawer box, then end the episode with Step 7. Only Step 4 depends on
where the divider starts: in Config L and M the **left gripper** fetches it and **hands it over** to the
right gripper in front of the drawer; in Config R the **right gripper** takes it from the right. Every other
line is the same in all three configs.

### Step 1: Fold the far wall and the near wall up

**Goal:** both long walls stand upright with the bottom panel still flat on the assembly spot.

- With the **left gripper**, press the middle of the bottom panel down flat against the table and keep
  it there through Step 2.
- With the **right gripper**, take the top edge of the **far wall** at its middle and fold it up on its
  score line until it stands upright.
- With the **right gripper**, fold the **near wall** up the same way.
- Fold on the score line only. Stop at upright, and do not fold a wall outward or past upright.

**Expected state:** the far wall and the near wall stand upright, and all four tab slots are open and
clear.

**Check:** both long walls stand up on their own and the bottom panel is still flat. If a wall falls
back down, press along its score line with the right gripper and fold it up again.

### Step 2: Fold the right wall up and lock both right corners

**Goal:** the right wall stands upright with both of its corner tabs seated.

- With the **left gripper**, keep pressing the bottom panel flat.
- With the **right gripper**, take the top edge of the **right wall** at its middle and fold it up on
  its score line.
- Keep folding it in until both corner tabs meet their tab slots.
- With the **right gripper**, press the **far** tab all the way into its slot, then press the **near**
  tab in.

**Check:** both right tabs are seated, the right wall stands on its own, and both right corners are
locked with no gap. If a tab sits outside its slot, fold the wall out a little with the right gripper,
line the tab up with the slot, and fold it in again. Do not force a tab past a slot that is not lined
up.

### Step 3: Fold the left wall up and lock both left corners

**Goal:** the left wall stands upright with both of its corner tabs seated, and the drawer is square.

- With the **left gripper**, take the top edge of the **left wall** at its middle and fold it up on its
  score line until both corner tabs meet their tab slots.
- With the **left gripper**, keep holding the left wall in.
- With the **right gripper**, press the **far** tab all the way into its slot, then press the **near**
  tab in.
- Release the left wall with the **left gripper** only after both tabs are seated.

**Expected state:** a square drawer sits on the assembly spot, empty, with all four corners locked.

**Check:** all four tabs are seated, no wall leans in or out, no corner shows a gap, and the bottom
panel is flat. If a corner is open or a wall leans, hold that wall in with the left gripper, seat the
tab again with the right gripper, and check again. If the drawer slides on the table, set it back
square on the assembly spot with the left gripper before going on.

### Step 4: Lower the divider in

**Goal:** the divider is seated on the bottom of the drawer, making six empty pockets.

Look where the divider is before reaching for it.

- **IF the divider is at the back-left (Config L):** with the **left gripper**, take the divider by the
  top edge of its long wall, near its **left end**, lift it off the divider spot, and carry it level, low
  over the table, forward and right to just in front of the drawer's **near wall**, long wall running left
  to right. Hold it still there. The **right gripper** closes on the top edge of the long wall near its
  **right end**; the **left gripper** opens and lifts clear.
- **IF the divider is at the front-center (Config M):** with the **left gripper**, take the divider by the
  top edge of its long wall, near its **left end**, lift it off the divider spot, and carry it level, low
  over the table, right along the front to just in front of the drawer's **near wall**, long wall running
  left to right. Hold it still there. The **right gripper** closes on the top edge of the long wall near
  its **right end**; the **left gripper** opens and lifts clear.
- **IF the divider is at the right (Config R):** with the **right gripper**, take the divider by the top
  edge of its long wall, at the middle, and lift it off the divider spot.

Then, in all three:

- With the **left gripper**, hold the outside of the drawer's **left wall** to keep the drawer still.
- With the **right gripper**, carry the divider level over the drawer, with its long wall running left to
  right.
- Lower it straight down into the drawer until it rests on the bottom panel.
- With the **right gripper**, press the divider down until it lies flat on the bottom all the way
  around.
- Keep the divider level. Do not turn it in the air and do not squeeze its walls together.

**Expected state:** six empty pockets, three in the far row and three in the near row.

**Check:** the divider is seated, none of its walls is folded over or pinched, and every pocket is
open. If it sits high or crooked, lift it out with the right gripper and lower it in again.

### Step 5: Load the six items

**Goal:** each of the six pockets holds its own item, in order, with nothing above the rim.

- With the **left gripper**, keep holding the outside of the drawer's left wall through the whole load.
- Carry one item at a time, straight from its cell to its pocket. Do not set an item on the table or on
  the rim, and do not carry two at once.

#### 5.1 Load the far row

- With the **right gripper**, take **item 1** from cell 1, lower it into **pocket 1**, and release it
  only once it rests on the drawer floor with its number label facing up.
- With the **right gripper**, load **item 2** into **pocket 2** the same way.
- With the **right gripper**, load **item 3** into **pocket 3** the same way.

#### 5.2 Load the near row

- With the **right gripper**, load **item 4** into **pocket 4**, **item 5** into **pocket 5**, then
  **item 6** into **pocket 6**, in that order and the same way.

**Check:** all six pockets hold one item each, the numbers match, every label faces up, nothing stands
above the rim, and the tray is empty. If an item stands above the rim, press it down with the right
gripper; if it still stands high, lift it out and set it back in flat. Do not force an item into a
pocket.

### Step 6: Slide the drawer into the sleeve

**Goal:** the loaded drawer is fully in the sleeve.

- With the **left gripper**, press the sleeve down flat against the table, holding it on its left side
  near the mouth.
- With the **right gripper**, close the gripper and set it low against the middle of the outside of the
  drawer's **near wall**.
- Push the drawer straight away from the front edge into the sleeve mouth, keeping it level and square
  to the mouth.
- Keep pushing until the drawer stops and its near edge is level with the edge of the sleeve mouth.
- Push on the near wall only. Do not push at a corner, and do not lift or carry the drawer.
- If the drawer catches at the mouth: stop pushing, take the top edge of the near wall with the
  **right gripper**, draw the drawer back a little, line it up square to the mouth, and push again.

**Check:** the drawer is fully in, the sleeve is still on its spot, no wall of the drawer is buckled,
and no item or divider wall was pushed up out of place. If the drawer sits short of the mouth edge,
push once more on the near wall with the right gripper.

### Step 7: End the episode

**Goal:** recording ends with the loaded drawer fully in the sleeve.

1. Confirm the drawer is fully in the sleeve, all four corners are still locked, all six pockets hold
   their item, the tray is empty, and the divider spot and assembly spot are clear.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

1. With recording off, pull the drawer out of the sleeve by hand and set it on the assembly spot.
2. Take the six items out and put each one back in its own numbered cell in the tray.
3. Lift the divider out and lay it back on the divider spot for the next episode's config — back-left
   (Config L), front-center (Config M), or right of the assembly spot (Config R) — pockets facing up, long
   wall running left to right.
4. Unseat the four corner tabs, fold all four walls back down, and lay the blank flat on the assembly
   spot, square to the front edge, inside face up.
5. Put the sleeve back behind the assembly spot, lying flat, mouth facing the front edge and square to
   the blank.
6. Inspect the blank, its tabs and slots, the divider, the sleeve, the tray, and the six items. Replace
   the blank if a score line is soft or split, a tab is torn or curled, a slot is chewed out, or a
   corner no longer holds. Replace the sleeve if its mouth is crushed and replace the divider if a wall
   is bent over.
7. Run both Setup checklists before the next episode.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

- the **start timestamp** in the video;
- the **violation name** from the list below; and
- the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation
label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain multiple violations; tag each
separately. Retain the episode in training data with its violation tags. Do not delete a recorded
episode solely because it contains a violation.

### Violations

**Note on the start position:** the violations below were written for Config R (the divider starts on the
divider spot at the right of the assembly spot). The pickup and arm-role cues will be rewritten later to
cover all three start positions; they are left as they are for now. Until then, anything that does not
match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the divider is not on
  the divider spot for the config; a gripper reaches across the table for the divider; in Config L or M the
  left gripper carries the divider over the drawer itself, or the right gripper reaches to the left or the
  front-center for it, instead of a hand-over in front of the near wall; or the wrong IF line is followed.
- **SOP rule broken:** the start position, the same-side rule, and the hand-over rule (the left gripper
  takes the divider in Config L and M and hands it to the right gripper in front of the drawer's near wall;
  in Config R the right gripper takes it from the right; no arm reaches across the table; the IF line
  followed is the one for the config on the table).
- **Coaching note:** look where the divider is before the first reach for it, then follow that config's IF
  line through Step 4.

**Violation: Walls folded out of order or the wrong way**
- **Visible cue:** an end wall is folded up before both long walls stand, or the right gripper folds a
  wall outward, past upright, or off its score line.
- **SOP rule broken:** Steps 1–3 (fold the far wall and near wall up first, then the right wall, then
  the left wall, each on its score line and only to upright).
- **Coaching note:** long walls first, then right, then left, and stop each fold at upright.

**Violation: Blank not held flat**
- **Visible cue:** the left gripper is off the bottom panel while the right gripper folds, and the
  blank lifts, slides, or is chased across the assembly spot.
- **SOP rule broken:** Steps 1 and 2 (the left gripper presses the bottom panel flat while the right
  gripper folds).
- **Coaching note:** set the left gripper on the bottom panel first, then fold with the right gripper.

**Violation: Tab not seated**
- **Visible cue:** a corner tab is left outside its slot, stands proud of the wall, springs back out
  when the gripper lets go, or the step moves on with fewer than four tabs in.
- **SOP rule broken:** Steps 2 and 3 (press each tab all the way into its slot, far tab first, then
  near, on both ends).
- **Coaching note:** four tabs, all the way in, and check each one holds before moving on.

**Violation: Blank forced or damaged**
- **Visible cue:** a tab is jammed against a slot that is not lined up, a wall is bent away from its
  score line, or the cardboard tears, buckles, or creases across a panel.
- **SOP rule broken:** Steps 1–3 (fold on the score line, and line a tab up with its slot instead of
  forcing it).
- **Coaching note:** line it up and press lightly; back the wall out and try again rather than forcing.

**Violation: Drawer left out of square**
- **Visible cue:** a wall leans in or out, a corner shows a gap, or the bottom panel lifts, and the
  divider or an item goes in anyway.
- **SOP rule broken:** Step 3 (the drawer is square with all four corners locked before anything goes
  in).
- **Coaching note:** hold the wall in with the left gripper, reseat the tab, and only then load.

**Violation: Divider skipped or out of order**
- **Visible cue:** an item goes into the drawer before the divider is in, or the divider is lowered in
  after items are already loaded.
- **SOP rule broken:** Steps 4 and 5 (the divider is seated on the bottom before the first item is
  loaded).
- **Coaching note:** divider first, always, then the six items.

**Violation: Divider not seated**
- **Visible cue:** the divider rides above the bottom panel, sits crooked, has a wall folded over or
  pinched, is turned with its long wall front to back, or is turned in the air on the way in.
- **SOP rule broken:** Step 4 (lower the divider in level and press it flat on the bottom, long wall
  running left to right).
- **Coaching note:** keep it level, lower it straight down, and press it flat before letting go.

**Violation: Wrong pocket or wrong load order**
- **Visible cue:** an item's number does not match its pocket, two items share a pocket, a pocket is
  left empty, or the near row is loaded before the far row.
- **SOP rule broken:** Step 5 (load item 1 to pocket 1 through item 6 to pocket 6, far row left to
  right, then near row left to right).
- **Coaching note:** match the number to the pocket and work far row first, left to right.

**Violation: Item mishandled**
- **Visible cue:** an item is set on the table or on the rim, two are carried at once, one is released
  above its pocket or dropped, one is forced into a pocket, or one is left standing above the rim or
  label down.
- **SOP rule broken:** Step 5 (carry one item at a time straight from its cell into its pocket, and
  release it only once it rests on the drawer floor, label up and below the rim).
- **Coaching note:** one item at a time, straight in, and let go only when it is resting flat.

**Violation: Drawer not steadied**
- **Visible cue:** the left gripper is away from the drawer's left wall while the divider or an item
  goes in, and the drawer slides, spins, or tips.
- **SOP rule broken:** Steps 4 and 5 (the left gripper holds the outside of the left wall while the
  right gripper loads).
- **Coaching note:** left gripper on the left wall first, then load with the right gripper.

**Violation: Drawer lifted instead of slid**
- **Visible cue:** the right gripper lifts or carries the loaded drawer to the sleeve, tips it, or
  pushes it at a corner instead of on the near wall.
- **SOP rule broken:** Step 6 (push the drawer along the table on its near wall, straight away from the
  front edge).
- **Coaching note:** keep it on the table and push flat on the middle of the near wall.

**Violation: Sleeve not held**
- **Visible cue:** the left gripper is off the sleeve during the push, and the sleeve slides, lifts,
  turns, or is pushed off its spot.
- **SOP rule broken:** Step 6 (the left gripper presses the sleeve flat on its left side near the mouth
  while the right gripper pushes).
- **Coaching note:** pin the sleeve down first, then push.

**Violation: Drawer not fully in the sleeve**
- **Visible cue:** the drawer stops short of the mouth edge, sits in at an angle, has a wall buckled at
  the mouth, or is left with an item or divider wall pushed up out of place.
- **SOP rule broken:** Step 6 (push until the drawer stops and its near edge is level with the sleeve
  mouth, square and level).
- **Coaching note:** square it to the mouth, push until it stops, then look at the near edge.

**Violation: Wrong arm used**
- **Visible cue:** an action assigned to one gripper is done by the other, including the left gripper
  seating a tab, lifting the divider, or loading an item, or the right gripper folding the left wall or
  holding the sleeve.
- **SOP rule broken:** Steps 1–6 (the right gripper folds the far, near, and right walls, seats all
  four tabs, loads the divider and items, and pushes; the left gripper presses the blank flat, folds
  and holds the left wall, steadies the drawer, and holds the sleeve).
- **Coaching note:** right gripper does the fine work, left gripper holds and folds the left wall.

**Violation: Drawer or supply knocked over**
- **Visible cue:** the drawer, the sleeve, the divider, or the tray is dropped, tipped, or pushed off
  its spot, or items spill on the table.
- **SOP rule broken:** Steps 1–6 (keep the drawer, sleeve, divider, and tray on their spots through the
  build).
- **Coaching note:** work slower and lower over the table, and keep carries short.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before the drawer is fully in the sleeve, an arm is not home, a
  gripper is closed, or an arm does something else after homing.
- **SOP rule broken:** Step 7 (confirm the end state, return both arms home with grippers open as their
  final action, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than
tagging them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- The blank is die-cut wrong, so a tab cannot reach its slot.
- The sleeve is undersized or crushed, so a correctly built drawer will not slide in.
- The divider is the wrong size for the drawer, or an item is too big for its pocket.

## Annotation subtasks (from SOP)

1. Fold the far wall and the near wall up on their score lines
2. Fold the right wall up and seat its two corner tabs
3. Fold the left wall up and seat its two corner tabs
4. Hand the divider from the left gripper to the right gripper in front of the drawer's near wall (Config L
   and M)
5. Lower the divider into the drawer to make six pockets
6. Load items 1, 2, and 3 into the far pockets, left to right
7. Load items 4, 5, and 6 into the near pockets, left to right
8. Slide the loaded drawer into the sleeve until it is fully in
9. Confirm the end state, return both arms home, and end the episode
