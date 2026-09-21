# Gift Wrap a Box SOP (1x Episode: 1 Box)

One episode wraps **one** closed rectangular box. The box is carried from the input pile onto a paper
sheet in the working area, the paper is cut to size, the body seam is closed and taped, both ends are
folded and taped, every edge is creased, one ribbon is tied into a bow, one gift tag is attached, and
the finished box is set down in the output zone.

The order never changes: cut the paper, close the body seam, close the near end, close the far end,
crease every edge, tie the bow, attach the tag, then place the box. Nothing is folded before the paper
is cut, and no tape touches the box before the body seam is made.

The left gripper owns the box and the paper. It carries the box, lays the sheet out, holds the paper
flat for the cut, holds the box steady, and makes the folds that need a flat hold. The right gripper
owns the tools. It works the scissors, the tape, the crease pass, the ribbon, the tag, and the carry to
the output zone. In Config R the box comes in from the right and goes out to the left, so those two
carries change hands; nothing else does.

Exactly one box, one paper sheet, one ribbon length, and one gift tag are handled per episode. The
paper always goes down print side down and the box always goes on it top face down, so the finished
box shows the print on all six faces and the body seam ends up on the bottom face.

The table is set up in one of three ways. Only the box pile moves; the paper sheet, the working area,
the tool rest, and the ribbon and tag station are in the same place in all three. In Config R the box
pile takes the back right, so the output zone moves to the back left.

* **Config L:** the box pile is at the back left; the output zone is at the back right.
* **Config M:** the box pile is at the front center, in front of the working area; the output zone is
  at the back right.
* **Config R:** the box pile is at the back right; the output zone is at the back left.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line
that matches.

What stays constant across all sessions:

* **Start position:** the box pile starts at the back left (**Config L**), the front center
  (**Config M**), or the back right (**Config R**). One config per episode, chosen before recording and
  never changed mid-episode.
* **Same-side rule:** the gripper on the box pile's side takes the box — the left gripper in Config L
  and M, the right gripper in Config R — and the gripper on the output zone's side carries the finished
  box out. No arm reaches across the table.
* **Fixed roles:** the left gripper always lays out and holds the paper; the right gripper always works
  the scissors, the tape, the ribbon, and the tag. The paper sheet, the tool rest, and the ribbon and
  tag station never move.

## Setup

Complete both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the box pile in the start zone for this episode's
   config, the paper sheet at the front left, the working area at the center, the tape dispenser and
   the scissors at the right edge, the ribbon spool and the tag stack at the front right, and the
   output zone at the back right (Config L and M) or the back left (Config R).
3. The working area is visible from above, so the cut line, the body seam, and both end faces can be
   seen.
4. Both arms are at home with grippers open.
5. The table is clean, dry, and bare apart from the boxes, the paper sheet, the tape dispenser, the
   scissors, the ribbon spool, and the tag stack.
6. The left arm reaches the paper sheet, the working area, (Config L and M) the box pile, and (Config R)
   the output zone at the back left. The right arm reaches the working area, the tape dispenser, the
   scissors, the ribbon spool, the tag stack, (Config L and M) the output zone at the back right, and
   (Config R) the box pile at the back right.

### Materials checklist

1. One or more **boxes** sit in the start zone for this episode's config, and the other two zones are
   empty. Each one is closed, empty, and sound: no crushed corner, no warp, no open flap.
   * **Config L:** back left
   * **Config M:** front center, in front of the working area, clear of the paper sheet
   * **Config R:** back right, where the output zone normally is
2. One **paper sheet** lies at the front left, **print side down**, flat and uncreased. It is long
   enough to wrap all the way around the body of the box with a **clear overlap** to spare, and wide
   enough to pass each **end face** by a bit more than half the height of the box.
3. One **tape dispenser** sits at the right edge, loaded, with the tape end free and its handle toward
   the front edge.
4. One pair of **scissors** lies at the right edge beside the tape dispenser, blades closed and handle
   toward the front edge, sharp enough to part the paper in one pass.
5. One **ribbon spool** stands at the front right, running freely, holding enough ribbon for the box
   with plenty to spare.
6. One **tag stack** sits at the front right beside the ribbon spool, tags writing side up.
7. The working area at the center is clear.
8. The output zone — the back right in Config L and M, the back left in Config R — is clear, or holds
   finished boxes from earlier episodes in one row.

### Workspace layout

* **Box pile:** the bare boxes waiting to be wrapped — back left (**Config L**), front center
  (**Config M**), or back right (**Config R**).
* **Paper sheet:** front left, lying print side down.
* **Working area:** center, where the cutting, wrapping, taping, creasing, and tying happen.
* **Tool rest:** right edge, the tape dispenser and the scissors.
* **Ribbon and tag station:** front right, the ribbon spool and the tag stack.
* **Output zone:** the finished boxes in one row — back right (**Config L** and **M**), back left
  (**Config R**).

Everything the left arm handles is staged on the left. Everything the right arm handles is staged on
the right. Neither arm reaches across to the other side for a supply.

### Arm assignments

* **Left gripper:** carries the box from the box pile (Config L and M), lays out the paper sheet, holds
  the paper flat and taut for the cut, brings the far long edge over for the body seam, presses the top
  panel down at each end, folds the end flap up, holds the box down for the crease pass, and (Config R)
  carries the finished box to the output zone at the back left.
* **Right gripper:** works the scissors, brings the near long edge over, applies every strip of tape,
  folds the side panels in, runs the crease pass, draws and cuts the ribbon, forms the bow, attaches
  the gift tag, carries the finished box to the output zone (Config L and M), and (Config R) carries
  the box from the box pile at the back right.

## Vocabulary

* **Box:** one closed rectangular box, wrapped whole in a single episode.
* **Start zone:** where the box pile stands at the start of the episode — back left (**Config L**),
  front center (**Config M**), or back right (**Config R**). One per episode, chosen before recording
  and never changed mid-episode.
* **Output side:** the back corner holding the output zone — the right in Config L and M, the left in
  Config R. The gripper on that side carries the finished box out.
* **Top face:** the face that points up on the finished box. It carries the bow and the tag.
* **Bottom face:** the face opposite the top face. The body seam closes here, and it points up while
  the box is being wrapped.
* **End face:** one of the two small faces. The **near end** is the one toward the front edge, and the
  **far end** is the one away from it.
* **Long edge:** one of the four edges running the length of the box.
* **Box outline:** the shape of an end face seen straight on. No paper sticks out past it once an end
  is closed.
* **Paper sheet:** the rectangle of wrapping paper. Its **print side** is the patterned face, and it
  ends up facing out.
* **Near long edge:** the long edge of the paper nearest the front edge of the table. **Far long
  edge:** the long edge of the paper away from it.
* **Cut line:** where the scissors part the sheet, running square across it.
* **Offcut:** the paper left over on the far side of the cut line.
* **Clear overlap:** the far long edge lies over the near long edge by a band wide enough to see from
  above. A join where the two edges only meet, or leave a gap, is not a clear overlap.
* **Body seam:** the clear overlap where the two long edges close on the bottom face, with a narrow
  **hem** folded under along the leading edge so the seam runs straight.
* **End overhang:** the paper sticking out past an end face before it is folded. Its **top panel** is
  the part above the end face, its two **side panels** are the parts to the left and the right of it,
  and its **bottom panel** is the part below it.
* **Side triangle:** the diagonal fold that forms at each side of an end face when the top panel is
  pressed down. The two side triangles at one end look the same size.
* **End flap:** the bottom panel once it is folded up against the end face and taped. Its edge sits
  inside the box outline.
* **Crease:** a sharp folded line pressed flat along a box edge. A creased edge shows a line, not a
  rounded shoulder.
* **Crease pass:** one run of the closed right gripper along a box edge, pressing the paper into the
  edge, while the left gripper holds the box down.
* **Ribbon:** the length of ribbon drawn off the spool for one box.
* **Crossing point:** the middle of the top face, where the two ribbon runs cross.
* **Tail:** one of the two loose ribbon ends left below the bow.
* **Loop:** one of the two folded ribbon lengths that make the bow. Both loops are the same size, each
  about a third of the width of the top face.
* **Bow:** the finished two-loop knot, pulled tight and centered on the crossing point.
* **Gift tag:** one card attached at the bow, lying flat on the top face, writing side up.
* **Lift:** coming straight down onto the grasp point, closing, and raising straight up until there is
  daylight under the thing, before anything moves sideways.
* **Release point:** over the working area, over the tool rest, over the ribbon and tag station, or
  over the output zone. A gripper opens nowhere else.

## Steps

Steps 1 and 2 stage the box and cut the paper. Steps 3 to 5 close the paper around the box. Steps 6
and 7 finish it with the ribbon and the tag. Step 8 puts it in the output zone and Step 9 ends the
episode.

Two steps depend on where the box pile is: in Step 1 the **left gripper** takes the box in Config L and
M and the **right gripper** takes it in Config R, and in Step 8 the **right gripper** carries the
finished box out to the back right in Config L and M while the **left gripper** carries it out to the
back left in Config R. Every other line is the same in all three configs.

### Step 1: Bring the paper and one box to the working area

**Goal:** one box sits top face down on the paper sheet in the working area.

* The **left gripper** closes on the **paper sheet** at the front left, carries it to the working area,
  and lays it flat at the center, **print side down**.
* Look where the box pile is before reaching for the box.
* **IF the box pile is at the back left (Config L):** the **left gripper** closes on one **box** in the
  box pile, lifts it clear of the table, carries it forward and to the right to the working area, and
  sets it down on the paper sheet **top face down**, so the bottom face points up.
* **IF the box pile is at the front center (Config M):** the **left gripper** closes on one **box** in
  the box pile, lifts it clear of the table, carries it straight back to the working area, and sets it
  down on the paper sheet **top face down**, so the bottom face points up.
* **IF the box pile is at the back right (Config R):** the **right gripper** closes on one **box** in
  the box pile, lifts it clear of the table, carries it forward and to the left to the working area,
  and sets it down on the paper sheet **top face down**, so the bottom face points up.

Then, in all three:

* The gripper releases, leaving the box roughly in the middle of the sheet.

Take one box only. Never drag or slide a box across the table, and never lay the paper print side up.

**Expected state:** one box rests top face down on a flat sheet, print side against the table, with
paper showing on all four sides of the box.

### Step 2: Cut the paper to size

**Goal:** the paper is one rectangle that wraps the body of the box with a clear overlap and passes
each end face by a bit more than half the height of the box.

#### 2.1 Check the wrap length

* The **right gripper** rolls the box one full turn across the sheet: bottom face, side, top face,
  side.
* Note where the box lands. The **cut line** sits past that landing point by a **clear overlap**.
* The **right gripper** rolls the box back to its starting place.
* If the sheet ends before the landing point, the **left gripper** draws more paper out and 2.1 runs
  again.

#### 2.2 Check the end overhang

* Look along both ends of the box and confirm the paper passes each **end face** by a bit more than
  half the height of the box.
* If one end overhang is short, the **left gripper** slides the box along the sheet until both end
  overhangs look the same, then 2.1 runs again.

#### 2.3 Hold the paper and cut

* The **left gripper** presses the paper flat against the table and holds it taut on the cut line.
* The **right gripper** closes on the **scissors** on the tool rest and lifts them.
* The **right gripper** cuts across the sheet in one straight pass, square to the long edge of the
  sheet, from the far side to the near side.
* If the cut wanders off square, the **right gripper** trims it straight before anything is folded.

Cut in one pass. Never tear the paper, and never cut with the left gripper off the sheet.

#### 2.4 Clear the offcut and center the box

* The **right gripper** carries the **scissors** back to the tool rest, lays them down with the blades
  closed and the handle toward the front edge, and releases.
* The **right gripper** then carries the **offcut** clear of the working area and releases it.
* The **left gripper** slides the box on the cut sheet until it sits in the middle, top face down, with
  the two end overhangs looking the same.

**Check:** one cut rectangle lies flat under the box, the cut runs square across the sheet, both end
overhangs look the same, the offcut is off the working area, and the scissors are back on the tool
rest.

### Step 3: Fold and tape the body seam

**Goal:** the paper is closed around the body of the box with one taped **body seam** running along
the bottom face.

* The **right gripper** brings the **near long edge** of the paper up and over the box and holds it
  flat against the bottom face.
* The **left gripper** brings the **far long edge** up and over so it lies on the near long edge with a
  **clear overlap**.
* Fold a narrow **hem** under along the leading edge of the far long edge so the seam runs straight,
  and hold it down.
* The **right gripper** applies **one** strip of tape along the middle of the body seam and presses it
  flat.

One strip of tape closes the body seam. If the seam gaps, if the overlap is not clear, or if the hem
was not folded under, open it, draw the far long edge further over, fold the hem, and tape it again.

**Check:** the paper wraps the body all the way around, the body seam runs along the bottom face with
a clear overlap and a folded hem, one strip of tape lies flat along it, and no tape sits on any other
face.

### Step 4: Fold and tape the two ends

**Goal:** both end faces are closed with matching side triangles and one taped end flap each, and no
paper sticks out past the box outline.

#### 4.1 Close the near end

* The **left gripper** presses the **top panel** flat down against the **near end** face and holds it,
  so a **side triangle** forms at each side.
* The **right gripper** folds the left **side panel** flat against the end face, pressing the diagonal
  crease flat as it goes.
* The **right gripper** folds the right side panel the same way.
* If a side panel bunches, the **right gripper** opens it and folds it again flat before going on.
* The **left gripper** folds the **bottom panel** up against the end face so its edge sits inside the
  **box outline**, and holds it there.
* The **right gripper** applies **one** strip of tape across the edge of the **end flap** and presses
  it flat.

#### 4.2 Close the far end

* Both grippers turn the box a half turn in the working area: the **left gripper** steadies the box
  while the **right gripper** swings it round, so the far end now faces the front edge.
* Repeat 4.1 on that end face.

**Check:** both end faces are closed, each shows two side triangles that look the same size with sharp
diagonal creases, each end flap is taped flat with one strip and sits inside the box outline, and no
paper sticks out past either end.

### Step 5: Crease every edge

**Goal:** every box edge shows a sharp crease and the paper lies flat on all six faces.

* The **left gripper** holds the box down against the table.
* The **right gripper** runs one **crease pass** along each of the four **long edges** in turn.
* The **right gripper** then runs one crease pass along each of the four edges of the near end face,
  and along each of the four edges of the far end face.
* The **left gripper** steadies the box while the **right gripper** turns it so the body seam is down
  and the **top face** is up, then the **left gripper** sets it in the middle of the working area.

Crease every edge, not just the ones facing up. Turn the box with both grippers rather than dragging
it round on one.

**Check:** all twelve edges show a crease line rather than a rounded shoulder, the paper lies flat on
all six faces, the box sits top face up in the middle of the working area, and the body seam is out of
sight underneath.

### Step 6: Tie the ribbon bow

**Goal:** the ribbon runs across the box on both axes and ends in a bow centered on the crossing
point.

#### 6.1 Run the ribbon across the short axis

* The **right gripper** draws **ribbon** off the spool at the front right and passes it under the box
  along the short axis.
* Both grippers bring one end each up to the middle of the **top face** and cross them at the
  **crossing point**.

#### 6.2 Run the ribbon across the long axis

* Both grippers turn their own end a quarter turn and pass it under the box along the long axis.
* Both grippers bring their own end back up to the crossing point.
* Both grippers pull their own end apart until the ribbon lies flat against all six faces with no
  slack.

#### 6.3 Cut the ribbon and knot it

* The **right gripper** cuts the ribbon off the spool, leaving both **tails** the same length, each
  about as long as the box's long edge.
* The **right gripper** returns the spool to the front right and releases.
* The **right gripper** crosses its tail over the left gripper's tail at the crossing point and passes
  it under and through.
* Both grippers pull their own tail apart until the knot seats down on the crossing point.

#### 6.4 Form the bow

* Fold one **loop** with each tail, cross the two loops, and pass one through.
* Both grippers grasp one loop each and pull apart until the bow is tight and sits on the **crossing
  point**, with the two loops the same size.
* The **right gripper** trims the two tails to the same length.

Cut the ribbon once. If the bow lands off the crossing point, if a loop collapses, or if the two loops
come out different sizes, loosen the bow and tie it again. Never cut the ribbon a second time to fix a
bow.

**Check:** the ribbon runs across both axes and lies flat on all six faces, the bow is tight and
centered on the crossing point, both loops look the same size, and both tails are the same length and
do not reach the table.

### Step 7: Attach the gift tag

**Goal:** one gift tag is held at the bow and lies flat on the top face, writing side up.

* The **right gripper** picks one **gift tag** off the tag stack at the front right.
* Pass the tag string under the knot at the crossing point. If the tag has no string, the **right
  gripper** applies one small piece of tape to the back of the tag instead.
* Lay the tag flat on the **top face** beside the bow, **writing side up**, and press it down.

One tag per box. Never leave a tag resting loose on the box, and never lay it writing side down.

**Check:** exactly one tag is held by its string or by tape, lies flat on the top face beside the bow,
writing side up, and stays put when the gripper opens.

### Step 8: Move the wrapped box to the output zone

**Goal:** the wrapped box stands in the output zone.

* **IF Config L or M:** the **right gripper** closes on the wrapped box at the middle of its right side,
  clear of the ribbon and the bow, lifts it clear of the table, and carries it back and to the right
  into the **output zone** at the back right. **IF Config R:** the **left gripper** closes on the
  wrapped box at the middle of its left side, clear of the ribbon and the bow, lifts it clear of the
  table, and carries it back and to the left into the **output zone** at the back left.
* If a wrapped box is already there, set the new box beside it with a clear gap, lined up front to
  back and not touching.
* Lower it until it sits flat, then release.

Grip the box body only. Never close on the ribbon or the bow, never set a box on top of another box,
and never drag the finished box across the table.

**Check:** the wrapped box sits top face up in the output zone in one row with any earlier boxes, the
bow is still tight and centered, the tag is still flat, and no paper is torn.

### Step 9: Confirm the box and end the episode

* Confirm the box shows paper on all six faces with no bare box, every edge creased, the body seam and
  both end flaps taped and out of sight from above, one bow centered on the crossing point, one tag
  flat beside it, the box in the output zone, the scissors and the tape dispenser on the tool rest,
  the ribbon spool and the tag stack at the front right, and the working area clear.
* Return both arms home, clear of the working area and the output zone, then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

### Between episodes of a batch

1. Leave the finished box in the output zone and the remaining boxes in the start zone.
2. Lay a fresh paper sheet at the front left, print side down, flat and uncreased.
3. Clear the working area of paper scraps, tape ends, and ribbon offcuts.
4. Confirm the scissors and the tape dispenser are on the tool rest, blades closed and handles toward
   the front edge, and that the ribbon spool and the tag stack are at the front right.
5. Run the Setup checklists again before the next episode.

### At the end of a batch

1. Carry the wrapped boxes from the output zone to the working area.
2. Cut the ribbon off, take the tag off, peel every strip of tape off, and unwrap each box.
3. Throw away the used paper, the used ribbon, and the used tags.
4. Set the bare boxes back in the start zone for the next episode's config — back left (Config L),
   front center (Config M), or back right (Config R) — and leave the other back corner bare for the
   output zone.
5. Restock a fresh paper sheet at the front left, the ribbon spool and the tag stack at the front
   right, and the tape dispenser and the scissors at the right edge.
6. Wipe the table and confirm the surface is clean, dry, and bare apart from the boxes and the
   supplies in their zones.
7. Replace a box that is crushed, warped, or will not stay closed, and a sheet that is torn or creased.

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

**Note on the start position:** the violations below were written for Config L (the box pile at the
back left, the output zone at the back right). The pickup and arm-role cues will be rewritten later to
cover all three start positions; they are left as they are for now. Until then, anything that does not
match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the operator does does not match the config on the table — the box pile is not
  in the start zone for the config; the output zone is not in the back corner for the config; a gripper
  reaches across the table for the box or carries the finished box to the far corner; or the wrong IF
  line is followed.
* **SOP rule broken:** the start position and the same-side rule (the left gripper takes the box in
  Config L and M and the right gripper takes it in Config R; the gripper on the output side carries the
  finished box out; no arm reaches across the table; the IF line followed is the one for the config on
  the table).
* **Coaching note:** look where the box pile is before the first reach, then follow that config's IF
  lines through Steps 1 and 8.

**Violation: Wrong pickup**

* **Visible cue:** the box is taken from the working area, the right side, or the output zone instead
  of the box pile, more than one box is lifted in one grasp, the box is dragged or slid across the
  table instead of lifted and carried, or it is set down off the paper sheet.
* **SOP rule broken:** Step 1, the left gripper lifts one box out of the box pile and sets it down on
  the paper sheet in the working area.
* **Coaching note:** one box per episode, lifted clear of the table and carried, never dragged.

**Violation: Paper or box laid the wrong way up**

* **Visible cue:** the paper sheet is laid print side up, or the box is set down bottom face down so
  the top face is against the paper and the body seam would close on a face that shows.
* **SOP rule broken:** Step 1, the paper goes down print side down and the box goes on it top face
  down.
* **Coaching note:** check the pattern is against the table and the box is upside down before the first
  fold. Everything after that depends on it.

**Violation: Paper cut wrong**

* **Visible cue:** folding starts while the paper is still joined to the sheet, the wrap length or the
  end overhang check is skipped, the cut sheet is too short to give a clear overlap or to pass each end
  face by half the box height, it is so long that the overlap or the end panels bunch, the cut runs off
  square, the paper is torn instead of cut in one pass, or the left gripper is off the sheet during the
  cut.
* **SOP rule broken:** Steps 2.1 to 2.3, check the wrap length and both end overhangs, hold the paper
  flat and taut with the left gripper, and cut one rectangle in one straight pass square across the
  sheet.
* **Coaching note:** roll the box a full turn and look at both ends before the scissors move. Hold the
  sheet taut and cut once.

**Violation: Body seam wrong**

* **Visible cue:** at the end of Step 3 the two long edges gap or only meet with no clear overlap, the
  leading edge is taped down without a hem folded under, the seam closes on the top face or on a long
  side instead of the bottom face, more than one strip of tape is on the seam, or tape sits on a face
  that shows.
* **SOP rule broken:** Step 3, one clear overlap on the bottom face with the leading edge hemmed under
  and one strip of tape along the middle of it.
* **Coaching note:** far edge over near edge, fold the hem, then one strip. If one strip will not hold
  it, the fold is wrong. Open it and fold again.

**Violation: End not closed properly**

* **Visible cue:** at the end of Step 4 the two side triangles at one end are visibly different sizes,
  a diagonal crease is rounded rather than sharp, a side panel is bunched under the end flap, an end
  flap lifts away or is left untaped, paper sticks out past the box outline, more than one strip of
  tape is on an end flap, or the far end is left open after the near end is finished.
* **SOP rule broken:** Steps 4.1 and 4.2, press the top panel down, fold both side panels flat with
  sharp diagonal creases, fold the end flap up inside the box outline, tape it with one strip, then
  turn the box and do the same at the other end.
* **Coaching note:** top panel down first, then each side panel flat, then the flap up and one strip.
  Both ends get the same treatment.

**Violation: Edges not creased**

* **Visible cue:** at the end of Step 5 the paper stands off the box edges and the box looks rounded,
  the crease pass is skipped, or only the four long edges are creased and the end face edges are not.
* **SOP rule broken:** Step 5, the right gripper runs a crease pass along all four long edges and along
  the four edges of each end face while the left gripper holds the box down.
* **Coaching note:** hold the box with the left gripper and run every edge, ends included, before the
  ribbon.

**Violation: Ribbon run wrong**

* **Visible cue:** the ribbon runs around one axis only, so the box shows a single band and no crossing
  point, the two runs do not cross at the middle of the top face, or the ribbon lifts off a face and
  slides because the grippers never pulled it tight before the knot.
* **SOP rule broken:** Steps 6.1 and 6.2, run the ribbon across the short axis, then the long axis,
  crossing at the crossing point, and pull it flat against all six faces before knotting.
* **Coaching note:** both axes, crossed at the center, pulled tight. Slack ribbon slides as soon as the
  box moves.

**Violation: Bow wrong**

* **Visible cue:** the ribbon is finished with a knot and no loops, the bow sits off the crossing
  point, a loop collapses, the two loops are visibly different sizes, the tails are different lengths
  or hang onto the table, or the ribbon is cut a second time to fix the bow.
* **SOP rule broken:** Steps 6.3 and 6.4, cut the ribbon once leaving two equal tails, seat the knot on
  the crossing point, form two loops of the same size, and retie rather than recut.
* **Coaching note:** cut once. If the bow comes out wrong, loosen it and tie it again.

**Violation: Gift tag missing, loose, or wrong way up**

* **Visible cue:** no tag is on the box at the end of Step 7, more than one tag is attached, the tag
  rests on the box with no string and no tape holding it, or it lies writing side down.
* **SOP rule broken:** Step 7, one tag held by its string under the knot or by one piece of tape, lying
  flat on the top face beside the bow, writing side up.
* **Coaching note:** one tag, held, writing side up. Confirm it stays put before the gripper opens.

**Violation: Wrapping damaged in handling**

* **Visible cue:** a gripper closes on the ribbon or the bow while lifting or placing and the bow ends
  up flat or pulled out of shape, or the paper splits at a corner, an edge, or the body seam during
  folding, creasing, tying, or carrying and the episode carries on with the torn paper.
* **SOP rule broken:** Steps 3 to 8, grasp the box body only, at the middle of its right side clear of
  the ribbon and the bow, and finish with paper covering all six faces.
* **Coaching note:** ease off the grip at the corners and come in on the side face so the gripper stays
  clear of the ribbon.

**Violation: Wrapped box placed wrong**

* **Visible cue:** at Step 8 the wrapped box is moved with the left gripper, is not grasped at the
  middle of its right side, is left in the working area, is dragged to the output zone, lands well off
  the zone, is set on top of another box, or is set touching the box beside it or out of line with it.
* **SOP rule broken:** Step 8, the right gripper lifts the box by the middle of its right side and
  carries it into the output zone, beside any box already there with a clear gap, lined up front to
  back and never stacked.
* **Coaching note:** finished boxes go side by side in a row. Stacking crushes the bow underneath.

**Violation: Arms swapped roles**

* **Visible cue:** the right gripper carries a box from the box pile or lays out the paper sheet, or
  the left gripper works the scissors, applies tape, runs the crease pass, handles the ribbon or the
  tag, or carries the finished box to the output zone.
* **SOP rule broken:** Steps 1 to 8, the left gripper owns the box and the paper and the right gripper
  owns the tools, the ribbon, the tag, and the carry to the output zone.
* **Coaching note:** each arm stays on its own supplies. Nothing crosses to the other side of the table
  for a tool.

**Violation: Dropped, collided, or knocked something over**

* **Visible cue:** a box, the scissors, the tape dispenser, the ribbon spool, or a tag falls to the
  table or the floor short of its spot, the ribbon spool or the tag stack is struck and shifts or
  tips, the box is knocked off the paper sheet, or the two arms strike each other.
* **SOP rule broken:** Steps 1 to 8, keep each thing on a clear travel path and release only after a
  settled placement.
* **Coaching note:** check the path and the landing spot before you move.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with bare box showing on any face, an untaped seam or end flap, no
  bow or no tag, the wrapped box still in the working area, the scissors or the tape dispenser off the
  tool rest, the ribbon spool or the tag stack out of place, an offcut left in the working area, or an
  arm away from home.
* **SOP rule broken:** Step 9, confirm the wrapped box, the supplies, and the clear working area;
  return both arms home clear of the scene; then stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

These failures are not caused by how the task was run. Log them as system issues, discard the episode,
and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Defective box:** crushed, warped, or will not stay closed, so it cannot be wrapped cleanly.
  Replace it before the next episode.
* **Defective paper sheet:** it arrives torn, creased, or too small to wrap the box. Replace it before
  the next episode.
* **Tape or scissors fault:** the dispenser jams, the tape will not release from the roll or will not
  stick, or the scissors will not part the paper in one correct pass. Replace them before the next
  episode.
* **Ribbon or tag fault:** the spool snags or knots, the ribbon frays so it cannot hold a knot, or a
  tag string is broken. Replace them before the next episode.

## Annotation subtasks (from SOP)

1. Lay the paper sheet out and set one box on it top face down
2. Cut the paper to size and clear the offcut
3. Fold and tape the body seam on the bottom face
4. Fold and tape the near end face
5. Fold and tape the far end face
6. Crease all twelve box edges
7. Run the ribbon across both axes and knot it at the crossing point
8. Form the bow and trim the tails
9. Attach the gift tag at the bow
10. Move the wrapped box to the output zone
11. Confirm the box and end the episode
