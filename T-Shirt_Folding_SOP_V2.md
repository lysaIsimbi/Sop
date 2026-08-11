# T-Shirt Folding SOP (Men's or Women's)

This SOP covers folding a single short-sleeve t-shirt (men's or women's) into a clean folded bundle using a two-arm robot system. Both arms are used throughout: the grippers cooperate to lift, straighten, tension, and fold the t-shirt, with the left and right grippers taking the specific roles called out in each step. The task runs from a crumpled t-shirt at the back-left of the table to a folded t-shirt (or folded stack) at the back-right.

What stays constant across all sessions:

- **Working position:** the t-shirt is always moved to the centre of the table before straightening and folding.
- **Straighten target:** every t-shirt must lie flat, **face down, with the collar on the right** before any folding begins.
- **Fold order:** the near side is folded first, then the far side, then the collar end is folded down to meet the hem to complete the fold.

## Setup

Go through both checklists before starting the episode.

### Hardware checklist

1. Cameras are on and recording.
2. Env camera frame includes the front and back edges of the table and is centered on the table's midpoint.
3. Both arms are at the home position with grippers open.
4. Table surface is clear of any objects other than the t-shirt(s).

### Materials checklist

1. T-shirt(s) to be folded are crumpled and placed at the back-left of the table.
2. Center of the table is clear (working area for straightening and folding).
3. Back-right of the table is clear (output location for the folded t-shirt / stack).

### Workspace layout

- **Back-left:** crumpled t-shirt(s) pile (input)
- **Center:** working area (straighten + fold)
- **Back-right:** folded t-shirt / folded stack (output)

## Steps

### Step 1: Move a t-shirt to the working area

Goal: one t-shirt sits in the working area, ready to be straightened.

- With the left gripper, grasp one t-shirt from the back-left pile.
- Move it to the center of the table.

### Step 2: Straighten the t-shirt

Goal: the t-shirt lies flat and face down, with the collar on the right.

**2.1 Lift the t-shirt**

- With the left gripper, grasp the highest point of the crumpled t-shirt and raise it until the bottom hem clears the table (or until full reach/extension).

**2.2 Transfer grip (transfer to the right gripper)**

- With the right gripper, grasp the lowest visible corner or sleeve, then release the left gripper.
- Raise the right gripper until the t-shirt hangs clear of the table (or the right arm is fully extended).

**2.3 Find the adjacent corner (trace along the hem)**

- With the left gripper, trace along the side hem from the current grasp point until you reach the next corner:
  - If holding a sleeve corner → trace to the nearest bottom corner.
  - If holding a bottom corner → trace to the nearest sleeve corner.

**2.4 Tension the t-shirt**

- Bring both grippers to the same height and pull outward in opposite directions to create tension along the hem.

**2.5 Fling the t-shirt flat**

- Fling the t-shirt so that both arms move towards the operator (front of the table) and the bottom of the t-shirt projects toward one side of the table and the collar is pulled toward the opposite side (left or right).
- If the t-shirt lands flat enough to identify orientation → continue. If it lands crumpled and orientation is unclear → return to 2.1.

**2.6 Check orientation — front vs. back**

- If face down → continue to 2.7.
- If face up → flip by draping (not flinging): confirm both near corners are accessible (un-tuck if needed), grasp the farthest sleeve corner and farthest bottom corner, lift the far edge until the near edge peels off the table, bring the hanging edge towards operator and down, then move back and down in one smooth motion to drape the gripped side over so it lands behind the contact line, and release. If it lands crumpled → return to 2.1.

**2.7 Check orientation — collar position**

- If the collar is on the left → rotate the t-shirt 180° clockwise.
- If the collar is on the right → continue to 2.8.

**2.8 Un-tuck any folded edges**

- Inspect the four corners (two bottoms + two sleeves) and the collar. For any corner/collar tucked under: fold it inward toward the center, then unfold back outward, stretching the corner outward. Repeat until all corners and the collar lie flat.

### Step 3: Fold the near side toward the center

Goal: the near side is folded in, with the resulting crease aligned to the near edge of the collar.

- With the right gripper, grasp the outer corner of the near sleeve (farthest from the collar, on the near side).
- With the left gripper, grasp the near bottom corner (the bottom-hem corner closest to the operator).
- Fold inward so the resulting horizontal crease aligns with the near edge of the collar, then make small adjustments to straighten the folded portion.

### Step 4: Fold the far side toward the center

Goal: the far side is folded in, with the new crease parallel to the Step 3 crease and aligned to the far edge of the collar.

- With the right gripper, grasp the outer corner of the far sleeve.
- With the left gripper, grasp the far bottom corner.
- Fold inward so the resulting horizontal crease aligns with the far edge of the collar and parallel to the crease from Step 3, then straighten as needed.

### Step 5: Reposition the folded shirt diagonally for the main fold

Goal: the t-shirt is set up diagonally so the collar end can be folded down to the hem.

- Move the folded t-shirt so the collar sits under the right-side working position (front-right area), the bottom hem points toward the back-left area, and the long axis is at roughly a 45° angle to the table's front edge (collar front-right → hem back-left).
- Multiple small grasp/release moves may be needed to rotate/translate. Keep the t-shirt flat and preserve the two parallel creases from Steps 3-4. If a crease opens, refold that side before continuing.

### Step 6: Fold the collar end down to meet the hem

Goal: the t-shirt is folded roughly in half, with the collar meeting the hem in a square-ish bundle.

- With the left gripper, grasp the near collar-side corner, and with the right gripper, grasp the far collar-side corner.
- Lift and carry the collar end up and across toward the bottom hem at the center of the table.
- Land each collar corner directly on top of its corresponding hem corner (target: within ~3 cm).
- If crumpled after folding, grasp the back-right and front-left corners and pull in opposite directions to create tension; repeat for the other back-left and front-right corners.
- Release both grippers.

> **Warning:** The shirt should now be folded roughly in half (collar meeting hem), producing a square-ish folded bundle.

### Step 7: Stack onto a pile (batch sessions only)

Goal: the newly folded t-shirt is stacked squarely on the existing pile.

- If this is a single-t-shirt episode or the back-right pile is empty → skip to Step 8.
- If stacking onto an existing pile:
  - With the left gripper, grasp the middle of the left edge of the newly folded shirt and pull it down to the left to clear stacking space.
  - With the right gripper, grasp the existing pile by the middle of its left edge and drag it down next to the new folded t-shirt (within 10-20 cm, aligned front-to-back).
  - With the left gripper grasp the top-left corner and with the right gripper grasp the bottom-right corner; lift the new folded t-shirt and place it on top (within 3 cm tolerance) so the fold edges align at the front (closed edge facing front) and the new t-shirt is centered side-to-side over the t-shirt below (midpoints aligned).
  - Release both grippers.

### Step 8: Move the folded t-shirt or stack to the back-right edge

Goal: the folded t-shirt/stack rests in the designated back-right output zone.

- With the right gripper, grasp the folded t-shirt/stack along the middle of its right edge.
- Drag it back and to the right into the output location at the back-right of the table.
- Release the gripper.

### Step 9: Return to home and end the episode

- Move both arms back to the home position with grippers open.
- End data collection.

## After each episode: repeat or reset (session-level workflow)

**Check the t-shirt count**

- Batch sessions (e.g., 5x): if fewer than the target number are folded, return to Step 1 with the next t-shirt. Once the target number is folded and stacked, reset the workspace before the next session.

**Reset the workspace**

This part is not recorded. It is just how you reset the table for the next episode. With recording off:

- Move the folded shirt(s) from the back-right back to the back-left.
- Crumple each shirt individually so the back-left once again contains distinct crumpled shirts matching the initial setup state.
- Confirm the table surface is clear of any objects other than the t-shirt(s) in their designated zone.

**Reverify setup**

- Go through the Setup checklist again before starting the next episode.

> **Warning:** If a t-shirt fell to the table or floor during the episode, retrieve it and return it to the input zone before re-running setup. The table must be clear except for the t-shirt(s) at the back-left.

## SOP Rubric (Steps-only violations)

Use this rubric to score whether each episode followed the SOP steps. These are process/step adherence checks (not quality-of-fold outcome checks), and each item is a violation if it occurs at any point during the episode.

**01: Correct pickup source & placement**
The t-shirt is picked from the back-left input pile with the left gripper and moved to the center working area (not started from center/right; not picked with the right gripper).

**02: Straighten sequence followed (lift → transfer → trace → tension → fling)**
The straighten sub-steps are performed in order — lift to clear the table, transfer grip to the right gripper, trace the side hem to the adjacent corner, tension, then fling flat (no skipping straight to folding while still crumpled).

**03: Adjacent corner found by tracing the hem**
The second corner is reached by tracing along the side hem from the first grasp (sleeve corner → bottom corner, or bottom corner → sleeve corner), not by grabbing a non-adjacent corner or random point.

**04: Tension performed before the flattening fling**
Both grippers are brought to the same height and pulled outward in opposite directions to tension the hem before the fling (no direct fling without tension).

**05: Correct straighten orientation before folding (face down, collar on the right)**
After straightening, the t-shirt lies flat, face down, with the collar on the right before any folding begins; face-up is corrected by draping and collar-on-left by a 180° clockwise rotation (no folding while face-up or with the collar on the left).

**06: Edges un-tucked before folding**
All four corners (two bottom + two sleeve) and the collar are un-tucked and lie flat before folding (no folding over tucked corners or collar).

**07: Near side folded first**
Step 3 folds the near side inward with the crease aligned to the near edge of the collar, using the right gripper on the outer near-sleeve corner and the left gripper on the near bottom corner (no far-side-first, no mid-cloth fold).

**08: Far side folded second with a parallel crease**
Step 4 folds the far side inward with the crease parallel to the Step 3 crease and aligned to the far edge of the collar (no out-of-order fold; crease not parallel).

**09: Diagonal reposition preserves the two creases**
The folded shirt is repositioned to the ~45° diagonal (collar front-right → hem back-left) while kept flat, preserving the two parallel creases (no opening a crease without refolding before continuing).

**10: Collar-to-hem main fold completed**
Step 6 folds the collar end down onto the hem, landing each collar corner on its hem corner within ~3 cm, producing a square-ish bundle (no incomplete or crumpled main fold).

**11: Conditional stacking logic followed**
If a single-t-shirt episode or the back-right pile is empty, stacking (Step 7) is skipped; if a pile exists, the shirt is stacked centered with fold edges aligned within 3 cm (no stacking onto empty space; no skipping stacking onto an existing pile).

**12: Move to back-right output using the right gripper**
The folded t-shirt/stack is grasped along the middle of its right edge with the right gripper and dragged into the back-right output zone (no moving with the left gripper; no leaving it in the center).

**13: Correct arm used for each gripper-specified action**
Every step that specifies the left or right gripper is performed with that gripper (no using the opposite arm).

**14: End-of-episode behavior correct**
Both arms return to the home position with grippers open and data collection ends; in batch sessions, if fewer than the target remain, the next t-shirt is started, and the workspace is reset only once the target is folded (no returning home early; no failing to return home).

## Annotation subtasks

1. Move one t-shirt from the input area to the center working area
2. Straighten the t-shirt (face down, collar on the right, arms out)
3. Fold the near sleeve and side toward the center
4. Fold the far sleeve and side toward the center
5. Reposition the t-shirt to a diagonal setup for the main fold
6. Fold the collar-side corners down to meet the bottom corners (close the fold)
7. Stack the folded t-shirt onto the pile (batch only)
8. Move the folded t-shirt or stack to the back-right output area
9. Home the arms

---

## Vocabulary

These are the terms used in this SOP. Operators and annotators must use this language consistently. One term per concept, used throughout.

### T-shirt anatomy

- **T-shirt:** a single short-sleeve garment to be folded.
- **Collar:** the neck opening of the t-shirt.
- **Bottom hem:** the bottom edge of the t-shirt body, opposite the collar.
- **Sleeve:** one of the two short arms of the t-shirt.
- **Sleeve corner:** the outer bottom corner of a sleeve cuff.
- **Bottom corner:** one of the two corners where the bottom hem meets a side hem.
- **Side hem:** the side edge of the body running between a sleeve corner and a bottom corner.
- **Face down:** the front of the t-shirt rests against the table.
- **Face up:** the front of the t-shirt faces the camera.
- **Near side:** the side of the t-shirt closest to the operator/front of the table.
- **Far side:** the side of the t-shirt farthest from the operator/back of the table.
- **Folded bundle:** the finished square-ish result after the main fold.

### Workspace zones

- **Back-left edge:** input zone holding crumpled t-shirts at the back-left of the table.
- **Working area:** the center of the table where straightening and folding happen.
- **Back-right edge:** output zone where the folded t-shirt/stack is placed at the back-right of the table.
- **Home position:** the default resting pose for each arm: gripper open and clear of the table.

### Actions

- **Pick:** move one crumpled t-shirt to the working area.
- **Straighten:** lift, tension, and fling/drape the t-shirt so it lies flat, face down, collar on the right.
- **Fold:** fold a side or end of the t-shirt inward along a crease until it lies flat.
- **Stack:** place the newly folded t-shirt onto an existing pile (batch sessions only).
