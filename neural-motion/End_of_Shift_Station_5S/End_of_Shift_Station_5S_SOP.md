# End-of-Shift Station 5S SOP (1x Station)

One episode closes out one workstation at the end of a shift. Work the five phases in this fixed
order: **clear the surface, restage the supplies to their marks, empty the scrap tub, wipe the
bench, sign the shift log.** Stray counts vary per episode. The marked items, the bins, the log
board, and the order of the phases never vary.

Every item that belongs at this station has a **mark**. A mark is a taped outline on the bench,
drawn a little larger than the item, so a correctly placed item shows a thin band of tape all the
way around it. Anything on the bench without an outline is a **stray** and does not belong at the
station.

The **right gripper** does the main work: it restages the three supply items, wipes the bench, and
signs the log with the pen. The **left gripper** does the supporting work: it moves strays into the
returns bin, empties the scrap tub into the waste bin, and holds the log board flat while the right
gripper signs. Both bins and the scrap tub sit on the left of the bench. The supply marks, the
cloth, the pen, and the log board sit on the right. Neither gripper reaches across the bench.

The bench is set up in one of three ways. Only the three supply items move; the strays are scattered
across the working area, and the bins, the scrap tub, the marks, the cloth, the pen, and the log
board are in the same place in all three.

* **Config L:** the supply items stand at the left end of the working area, beside the scrap tub.
* **Config M:** the supply items stand at the front-center of the working area, at the front bench
  edge.
* **Config R:** the supply items stand at the right end of the working area, in front of the mark
  strip.

Where a step depends on the setup it says so on an **IF** line — look at the bench and follow the
line that matches.

What stays constant across all sessions:

* **Start position:** the supply items start at the left end of the working area (**Config L**), the
  front-center (**Config M**), or the right end (**Config R**). One config per episode, chosen before
  recording and never changed mid-episode.
* **Same-side rule:** the gripper on the supply items' side takes each one — the left gripper in
  Config L and M, the right gripper in Config R. No arm reaches across the bench.
* **Hand-over rule:** in Config L and M the mark strip is too far for the left gripper, so it **hands
  each supply item over** to the right gripper above the middle of the working area: the left gripper
  holds the item still, the right gripper closes on the opposite side of it, and only then does the
  left gripper open. The right gripper carries it on to its mark. Nothing is handed over in Config R.
* **Fixed roles:** the right gripper sets every supply item on its mark, wipes the bench, and signs
  the log; the left gripper bins the strays, empties the scrap tub, and holds the log board. The five
  phases run in the same order in every config.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole bench: the three supply marks along the back right, the
   returns bin at the back left, the waste bin at the front left, the scrap tub mark on the left
   between the two bins, the cloth mark at the right edge, the log board at the front right, the pen
   mark beside it, and the front bench edge.
3. Every taped outline is fully visible from above and none is hidden by an item, an arm, or a
   shadow.
4. The mouths of the returns bin and the waste bin are visible from above, so what lands inside each
   one can be seen.
5. Both arms are at home with grippers open.
6. The bench holds nothing except the marked items, the two bins, the log board, the staged strays,
   and robot hardware.
7. The right arm reaches all three supply marks, the cloth mark, the pen mark, the sign-out box, the
   front and back of the working area, and (Config R) the supply items at the right end of the
   working area without stretching. The left arm reaches both bin mouths, the scrap tub mark, the
   top edge of the log board, and (Config L and M) the supply items in the start zone without
   stretching.

### Materials checklist

Stray counts vary per episode. Item types, marks, and staging positions do not.

1. **Three supply items**, each with its own taped outline on the back-right mark strip. Left to
   right the outlines are: **parts tote**, **fastener cup**, **tape roll**. All three items start
   **off their marks**, standing together in the start zone for this episode's config, each one
   clearly away from its own outline:
   * **Config L:** the left end of the working area, beside the scrap tub.
   * **Config M:** the front-center of the working area, at the front bench edge.
   * **Config R:** the right end of the working area, in front of the mark strip.
   All three outlines start empty.
2. The **parts tote** is an open-top tote holding small parts. It stays loaded for the whole
   episode; nothing is added to it and nothing is taken out of it.
3. The **fastener cup** is a straight-sided cup. The **tape roll** is one roll of tape with an open
   hole through the middle.
4. The **scrap tub** is an open-top tub standing **on its mark**, on the left of the bench between
   the two bins. It holds **4–8 scrap pieces** and nothing else.
5. The **returns bin** is at the back left, open, mouth clear, and **empty**.
6. The **waste bin** is at the front left, open, mouth clear, and **empty**.
7. The **cloth** is one wiping cloth, damp and wrung out so it does not drip, folded flat **on its
   mark** at the right edge of the bench.
8. The **log board** is a clipboard at the front right corner, holding one shift log sheet with an
   empty **sign-out box** printed across its top. The log board does not move during the episode.
9. The **pen** is one uncapped marker, lying **on its mark**, a taped outline just above the log
   board.
10. **3–6 strays** are scattered across the working area, for example an empty drink cup, a torn
    wrapper, a small carton, a used glove. No stray has an outline anywhere on the bench, and no
    stray starts inside a bin, inside the scrap tub, or on the log board.

### Workspace layout

Everything below is a fixed area of the bench, judged by eye against the bench edges, the taped
outlines, and the fixtures standing on it.

- **Back right — the mark strip:** three taped outlines in a row, left to right: parts tote,
  fastener cup, tape roll.
- **Back left — returns bin:** open-top, on the bench, mouth clear. Strays end here.
- **Front left — waste bin:** open-top, on the bench, mouth clear. Scrap ends here.
- **Left, between the two bins — scrap tub mark:** one taped outline. The scrap tub starts and ends
  here.
- **Right edge, mid-bench — cloth mark:** one taped outline. The cloth starts and ends here.
- **Front right — log board:** a clipboard flat on the bench, its top edge toward the back edge, with
  the sign-out box across its top. Fixed for the whole episode.
- **Above the log board — pen mark:** one taped outline. The pen starts and ends here.
- **Working area:** the open band of bench between the mark strip at the back and the front bench
  edge, running from the two bins on the left to the log board on the right. This is where the
  strays start, it holds the supply start zone, and it is the band that gets wiped.
- **Supply start zone:** where the three supply items stand at the start — the left end of the
  working area (**Config L**), the front-center (**Config M**), or the right end (**Config R**). One
  per episode. It is bare once Step 2 is done. In Config L and M every supply item is handed over
  above the middle of the working area.

### Arm assignments

- **Right gripper — main work:** restages the parts tote, the fastener cup, and the tape roll onto
  their marks, picking each one from the start zone in Config R and taking it from the left gripper
  above the middle of the working area in Config L and M; wipes the working area with the cloth and
  returns the cloth to its mark; draws the sign-out stroke with the pen and returns the pen to its
  mark.
- **Left gripper — supporting work:** moves every stray into the returns bin; in Config L and M picks
  each supply item from the start zone and hands it over to the right gripper; empties the scrap tub
  into the waste bin and returns the tub to its mark; presses the log board flat while the right
  gripper signs.

## Vocabulary

- **Mark:** a taped outline printed on the bench for one named item. Each outline is drawn a little
  larger than its item.
- **On its mark:** the item stands inside its own outline, upright, with a thin band of tape showing
  all the way around it and no part of the item covering or crossing the tape.
- **Marked item:** any item that has an outline on this bench: the parts tote, the fastener cup,
  the tape roll, the scrap tub, the cloth, and the pen. A marked item is never binned.
- **Stray:** anything resting on the bench that is not a marked item, not the log board, not a bin,
  and not robot hardware. A stray has no outline. No other test is applied.
- **Working area:** the open band of bench between the mark strip at the back and the front bench
  edge, from the two bins on the left to the log board on the right.
- **Start zone:** where the three supply items stand at the start of the episode — the left end of
  the working area (**Config L**), the front-center (**Config M**), or the right end (**Config R**).
  One per episode, chosen before recording and never changed mid-episode.
- **Hand over:** the left gripper holds a supply item still above the middle of the working area,
  the right gripper closes on the opposite side of the item, and only then does the left gripper
  open and lift clear. Config L and M only, because the mark strip is too far for the left gripper.
- **Squared to the front edge:** the item's front face, or its long edge, looks parallel to the
  front bench edge.
- **Scrap:** everything sitting in the scrap tub at the start of the episode. Scrap is not sorted
  and not inspected. Whatever is in the tub goes in the waste bin.
- **Tub empty:** seen from above, no piece is left on the tub floor and no piece is stuck against an
  inside wall.
- **Wipe lane:** one straight pass of the cloth across the working area, pressed flat on the bench,
  running from the back of the working area to the front bench edge without the cloth leaving the
  bench.
- **Damp trail:** the darker band the damp cloth leaves behind on the bench, visible from above
  right after a lane. Unvalidated. Confirm the trail shows on this bench surface at the station.
- **Stable placement:** the item stays still for 2 seconds after release and does not rock, roll,
  tip, or slide.
- **Working area clear:** no stray, no supply item, no scrap piece, and no cloth is left anywhere in
  the working area.

## Steps

Step 2 depends on where the supply items start: in Config L and M the **left gripper** takes each
item from the start zone and **hands it over** to the right gripper above the middle of the working
area; in Config R the **right gripper** takes each item itself. The right gripper sets every item on
its mark in all three. Every other line in Steps 1 to 6 is the same in all configs.

### Step 1: Clear the station surface

**Goal:** every stray is inside the returns bin and no stray is left anywhere on the bench.

- Apply the stray test in Vocabulary. If the item has an outline, it is a marked item. Leave it
  where it stands and do not bin it.
- Work one stray at a time. Start with the stray nearest the front bench edge and work back.
- With the **left gripper**, grasp the stray at its widest visible point. Close only hard enough to
  hold it.
- Lift it clear of the bench and carry it to the returns bin at the back left. Do not pass it over
  the scrap tub, the waste bin, the log board, or the mark strip.
- Center it over the returns bin mouth and release it. Do not throw it and do not release it outside
  the mouth.
- If a stray misses the bin, pick it up again with the **left gripper** and bin it once more.
- Repeat until no stray is left on the bench.

**Check:** the working area holds nothing except the parts tote, the fastener cup, and the tape
roll. If a stray is still on the bench, bin it before starting Step 2.

**Expected state:** the returns bin holds every stray. The three supply items still stand off their
marks in the working area. The scrap tub, the cloth, and the pen are untouched on their marks.

### Step 2: Restage the supplies to their marks

**Goal:** the parts tote, the fastener cup, and the tape roll each stand on its own mark, squared to
the front edge.

Restage them in this fixed order: **parts tote, then fastener cup, then tape roll.** The **right
gripper** sets all three on their marks. Do not touch the scrap tub, the cloth, or the pen in this
step. Those three end on their marks in Steps 3, 4, and 5.

#### 2.1 Parts tote

Look where the supply items are before reaching for the tote.

- **IF the supply items are at the left end of the working area (Config L):** with the **left
  gripper**, grasp the tote's rim at the middle of the side nearest the front bench edge, lift it
  straight up, and carry it level, straight right, to above the middle of the working area. Hold it
  still. The **right gripper** closes on the rim at the middle of the opposite side; the left
  gripper opens and lifts clear.
- **IF the supply items are at the front-center of the working area (Config M):** with the **left
  gripper**, grasp the tote's rim at the middle of the side nearest the front bench edge, lift it
  straight up, and carry it level, straight back, to above the middle of the working area. Hold it
  still. The **right gripper** closes on the rim at the middle of the opposite side; the left
  gripper opens and lifts clear.
- **IF the supply items are at the right end of the working area (Config R):** with the **right
  gripper**, grasp the tote's rim at the middle of the side nearest the front bench edge and lift it
  straight up.

Then, in all three:

- Keep it level for the whole carry, so nothing tips out of it.
- Carry it with the **right gripper** to the leftmost outline on the mark strip.
- Turn it so its long side is squared to the front bench edge.
- Lower it inside the outline and release when it is stable.

#### 2.2 Fastener cup

- **IF Config L or M:** with the **left gripper**, grasp the cup around its outside at the middle of
  its height, lift it clear of the bench, upright, and hand it over above the middle of the working
  area — the **right gripper** closes on the opposite side of the cup at the same height, then the
  left gripper opens and lifts clear. **IF Config R:** with the **right gripper**, grasp the cup
  around its outside at the middle of its height and lift it clear of the bench, keeping it upright.
- Neither gripper grasps the cup's rim or reaches inside it.
- Carry it with the **right gripper** to the middle outline on the mark strip, keeping it upright.
- Lower it inside the outline, upright, and release when it is stable.

#### 2.3 Tape roll

- **IF Config L or M:** with the **left gripper**, grasp the roll across its outer rim, lift it clear
  of the bench, flat, and hand it over above the middle of the working area — the **right gripper**
  closes across the outer rim on the opposite side, then the left gripper opens and lifts clear.
  **IF Config R:** with the **right gripper**, grasp the roll across its outer rim and lift it clear
  of the bench, keeping it flat.
- Neither gripper goes through the hole in the middle.
- Carry it with the **right gripper** to the rightmost outline on the mark strip, keeping it flat.
- Lay it flat inside the outline and release when it is stable.

**Check:** each of the three items stands inside its own outline with a thin band of tape showing
all the way around it, and the tote is squared to the front bench edge. If an item covers or crosses
its tape, regrasp it at the same grip point with the **right gripper**, lift it clear, and set it
down inside the outline again.

**Expected state:** the working area is bare. All three supply marks are filled.

### Step 3: Empty the scrap tub

**Goal:** every scrap piece is in the waste bin and the empty tub stands back on its mark, mouth up.

- With the **left gripper**, grasp the scrap tub's rim at the middle of the side nearest the back
  bench edge.
- Lift it straight up, keeping it level so nothing spills on the way.
- Carry it to the waste bin at the front left and hold it over the bin mouth.
- Rotate a quarter turn so the tub mouth faces down into the bin, and hold it there until nothing
  more falls out.
- Rotate the tub back level, still over the bin mouth.
- Carry it back to its outline, lower it inside mouth up, and release when it is stable.

**Check:** seen from above, the tub floor and inside walls are bare, and the tub stands inside its
outline with a thin band of tape showing all the way around it. If a piece is still stuck inside,
lift the tub with the **left gripper** and tip it over the waste bin once more. If a piece falls on
the bench, pick it up with the **left gripper** and drop it into the waste bin.

**Expected state:** the waste bin holds all the scrap. The tub stands empty on its mark.

### Step 4: Wipe the bench

**Goal:** the working area is wiped in overlapping lanes and the cloth is flat back on its mark.

- With the **right gripper**, grasp the cloth at its middle and lift it off its mark.
- Press it flat on the bench at the back left corner of the working area.
- Wipe one lane: keep the cloth pressed flat and pull it straight from the back of the working area
  to the front bench edge. Do not lift the cloth part way through a lane.
- At the end of the lane, lift the cloth clear of the bench, move it back to the start of the lane,
  step it to the right by about half the width of the cloth, and press it flat again.
- Wipe the next lane the same way. Each lane overlaps the lane before it.
- Keep wiping lanes until the lanes have crossed the working area from its left side to its right
  side.
- Wipe only the working area. Do not run the cloth over the mark strip, the two bins, the scrap tub,
  or the log board.
- Carry the cloth back to its outline with the **right gripper**, lay it flat inside, and release.

**Check:** the working area shows a damp trail from its left side to its right side with no dry gap
between lanes, and every lane reaches the front bench edge. If a dry gap shows, pick the cloth up
with the **right gripper**, wipe that gap as one more lane, and lay the cloth back on its mark.

**Expected state:** the working area is bare and wiped. The cloth is flat on its mark.

### Step 5: Sign the shift log

**Goal:** one stroke stands inside the sign-out box and the pen is back on its mark.

- With the **left gripper**, press the top edge of the log board flat against the bench. Hold it
  there for the whole step, so the board cannot slide while the pen is on it.
- With the **right gripper**, grasp the pen at the middle of its barrel. Do not grasp its tip and do
  not grasp its back end.
- Bring the tip down into the left end of the sign-out box until it touches the sheet.
- Draw one straight stroke from left to right across the box, staying inside the box, without
  lifting the tip.
- Lift the tip straight up, clear of the sheet.
- Carry the pen back to its outline with the **right gripper**, lay it inside, and release when it
  is stable.
- Release the log board with the **left gripper** only after the pen is on its mark.

**Check:** one stroke is visible inside the sign-out box and it does not cross the box edges. If the
tip left no visible line at all, draw the stroke once more in the same box. Do not draw a third
stroke, and do not draw over a stroke that is already visible.

**Expected state:** the log sheet carries one sign-out stroke. The pen is on its mark and the log
board is flat and unmoved at the front right.

### Step 6: End the episode

**Goal:** recording ends with the station cleared, restaged, emptied, wiped, and signed.

1. Confirm the end state:
   - the working area is bare, with no stray, supply item, scrap piece, or cloth left on it;
   - the parts tote, the fastener cup, and the tape roll each stand on their own mark, each showing
     a thin band of tape all the way around;
   - the scrap tub stands empty and mouth up on its mark;
   - the cloth lies flat on its mark and the pen lies on its mark;
   - the returns bin holds every stray and the waste bin holds all the scrap;
   - one stroke stands inside the sign-out box, and the log board is still flat at the front right.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Empty the returns bin and put the strays back where they are kept.
2. Empty the waste bin into the designated disposal container.
3. Put 4–8 scrap pieces back in the scrap tub and stand the tub on its mark.
4. Take the parts tote, the fastener cup, and the tape roll off their marks and stand them together
   in the start zone for the next episode's config — the left end of the working area (Config L), the
   front-center (Config M), or the right end (Config R) — each one clearly away from its own outline.
5. Scatter 3–6 strays across the working area, none of them inside a bin, inside the tub, or on the
   log board.
6. Put a fresh log sheet on the log board, with an empty sign-out box, and set the board flat at the
   front right.
7. Lay the pen on its mark.
8. Rinse the cloth, wring it out so it does not drip, fold it flat, and lay it on its mark. Replace
   the cloth if it is soiled or torn.
9. Check every taped outline. Re-tape any outline that is lifting, torn, or unreadable.
10. Inspect the totes, cup, roll, tub, bins, and log board for damage. Replace damaged items.
11. Run both Setup checklists again.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

- the **start timestamp** in the video;
- the **violation name** from the list below; and
- the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an
annotation label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain several violations; tag each
one separately. Retain the episode in training data with its violation tags. Do not delete a
recorded episode solely because it contains a violation.

### Violations

**Note on the start position:** the violations below were written for Config R (the supply items
start at the right end of the working area and the right gripper picks them itself). The pickup and
arm-role cues will be rewritten later to cover all three start positions; they are left as they are
for now. Until then, anything that does not match the episode's config goes under **Config
misaligned**.

**Violation: Config misaligned**

- **Visible cue:** what the operator does does not match the config on the table — the supply items
  are not in the start zone for the config; a gripper reaches across the bench for a supply item; in
  Config L or M the left gripper carries a supply item toward the mark strip itself, or the right
  gripper reaches to the left end or the front-center for one, instead of a hand-over above the
  middle of the working area; or the wrong IF line is followed.
- **SOP rule broken:** the start position, the same-side rule, and the hand-over rule (the left
  gripper takes each supply item from the start zone in Config L and M and hands it over to the right
  gripper above the middle of the working area; in Config R the right gripper takes it itself; no
  arm reaches across the bench; the IF line followed is the one for the config on the table).
- **Coaching note:** look where the supply items are before the first reach in Step 2, then follow
  that config's IF lines through Steps 2.1 to 2.3.

**Violation: Marked item binned as a stray**

- **Visible cue:** the left gripper drops the parts tote, the fastener cup, the tape roll, the scrap
  tub, the cloth, or the pen into the returns bin or the waste bin.
- **SOP rule broken:** Step 1, an item with an outline on the bench is a marked item and is never
  binned.
- **Coaching note:** look for the outline before picking. Outline means restage, no outline means
  bin.

**Violation: Stray left on the bench**

- **Visible cue:** the episode moves on to Step 2 while an item with no outline is still on the
  bench, or a stray is still visible in the working area at the end of the episode.
- **SOP rule broken:** Step 1 (repeat until no stray is left on the bench) and Step 6 (confirm the
  working area is bare).
- **Coaching note:** scan the whole bench, front to back, before starting the restage.

**Violation: More than one stray moved at once, or dragged**

- **Visible cue:** two or more strays are lifted or carried in one pick by the left gripper, or a
  stray is pushed or slid across the bench instead of being lifted clear.
- **SOP rule broken:** Step 1 (work one stray at a time, and lift it clear of the bench before
  carrying it).
- **Coaching note:** one stray per pick, and lift it off the bench before the carry.

**Violation: Stray put in the wrong place**

- **Visible cue:** a stray goes into the waste bin instead of the returns bin, is thrown, is released
  where it misses the bin mouth, is carried over the scrap tub, the log board, or the mark strip, or
  is left on the bench after a miss.
- **SOP rule broken:** Step 1 (carry each stray clear of the other areas, center it over the returns
  bin mouth, release it inside, and re-bin any miss once).
- **Coaching note:** strays go in the returns bin only, centered over the mouth, released not thrown.

**Violation: Wrong phase order**

- **Visible cue:** supplies are restaged before the strays are cleared, the scrap tub is emptied
  before the supplies are on their marks, the bench is wiped before the scrap tub is emptied, or the
  log is signed before the wipe is finished.
- **SOP rule broken:** Steps 1 to 5 (work the five phases in the fixed order: clear, restage, empty
  scrap, wipe, sign).
- **Coaching note:** finish each phase and its check before starting the next one.

**Violation: Supplies restaged out of order**

- **Visible cue:** the fastener cup or the tape roll is placed on its mark before the parts tote, or
  the tape roll is placed before the fastener cup.
- **SOP rule broken:** Step 2, restage in the fixed order: parts tote, then fastener cup, then tape
  roll.
- **Coaching note:** tote, cup, roll, every time, whichever one is nearest.

**Violation: Item not on its mark**

- **Visible cue:** at the end of a step or at the end of the episode, the parts tote, the fastener
  cup, the tape roll, the scrap tub, the cloth, or the pen sits outside its outline, covers its
  tape, crosses its tape, or sits on the wrong outline.
- **SOP rule broken:** Steps 2, 3, 4 and 5 (each item ends inside its own outline with a thin band
  of tape showing all the way around it).
- **Coaching note:** check for the tape band on all four sides before releasing.

**Violation: Supply not squared to the front edge**

- **Visible cue:** the parts tote is released with its long side visibly skewed to the front bench
  edge, or the fastener cup is released tilted rather than upright, or the tape roll is released
  standing on edge rather than flat.
- **SOP rule broken:** Step 2 (turn the tote square to the front bench edge, set the cup down
  upright, and lay the roll flat).
- **Coaching note:** set the angle before lowering, not after.

**Violation: Supply carried tilted or spilled**

- **Visible cue:** the parts tote tips during the carry, parts fall out of it onto the bench, or
  spilled parts are left where they fall.
- **SOP rule broken:** Step 2.1 (keep the tote level for the whole carry so nothing tips out of it).
- **Coaching note:** grip the front rim, lift straight up, and keep the tote level all the way to
  the mark.

**Violation: Wrong grip point**

- **Visible cue:** the tote is grasped anywhere but the middle of its front rim, the cup is grasped
  by its rim or from inside, the gripper goes through the hole in the tape roll, the scrap tub is
  grasped anywhere but its back rim, the cloth is grasped by a corner rather than its middle, or the
  pen is grasped at its tip or its back end.
- **SOP rule broken:** Steps 2, 3, 4 and 5, each item is grasped at the point its step names.
- **Coaching note:** the named grip point is what makes the lift repeatable; do not improvise a grip.

**Violation: Scrap emptied wrong or spilled**

- **Visible cue:** the scrap tub is tipped, poured, or dumped somewhere other than over the waste bin
  mouth, scrap is thrown from the tub, scrap falls on the bench, or spilled scrap is left on the
  bench.
- **SOP rule broken:** Step 3 (carry the tub to the waste bin, hold it over the mouth, rotate a
  quarter turn to tip it, and pick up any piece that falls on the bench).
- **Coaching note:** the tub only turns over once it is above the bin mouth, and any spill gets
  picked up.

**Violation: Scrap tub left with scrap in it**

- **Visible cue:** pieces are still visible on the tub floor or against its inside walls when the tub
  is set back on its mark.
- **SOP rule broken:** Step 3, the tub floor and inside walls are bare before the tub goes back on
  its mark.
- **Coaching note:** look into the tub from above before carrying it back, and tip once more if a
  piece is stuck.

**Violation: Scrap tub returned mouth down**

- **Visible cue:** the scrap tub is set on its mark upside down, on its side, or is not carried back
  to its mark at all.
- **SOP rule broken:** Step 3 (rotate the tub back level over the bin, then set it inside its
  outline mouth up).
- **Coaching note:** level it over the bin first, then carry, then set it down mouth up.

**Violation: Wipe pattern wrong**

- **Visible cue:** the cloth is moved in circles or side to side, a lane runs front to back instead
  of back to front, the cloth lifts off the bench part way through a lane, or a lane is laid down
  with no overlap onto the lane before it.
- **SOP rule broken:** Step 4 (wipe straight lanes from the back of the working area to the front
  bench edge, without lifting mid-lane, each lane overlapping the one before).
- **Coaching note:** flat, straight, back to front, and step right by half a cloth between lanes.

**Violation: Working area not fully wiped**

- **Visible cue:** a dry gap shows between lanes, a lane stops short of the front bench edge, or the
  lanes do not reach the left or the right side of the working area.
- **SOP rule broken:** Step 4 (keep wiping lanes until they cross the working area from side to
  side, each lane reaching the front bench edge).
- **Coaching note:** run every lane all the way to the front edge, then look for dry gaps before
  putting the cloth down.

**Violation: Wiped over fixtures or marks**

- **Visible cue:** the cloth is run over the mark strip, the returns bin, the waste bin, the scrap
  tub, or the log board, or a wipe pushes one of them out of place.
- **SOP rule broken:** Step 4, wipe only the working area.
- **Coaching note:** the lanes stop at the mark strip, at the bins, and at the log board.

**Violation: Log board not held**

- **Visible cue:** the left gripper is off the log board while the pen is on the sheet, the board
  slides or lifts during the stroke, or the left gripper leaves the board before the pen is back on
  its mark.
- **SOP rule broken:** Step 5 (press the top edge of the log board flat with the left gripper and
  hold it there until the pen is on its mark).
- **Coaching note:** the left gripper lands on the board before the pen is picked up and leaves it
  last.

**Violation: Sign-out stroke wrong**

- **Visible cue:** the stroke runs outside the sign-out box or crosses its edges, the tip lifts part
  way through the stroke, more than one stroke is drawn in the box, or a visible stroke is drawn
  over a second time.
- **SOP rule broken:** Step 5 (draw one straight stroke left to right inside the box without lifting
  the tip, and redraw only if no line is visible at all).
- **Coaching note:** one stroke, inside the box, tip down the whole way.

**Violation: Wrong arm used**

- **Visible cue:** a stray or the scrap tub is handled by the right gripper, a supply item, the
  cloth, or the pen is handled by the left gripper, or an item is passed from one gripper to the
  other part way through a carry.
- **SOP rule broken:** Steps 1 to 5, each action is done by the gripper its step names.
- **Coaching note:** left gripper for strays and scrap, right gripper for supplies, cloth, and pen,
  and nothing changes hands mid-carry.

**Violation: Item dropped or knocked over**

- **Visible cue:** an item falls from a gripper onto the bench or the floor, a bin or the scrap tub
  is knocked over, or an arm sweeps an item off its mark while moving.
- **SOP rule broken:** Steps 1 to 5 (lift each item clear, carry it on the path its step names, and
  release it only when it is stable).
- **Coaching note:** lift higher over the bins and the mark strip, and slow the carry near a
  fixture.

**Violation: Finished item disturbed later**

- **Visible cue:** an item that was already on its mark is bumped, slid, or knocked off its outline
  during a later step, for example a supply item moved during the wipe, or the scrap tub pushed off
  its mark while the log is signed.
- **SOP rule broken:** Steps 2 to 6, an item that is on its mark stays on its mark for the rest of
  the episode.
- **Coaching note:** route the arms around the filled marks once a phase is done.

**Violation: Check skipped**

- **Visible cue:** an arm moves straight on to the next step with no look at the step's end state:
  no scan of the bench after the strays, no look at the tape bands after the restage, no look into
  the tub after tipping it, or no look across the lanes after the wipe.
- **SOP rule broken:** Steps 1 to 5, each step's check is done before the next step starts.
- **Coaching note:** every step ends with a look, and the fix happens in that step, not later.

**Violation: Wrong episode ending**

- **Visible cue:** the episode ends with a stray on the bench, an item off its mark, scrap in the
  tub, the working area unwiped, or the sign-out box empty; or the arms are away from home, the
  grippers are closed, or an arm makes a correction after homing.
- **SOP rule broken:** Step 6 (confirm the end state, return both arms home with grippers open, then
  stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures that are not caused by how the task was run do not go in the violation set. Log them as
system issues, discard the episode, and do not use them for coaching.

- **Recording stopped or paused during the episode** (recording system).
- **Camera dropped frames or lost feed** (capture system).
- **Hardware fault on an arm:** gripper failure, drift, collision caused by controller error, or
  motor error.
- **Defective item:** a cracked tote or tub, a bin that tips on its own, a taped outline that lifts
  off the bench during the episode, or a pen that leaves no mark at all. Replace before the next
  episode.

## Annotation subtasks (from SOP)

1. Move one stray into the returns bin
2. Hand one supply item over to the right gripper (Config L and M)
3. Place the parts tote on its mark
4. Place the fastener cup on its mark
5. Place the tape roll on its mark
6. Empty the scrap tub into the waste bin
7. Return the scrap tub to its mark
8. Wipe one lane of the working area
9. Return the cloth to its mark
10. Hold the log board steady
11. Draw the sign-out stroke
12. Return the pen to its mark
13. Return both arms home and end the episode
