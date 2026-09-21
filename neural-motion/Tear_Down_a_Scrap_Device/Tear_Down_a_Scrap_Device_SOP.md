# Tear Down a Scrap Device SOP (Single Unit)

This SOP covers tearing down a single scrap handheld device into sorted recycling streams using a two-arm
robot system. Both arms are used throughout: the grippers cooperate to hold the unit, drive out the
back-panel screws, disconnect the battery lead, extract the board, and sort the board, plastics, metal
and cell into their bins, with the left and right grippers taking the specific roles called out in each
step. The task runs from a scrap unit in its start zone to four sorted bins and a logged unit record.

The table is set up in one of three ways. Only the unit moves; the screw cup, the tools, the bin row and the
log sheet are in the same place in all three.

- **Config L:** the unit is at the back-left.
- **Config M:** the unit is at the front-center, in front of the working area.
- **Config R:** the unit is at the back-right.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

- **Start position:** the unit starts at the back-left (**Config L**), the front-center (**Config M**) or
  the back-right (**Config R**). One config per episode, chosen before recording and never changed
  mid-episode.
- **Same-side rule:** the gripper on the unit's side picks it — the left gripper in Config L and M, the
  right gripper in Config R. No arm reaches across the table. Nothing is handed over: the working area is
  within reach of both grippers.
- **Fixed roles:** from Step 2 on the grippers keep the roles called out in each step in every config — the
  left gripper holds the unit and cups the screws, the right gripper drives and pries.
- **Working position:** the unit is always moved to the centre of the table before any screw is driven.
- **Screws first:** the back panel is only lifted once all four screws are out and in the screw cup. The
  panel is never prised off against a screw.
- **Battery before board:** the battery lead is always disconnected before any other connector is touched
  or the board is lifted.
- **Teardown order:** back panel first, then the battery lead, then the board, then the cell, then the
  remaining plastics and metal.
- **One stream per bin:** every part is placed in the bin for its material. No part is left in the
  working area at the end of the episode.
- **Log last:** the unit is logged only after all four bins are loaded and the working area is clear.

## Setup

Go through both checklists before starting the episode.

### Hardware checklist

- Cameras are on and recording
- Env camera frame includes the front and back edges of the table, the four bins, and is centered on
    the table's midpoint
- Both arms are at the home position with grippers open
- Table surface is clear of any objects other than the scrap unit(s), the tools and the bins

### Materials checklist

- Scrap unit(s) to be torn down are placed in the start zone, back panel up, one unit per episode
    - **Config L:** back-left
    - **Config M:** front-center, in front of the working area
    - **Config R:** back-right
- Each unit has a back panel held by 4 screws, 1 board, 1 cell with a battery lead, and a plastic
    housing
- The driver is at the right edge, next to the pry tool, and matches the back-panel screws
- The screw cup is at the front-left and is empty at the start of the episode
- All four bins are in the bin row along the back edge, labelled **board**, **plastics**, **metal**
    and **cell**, and none is overfull
- Center of the table is clear (working area for unscrewing, disconnecting and extracting)
- The log sheet is at the front-right with the next unit line blank

## Workspace layout

- **Start zone**: scrap unit(s), back panel up (input) — back-left (Config L), front-center (Config M) or
  back-right (Config R)
- **Center**: working area (unscrew, disconnect, extract, sort)
- **Front-left**: screw cup (the four back-panel screws)
- **Right edge**: driver and pry tool
- **Back edge**: bin row, left to right: board, plastics, metal, cell (output)
- **Front-right**: log sheet (unit record)

## Vocabulary

These are the terms used in this SOP. Operators and annotators must use this language consistently. One
term per concept, used throughout.

### Device anatomy

- **Unit:** a single scrap device to be torn down, counted as one episode.
- **Back panel:** the removable cover on the back of the unit, held by four screws.
- **Front housing:** the plastic shell left after the back panel and board are out.
- **Screw:** one of the four fasteners holding the back panel to the housing.
- **Screw boss:** the threaded post in the housing that a screw turns into.
- **Near-left screw:** the back-panel screw closest to the operator on the left. Work starts here.
- **Far-left screw:** the back-panel screw farthest from the operator on the left.
- **Far-right screw:** the back-panel screw farthest from the operator on the right.
- **Near-right screw:** the back-panel screw closest to the operator on the right. Work ends here.
- **Board:** the printed circuit board carrying the components and connectors.
- **Board screw:** the single screw holding the board to the housing, under the board's near edge.
- **Cell:** the battery pack inside the unit, held to the housing by adhesive or a clip.
- **Battery lead:** the two-wire cable running from the cell to the board.
- **Battery connector:** the plug on the end of the battery lead that seats on the board.
- **Socket:** the matching header on the board that the battery connector seats in.
- **Ribbon cable:** the flat cable between the board and the display, seated in a latch.
- **Latch:** the small hinged clamp that holds a ribbon cable in place.
- **Shield can:** the stamped metal cover soldered or clipped over part of the board.
- **Bracket:** a metal frame or plate screwed to the housing, separate from the board.
- **Swollen cell:** a cell with a domed or split face; it is a stop condition, not a sort.

### Bins and tools

- **Bin row:** the four labelled bins along the back edge of the table.
- **Board bin:** the bin for the board and any board-mounted daughterboard.
- **Plastics bin:** the bin for the back panel, the front housing and any plastic clip or lens.
- **Metal bin:** the bin for screws, brackets, shield cans and any loose metal part.
- **Cell bin:** the bin for the cell, taped and placed on its own.
- **Screw cup:** the cup at the front-left that holds screws until they go to the metal bin.
- **Driver:** the tool that drives the screws.
- **Pry tool:** the flat tool used to lift the back panel and to unseat the board.
- **Log sheet:** the record at the front-right holding one line per unit.
- **Unit line:** the single row on the log sheet for the unit torn down in this episode.

### Workspace zones

- **Start zone:** where the unit lies at the start of the episode — back-left (**Config L**), front-center
  (**Config M**) or back-right (**Config R**). One per episode, chosen before recording and never changed
  mid-episode.
- **Working area:** the center of the table where unscrewing, disconnecting, extracting and sorting
  happen.
- **Front-left cup:** the screw cup holding the back-panel screws and the board screw.
- **Right edge:** the rest position for the driver and the pry tool.
- **Back edge:** the bin row, the output zone for all four material streams.
- **Front-right:** the log sheet position.
- **Home position:** the default resting pose for each arm: gripper open and clear of the table.

### Actions

- **Pick:** move one unit to the working area.
- **Unscrew:** drive a screw out with the driver until it is free of its boss, then lift it clear.
- **Lift:** raise the back panel off the housing once all four screws are out.
- **Disconnect:** pull the battery connector straight up out of its socket.
- **Release:** open a latch so a ribbon cable can be pulled free.
- **Extract:** lift the board clear of the housing with no cable still attached.
- **Sort:** place one part in the bin for its material.
- **Tape:** cover the cell's contacts with a tape strip before it goes to the cell bin.
- **Log:** write the unit line on the log sheet at the end of the episode.

## Steps

Only Step 1 depends on where the unit is: in Config L and M the **left gripper** picks it, in Config R the
**right gripper** picks it. Every other line, from Step 2 on, is the same in all three configs.

### Step 1: Move a unit to the working area

**Goal:** one unit sits in the working area, back panel up, ready to be unscrewed.

Look where the unit is before reaching for it.

- **IF the unit is at the back-left (Config L):** with the **left gripper**, grasp one unit from the
  back-left pile by the middle of its left edge.
- **IF the unit is at the front-center (Config M):** with the **left gripper**, grasp one unit from the
  front-center by the middle of its left edge.
- **IF the unit is at the back-right (Config R):** with the **right gripper**, grasp one unit from the
  back-right pile by the middle of its right edge.

Then, in all three:

- Lift it clear of the table and carry it to the center; do not drag or slide it.
- Set it down flat with the back panel up and release.
- If the unit lands front-up, grasp the left and right edges, lift it 5 cm clear and turn it over so the
  back panel faces up.

### Step 2: Unscrew the back panel

**Goal:** all four back-panel screws are out and in the screw cup, and the back panel is off and in the
plastics bin.

#### 2.1 Inspect the unit before opening

- Confirm the back panel is up and all four screws are visible and reachable.
- Check the unit for a swollen cell: a domed back panel, a split seam, or a panel that will not sit flat.
- If the cell is swollen, the unit is leaking, or the panel is already off → stop the episode and report
  a defective unit. Do not unscrew it.

#### 2.2 Take the driver

- With the right gripper, take the driver from the right edge.
- With the left gripper, hold the unit down by the middle of its left edge for the whole step.
- Confirm the driver tip matches the screw heads before the first turn.

#### 2.3 Drive out the four screws

- Working in corner order (near-left, far-left, far-right, near-right), seat the driver in each screw
  head and turn it out until the screw is free of its boss.
- Keep the driver square to the screw; do not turn a screw that is not seated in the tip.
- If a screw turns without backing out, or the head rounds off → stop the episode and report a defective
  unit.

#### 2.4 Cup the screws

- With the left gripper, lift each freed screw clear of the unit and drop it in the screw cup.
- Count four screws in the cup before continuing.
- With the right gripper, return the driver to the right edge.

#### 2.5 Lift the back panel

- Confirm the screw cup holds four screws and no screw is left in the housing.
- With the right gripper, take the pry tool, enter the seam at the near edge and lift the panel until the
  seam opens along one side.
- With the left gripper, grasp the lifted edge and raise the panel straight off the housing.
- Return the pry tool to the right edge.
- If the panel does not lift with light pressure → set it back down, re-check for a fifth screw and
  repeat 2.3 for it. Do not force the panel.

#### 2.6 Sort the back panel

- With the left gripper, carry the back panel to the plastics bin and release it inside the bin.
- Confirm the working area holds the open unit only.

### Step 3: Disconnect the battery lead

**Goal:** the battery connector is out of its socket and the lead lies clear of the board, with no other
connector touched first.

#### 3.1 Find the battery connector

- Identify the cell, follow the battery lead from the cell to the board, and find its socket.
- Confirm it is the battery lead and not the ribbon cable before gripping.

#### 3.2 Pull the connector

- With the left gripper, hold the board down next to the socket so the board does not lift.
- With the right gripper, grasp the battery connector by its body, not by the wires, and pull it straight
  up out of the socket.
- Lay the freed lead to the side of the board so it is clear of the extraction path.
- If the connector does not release with a straight pull, release, re-seat the grip on the connector body
  and pull again. Never pull on the wires.

#### 3.3 Confirm the unit is dead

- Confirm the connector is fully out of the socket and no pin is still engaged.
- Confirm no other connector was disturbed during the pull.

**Warning:** No further connector is touched and the board is not lifted until the battery lead is
disconnected.

### Step 4: Extract the board

**Goal:** the board is out of the housing, free of every cable, and in the board bin.

#### 4.1 Free the remaining cables

- With the right gripper, open each ribbon-cable latch on the board.
- With the left gripper, pull each freed ribbon cable straight out of its latch.
- Confirm no cable still runs between the board and the housing.

#### 4.2 Remove the board screw

- With the right gripper, take the driver and drive out the board screw at the board's near edge.
- With the left gripper, lift the screw clear and drop it in the screw cup.
- Return the driver to the right edge.

#### 4.3 Lift the board out

- With the right gripper, enter the pry tool under the board's near edge and lift it until the board
  clears the housing lip.
- With the left gripper, grasp the board by its edges and lift it straight up out of the housing.
- Return the pry tool to the right edge.
- If the board resists, set it back down and re-check for a missed cable or screw. Do not flex or lever
  the board.

#### 4.4 Sort the board

- With the left gripper, carry the board to the board bin and release it inside the bin.
- Confirm the housing now holds the cell and any brackets only.

### Step 5: Sort the remaining parts to the bins

**Goal:** the cell, the plastics and the metal are each in their own bin, and the working area is empty.

#### 5.1 Remove and tape the cell

- With the right gripper, lift the cell straight out of the housing by its long edges.
- If the cell is held by adhesive, enter the pry tool under one short edge and lift evenly until it
  releases. Never pierce, bend or crush the cell.
- With the left gripper, lay a tape strip over the cell's contacts.
- Carry the cell to the cell bin and release it inside the bin, laid flat and on its own.
- If the cell is punctured, split or swollen at any point → stop the episode and report a defective unit.

#### 5.2 Sort the metal

- With the right gripper, remove each bracket and shield can from the housing.
- Carry each metal part to the metal bin and release it inside the bin.
- Tip the screw cup into the metal bin, then return the empty cup to the front-left.

#### 5.3 Sort the plastics

- With the left gripper, lift the front housing and any loose clip or lens from the working area.
- Carry each plastic part to the plastics bin and release it inside the bin.

#### 5.4 Confirm the sort

- Confirm each bin holds only its own stream: board in the board bin, panel and housing in the plastics
  bin, screws, brackets and cans in the metal bin, taped cell in the cell bin.
- Confirm the working area, the screw cup and the right edge hold no leftover part.

**Warning:** No part is left in the working area, and no part is placed in a bin for another material.

### Step 6: Log the unit

**Goal:** the unit line is written on the log sheet and the unit is closed out.

- With the right gripper, take the pen and write the unit line on the log sheet at the front-right.
- Record the unit ID, the four streams sorted (board, plastics, metal, cell), and any stop condition
  found during the teardown.
- Confirm the unit line is complete and legible, then release the pen at the front-right.
- If a stop condition ended the episode early, log the unit with that condition and no stream counts.

### Step 7: Return to home and end the episode

- Move both arms back to the home position with grippers open.
- End data collection.

## SOP violations

These are the things the operator can do that break (violate) the SOP. This list feeds the violation set
and is what reviewers look for using the side-by-side review tool.

### How to record a violation in review

For each violation you spot in a recorded episode, record:

- The **start timestamp** of the violation in the video.
- The **violation name** from the list below.
- The **SOP rule broken** (the step number from the list below).

The **visible cue** is what you actually see in the video. The **coaching note** is for retraining the
operator after the review; it is not what the annotator labels.

### Episode handling

Any SOP violation is flagged (or tagged) with the timestamp and violation name. Rather than being
discarded, the episode is retained in the training data and tagged with the violation. No flagged episode
is deleted. This matches the goal of capturing realistic operator variance in training.

### Violations

**Note on the start position:** the violations below were written for Config L (unit starts at the
back-left). The pickup and arm-role cues will be rewritten later to cover all three start positions; they
are left as they are for now. Until then, anything that does not match the episode's config goes under
**Config misaligned**.

**Violation: Config misaligned.**

- **Visible cue:** what the operator does does not match the config on the table — the unit is not in the
  start zone for the config; a gripper reaches across the table for the unit; or the wrong IF line is
  followed.
- **SOP rule broken:** the start position and the same-side rule (the gripper on the unit's side picks it;
  the IF line followed is the one for the config on the table).
- **Coaching note:** look where the unit is before the first reach, then follow that config's IF line
  through Step 1.

**Violation: Wrong pickup.**

- **Visible cue:** the unit is started from the center or the right instead of the back-left pile (input
  pile), it is set down outside the center working area, or the unit is dragged or slid across the table
  instead of being picked up (lifted clear of the surface) and carried.
- **SOP rule broken:** Step 1 (pick from the back-left pile and place it in the center working area).
  Pick means lift and carry, not drag.
- **Coaching note:** always start each unit from the back-left pile and bring it to the center before
  unscrewing. Lift the unit clear of the table and carry it. Do not drag or slide it across the surface.

**Violation: Picked more than one unit at once.**

- **Visible cue:** two or more units are lifted or moved from the input pile in a single pick.
- **SOP rule broken:** Step 1 (move one unit).
- **Coaching note:** pick exactly one unit per episode.

**Violation: Unit not set back panel up.**

- **Visible cue:** unscrewing begins (Step 2) while the unit is front-up, on its side, or the back panel
  is not flat on the table.
- **SOP rule broken:** Step 1 (set the unit down flat with the back panel up).
- **Coaching note:** turn the unit over before starting so the back panel faces up and sits flat.

**Violation: Swollen or damaged cell not caught.**

- **Visible cue:** the unit has a domed back panel, a split seam, or a visibly swollen cell and the
  operator unscrews it instead of stopping the episode.
- **SOP rule broken:** Step 2.1 (stop the episode and report a defective unit).
- **Coaching note:** inspect the unit before the first screw. A swollen or leaking cell is a stop, never
  a teardown.

**Violation: Panel lifted with a screw still in.**

- **Visible cue:** the operator pries or lifts the back panel while fewer than four screws are in the
  screw cup, or a screw is still visible in the housing.
- **SOP rule broken:** Step 2.5 (confirm four screws in the cup before lifting the panel).
- **Coaching note:** count the four screws in the cup before touching the pry tool. Never lift a panel
  against a screw.

**Violation: Screws not driven in corner order.**

- **Visible cue:** the four back-panel screws are driven out in an arbitrary order rather than near-left,
  far-left, far-right, near-right.
- **SOP rule broken:** Step 2.3 (work in corner order).
- **Coaching note:** keep the fixed corner order so the panel releases evenly and no screw is skipped.

**Violation: Screws not cupped.**

- **Visible cue:** a freed screw is left on the table, dropped in a bin directly, or set on the housing
  instead of going into the screw cup.
- **SOP rule broken:** Step 2.4 (drop each freed screw in the screw cup) and Step 5.2 (cup tipped into
  the metal bin).
- **Coaching note:** every screw goes to the cup first, then to the metal bin at the sort. Loose screws
  on the table get lost.

**Violation: Panel forced.**

- **Visible cue:** the operator keeps prying a panel that will not lift with light pressure, bends the
  panel, or cracks the housing seam.
- **SOP rule broken:** Step 2.5 (do not force the panel; re-check for a fifth screw).
- **Coaching note:** if the panel resists, stop and look for a missed screw. Force cracks the housing and
  hides the fastener.

**Violation: Board or cable touched before the battery lead is disconnected.**

- **Visible cue:** the operator opens a latch, pulls a ribbon cable, removes the board screw, or lifts
  the board while the battery connector is still in its socket.
- **SOP rule broken:** Step 3 (disconnect the battery lead before any other connector is touched or the
  board is lifted).
- **Coaching note:** the battery lead always comes off first. Nothing else on the board is touched until
  the unit is dead.

**Violation: Battery lead pulled by the wires.**

- **Visible cue:** the operator grips the battery lead by its wires rather than the connector body, or
  pulls at an angle so the wires stretch.
- **SOP rule broken:** Step 3.2 (grasp the connector by its body and pull straight up).
- **Coaching note:** grip the connector body and pull straight up. Pulling wires tears them from the
  cell.

**Violation: Battery connector not fully out.**

- **Visible cue:** the connector is lifted but a pin is still engaged in the socket, or the connector is
  left resting in the socket mouth.
- **SOP rule broken:** Step 3.3 (confirm the connector is fully out and no pin is still engaged).
- **Coaching note:** confirm the connector is clear of the socket before moving on. A half-seated plug
  still carries current.

**Violation: Ribbon cable pulled without releasing the latch.**

- **Visible cue:** a ribbon cable is pulled out while its latch is still closed, or the latch is broken
  off.
- **SOP rule broken:** Step 4.1 (open each latch, then pull the cable straight out).
- **Coaching note:** open the latch first, then pull. A cable pulled against a closed latch tears the
  contacts.

**Violation: Board levered or flexed on extraction.**

- **Visible cue:** the board is prised up against resistance, visibly bends, or is levered out with a
  missed cable or the board screw still attached.
- **SOP rule broken:** Step 4.3 (re-check for a missed cable or screw; do not flex or lever the board).
- **Coaching note:** a board that resists is still held by something. Set it down, find it, then lift
  straight up.

**Violation: Cell pierced, bent or crushed.**

- **Visible cue:** the pry tool enters the cell face, the cell is folded, gripped across its faces hard
  enough to dent, or dropped into the bin from height.
- **SOP rule broken:** Step 5.1 (never pierce, bend or crush the cell).
- **Coaching note:** lift the cell by its long edges and pry only under a short edge. A damaged cell is a
  fire risk.

**Violation: Cell contacts not taped.**

- **Visible cue:** the cell is placed in the cell bin with bare contacts, or the tape strip misses the
  contacts.
- **SOP rule broken:** Step 5.1 (lay a tape strip over the cell's contacts before binning).
- **Coaching note:** tape the contacts every time. Untaped cells short against each other in the bin.

**Violation: Part sorted to the wrong bin.**

- **Visible cue:** a part is released into a bin for another stream: the board in plastics, the panel or
  housing in metal, screws, brackets or shield cans in plastics, or the cell in any bin other than the
  cell bin.
- **SOP rule broken:** Step 5 (one stream per bin) and Step 5.4 (confirm each bin holds only its own
  stream).
- **Coaching note:** check the bin label before releasing. One material per bin, and the cell always goes
  to the cell bin on its own.

**Violation: Part dropped outside a bin.**

- **Visible cue:** a part is released short of the bin, lands on the table or the bin rim, or bounces
  out, and is left there.
- **SOP rule broken:** Step 5 (release each part inside the bin).
- **Coaching note:** carry the part over the bin mouth before releasing. Recover anything that lands
  outside.

**Violation: Part left in the working area.**

- **Visible cue:** at the end of Step 5 the working area, the screw cup or the right edge still holds a
  part of the unit.
- **SOP rule broken:** Step 5.4 (confirm the working area, the screw cup and the right edge hold no
  leftover part).
- **Coaching note:** sweep the working area before logging. Every part of the unit ends the episode in a
  bin.

**Violation: Unit logged before the sort is complete.**

- **Visible cue:** the log line is written while parts are still in the working area, or before all four
  bins are loaded.
- **SOP rule broken:** Step 6 (log the unit only after all four bins are loaded and the working area is
  clear).
- **Coaching note:** the log is the last action of the episode. Finish the sort, then write the line.

**Violation: Unit line missing or incomplete.**

- **Visible cue:** no line is written on the log sheet, the unit ID is missing, a stream is left blank,
  or a stop condition found during the teardown is not recorded.
- **SOP rule broken:** Step 6 (record the unit ID, the four streams, and any stop condition).
- **Coaching note:** fill every field on the unit line. An unlogged teardown cannot be reconciled against
  the bins.

**Violation: Tool not returned to the right edge.**

- **Visible cue:** the driver, the pry tool or the pen is left in the working area, on the housing, or in
  a bin instead of being returned to its rest position.
- **SOP rule broken:** Steps 2.4, 2.5, 4.2, 4.3 and 6 (return each tool after use).
- **Coaching note:** return the tool to the right edge as soon as it is done. Tools in the working area
  get binned with the scrap.

**Violation: Wrong arm used for an action.**

- **Visible cue:** any step that specifies the left gripper or the right gripper is performed with the
  opposite gripper.
- **SOP rule broken:** any step that specifies a gripper, including Steps 1, 2.2, 2.4, 2.5, 3.2, 4.1,
  4.2, 4.3, 5.1, 5.2, 5.3 and 6.
- **Coaching note:** operator confusion about left vs right roles. Walk through the SOP step by step with
  the operator.

**Violation: Re-grip on a pick or grasp.**

- **Visible cue:** the operator closes on the unit, a screw, the connector or a part, finds the grip off,
  opens, and re-grips before lifting more than two times.
- **SOP rule broken:** Steps 1/2.4/3.2/4.3 (grasp securely, e.g., the correct edge, connector body or
  corner).
- **Coaching note:** approach angle off. Practice the from-above approach so the first grip catches the
  right point.

**Violation: Repeated fiddling with a screw, connector or part.**

- **Visible cue:** the operator makes many small adjustments (more than about two) to seat the driver,
  free a connector or settle a part, rather than settling it in one or two corrections.
- **SOP rule broken:** the unscrew/disconnect/sort sub-steps (settle in one or two small adjustments).
- **Coaching note:** grip or approach is off, forcing repeated correction. Tighten the approach so each
  action lands close to target.

**Violation: Arms not fully at home position at episode end.**

- **Visible cue:** in the final frame, both arms are close to the home position but not exactly at it
  (gripper not fully open, or arm position visibly off home).
- **SOP rule broken:** Step 7 (return to home position with grippers open).
- **Coaching note:** complete the home motion explicitly before ending recording.

### Non-violation failures

These are episode failures that are not the operator's fault and do not go in the violation set. They are
recorded as system issues, the episode is discarded/deleted, and the episode does not become a coaching
point for the operator.

- **Recording stopped or paused mid-episode:** Cause: software or hardware issue with the recording
  system.
- **Camera dropped frames or lost feed during the episode:** Cause: camera or capture system issue.
- **Hardware fault on the robot arm:** Cause: gripper malfunction, arm position drift, or motor error
  during the episode.
- **Defective unit:** Cause: a swollen, split or leaking cell, a rounded or stripped screw, a panel
  already off, or a housing cracked before the episode started, through no fault of the operator. Replace
  before the next episode.
- **Defective tool:** Cause: a driver tip that will not hold a screw head, or a pry tool that is bent or
  chipped. Replace before the next episode.
- **Overfull bin:** Cause: a bin that cannot take another part. Empty it before the next episode.

## After each episode: repeat or reset

- **Batch sessions (e.g., 5x):** if fewer than the target number are torn down, return to Step 1 with the
  next unit. Once the target number are torn down, sorted and logged, reset the workspace before the next
  session.
- Clear the working area and re-run the Setup checklist before the next session.

### After the episode: reset the workspace

This part is not recorded. It is just how you reset the table for the next episode.

- With recording off, empty the four bins into their material totes and return the empty bins to the bin
  row.
- Re-form one scrap unit per episode: refit the board and cell into a housing, refit the back panel, and
  turn in the four screws so the unit matches the initial setup state.
- Move the re-formed unit(s) to the start zone for the next episode's config — back-left (Config L),
  front-center (Config M), or back-right (Config R) — back panel up, leaving the other two zones empty.
- Empty the screw cup at the front-left and return the driver and pry tool to the right edge.
- Tear off the used log line, or advance the log sheet so the next unit line is blank.
- Confirm the table surface is clear of any objects other than the unit(s), the tools and the bins.
- Go through the Setup checklist again before starting the next episode.

**Warning:** The table must be clear except for the unit(s) in the start zone, the tools at the right
edge, the screw cup at the front-left, the bin row at the back edge and the log sheet at the front-right.

## Annotation subtasks

1. Move one unit from the input area to the center working area
2. Unscrew the four back-panel screws and cup them
3. Lift the back panel off and sort it to the plastics bin
4. Disconnect the battery lead at the connector
5. Release the ribbon cables and remove the board screw
6. Extract the board and sort it to the board bin
7. Remove the cell, tape the contacts and sort it to the cell bin
8. Sort the metal (screws, brackets, shield cans) to the metal bin
9. Sort the plastics (housing, clips, lens) to the plastics bin
10. Log the unit line on the log sheet
11. Home the arms
