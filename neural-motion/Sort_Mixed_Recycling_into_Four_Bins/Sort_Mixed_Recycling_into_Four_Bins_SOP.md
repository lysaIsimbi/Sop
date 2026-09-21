# Sort Mixed Recycling into Four Bins SOP (1x Episode)

One episode clears one **pile** of mixed recycling into four category bins. The pile lies loose on the table at
the front left when recording starts. The episode runs in two halves. First the plastic, the glass, and the
metal are picked out of the pile, called, and set down on the **staging spot** in front of the bin each one's
category names, while the paper stays lying in the pile. Then each category is loaded into its bin, one
category at a time, and the paper goes in last straight from the pile. The pile is gone, the three staging
spots are bare, and the four bins hold the sorted items when the episode ends.

The sort runs one category at a time and the order never changes: **plastics first, glass second, metal third,
paper last**. Nothing but the category being worked leaves the pile during its pass. An item called anything
else is laid straight back in the pile and picked up again on its own pass, and paper is laid back every time
until the PAPER bin is loaded.

The bins stand in one row along the back edge in a fixed order that never changes, running left to right:
**PAPER**, **METAL**, **GLASS**, **PLASTIC**. A staging spot is marked on the table directly in front of the
**METAL**, **GLASS**, and **PLASTIC** bins.

The bins are loaded in the same order the sort ran: the **PLASTIC** bin first, after the cups are nested into
one stack; then **GLASS**; then **METAL**; then **PAPER**, where the carton comes out of the pile to be
flattened and goes in first, and the rest of the paper is laid on top of it. Nothing is ever taken back out of
a bin.

The left gripper lifts every item out of the pile and turns it for the call. Glass and metal it carries to
their spots itself. A plastic item it does not: it holds the item out at the **handover point** in the middle
of the table and **passes it across** to the right gripper, which sets it on the PLASTIC spot. The right
gripper never reaches into the pile.

The bin row is split down the middle. The **right gripper** nests the cups and loads the two bins on the
right, **GLASS** and **PLASTIC**. The **left gripper** loads the two bins on the left, **PAPER** and **METAL**.
Neither gripper loads the other's bins.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the pile at the front left, the three staging spots in one row
   across the middle, and the four bins in a row along the back edge.
3. The pile is in frame from above, with every item in it visible.
4. The mouth of all four bins is in frame from above, so an item can be seen going in below the rim.
5. The **bin label** on each of the four bins is readable in frame.
6. All three staging spots are in frame from above, so what is standing on each one can be counted.
7. Both arms are at home with grippers open.
8. The table is bare apart from the pile, the four bins, and robot hardware.
9. The staging row is compact enough that **both** arms reach all three staging spots without stretching or
   leaning out, and both arms reach the **handover point** in the middle of the table, where they meet with an
   item held between them and where the carton is flattened.
10. The left arm reaches every part of the pile and the mouths of the **PAPER** and **METAL** bins. The right
    arm reaches the mouths of the **GLASS** and **PLASTIC** bins.
11. The travel from each staging spot to the bin behind it is bare and level.

### Materials checklist

1. The **pile** lies loose on the table at the front left, inside its printed outline, in one layer, with no
   item stacked on or overlapping another.
2. The pile is mixed recycling and holds items of all four categories: **plastic**, **paper**, **metal**, and
   **glass**. Every item in it belongs to one of the four.
3. Every item is clean, dry, and empty, is small enough for a gripper to close across it somewhere, and lifts
   with one gripper.
4. Among the plastics there are **cups** that **nest**. Each drops inside the next with no lip that catches on
   the way in, and they lift as one stack. The cups are the only items in the pile that nest.
5. Among the paper there is one **carton**, a paper-bodied drink box, empty and open, with its faces still
   square, that presses flat by hand without tearing.
6. **Three staging spots** are printed on the table in one row across the middle, one directly in front of the
   **METAL** bin, one in front of the **GLASS** bin, and one in front of the **PLASTIC** bin, each carrying
   that bin's category name. Each spot is wide enough to hold its whole category side by side. The paper stays
   in the pile until the PAPER bin is loaded.
7. **Four bins** stand in one row along the back edge of the table, each in its printed outline, each with its
   printed **bin label** facing the front edge. Running left to right: **PAPER**, **METAL**, **GLASS**,
   **PLASTIC**.
8. Every bin is empty, upright, wide at the mouth, and deep enough that an item released just inside the rim
   stays in, and deep enough to take its whole category with room to spare.
9. Before collection, confirm by hand that:
   - each item lifts out of the pile without bringing a second item with it;
   - the cups nest into one stack and that stack lifts as one;
   - the carton presses flat and stays flat on its own;
   - an item released just inside a bin mouth drops in and does not catch on the rim.

### Workspace layout

* **Pile:** the front left of the table, in front of the left arm, inside its printed outline. Every item
  starts here, the paper stays here until the PAPER bin is loaded, and the outline is bare from the end of
  Step 7 onward.
* **Staging row:** three printed spots in one row across the middle of the table, reached by both arms. Left to
  right: **METAL**, **GLASS**, **PLASTIC**. Each spot holds one category and is bare once that category's bin
  has been loaded.
* **Bin row:** four bins in one straight line along the back edge, the METAL, GLASS, and PLASTIC bins each
  standing directly behind their own staging spot. Left to right: **PAPER**, **METAL**, **GLASS**, **PLASTIC**.
  The row is never moved and never reordered.
* **Handover point:** the middle of the table, in front of the staging row, where the left gripper passes a
  plastic item across to the right gripper and where the carton is flattened.
* The left arm's zones are the pile, the staging row, and the **PAPER** and **METAL** bins. The right arm's
  zones are the staging row and the **GLASS** and **PLASTIC** bins. Neither arm goes to the other's bins.

### Arm assignments

* **Left gripper:** lifts every item out of the pile and turns it once for the call; carries glass and metal
  items to their staging spots; passes every plastic item across to the right gripper at the handover point;
  brings the carton and the rest of the paper out of the pile when the PAPER bin is loaded; holds items down
  while the right gripper presses the carton flat; and loads the **PAPER** and **METAL** bins.
* **Right gripper:** takes each plastic item at the handover point and sets it on the PLASTIC spot; nests the
  cups; flattens the carton; and loads the **PLASTIC** and **GLASS** bins.

## Vocabulary

* **Item:** one piece of recycling to be called and binned.
* **Pile:** the loose heap of mixed recycling at the front left of the table, holding every item at the start.
* **Body:** the main wall of an item, the part its material is read from. An item with no clear body is read
  from whichever face shows its material and is gripped wherever the hold is firm.
* **Cup:** one of the plastic cups in the pile. They are nested into one stack before they are binned.
* **Nest:** the cups lowered one inside another by the right gripper so their rims sit level and the stack
  lifts as one piece.
* **Carton:** the paper-bodied drink box, open from the start. A carton is paper once it has been flattened.
* **Plastic:** bottles, cups, tubs, trays, and rigid plastic packaging. Reads as light for its size, bends, and
  dents rather than creases.
* **Paper:** paper, card, cardboard, and cartons. Reads as fibrous, creases when bent, and holds the crease.
* **Metal:** cans, tins, foil trays, and metal lids. Reads as heavy for its size, rigid, and dents without
  creasing.
* **Glass:** bottles and jars. Reads as heavy, hard, and does not bend or dent at all.
* **Call the category:** naming one of the four categories for the item while the left gripper holds it just
  clear of the pile, before it is carried anywhere.
* **Staging spot:** one of the three printed spots across the middle of the table, each in front of the bin
  whose category it carries. Every plastic, glass, and metal item waits on its spot until its bin is loaded.
* **Category pass:** one trip through the pile for a single category. The category passes run plastic, then
  glass, then metal, and never in another order. Paper has no pass: it stays in the pile until the PAPER bin is
  loaded.
* **Handover point:** the place in the middle of the table, in front of the staging row, where the left gripper
  holds a plastic item out and the right gripper takes it.
* **Pass across:** the left gripper holds the item still at the handover point, the right gripper closes on it,
  and only then does the left gripper open and withdraw. Plastic items are the only ones passed across.
* **Flattened:** the carton pressed down so its faces lie together and it stays flat on its own with both
  grippers clear of it.
* **Bin:** one of the four open containers in the bin row.
* **Bin mouth:** the open top of a bin, inside its rim. An item is released here and nowhere else.
* **Bin label:** the printed category name on the front face of a bin.
* **Lowered in:** the gripper carries the item down through the bin mouth, below the rim, and opens there.
  Nothing is ever released above the rim.
* **Touched down:** for glass, the item is lowered until it rests on the bin floor or on what is already in the
  bin, and only then does the gripper open.
* **Caught on the rim:** the item is left lying across the bin mouth or hooked on the rim instead of inside the
  bin.
* **Spot clear:** a staging spot holds no item and no debris.

## Steps

Steps 1 to 3 stage the plastic, the glass, and the metal on their spots, one category pass at a time, while the
paper stays in the pile. Steps 4 to 7 load the four bins in the same order, the paper coming straight out of
the pile in Step 7. Then end the episode with Step 8.

### Step 1: Stage the plastics

**Goal:** every plastic item stands on the **PLASTIC** spot and no plastic is left in the pile.

* With the **left gripper**, close across the body of one item in the pile, or across any other part of it that
  gives a firm hold, and lift it straight up, clear of the items around it.
* Take one item only. If a second item comes up with it, lower both back into the pile with the **left
  gripper** and take one again.
* With the **left gripper**, turn the item once so its sides, its base, and its top all come into view of the
  camera. Read the material and call exactly one category: **plastic**, **paper**, **metal**, or **glass**. A
  **cup** is plastic. The **carton** is paper.
* If the call is not plastic, lay the item back in the pile with the **left gripper** and lift the next one.
  Only plastic leaves the pile in this step.
* If the call is plastic, **pass it across**: with the **left gripper**, bring it to the **handover point** in
  the middle of the table and hold it still, upright, and clear of the table. With the **right gripper**, close
  on its body, or on any other part that gives a firm hold. Only once the right gripper has closed does the
  **left gripper** open and withdraw. The left
  gripper never carries a plastic item to the PLASTIC spot itself.
* With the **right gripper**, carry the item to the **PLASTIC** spot at the right end of the staging row and
  set it down. Never drag or slide an item across the table.
* Repeat until no plastic is left in the pile.

**Check:** the **PLASTIC** spot holds every item called plastic in this step, and no plastic is left in the
pile. If a plastic item is still in the pile, take it now before Step 2 starts.

**Expected state:** every plastic item standing side by side on the **PLASTIC** spot, the rest of the items
still lying in the pile, and both grippers empty.

### Step 2: Stage the glass

**Goal:** every glass item stands on the **GLASS** spot and no glass is left in the pile.

* With the **left gripper**, lift one item out of the pile, turn it once for the camera, and call its category,
  exactly as in Step 1.
* If the call is not glass, lay the item back in the pile with the **left gripper** and lift the next one.
* If the call is glass, the **left gripper** keeps it the whole way. Glass is never passed across.
* With the **left gripper**, carry it to the **GLASS** spot and set it down. Never drag or slide an item across
  the table.
* Repeat until no glass is left in the pile.

**Check:** the **GLASS** spot holds every item called glass in this step, standing upright and not touching
each other, and no glass is left in the pile.

**Expected state:** every glass item on the **GLASS** spot, the rest of the items still lying in the pile, and
both grippers empty.

### Step 3: Stage the metal

**Goal:** every metal item stands on the **METAL** spot, and the pile holds nothing but paper.

* With the **left gripper**, lift one item out of the pile, turn it once for the camera, and call its category,
  exactly as in Step 1.
* If the call is not metal, lay the item back in the pile with the **left gripper** and lift the next one.
* If the call is metal, the **left gripper** keeps it the whole way. Metal is never passed across.
* With the **left gripper**, carry it to the **METAL** spot and set it down. Never drag or slide an item across
  the table.
* Repeat until no metal is left in the pile.

**Check:** the **METAL** spot holds every item called metal in this step, and the pile holds the carton and the
rest of the paper and nothing else. If something that is not paper is still in the pile, take it to its spot
before Step 4 starts.

**Expected state:** every plastic on the **PLASTIC** spot, every glass item on the **GLASS** spot,
every metal item on the **METAL** spot, the paper still lying in the pile, and both grippers empty.

### Step 4: Nest the cups and load the PLASTIC bin

**Goal:** the **PLASTIC** bin holds the nested cups and every other plastic that was on the spot, and the
**PLASTIC** spot is bare.

* Leave one cup standing upright on the **PLASTIC** spot as it was staged. It is not held.
* With the **right gripper**, close on a second cup, bring it over the standing cup, and lower it straight in
  until its rim settles. Do not push it in at an angle. If the standing cup shifts or tips, set the cup in the
  gripper down, stand the tipped one upright again with the **right gripper**, and start the nest again.
* Open the **right gripper**, lift clear, and lower the next cup into the stack the same way.
* Repeat until every cup on the spot stands in one **nest** with the rims level, however many cups the spot
  holds.
* With the **right gripper**, close across the outside of the nest below the rims and lift it. If a cup slips
  out, set the nest down, push the loose cup back in with the **right gripper**, and lift again.
* With the **right gripper**, carry the nest to the **PLASTIC** bin at the right end of the back row, reading
  the **bin label** on the way. Bring it over the **bin mouth** so the whole nest is inside the rim, lower it
  below the rim, and open the gripper. Never throw, toss, or drop an item toward a bin from above the rim.
* With the **right gripper**, take every other plastic on the spot to the **PLASTIC** bin the same way, one
  item at a time. Only cups are nested; a plastic that is not a cup goes in on its own and is never pushed into
  the nest.
* Repeat until no plastic item is left standing on the spot, however many the spot holds.
* Once the **right gripper** has opened over a bin, that item stays in that bin. Never reach into a bin to take
  an item back out.

**Check:** every cup went in as one nest, every other plastic went in on its own, nothing is caught on the rim,
and the **PLASTIC** spot holds no item and no debris. If something is caught on the rim, push it down
through the mouth with the **right gripper**.

**Expected state:** the **PLASTIC** bin holding the nest and every other plastic from the spot, the
**PLASTIC** spot bare, and both grippers empty.

### Step 5: Load the GLASS bin

**Goal:** the **GLASS** bin holds everything that was staged on the **GLASS** spot and the spot is bare.

* With the **right gripper**, close on the middle of one glass item, or wherever the hold is firm, and lift it
  clear of the spot.
* With the **right gripper**, carry it straight back to the **GLASS** bin, reading the **bin label** on the
  way, and bring it over the **bin mouth** so the whole item is inside the rim.
* Lower it until it **touches down** on the bin floor or on what is already in the bin, and only then open the
  **right gripper**. Glass is placed, never dropped.
* Repeat until the **GLASS** spot is bare. Everything staged in front of the bin goes in, however many items
  the spot holds.

**Check:** every item that was staged on the **GLASS** spot is standing inside the **GLASS** bin, none is
caught on the rim, and the spot is bare.

**Expected state:** every glass item from the spot in the **GLASS** bin, the **GLASS** spot bare, and the right
gripper empty.

### Step 6: Load the METAL bin

**Goal:** the **METAL** bin holds everything that was staged on the **METAL** spot and the spot is bare.

* With the **left gripper**, close on the middle of one metal item, or wherever the hold is firm, and lift it
  clear of the spot. The
  METAL bin is the left gripper's; the right gripper does not load it.
* With the **left gripper**, carry it straight back to the **METAL** bin, reading the **bin label** on the way,
  bring it inside the **bin mouth**, lower it below the rim, and open the gripper.
* Repeat until the **METAL** spot is bare. Everything staged in front of the bin goes in, however many items
  the spot holds.

**Check:** every item that was staged on the **METAL** spot is inside the **METAL** bin, none is caught on the
rim, and the spot is bare.

**Expected state:** every metal item from the spot in the **METAL** bin, the **METAL** spot bare, and the left
gripper empty.

### Step 7: Flatten the carton and load the PAPER bin

**Goal:** the flattened carton lies on the floor of the **PAPER** bin with the rest of the paper on top of it,
and the pile is gone.

* With the **left gripper**, lift the carton out of the pile and set it down at the **handover point** in the
  middle of the table, where both arms reach it.
* With the **left gripper**, hold the carton down at its base.
* With the **right gripper**, push the top of the carton down and inward until the top folds in.
* With the **right gripper**, press the two wide faces together until the carton lies flat, then run the
  gripper once along each crease to set it.
* Open both grippers and lift clear. The carton stays flat on its own.
* With the **left gripper**, lift the flat carton and carry it to the **PAPER** bin at the left end of the back
  row. Bring it inside the **bin mouth**, lower it below the rim, and open the gripper so it lies flat on the
  bin floor. The PAPER bin is the left gripper's; the right gripper does not load it.
* With the **left gripper**, lift each remaining piece of paper straight out of the pile, one at a time, and
  lay it on top of the carton the same way. Repeat until nothing is left inside the pile outline, however many
  pieces it holds. Nothing goes into the **PAPER** bin before the flattened carton.

**Check:** the carton went in flat and went in first, every other piece of paper is lying on top of it, nothing
is caught on the rim, and the pile outline is bare. If the carton springs back open, hold it with the **left
gripper** and press the same creases flat again with the **right gripper** before it is carried.

**Expected state:** the **PAPER** bin holding the flat carton with the rest of the paper on top of it, the pile
outline bare, and both grippers empty.

### Step 8: End the episode

**Goal:** recording ends with the pile gone and every item binned.

1. Confirm the end state:
   - the pile outline is bare and all three staging spots are bare;
   - every item sits in the bin its called category names, with none caught on a rim.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

### After each episode

1. Empty all four bins. Stand each bin back in its printed outline with its label facing the front edge, in the
   order PAPER, METAL, GLASS, PLASTIC from left to right.
2. Rebuild the pile from mixed recycling covering all four categories, with cups among the plastics and one
   carton among the paper.
3. Pull the cups apart and check each one still nests cleanly. Replace a cup that sticks or that no longer sits
   level in the stack.
4. Replace the carton with a fresh one, open and square. A carton that has been flattened once does not go back
   in the pile.
5. Lay the items loose inside the pile outline in one layer, none stacked and none overlapping.
6. Wipe the three staging spots clean and dry.
7. Run both Setup checklists before the next episode.

### At the end of the session

1. Inspect the items. Replace anything cracked, crushed, torn, or too dented for a gripper to close on.
2. Wash and dry the four bins and wipe the staging row and the pile outline down.
3. Leave the four bins empty and in order along the back edge, the staging spots bare, and a fresh pile built
   inside its outline at the front left.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

* the **start timestamp** in the video;
* the **violation name** from the list below; and
* the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain multiple violations; tag each
separately. Retain the episode in training data with its violation tags. Do not delete a recorded episode
solely because it contains a violation.

### Violations

**Violation: More than one item taken at once**
* **Visible cue:** the left gripper lifts or carries two items out of the pile in one pick, or a second item
  comes up with the first and is worked on instead of being laid back in the pile.
* **SOP rule broken:** Steps 1–3 (take one item only; if a second comes up, lower both back into the pile and
  take one again).
* **Coaching note:** one item per pick. If two come up, put both back and start again.

**Violation: Item dragged instead of lifted**
* **Visible cue:** a gripper slides or pushes an item across the table or a staging spot instead of lifting it
  clear and carrying it.
* **SOP rule broken:** Steps 1–3 (lift the item straight up clear of the items around it and carry it to its
  staging spot).
* **Coaching note:** lift it clear, carry it, set it down. Never push it along the table.

**Violation: Category not called before the carry**
* **Visible cue:** the left gripper lifts an item out of the pile and carries it to a staging spot without
  turning it first so its sides, base, and top come into view.
* **SOP rule broken:** Steps 1–3 (turn the item once for the camera and call one category before carrying it
  anywhere).
* **Coaching note:** turn it, look at it, name the category. Then move.

**Violation: Item staged away from its category's spot**
* **Visible cue:** an item is set down on a staging spot whose label does not match the category called for it,
  a paper item is carried to the staging row instead of being laid back in the pile, or an item is set down on
  the table, on another item, or in a bin instead of on its spot.
* **SOP rule broken:** Steps 1–3 (carry a plastic, glass, or metal item to the staging spot in front of the bin
  its called category names and set it down there; paper is laid back in the pile).
* **Coaching note:** the call picks the spot. Paper waits in the pile, everything else waits in front of its
  own bin.

**Violation: Work run out of order**
* **Visible cue:** an item is staged for a category whose pass has not started, such as glass or metal leaving
  the pile while plastics are still in it. Or a bin takes an item before the bin ahead of it in the order is
  finished, such as the GLASS bin loading while the PLASTIC spot still holds items.
* **SOP rule broken:** Steps 1–7 (staging and loading both run plastics first, glass second, metal third, paper
  last, and only the category being worked leaves the pile).
* **Coaching note:** finish the whole category before you start the next one. Anything else goes back in the
  pile.

**Violation: Handover skipped or used on the wrong category**
* **Visible cue:** the left gripper carries a plastic item to the PLASTIC spot itself instead of passing it
  across, or the left gripper opens at the handover point before the right gripper has closed and the item
  drops or is regripped off the table, or a glass or metal item is handed to the right gripper instead of being
  carried to its spot by the left gripper.
* **SOP rule broken:** Steps 1–3 (plastic items, and only plastic items, are passed across at the handover
  point, and the left gripper opens only once the right gripper has closed).
* **Coaching note:** plastics change hands in the middle. Everything else stays in the left gripper the whole
  way.

**Violation: Carton not held while the right gripper presses it**
* **Visible cue:** the left gripper is off the carton while the right gripper folds or presses it, and the
  carton slides, spins, tips over, or is chased across the table.
* **SOP rule broken:** Step 7 (the left gripper holds the carton down at its base while the right gripper
  presses it flat).
* **Coaching note:** left gripper down first, then press.

**Violation: Cups not nested before binning**
* **Visible cue:** a cup goes into the PLASTIC bin on its own, or the others are nested and one is binned
  loose, or a cup is pushed in at an angle and rides up out of the stack while the nest is carried, or a
  plastic that is not a cup is pushed into the nest.
* **SOP rule broken:** Step 4 (the right gripper lowers each cup straight into the one below until they stand
  as one nest with rims level, and carries the nest in as one piece).
* **Coaching note:** every cup, one stack, one trip. If one slips out, set it down and seat it again.

**Violation: More than one item loaded in one trip**
* **Visible cue:** a gripper closes on two items at once on a staging spot and carries both to the bin in one
  trip, or picks up the next item before the one in the gripper has been released inside the bin.
* **SOP rule broken:** Steps 4–7 (take the items to the bin one at a time; only the nested cups travel as one
  piece).
* **Coaching note:** one item per trip. The nest is the only thing that goes in as a group.

**Violation: Item dropped in from above the rim**
* **Visible cue:** a gripper opens above the bin rim and the item falls in, is tossed toward the bin, or is
  released before it passes below the rim.
* **SOP rule broken:** Steps 4–7 (bring the item inside the mouth, lower it below the rim, and only then open
  the gripper).
* **Coaching note:** take it down inside the bin before you let go. No drops from above.

**Violation: Glass released before it touched down**
* **Visible cue:** the right gripper opens on a glass item while it is still hanging inside the bin, and the
  item falls onto the bin floor or onto the contents below it.
* **SOP rule broken:** Step 5 (lower a glass item until it touches down on the bin floor or on what is already
  in the bin, and only then open the gripper).
* **Coaching note:** glass is placed, never dropped. Feel it land, then open.

**Violation: Item left caught on the rim**
* **Visible cue:** an item ends up lying across a bin mouth or hooked on the rim, and the episode moves on to
  the next item or to the ending.
* **SOP rule broken:** Steps 4–7 (confirm the item landed inside the bin, and push it down through the mouth
  with the gripper that loaded it if it is caught).
* **Coaching note:** look into the bin after every release. If it is on the rim, push it in.

**Violation: Item taken back out of a bin**
* **Visible cue:** either gripper reaches into a bin mouth and lifts an item back out, whatever the reason.
* **SOP rule broken:** Steps 4–7 (once a gripper has opened over a bin, the item stays in that bin).
* **Coaching note:** decide before you release. A wrong bin is tagged, not undone.

**Violation: Carton not flattened**
* **Visible cue:** the carton goes to the PAPER bin still square, or is pressed only part way so it springs
  back open and goes in anyway.
* **SOP rule broken:** Step 7 (press the two wide faces together until the carton lies flat and stays flat with
  both grippers clear of it).
* **Coaching note:** fold the top in, press the faces together, run the creases, then let go and watch it stay
  flat.

**Violation: Paper laid in before the flattened carton**
* **Visible cue:** a piece of paper goes into the PAPER bin before the carton does, or the carton is lowered in
  on top of paper that is already lying in the bin.
* **SOP rule broken:** Step 7 (the flattened carton goes in first and lies on the bin floor; the rest of the
  paper is laid on top of it).
* **Coaching note:** carton flat on the floor of the bin, paper on top of it. Nothing goes in ahead of it.

**Violation: Item put in the wrong bin**
* **Visible cue:** a gripper releases an item into a bin whose label does not match the category called for it,
  and the episode moves on.
* **SOP rule broken:** Steps 4–7 (carry the item to the bin for its called category, reading the bin label on
  the way).
* **Coaching note:** read the label on the bin before you lower the item in. Category first, label second.

**Violation: Bin row moved or reordered**
* **Visible cue:** either gripper pushes, drags, tips, or turns a bin, a bin ends the episode out of its
  outline, out of the left-to-right order, or with its label turned away from the front edge.
* **SOP rule broken:** Steps 4–7 (the four bins stay in their outlines, in the order PAPER, METAL, GLASS,
  PLASTIC from left to right, labels facing the front edge).
* **Coaching note:** come down into the mouth from above. Do not lean the gripper on the bin wall.

**Violation: Wrong arm used**
* **Visible cue:** an action assigned to one gripper is done by the other: the right gripper reaching into the
  pile; the left gripper pressing the carton flat or touching a cup at any point in the nesting; the left gripper loading the GLASS or PLASTIC bin; or the right gripper loading the METAL or PAPER
  bin.
* **SOP rule broken:** Steps 1–7 (the left gripper clears the pile, stages glass and metal, holds items down
  for the carton, and loads the PAPER and METAL bins; the right gripper takes the plastics across, nests the
  cups, flattens, and loads the PLASTIC and GLASS bins).
* **Coaching note:** the bin row splits down the middle. The left arm takes the two left bins and the right arm
  the two right. It does not swap.

**Violation: Item dropped or the pile pushed out of its outline**
* **Visible cue:** either gripper drops an item on the table or the floor, or pushes, drags, or scatters the
  pile outside its printed outline.
* **SOP rule broken:** Steps 1–7 (the pile stays inside its outline, and every carry stays level and low over
  the table).
* **Coaching note:** work slower and lower over the table, and keep each carry short.

**Violation: Wrong episode ending**
* **Visible cue:** recording stops before the bare pile outline, the bare spots, and the four bins are
  confirmed, an arm is not home, a gripper is closed, or an arm does something else after homing.
* **SOP rule broken:** Step 8 (confirm the end state, return both arms home with grippers open as their final
  action, then stop recording).
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than tagging
them as SOP violations.

* Recording stops or pauses during the episode.
* A camera drops frames or loses its feed.
* An arm or gripper fails, drifts, or reports a motor error.
* An item arrives wet, soiled, or still holding food, so it cannot be sorted clean.
* An item arrives crushed or split so a gripper cannot close across it anywhere.
* A cup arrives dented or out of round, so the cups will not nest.
* The carton arrives already torn or already crushed, so it cannot be flattened square.
* A bin is cracked, will not stand upright, or has no readable label.

## Annotation subtasks (from SOP)

1. Lift one item out of the pile with the left gripper and turn it for the call
2. Lay a called item back in the pile because its category pass has not started
3. Lay a paper item back in the pile to wait for the PAPER bin
4. Pass a plastic item across to the right gripper at the handover point
5. Set a called item on the staging spot in front of its bin
6. Nest the cups into one stack with the right gripper
7. Lower the nested cups and the other plastics into the PLASTIC bin with the right gripper
8. Lower each glass item into the GLASS bin with the right gripper until it touches down
9. Lower each metal item into the METAL bin with the left gripper
10. Lift the carton out of the pile and fold and press it flat at the handover point
11. Lower the flat carton into the PAPER bin with the left gripper
12. Lift each remaining piece of paper out of the pile and lay it on top of the carton
13. Confirm the end state, return both arms home, and end the episode
