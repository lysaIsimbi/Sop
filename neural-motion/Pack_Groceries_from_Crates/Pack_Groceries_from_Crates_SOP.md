# Pack Groceries from Crates SOP

This SOP covers packing groceries out of two labeled source crates into two bags, loading the
non-fragile groceries first and the fragile ones on top, using a two-arm robot system. The episode ends with every grocery in its bag and both
crates empty. The bags are not folded, closed, or moved — they stay standing open where they were
packed.

**Crate 1 packs into Bag A and Crate 2 packs into Bag B.** A grocery never crosses between crates or
bags, so no destination is ever chosen — only the order items are loaded in.

Both bags begin open and upright in their own marked positions and never move. Groceries go in **one
at a time**: fill Bag A completely from Crate 1 and check it, then do the same for Bag B from
Crate 2.

Both bags stand in the middle of the table with a crate outside each one. **Each arm lifts groceries
from the crate on its own side, and the opposite arm holds the bag open.** So Bag A is loaded by the
left gripper out of Crate 1 and held by the right gripper, and Bag B is loaded by the right gripper
out of Crate 2 and held by the left gripper.

A session is two crates holding a variable number of approved groceries, recorded in the session
manifest as a total of **N** with the handling class and handling attributes of every item and the
expected count per crate.

This is the reverse of the Unpack Groceries and Sort to Crates SOP.

## Setup

Go through both checklists before starting the episode.

### Hardware checklist

- [ ] Cameras are on and recording
- [ ] Env camera frame includes both crate openings and labels, both bag positions and mouths, and
  both grippers
- [ ] Both arms are at the home position with grippers open
- [ ] Table surface is clean, dry, stable, and clear of unrelated objects
- [ ] Both crates and both bags are stable and fully reachable
- [ ] Each crate and the bag beside it are reachable by that side's loading arm, and each bag is
  reachable by the opposite arm for holding

### Materials checklist

- [ ] Bag A stands open, empty, and upright in its marked center-left position; Bag B stands open,
  empty, and upright in its marked center-right position
- [ ] Each bag holds its own shape open without support and stands clear of its crate and the other
  bag
- [ ] Crate 1 sits on the left of the table and Crate 2 on the right, outside the two bags, both
  open, stable, and visibly labeled
- [ ] Crate 1 holds only the Bag A groceries; Crate 2 holds only the Bag B groceries
- [ ] Inside each crate, groceries are grouped into two marked lanes — non-fragile and fragile —
  running front to back
- [ ] The session manifest lists every grocery, its handling class, its handling attributes, the
  count per crate, and the total count N
- [ ] The two crates together hold exactly the N manifest items, and each crate is nonempty
- [ ] Each grocery sits in the orientation it will be packed in, on its widest flat face where it
  has one, without touching another grocery
- [ ] Every item is within the tested gripper payload and size limits and fits through the crate and
  bag openings
- [ ] Each bag can hold its crate's groceries with the contents sitting below the bag rim
- [ ] All packages are closed, dry, undamaged, and free from leaks
- [ ] Produce is clean, dry, sound, and free from loose dirt
- [ ] No item is hot, open, leaking, sharp, hazardous, contaminated, excessively fragile, or
  ambiguous

### Workspace layout

- **Left side:** Crate 1, the Bag A source
- **Center-left:** Bag A, open and upright, beside Crate 1
- **Center-right:** Bag B, open and upright, beside Crate 2
- **Right side:** Crate 2, the Bag B source

Each bag sits directly beside its own crate, so every loaded move is short and stays on that arm's
own side of the table. Neither bag ever leaves its marked position. The visible crate label
determines which bag its groceries belong to, and crate position is only a supporting cue.

### Arm assignments

Each arm loads from the crate on its own side; the opposite arm holds the bag.

- **Bag A:** the **left gripper** lifts groceries from Crate 1 and lowers them into Bag A. The
  **right gripper** holds Bag A open and steady.
- **Bag B:** the **right gripper** lifts groceries from Crate 2 and lowers them into Bag B. The
  **left gripper** holds Bag B open and steady.

Each loading arm stays on its own side of the table, so no loaded grocery crosses the workspace. The
holding arm reaches in from the opposite side, so the two arms approach the bag mouth from opposite
directions and never contest the same space. The holding gripper never lifts a grocery.

## Vocabulary

These are the terms used in this SOP. Annotators must use this language consistently.
One term per concept, used throughout.

### Handling classes

Handling class decides **where in the bag** an item goes. It is assigned by the setup crew before
recording and recorded on the manifest, so nothing is judged mid-episode.

- **Non-fragile grocery:** an item that holds its shape under the weight of the rest of the bag.
  Examples include sealed bottles and cartons, cans, glass jars, sealed bags of rice, flour, or
  sugar, boxed dry goods, sealed multipacks, firm sealed tubs, and firm or netted vegetables.
- **Fragile grocery:** an item that crushes, bruises, cracks, or deforms under load and can carry no
  weight. Examples include eggs, bread and bakery items, snack bags, soft fruit, soft-skinned
  vegetables, leafy greens and florets, and single thin-walled cups.
- **Handling attributes:** manifest notes such as crushable, leak-prone, keep upright, rollable, or
  flexible that change how an item is grasped and released, not which layer it enters.
- **Crushable grocery:** an item damaged by grip force or by load placed on it.
- **Leak-prone grocery:** a closed container that must stay upright to protect its cap, lid, or
  seal.
- **Approved grocery:** an item accepted for the session because its handling class is unambiguous,
  its package or surface is safe and intact, and its mass and dimensions are within the tested
  robot, crate, and bag limits.
- **Session manifest:** the setup record listing all N items, each item's handling class and
  handling attributes, and the expected count in each crate.

### Bag and crate components

- **Crate 1 / Crate 2:** the two source crates, emptied in that order. Crate 1 packs into Bag A;
  Crate 2 packs into Bag B.
- **Lane:** one of the two marked areas inside a crate holding that crate's non-fragile or fragile
  groceries.
- **Bag A / Bag B:** the two bags, packed in that order.
- **Active bag:** the bag currently being packed. The other bag is left untouched until its turn.
- **Bag mouth:** the top opening through which groceries are loaded.
- **Non-fragile layer:** all of a bag's non-fragile groceries, resting on the bag base.
- **Fragile layer:** all of a bag's fragile groceries, resting side by side on top of the
  non-fragile layer with nothing above them.
- **Rim clearance:** the packed contents sit below the bag rim, with no item protruding above it or
  leaning on it.

### Actions

- **Stabilize:** hold the active bag by a clear upper edge, handle, or side so it stays upright and
  open throughout loading.
- **Select:** choose the next grocery from the lane the current layer calls for.
- **Lift:** grasp one grocery and raise it clear of the crate without catching another item.
- **Place:** lower the grocery through the bag mouth onto the current layer and release it only once
  it is supported.
- **Seat:** settle an item flat so it does not rock, stand on edge, or press the bag wall outward.

### Handling standard

- Move exactly one grocery per pick. Lift it clear of the crate, carry it level, lower it into the
  bag, and release only once it is supported.
- Grip fragile and crushable groceries lightly. Never squeeze one to hold a slipping grasp — set it
  back down in its lane, release, and regrasp.
- Do not rotate a grocery in the air. If an item needs a different orientation, set it flat in its
  lane, release, regrasp, and lift again.
- Keep leak-prone groceries upright from lift through release.
- Never drag a grocery across the crate or force one past an item already in the bag.

## Steps

**Fill Bag A completely before touching Crate 2 or Bag B.** Step 1 packs one bag, Step 2 packs the
other, and Step 3 ends the episode. Within a bag, load the whole non-fragile layer first, then the
fragile layer on top of it.

Each step ends with a **Check** — the state the workspace has to be in before moving on. It is
something already visible in the workspace, not a separate inspection action.

### Step 1: Pack the Crate 1 groceries into Bag A

**Goal:** every grocery in Crate 1 is moved one at a time into Bag A, non-fragile first and fragile
on top.

- With the **right gripper**, hold Bag A open at a clear upper edge, handle, or side, reaching in
  from the right.
- Keep that hold from the first pick until the last grocery is supported, reopening or restabilizing
  the bag whenever it starts to close or lean.
- Keep the right gripper clear of the bag mouth so the left gripper has an open loading path.

#### 1.1 Select the next grocery

- Work one layer at a time: empty the **non-fragile lane** first, then the **fragile lane**.
- Select one accessible grocery from the current lane without digging under, trapping, or lifting
  another item.
- Take groceries only from Crate 1. Do not reach into Crate 2 or touch Bag B.
- Confirm the item's handling attributes on the manifest before grasping.

#### 1.2 Grasp and lift the grocery

- With the **left gripper**, grasp a secure part of the grocery body.
- Do not grasp a cap, lid, seal, thin film, unsupported package corner, or produce stem.
- Use the minimum force needed to hold the item securely.
- If the grasp is unstable, return the item to its lane and perform one deliberate re-grasp.

#### 1.3 Place the grocery in Bag A

- Carry the grocery level along a clear path to the bag mouth.
- Lower it into the bag onto the current layer — non-fragile groceries onto the bag base or onto the
  non-fragile items already there, fragile groceries side by side on top of the non-fragile layer.

#### 1.4 Complete each layer before the next

- Repeat Steps 1.1 through 1.3 for one grocery at a time until the current lane is empty.
- **Non-fragile layer check:** every non-fragile grocery sits flat and stays still, none standing on
  edge or pressing the bag wall outward, and the layer is level enough to carry the fragile items.
- **Fragile layer check:** every fragile grocery is undeformed, side by side rather than stacked,
  free of pressure from the bag wall, with nothing above it.
- Reseat one failed item per lane before moving to the next one.
- Leave Bag A standing open where it is. Do not fold, close, or move it.

**Check:** both lanes of Crate 1 are empty, including its base and corners. Bag A holds the Crate 1
manifest count, with the non-fragile groceries below and the fragile ones side by side on top,
nothing above them, and the contents below the bag rim. Bag A still stands open in its marked
position.

### Step 2: Pack the Crate 2 groceries into Bag B

**Goal:** every grocery in Crate 2 is packed into Bag B the same way, with the arm roles mirrored.

- With the **left gripper**, hold Bag B open at a clear upper edge, handle, or side, reaching in
  from the left and keeping that hold throughout loading.
- With the **right gripper**, perform Steps 1.1 through 1.4 drawing only from **Crate 2**,
  non-fragile lane first and fragile lane second.
- Move and place exactly one grocery at a time.
- Do not disturb packed Bag A or reach into Crate 1.
- Leave Bag B standing open where it is. Do not fold, close, or move it.

**Check:** the same conditions as Step 1, for Crate 2 and Bag B.

### Step 3: Return to home and end the episode

- Move both arms back to the home position with grippers open.
- End data collection only after both arms are fully home.

**Expected end state:** all N groceries are bagged, each bag holding its own crate's count. Both
crates are empty and stable in their marked positions with labels visible. Both bags stand upright
and open where they were packed, fragile groceries on top, contents below the rim. No package is
open, leaking, or crushed and no produce is visibly bruised.

## After the episode: reset the workspace

### Check the completed task

- Both bags packed: all N manifest groceries are bagged, the two bag counts sum to N, both bags
  stand upright and open in their marked positions, both crates are empty, and both arms are home.
- If the task stopped because of a Critical violation or non-violation failure, quarantine the
  affected grocery or equipment and follow the data-pipeline rule before resetting.

### Reset the workspace

This part is not recorded. It is just how you reset the table for the next session. With recording
off:

- Return every grocery from both bags to its crate.
- Inspect every grocery and replace any package or produce item that is damaged, leaking, bruised,
  or spoiled.
- Replace any bag that no longer stands open on its own or has a torn handle or wall.
- Select the next approved grocery set from the data-collection coverage plan and create its session
  manifest.
- Assign each item a handling class, and record every item's class, handling attributes, per-crate
  count, and total N.
- Load the Bag A groceries into Crate 1 and the Bag B groceries into Crate 2, grouped into the
  non-fragile and fragile lanes.
- Confirm each crate's fragile items can sit side by side in one bag layer, and that each bag can
  hold its crate with the contents below the rim.
- Vary the item types, package types, size, shape, weight, fragile-to-non-fragile mix, and lane
  arrangement according to the coverage plan.
- Stand Bag A open and empty in its marked center-left position, beside Crate 1, and Bag B open and
  empty in its marked center-right position, beside Crate 2.
- Return Crate 1 to the left side and Crate 2 to the right side with labels facing the camera.
- Remove all unrelated objects from the table.

### Reverify setup

Run through the Setup checklist again before starting the next episode.

## SOP violations

These are the things that break (violate) the SOP. This list feeds the violation
set and is what reviewers look for using the side-by-side review tool.

### How to record a violation in review

For each violation you spot in a recorded episode, record:

- The start timestamp of the violation in the video.
- The violation name from the list below.
- The SOP rule broken (the step number from the list below).

The visible cue is what you actually see in the video. The coaching note is for retraining after
the review; it is not what the annotator labels.

### Episode handling

Any SOP violation is flagged (or tagged) with the timestamp and violation name. Rather than being
discarded, the episode is retained in the training data and tagged with the violation. No flagged
episode is deleted. This matches the goal of capturing realistic variance in training.

### Violations

A Critical violation should be flagged or tagged with the timestamp and name; episode handling
follows the applicable data-pipeline rule.

**Violation: Unsafe or unsupported grocery included (Critical).**

- **Visible cue:** the episode starts or continues with an item that is hot, open, leaking, sharp,
  hazardous, contaminated, outside validated mass or size limits, or unable to fit through the crate
  or bag opening.
- **SOP rule broken:** Steps 1 and 2, only groceries that pass the acceptance criteria are packed.
- **Coaching note:** remove or replace the item during recording-off setup; never test an
  unvalidated grocery in a recorded episode.

**Violation: Bag B started before Bag A was complete.**

- **Visible cue:** Crate 2 or Bag B is touched or loaded before Bag A is fully packed.
- **SOP rule broken:** Steps 1 and 2 (complete Bag A before starting Bag B).
- **Coaching note:** finish packing Bag A before touching Crate 2.

**Violation: Grocery taken from the wrong crate.**

- **Visible cue:** an item from Crate 2 is loaded into Bag A, an item from Crate 1 is loaded into
  Bag B, or a gripper reaches into the crate not assigned to the active bag.
- **SOP rule broken:** Steps 1.1 and 2, Crate 1 packs into Bag A and Crate 2 packs into Bag B.
- **Coaching note:** draw only from the crate assigned to the bag being packed.

**Violation: Layer order not followed.**

- **Visible cue:** a fragile grocery is loaded before the non-fragile lane is empty, or an item is
  drawn from a lane out of turn.
- **SOP rule broken:** Steps 1.1 and 1.4 (empty the non-fragile lane, then the fragile lane).
- **Coaching note:** clear the whole non-fragile lane before touching the fragile one.

**Violation: Fragile grocery not left on top or loaded under weight (Critical if the item is
damaged).**

- **Visible cue:** a fragile grocery ends up below the non-fragile layer, stacked under another
  fragile item, pressed against the bag wall, or with any item resting on it.
- **SOP rule broken:** Step 1.3 and the Step 1.4 fragile layer check (fragile groceries side by side
  on top of the non-fragile layer with nothing above them).
- **Coaching note:** keep the fragile layer flat and single, and load nothing after it.

**Violation: More than one grocery handled at once.**

- **Visible cue:** the gripper traps, lifts, carries, or releases two or more groceries together.
- **SOP rule broken:** Steps 1 and 2, pack one grocery at a time.
- **Coaching note:** isolate one accessible grocery and complete its placement before selecting
  another.

**Violation: Wrong arm used for an action.**

- **Visible cue:** Bag A is loaded by the right gripper or held by the left; Bag B is loaded by the
  left gripper or held by the right; or the holding gripper lifts a grocery.
- **SOP rule broken:** Steps 1 and 2, each arm loads from the crate on its own side and the opposite
  arm holds the bag.
- **Coaching note:** left loads Bag A and right holds it; right loads Bag B and left holds it.

**Violation: Active bag not held open during loading.**

- **Visible cue:** the holding gripper releases the bag while a grocery is being lowered, the bag
  collapses, tips, or closes around an item, or the holding gripper blocks the loading path across
  the bag mouth.
- **SOP rule broken:** Steps 1 and 2 (hold the bag open throughout loading and keep the holding
  gripper clear of the mouth).
- **Coaching note:** keep the hold until each item is supported, and hold from the edge rather than
  over the opening.

**Violation: Other crate, other bag, or packed bag disturbed.**

- **Visible cue:** the crate or bag not in use is nudged, shifted, or reached over before its turn;
  a lane is dug through or mixed; a crate shifts, tips, or has its label obscured; or a packed bag
  is nudged, toppled, or unloaded.
- **SOP rule broken:** Steps 1.1 and 2 (leave the other side untouched until its turn and preserve
  completed work).
- **Coaching note:** take the top accessible item from the current lane and route both arms clear of
  everything else.

**Violation: Delicate feature used as the primary grasp.**

- **Visible cue:** a grocery is lifted by a cap, lid, seal, thin film, unsupported package corner,
  or produce stem.
- **SOP rule broken:** Step 1.2 (use a secure body grasp).
- **Coaching note:** grasp a stable body area that will not open, tear, leak, or bruise.

**Violation: Excessive grip force or grocery damage (Critical if leaking or broken).**

- **Visible cue:** packaging dents or opens, produce bruises, a fragile item compresses, glass
  breaks, or liquid leaks.
- **SOP rule broken:** Step 1.2, use the minimum secure force and a light grip on fragile groceries.
- **Coaching note:** reduce grip force, choose a stronger grasp area, and stop if a package leaks or
  breaks.

**Violation: Grocery reoriented in the air.**

- **Visible cue:** the gripper turns, tips, or rolls a grocery while it is off the crate instead of
  setting it down and regrasping.
- **SOP rule broken:** Steps 1 and 2, set the item flat in its lane, release, and regrasp to change
  orientation.
- **Coaching note:** put the item back in its lane before changing your grip.

**Violation: Grocery dragged, snagged, or forced into the bag.**

- **Visible cue:** an item scrapes the crate rim or table, catches a handle or fold, or is pushed
  past an item already in the bag.
- **SOP rule broken:** Step 1.3, lift clear of the crate and lower through a clear bag mouth.
- **Coaching note:** reopen the bag, choose a clear path, and lower without force.

**Violation: Grocery dropped or collision during transport.**

- **Visible cue:** the grocery falls or strikes a crate, bag, work surface, robot, or another
  grocery.
- **SOP rule broken:** Steps 1.2 and 1.3 (stable grasp and a level carry along a clear path).
- **Coaching note:** confirm the hold before transport and maintain clearance.

**Violation: Grocery released before it is supported.**

- **Visible cue:** an item is dropped into the bag from above the mouth, released while still
  leaning on the gripper, or left rocking on the layer below.
- **SOP rule broken:** Steps 1 and 2, release only once the item is supported.
- **Coaching note:** lower to a supported space and confirm the item settles before opening the
  gripper.

**Violation: Leak-prone grocery left unstable.**

- **Visible cue:** a bottle, carton, cup, or similar container is packed on its side, inverted,
  leaning, or unsupported.
- **SOP rule broken:** Steps 1 and 2, keep leak prone groceries upright from lift through release.
- **Coaching note:** preserve upright orientation and confirm stability before retracting.

**Violation: Retry limit exceeded.**

- **Visible cue:** a grocery is regrasped more than once after an unstable hold, more than one item
  is reseated in the same lane, or the same pick or placement is reattempted repeatedly.
- **SOP rule broken:** Step 1.2 (one deliberate re-grasp) and Step 1.4 (reseat one failed item per
  lane).
- **Coaching note:** improve the first approach and stop the episode after the allowed recovery
  fails.

**Violation: Grocery left in a crate.**

- **Visible cue:** a grocery remains in a lane, crate corner, or crate base after the episode moves
  on to the other crate or to home.
- **SOP rule broken:** Steps 1 and 2 (empty both lanes of the crate).
- **Coaching note:** clear every lane and corner before leaving a crate.

**Violation: Bag overfilled or rim clearance missing.**

- **Visible cue:** an item protrudes above the bag rim, leans on it, or is forced in once the bag is
  full, and the episode continues without it being corrected.
- **SOP rule broken:** Steps 1 and 2 (keep the packed contents below the bag rim).
- **Coaching note:** seat each item down into the bag and stop loading a bag that is full.

**Violation: Packed bag folded, closed, or moved.**

- **Visible cue:** a bag is folded shut, tipped, lifted, slid, or repositioned at any point, or the
  episode ends with a bag away from its marked position.
- **SOP rule broken:** Steps 1 and 2 (leave each packed bag standing open where it was packed).
- **Coaching note:** the task ends at packed — do not close or carry the bags.

**Violation: Episode ended in an incorrect final state.**

- **Visible cue:** the final frames show a grocery left in a crate or on the table, a grocery in the
  wrong bag, a bag count that does not match its crate's manifest count, or a bag fallen,
  overfilled, or moved from its marked position.
- **SOP rule broken:** Step 3 expected end state (both crates empty, both bags packed and upright
  where they stand).
- **Coaching note:** put every grocery in its own crate's bag and leave both bags standing as
  packed.

**Violation: Arms not fully at home at episode end.**

- **Visible cue:** either arm is visibly off home or either gripper remains closed in the final
  frame.
- **SOP rule broken:** Step 3 (return both arms home with grippers open).
- **Coaching note:** complete the home motion explicitly before ending recording.

**Violation: Human intervention in the recorded workspace (Critical).**

- **Visible cue:** a human hand touches or repositions a grocery, bag, crate, label, or robot during
  recording.
- **SOP rule broken:** Steps 1 to 3, the recorded task is completed entirely by the robot.
- **Coaching note:** stop and reset; keep all recorded corrections robotic and visible.

**Violation: Episode paused, cut, restarted, or corrected off-camera.**

- **Visible cue:** the recording contains an intentional pause, splice, discontinuity, hidden
  correction, or restarted attempt.
- **SOP rule broken:** Steps 1 to 3, the session is one continuous recorded episode.
- **Coaching note:** record both bags without intentional interruption and keep recoveries visible.

**Violation: Required action or label not visible.**

- **Visible cue:** the active grocery, gripper, bag mouth, or crate opening or label leaves the
  env-camera view.
- **SOP rule broken:** Steps 1 to 3, every action and every label stays visible in frame.
- **Coaching note:** keep every lift and placement camera-verifiable.

### Non-violation failures

These are episode failures that are not caused by how the task was run and do not go in the violation set. They
are recorded as system issues, the episode is discarded or deleted, and the episode does not become a
coaching point.

- **Recording stopped or paused mid-episode:** software or hardware issue with the recording system.
- **Camera dropped frames or lost feed during the episode:** camera or capture-system issue.
- **Hardware fault on the robot arm:** gripper malfunction, arm-position drift, or motor error
  during the episode.
- **Defective grocery:** an item was already leaking, spoiled, damaged, or mislabeled through no
  fault of the way the task was run.
- **Defective bag:** a bag was already torn, wet, or unable to stand open and hold its shape as
  specified, or it collapsed under a correctly placed grocery.
- **Defective crate or label:** a crate collapsed or a label detached without a gripper touching it.
- **Incorrect supplied manifest:** the controlled manifest contained a wrong item identity, handling
  class, handling attribute, or expected count through no fault of the way the task was run.

## Annotation subtasks (from SOP)

1. Pack the Crate 1 non-fragile layer into Bag A
2. Pack the Crate 1 fragile layer into Bag A
3. Pack the Crate 2 non-fragile layer into Bag B
4. Pack the Crate 2 fragile layer into Bag B
5. Return both arms home and end the episode
