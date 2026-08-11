# Generic SOP Violations

Use this document as the shared violation standard for all teleoperated data-collection SOPs. Add
task-specific violations to the individual SOP when the task has unique requirements such as fill
volume, coil diameter, ingredient order, screw depth, or tableware orientation.

## Application rules

1. Include every **Core violation** in each SOP.
2. Include a **Conditional reusable violation** only when the SOP contains the corresponding rule.
3. Replace bracketed references such as `[Step N]` with the actual section or step.
4. Record only visible actions. Do not infer an invisible decision or intention.
5. Use the most specific available label. Do not apply a generic and task-specific label to the
   same action unless the actions break two distinct rules.
6. A poor task outcome is not automatically a violation. Tag it only when the recording
   shows the prescribed process rule being broken.
7. System, recording, and defective-material failures belong under **Non-violation failures**.

## How to record a violation in review

For every violation, record:

- the **start timestamp**;
- the **violation name** exactly as written;
- the **SOP rule broken**, given as its step number and nothing else; and
- the affected object or subtask when the review tool provides that field.

If the review tool supports temporal ranges, also record the end timestamp. The visible cue is what
the reviewer sees. The coaching note is for retraining and is not an annotation label.

## Episode handling

Tag every violation with its timestamp and name. Retain the episode with the violation tag
unless the project data-acceptance policy excludes that violation class. Log failures that are
not violations separately and discard the affected episode when the recording or robot state is
unusable.

## Core violations

These violations apply to every SOP.

### Violation: Required sequence not followed

- **Visible cue:** a required phase or step is skipped, repeated without a prescribed reason,
  performed early, or performed in an order different from the SOP.
- **SOP rule broken:** `[Steps N to N]` (perform the required phases and steps in the
  prescribed order).
- **Coaching note:** follow the written sequence and use only its stated conditional branches.

### Violation: Prescribed arm, gripper, or tool assignment not followed

- **Visible cue:** an action assigned to the left or right gripper is performed with the other
  gripper; the wrong tool is selected; or a required two-arm action is performed with one arm.
- **SOP rule broken:** `[Step N]` (use the prescribed arm, gripper,
  and tool for the action).
- **Coaching note:** review the arm and tool assignments before beginning the subtask.

### Violation: Object handled or transported incorrectly

- **Visible cue:** an object is grasped at a prohibited location; carried with a prohibited tilt or
  orientation; dragged, crushed, forced, shaken, or pulled when prohibited; moved through an
  obstructed path; or released before it is supported and stable.
- **SOP rule broken:** `[Step N]` (use the prescribed grasp, orientation,
  path, force, and release condition).
- **Coaching note:** use the specified contact point and keep the object controlled until stable.

### Violation: Object dropped, collided, or released uncontrollably

- **Visible cue:** an object falls from a gripper, strikes the robot or another object, leaves the
  work surface, or is released outside its intended stable placement.
- **SOP rule broken:** `[Step N]` (maintain control, use a clear path, and
  release only at the prescribed destination when stable).
- **Coaching note:** confirm the grasp, travel path, and landing area before moving or releasing.

### Violation: Required check, retry, or recovery not followed

- **Visible cue:** the episode continues without a required visible check; ignores a
  visible failed condition; retries more times than allowed; or uses a recovery action not permitted
  by the SOP.
- **SOP rule broken:** `[Step N]` (perform the prescribed check and
  follow only the stated retry or recovery action).
- **Coaching note:** stop at each required check and follow its recovery branch exactly.

### Violation: Workspace or tool state not restored

- **Visible cue:** a tool or non-output object is left outside its required position; debris, a
  spill, or an obstruction remains when the SOP requires it cleared; or a required working or
  handoff zone is not empty before the next phase or episode.
- **SOP rule broken:** `[Step N]` (restore tools and required zones
  to their prescribed states).
- **Coaching note:** verify tool positions and clear the required zones before continuing.

### Violation: Incorrect episode ending

- **Visible cue:** recording ends before the required task state is complete; the final output is
  outside its prescribed zone; tools or zones are not in their required final states; arms are not
  in the prescribed end pose; grippers have the wrong end state; or the required final hold is
  skipped.
- **SOP rule broken:** `[Step N]` (complete the required final checks, output state,
  robot end state, and recording boundary).
- **Coaching note:** complete the final checklist and robot end state before stopping recording.

## Conditional reusable violations

Use these only when the individual SOP explicitly contains the corresponding rule.

### Violation: More than one object moved at once

- **Visible cue:** two or more task objects are lifted, dragged, transferred, or placed together
  when the SOP requires one object at a time.
- **SOP rule broken:** `[Step N]` (move exactly one task object at a time).
- **Coaching note:** separate and move only the current assigned object.

### Violation: Wrong object, source, or destination selected

- **Visible cue:** the wrong object or variant is selected; an object is taken from the wrong source
  zone; or it is placed in the wrong output position, container, compartment, or assigned location.
- **SOP rule broken:** `[Step N]` (use the assigned object, source, and
  destination).
- **Coaching note:** confirm the current object and its source-to-destination assignment before
  moving it.

### Violation: Handoff not completed correctly

- **Visible cue:** the receiving gripper uses the wrong contact point; the sending gripper releases
  before the required receiving hold; the item is transferred outside the handoff zone; or the item
  is released unsupported.
- **SOP rule broken:** `[Step N]` (transfer in the assigned zone with the
  prescribed grips, overlap, and release order).
- **Coaching note:** establish a stable receiving grasp before the sending gripper releases.

### Violation: Prohibited contact or cross-contamination

- **Visible cue:** a gripper or tool touches a protected interior, food-contact surface, sharp
  surface, connector, or other prohibited area; products are mixed; or a contaminated tool is used
  on another product.
- **SOP rule broken:** `[Step N]` (avoid prohibited
  contact and preserve the required separation).
- **Coaching note:** use only the permitted grasp surface and keep assigned products and tools
  separate.

### Violation: Placement or alignment outside the prescribed tolerance

- **Visible cue:** an object is visibly outside its numeric position, orientation, spacing,
  alignment, stability, or containment tolerance and is not corrected as prescribed.
- **SOP rule broken:** `[Step N]` (place and correct the object within the stated
  tolerance).
- **Coaching note:** check the specified reference and tolerance before releasing or continuing.

### Violation: Spill, debris, or waste handled incorrectly

- **Visible cue:** cleanup begins at a prohibited time; waste is returned to a product or clean
  supply; debris is moved outside the waste zone; the wrong cleanup tool is used; or visible residue
  remains after the required cleanup step.
- **SOP rule broken:** `[Step N]` (stabilize the task, protect clean objects,
  and clean the spill or debris at the prescribed time and location).
- **Coaching note:** follow the stated spill branch and move waste only to its assigned container.

### Violation: Machine safety condition not followed

- **Visible cue:** the machine is started without its guard, lid, workpiece, or tool fully seated;
  an arm or object remains inside a prohibited operating zone; the machine is touched while moving;
  or an abnormal condition is ignored.
- **SOP rule broken:** `[Step N]` (meet every
  safety condition before activation and follow the prescribed stop response).
- **Coaching note:** verify guards, clearances, and robot position before activation; stop on any
  abnormal condition.

## Non-violation failures

Record these as system, environment, or material issues rather than coaching violations:

- recording stops, pauses, is corrupted, or lacks required time synchronization;
- a camera drops frames, loses its feed, moves, or becomes obstructed during the episode;
- an arm, gripper, tool, fixture, or machine malfunctions, drifts, disconnects, or reports an error;
- a required object is defective, broken, contaminated, or incompatible despite passing setup;
- power, lighting, or an external environmental condition makes the task or recording unusable; or
- an unexpected safety hazard requires stopping the episode.

For each non-violation failure, record the timestamp, failure type, affected system or object, and
episode disposition.

## Per-SOP adoption checklist

Before inserting these violations into an SOP:

1. Replace every bracketed placeholder with the real section or step number.
2. Remove conditional violations that have no corresponding task rule.
3. Add task-specific violations for unique quantities, orientations, orders, tolerances, or safety
   conditions.
4. Confirm every prescribed step maps to at least one violation or non-violation failure.
5. Confirm every violation has a cue that is visible in the recorded camera views.
6. Keep violation names identical across SOPs when the meaning is identical.
