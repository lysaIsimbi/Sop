# Sort Dispositions to Four Bins SOP (1x Episode: 12 Items)

One episode empties one **returns tote** of twelve items into four disposition bins. The tote sits in the
**start zone** for the episode's config when recording starts, holding the twelve items loose in one layer.
Every item is picked out one at a time, set on the **read spot** in the middle, turned so its **condition
tag** and its base come into view, and given a **stream** — **restock**, **refurb**, **liquidate**, or
**scrap** — from the **rule card**. The item then goes in the bin for that stream. When the tote is bare, each
stream is tallied with a **count chip**, and the **SCRAP** bin is shut and sealed with one **seal sticker**.

The order never changes for each item: pick one, set it on the read spot, read the tag and the base, call the
stream from the rule card, bin it, clear the read spot. No item is carried toward the bin row before its stream
is called. Nothing is ever taken back out of a bin.

The four bins stand in one row along the right side in a fixed order that never changes: **RESTOCK**,
**REFURB**, **LIQUIDATE**, **SCRAP**, running from the front edge back. The **rule card** stands upright at the
back-center and is what decides every stream. The **tally card** and the **chip rack** sit at the front-left.
The **seal pad** sits at the front-right.

The tally comes before the seal. The bins are counted while they are all still open, and the **SCRAP** bin is
shut and sealed only after its chip is resting on the tally card.

The right gripper does the primary work: it turns and reads every item, calls the stream, puts every item in
its bin, shuts the scrap lid, and presses the seal sticker. The left gripper supports: it lifts each item out
of the returns tote onto the read spot, steadies items while the right gripper turns them, and places the four
count chips on the tally card. The left gripper never goes to the bin row or the seal pad, and the right
gripper never goes into the returns tote or to the tally card.

The table is set up in one of three ways. Only the returns tote moves; the read spot, the bin row, the rule
card, the tally card, the chip rack, and the seal pad are in the same place in all three.

* **Config L1:** the returns tote is just left of the middle, in front of the left arm.
* **Config L2:** the returns tote is in the back-left corner, left of the rule card.
* **Config M:** the returns tote is at the front-center, in front of the read spot.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the returns tote starts just left of the middle (**Config L1**), in the back-left corner
  (**Config L2**), or at the front-center (**Config M**). One config per episode, chosen before recording and
  never changed mid-episode.
* **Same-side rule:** the **left gripper** takes every item out of the returns tote in all three configs — the
  tote is on the left in Config L1 and L2, and the front-center in Config M is the left gripper's by
  convention. No arm reaches across the table. There is no right-side config because the bin row, the seal
  pad, and the carry lane from the read spot to the bin row fill the right side.
* **Fixed roles:** everything else is the same in all three configs — the right gripper reads, calls, bins,
  shuts the lid, and seals; the left gripper feeds the read spot and places the chips; nothing is handed over.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the returns tote in the start zone for this episode's config,
   the read spot in the middle, the four bins in a row along the right side, the rule card standing at the
   back-center, the tally card and chip rack at the front-left, and the seal pad at the front-right.
3. The printed face of the **rule card** is readable in frame, and all five of its lines can be read.
4. The **bin label** and the **fill line** on each of the four bins are readable in frame.
5. Both arms are at home with grippers open.
6. The table is bare apart from the returns tote, the read spot outline, the four bins, the rule card, the
   tally card, the chip rack, the seal pad, and robot hardware.
7. The right arm reaches the read spot, the mouth of all four bins, the seal pad, and the front seam of the
   **SCRAP** bin without stretching or leaning out.
8. The left arm reaches every corner of the returns tote (in all three configs), the read spot, the tally card,
   and every lane of the chip rack without stretching. The left arm never needs the bin row.
9. The travel from the read spot to the bin row is bare and level.

### Materials checklist

1. One **returns tote**, shallow and open, rests in the printed outline for this episode's config, on a mat
   that keeps it from sliding. Its walls are low enough that a gripper clears them going in and out.
   * **Config L1:** just left of the middle, in front of the left arm
   * **Config L2:** the back-left corner, left of the rule card and clear of it
   * **Config M:** the front-center, in front of the read spot, clear of the tally card and the seal pad
2. **Twelve items** lie loose in the returns tote in one layer, none stacked and none overlapping. Each is a
   boxed return, rigid, and small enough for the right gripper to close across its body.
3. Each item carries one **condition tag** on its top face, printed with one **grade letter**: **A**, **B**,
   **C**, or **D**. Every letter is readable from above and no tag is torn or lifting.
4. Each grade appears at least twice and at most four times across the twelve items. The grade mix changes
   between episodes.
5. Exactly **two** items carry a **hazard dot**: one red dot printed on the base of the item, readable once the
   item is turned. At least one of the two sits on an item graded A, B, or C. Which items carry a dot changes
   between episodes.
6. One **read spot**, a printed outline in the middle of the table, bare and dry. It is wide enough for one
   item with room to turn it.
7. **Four bins** stand in one row along the right side of the table, each in its printed outline, each with its
   printed **bin label** facing the front edge. Running from the front edge back: **RESTOCK**, **REFURB**,
   **LIQUIDATE**, **SCRAP**.
8. Every bin is empty, upright, wide at the mouth, and deep enough that an item released just inside the rim
   stays in. Every bin carries a readable **fill line**.
9. The **SCRAP** bin carries a hinged **lid**, folded back open against the back of the bin so the mouth is
   clear. The lid swings forward onto the mouth and snaps shut with one press.
10. One **rule card** stands upright in its stand at the back-center, printed face toward the front edge,
    carrying these five lines in this order:
    - **Hazard dot → SCRAP**
    - **A → RESTOCK**
    - **B → REFURB**
    - **C → LIQUIDATE**
    - **D → SCRAP**
11. One **tally card** at the front-left, carrying four printed rows in the order **RESTOCK**, **REFURB**,
    **LIQUIDATE**, **SCRAP**, each row with one empty slot and a readable label.
12. The **chip rack** at the front-left corner, outboard of the tally card, with four labeled lanes in that
    same order, each lane holding seven chips standing in notches and numbered 0 to 6 on their top faces.
13. One **seal pad** at the front-right, between the read spot and the front end of the bin row: one liner
    square taped flat, carrying one **seal sticker** with its near edge lifted free of the liner.
14. Before collection, confirm by hand that:
    - each of the twelve items lifts out of the returns tote without bringing a second item with it;
    - every grade letter and both hazard dots can be read from arm's length;
    - an item released just inside a bin mouth drops in and does not catch on the rim;
    - the scrap lid swings forward with one push and stays down on its own once it snaps shut;
    - the near edge of the seal sticker stays lifted off the liner and the sticker holds when pressed down.

### Workspace layout

* **Returns tote (start zone):** just left of the middle (**Config L1**), the back-left corner (**Config L2**),
  or the front-center (**Config M**). The twelve items start here and it is bare when the episode ends. The
  tote itself never moves during the episode.
* **Read spot:** the middle of the table, reached by both arms. Every item is turned, read, and called here. It
  holds one item at a time and it is bare at the start and at the end.
* **Bin row:** four bins in one straight line along the right side, running from the front edge back —
  **RESTOCK**, **REFURB**, **LIQUIDATE**, **SCRAP**. The row is never moved and never reordered.
* **Rule card:** standing at the back-center, facing the front edge. Neither gripper ever touches it.
* **Tally card:** the front-left, between the chip rack and the middle of the table.
* **Chip rack:** the front-left corner, outboard of the tally card.
* **Seal pad:** the front-right, between the read spot and the front end of the bin row.
* The left arm's zones are the returns tote, the read spot, the tally card, and the chip rack. The right arm's
  zones are the read spot, the bin row, and the seal pad. Only the read spot is shared.

### Arm assignments

* **Right gripper:** turns and reads every item, calls the grade, the hazard dot, and the stream, puts every
  item in its bin, shuts the scrap lid, and takes and presses the seal sticker. It never goes into the returns
  tote in any config.
* **Left gripper:** lifts each item out of the returns tote — from the left in Config L1 and L2, from the
  front-center in Config M — and sets it on the read spot, steadies the item
  while the right gripper turns it, presses the returns tote down if it lifts, and places the four count chips
  on the tally card.

## Vocabulary

* **Item:** one returned good to be read and binned. Twelve items are sorted in one episode.
* **Returns tote:** the shallow tote in the start zone holding the twelve items at the start.
* **Start zone:** where the returns tote stands at the start of the episode — just left of the middle
  (**Config L1**), the back-left corner (**Config L2**), or the front-center (**Config M**). One per episode,
  chosen before recording and never changed mid-episode.
* **Read spot:** the printed outline in the middle of the table where every item is turned, read, and called.
* **Body:** the main wall of an item — the part the right gripper closes across.
* **Condition tag:** the printed tag on the top face of an item, carrying one grade letter.
* **Grade letter:** the letter **A**, **B**, **C**, or **D** printed on a condition tag.
* **Hazard dot:** a red dot printed on the base of an item. It is seen only once the item is turned.
* **Rule card:** the upright card at the back-center that maps what is read off an item to one stream. It is
  read top to bottom, and the first line that fits the item wins.
* **Stream:** one of the four dispositions — **restock**, **refurb**, **liquidate**, or **scrap**. Every item
  gets exactly one.
* **Call:** naming something out loud while the item is resting on the read spot, before it is carried
  anywhere. The grade, the hazard dot, and the stream are each called.
* **Bin:** one of the four open containers in the bin row.
* **Bin mouth:** the open top of a bin, inside its rim. An item is released here and nowhere else.
* **Bin label:** the printed stream name on the front face of a bin.
* **Fill line:** the marked level on a bin that its contents must stay below.
* **Full bin:** a bin whose contents have reached its fill line.
* **Lowered in:** the gripper carries the item down through the bin mouth, below the rim, and opens there.
  Nothing is ever released above the rim.
* **Touched down:** for a scrap item, the item is lowered until it rests on the bin floor or on what is already
  in the bin, and only then does the gripper open.
* **Caught on the rim:** the item is left lying across the bin mouth or hooked on the rim instead of inside the
  bin.
* **Read spot clear:** the read spot holds no item and no debris.
* **Count chip:** one numbered chip from the chip rack, taken by closing across its two side faces with the
  number on top and lifting it straight up out of its notch.
* **Lane:** one labeled column of the chip rack. A chip for a row is only ever taken from the lane whose label
  matches that row.
* **Card slot:** the printed slot at the end of a tally card row. One chip rests in it, number face up and
  readable from above.
* **Settled:** the chip stays put for 2 seconds after the left gripper lifts clear, with nothing rocking,
  sliding, or falling over.
* **Scrap lid:** the hinged lid on the SCRAP bin. It starts folded back open and is swung forward and snapped
  shut in Step 8.
* **Snapped shut:** the scrap lid lies down on the bin mouth and stays down on its own with both grippers
  clear of it.
* **Lid seam:** the line at the front of the SCRAP bin where the shut lid edge meets the bin wall.
* **Seal pad:** the liner square at the front-right carrying one seal sticker with its near edge lifted free.
* **Seal sticker:** the single sticker that is pressed across the lid seam. One sticker per episode, laid down
  once.
* **Sealed:** the seal sticker lies flat across the lid seam, bridging the lid and the bin wall, and the lid
  does not lift when the right gripper nudges its edge.

## Steps

Run Steps 1–5 as a loop, one item at a time, until the returns tote is empty. Then run Steps 6, 7, and 8, and
end the episode with Step 9.

Only the pick in Step 1 depends on the config: the **left gripper** takes each item out of the returns tote
wherever this episode's config puts it and carries it to the read spot. Every other line is the same in all
three configs.

### Step 1: Move one item to the read spot

**Goal:** exactly one item rests on the read spot, ready to be read.

Look where the returns tote is before reaching for the first item.

* **IF the returns tote is just left of the middle (Config L1):** with the **left gripper**, close across the
  body of one item in the returns tote, lift it straight up clear of the tote wall, and carry it level, low
  over the table, a short way right to the read spot.
* **IF the returns tote is in the back-left corner (Config L2):** with the **left gripper**, close across the
  body of one item in the returns tote, lift it straight up clear of the tote wall, and carry it level, low
  over the table, forward and right to the read spot, keeping clear of the rule card.
* **IF the returns tote is at the front-center (Config M):** with the **left gripper**, close across the body
  of one item in the returns tote, lift it straight up clear of the tote wall, and carry it level, low over
  the table, straight back to the read spot.

Then, in all three:

* Take one item only. If a second item comes up with it, lower both back into the tote with the **left
  gripper** and take one again.
* With the **left gripper**, set the item down on the read spot. Never drag or slide an item across the table.
* Open the **left gripper** and lift clear.

**Check:** exactly one item rests on the read spot and the spot holds nothing else. If a second item is on the
spot, pick it up with the **left gripper** and lay it back in the returns tote.

**Expected state:** one item on the read spot, the rest of the items still lying in the returns tote, and both
grippers empty.

### Step 2: Read the item

**Goal:** the grade letter and the hazard dot are both known for the item, while it is still on the read spot.

* With the **right gripper**, close on the body of the item, lift it just clear of the read spot, and turn it
  once so the **condition tag** on the top face and the **base** both come into view of the camera.
* With the **left gripper**, steady the item from the other side if it swings or slips.
* With the **right gripper**, set the item back down on the read spot.
* Call the **grade letter** on the condition tag: **A**, **B**, **C**, or **D**.
* Call whether the item carries a **hazard dot** on its base. Every item is checked for a dot, whatever its
  grade.

**Check:** the grade letter has been called and the base has been brought into view and called dot or no dot.
If the letter or the base cannot be read, lift the item once more with the **right gripper** and turn it the
other way before calling it.

**Expected state:** the item back on the read spot with its grade and its dot called, and both grippers clear.

### Step 3: Call the stream from the rule card

**Goal:** exactly one stream is named for the item, while it is still resting on the read spot.

* Read the **rule card** at the back-center from the top line down, and take the first line that fits the item:
  1. **Hazard dot → SCRAP**
  2. **A → RESTOCK**
  3. **B → REFURB**
  4. **C → LIQUIDATE**
  5. **D → SCRAP**
* An item with a hazard dot goes to **SCRAP** whatever its grade letter says. The dot line is read first and it
  wins.
* Call the stream: **restock**, **refurb**, **liquidate**, or **scrap**.
* Do not carry the item toward the bin row until a stream has been called for it.

**Check:** one stream has been called, it matches the first rule card line that fits the grade and dot called in
Step 2, and the item is still on the read spot.

**Expected state:** the item on the read spot with one stream called for it, and both grippers clear.

### Step 4: Put the item in its bin

**Goal:** the item is released inside the mouth of the bin for its called stream.

* With the **right gripper**, close on the middle of the item's body and lift it clear of the read spot.
* With the **right gripper**, carry it to the bin for the called stream, reading the **bin label** on the way:
  RESTOCK nearest the front edge, then REFURB, then LIQUIDATE, then SCRAP farthest back.
* Bring the item over the **bin mouth** so the whole item is inside the rim.
* Lower it through the mouth, below the rim, then open the **right gripper**. Never throw, toss, or drop an item
  toward a bin from above the rim.
* For a **scrap** item, keep lowering with the **right gripper** until it touches down on the bin floor or on
  what is already in the bin, and only then open the gripper.
* Once the **right gripper** has opened over a bin, that item stays in that bin. Never reach into a bin to take
  an item back out.

**Check:** the item landed inside the bin and is not caught on the rim. If it is caught, push it down through
the mouth with the **right gripper**. Then check the bin's contents are still below its **fill line**. If a bin
has reached its fill line, stop the episode and report a full bin.

**Expected state:** the item inside the bin its stream names, the right gripper empty, and the scrap lid still
folded back open.

### Step 5: Clear the read spot and take the next item

**Goal:** the read spot is bare and ready for the next item.

* Confirm the read spot holds no item and no debris. If anything is left, put it where its called stream says
  with the **right gripper**.
* If the returns tote still holds an item, go back to Step 1 and take the next one.
* If the returns tote is empty, go on to Step 6.

**Check:** the read spot is bare and the returns tote is either empty or still holds items to work.

**Expected state:** the read spot bare, and the count of items still in the returns tote one lower than before.

### Step 6: Sweep the tote and read the bin row

**Goal:** the returns tote and the read spot are bare, and every bin holds only what its label calls for.

* With the **left gripper** clear, look over the returns tote from above and confirm no item is left in a corner
  or under the tote wall. If one is left, take it through Steps 1 to 5.
* Confirm the read spot holds nothing.
* With the **right gripper** clear of the row, look into each bin mouth in turn, front to back, and confirm the
  contents match the bin label: RESTOCK, REFURB, LIQUIDATE, SCRAP.
* Confirm all four bins are still upright, still in the same order front to back, still labelled toward the
  front edge, and all still below their fill lines.
* Confirm the **scrap lid** is still folded back open, so the SCRAP bin can be counted in Step 7.

**Check:** every one of the twelve items is now inside exactly one bin, the returns tote is bare, and the bin
row has not moved.

**Expected state:** the returns tote bare, the read spot bare, the four bins holding the sorted items, and all
four bin mouths open.

### Step 7: Tally the four streams

**Goal:** four count chips resting in the four card slots, each matching what is in its bin.

* Count what is in the **RESTOCK** bin.
* With the **left gripper**, close across the side faces of the chip carrying that number in the **RESTOCK
  lane**, lift it straight up out of its notch, carry it level to the **RESTOCK row**, lower it flat into the
  slot until it is resting, and release.
* Lift the **left gripper** clear.
* Do the same for **REFURB**, then **LIQUIDATE**, then **SCRAP**, in that order, always taking the chip from
  the lane whose label matches the row.
* Count the bin before going to the rack. Take each chip straight up out of its notch and leave the chips
  beside it standing.

**Check:** four chips rest flat in the four card slots, settled, number face up and readable from above, each
matching the count in the bin named on its row, and each taken from its own lane. The four numbers add up to
**twelve**. If they do not add up to twelve, count every bin again and correct the chips before going on. If a
wrong chip went down, lift it clear with the **left gripper**, stand it back in its own notch, and place the
right one.

**Expected state:** four chips resting on the tally card, the chip rack otherwise untouched, and the four bins
still open and holding the sorted items.

### Step 8: Shut and seal the scrap bin

**Goal:** the SCRAP bin is snapped shut and one seal sticker lies flat across the lid seam.

* Confirm the **SCRAP** row chip is already resting on the tally card. The scrap bin is never sealed before it
  has been counted.

#### 8.1 Shut the lid

* With the **right gripper**, close on the top edge of the **scrap lid** where it is folded back, swing it
  forward and down onto the bin mouth, and press down along its front edge until it snaps shut.
* Open the **right gripper** and lift clear.
* Confirm the lid is **snapped shut**: it lies down on the mouth and stays down on its own, with nothing caught
  under it holding it up.
* If the lid rides up on an item, lift the lid back open with the **right gripper**, push the item down into
  the bin with the **right gripper**, and shut the lid again.

#### 8.2 Press the seal sticker

* With the **right gripper**, close on the lifted near edge of the **seal sticker** at the seal pad and lift it
  straight up off the liner square.
* With the **right gripper**, carry it level to the SCRAP bin with the printed face up, lower it onto the
  middle of the **lid seam** so it bridges the lid edge and the bin wall, press it down for 2 seconds, and lift
  straight off.
* One sticker, one press, on the seam and nowhere else. The sticker is laid down once. Do not lift a stuck
  sticker to place it again, because the adhesive loses its hold on a second try.
* With the **right gripper**, nudge the front edge of the lid once. The lid must not lift.

**Check:** the sticker lies flat across the lid seam with part of it on the lid and part on the bin wall,
printed face up, pressed down across its whole width with no corner lifting, and the lid does not lift when the
**right gripper** nudges it. If a corner lifts, press along it again with the **right gripper**. If the lid
lifts, the seal has failed: stop the episode and report it.

**Expected state:** the SCRAP bin shut and sealed, the seal pad holding only its bare liner square, and the
other three bins still open.

### Step 9: End the episode

**Goal:** recording ends with the tote empty, every item binned, the tally placed, and the scrap bin sealed.

1. Confirm the end state:
   - the returns tote is bare and the read spot is bare;
   - every item sits in the bin its called stream names, with none caught on a rim;
   - the four bins stand in their outlines, in order, upright, and below their fill lines;
   - four chips rest in the four card slots, number face up, adding up to twelve;
   - the SCRAP bin is snapped shut with one seal sticker across its lid seam.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

### After each episode

1. Peel the used seal sticker off the SCRAP bin and discard it. Stickers are single use. Lift the scrap lid
   back open and fold it against the back of the bin.
2. Empty all four bins. Stand each bin back in its printed outline with its label facing the front edge, in the
   order RESTOCK, REFURB, LIQUIDATE, SCRAP from the front edge back.
3. Lift the four chips out of the card slots with your hand and stand each one back in its own notch in its own
   lane, number up, with every lane holding chips 0 to 6 in number order.
4. Rebuild the twelve-item set. Change the grade mix from the last episode, keeping each grade at two, three,
   or four items. Move both hazard dots onto different items, keeping exactly two dots and keeping at least one
   of them on an item graded A, B, or C.
5. Replace any condition tag that is torn, curling, or worn so its letter is hard to read.
6. Lay the twelve items loose in the returns tote in one layer, none stacked and none overlapping, and set the
   tote in the outline for the next episode's config — just left of the middle (Config L1), the back-left
   corner (Config L2), or the front-center (Config M).
7. Lay a fresh seal sticker on the liner square at the seal pad and lift its near edge free of the liner.
8. Wipe the read spot clean and dry.
9. Run both Setup checklists before the next episode.

### At the end of the session

1. Inspect the item set. Replace anything crushed, split, or too dented for the right gripper to close on, and
   replace any item whose condition tag will not stay stuck.
2. Check the scrap lid: it swings freely, snaps shut with one press, and stays down on its own. Replace the bin
   if the hinge is loose or the lid will not stay shut.
3. Check the chip rack: every lane holds chips 0 to 6, every number is readable, and every chip stands in its
   notch. Replace any chip whose number has worn away and any tally card whose printed rows have worn away.
4. Confirm the rule card still stands square in its stand, facing the front edge, with all five lines readable.
5. Leave the four bins empty and in order along the right side, the scrap lid folded back open, the read spot
   bare in the middle, the returns tote holding the twelve-item set in the outline for the next session's
   config, the tally card empty, the
   chip rack full, and one fresh seal sticker on the seal pad.

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

**Note on the start position:** the violations below were written for Config L1 (the returns tote just left
of the middle, in front of the left arm). The pickup and arm-role cues will be rewritten later to cover all
three start positions; they are left as they are for now. Until then, anything that does not match the
episode's config goes under **Config misaligned**.

**Violation: Config misaligned**
* **Visible cue:** what the operator does does not match the config on the table — the returns tote is not in
  the start zone for the config; a gripper reaches across the table for an item, including the right gripper
  going into the tote at the front-center; or the wrong IF line is followed.
* **SOP rule broken:** the start position and the same-side rule (the left gripper takes every item out of the
  returns tote in all three configs, and no arm reaches across the table; the IF line followed is the one for
  the config on the table).
* **Coaching note:** look where the returns tote is before the first reach, then follow that config's IF line
  through Step 1.

**Violation: More than one item taken at once**
* **Visible cue:** the left gripper lifts or carries two items out of the returns tote in one pick, or a second
  item comes up with the first and is worked on instead of being laid back in the tote.
* **SOP rule broken:** Step 1 (take one item only; if a second comes up, lower both back into the tote and take
  one again).
* **Coaching note:** one item per pick. If two come up, put both back and start again.

**Violation: Item dragged instead of lifted**
* **Visible cue:** the left gripper slides or pushes an item across the tote floor, the read spot, or the table
  instead of lifting it clear and carrying it.
* **SOP rule broken:** Step 1 (lift the item straight up clear of the tote wall and carry it to the read spot).
* **Coaching note:** lift it clear, carry it, set it down. Never push it along the table.

**Violation: Item started or worked outside its zone**
* **Visible cue:** an item is started from somewhere other than the returns tote, is set down anywhere other
  than the read spot, or is turned, read, or called off the read spot — including in mid-air on the way to a
  bin.
* **SOP rule broken:** Steps 1–3 (every item comes out of the returns tote, and every turn, read, and call
  happens with the item on the read spot).
* **Coaching note:** tote to read spot, read on the read spot, read spot to bin. Nothing happens anywhere else.

**Violation: Base not brought into view**
* **Visible cue:** the right gripper calls the grade from the top face only. The item is never turned, or is
  turned so its base never comes into the camera's view, and the episode moves on.
* **SOP rule broken:** Step 2 (turn the item once so the condition tag and the base both come into view, and
  call whether it carries a hazard dot).
* **Coaching note:** turn every item over, every time. The dot is on the base and you cannot call it from the
  top.

**Violation: Hazard dot ignored**
* **Visible cue:** an item whose base shows a red hazard dot is carried to the bin for its grade letter —
  RESTOCK, REFURB, or LIQUIDATE — instead of SCRAP.
* **SOP rule broken:** Step 3 (read the rule card from the top line down; the hazard dot line is first and wins
  whatever the grade letter says).
* **Coaching note:** dot first, letter second. A dot sends the item to SCRAP no matter what the tag reads.

**Violation: Stream not called before the carry**
* **Visible cue:** the right gripper lifts an item off the read spot and carries it toward the bin row without a
  stream having been called for it.
* **SOP rule broken:** Step 3 (call one stream with the item resting on the read spot, before it is carried
  anywhere).
* **Coaching note:** read the card, name the stream, then move. Never decide on the way.

**Violation: Item put in the bin the rule card does not name**
* **Visible cue:** the right gripper releases an item into a bin whose label does not match the rule card line
  for the grade and dot visible on that item, and the episode moves on.
* **SOP rule broken:** Steps 3 and 4 (take the first rule card line that fits, and carry the item to the bin for
  that stream, reading the bin label on the way).
* **Coaching note:** read the label on the bin before you lower the item in. Rule card first, bin label second.

**Violation: Item dropped in from above the rim**
* **Visible cue:** the right gripper opens above the bin rim and the item falls in, is tossed toward the bin, or
  is released before it passes below the rim.
* **SOP rule broken:** Step 4 (bring the item inside the mouth, lower it below the rim, and only then open the
  gripper).
* **Coaching note:** take it down inside the bin before you let go. No drops from above.

**Violation: Scrap item released before it touched down**
* **Visible cue:** the right gripper opens on a scrap item while it is still hanging inside the SCRAP bin, and
  the item falls onto the bin floor or onto the contents below it.
* **SOP rule broken:** Step 4 (lower a scrap item until it touches down on the bin floor or on what is already
  in the bin, and only then open the gripper).
* **Coaching note:** scrap is placed, never dropped. Feel it land, then open.

**Violation: Item left caught on the rim**
* **Visible cue:** an item ends up lying across a bin mouth or hooked on the rim, and the episode moves on to
  the next item or to the tally.
* **SOP rule broken:** Step 4 (confirm the item landed inside the bin, and push it down through the mouth with
  the right gripper if it is caught).
* **Coaching note:** look into the bin after every release. If it is on the rim, push it in.

**Violation: Item taken back out of a bin**
* **Visible cue:** either gripper reaches into a bin mouth and lifts an item back out, whatever the reason.
* **SOP rule broken:** Step 4 (once the right gripper has opened over a bin, the item stays in that bin).
* **Coaching note:** decide before you release. A wrong bin is tagged, not undone.

**Violation: Read spot not cleared**
* **Visible cue:** the left gripper brings the next item onto the read spot while the last item or debris from
  it is still lying there.
* **SOP rule broken:** Step 5 (confirm the read spot holds no item and no debris before taking the next item).
* **Coaching note:** finish one item completely, clear the spot, then pick the next.

**Violation: Full bin not reported**
* **Visible cue:** a bin's contents reach or pass its fill line and the episode keeps loading that bin.
* **SOP rule broken:** Step 4 (check the fill line after each release; if a bin has reached it, stop the episode
  and report a full bin).
* **Coaching note:** glance at the fill line every time you release. A full bin ends the episode.

**Violation: Bin row moved or reordered**
* **Visible cue:** either gripper pushes, drags, tips, or turns a bin; or a bin ends the episode out of its
  outline, out of the front-to-back order, or with its label turned away from the front edge.
* **SOP rule broken:** Steps 4, 6, and 8 (the four bins stay in their outlines, in the order RESTOCK, REFURB,
  LIQUIDATE, SCRAP from the front edge back, labels facing the front edge).
* **Coaching note:** come down into the mouth from above. Do not lean the gripper on the bin wall.

**Violation: Sweep skipped or an item left behind**
* **Visible cue:** the episode ends with an item still in the returns tote or still on the read spot, or the
  bin mouths are never looked into after the last item.
* **SOP rule broken:** Step 6 (look over the returns tote and the read spot, then look into each bin mouth front
  to back and confirm the contents match the label).
* **Coaching note:** twelve items in, twelve items out. Sweep the tote and read the row before you tally.

**Violation: Tally started before the tote is empty**
* **Visible cue:** the left gripper takes a chip out of the rack while items are still lying in the returns tote
  or on the read spot.
* **SOP rule broken:** Steps 5 and 7 (the loop runs until the returns tote is empty, and only then is any stream
  tallied).
* **Coaching note:** sort everything first. The tally is the last count, not a running one.

**Violation: Chip placed without counting, or not matching its bin**
* **Visible cue:** the left gripper goes to the chip rack without the bin for that row having been looked into;
  or a chip is left resting in a slot whose number does not match the count in the bin named on that row; or a
  chip is taken from a lane whose label does not match the row it goes to.
* **SOP rule broken:** Step 7 (count the bin, then take the chip carrying that number from the lane whose label
  matches the row, and lower it into that row's slot).
* **Coaching note:** look in the bin, count it, then reach for the chip. Every chip comes from its own lane.

**Violation: Tally does not come to twelve**
* **Visible cue:** the four chips resting on the tally card add up to a number other than twelve, and the
  episode moves on to the seal or to the ending.
* **SOP rule broken:** Step 7 (the four numbers add up to twelve; if they do not, count every bin again and
  correct the chips before going on).
* **Coaching note:** add the four chips before you move on. Twelve went in, so twelve come out.

**Violation: Scrap bin sealed before the tally**
* **Visible cue:** the right gripper shuts the scrap lid, or lays the seal sticker, while the SCRAP row slot on
  the tally card is still empty.
* **SOP rule broken:** Steps 7 and 8 (all four streams are tallied first, and the scrap bin is shut and sealed
  only once its chip is resting).
* **Coaching note:** count it while you can still see into it. Sealing is the last thing that happens to that
  bin.

**Violation: Scrap lid not shut, or shut on an item**
* **Visible cue:** the seal sticker goes on while the lid is still folded back or standing ajar; or the lid
  rides up on an item sticking out of the bin and does not stay down on its own.
* **SOP rule broken:** Step 8.1 (swing the lid forward, press it until it snaps shut, and confirm it stays down
  on its own with nothing caught under it).
* **Coaching note:** press it shut and take your gripper away. If it springs back up, push the item down and
  shut it again.

**Violation: Seal sticker off the seam**
* **Visible cue:** the sticker ends up wholly on the lid, wholly on the bin wall, or on another bin or the
  table, instead of bridging the lid edge and the bin wall at the front of the SCRAP bin.
* **SOP rule broken:** Step 8.2 (lower the sticker onto the middle of the lid seam so it bridges the lid edge
  and the bin wall).
* **Coaching note:** aim for the line where the lid meets the bin. Half on the lid, half on the bin.

**Violation: Seal sticker not pressed, or the seal not checked**
* **Visible cue:** the right gripper lays the sticker and lifts straight off with no press; or it peels a stuck
  sticker up and lays it again; or a second sticker is taken from the seal pad; or the lid edge is never nudged
  after the press.
* **SOP rule broken:** Step 8.2 (press the sticker down for 2 seconds, lay it once, and then nudge the front
  edge of the lid to confirm it does not lift).
* **Coaching note:** press and hold, one sticker only, then nudge the lid. A seal you did not test is not a
  seal.

**Violation: Wrong arm used**
* **Visible cue:** an action assigned to one gripper is done by the other, including the right gripper reaching
  into the returns tote or working the tally card or chip rack, or the left gripper calling a stream, going to
  the bin row, shutting the scrap lid, or touching the seal pad.
* **SOP rule broken:** Steps 1–8 (the left gripper feeds the read spot, steadies items, and places the chips;
  the right gripper reads, calls, bins, shuts the lid, and seals).
* **Coaching note:** left gripper feeds and tallies, right gripper reads, bins, and seals. It does not swap.

**Violation: Item dropped, or a fixture knocked off its spot**
* **Visible cue:** either gripper drops an item on the table or the floor; or tips, pushes, or drags the returns
  tote, the tally card, the chip rack, the seal pad, or the rule card off its spot; or knocks the rule card over
  or turns it away from the front edge.
* **SOP rule broken:** Steps 1–8 (the returns tote, the tally card, the chip rack, the seal pad, and the rule
  card stay on their spots, and every carry stays level and low over the table).
* **Coaching note:** work slower and lower over the table, and keep each carry short.

**Violation: Wrong episode ending**
* **Visible cue:** recording stops before the empty tote, the four bins, the four chips, and the sealed scrap
  bin are confirmed; an arm is not home; a gripper is closed; or an arm does something else after homing.
* **SOP rule broken:** Step 9 (confirm the end state, return both arms home with grippers open as their final
  action, then stop recording).
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than tagging
them as SOP violations.

* Recording stops or pauses during the episode.
* A camera drops frames or loses its feed.
* An arm or gripper fails, drifts, or reports a motor error.
* An item arrives with its condition tag missing, torn off, or worn away, so no grade can be read from it.
* An item arrives crushed or split so the right gripper cannot close across its body.
* A bin is cracked, will not stand upright, or has no readable label or fill line.
* The scrap lid hinge is broken, so the lid will not swing forward or will not stay shut.
* The seal sticker will not lift off its liner, tears on the way up, or has no tack left and will not hold.
* A chip's number cannot be read, a chip lane is short, or a tally card slot is torn.
* The rule card arrives with a line unreadable or missing.

## Annotation subtasks (from SOP)

1. Lift one item out of the returns tote with the left gripper and set it on the read spot
2. Turn the item with the right gripper and call its grade letter and its hazard dot
3. Read the rule card and call the stream
4. Lower the item into the bin its stream names
5. Clear the read spot and take the next item
6. Sweep the returns tote and read the four bin labels
7. Count a bin and place its count chip in the tally card row
8. Swing the scrap lid forward and snap it shut
9. Take the seal sticker off the pad and press it across the lid seam
10. Nudge the lid edge to confirm the seal holds
11. Confirm the end state, return both arms home, and end the episode
