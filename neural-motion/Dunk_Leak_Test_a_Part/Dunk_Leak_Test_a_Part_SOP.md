# Dunk Leak-Test a Part SOP (Fit, Submerge, Observe, Dry, Sort)

This SOP covers dunk leak-testing a single part using a two-arm robot system. Both arms are used
throughout: the grippers cooperate to fit the part to the test manifold, submerge it in the water tank,
hold it still while it is observed for bubbles, dry it with the air nozzle and towel, and place it in the
pass or fail tray, with the left and right grippers taking the specific roles called out in each step.
The task runs from an untested part in the start zone to a dried, sorted part in one of the two output
trays at the back-right.

The table is set up in one of three ways. Only the untested parts move; the manifold, the tank, the drying
station and the two trays are in the same place in all three.

- **Config L:** the untested parts are at the back-left.
- **Config M:** the untested parts are at the back-center, behind the manifold.
- **Config R:** the untested parts are at the front-right, beside the tank.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

- **Start position:** the untested parts start at the back-left (**Config L**), the back-center
  (**Config M**) or the front-right (**Config R**). One config per episode, chosen before recording and never
  changed mid-episode.
- **Same-side rule:** the gripper on the parts' side takes each part from the start zone — the left gripper
  in Config L and M, the right gripper in Config R. No arm reaches across the table.
- **Fixed roles:** whichever gripper brings the part in, it is set down beside the manifold and the right
  gripper takes it from there in Step 2.1. Every gripper role from Step 2 onward is the same in all three
  configs.
- **One part at a time:** exactly one part is fitted, submerged, observed, dried and sorted before the
  next part is touched.
- **Working position:** every part is always brought to the centre of the table and fitted to the
  manifold there, before it goes anywhere near the tank.
- **Fit before pressure, pressure before water:** the part is seated and coupled first, then pressurised
  to test pressure, and only then submerged. The order never changes.
- **Fixed dwell:** every part is held fully submerged and still for the full **10-second dwell** before
  the result is called, whether or not bubbles appear early.
- **Bubbles decide the result:** a **bubble stream** that keeps renewing from the same point on the part
  is a **fail**. **Cling bubbles** that sit on the surface and do not renew are not a leak.
- **Depressurise before uncoupling:** the manifold is vented to zero and the part is lifted clear of the
  water before the coupling is released. A part is never uncoupled under pressure or under water.
- **Dry before sorting:** every part is blown out with the air nozzle and wiped with the towel before it
  reaches a tray. A wet part never goes in a tray.
- **One part, one tray:** a part is tested once and placed in exactly one tray. Nothing is re-tested, and
  nothing is moved from one tray to the other.

## Setup

Go through both checklists before starting the episode.

### Hardware checklist

- Cameras are on and recording
- Env camera frame includes the front and back edges of the table and is centered on the table's
    midpoint
- Env camera frame includes the start zone for this episode's config, the manifold, the full water surface
    of the tank, and both output trays
- Both arms are at the home position with grippers open
- The manifold is bolted down at the center of the table and does not move when tugged
- The regulator reads **zero** and the vent valve is open
- The regulator set point is at the part's **test pressure** and the gauge face is toward the
    operator
- The air nozzle is in its holder at the front-left with the supply on
- Table surface is clear of any objects other than the parts, the manifold, the tank, the nozzle and
    the towel

### Materials checklist

- Untested part(s) are placed in the start zone for this episode's config, dry, in one loose row, port
    facing up, not stacked, with the other two zones bare:
    - **Config L:** back-left
    - **Config M:** back-center, behind the manifold and clear of the working area
    - **Config R:** front-right, beside the tank
- Each part has its **test port** clear and its **sealing face** clean and free of chips or grit
- A seated, undamaged **gasket** is on the manifold test port
- **Blanking caps** are fitted to every other opening on each part
- The **tank** is at the front-center, filled to the **fill line**, and the water is still and clear
- The water is clear enough to read the whole part through it before the first episode
- The **towel** is dry and laid flat at the front-left beside the nozzle holder
- The **pass tray** is at the back-right and the **fail tray** is to its right, both empty and
    labelled toward the operator
- Center of the table is clear apart from the manifold (working area for fitting and pressurising)

## Workspace layout

- **Start zone**: untested parts (input) — back-left (**Config L**), back-center, behind the manifold
  (**Config M**), or front-right (**Config R**). One per episode.
- **Center**: working area with the test manifold (fit, pressurise, vent, uncouple)
- **Front-center**: water tank (submerge and observe)
- **Front-left**: drying station: air nozzle in its holder and the towel laid flat
- **Back-right**: pass tray, and fail tray to its right (output)

## Vocabulary

These are the terms used in this SOP. Operators and annotators must use this language consistently. One
term per concept, used throughout.

### Part anatomy

- **Part:** a single component to be leak-tested in one episode.
- **Test port:** the one opening on the part that couples to the manifold.
- **Sealing face:** the flat rim around the test port that presses onto the gasket.
- **Blanking cap:** a plug fitted to every opening on the part other than the test port.
- **Body:** the main wall of the part, the surface bubbles are read from.
- **Seam:** a joined or welded edge on the part body, a common leak point.
- **Weld:** a fused joint on the part body, a common leak point.
- **Boss:** a raised threaded feature on the part body, a common leak point.
- **Blind pocket:** a recess or cavity on the part that traps air or water.

### Station anatomy

- **Manifold:** the fixed fitting at the center of the table that the part couples to.
- **Coupling:** the quick-connect collar on the manifold that locks the part's test port in place.
- **Gasket:** the seal on the manifold test port that the part's sealing face presses onto.
- **Regulator:** the control that sets and reads the pressure applied to the part.
- **Vent valve:** the valve that releases pressure from the manifold back to zero.
- **Test pressure:** the pressure the part is held at for the whole dwell.
- **Tank:** the open water tank at the front-center that the part is submerged in.
- **Fill line:** the marked water level on the tank that the water must sit at.
- **Water surface:** the top of the water, the line the part passes through.
- **Air nozzle:** the blow gun at the front-left used to clear water off and out of the part.
- **Towel:** the dry cloth at the front-left used to wipe the part after the nozzle.
- **Pass tray:** the left output tray at the back-right, for parts that showed no leak.
- **Fail tray:** the right output tray at the back-right, for parts that leaked.

### Test states

- **Fitted:** the part is seated on the gasket and locked in the coupling, still at zero pressure.
- **Pressurised:** the part is fitted and the regulator is holding at test pressure.
- **Submerged:** the whole part, including the coupling joint, is under the water surface.
- **Dwell:** the 10 seconds the part is held submerged, still and pressurised, while it is observed.
- **Vented:** the vent valve is open and the regulator has fallen back to zero.
- **Dried:** the part has been blown out with the nozzle and wiped with the towel, inside and out.

### Bubble reading

- **Bubble stream:** bubbles that keep coming from the same point on the part and renew after they rise.
  A bubble stream is a **leak**.
- **Cling bubble:** a bubble sitting on the part surface that was carried in on entry. It does not renew
  once it releases, and it is **not** a leak.
- **Leak point:** the exact spot on the part a bubble stream comes from: a seam, weld, boss or the
  sealing face.
- **Joint bubbles:** a stream from the coupling or gasket rather than from the part body. This is a bad
  fit, not a part failure.
- **Pass:** the full dwell finished with no bubble stream anywhere on the part body.
- **Fail:** a bubble stream was seen coming from a point on the part body during the dwell.

### Workspace zones

- **Start zone:** input zone holding the untested parts — back-left (**Config L**), back-center, behind the
  manifold (**Config M**), or front-right (**Config R**). One per episode, chosen before recording and never
  changed mid-episode.
- **Working area:** the center of the table, where the manifold sits and fitting happens.
- **Tank zone:** the front-center of the table, where the part is submerged and observed.
- **Drying station:** the front-left of the table, holding the air nozzle and the towel.
- **Back-right edge:** output zone holding the pass tray and, to its right, the fail tray.
- **Home position:** the default resting pose for each arm: gripper open and clear of the table.

### Actions

- **Pick:** lift one part clear of the input row and carry it to the working area.
- **Fit:** seat the part's sealing face on the gasket and lock it into the coupling.
- **Pressurise:** close the vent valve and bring the regulator up to test pressure.
- **Submerge:** lower the part through the water surface until the whole part and its joint are under
  water.
- **Observe:** watch the part through the water for the full dwell and read the bubbles.
- **Call:** state the result, pass or fail, once the dwell has finished.
- **Vent:** open the vent valve and let the regulator fall back to zero.
- **Uncouple:** release the coupling collar and lift the part off the manifold.
- **Blow out:** run the air nozzle over and into the part until no water comes out.
- **Wipe:** dry the outside of the part with the towel.
- **Sort:** place the dried part in the pass tray or the fail tray according to the call.
- **Sweep:** check the working area, the tank and the drying station are clear at the end of the episode.

## Steps

Only Step 1 depends on where the parts start: in Config L and M the **left gripper** takes the part from the
start zone; in Config R the **right gripper** takes it from the front-right. In all three the part is set
down beside the manifold, and every line from Step 2 onward is the same in all configs.

### Step 1: Move one part to the working area

**Goal:** exactly one part sits in the working area beside the manifold, ready to be fitted.

Look where the parts are before reaching for one.

- **IF the parts are at the back-left (Config L):** with the **left gripper**, grasp one part from the row
  at the middle of its body.
- **IF the parts are at the back-center (Config M):** with the **left gripper**, grasp one part from the
  row behind the manifold at the middle of its body.
- **IF the parts are at the front-right (Config R):** with the **right gripper**, grasp one part from the
  row at the middle of its body.

Then, in all three:

- Lift it clear of the table and carry it to the center; do not drag or slide it.
- If a second part comes up with it, set both down in the working area, return the extra part to the start
  zone, and carry on with the first.
- Set the part down beside the manifold with its **test port** facing up, and release.

### Step 2: Fit the part to the manifold

**Goal:** the part is seated square on the gasket and locked in the coupling, with every other opening
capped and the manifold still at zero.

#### 2.1 Inspect the part and the gasket

- With the right gripper, raise the part until its base clears the table and turn it once so the body,
  the sealing face and every opening come into view.
- Confirm the **sealing face** is clean and unchipped and that a **blanking cap** is fitted to every
  opening other than the test port.
- Confirm the **gasket** on the manifold is seated in its groove, flat, and undamaged. If the gasket is
  torn, pinched or out of its groove, stop and report a station fault.
- Confirm the **regulator** reads zero and the **vent valve** is open before anything is coupled.

#### 2.2 Seat the part on the gasket

- With the right gripper, hold the part by the middle of its body and bring the test port down square
  over the manifold gasket.
- With the left gripper, steady the far side of the part so it lands level, not tilted.
- Lower until the sealing face makes flat contact all the way round the gasket.
- If the part lands tilted or off the gasket, lift clear and re-aim rather than sliding it into place.

#### 2.3 Lock the coupling

- With the right gripper, hold the part down onto the gasket.
- With the left gripper, turn the **coupling** collar until it locks onto the test port.
- Release the right gripper and tug the part gently upward: a fitted part does not lift off the manifold.
- If the part lifts, or the collar did not reach its lock, unlock, re-seat from 2.2 and lock again.

#### 2.4 Pressurise to test pressure

- With the left gripper, close the **vent valve**.
- With the right gripper, bring the **regulator** up until the gauge reads the part's **test pressure**.
- Hold at test pressure and confirm the gauge is steady before the part goes near the water.
- If the gauge will not reach or will not hold test pressure with the part fitted, vent to zero, re-seat
  from 2.2, and pressurise again.
- Never carry a part toward the tank before the gauge is steady at test pressure.

### Step 3: Submerge the part in the tank

**Goal:** the whole part and its coupling joint sit under the water surface, still and pressurised.

- Confirm the water is at the **fill line** and the surface is still before the part goes in.
- With the right gripper, grasp the manifold arm at the middle and swing the fitted part over the tank;
  with the left gripper, steady the far side of the part.
- Lower the part through the **water surface** in one slow, smooth motion until the whole part **and the
  coupling joint** are under water.
- Enter slowly and without splashing. A fast entry drags air down with the part and fills the water with
  bubbles that cannot be read.
- Turn any **blind pocket** downward on the way in so it does not carry a pocket of trapped air under.
- Release both grippers and let the part settle. The dwell does not start until the part is still.

### Step 4: Observe for bubbles

**Goal:** the part is watched for the full dwell and the result is called from what the bubbles show.

#### 4.1 Hold the dwell

- Hold the part submerged, still and at test pressure for the full **10-second dwell**.
- Keep both grippers clear of the part and off the tank so the water stays still.
- Do not shorten the dwell because bubbles appeared early, and do not extend it because none did.

#### 4.2 Read the bubbles

- A **bubble stream** is bubbles that keep coming from the same point on the part body and renew after
  each one rises. A bubble stream is a **leak**.
- A **cling bubble** is a bubble carried in on entry that sits on the surface and does not renew once it
  releases. Cling bubbles are **not** a leak.
- Watch the **seams, welds and bosses** first; these are where a leak shows.
- Track each stream back to its **leak point** on the part before calling it.

#### 4.3 Separate joint bubbles from part bubbles

- If the stream comes from the **coupling or the gasket** rather than from the part body, these are
  **joint bubbles**: a bad fit, not a part failure.
- For joint bubbles, lift the part clear of the water, vent to zero per Step 5, re-seat from 2.2 and run
  the test again from Step 2.4. Do not call a result off a leaking joint.
- Do not call a **fail** off a stream you could not track back to a point on the part body.

#### 4.4 Call the result

- **Pass:** the full dwell finished with no bubble stream anywhere on the part body.
- **Fail:** a bubble stream was seen coming from a point on the part body during the dwell.
- Call exactly one result, once, at the end of the dwell. The call does not change after this point.

### Step 5: Withdraw, vent and uncouple

**Goal:** the part is out of the water, the manifold is back at zero, and the part is off the manifold
undamaged.

- With the right gripper, raise the part in one slow motion until the whole part and the coupling joint
  are clear of the water surface.
- Hold the part over the tank for a moment and let the loose water run back into the tank.
- Swing the part back over the working area at the center of the table.
- With the left gripper, open the **vent valve** and confirm the regulator has fallen back to **zero**.
- **Never uncouple under pressure and never uncouple under water:** the part comes out of the tank first,
  then the manifold is vented to zero, and only then is the collar released.
- With the left gripper, turn the **coupling** collar to unlock; with the right gripper, hold the part.
- Lift the part straight up off the gasket and carry it to the drying station at the front-left.

### Step 6: Dry the part

**Goal:** the part is dry inside and out, with no water left in it, before it reaches a tray.

- With the left gripper, hold the part over the tank; with the right gripper, take the **air nozzle**
  from its holder.
- Blow out the **test port** first, then each **blind pocket**, turning the part with the left gripper so
  every pocket points down as it is blown.
- Work the nozzle over the whole body, including the seams, welds and bosses, until no more water comes
  out.
- Return the nozzle to its holder before picking up the towel.
- With the right gripper, take the **towel** and wipe the outside of the part dry, including the sealing
  face.
- Lay the towel back flat at the front-left.
- Turn the part once with the left gripper and confirm no water runs out and no wet film is left. If
  water still comes out, return to the nozzle and blow it out again.
- A part that is still wet does not go in a tray.

### Step 7: Sort the part into the pass or fail tray

**Goal:** the dried part rests in the tray that matches the result called in Step 4.

- With the right gripper, grasp the dried part at the middle of its body.
- Read the tray labels on the way: the **pass tray** is on the left, the **fail tray** is on its right.
- **Pass** parts go in the **pass tray**. **Fail** parts go in the **fail tray**.
- Bring the part over the tray so the whole part sits inside the tray outline, then lower it until it
  touches down and release.
- Never throw, toss or drop a part toward a tray from outside the tray outline.
- Set the part down flat and clear of the parts already in the tray; do not stack parts on top of each
  other.
- Once the gripper has opened over a tray, the part stays in that tray. Never move a part from one tray
  to the other, and never re-test a part that has been sorted.

### Step 8: Sweep and reset the station

**Goal:** the station is clear and ready, and every part that was tested is in exactly one tray.

- Confirm the part landed inside the tray and is not resting on the tray rim or across two trays.
- Confirm the manifold is empty, the regulator reads **zero**, and the **vent valve** is left open.
- Confirm the gasket is still seated in its groove and undamaged before the next part.
- Confirm the air nozzle is back in its holder and the towel is laid flat at the front-left.
- Confirm the tank water is back at the **fill line** and no part or cap has been left in the tank.
- Confirm the working area holds no part, cap or debris before the next pick.
- Return to Step 1 while the start zone still holds untested parts.

**Warning:** every part taken from the input row should now be in exactly one tray, dry, with the
manifold vented to zero and the tank clear.

### Step 9: Return to home and end the episode

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

**Note on the start position:** the violations below were written for Config L (untested parts start in a
row at the back-left). The pickup and arm-role cues will be rewritten later to cover all three start
positions; they are left as they are for now. Until then, anything that does not match the episode's config
goes under **Config misaligned**.

**Violation: Config misaligned.**

- **Visible cue:** what the operator does does not match the config on the table — the untested parts are
  not in the start zone for the config; a gripper reaches across the table for a part; or the wrong IF line
  is followed.
- **SOP rule broken:** the start position and the same-side rule (the left gripper takes the part from the
  start zone in Config L and M, the right gripper in Config R; no arm reaches across the table; the IF line
  followed is the one for the config on the table).
- **Coaching note:** look where the parts are before the first reach, then follow that config's IF line
  through Step 1.

**Violation: Wrong pickup.**

- **Visible cue:** the part is started from the center, the tank, the drying station or a tray instead of
  the back-left row (input row), it is placed outside the center working area, or the part is dragged or
  slid across the table instead of being picked up (lifted clear of the surface) and carried.
- **SOP rule broken:** Step 1 (pick from the back-left row and place it in the center working area). Pick
  means lift and carry, not drag.
- **Coaching note:** always start each part from the back-left row and bring it to the center before
  fitting. Lift the part clear of the table and carry it. Do not drag or slide it across the surface.

**Violation: Picked more than one part at once.**

- **Visible cue:** two or more parts are lifted or carried from the input row in a single pick, or a
  second part comes up with the first and is carried on with instead of being returned to the row.
- **SOP rule broken:** Step 1 (move one part, one part at a time).
- **Coaching note:** pick exactly one part at a time. If a second part comes up, set it down and return
  it to the back-left row before carrying on.

**Violation: Blanking cap missing or not checked.**

- **Visible cue:** the part goes into the tank with an uncapped opening other than the test port, or the
  operator never turns the part to check every opening in 2.1.
- **SOP rule broken:** Step 2.1 (confirm a blanking cap is fitted to every opening other than the test
  port).
- **Coaching note:** turn the part once and check every opening before fitting. An uncapped opening blows
  a stream that reads as a failure but is really an open port.

**Violation: Part fitted onto a damaged or unseated gasket.**

- **Visible cue:** the part is seated and coupled while the gasket is torn, pinched, or sitting out of
  its groove, instead of the operator stopping and reporting a station fault.
- **SOP rule broken:** Step 2.1 (confirm the gasket is seated, flat and undamaged before coupling).
- **Coaching note:** check the gasket before every fit. A bad gasket leaks at the joint and wastes the
  whole test.

**Violation: Part seated tilted or off the gasket.**

- **Visible cue:** the sealing face does not make flat contact all the way round the gasket, or the
  operator slides a tilted part sideways into place instead of lifting clear and re-aiming.
- **SOP rule broken:** Step 2.2 (bring the test port down square and land the part level; lift clear and
  re-aim rather than sliding it into place).
- **Coaching note:** land the part square and level in one motion. Sliding a tilted part across the
  gasket rolls and damages it.

**Violation: Coupling not locked (fit not confirmed).**

- **Visible cue:** the collar is not turned to its lock, or the operator never tugs the part upward to
  confirm the fit, and moves on to pressurising anyway.
- **SOP rule broken:** Step 2.3 (lock the collar and tug the part upward to confirm it does not lift
  off).
- **Coaching note:** lock the collar and confirm with a gentle tug every time. An unlocked part can blow
  off the manifold under pressure.

**Violation: Submerged without pressurising (pressure skipped).**

- **Visible cue:** the part goes into the water with the vent valve still open or the regulator still at
  zero, or the operator carries it to the tank before the gauge is steady at test pressure.
- **SOP rule broken:** Step 2.4 (close the vent, bring the regulator to test pressure, confirm the gauge
  is steady) and Step 3.
- **Coaching note:** fit, then pressurise, then submerge. An unpressurised part cannot bubble, so the
  dwell shows nothing.

**Violation: Wrong test pressure.**

- **Visible cue:** the regulator is left short of, or driven past, the part's test pressure, or the gauge
  is still drifting when the part is carried to the tank.
- **SOP rule broken:** Step 2.4 (bring the regulator to the part's test pressure and confirm the gauge is
  steady).
- **Coaching note:** read the gauge face before moving. Under pressure hides real leaks; over pressure
  can damage the part.

**Violation: Part not fully submerged.**

- **Visible cue:** part of the body, or the coupling joint, stays above the water surface for any of the
  dwell.
- **SOP rule broken:** Step 3 (lower until the whole part and the coupling joint are under water).
- **Coaching note:** put the whole part under, joint included. A leak above the waterline never shows a
  bubble.

**Violation: Splashed or dropped entry.**

- **Visible cue:** the part is pushed or dropped through the water surface fast enough to splash and
  churn the water, rather than being lowered in one slow, smooth motion.
- **SOP rule broken:** Step 3 (lower slowly and smoothly, without splashing).
- **Coaching note:** enter slowly. A fast entry drags air down and fills the water with bubbles that
  cannot be read.

**Violation: Dwell cut short.**

- **Visible cue:** the part is lifted, or the result is called, before the full 10-second dwell has run,
  usually after bubbles appear early.
- **SOP rule broken:** Step 4.1 (hold the full 10-second dwell before the result is called).
- **Coaching note:** run the full dwell every time, whatever the bubbles do. A short dwell misses slow
  leaks and makes episodes inconsistent.

**Violation: Part disturbed during the dwell.**

- **Visible cue:** a gripper touches, turns or repositions the part, or leans on the tank, while the
  dwell is running, so the water is not still.
- **SOP rule broken:** Step 4.1 (keep both grippers clear of the part and off the tank during the dwell).
- **Coaching note:** release and stand clear once the part is settled. Moving the part shakes loose
  bubbles that read as a leak.

**Violation: Cling bubbles called as a leak.**

- **Visible cue:** the result is called a fail off bubbles that were carried in on entry and do not
  renew, or off a stream that was never tracked back to a point on the part body.
- **SOP rule broken:** Step 4.2 (a bubble stream renews from the same point; cling bubbles are not a
  leak) and Step 4.4.
- **Coaching note:** watch whether the bubbles renew and find the leak point before calling. A bubble
  that releases and never returns is air off the entry, not a leak.

**Violation: Joint bubbles called as a part failure.**

- **Visible cue:** a stream from the coupling or the gasket is called a part fail instead of being
  treated as a bad fit and re-run.
- **SOP rule broken:** Step 4.3 (joint bubbles are a bad fit, not a part failure: re-seat and run the
  test again).
- **Coaching note:** track the stream to its source. A leak at the joint is the station's fault, not the
  part's; re-seat and re-run.

**Violation: No result called.**

- **Visible cue:** the part is withdrawn, dried and sorted without a pass or fail being called at the end
  of the dwell.
- **SOP rule broken:** Step 4.4 (call exactly one result, once, at the end of the dwell).
- **Coaching note:** call the result out loud at the end of every dwell, before the part leaves the tank.

**Violation: Uncoupled under pressure.**

- **Visible cue:** the coupling collar is released while the regulator still reads above zero, or before
  the vent valve is opened.
- **SOP rule broken:** Step 5 (vent to zero and confirm the regulator has fallen before the collar is
  released).
- **Coaching note:** vent first, confirm zero on the gauge, then unlock. Releasing under pressure throws
  the part off the manifold.

**Violation: Uncoupled under water.**

- **Visible cue:** the collar is released, or the part is taken off the manifold, while the part or the
  joint is still below the water surface.
- **SOP rule broken:** Step 5 (raise the part clear of the water surface before venting and uncoupling).
- **Coaching note:** bring the part out of the tank first. Uncoupling under water floods the part and the
  manifold.

**Violation: Part sorted while still wet (drying skipped).**

- **Visible cue:** the part goes to a tray without the nozzle, without the towel, or with water still
  running out of it when it is turned.
- **SOP rule broken:** Step 6 (blow out and wipe the part, inside and out, before it reaches a tray).
- **Coaching note:** blow out every pocket and the test port, wipe the outside, and turn the part to
  confirm it is dry. A wet part never goes in a tray.

**Violation: Blind pockets not blown out.**

- **Visible cue:** the nozzle is run over the outside only, with the part never turned so each pocket
  points down, and water runs out of the part after it is set down.
- **SOP rule broken:** Step 6 (blow out the test port and each blind pocket, turning the part so every
  pocket points down).
- **Coaching note:** turn the part as you blow so each pocket empties. Trapped water carries into the
  tray and onto the next episode.

**Violation: Nozzle or towel not returned.**

- **Visible cue:** the air nozzle is left out of its holder, or the towel is left bunched, dropped, or
  somewhere other than flat at the front-left.
- **SOP rule broken:** Step 6 and Step 8 (return the nozzle to its holder and lay the towel back flat).
- **Coaching note:** put the nozzle back before picking up the towel, and lay the towel flat before
  moving on.

**Violation: Wrong tray (result and tray do not match).**

- **Visible cue:** a part called pass is placed in the fail tray, or a part called fail is placed in the
  pass tray.
- **SOP rule broken:** Step 7 (pass parts go in the pass tray, fail parts in the fail tray; the pass tray
  is on the left).
- **Coaching note:** read the tray label again on the way over. A mis-sorted fail ships a leaking part.

**Violation: Part thrown or tossed toward a tray.**

- **Visible cue:** the part is released from outside the tray outline and travels to the tray through the
  air, or is thrown, lobbed or flicked at the tray row.
- **SOP rule broken:** Step 7 (bring the part over the tray, lower it until it touches down, and
  release).
- **Coaching note:** carry every part over the tray and lower it in. Nothing is released from outside the
  outline.

**Violation: Part moved between trays or re-tested.**

- **Visible cue:** after the gripper has opened over a tray, the operator moves the part to the other
  tray, or takes a sorted part back to the manifold for a second test.
- **SOP rule broken:** Step 7 (one part, one tray: a sorted part is never moved between trays and never
  re-tested).
- **Coaching note:** call the result once and place it once. A wrong tray is flagged and left alone, not
  corrected on the table.

**Violation: Parts stacked in a tray.**

- **Visible cue:** the part is set down on top of a part already in the tray instead of flat and clear of
  it.
- **SOP rule broken:** Step 7 (set the part down flat and clear of the parts already in the tray).
- **Coaching note:** leave space in the tray so every part stays visible and countable at the end of the
  session.

**Violation: Manifold left pressurised or vent left closed.**

- **Visible cue:** the episode ends, or the next part is picked, with the regulator reading above zero or
  the vent valve still closed.
- **SOP rule broken:** Step 8 (the manifold is empty, the regulator reads zero, and the vent valve is
  left open).
- **Coaching note:** vent the manifold and leave the valve open before reaching for the next part.

**Violation: Station not swept (part, cap or debris left behind).**

- **Visible cue:** the episode ends with a part or a blanking cap left in the tank, on the manifold, at
  the drying station, or in the working area.
- **SOP rule broken:** Step 8 (sweep the working area, the tank and the drying station before homing).
- **Coaching note:** sweep all three zones before homing, including the bottom of the tank.

**Violation: Wrong arm used for an action.**

- **Visible cue:** any step that specifies the left gripper or the right gripper is performed with the
  opposite gripper.
- **SOP rule broken:** any step that specifies a gripper, including Steps 1, 2.1, 2.2, 2.3, 2.4, 3, 5, 6
  and 7.
- **Coaching note:** operator confusion about left vs right roles. Walk through the SOP step by step with
  the operator.

**Violation: Re-grip on a pick or grasp.**

- **Visible cue:** the operator closes on a part, finds the grip off, opens, and re-grips before lifting
  more than two times.
- **SOP rule broken:** Steps 1/2.2/5/7 (grasp securely at the middle of the body).
- **Coaching note:** approach angle off. Practice the from-above approach so the first grip catches the
  middle of the body.

**Violation: Repeated fiddling with the fit, the regulator or the placement.**

- **Visible cue:** the operator makes many small adjustments (more than about two) to seat the part,
  settle the regulator, or square the part in a tray, rather than settling it in one or two corrections.
- **SOP rule broken:** the fit/pressurise/sort sub-steps (settle in one or two small adjustments).
- **Coaching note:** grip or approach is off, forcing repeated correction. Tighten the approach so each
  seat and each placement lands close to target.

**Violation: Arms not fully at home position at episode end.**

- **Visible cue:** in the final frame, both arms are close to the home position but not exactly at it
  (gripper not fully open, or arm position visibly off home).
- **SOP rule broken:** Step 9 (return to home position with grippers open).
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
- **Air supply lost or regulator fault:** Cause: the supply drops out, or the regulator will not hold or
  read pressure with a known-good part fitted. Repair before the next episode.
- **Gasket failed on the manifold:** Cause: the manifold gasket tears or extrudes under normal pressure.
  Replace the gasket before the next episode.
- **Defective part:** Cause: a cracked, chipped or misshapen part that cannot be sealed to the manifold
  at all, through no fault of the operator. Replace before the next episode.
- **Water clouded or below the fill line:** Cause: the tank goes cloudy, oily or low so bubbles cannot be
  read through it. Refill or change the water before the next episode.

## After each episode: repeat or reset

- **Batch sessions (e.g., 5x):** if fewer than the target number of parts are tested, return to Step 1
  with the next part. Once the target number is tested and sorted, reset the workspace before the next
  session.
- Clear the working area and re-run the Setup checklist before the next session.

### After the episode: reset the workspace

This part is not recorded. It is just how you reset the table for the next episode.

- With recording off, confirm the regulator reads zero and the vent valve is open.
- Move the parts from the pass tray and the fail tray back to the start zone for the next episode's config
  — back-left (Config L), back-center (Config M), or front-right (Config R).
- Lay them out in one loose row, dry, port facing up, not stacked, so the input zone matches the initial
  setup state.
- Re-fit any blanking cap that came off, and confirm every opening other than the test port is capped.
- Wipe each part dry again and confirm no water is left in any blind pocket.
- Inspect the manifold gasket and replace it if it is torn, pinched or flattened.
- Top the tank back up to the fill line and let the water settle still and clear.
- Fish out anything that fell into the tank and dry it before it returns to the input row.
- Hang the towel to dry and lay out a dry one flat at the front-left, and return the nozzle to its
  holder.
- Return both trays empty to the back-right, pass tray on the left, labels toward the operator.
- Wipe the working area and the drying station dry and confirm both are clear.
- Confirm the table surface is clear of any objects other than the parts, the manifold, the tank, the
  nozzle and the towel.
- Go through both Setup checklists again before starting the next episode.

**Warning:** The table must be clear except for the parts in the start zone, the manifold at the center,
the tank at the front-center, the nozzle and towel at the front-left, and the two trays at the
back-right.

## Annotation subtasks

1. Move one part from the input row to the center working area
2. Fit the part to the manifold (inspect, seat on the gasket, lock the coupling)
3. Pressurise the part to test pressure and confirm the gauge holds
4. Submerge the part in the tank (whole part and joint under water)
5. Observe for bubbles through the full dwell and call pass or fail
6. Re-seat and re-run a test that showed joint bubbles
7. Withdraw the part, vent the manifold to zero, and uncouple
8. Dry the part with the air nozzle and the towel
9. Sort the part into the pass tray or the fail tray
10. Sweep the station and reset the manifold
11. Home the arms
