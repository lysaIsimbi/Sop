# Pick and Place SOP

## Setup

Complete both checklists below before starting any episode.

### Hardware checklist

1. Cameras are on and recording
2. Env camera frame includes the front and back edges of the table and is centered on the table's midpoint
3. Gripper is at the home position with gripper open
4. Table surface is clear except for the cup/object and the tray/target

### Materials checklist

1. Source area contains N objects (define type/size) arranged within reachable workspace
2. Target area (bin/slot/marked region) is empty and reachable
3. Any fixtures (tray, jig, dividers) are secured and aligned to the table area.
4. If using labels/markers: markers are visible and not occluded (in line of sight or not blocked)

### Workspace layout

- Left / Source → objects to pick (input)
- Center → transit/working area (optional)
- Right / Target → placement area (output)

## Steps

### Step 1: Move to object and grasp (pick)

Goal: N object is securely grasped and lifted clear of the table.

- Move the gripper from home position to the object.
- Approach from the top or the side, using a smooth, collision-free path.
- Grasp securely around the object body (or handle if present).
- Lift the object clear of the table and pause briefly to confirm it is stable (no slip/rotation).

### Step 2: Adjust / re-grasp (if needed)

Goal: secure, centered grasp suitable for precise placement.

- If the grasp is unstable, off-center, or slipping:
  - Lower the object gently onto the table in the center/working area.
  - Release and re-grasp with better finger placement.
  - Re-lift and confirm the object is held firmly.
- If the grasp is stable, skip this step and continue.

### Step 3: Transport and place on the target

Goal: object is placed upright/centered and stable at the target location.

- Carry the object from the source area to the target (e.g., tray/bin/marked region).
- Hover above the target and visually align position and orientation.
- Lower slowly and precisely until the object is fully seated/on the surface.
- Release only when the object is stable and not moving or shaking unsteadily.
- Lift the gripper slightly away from the object.

### Step 4: Return to home and end the episode

- Return the gripper to the home position with the gripper open.
- End data collection/recording for the episode.

## After each episode: repeat or reset

This section is not a recorded subtask: it covers session-level workflow between episodes.

- If more objects remain in the source area → continue to Step 1 with the next object.
- If the source area is empty or the target area is full → reset the workspace:
  - With recording off, clear the target area as needed.
  - Refill/rearrange the source area to the initial setup state.
  - Re-verify setup checklists before the next run.

## SOP Rubric (Steps-only violations)

Use this rubric to score whether each episode followed the SOP steps. These are
process/step adherence checks (not quality-of-fold outcome checks), and each item is a
violation if it occurs at any point during the episode.

**01: Move to object smoothly**
Gripper moves from home to the object using a smooth, collision-free path (top/side approach).

**02: Secure grasp**
Object is grasped securely around the body/handle (not pinched precariously or off-contact).

**03: Lift clear + stable hold**
Object is lifted clear of the table and remains stable during a brief pause (no slip/rotation).

**04: Correct decision on re-grasp**
If grasp is unstable/off-center/slipping, re-grasp is attempted; if grasp is stable, step is correctly skipped.

**05: Re-grasp executed correctly (when needed)**
Object is lowered to center/working area, released, re-grasped with improved finger placement, then re-lifted stable.

**06: Controlled transport + alignment**
Object is carried to target without collisions/drops; robot hovers above target and aligns position/orientation before lowering.

**07: Precise placement + clean release**
Object is lowered slowly until seated; release occurs only when stable; gripper lifts away without disturbing the object.

**08: Return to home**
Gripper returns to the home position with gripper open.

## Annotation subtasks

1. Move to object and grasp (pick) (Step 1)
2. Grasp adjustment / verification (Step 2)
3. Transport and precise placement (Step 3)
4. Return to home (Step 4)
