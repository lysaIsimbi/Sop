# Sort and Flatten Dunnage SOP (1x Episode: 2 Cartons)

One episode puts away all the loose dunnage on the table into three piles on the bare table and two cartons
into one flat stack on the bare table. The loose pieces, paper and bubble in no set number and two foam
pieces, lie loose on the table at one of three start positions when recording starts. The two cartons stand
square and open at both ends on the table at the back of the right half, just right of the middle. The **left
gripper** does all the loose work, one piece at a time, in a fixed order: every paper piece onto the **paper
pile** in the front-left corner, then every bubble piece onto the **bubble pile** just right of it along the
front edge, then the two foam pieces into one aligned **foam pile** behind the paper pile. Then the **right
gripper** brings the **right carton** to the **work zone** in the middle. There the right gripper folds its
flaps outward while the left gripper holds it by one flap and folds that flap out, the right gripper pushes
the carton down along a side wall to collapse it toward the table while the left gripper anchors it, and the
right gripper takes the flat carton off the table while the left gripper anchors it and lays it on the **bale
stage** in the back-right corner. The same is done with the **left carton**, except that the **left gripper**
brings it from the back to the work zone; the flat carton goes on top of the first. The start zone is bare,
the work zone is bare, the three piles stand in the front-left, and the two flat cartons lie in one stack in
the back-right corner when the episode ends.

The table is set up in one of three ways. Only the loose pieces move; the piles, the work zone, the cartons,
and the bale stage are in the same place in all three.

* **Config L:** the paper and bubble pieces are at the back-left. The two foam pieces are already on the
  left side, near or at the foam pile place behind the paper pile: lying separately, stacked but misaligned,
  or already stacked correctly.
* **Config M:** the loose pieces, foam included, are at the front-centre, in front of the work zone.
* **Config R:** the loose pieces, foam included, are at the front-right.

Where a step depends on the setup it says so on an **IF** line: look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the loose pieces start at the back-left (**Config L**), the front-centre
  (**Config M**) or the front-right (**Config R**). One config per episode, chosen before recording and never
  changed mid-episode.
* **Pile side:** the three piles are always in the front-left corner, and the **left gripper** sets every
  loose piece down on its pile.
* **Carton side:** the two cartons and the bale stage are always on the right. The **right gripper** brings
  the right carton to the work zone and the **left gripper** brings the left carton. The **right gripper**
  folds, collapses, and stacks every carton while the left gripper holds and anchors it.
* **Same-side rule:** the gripper on the loose pieces' side takes each piece: the left gripper in Config L
  and M, the right gripper in Config R. No arm reaches across the table.
* **Hand-over rule:** in Config R the loose pieces are too far for the left gripper, so the right gripper
  **hands each piece over**
  to the left gripper above the work zone: the right gripper holds the piece still, the left gripper closes on
  the opposite side of it, and only then does the right gripper open. The left gripper carries it on to the
  pile. Nothing is handed over in Config L or M.
* **Order:** paper, then bubble, then foam, then the right carton, then the left carton. No carton is
  touched while a loose piece still lies in the start zone. Nothing is ever taken back off a pile or off the
  stack.
* **Pile places:** the **paper pile** one gripper's width in from the front edge and from the left edge, the
  **bubble pile** the same distance from the front edge and one gripper's width to the right of the paper
  pile, and the **foam pile** the same distance from the left edge and one gripper's width behind the paper
  pile. The first piece of paper and of bubble founds its pile and every later piece of that material goes on
  top of it. The two foam pieces are stacked flush on each other and the pile is aligned to the left edge.
* **Bale stage:** the back-right corner, one gripper's width in from the back edge and from the right edge,
  where the first flat carton is laid and the second is laid on top of it.
* **Work zone:** every carton is stood, has its flaps folded out, and is collapsed in the middle of the
  table, straight on the table, before it goes to the bale stage. In Config R every loose piece changes hands
  above it; loose pieces never stop on it.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table with all four edges and all four corners in frame, so all
   three start zones are visible: every loose piece in the start zone for this episode's config, the bare
   front-left corner where the three piles will go, the bare work zone in the middle, the two cartons at the
   back of the right half, and the bare back-right corner where the cartons will be stacked.
3. Both arms are at home with grippers open.
4. The table is bare apart from the loose pieces, the two cartons, and robot hardware. The front-left
   quarter, the work zone, and the back-right corner hold nothing.
5. The left arm reaches the whole front-left quarter, the whole work zone, and (Config L and M) every loose
   piece in the start zone without stretching or leaning out. The left arm also reaches the left carton
   where it stands at the back, just right of the middle. The right arm reaches the right carton, the whole
   work zone, the back-right corner, and (Config R) every loose piece at the front-right without stretching
   or leaning out.
6. The table is bare and level between the start zone, the work zone, and the front-left corner, and between
   the cartons, the work zone, and the back-right corner.

### Materials checklist

1. The **loose pieces** lie loose on the bare table in the start zone for this episode's config, in one
   layer, none stacked, none overlapping, and none touching another, and the other two start zones are bare.
   The only exception is the foam in Config L, which starts near its pile place (item 6):
   * **Config L:** back-left, just left of the middle
   * **Config M:** front-centre, in front of the work zone, clear of the pile places
   * **Config R:** front-right, clear of the cartons and the bale stage
2. The loose pieces are a mix of **paper**, **bubble**, and **foam**: at least one paper piece and one bubble
   piece, their number not fixed and free to change from episode to episode, and exactly **two foam pieces**.
3. Every piece is clean, dry, and free of tape, staples, and stuck-on labels.
4. Every **paper** piece is loose kraft paper crumpled into a wad the gripper can close across, that stays in
   a wad when it is set down.
5. Every **bubble** piece is a bubble wrap sheet with its bubbles whole, none already popped flat, small
   enough that the whole bubble pile lying in the front-left corner does not reach the paper pile or the foam
   pile.
6. There are exactly two **foam** pieces. They are foam sheets or foam corner blocks of the same size, firm
   enough to hold their shape and soft enough to dent under a hard squeeze. Each piece has at least one
   graspable edge. Their starting condition depends on the config:
   * **Config L:** the two foam pieces are already on the left side, near or at the foam pile position
     behind the paper pile. They may be lying separately, stacked but misaligned, or already stacked
     correctly.
   * **Config M:** the two foam pieces start separately in the front-centre start zone with the other loose
     pieces.
   * **Config R:** the two foam pieces start separately in the front-right start zone with the other loose
     pieces.

   The finished foam pile must fit behind the paper pile without touching it.
7. The front-left quarter of the table is bare. The three finished piles fit there with a clear gripper's
   width between any two piles and between every pile and the table edges.
8. **Two cartons**, empty shipping boxes, stand square and side by side on the bare table at the back of
   the right half, just right of the middle, a gripper's width apart, **open at both ends**: tape already
   cut, all eight flaps open and pointing out at the top and at the bottom, and the four upright **creases**
   still sharp. The one further right is the **right carton**; the one nearer the middle is the **left
   carton**.
9. Each carton's flaps turn outward along their hinge creases and stay out, and the carton then collapses
   flat by hand along its four upright creases with one push down a side wall and stays flat on its own.
10. The back-right corner of the table is bare. A flat carton laid there one gripper's width in from the
    back edge and from the right edge lies fully on the table, a clear gripper's width from the right carton,
    and reaches neither the work zone nor the front-right.
11. Before collection, confirm by hand that:
    - each loose piece lifts off the table without bringing a neighbour with it;
    - all the paper and all the bubble each pile in their place without the pile sliding, tipping, or
      touching the next pile, and the two foam pieces stack flush behind the paper pile;
    - each carton can be taken by its top edge and stood in the work zone without folding on the way,
      lifted clear if it lifts cleanly or slid level across the bare table if it is too big to lift;
    - each carton, with all its flaps turned out, collapses along its four upright creases under one push
      down a side wall without sliding across the table;
    - a collapsed carton lies flat in the work zone on its own, touching nothing;
    - the second flat carton lies on top of the first on the bale stage without sliding off.

### Workspace layout

* **Start zone:** the loose pieces (input): back-left (**Config L**), front-centre (**Config M**), or
  front-right (**Config R**). One per episode. The zone is bare when the episode ends, and nothing is ever put
  back there.
* **Paper pile:** the front-left corner, one gripper's width in from the front edge and from the left edge.
* **Bubble pile:** the same distance from the front edge, one gripper's width to the right of the paper pile.
* **Foam pile:** the same distance from the left edge, one gripper's width behind the paper pile.
* **Work zone:** the bare stretch of tabletop in the middle, reached by both arms. Every carton is stood here,
  has its flaps folded out here, and is collapsed here, straight on the table. It holds one carton at a time and
  it is bare at the start and at the end. In Config R every loose piece is handed over above it; loose pieces
  never stop on it.
* **Cartons:** the bare table at the back of the right half, just right of the middle, where the two cartons
  stand side by side at the start. The area is bare when the episode ends.
* **Bale stage:** the back-right corner, one gripper's width in from the back edge and from the right edge.
  The first flat carton is laid here with its long edge along the back edge of the table, and the second is
  laid on top of it.
* The left arm's zones are the three piles, the work zone, the left carton's place at the back, and
  (Config L and M) the start zone. The right arm's zones are the right carton's place at the back, the work
  zone, the bale stage, and (Config R) the start zone. Only the work zone is shared.

### Arm assignments

* **Left gripper:** sets every loose piece down on its pile, taken straight from the start zone in Config L
  and M, received from the right gripper above the work zone in Config R; stacks and aligns the two foam
  pieces; takes the left carton from the back and stands it in the work zone; holds each carton steady in
  the work zone by one flap, folds that flap out while the right gripper folds the others, anchors it while
  the right gripper collapses
  it, and anchors the flat carton while the right gripper takes its grip.
* **Right gripper:** in Config R, takes each loose piece from the front-right and hands it over to the left
  gripper above the work zone; takes the right carton from the back of the right half and stands it in the
  work zone; for each carton, folds outward every flap except the one the left gripper holds, pushes it
  down along a side wall to collapse it along
  its creases, takes the flat carton, and lays it on the bale stage.

## Vocabulary

* **Dunnage:** the loose packing material that comes out of an opened carton: paper, bubble wrap, and foam.
* **Piece:** one item to be put away. One episode puts away every loose piece on the table and two cartons.
* **Loose piece:** any paper, bubble, or foam piece, that is, a piece that goes on a pile.
* **Start zone:** where the loose pieces lie at the start of the episode: back-left (**Config L**),
  front-centre (**Config M**), or front-right (**Config R**). One per episode, chosen before recording and
  never changed mid-episode.
* **Paper:** a crumpled wad of kraft paper. It goes on the paper pile.
* **Bubble:** a sheet of bubble wrap. It goes on the bubble pile.
* **Foam:** a foam sheet or foam corner block. There are two; they make the foam pile.
* **Base piece:** the foam piece that lies on the table behind the paper pile. The **top piece** is the one
  stacked on it.
* **Graspable edge:** a narrow edge of a foam piece the gripper can close across without clamping its wide
  face.
* **Pile:** the pieces of one material set down on top of each other in their place in the front-left. The
  first piece founds the pile; each later piece goes on top. A pile holds every piece of its material.
* **Gripper's width:** the width of the open gripper, used to place the piles and the bale stage: one in from
  each table edge, one between any two piles.
* **Set down:** the gripper lowers the piece until it rests on the table or on the pile, and opens only then.
  Nothing is ever released in the air.
* **Hand over:** the right gripper holds a loose piece still above the work zone, the left gripper closes on
  the opposite side of the piece, and only then does the right gripper open and lift clear. Config R only,
  because the loose pieces are too far for the left gripper.
* **Anchor:** the left gripper closed on the carton, or pressing it down onto the table, and held still so
  the carton cannot slide, spin, or lift while the right gripper works on it.
* **Carton:** an empty shipping box, standing square and open at both ends. A carton never goes on a pile.
  It is flattened and stacked on the bale stage.
* **Right carton:** the carton standing further to the right of the two, nearer the bale stage. It is done
  first, in Steps 4–7, and the right gripper brings it to the work zone.
* **Left carton:** the carton standing nearer the middle. It is done second, in Steps 8–11, and the left
  gripper brings it to the work zone.
* **Open at both ends:** a carton with all eight flaps open, four at each end, so the body is a square tube.
* **Flap:** one of the eight hinged panels at the ends of a carton, four at each end.
* **Flaps out:** every flap turned outward along its hinge crease, away from the opening, so nothing points
  into either end. A flap has to be out; it does not have to lie flat against the outside wall.
* **Both openings open:** all the flaps are out and both ends of the carton are unobstructed. Only then is
  the body collapsed.
* **Work zone:** the bare stretch of tabletop in the middle where every carton is stood, has its flaps folded
  out, and is collapsed straight on the table.
* **Crease:** one of the four upright fold lines already in a carton, at its four standing corners.
* **Along the creases:** the carton body folds only on those four upright lines, and nowhere else.
* **New crease:** any fold line pressed into the middle of a carton face. A carton with a new crease has been
  crushed, not flattened.
* **Collapsed:** the carton body pushed down along a side wall so it folds on its four existing creases and
  its two wide faces lie together, flat on the table, on its own.
* **Slide:** the gripper moves a carton level across the bare table without lifting it clear. Allowed for a
  carton too big to lift completely; never for a loose piece on its way to a pile.
* **Bale stage:** the place in the back-right corner where the flat cartons are stacked, one gripper's width
  in from the back edge and from the right edge.
* **Stack:** the two flat cartons lying on the bale stage, the second on top of the first with their edges
  lined up.
* **Work zone clear:** the work zone holds no carton and no debris.

## Steps

Steps 1–3 put all the loose pieces away, one material at a time. They depend on where the loose pieces are:
in Config L and M the **left gripper** takes each piece from the start zone; in Config R the **right
gripper** takes each piece from the front-right and **hands it over** to the left gripper above the work
zone. The left gripper sets every piece on its pile in all three. Steps 4–11 do the cartons and are the same
in all three configs: Steps 4–7 for the right carton, which the right gripper fetches, then Steps 8–11 for
the left carton, which the left gripper fetches. Then end the episode with Step 12.

### Step 1: Pile the paper

**Goal:** every paper piece stands in one pile in the front-left corner, and no paper is left in the start zone.

Look where the loose pieces are before reaching for the first one.

* **IF the loose pieces are at the back-left (Config L):** the **left gripper** takes the top or most
  reachable paper piece, closing anywhere on the wad, lifts it straight up, and carries it level, low
  over the table, straight forward to the front-left corner.
* **IF the loose pieces are at the front-centre (Config M):** the **left gripper** takes the top or most
  reachable paper piece, closing anywhere on the wad, lifts it straight up, and carries it level, low
  over the table, straight left along the front edge to the front-left corner.
* **IF the loose pieces are at the front-right (Config R):** the **right gripper** takes the top or most
  reachable paper piece, closing anywhere on the wad, lifts it straight up, carries it level to above the
  work zone, and holds it still. The **left gripper** closes on the other side of the wad; the **right
  gripper** opens and lifts clear. The left gripper carries it level, low over the table, to the front-left
  corner.

Then, in all three:

* Take one piece only. If a neighbour comes up with it, lower both back onto the table in the start zone and
  take one again. Never set a piece down on the way.
* For the first piece, bring it one gripper's width in from the front edge and from the left edge. **Set it
  down**: lower it until it rests on the table, then open the **left gripper** and lift straight up. This
  founds the **paper pile**.
* For every later piece, bring it directly over the pile, lower it until it rests on top, then open and lift
  straight up. Never release a piece in the air and never drop or toss it toward the pile.
* Take the next paper piece the same way until no paper is left in the start zone.

**Check:** every paper wad stands in one pile in the front-left corner, a gripper's width clear of both edges,
and the pile stands on its own with the gripper clear. If the pile has slid apart, or a piece lies beside it
rather than on it, put it right with the **left gripper**, either now or in Step 12. Once the **left
gripper** has opened over a pile, that piece stays on that pile. Never take a piece back off a pile.

**Expected state:** all the paper in one pile in the front-left corner, all the bubble pieces still in the
start zone, the foam pieces where they started, both cartons untouched, and both grippers clear.

### Step 2: Pile the bubble

**Goal:** every bubble sheet lies flat in one pile just right of the paper pile, and no bubble is left in the
start zone.

* **IF Config L or M:** with the **left gripper**, take the top or most reachable bubble piece by a corner of
  the sheet, never closed across its face. **IF Config R:** with the **right gripper**, take the top or most
  reachable bubble piece by a corner of the sheet, never closed across its face, and hand it over above the
  work zone. The **left gripper** closes on the corner diagonally opposite, then the right gripper opens.
* Take one piece only, lift it straight up, and carry it level, low over the table, straight to the front
  edge. Never set it down on the way.
* For the first sheet, bring it the same distance in from the front edge as the paper pile and one gripper's
  width to the right of it. Lower it until it lies flat on the table, then open the **left gripper** and lift
  straight up. This founds the **bubble pile**.
* For every later sheet, bring it directly over the pile, lower it until it lies flat on top, then open and
  lift straight up. Do not press the pile down after it is set.
* Take the next bubble piece the same way until no bubble is left in the start zone.

**Check:** every sheet lies flat in one pile just right of the paper pile, none folded under itself, none
touching the paper pile, and no bubbles were popped in the gripper.

**Expected state:** all the bubble in one pile beside the paper pile, both foam pieces where they started,
both cartons untouched, and both grippers clear.

### Step 3: Stack and align the foam pieces

**Goal:** both foam pieces form one neat, stable two-piece stack behind the paper pile. The pieces are flat
and aligned with each other, and the foam pile is one gripper's width behind the paper pile.

Before moving anything, look at the foam and determine its current condition.

**IF Config L: check and correct the foam**

In Config L the foam is already on the left side near its final pile position. Use the **left gripper**.
First check whether the foam pieces are already stacked and correctly aligned, stacked but off-centre or
tilted, or lying separately. Only correct what is necessary.

* **If already stacked and correctly positioned:** do not move the foam. Continue to the final alignment.
* **If stacked but misaligned:** grip a graspable edge of the top foam piece. Lift or shift it slightly and
  reposition it until its edges are flush with the bottom piece. Lower it flat and release. Do not clamp
  across the wide flat face of the foam.
* **If the pieces are lying separately:** check whether one piece is already in the correct foam pile
  position behind the paper pile.
  * If one piece is correctly positioned, leave it as the bottom piece. Pick up the other piece by a
    graspable edge, carry it level over the bottom piece, lower it flat on top, and release.
  * If neither piece is correctly positioned, take one piece by a graspable edge and place it flat in the
    foam pile area. Then place the second piece directly on top.

**IF Config M: build the foam stack**

Use the **left gripper**.

* Take one foam piece from the start zone by a graspable edge.
* Lift it straight up and carry it level, low over the table.
* Place it flat behind the paper pile: the same distance in from the left edge as the paper pile, and one
  gripper's width behind the paper pile.
* Lower it until it rests on the table, then release.
* Take the second foam piece by a graspable edge.
* Carry it level over the first piece, lower it flat and flush on top, then release.

**IF Config R: hand over and build the foam stack**

* Use the **right gripper** to take one foam piece from the start zone by a graspable edge.
* Lift it straight up and carry it level to above the work zone.
* Hold it still.
* The **left gripper** closes on the opposite graspable edge.
* Only after the left gripper has a secure grasp does the right gripper open and move clear.
* The **left gripper** carries the foam level and low over the table and places it flat behind the paper
  pile: the same distance in from the left edge as the paper pile, and one gripper's width behind the paper
  pile.
* Repeat the same hand-over for the second foam piece.
* The **left gripper** places the second piece directly on top of the first, lowers it flat and flush, and
  releases.

**Final alignment**

* If the stack is slightly out of position, use the **left gripper** to gently nudge it, or grasp it by a
  graspable edge, and move it into position.
* If the stack is already in position, do not touch it.

**Check:** both foam pieces form one stable two-piece stack behind the paper pile, flat and flush with each
other, one gripper's width behind the paper pile and not touching it, and no foam came out of the gripper
dented. The start zone holds nothing.

**Expected state:** the start zone bare, three piles standing in the front-left with a gripper's width
between them, both cartons still standing at the back of the right half, and both grippers clear.

### Step 4: Bring the right carton to the work zone

**Goal:** the right carton stands square and alone in the work zone.

* Do not start this step while any loose piece still lies in the start zone.

* With the **right gripper**, take the **right carton**, the one standing on the right of the two cartons
  at the back.
* Close on the top edge of one of its walls, next to an upright crease, so the body stays square in the
  gripper.
* Lift it straight up, clear of the left carton, and carry it level to the work zone. If the carton is too big
  to lift completely, **slide** it level across the bare table to the work zone instead, keeping it clear of
  the left carton.
* Stand it on the bare table in the middle the same way up it stood at the back, one open end up. Open the
  **right gripper** and lift clear.

**Check:** the right carton stands square and alone in the work zone, and the left carton remains undisturbed
in its position at the back.

**Expected state:** the right carton stands open in the work zone; the left carton remains at the back; both
grippers are clear.

### Step 5: Fold the right carton's flaps outward

**Goal:** all base flaps are folded outward and clear, leaving the carton stabilized and ready to be
collapsed.

* With the **left gripper**, hold the carton stable by gripping one of its flaps, keeping the carton firmly
  in place on the table.
* The **left gripper** folds outward the flap it has grabbed, turning it along its hinge crease while
  keeping hold of it so the carton stays steady.
* With the **right gripper**, fold the other flaps outward along their hinge creases, focusing primarily on
  the flaps at the base side. Work around the carton until all target flaps are turned fully out. A flap has to
  be out; it does not have to lie flat against the outside wall.

**Check:** all target flaps are flared outward away from the body, the carton remains upright on the table,
and both openings are unobstructed.

**Expected state:** the right carton stands upright in the work zone with its flaps folded out; both
grippers ready for collapsing.

### Step 6: Collapse the right carton toward the table

**Goal:** the right carton lies collapsed flat on the table, folded cleanly along existing creases with no
new creases formed.

* Once all flaps are folded outward, keep the carton anchored or stabilized as needed with the **left
  gripper**.
* With the **right gripper**, push the carton down along a side wall to collapse it toward the table,
  applying steady force while ensuring no new crease is created across the faces.
* If the carton slides instead of folding, lift the **right gripper** clear, re-square the carton with the
  **right gripper**, re-anchor with the **left gripper**, and push again with a shorter stroke.
* Open both grippers and lift clear.

**Check:** the carton lies flat on the table along its natural creases, no new crease runs across any face,
and flaps remain flared out. If it springs back open, anchor it again with the **left gripper** and push it
down again with the **right gripper**. If a crease tears through, leave the carton flat in the work zone,
log it for a station check, and proceed to Step 12.

**Expected state:** the right carton rests collapsed flat in the work zone; both grippers are clear.

### Step 7: Lift the right carton and lay it on the bale stage

**Goal:** the collapsed right carton lies on the bale stage in the back-right corner, and the work zone is
bare.

* With the **left gripper**, **anchor** the flat carton: press down on the rear folded edge to prevent
  sliding or springing open.
* With the **right gripper**, close on the front folded edge.
* Lift the **left gripper** clear, then lift the carton level off the table with the **right gripper**.
* Carry it level and low over the table to the back-right corner. If the carton is too big to lift
  completely, **slide** it level across the bare table instead. The left gripper remains in the work zone; it
  never goes to the bale stage.
* Lower the carton until it lies flat on the table, one gripper's width in from both the back edge and the
  right edge, with its long edge aligned along the back edge of the table. This founds the **bale stage**
  stack.
* Open the **right gripper** once the carton fully rests, then lift straight up. Never drop the carton onto
  the table.

**Check:** the right carton lies flat on the bale stage, square to the back edge, a gripper's width clear of
both edges. The work zone is bare. The left carton is still standing at the back. Once the **right gripper**
has opened over the bale stage, that carton stays there.

**Expected state:** the first carton rests on the bale stage, the work zone is bare, and the left carton
remains at the back.

### Step 8: Bring the left carton to the work zone

**Goal:** the left carton stands square and alone in the work zone.

* Do not start this step while the right carton, or debris from it, still lies in the work zone.

* With the **left gripper**, take the remaining **left carton** standing at the back. The right gripper
  stays clear; it does not go to the back for this carton.
* Close on the top edge of one of its walls, next to an upright crease, keeping the body square in the
  gripper.
* Lift it straight up and carry it level into the work zone. If the carton is too big to lift completely,
  **slide** it level across the bare table to the work zone instead.
* Stand it on the bare table in the middle the same way up it stood at the back, one open end up. Open the
  **left gripper** and lift clear.

**Check:** the left carton stands square and alone in the work zone; the carton area at the back is now
completely empty.

**Expected state:** the left carton stands open in the work zone; the bale stage holds the first carton; both
grippers are clear.

### Step 9: Fold the left carton's flaps outward

**Goal:** all base flaps are folded outward and clear, leaving the carton stabilized and ready to be
collapsed.

* With the **left gripper**, hold the carton stable by gripping one of its flaps, keeping the carton firmly
  in place on the table.
* The **left gripper** folds outward the flap it has grabbed, turning it along its hinge crease while
  keeping hold of it so the carton stays steady.
* With the **right gripper**, fold the other flaps outward along their hinge creases, focusing primarily on
  the flaps at the base side. Work around the carton until all target flaps are turned fully out.

**Check:** all target flaps are flared outward away from the body, the carton remains upright on the table,
and both openings are unobstructed.

**Expected state:** the left carton stands upright in the work zone with its flaps folded out; both grippers
ready for collapsing.

### Step 10: Collapse the left carton toward the table

**Goal:** the left carton lies collapsed flat on the table, folded cleanly along existing creases with no
new creases formed.

* Once all flaps are folded outward, keep the carton anchored or stabilized as needed with the **left
  gripper**.
* With the **right gripper**, push the carton down along a side wall to collapse it toward the table,
  applying steady force while ensuring no new crease is created across the faces.
* If the carton slides instead of folding, or springs back open, recover as in Step 6.
* Open both grippers and lift clear.

**Check:** the carton lies flat on the table along its natural creases, no new crease runs across any face,
and flaps remain flared out. If a crease tears through, leave the carton flat in the work zone, log it for a
station check, and proceed to Step 12.

**Expected state:** the left carton rests collapsed flat in the work zone; both grippers are clear.

### Step 11: Lift the left carton and stack it on the first carton

**Goal:** the flat left carton lies stacked directly on top of the first carton on the bale stage, and the
work zone is bare.

* With the **left gripper**, **anchor** the flat carton: press down onto the table along its rear folded edge
  so it cannot slide or spring open.
* With the **right gripper**, close firmly on the front folded edge.
* Lift the **left gripper** clear, then lift the carton level off the table with the **right gripper**.
* Carry it level, low over the table, toward the back-right corner. If the carton is too big to lift
  completely, **slide** it level across the bare table until it is beside the stack, then lift it onto the
  stack. The left gripper stays behind in the work zone.
* Position the carton directly over the first carton already resting on the bale stage, matching its
  orientation.
* Lower it straight down until it lies flat directly on top of the first carton, with all four edges aligned
  flush with the carton below.
* Open the **right gripper** only once the carton fully rests on the stack, then lift the gripper straight
  up. Never drop the carton onto the stack or leave it misaligned.

**Check:** both cartons form a neat, aligned two-layer stack on the bale stage. The work zone and the carton
area at the back are completely bare. Both grippers are clear.

**Expected state:** a two-carton stack rests on the bale stage, the work zone is bare, and no cartons remain
at the back.

### Step 12: End the episode

* Look over the piles and the stack. If a piece lies beside its pile, a pile has slid apart or touches its
  neighbour, or the two flat cartons are not lined up, **adjust** it now: with the **left gripper**, nudge or
  slide the loose piece onto its pile or the pile back into place; with the **right gripper**, slide the top
  carton until its edges line up with the one below. Adjusting keeps the piece on its pile or on the stack;
  it is never lifted back off.
* Confirm the start zone, the carton area at the back, and the work zone are bare, the three piles stand in
  the front-left corner with paper in the corner, bubble to its right, and foam behind, and both cartons lie
  flat in one stack in the back-right corner with their edges lined up.
* Return both arms home with grippers open.
* Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

### After each episode

1. Clear the three piles off the front-left of the table and the flat cartons off the back-right corner.
2. Replace both cartons with fresh square ones, tape already cut and all eight flaps open and pointing out.
   A carton that has been flattened once does not go back. Stand the two side by side at the back of the
   right half, just right of the middle, a gripper's width apart, a clear gripper's width from the bale stage.
3. Rebuild the loose set with at least one paper piece, at least one bubble piece, and exactly two foam
   pieces; the number of paper and bubble may differ from the last episode. Re-crumple each paper wad.
   Replace any bubble sheet whose bubbles were pressed flat.
4. Lay the loose pieces on the bare table in the start zone for the next episode's config, back-left
   (Config L), front-centre (Config M), or front-right (Config R), in one layer, none stacked, none
   overlapping, and none touching another, leaving the other two zones bare. In Config L the two foam
   pieces go on the left side instead, near or at the foam pile place: lying separately, stacked but
   misaligned, or stacked correctly, varied from episode to episode.
5. Wipe the work zone clean and dry.
6. Run both Setup checklists before the next episode.

### At the end of the session

1. Inspect the loose set. Replace any foam that stays dented, any bubble sheet that is mostly popped, and any
   paper wad that has gone limp and flat.
2. Wipe down the whole table.
3. Leave the front-left quarter bare, the work zone bare, the back-right corner bare, the loose set laid out
   in the start zone for the next session's config, and two fresh cartons standing at the back of the right
   half.

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

**Note on the start position:** the violations below were written for Config L (loose pieces start at the
back-left). The pickup and arm-role cues will be rewritten later to cover all three start positions; they are
left as they are for now. Until then, anything that does not match the episode's config goes under
**Config misaligned**.

**Violation: Config misaligned**
* **Visible cue:** what the operator does does not match the config on the table: the loose pieces are not
  in the start zone for the config; a gripper reaches across the table for a loose piece; in Config R the
  right gripper carries a loose piece to a pile itself, or the left gripper reaches to the front-right for
  one, instead of a hand-over above the work zone; or the wrong IF line is followed.
* **SOP rule broken:** the start position, the same-side rule, and the hand-over rule (the left gripper
  takes each piece from the start zone in Config L and M; in Config R the right gripper takes it and hands it
  over to the left gripper above the work zone; no arm reaches across the table; the IF line followed is the
  one for the config on the table).
* **Coaching note:** look where the loose pieces are before the first reach, then follow that config's IF
  lines through Steps 1–3.

**Violation: Work done out of order**
* **Visible cue:** the left gripper takes a bubble piece while paper still lies in the start zone, or a foam
  piece while bubble still lies there; the right gripper takes a carton while any loose piece still lies in
  the start zone; the left carton is taken before the right carton; or a carton is pushed down before all
  its flaps are turned out.
* **SOP rule broken:** Steps 1–10 (all paper, then all bubble, then the foam, then the right carton in
  Steps 4–7, then the left carton in Steps 8–11; and for each carton, flaps out before the body is collapsed).
* **Coaching note:** paper, bubble, foam, right carton, left carton. Flaps out first, then the push.

**Violation: More than one piece taken at once**
* **Visible cue:** either gripper lifts or carries two loose pieces in one pick, or a neighbour comes up
  with the first and is worked on instead of being laid back down in the start zone.
* **SOP rule broken:** Steps 1–3 (take one piece only; if a neighbour comes up, lower both back onto the
  table and take one again).
* **Coaching note:** one piece per pick. If two come up, put both back and start again.

**Violation: Loose piece set down on the way**
* **Visible cue:** either gripper sets a paper, bubble, or foam piece down in the work zone or anywhere on
  the table between the start zone and its pile, and picks it up again.
* **SOP rule broken:** Steps 1–3 (a loose piece goes straight from the start zone to its pile and is never set
  down on the way; in Config R it changes hands above the work zone, never on it).
* **Coaching note:** one lift, one carry, one set-down on the pile. Only cartons stop in the work zone.

**Violation: Piece put on the wrong pile**
* **Visible cue:** the left gripper sets a piece down on a pile of another material, paper on the bubble or
  foam pile, bubble on the paper or foam pile, foam on the paper or bubble pile, and the episode moves on.
* **SOP rule broken:** Steps 1–3 (paper to the paper pile in the front-left corner, bubble to the bubble pile
  just right of it, foam to the foam pile behind it).
* **Coaching note:** paper in the corner, bubble beside it, foam behind it. Look at what is under the gripper
  before you lower.

**Violation: Pile founded in the wrong place**
* **Visible cue:** the first piece of a material is set down somewhere other than its place: the paper pile
  not in the front-left corner, the bubble pile not to the right of the paper pile along the front edge, the
  foam pile not behind the paper pile; or a pile is founded touching another pile or the table edge.
* **SOP rule broken:** Steps 1–3 (the paper pile one gripper's width in from the front edge and the left
  edge; the bubble pile one gripper's width to its right; the foam pile one gripper's width behind it).
* **Coaching note:** the first piece decides where the pile lives. Place it by the edges and by the paper
  pile, a gripper's width clear.

**Violation: Piece released in the air**
* **Visible cue:** either gripper opens before the piece rests on the table, on the pile, or on the stack,
  and the piece falls, bounces, or is tossed toward its place; or in Config R the right gripper opens before
  the left gripper has closed on the piece.
* **SOP rule broken:** Steps 1–3, 7, and 11 (lower the piece until it rests, and only then open the gripper; in a
  hand-over the right gripper opens only once the left gripper has closed).
* **Coaching note:** take it all the way down before you let go. No drops.

**Violation: Piece taken back off a pile or the stack**
* **Visible cue:** either gripper lifts a piece back off one of the three piles or a carton back off the bale
  stage, whatever the reason. Adjusting the top foam piece flush on the base piece in Step 3, or nudging a
  piece, a pile, or the top carton into place in Step 12 without lifting it off, is not this.
* **SOP rule broken:** Steps 1–3, 7, and 11 (once a gripper has opened over a pile or the stack, the piece stays
  there).
* **Coaching note:** decide before you release. A wrong place is tagged, not undone.

**Violation: Carton worked outside the work zone**
* **Visible cue:** a carton has its flaps folded out or is collapsed anywhere other than the work zone:
  where it stood at the back, on the bale stage, or in the air.
* **SOP rule broken:** Steps 4–6 and 8–10 (every carton is stood in the work zone and has its flaps folded
  out and its body collapsed there, straight on the table).
* **Coaching note:** stand it in the middle, fold and collapse it in the middle, then carry it flat. Nothing
  is folded anywhere else.

**Violation: Carton put on a pile**
* **Visible cue:** either gripper sets a carton, flat or square, on or against any of the three piles instead
  of standing it in the work zone and laying it flat on the bale stage.
* **SOP rule broken:** Steps 4, 7, 8, and 11 (a carton goes to the work zone and then to the bale stage; it
  never goes on a pile).
* **Coaching note:** cartons never go on a pile. Middle, then back-right corner.

**Violation: Carton not anchored while the right gripper works on it**
* **Visible cue:** the left gripper is off the carton while the right gripper folds a flap out, pushes the
  carton down, or closes on the flat carton to lift it, and the carton slides, spins, tips over, springs open,
  or is chased across the table.
* **SOP rule broken:** Steps 5–7 and 9–11 (the left gripper holds the carton by one flap while the right
  gripper folds the others out, anchors it while it is pushed down, and anchors the flat carton while the
  right gripper takes its grip).
* **Coaching note:** left gripper on first, then fold, push, or grip.

**Violation: Flaps not turned out**
* **Visible cue:** the carton is pushed down, lifted, or stacked with one or more flaps, at either end, not
  turned out, still pointing into the opening or folded in. A flap has to be out, but it does not have to
  lie flat against the outside wall.
* **SOP rule broken:** Steps 5 and 9 (fold the flaps outward along their hinge creases until all target flaps
  are turned fully out and both openings are unobstructed).
* **Coaching note:** every flap out. Look into both ends before you push.

**Violation: Carton crushed instead of folded along its creases**
* **Visible cue:** a new crease is left across a face of the flat carton, or a face stays bowed, after the
  push. Where the right gripper pressed does not matter: on a face, on a wall, or anywhere else is fine so
  long as the carton folds only on its four existing creases.
* **SOP rule broken:** Steps 6 and 10 (the carton collapses along its existing creases with no new crease
  across a face).
* **Coaching note:** push anywhere that works, but watch the faces. If a fold line appears where there was
  none, it is a violation.

**Violation: Carton lifted before it lies flat**
* **Visible cue:** the right gripper lifts or slides the carton while it is still opening back up, or lays it
  on the bale stage and it springs partly open there.
* **SOP rule broken:** Steps 6–7 and 10–11 (confirm the carton lies flat on its own with both grippers clear,
  then anchor it and take it; if it springs open, push it down again).
* **Coaching note:** let go, watch it, then anchor and lift. If it opens, push it down again first.

**Violation: Work zone not cleared**
* **Visible cue:** the left gripper brings the left carton into the work zone while the right carton, or
  debris from it, is still lying there.
* **SOP rule broken:** Step 8 (the work zone holds no carton and no debris before the left carton is brought
  in).
* **Coaching note:** finish one carton completely, clear the middle, then fetch the next.

**Violation: Piece left behind**
* **Visible cue:** the episode ends with a loose piece still in the start zone, a carton still at the back or
  in the work zone, or a piece lying anywhere other than on its pile or on the stack.
* **SOP rule broken:** Step 12 (confirm the start zone, the carton area, and the work zone are bare and every
  piece is on its own pile or in the stack before homing).
* **Coaching note:** everything that started on the table ends on a pile or in the stack. Look over the
  table before you home.

**Violation: Wrong arm used**
* **Visible cue:** an action assigned to one gripper is done by the other, including the right gripper
  taking a loose piece, setting anything on a pile, or taking the left carton from the back; or the left
  gripper taking the right carton from the back, folding out any flap other than the one it holds, pushing
  a carton down, carrying a flat carton, or going to the bale stage.
* **SOP rule broken:** Steps 1–11 (the left gripper piles the loose pieces, fetches the left carton, holds
  each carton by one flap and folds that flap out, and anchors it; the right gripper fetches the right
  carton, folds the other flaps out, and collapses and stacks both).
* **Coaching note:** left gripper for the loose pieces, the left carton, and anchoring; right gripper for the
  right carton and everything the cartons need in the work zone and after. It does not swap.

**Violation: Piece dropped**
* **Visible cue:** either gripper drops a loose piece or a carton on the table or the floor during a lift or
  a carry.
* **SOP rule broken:** Steps 1–11 (every carry stays level and low over the table, and the gripper opens only
  once the piece rests).
* **Coaching note:** grip it properly, lift straight up, and keep each carry short and low.

**Violation: Wrong episode ending**
* **Visible cue:** recording stops before the bare start zone, the three piles, and the carton stack
  are confirmed, an arm is not home, a gripper is closed, or an arm does something else after homing.
* **SOP rule broken:** Step 12 (confirm the end state, return both arms home with grippers open as their final
  action, then stop recording).
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than tagging
them as SOP violations.

* Recording stops or pauses during the episode.
* A camera drops frames or loses its feed.
* An arm or gripper fails, drifts, or reports a motor error.
* A loose piece arrives wet, soiled, or taped, so it cannot be piled clean.
* A paper wad arrives so loose that it unfolds when it is set down, so it will not stay in a pile.
* A carton arrives with its tape still whole or a flap stuck closed, so its flaps cannot be folded down or its
  body cannot be collapsed.
* A carton arrives already crushed, soft at the creases, or torn through a crease, so it cannot be collapsed
  flat.
* A foam piece arrives already dented flat or split through.

## Annotation subtasks (from SOP)

1. Set a paper piece down on the paper pile with the left gripper
2. Set a bubble piece down on the bubble pile with the left gripper
3. Hand a loose piece from the right gripper to the left gripper above the work zone (Config R)
4. Stack the two foam pieces behind the paper pile and align the pile to the left edge with the left gripper
5. Take the right carton from the back with the right gripper, and the left carton with the left gripper,
   and stand it in the work zone
6. Hold the carton by one flap with the left gripper, fold that flap out, and fold the other flaps outward
   with the right gripper
7. Anchor the carton with the left gripper and push it down along a side wall with the right gripper to
   collapse it
8. Anchor the flat carton with the left gripper, take it with the right gripper, and lay it on the bale stage
9. Confirm the end state, return both arms home, and end the episode
