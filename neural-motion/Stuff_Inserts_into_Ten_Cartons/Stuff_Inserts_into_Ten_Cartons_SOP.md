# Stuff Inserts into Ten Cartons SOP

One episode stuffs, closes, and seals ten cartons. The cartons begin in a single-file input queue that
runs into the stuffing spot. Each carton slides onto the stuffing spot, takes one flyer laid flat
and one sample stood upright, is held still while both inserts are confirmed, has its four top flaps
folded in, is sealed with one tape strip along the top seam, and slides into the finished row. The
carton nearest the stuffing spot is always worked next, one carton at a time.

The order never changes within a carton: slide in, flyer, sample, confirm, close, seal, slide out. No
sample goes in before the flyer is flat on the carton floor, no flap folds before both inserts are
confirmed, and no strip comes out of the tape dispenser before all four flaps are in.

Both grippers move every carton while its base stays on the table. The right gripper takes the flyer,
the sample, and the presented tape strip, folds three of the four top flaps, and makes the seal press.
The left gripper folds the left flap and steadies the carton for every insert, every fold, and the
press. Nothing is turned in the air, and a gripper opens only over the spot the thing in it is going to.

The table is set up in one of three ways. Only the input queue moves; the stuffing spot, the flyer stack,
the sample tray, the tape dispenser, and the tape scrap rest are in the same place in all three. The
finished row moves only in Config L, where the queue takes its side.

* **Config L:** the input queue runs in from the left edge toward the stuffing spot. The finished row is
  behind the stuffing spot, running toward the back edge.
* **Config M1:** the input queue runs in from the front edge toward the stuffing spot. The finished row is
  on its left.
* **Config M2:** the input queue runs in from the back edge toward the stuffing spot. The finished row is
  on its left.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the input queue runs into the stuffing spot from the left edge (**Config L**), the
  front edge (**Config M1**) or the back edge (**Config M2**). One config per episode, chosen before
  recording and never changed mid-episode.
* **No right zone:** the tape dispenser, tape scrap rest, sample tray, and flyer stack fill the right side,
  so no right zone gives a straight ten-carton queue into the stuffing spot. The second center zone is used
  instead of a Config R.
* **Same-side rule:** both grippers slide every carton in every config. The **right gripper** pushes and
  the **left gripper** guides, except the Config L slide into the stuffing spot, where the carton comes from
  the left: there the **left gripper** pushes its left wall and the **right gripper** guides. No arm reaches
  across the table.
* **Fixed roles:** the fetches, the flat hold, the flap folds, and the seal press are the same in all three
  configs — the right gripper fetches, folds the near, far, and right flaps, and presses; the left gripper
  folds the left flap and holds.

## Setup

Complete both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole tabletop: the input queue and the finished row where this
   episode's config puts them, the stuffing spot at the center, and the flyer stack, sample tray, tape
   dispenser, and tape scrap rest on its right.
3. The stuffing spot is visible from above, so the flyer face, the standing sample, every flap fold,
   and the strip landing on the seam can all be seen.
4. Both arms are at home with grippers open.
5. The tabletop is clear of anything but the zones listed below.
6. Both arms reach the stuffing spot, the whole input queue, and the whole finished row where this
   episode's config puts them (left and back in Config L, front and left in Config M1, back and left in
   Config M2) without crossing or reaching a joint limit. The right arm also reaches the flyer stack, sample tray, tape dispenser, and
   tape scrap rest. Both grippers can travel beside a carton through each slide without touching.

### Materials checklist

1. Ten small **cartons** stand single file in the **input queue**, which runs toward the stuffing spot
   from the edge for this episode's config. The carton nearest the stuffing spot is worked first. There is
   an even gap between cartons, and the straight path from the first carton to the stuffing spot is bare.
   * **Config L:** the left edge, with the finished row moved to run from the stuffing spot toward the back edge
   * **Config M1:** the front edge
   * **Config M2:** the back edge
2. Every carton has its bottom already taped, is empty, and stands with all four **top flaps**
   standing up and clear of the opening.
3. Ten **flyers**, flat printed sheets of the same size, lie in one stack at the front right, all
   printed face up and all facing the same way. Each fits flat on a carton floor with room to spare.
4. Ten **samples**, identical capped units that stand on their own, sit upright in the sample tray
   at the right edge, caps up, spaced so a gripper can take one without touching its neighbor.
5. One tabletop **tape dispenser** stands to the right of the stuffing spot. It contains enough tape
   for the episode and any retries and automatically presents one cut-to-length strip at a time, sticky
   side down, with a stiff non-sticky **grab tab** accessible to the right gripper. Its stock is not
   counted during the episode.
6. One bare **tape scrap rest** sits beside the dispenser for a strip that must be scrapped.
7. The stuffing spot and the finished row are bare, clean, and dry.

### Workspace layout

* **Input queue:** a straight, unmarked single-file row running toward the stuffing spot from the left
  edge (**Config L**), the front edge (**Config M1**), or the back edge (**Config M2**). It holds the open
  cartons and has no slots or printed positions.
* **Stuffing spot:** the center of the table, at the end of the input queue, where every insert,
  fold, and seal happens. It holds one carton at a time and nothing else.
* **Finished row:** the clear area immediately left of the stuffing spot (**Config M1 and M2**) or
  immediately behind it (**Config L**). Sealed cartons stand here in one unmarked row. The first carton
  goes at the far end — the far-left end, or the far-back end in Config L; each later carton stops beside
  the last one, leaving an even gap.
* **Tape dispenser:** right of the stuffing spot, presenting one cut strip at a time by its grab tab.
* **Tape scrap rest:** beside the dispenser, where a damaged or badly laid strip is placed.
* **Flyer stack:** front right, ten flyers flat and printed face up.
* **Sample tray:** right edge, ten samples standing upright with caps up.

Everything the right gripper fetches is staged on the right. The input queue, stuffing spot, and
finished row are shared, and both grippers reach every carton position together.

## Vocabulary

* **Arm assignment:** both grippers move every carton by guided slides. The right gripper fetches the
  flyer, the sample, and the presented tape strip, folds the near, far, and right top flaps, and presses
  the seal. The left gripper folds the left top flap and holds the carton for every insert and fold.
  Neither gripper takes over the other's work. The right gripper also pushes every slide and the left
  gripper guides it, except the Config L slide into the stuffing spot, where the left gripper pushes and
  the right gripper guides.
* **Queue side:** the edge the input queue runs in from — the left edge (**Config L**), the front edge
  (**Config M1**), or the back edge (**Config M2**). One per episode, chosen before recording and never
  changed mid-episode.
* **Carton:** one small open box standing on its taped bottom. Its **near wall** faces the front
  edge and its **far wall** faces away.
* **Top flaps:** the four flaps standing up around the carton opening, named for the wall they hinge
  from: **near flap**, **far flap**, **left flap**, **right flap**.
* **Top seam:** the line down the middle of the closed top where the left flap and the right flap
  meet. It runs near to far and it is the only place a strip goes.
* **Forward slide:** **Unvalidated at the station.** Both grippers closed before contact. The right
  gripper presses the middle of the carton's near wall away from the front edge while the left gripper
  travels against the left wall as a guide. The carton moves straight away from the front edge with its
  base flat on the table — into the stuffing spot in Config M1, into the finished row in Config L.
* **Near slide:** **Unvalidated at the station.** Config M2 only. Both grippers closed before contact.
  The right gripper presses the middle of the carton's far wall toward the front edge while the left
  gripper travels against the left wall as a guide. The carton moves straight into the stuffing spot with
  its base flat on the table.
* **Right slide:** **Unvalidated at the station.** Config L only. Both grippers closed before contact.
  The left gripper presses the middle of the carton's left wall toward the stuffing spot while the right
  gripper travels against the right wall as a guide. The carton moves straight into the stuffing spot with
  its base flat on the table.
* **Left slide:** **Unvalidated at the station.** Config M1 and M2 only. Both grippers closed before
  contact. The right gripper presses the middle of the carton's right wall toward the finished row while
  the left gripper travels against the left wall as a guide. The carton keeps its facing and its base
  stays flat on the table.
* **Flyer:** one flat printed sheet. It lies on the carton floor **printed face up** with no corner
  folded under and no corner riding up a wall.
* **Sample:** one capped unit that stands on its own. It goes in **upright, cap up**, standing
  either on the carton floor beside the flyer or squarely on top of the flyer. Either resting place
  is correct as long as the sample stands on its own and the flyer stays flat and printed face up.
* **Tape dispenser:** **Unvalidated at the station.** The tabletop machine automatically advances and
  cuts one ready-to-use strip after the presented strip is removed. The grippers do not operate its
  cutter or reach inside it.
* **Strip:** one cut length of tape presented by the dispenser. It is only ever handled by its **grab
  tab**, the non-sticky end. A strip that touches a gripper anywhere else is scrapped.
* **Hangs straight:** the strip dangling free and flat from the lifted grab tab, not curled,
  twisted, or stuck to itself.
* **Laid along the seam:** the far end of the hanging strip set down on the far end of the top seam,
  then drawn toward the front edge along the seam so the strip settles onto it behind the gripper,
  with the tab released past the near end.
* **Flat hold:** the left gripper closed and resting on the carton's near wall to keep it from
  shifting while the right gripper works. It goes on before the right gripper moves and comes off
  after the right gripper is clear.
* **Lift:** coming straight down onto the grasp point, closing, and raising straight up until there
  is daylight under the thing, before anything moves sideways.
* **Lower in:** carrying level over the opening, lowering straight down until the thing is resting
  on the carton floor, and releasing once it is resting. Nothing is dropped in from above the rim.
* **Settled:** the thing stays put for 2 seconds after the gripper lifts clear, with nothing
  sliding, toppling, springing open, or hanging over an edge.
* **Release point:** inside the carton being worked, on the tape scrap rest, or on the applied strip
  after it is resting on the seam. A gripper opens nowhere else. Cartons are moved with already-closed
  grippers and are never held or released.

## Steps

Steps 1 to 6 finish one carton. Run them ten times, always taking the carton nearest the stuffing spot.
Step 7 ends the episode once the tenth sealed carton is in the finished row.

Steps 1 and 6 depend on the config: the carton slides into the stuffing spot from the left edge, the front
edge, or the back edge, and in Config L the sealed carton slides back instead of left. Every other line,
and all of Steps 2 to 5 and 7, is the same in all three configs.

### Step 1: Bring one carton to the stuffing spot

**Goal:** one open carton standing square on the stuffing spot, all four top flaps still standing up.

Close both grippers before either one touches the carton nearest the stuffing spot, and look which edge
the input queue runs in from.

* **IF the queue runs in from the left edge (Config L):** the **left gripper** presses against the middle
  of the carton's **left wall**. The **right gripper** rests against the middle of its **right wall** as a
  guide. Make one slow **right slide** toward the stuffing spot.
* **IF the queue runs in from the front edge (Config M1):** the **right gripper** presses against the
  middle of the carton's **near wall**. The **left gripper** rests against the middle of its **left wall**
  as a guide. Make one slow **forward slide** away from the front edge.
* **IF the queue runs in from the back edge (Config M2):** the **right gripper** presses against the
  middle of the carton's **far wall**. The **left gripper** rests against the middle of its **left wall**
  as a guide. Make one slow **near slide** toward the front edge.

Then, in all three:

* Slide until the carton is centered on the **stuffing spot**. Keep its base flat and all four top flaps
  clear of both grippers.
* Stop once it is centered, then lift both grippers straight clear.

Move one carton at a time. Do not pinch or lift a carton, and do not start the next carton until the one
on the stuffing spot is sealed and in the finished row.

**Check:** the carton stands square on the stuffing spot with its near wall toward the front edge, all
four top flaps standing up and clear of the opening, and nothing inside. If it stops short or starts to
turn, slide it back to the head of the input queue with the same push and guide, then repeat this
config's slide.

### Step 2: Load the flyer and the sample

**Goal:** one flyer lying flat on the carton floor printed face up, and one sample standing upright
in the carton, either beside the flyer or on top of it.

The **left gripper** takes a **flat hold** on the carton's near wall before the first insert and keeps it
through both inserts.

#### 2.1 The flyer

* The **right gripper** closes on the near edge of the top **flyer** on the flyer stack, lifts it
  straight up, carries it level over the carton opening, lowers it in until it is resting on the
  carton floor, and releases.
* The flyer goes in printed face up, the way it lay on the stack. It is not turned, folded, or
  curled on the way in.

#### 2.2 The sample

* The **right gripper** closes on one **sample** in the sample tray, lifts it straight up, carries
  it level and upright over the carton opening, lowers it in until it is standing on the carton floor
  beside the flyer or squarely on top of the flyer, and releases once it is standing on its own.
* Take one sample per trip. The sample stays upright the whole way. It is lowered onto its resting
  place, never set down half on the flyer and half on the floor, and never leaned against a wall.

The **left gripper** releases the flat hold once the right gripper is clear of the opening.

**Check:** the flyer lies flat on the carton floor printed face up with no corner folded under or riding
a wall, and the sample stands upright and cap up on the carton floor beside it or squarely on top of it.
If the flyer landed folded, the sample landed leaning, or the sample sits half on the flyer and half on
the floor, lift it clear and put it in again.

### Step 3: Confirm the orientation of both inserts

**Goal:** both inserts seen and held still, so the reviewer can read the flyer face and the standing
sample from above.

* Lift both grippers clear of the carton opening.
* Leave the open carton untouched for 2 seconds with the stuffing spot in frame. Nothing is held,
  nudged, or moved during the hold.
* If the flyer is face down, folded, or riding a wall, or the sample is leaning, lying down, or
  standing half on the flyer and half on the floor, correct it now by lifting it clear and putting it
  in again, then hold for 2 seconds again.

Nothing is folded, sealed, or fetched until this hold is done.

**Check:** during the hold the flyer is flat and printed face up on the carton floor and the sample
stands upright with its cap up, both visible from above, and both grippers are clear of the opening.

### Step 4: Close the four top flaps

**Goal:** all four top flaps folded in flat, with the top seam running near to far down the middle.

Fold in this order and no other. Every fold is a fold down onto the flaps already in, never a press on
the carton contents.

#### 4.1 Near flap, then far flap

* The **left gripper** takes a **flat hold** on the carton's near wall and keeps it for the whole
  step.
* The **right gripper** pinches the free edge of the **near flap**, folds it away from the front
  edge down over the opening, and releases.
* The **right gripper** pinches the free edge of the **far flap**, folds it toward the front edge
  down over the near flap, and releases.

**Expected state:** the opening covered near to far, the left and right flaps still standing up.

#### 4.2 Left flap, then right flap

* The **left gripper** lifts off the near wall, pinches the free edge of the **left flap**, folds it
  right down over the flaps already in until it reaches the middle, releases, and goes back to its
  flat hold on the near wall.
* The **right gripper** pinches the free edge of the **right flap**, folds it left down over the
  flaps already in until its edge meets the left flap along the middle, and releases.

**Check:** all four flaps lie flat and down, no flap edge stands proud or is trapped under another flap,
and the left and right flaps meet along the middle in one straight top seam running near to far. If a
flap stands proud or the seam is off the middle, lift that flap and fold it again.

### Step 5: Seal the top seam

**Goal:** one tape strip laid down the top seam and pressed flat, with the carton still square on the
stuffing spot.

* The **left gripper** keeps its **flat hold** on the near wall for the whole seal.
* The **right gripper** pinches the **grab tab** of the strip presented by the **tape dispenser**, lifts
  it straight up until it **hangs straight**, and carries it level over the carton. The dispenser
  presents the next strip after this one clears it.
* Lay it **along the seam**: set the far end of the strip down on the far end of the top seam, draw
  the tab toward the front edge along the seam so the strip settles onto it behind the gripper, and
  release the tab once it lies past the near end.
* The **right gripper** presses along the strip from far to near in one stroke, without coming off
  the tape, until it lies flat with no lifted end and no bubble standing up.
* Release the right gripper, then the left.

A strip is touched only by its grab tab. If it folds onto itself before landing, place it on the tape
scrap rest and take the next presented strip. If it lands off the seam or folds on the carton, peel it
off, place it on the scrap rest, and take the next presented strip. A scrapped strip is never reused.

**Check:** one strip runs down the top seam from end to end, lies flat with no lifted end, and the flaps
stay down when the carton moves. The dispenser has presented another strip, any scrapped strip is on the
tape scrap rest, and no strip is stuck to a gripper.

### Step 6: Slide the sealed carton into the finished row

**Goal:** the sealed carton standing square at the open end of the finished row, taped seam up.

* Close both grippers before either one touches the sealed carton.
* **IF Config M1 or M2:** the **right gripper** presses against the middle of the carton's **right
  wall**, the **left gripper** rests against the middle of its **left wall** as a guide, and one slow
  **left slide** takes it into the finished row on the left; the first carton goes to the far-left end.
  **IF Config L:** the **right gripper** presses against the middle of the carton's **near wall**, the
  **left gripper** rests against the middle of its **left wall** as a guide, and one slow **forward
  slide** away from the front edge takes it into the finished row behind the stuffing spot; the first
  carton goes to the far-back end.
* Each later carton stops beside the carton already at the row's open end, with an even gap and without
  touching it.
* Stop once the carton stands square in the row, then lift both grippers straight clear.

**Check:** the sealed carton stands square at the open end of the finished row with its taped seam up,
its near wall still toward the front edge, an even gap from its neighbor, and no finished carton moved.
If it stops short or starts to turn, slide it back to the stuffing spot, then repeat this config's slide.

### Step 7: Confirm the ten cartons and end the episode

* Confirm the finished row holds ten cartons, each closed with all four flaps down and one strip along
  its top seam, all standing in one row with even gaps; and confirm the input queue, flyer stack, and
  sample tray are empty and the stuffing spot is bare.
* Return both arms home, clear of the finished row and the stuffing spot, then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the ten sealed cartons out of the finished row, peel the strip off each top, and open all four
   flaps.
2. Take the flyer and the sample out of each carton. Set the used strips aside for disposal.
3. Check each carton for a crushed wall, a torn flap, or a bottom tape that has let go. Replace any
   carton that will not stand square with its flaps standing up.
4. Stand ten cartons single file in the input queue for the next episode's config — running in from the
   left edge (Config L), the front edge (Config M1), or the back edge (Config M2) — with an even gap,
   bottoms taped, empty, all four top flaps standing up. Put the first carton nearest the stuffing spot
   and leave the path ahead bare, and leave the finished row for that config bare (behind the stuffing
   spot in Config L, left of it otherwise).
5. Restack ten flyers flat at the front right, all printed face up and all facing the same way.
   Replace any flyer that is creased or torn.
6. Stand ten samples upright in the sample tray with caps up and an even gap between them. Replace
   any sample that will not stand on its own or whose cap is loose.
7. Remove all tape scraps from the scrap rest. Check that the tape dispenser contains enough tape for
   one episode and retries, cuts each strip to the full seam length, and presents the next strip by a
   clean non-sticky grab tab.
8. Wipe the input path, stuffing spot, and finished row and confirm they are clean and dry. A dirty base
   or tabletop can make a carton catch or turn during a slide.
9. Vary which sample and which flyer face is used on each cycle rather than running the same pairing
   every time. The count stays at ten cartons, ten flyers, and ten samples; tape comes from the
   dispenser on demand.
10. Run both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The
visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation
label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do
not delete it just because a rule was broken.

### Violations

**Note on the start position:** the violations below were written for Config M1 (input queue running in
from the front edge, finished row on the left). The slide and arm-role cues will be rewritten later to
cover all three start positions; they are left as they are for now. Until then, anything that does not
match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the operator does does not match the config on the table — the input queue does
  not run in from the edge for the config, or the finished row is not where the config puts it; a carton
  is slid into the stuffing spot from a different edge than the one the queue runs in from; the pushing
  and guiding grippers are the ones for another config; a sealed carton slides left in Config L or back
  in Config M1 or M2; or the wrong IF line is followed.
* **SOP rule broken:** the start position and the same-side rule (the queue runs in from the left edge in
  Config L, the front edge in Config M1, or the back edge in Config M2; the right gripper pushes and the
  left gripper guides, except the Config L slide in, where the left gripper pushes and the right gripper
  guides; the IF line followed is the one for the config on the table).
* **Coaching note:** look which edge the input queue runs in from before the first reach, then follow that
  config's IF lines through Steps 1 and 6.

**Violation: Wrong order**

* **Visible cue:** the sample goes in before the flyer, a flap folds before the confirm hold, a strip
  comes out of the dispenser before all four flaps are in, or the carton moves to the finished row
  before the seam is sealed.
* **SOP rule broken:** Steps 1 to 6, the order within a carton never changes: slide in, flyer, sample,
  confirm, close, seal, slide out.
* **Coaching note:** slide in, flyer, sample, confirm, close, seal, slide out. Finish the step you are in
  before starting the next one.

**Violation: Cartons taken out of order**

* **Visible cue:** a carton behind the front carton in the input queue is moved first, or a second carton
  reaches the stuffing spot before the first is sealed and in the finished row.
* **SOP rule broken:** Step 1, take the carton nearest the stuffing spot and finish it before moving the
  next carton.
* **Coaching note:** work the single-file queue from front to back, one carton at a time.

**Violation: Arms swapped roles**

* **Visible cue:** the left gripper takes a flyer, sample, or strip, folds the near, far, or right flap,
  or makes the seal press; or the right gripper folds the left flap or the guide and push roles are
  swapped during a carton slide.
* **SOP rule broken:** Steps 1 to 6, the right gripper fetches and performs the primary work and supplies
  each push, while the left gripper holds, folds the left flap, and guides each slide.
* **Coaching note:** right fetches, works, and pushes; left holds, folds left, and guides.

**Violation: Carton slid wrong**

* **Visible cue:** a carton is pinched, lifted, tipped, turned, moved by a flap, or pushed without the
  other gripper guiding its side wall.
* **SOP rule broken:** Steps 1 and 6, both grippers are closed before contact, the right gripper supplies
  the push, the left gripper guides, and the carton base stays flat on the table.
* **Coaching note:** let the table support the carton; right pushes and left guides.

**Violation: More than one thing handled at once**

* **Visible cue:** two flyers come off the stack together, two samples leave the tray together, two
  strips are taken together, or a carton is moved while a flyer, sample, or strip is still held.
* **SOP rule broken:** Steps 1, 2, 5, and 6, move one carton at a time and take one flyer, one sample,
  and one strip for its cycle.
* **Coaching note:** one carton, one flyer, one sample, and one strip at a time.

**Violation: Flyer put in wrong**

* **Visible cue:** the flyer goes in printed face down, folded, curled, standing on edge, riding up
  a carton wall with a corner, or landing on top of the sample, and the flaps are folded over it
  anyway.
* **SOP rule broken:** Step 2.1, the flyer is lowered in printed face up and rests flat on the
  carton floor, and a bad landing is corrected by lifting it clear and putting it in again.
* **Coaching note:** face up, flat on the floor, first thing in. Everything after this is scored on
  it.

**Violation: Sample put in wrong**

* **Visible cue:** the sample goes in lying down, upside down, leaning against a wall, straddling the
  flyer edge with part of its base on the flyer and part on the carton floor, or it is turned or tipped
  between the lift and the set down. Standing squarely on top of the flyer is not a violation.
* **SOP rule broken:** Step 2.2, the sample is carried level and upright and lowered in until it stands
  on its own, cap up, on the carton floor beside the flyer or squarely on top of it.
* **Coaching note:** upright the whole way, and all the way down onto one surface — the floor or the
  flyer, not both.

**Violation: Dropped in from above the rim**

* **Visible cue:** a gripper opens above the carton opening and the flyer flutters in or the sample
  falls in, instead of the thing being lowered until it is resting.
* **SOP rule broken:** Step 2, lower the flyer and the sample straight down until each is resting on
  the carton floor, then release.
* **Coaching note:** take it all the way down, then let go. Nothing gets dropped in.

**Violation: Carton not steadied**

* **Visible cue:** the left gripper is off the near wall while a flyer or a sample goes in, while a
  flap is folded, or during the seal press, or the carton slides, rocks, or shifts under the right
  gripper.
* **SOP rule broken:** Steps 2, 4, and 5, the left gripper takes a flat hold on the near wall before
  the right gripper moves and keeps it until the right gripper is clear.
* **Coaching note:** the hold goes on first and comes off last. A loose carton ruins the seam.

**Violation: Confirm hold skipped or worked through**

* **Visible cue:** a flap is folded straight after the sample lands with no still scene between
  them, a gripper stays in or over the opening during the hold, or something is nudged, pushed down,
  or rearranged while the hold is meant to be running.
* **SOP rule broken:** Step 3, lift both grippers clear and leave the open carton untouched for 2
  seconds with the stuffing spot in frame before anything is folded.
* **Coaching note:** hands off and count two. The reviewer has to see what went in.

**Violation: Bad orientation left uncorrected**

* **Visible cue:** the confirm hold runs with the flyer face down, folded, or riding a wall, or with
  the sample leaning, lying down, or straddling the flyer edge, and the flaps are folded anyway.
* **SOP rule broken:** Step 3, correct a wrong insert by lifting it clear and putting it in again,
  then hold for 2 seconds again.
* **Coaching note:** fix it and hold again. A confirm that confirms the wrong thing is worse than
  none.

**Violation: Flaps folded in the wrong order**

* **Visible cue:** a side flap goes in before the near and far flaps, the far flap goes before the
  near flap, a flap is trapped under one folded later, or a flap is left standing up when the strip
  comes out.
* **SOP rule broken:** Step 4, fold near, then far, then left, then right, each one down over the
  flaps already in.
* **Coaching note:** near, far, left, right. Every time, no exceptions.

**Violation: Top seam off the middle or flaps proud**

* **Visible cue:** the left and right flaps overlap heavily, leave a gap, or meet well off the
  middle, or a flap edge stands proud of the top, and the strip goes on anyway.
* **SOP rule broken:** Step 4.2, the left and right flaps fold in until they meet along the middle
  in one straight top seam running near to far, and a proud or crooked flap is lifted and folded
  again.
* **Coaching note:** get the seam straight down the middle before you reach for the tape.

**Violation: Strip handled off the grab tab**

* **Visible cue:** a gripper pinches a strip anywhere but its grab tab, touches the sticky face, or
  reaches inside the tape dispenser instead of taking the presented tab.
* **SOP rule broken:** Step 5, the grab tab is the only part of a strip a gripper touches.
* **Coaching note:** take only the tab presented by the dispenser.

**Violation: Strip laid off the seam or reused after a bad landing**

* **Visible cue:** the strip lands at an angle, off to one side, short of either end, or folded onto
  itself, and is reused instead of being placed on the tape scrap rest.
* **SOP rule broken:** Step 5, lay the strip along the whole seam; scrap a damaged or badly laid strip
  and take the next strip presented by the dispenser.
* **Coaching note:** tape sticks once. Move the bad strip to the scrap rest and take the next one.

**Violation: Seam not pressed**

* **Visible cue:** the strip is laid but never pressed, pressed only at one end, pressed in several
  separate dabs, or left with an end lifting or a bubble standing up when the carton moves.
* **SOP rule broken:** Step 5, press along the strip from far to near in one stroke without coming
  off the tape until it lies flat with no lifted end.
* **Coaching note:** one stroke, all the way across, without leaving the tape.

**Violation: Carton placed wrong in the finished row**

* **Visible cue:** a sealed carton stops outside the finished row, is turned, touches another carton,
  leaves an uneven gap, or pushes a carton already in the row.
* **SOP rule broken:** Step 6, slide the carton left into the open end of the finished row, keep its
  facing, leave an even gap, and do not move a finished carton.
* **Coaching note:** use the row's open end and stop before touching its neighbor.

**Violation: Turned in the air**

* **Visible cue:** a flyer, sample, or strip is rotated or flipped between lift and placement, or a
  carton turns during either guided slide.
* **SOP rule broken:** Steps 1 to 6, held items keep their staged orientation, and cartons keep their
  facing while sliding on the table.
* **Coaching note:** preserve orientation during picks and use the guide gripper during carton slides.

**Violation: Held item dragged instead of lifted**

* **Visible cue:** a flyer, sample, or strip drags along its stage during a pick instead of lifting
  clear. The prescribed carton slides, flap folds, and tape draw are not violations.
* **SOP rule broken:** Steps 2 and 5, lift a held item clear before carrying it sideways.
* **Coaching note:** lift held items; slide only the cartons as prescribed.

**Violation: Regripped in the air**

* **Visible cue:** a gripper shifts, rolls, or seats its hold again on a flyer, sample, or strip without
  setting it down first. Travelling side-wall contact during a carton slide is not a grasp.
* **SOP rule broken:** Steps 2 and 5, set a held item down before taking a new hold.
* **Coaching note:** put it down before you take a new hold.

**Violation: Gripper released over the wrong place**

* **Visible cue:** a gripper opens over the input queue, finished row, flyer stack, sample tray, tape
  dispenser, a carton that is not being worked, or open table.
* **SOP rule broken:** Steps 1 to 6, a gripper opens inside the carton being worked, on the tape scrap
  rest, or after the strip is resting on the seam. Cartons are moved with closed grippers.
* **Coaching note:** know where it lands before you open the gripper.

**Violation: Placement corrected by shoving**

* **Visible cue:** a flyer or sample is nudged after release, a sealed top is pushed to square a flap,
  or a carton is corrected with small pats instead of returning it to the start of its slide.
* **SOP rule broken:** Steps 1 to 6, lift and replace a bad insert, refold a bad flap, and return a
  misplaced carton to the slide's starting point before repeating the full slide.
* **Coaching note:** restart the prescribed motion instead of making small corrective shoves.

**Violation: Dropped, collided, or knocked something over**

* **Visible cue:** a flyer, sample, or strip falls short of its destination; a sample topples; a carton
  tips or strikes another carton; the dispenser, scrap rest, flyer stack, or sample tray shifts; or the
  two arms strike each other.
* **SOP rule broken:** Steps 1 to 6, keep each held item on a clear travel path, each carton on its base,
  and both arms clear of each other.
* **Coaching note:** check the path and the landing spot before you move.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a carton open or still on the stuffing spot, a flyer or sample
  left on its stage, fewer than ten sealed cartons in the finished row, a strip stuck to a gripper, an
  arm away from home, or recording stops before both arms return home.
* **SOP rule broken:** Step 7, confirm the ten sealed cartons and empty input stages; return both arms
  home; then stop recording.
* **Coaching note:** confirm first, then home, then stop recording.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never
use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Defective carton:** a wall that crushes under a correct push, a base that catches or tips on a clean
  table, a flap that tears at its fold, or bottom tape that lets go. Replace it before the next episode.
* **Defective flyer:** creased, torn, or stuck to the flyer under it so two lift together on a
  correct pick. Replace the stack before the next episode.
* **Defective sample:** one that will not stand on its own on a flat carton floor, or whose cap
  comes off in the gripper. Replace it before the next episode.
* **Tape dispenser fault:** it fails to present a strip, cuts a strip shorter than the seam, presents a
  sticky or inaccessible grab tab, or does not advance after a correct pick. Service it before the next
  episode.
* **Input queue, finished row, dispenser, or tape scrap rest shifts out of its zone** during the episode.
* **Carton slides** under a correct flat hold because the stuffing spot is dusty or slick. Wipe it
  before the next episode.

## Annotation subtasks (from SOP)

1. Slide one carton from the input queue to the stuffing spot
2. Lower one flyer into the carton face up
3. Lower one sample into the carton upright
4. Hold the open carton still to confirm both inserts
5. Fold the near and far top flaps in
6. Fold the left and right top flaps in
7. Lay one tape strip along the top seam
8. Press the seam strip flat
9. Slide the sealed carton into the finished row
10. Confirm ten sealed cartons and end the episode
11. Return both arms home and end the episode
