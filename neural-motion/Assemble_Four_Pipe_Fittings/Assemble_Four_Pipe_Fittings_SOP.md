# Assemble Four Pipe Fittings SOP (4x)

This SOP covers assembling a threaded pipe joint using a two-arm robot system, a bench vise and a pipe
wrench, repeated for four joints in one episode. Both arms are used throughout: the grippers cooperate to
clamp the nipple, wrap the threads with tape, start the fitting by hand, drive the wrench, and cap the
open ends, with the left and right grippers taking the specific roles called out in each step. The task
runs from four bare pipe nipples, four fittings and four caps in the start zone to four capped assemblies
in the output row.

The table is set up in one of three ways. Only the parts (the nipples, fittings and caps) move; the vise,
the tape dispenser and the wrench rest are in the same place in all three.

- **Config L:** the parts are at the back-left; the output row is at the back-right.
- **Config M:** the parts are at the front-center, in front of the vise; the output row is at the back-right.
- **Config R:** the parts are at the back-right, where the output row normally is; the output row is at the
  back-left instead.

Where a step depends on the setup it says so on an **IF** line - look at the table and follow the line that
matches.

What stays constant across all sessions:

- **Start position:** the parts start at the back-left (**Config L**), the front-center (**Config M**) or
  the back-right (**Config R**). One config per episode, chosen before recording and never changed
  mid-episode.
- **Same-side rule:** the gripper on the parts' side picks every nipple, fitting and cap from the start zone
  - the left gripper in Config L and M, the right gripper in Config R. No arm reaches across the table.
- **Hand-over rule:** the pick follows the same-side rule but the working roles do not change, so a part
  picked by the other gripper is **handed over** above the assembly station: the giver holds the part still,
  the receiver closes on the opposite side of it, and only then does the giver open and lift clear. In
  Config L and M the left gripper hands each fitting and each cap to the right gripper; in Config R the
  right gripper hands each nipple to the left gripper. Nothing else is handed over.
- **Fixed roles:** in every config the left gripper holds the nipple between the jaws and the right gripper
  closes the vise; the right gripper draws the tape, starts every fitting and cap, and drives the wrench;
  the left gripper stages every finished assembly.
- **Working position:** the nipple is always clamped in the vise at the centre of the table before any
  tape is wrapped or any fitting is started.
- **Wrap direction:** tape is always wrapped **clockwise as viewed from the open end of the male thread**
  - the same direction the fitting turns on - so the fitting cannot peel the tape off.
- **Cycle order:** wrap the threads with tape, start the fitting by hand, wrench-tighten to the alignment
  marks, then cap the open ends. One fitting per nipple, four joints per episode.
- **Hand-start rule:** every fitting is turned on by hand until hand-tight before the wrench touches it.
  The wrench is never used to start a thread.
- **Pass condition:** an assembly is only staged as finished once the alignment marks line up and both
  open ends are capped hand-tight.

## Setup

Go through both checklists before starting the episode.

### Hardware checklist

- Cameras are on and recording
- Env camera frame includes the front and back edges of the table and is centered on the table's
    midpoint
- Both arms are at the home position with grippers open
- Table surface is clear of any objects other than the vise, the wrench, the tape dispenser and the
    parts

### Materials checklist

- Four pipe nipples are placed in the **start zone** for this episode's config, threads clean and dry, not
    touching each other, and the other two start zones are bare:
    - **Config L:** back-left
    - **Config M:** front-center, in front of the vise, clear of the tape dispenser and the wrench rest
    - **Config R:** back-right, where the output row normally is
- Four fittings are placed in the **start zone** beside the nipples, female thread up
- Four caps are placed in the **start zone** beside the fittings, open end up
- Every nipple and every fitting carries its **alignment mark**, and the marks are visible to the env
    camera
- Bench vise is at the **center** of the table with the jaws open and clear
- Pipe wrench is at the **front-right** of the table on its rest, jaw set to size
- Tape dispenser is at the **front-left** of the table with a free tape end available
- The output location for the finished assemblies is clear: the back-right (Config L and M) or the
    back-left (Config R)

## Workspace layout

- **Start zone**: bare nipples, fittings and caps (input) - back-left (Config L), front-center (Config M)
  or back-right (Config R)
- **Center**: assembly station - the vise (wrap + start + tighten + cap)
- **Front-left**: tape dispenser
- **Front-right**: wrench rest
- **Back-right**: finished capped assemblies (output); in Config R the output row is at the **back-left**

## Vocabulary

These are the terms used in this SOP. Operators and annotators must use this language consistently. One
term per concept, used throughout.

### Pipe and fitting anatomy

- **Nipple:** a single short length of pipe with a male thread at each end.
- **Male thread:** the external thread on the end of the nipple; this is the end that gets taped.
- **Female thread:** the internal thread inside the fitting or the cap.
- **Fitting:** the elbow that is threaded onto one end of the nipple.
- **Cap:** the closure threaded onto an open end of the finished assembly.
- **Thread start:** the first thread at the very end of the male thread, where engagement begins.
- **Thread engagement:** how far the female thread has travelled onto the male thread, counted in turns.
- **Alignment mark:** the painted line on the nipple and the matching line on the fitting; the two lines
  meet when the joint is tightened to the correct depth.
- **Marks aligned:** the fitting mark sits directly on the nipple mark - the target for tightening.
- **Marks short:** the fitting mark has not yet reached the nipple mark (under-tightened).
- **Marks past:** the fitting mark has travelled beyond the nipple mark (over-tightened).
- **Hand-tight:** turned on by gripper force alone until it stops turning, before any wrench is used.
- **Wrench-tight:** turned the rest of the way with the pipe wrench until the marks align.
- **Crossthreaded:** the fitting has started on at an angle, so it binds and its face is not square to
  the nipple axis.
- **Open end:** an end of the finished assembly that is not yet capped.

### Tape

- **Tape:** the thread-sealing tape wrapped onto the male thread before the fitting goes on.
- **Tape dispenser:** the spool at the front-left of the table that the tape is drawn from.
- **Wrap:** one full turn of tape around the male thread.
- **Wrap direction:** clockwise as viewed from the open end of the male thread - the same direction the
  fitting turns on.
- **Tape tail:** the loose end of tape left after the wrap is broken off.
- **Threads filled:** the tape sits down in the thread grooves and the thread form is still visible
  through it.
- **Threads buried:** so much tape is on that the thread form can no longer be seen (too many wraps).

### Tooling

- **Bench vise:** the clamp at the center of the table that holds the nipple during assembly.
- **Jaws:** the two faces of the vise that close onto the nipple.
- **Clamped square:** the nipple is held with its axis horizontal and it does not turn in the jaws.
- **Pipe wrench:** the wrench used to tighten the fitting to the alignment marks.
- **Wrench rest:** the marked spot at the front-right of the table where the wrench lives.
- **Swing path:** the arc the wrench handle travels through while tightening.

### Workspace zones

- **Start zone:** input zone holding the bare nipples, the fittings and the caps - back-left (**Config L**),
  front-center (**Config M**) or back-right (**Config R**). One per episode, chosen before recording and
  never changed mid-episode.
- **Assembly station:** the center of the table where wrapping, starting, tightening and capping happen.
- **Back-right edge:** output zone where each finished assembly is placed at the back-right of the table.
  In Config R the output row is at the back-left instead.
- **Home position:** the default resting pose for each arm: gripper open and clear of the table.

### Actions

- **Pick:** move one nipple, one fitting, or one cap from the start zone to the assembly station.
- **Hand over:** the giver holds a part still above the assembly station, the receiver closes on the
  opposite side of it, and only then does the giver open and lift clear. Right to left for the nipple in
  Config R; left to right for the fitting and the cap in Config L and M.
- **Clamp:** close the vise jaws onto the nipple so it is held square and cannot turn.
- **Wrap:** lay three full turns of tape onto the male thread clockwise and under tension.
- **Start:** turn the fitting on by hand until it is hand-tight.
- **Tighten:** pull the wrench in one continuous stroke until the alignment marks meet.
- **Cap:** thread a cap hand-tight onto an open end of the assembly.
- **Stage:** place the finished assembly in the output zone (batch sessions place them in a row).
- **Next fitting:** return to Step 1 with the next nipple until four joints are done.

## Steps

Steps 1, 3.1 and 5.1 depend on where the parts are: in Config L and M the **left gripper** picks each part
from the start zone, in Config R the **right gripper** picks it, and a part picked by the gripper that does
not hold or turn it is handed over above the assembly station. Step 6 depends on where the output row is.
Every other line is the same in all three configs.

### Step 1: Move a nipple to the working area

**Goal:** one nipple is clamped in the vise, ready for its threads to be taped.

Look where the parts are before reaching for the first nipple.

- **IF the parts are at the back-left (Config L):** with the left gripper, grasp one nipple from the pile
  around its middle and carry it to the vise.
- **IF the parts are at the front-center (Config M):** with the left gripper, grasp one nipple from the pile
  around its middle and carry it back to the vise.
- **IF the parts are at the back-right (Config R):** with the right gripper, grasp one nipple from the pile
  around its middle, carry it to above the vise and hold it still. The left gripper closes on the nipple on
  the other side of the middle; the right gripper opens and lifts clear.

Then, in all three:

- With the left gripper, hold the nipple between the open jaws of the vise at the center of the table.
- With the right gripper, close the vise until the nipple is clamped square, with one male thread
  standing clear of the jaws and the nipple's alignment mark facing up.

### Step 2: Wrap the threads with tape

**Goal:** the male thread carries three full clockwise wraps of tape, laid under tension, with the
threads filled and not buried and the tape tail pressed down.

#### 2.1 Check the clamp before wrapping

- Confirm the nipple does not turn or rock in the jaws, and that its axis is horizontal.
- If it turns or rocks → re-open the jaws, reset the nipple square and re-clamp before wrapping.

#### 2.2 Find and pick up the tape end

- With the right gripper, grasp the free tape end at the dispenser; if no free end is showing,
  rotate/reorient the spool anti-clockwise until the end comes into view, then grasp it.
- Draw the tape out and carry the end to the male thread at the assembly station.

#### 2.3 Check direction - clockwise onto the thread

- If the wrap will run clockwise as viewed from the open end of the male thread → continue to 2.4.
- If the wrap would run anti-clockwise → carry the tape end around to the other side of the nipple and
  re-approach so the wrap runs clockwise. The tape must go on the way the fitting turns on, or the
  fitting peels it off.

#### 2.4 Start the tape on the second thread

- Lay the tape end onto the second thread from the end, not over the thread start, and hold it down with
  the left gripper.
- Leaving the first thread bare keeps tape out of the joint and lets the fitting find the thread start
  cleanly.

#### 2.5 Wrap three full turns under tension

- With the right gripper, carry the tape around the male thread three full turns, working back from the
  thread start toward the jaws and overlapping each turn by about half its width.
- Keep the tape pulled taut throughout so it stretches down into the thread grooves rather than bridging
  across them.
- Do not wrap fewer than three turns and do not wrap more than three turns.

#### 2.6 Break the tape and press the tail down

- With the left gripper, hold the wrap in place and with the right gripper pull the tape until it breaks.
- Press the tape tail flat against the wrap so nothing stands loose off the thread.

#### 2.7 Check coverage - filled, not buried

- If the thread form is still visible through the tape and every wrapped thread is covered → continue to
  Step 3.
- If the threads are buried, or the wrap is loose, bunched or torn → with the left gripper peel all of
  the tape off the thread, discard it, and return to 2.2 with a fresh start. Never wrap fresh tape over a
  bad wrap.

### Step 3: Start the fitting by hand

**Goal:** the fitting is turned onto the taped thread by hand until hand-tight, running square and free
with no crossthreading, and no wrench has touched it.

#### 3.1 Find and pick up a fitting

- **IF Config L or M:** with the left gripper, grasp one fitting from the start zone by its body.
  **IF Config R:** with the right gripper, grasp one fitting from the start zone by its body. In either
  case, if no fitting is clear of the others, rotate/reorient anti-clockwise until one comes free, then
  grasp it.
- Raise it clear of the input pile and carry it to the assembly station. **IF Config L or M:** hold it
  still above the assembly station, let the right gripper close on the opposite side of its body, then open
  the left gripper and lift clear.

#### 3.2 Check orientation - female thread onto the male thread

- If the fitting's female thread faces the taped male thread and its alignment mark is up → continue to
  3.3.
- If the fitting is presented the wrong way round → hand it to the left gripper, regrip it from the
  opposite side with the right gripper, and turn it until the female thread faces the nipple and the mark
  is up.

#### 3.3 Engage the thread start square

- Bring the fitting up to the nipple so the two axes are in line, seat the female thread onto the thread
  start, and turn clockwise until it catches.
- Do not force the first turn; a thread that will not catch under light force is not lined up.

#### 3.4 Turn it on by hand to hand-tight

- Turn the fitting clockwise by hand, regripping as needed, until it stops turning under gripper force
  alone.
- Expect the fitting to run on freely for several turns before it starts to tighten. Do not pick up the
  wrench at any point in this step.

#### 3.5 Check alignment - crossthread check

- If the fitting ran on freely and its face is square to the nipple axis → note where the fitting mark
  sits relative to the nipple mark and continue to Step 4.
- If the fitting bound up within the first two turns, or sits cocked so its face is not square → turn it
  back off anti-clockwise all the way, inspect the tape, and return to 3.3. If it crossthreads again →
  return to 2.7 and re-tape the thread.

### Step 4: Wrench-tighten to the alignment marks

**Goal:** the joint is pulled up in one continuous stroke until the alignment marks line up exactly.

#### 4.1 Fetch the pipe wrench

- With the right gripper, grasp the pipe wrench by its handle from the rest at the front-right of the
  table.
- Carry it to the assembly station and bring it up to the fitting.

#### 4.2 Set the wrench on the fitting

- Set the wrench jaw squarely on the body of the **fitting**, never on the nipple and never on the taped
  thread, with the jaw facing so that pulling the handle turns the fitting clockwise.
- With the left gripper, steady the vise, and confirm the wrench swing path is clear of the other arm and
  of the input pile.

#### 4.3 Pull up to the marks in one continuous stroke

- Pull the handle in one smooth, continuous stroke, watching the fitting mark travel toward the nipple
  mark, and stop the moment the two marks line up.
- Do not ratchet the wrench back and forth, do not reset the jaw part way through the pull, and do not
  tighten on feel instead of on the marks.

#### 4.4 Check the marks

- If the marks are aligned → continue to 4.5. Leave the joint exactly where it is.
- If the marks are short → reset the jaw and take one more continuous pull to bring them together.
- If the marks are past → the joint is over-tightened. Do not back the fitting off to correct it. Leave
  it, flag the assembly, and continue; a joint that has been backed off no longer seals.

#### 4.5 Return the wrench to its rest

- Lift the wrench clear of the fitting and carry it back to the rest at the front-right of the table.
- Release the wrench and bring the right gripper back over the assembly station.

**Warning:** The fitting should now be wrench-tight with its mark on the nipple mark, ready for the open
ends to be capped.

### Step 5: Cap the open ends

**Goal:** every open end of the assembly is closed with a cap turned on hand-tight.

#### 5.1 Find and pick up a cap

- **IF Config L or M:** with the left gripper, grasp one cap from the start zone by its outside.
  **IF Config R:** with the right gripper, grasp one cap from the start zone by its outside. In either
  case, if no cap is clear of the others, rotate/reorient anti-clockwise until one comes free, then grasp
  it.
- Carry it to the assembly station. **IF Config L or M:** hold it still above the assembly station, let the
  right gripper close on the opposite side of its outside, then open the left gripper and lift clear.
- With the right gripper, bring the cap up to the open end.

#### 5.2 Turn the cap on hand-tight

- Seat the cap's female thread onto the open end square, then turn it clockwise by hand until it stops.
- Caps are hand-tight only. Do not fetch the wrench for a cap; the cap is a cover for handling, not a
  sealed joint.

#### 5.3 Confirm every open end is capped

- Walk the assembly and confirm no thread is left open: the outlet of the fitting and any remaining
  nipple end each carry a cap.
- If an end is still open → return to 5.1 with another cap.

### Step 6: Move the assembly to the output row

**Goal:** the finished capped assembly rests in the designated output zone.

- With the right gripper, open the vise jaws and release the assembly.
- With the left gripper, grasp the assembly around the nipple and lift it clear of the jaws.
- **IF Config L or M:** carry it to the back-right of the table. **IF Config R:** carry it to the back-left
  of the table. Set it down in the output row, alongside the assemblies already finished and not touching
  them.
- Release the gripper.

### Step 7: Next fitting (repeat to four)

- If fewer than four assemblies are finished → return to Step 1 with the next nipple.
- Once four assemblies are capped and staged in the output row → continue to Step 8.

### Step 8: Return to home and end the episode

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

**Note on the start position:** the violations below were written for Config L (parts start at the
back-left, output row at the back-right). The pickup and arm-role cues will be rewritten later to cover all
three start positions; they are left as they are for now. Until then, anything that does not match the
episode's config goes under **Config misaligned**.

**Violation: Config misaligned.**

- **Visible cue:** what the operator does does not match the config on the table - the parts are not in
  the start zone for the config; a gripper reaches across the table for a nipple, fitting or cap; a part
  picked by the other gripper is not handed over above the assembly station, or the giver opens before the
  receiver has closed; the assembly is staged on the wrong side; or the wrong IF line is followed.
- **SOP rule broken:** the start position, the same-side rule and the hand-over rule (the left gripper
  picks every part in Config L and M and the right gripper in Config R; a fitting or cap picked by the left
  gripper, or a nipple picked by the right gripper, is handed over above the assembly station; no arm
  reaches across the table; the IF line followed is the one for the config on the table).
- **Coaching note:** look where the parts are before the first reach, then follow that config's IF lines
  through Steps 1, 3.1, 5.1 and 6.

**Violation: Wrong pickup.**

- **Visible cue:** a nipple, a fitting or a cap is started from the center or right instead of the
  back-left input zone, it is placed outside the assembly station, or it is dragged or slid across the
  table instead of being picked up (lifted clear of the surface) and carried.
- **SOP rule broken:** Steps 1, 3.1 and 5.1 (pick from the back-left input zone and bring it to the
  assembly station). Pick means lift and carry, not drag.
- **Coaching note:** always start each nipple, fitting and cap from the back-left and bring it to the
  center. Lift it clear of the table and carry it. Do not drag or slide it across the surface.

**Violation: Picked more than one part at once.**

- **Visible cue:** two or more nipples, two or more fittings, or two or more caps are lifted/moved from
  the input zone in a single pick.
- **SOP rule broken:** Steps 1, 3.1 and 5.1 (move one nipple, one fitting and one cap per cycle).
- **Coaching note:** pick exactly one nipple, one fitting and one cap per assembly cycle.

**Violation: Nipple not clamped square or loose in the vise.**

- **Visible cue:** wrapping or tightening starts while the nipple turns in the jaws, rocks, sits at an
  angle rather than horizontal, or is held so the male thread is not clear of the jaws.
- **SOP rule broken:** Steps 1 and 2.1 (clamp square, horizontal, with the male thread clear of the jaws
  and the nipple not turning).
- **Coaching note:** clamp the nipple square and check it cannot turn before wrapping. A nipple that
  turns in the jaws takes the tightening load and the marks never come together.

**Violation: Tape wrapped in the wrong direction.**

- **Visible cue:** the tape is carried around the male thread anti-clockwise as viewed from the open end
  of the thread, against the direction the fitting turns on.
- **SOP rule broken:** Wrap direction and Step 2.3 (clockwise as viewed from the open end of the male
  thread).
- **Coaching note:** wrap the way the fitting turns on. Tape wrapped the wrong way is peeled off the
  thread by the fitting and bunches into the joint.

**Violation: Tape end not correctly found before grasping.**

- **Visible cue:** the operator fails to find and grasp the free tape end: the grip closes on empty air
  or on the spool body, or the tape is torn off mid-roll; or, when no free end is showing, the operator
  reorients the spool clockwise (or in an arbitrary back-and-forth direction) instead of anti-clockwise
  to bring the end into view.
- **SOP rule broken:** Step 2.2 (grasp the free tape end; if none is showing, rotate/reorient the spool
  anti-clockwise until the end comes into view, then grasp it).
- **Coaching note:** confirm the tape end is actually in view before closing the gripper. If it is not
  showing, reorient the spool anti-clockwise (a consistent search direction) until it appears, then grasp
  it.

**Violation: Tape started on the wrong thread.**

- **Visible cue:** the wrap is started over the thread start (the first thread at the very end) or off
  the end of the nipple entirely, instead of on the second thread.
- **SOP rule broken:** Step 2.4 (lay the tape end on the second thread from the end, not over the thread
  start).
- **Coaching note:** leave the first thread bare. Tape over the thread start goes into the joint and
  stops the fitting finding the thread cleanly.

**Violation: Wrong number of tape wraps.**

- **Visible cue:** the male thread receives fewer than three or more than three full turns of tape.
- **SOP rule broken:** Step 2.5 (three full turns, no fewer and no more).
- **Coaching note:** count the turns out loud: three. Too few will not seal, too many buries the thread
  and the marks cannot come together.

**Violation: Tape wrapped slack.**

- **Visible cue:** the tape is laid on loose so it bridges across the thread grooves, bunches, or stands
  off the thread instead of being pulled taut into the grooves.
- **SOP rule broken:** Step 2.5 (keep the tape pulled taut so it stretches down into the thread grooves).
- **Coaching note:** keep tension on the tape the whole way round. Slack tape rolls up into a rope when
  the fitting goes on.

**Violation: Tape tail left loose.**

- **Visible cue:** the wrap is broken off and the tape tail is left standing off the thread rather than
  pressed flat against the wrap.
- **SOP rule broken:** Step 2.6 (press the tape tail flat against the wrap).
- **Coaching note:** press the tail down before the fitting goes on, or the fitting catches it and drags
  the whole wrap with it.

**Violation: Fresh tape wrapped over a bad wrap.**

- **Visible cue:** a loose, bunched, torn or buried wrap is corrected by adding more tape over the top of
  it rather than peeling all of it off and starting again.
- **SOP rule broken:** Step 2.7 (peel all of the tape off, discard it, and return to 2.2 with a fresh
  start).
- **Coaching note:** strip a bad wrap right back to bare thread. Tape over tape only makes the joint
  thicker and the marks unreachable.

**Violation: Fitting started with the wrench (hand-start skipped).**

- **Visible cue:** the wrench is picked up and set on the fitting before the fitting has been turned on
  by hand to hand-tight, or the very first turns of the fitting are made with the wrench.
- **SOP rule broken:** Hand-start rule and Step 3.4 (turn the fitting on by hand until hand-tight before
  the wrench touches it).
- **Coaching note:** never start a thread with the wrench. Hand-start first; the wrench cannot feel a
  crossthread and drives it in instead of catching it.

**Violation: Fitting crossthreaded.**

- **Visible cue:** the fitting binds within the first two turns, or sits cocked with its face not square
  to the nipple axis, and the operator carries on tightening instead of backing it off.
- **SOP rule broken:** Steps 3.3 and 3.5 (engage the thread start square; if it binds or sits cocked,
  turn it all the way back off and re-start).
- **Coaching note:** line the two axes up and let the thread catch under light force. If it binds early,
  back it off all the way and start again rather than forcing it.

**Violation: Fitting forced onto the thread start.**

- **Visible cue:** the first turn is driven through heavy resistance rather than the fitting being backed
  off and re-lined-up.
- **SOP rule broken:** Step 3.3 (do not force the first turn; a thread that will not catch under light
  force is not lined up).
- **Coaching note:** a correctly lined-up fitting catches easily. Force at the first turn is cutting the
  thread, not tightening it.

**Violation: Wrench set on the nipple or on the taped thread.**

- **Visible cue:** the wrench jaw is set on the nipple, on the vise, or across the taped male thread
  instead of on the body of the fitting.
- **SOP rule broken:** Step 4.2 (set the jaw squarely on the body of the fitting, never on the nipple and
  never on the taped thread).
- **Coaching note:** the wrench only ever goes on the fitting. On the nipple it turns the whole joint; on
  the tape it tears the wrap.

**Violation: Wrench jaw set backwards.**

- **Visible cue:** the jaw is set so that pulling the handle turns the fitting anti-clockwise (loosening)
  rather than clockwise, or the jaw slips off the fitting on the pull.
- **SOP rule broken:** Step 4.2 (jaw facing so that pulling the handle turns the fitting clockwise).
- **Coaching note:** check which way the jaw faces before pulling. A backwards jaw either loosens the
  joint or skates off the fitting.

**Violation: Tightening not continuous (ratcheted or re-set mid-pull).**

- **Visible cue:** the wrench is worked back and forth in short strokes, or the jaw is lifted and re-set
  part way through a pull, rather than one smooth continuous stroke to the marks.
- **SOP rule broken:** Step 4.3 (one smooth, continuous stroke, stopping the moment the marks line up).
- **Coaching note:** one continuous pull. Ratcheting makes it impossible to see the mark arrive and
  usually overshoots it.

**Violation: Tightened on feel instead of to the marks.**

- **Visible cue:** the operator stops the pull without the marks being watched or lined up - the marks
  are ignored and the joint is judged by resistance alone.
- **SOP rule broken:** Step 4.3 (watch the fitting mark travel to the nipple mark and stop when they line
  up).
- **Coaching note:** the marks are the target, not the feel of the joint. Watch the fitting mark all the
  way in.

**Violation: Under-tightened - marks left short.**

- **Visible cue:** the pull ends with the fitting mark still short of the nipple mark, and the operator
  moves on to capping without taking another pull.
- **SOP rule broken:** Step 4.4 (if the marks are short, reset the jaw and take one more continuous pull
  to bring them together).
- **Coaching note:** finish the joint. Marks short means the joint is not made up; take another pull
  rather than leaving it.

**Violation: Over-tightened - marks driven past.**

- **Visible cue:** the pull carries the fitting mark beyond the nipple mark.
- **SOP rule broken:** Step 4.3 (stop the moment the two marks line up).
- **Coaching note:** ease off as the mark comes in and stop on it. Past the mark cannot be undone, only
  flagged.

**Violation: Backed the fitting off to correct an over-tighten.**

- **Visible cue:** an over-tightened joint is turned anti-clockwise to bring the marks back together.
- **SOP rule broken:** Step 4.4 (do not back the fitting off; leave it, flag the assembly, and continue).
- **Coaching note:** never back a made-up joint off to fix the marks. Backing off breaks the tape seal,
  and the joint has to be stripped and re-taped to be good again. Flag it instead.

**Violation: Wrench swing path not clear.**

- **Visible cue:** the pull starts while the other gripper, the input pile, or another assembly is inside
  the arc the handle travels through.
- **SOP rule broken:** Step 4.2 (confirm the wrench swing path is clear of the other arm and of the input
  pile).
- **Coaching note:** clear the swing path before pulling. The handle travels further than it looks.

**Violation: Wrench not returned to its rest.**

- **Visible cue:** at the end of Step 4 the wrench is left on the fitting, on the table, or dropped,
  instead of being carried back to the rest at the front-right.
- **SOP rule broken:** Step 4.5 (carry the wrench back to the rest at the front-right and release it
  there).
- **Coaching note:** put the wrench back on its rest every cycle. A wrench left loose on the table fouls
  the next pick.

**Violation: Open end left uncapped.**

- **Visible cue:** the assembly is staged in the output row with the fitting outlet, or a nipple end,
  still open.
- **SOP rule broken:** Steps 5.2 and 5.3 (every open end carries a cap, turned on hand-tight).
- **Coaching note:** walk the assembly and check every thread before staging it. An uncapped end means
  the assembly is not finished.

**Violation: Cap wrench-tightened.**

- **Visible cue:** the wrench is fetched or used on a cap instead of the cap being turned on by hand.
- **SOP rule broken:** Step 5.2 (caps are hand-tight only; do not fetch the wrench for a cap).
- **Coaching note:** caps go on by hand. They are covers for handling, not sealed joints, and the wrench
  splits them.

**Violation: Assembly placement off zone.**

- **Visible cue:** in Step 6 the assembly is left in the vise or at the center, is released at the
  back-right but ends up noticeably off the designated zone, or is set down touching the assemblies
  already staged, without falling or requiring further correction.
- **SOP rule broken:** Step 6 (carry the assembly to the back-right output zone and set it in the output
  row, not touching the others).
- **Coaching note:** move the finished assembly to the back-right output zone. Do not leave it in the
  vise, and aim the release point so it lands in the row with clear space around it.

**Violation: Fewer than four assemblies completed.**

- **Visible cue:** the episode ends with fewer than four capped assemblies staged in the output row,
  without a hardware or material fault.
- **SOP rule broken:** Step 7 (return to Step 1 with the next nipple until four joints are done).
- **Coaching note:** the episode is four joints. Check the output row count before homing the arms.

**Violation: Wrong arm used for an action.**

- **Visible cue:** any step that specifies the left gripper or the right gripper is performed with the
  opposite gripper.
- **SOP rule broken:** any step that specifies a gripper, including Steps 1, 2.2, 2.4, 2.5, 2.6, 3.1,
  4.1, 4.2, 5.1 and 6.
- **Coaching note:** operator confusion about left vs right roles. Walk through the SOP step by step with
  the operator.

**Violation: Re-grip on a pick or grasp.**

- **Visible cue:** the operator closes on a nipple, fitting, cap, tape end or the wrench, finds the grip
  off, opens, and re-grips before lifting more than two times.
- **SOP rule broken:** Steps 1/2.2/3.1/4.1/5.1 (grasp securely, e.g., around the middle, by the body, or
  by the handle).
- **Coaching note:** approach angle off. Practice the from-above approach so the first grip catches the
  right point.

**Violation: Repeated fiddling with placement or turns.**

- **Visible cue:** the operator makes many small adjustments (more than about two) to settle the clamp,
  the wrap, the fitting or the cap, rather than settling it in one or two corrections.
- **SOP rule broken:** the wrap/start/tighten sub-steps (settle in one or two small adjustments).
- **Coaching note:** grip or approach is off, forcing repeated correction. Tighten the approach so each
  turn lands close to target.

**Violation: Arms not fully at home position at episode end.**

- **Visible cue:** in the final frame, both arms are close to the home position but not exactly at it
  (gripper not fully open, or arm position visibly off home).
- **SOP rule broken:** Step 8 (return to home position with grippers open).
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
- **Vise or wrench fault:** Cause: the vise screw slips under load, the jaws will not hold, the wrench
  jaw fails to bite at its set size, or the vise walks on the table during the pull, through no fault of
  the operator.
- **Tape fault:** Cause: the tape shreds or breaks under normal wrapping tension, or the spool seizes on
  the dispenser, through no fault of the operator.
- **Defective nipple, fitting or cap:** Cause: a burred, damaged or mis-cut thread, a missing or wrongly
  placed alignment mark, or a fitting that cannot reach its mark in any orientation, through no fault of
  the operator. Replace before the next episode.

## After each episode: repeat or reset

- **Batch sessions (e.g., 4x):** the four joints are assembled within the single episode. Once all four
  are tightened to their marks, capped and staged in the output row, reset the workspace before the next
  session.
- Clear the assembly station and re-run the Setup checklist before the next session.

### After the episode: reset the workspace

This part is not recorded. It is just how you reset the table for the next episode.

- With recording off, move the four finished assemblies from the output row back to the start zone.
- Take each assembly apart: remove the caps by hand, then clamp the nipple and back the fitting off with
  the wrench.
- Peel all of the old tape off every male thread and discard it, so each nipple goes back to the input
  pile with clean, bare, dry threads.
- Set the nipples, fittings and caps in the start zone for the next episode's config - back-left
  (Config L), front-center (Config M), or back-right (Config R) - fittings female thread up, caps open end
  up, matching the initial setup state, and leave the other two start zones and the output zone bare.
- Confirm every nipple and fitting still carries a legible alignment mark; re-mark any that have worn.
- Set any assembly flagged in Step 4.4 aside for inspection; do not return it to the input pile.
- Open the vise jaws and return the wrench to its rest at the front-right.
- Confirm the table surface is clear of any objects other than the vise, the wrench, the tape dispenser
  and the parts in their designated zone.
- Go through the Setup checklist again before starting the next episode.

**Warning:** The table must be clear except for the vise at the center, the wrench on its rest, the tape
dispenser at the front-left, and the nipples, fittings and caps in the start zone for the next episode's
config.

## Annotation subtasks

1. Move one nipple from the input area to the vise and clamp it square
2. Hand a part over to the other gripper above the assembly station (Config R nipple; Config L and M
   fitting and cap)
3. Find the tape end and start the tape on the second thread
4. Wrap the male thread with three clockwise turns under tension
5. Break the tape and press the tail down
6. Pick one fitting and orient the female thread to the nipple
7. Start the fitting by hand and turn it to hand-tight
8. Set the wrench on the fitting and tighten to the alignment marks
9. Return the wrench to its rest
10. Cap every open end of the assembly hand-tight
11. Move the finished assembly to the output area
12. Repeat for the next nipple until four joints are assembled
13. Home the arms
