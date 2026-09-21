# Wire Six Terminal Blocks SOP (1x Episode: 6 Terminals)

One episode wires all six terminals on one terminal strip. The table begins with the **terminal board** on the
assembly spot, just right of the center of the table. A six-position **terminal strip** runs across the middle
of the board, its terminals numbered **1** at the left to **6** at the right. Each terminal has a **screw** on
its top face and a **hole** in its front face. A **wire comb** with six numbered **channel slots** runs along
the front edge of the board. A **lead rack** holding six stripped, color-coded **leads** sits in the **start
zone**, and a **driver** stands in the **driver stand**; the config below says where each one is.

The order never changes: insert all six leads per the **color map**, working terminal 1 through 6; then screw
all six terminals down with the driver, again 1 through 6; then park the driver and tug-test all six leads, 1
through 6; then dress the six leads into the comb. No screw is turned until all six leads are in their holes.
No lead is tug-tested with the driver still in the gripper. Nothing is dressed until every lead has passed its
tug test. The episode does not end until all six leads sit in their channel slots.

The right gripper picks each lead, inserts it, drives every screw, tug-tests every lead, and dresses every
wire. The left gripper presses the terminal board flat against the table by its left edge and holds it there
for the whole episode, so the board cannot slide while a lead goes in, a screw turns, or a lead is pulled. The
left gripper stays on the left edge of the board and never reaches across it. The right gripper works the
board, the lead rack, the driver stand, and the comb.

The table is set up in one of three ways. Only the lead rack moves; the terminal board, the color map, and
the comb are in the same place in all three. The driver stand keeps the back-right except in Config R2,
where the rack takes that corner and the stand moves to the front-right.

* **Config M:** the lead rack is at the back-center, behind the board.
* **Config R1:** the lead rack is at the front-right.
* **Config R2:** the lead rack is at the back-right, and the driver stand is at the front-right.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the lead rack starts at the back-center (**Config M**), the front-right
  (**Config R1**) or the back-right (**Config R2**). One config per episode, chosen before recording and
  never changed mid-episode.
* **Same-side rule:** the **right gripper** takes every lead from the rack in all three configs. There is no
  left-side config, because the left gripper holds the board's left edge for the whole episode and the
  right gripper never reaches across the board. Nothing is handed over.
* **Fixed roles:** everything else is the same in all three configs — the left gripper holds the board, the
  right gripper inserts, screws, tug-tests, and dresses, and the four phases run in the order above.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the terminal board with all six terminals, the color map
   card, the wire comb, the lead rack in the start zone for this episode's config, and the driver stand.
3. The terminal board is visible from above and from the front, so all six screws, all six holes, the
   **insulation shoulder** of each lead, and all six channel slots can be seen.
4. Both arms are at home with grippers open.
5. The table is bare apart from the terminal board, the color map card, the lead rack, the driver stand, and
   robot hardware.
6. The right arm reaches the lead rack — at the back-center (Config M), the front-right (Config R1), or the
   back-right (Config R2) — terminal 1, terminal 6, the driver stand, and the comb without stretching. The
   left arm reaches the left edge of the terminal board without stretching.

### Materials checklist

1. One **terminal board** lies on the **assembly spot**, just right of the center of the table, **square** to
   the front edge and flat on the table.
2. The **terminal strip** is fixed across the middle of the board. Its six terminals are numbered **1** at the
   left to **6** at the right, and the numbers are printed on the strip and readable from above.
3. Every terminal **screw** starts **open**: backed off far enough that a stripped end slides into the hole
   below it without being forced.
4. Every terminal **hole** is empty and clear.
5. The **color map** card is fixed at the back of the board, behind the strip, and reads: terminal 1 brown,
   terminal 2 red, terminal 3 orange, terminal 4 yellow, terminal 5 green, terminal 6 blue.
6. The **lead rack** sits in the start zone for this episode's config, and the other two zones are empty:
   * **Config M:** back-center, behind the board
   * **Config R1:** front-right
   * **Config R2:** back-right, where the driver stand normally stands

   It has six **rack slots**, numbered 1 at the left to 6 at the right. Each slot is labeled with one color
   and holds that one lead: slot 1 blue, slot 2 green, slot 3 yellow, slot 4 orange, slot 5 red, slot 6
   brown.
7. All six **leads** are solid-core, one color each, cut to the same length, and stripped at one end only. The
   **stripped end** is bare copper, straight, with no kink, and about as long as the terminal hole is deep.
8. The **wire comb** runs along the front edge of the board with six open **channel slots**, numbered 1 at the
   left to 6 at the right, one slot in front of each terminal.
9. One **driver** stands in the **driver stand**, handle up, blade down, matching the screw slots. The stand
   is at the back-right in Config M and R1. **IF Config R2**, it is at the front-right, clear of the comb.
10. Keep the left side of the table clear. The left gripper comes in from there onto the board's left edge.
11. Before collection, confirm by hand that:
    - each stripped end slides into its hole without force;
    - a closed screw holds its lead against a light pull;
    - the driver blade sits in a screw slot without slipping;
    - a lead presses down into its channel slot and stays there.

### Workspace layout

- **Assembly spot:** just right of the center of the table — the terminal board stays here all episode
- **Middle of the board:** the terminal strip, terminals 1 to 6 left to right
- **Back of the board:** the color map card
- **Front edge of the board:** the wire comb, channel slots 1 to 6 left to right
- **Start zone:** the lead rack with six leads — back-center, behind the board (**Config M**), front-right
  (**Config R1**), or back-right (**Config R2**)
- **Tool zone:** the driver stand — back-right in Config M and R1, front-right in Config R2
- **Left side:** kept clear, so the left gripper can come in onto the board's left edge

### Arm assignments

- **Left gripper:** presses the terminal board flat by its left edge and holds it there for the whole episode,
  so the board cannot slide while the right gripper works.
- **Right gripper:** reads off the color map, picks each lead from the rack in whichever start zone the
  config puts it, pushes it into its terminal, picks up and parks the driver, turns every screw, tug-tests
  every lead, and presses every lead into its channel slot.

## Vocabulary

- **Assembly spot:** the place on the table, just right of center, where the terminal board sits. The board
  stays here for the whole episode.
- **Square:** the front edge of the board lines up with the front edge of the table, so the strip runs level
  across the board and neither end of the board sits nearer the front.
- **Terminal board:** the flat board the terminal strip is mounted on. It stays on the assembly spot for the
  whole episode and is never lifted.
- **Terminal strip:** the block of six terminals fixed across the middle of the board.
- **Terminal:** one wiring position on the strip. Each one has its own number, screw, and hole.
- **Terminal number:** the number printed on the strip beside each terminal, 1 at the left to 6 at the right.
- **Screw:** the small slotted screw on top of a terminal. Turning it clockwise clamps the lead in the hole
  below it.
- **Screw slot:** the straight groove across the head of a screw that the driver blade sits in.
- **Hole:** the opening in the front face of a terminal that the stripped end goes into.
- **Lead:** one colored wire. Six leads are wired in one episode.
- **Insulation:** the colored plastic covering along the lead.
- **Stripped end:** the bare copper at one end of a lead, with the insulation removed.
- **Insulation shoulder:** the step where the insulation ends and the bare copper begins.
- **Fully home:** the stripped end is all the way inside the hole and the insulation shoulder touches the front
  face of the terminal, so no bare copper shows outside the hole.
- **Color map:** the card at the back of the board that says which lead color goes in which terminal.
- **Start zone:** where the lead rack sits at the start of the episode — back-center, behind the board
  (**Config M**), front-right (**Config R1**), or back-right (**Config R2**). One per episode, chosen before
  recording and never changed mid-episode.
- **Lead rack:** the holder with six numbered slots, one lead per slot. It sits in the start zone.
- **Rack slot:** one numbered slot in the lead rack. Each slot is labeled with the color of the lead it holds.
- **Driver:** the screwdriver used to turn the terminal screws.
- **Driver stand:** the holder the driver stands in when it is not in the right gripper — at the back-right
  in Config M and R1, at the front-right in Config R2.
- **Blade seated:** the driver blade sits down in the screw slot, in line with it, and does not skate out when
  the screw is turned.
- **Screw closed:** the screw has been turned clockwise until it stops turning.
- **Tug test:** a light, steady pull on a lead, straight out away from the front face of the terminal, for a
  count of one.
- **Holds:** the lead does not move at all during its tug test.
- **Pulls out:** the lead slides out of the hole, or the insulation shoulder lifts off the terminal face,
  during its tug test.
- **Wire comb:** the strip along the front edge of the board with six open channel slots.
- **Channel slot:** one numbered slot in the comb. Lead 1 goes in slot 1, lead 2 in slot 2, and so on.
- **Dressed:** the lead is pressed down into its channel slot, below the top of the comb, and stays there when
  the right gripper lets go.
- **Crossing:** two leads lie over each other between the strip and the comb.
- **Kink:** a sharp bend in the bare copper of a stripped end. A kinked end does not go fully home.

## Steps

Run Steps 1–5 in order on the one terminal strip, then end the episode with Step 6. Only 2.1 and 3.1 depend
on the config: in 2.1 the **right gripper** reaches to wherever the rack is, and in 3.1 it takes the driver
from the back-right or, in Config R2, the front-right. Every other line is the same in all three configs.

### Step 1: Hold the terminal board down

**Goal:** the terminal board is pinned flat on the assembly spot and cannot slide for the rest of the episode.

- With the **left gripper**, press down on the **left edge** of the terminal board and hold it against the
  table.
- Keep the **left gripper** there through Steps 2, 3, 4, and 5.

**Check:** the board is flat on the table, **square** to the front edge, and does not slide when the left
gripper presses. If the board is crooked, straighten it with the **left gripper** first, then press it down.

**Expected state:** the board is held, all six holes are empty, and all six screws are open.

### Step 2: Insert all six leads per the color map

**Goal:** all six stripped ends are fully home in the right terminals, with no screw turned yet.

- With the **left gripper**, keep pressing the terminal board down.
- Work **terminal 1 first, then 2, 3, 4, 5, 6**. Do one lead at a time.
- Turn no screw in this step. The **right gripper** leaves the **driver** standing in its stand.
- With the **right gripper**, carry each lead in one go, straight from the rack to its terminal. Do not set a
  lead down on the board or the table on the way.
- Hold each lead by its **insulation** with the **right gripper** only. Never pinch the **stripped end**, and
  never bend or **kink** it.

#### 2.1 Pick the right lead

Look where the lead rack is before reaching for the first lead.

- **IF the rack is at the back-center (Config M):** the **right gripper** reaches back over the strip to the
  rack behind the board, and brings each lead forward over the board to the front face of its terminal.
- **IF the rack is at the front-right (Config R1):** the **right gripper** reaches to the rack at the
  front-right and brings each lead left along the front of the board to its terminal.
- **IF the rack is at the back-right (Config R2):** the **right gripper** reaches to the rack in the
  back-right corner, where the driver stand normally stands, and brings each lead forward and left to its
  terminal.

Then, in all three:

- Read the **color map** for the terminal being wired, and find that color's **rack slot**.
- With the **right gripper**, pinch that lead by its insulation, a little way back from the stripped end, and
  lift it straight up out of the rack.

#### 2.2 Push the lead fully home

- With the **right gripper**, bring the **stripped end** to the **hole** in the front face of that terminal and
  line it up with the hole.
- With the **right gripper**, push the lead straight into the hole until the **insulation shoulder** touches
  the front face of the terminal.
- Push straight in only. The **right gripper** never twists the lead and never forces it in at an angle.
- If the end will not go in, pull the lead back out with the **right gripper**, straighten it, and push it
  straight in again.
- Open the **right gripper** and let go. The lead must stay in the hole.
- Go back to 2.1 for the next terminal.

**Check:** after each lead, no bare copper shows outside the hole, the insulation shoulder touches the
terminal face, the lead color matches the color map for that terminal number, and the lead stays in the hole
when the right gripper lets go. If bare copper shows, push the lead in further with the **right gripper**. If
the lead falls out, pick it up with the **right gripper** and push it home again. If the color is wrong, pull
that lead out with the **right gripper**, lay it back in its rack slot, and insert the right one.

**Expected state:** all six terminals hold a lead, each color matches the color map, the lead rack is empty,
every screw is still open, and the driver is still in its stand.

### Step 3: Screw all six terminals down

**Goal:** all six screws are closed on their leads, driven with the driver in terminal order.

- With the **left gripper**, keep pressing the terminal board down.
- Screw **terminal 1 first, then 2, 3, 4, 5, 6**. Do not skip a terminal and do not come back out of order.
- The **right gripper** turns screws with the **driver** only, never with its own tip.

#### 3.1 Take the driver

- **IF Config M or R1:** the **driver stand** is at the back-right. **IF Config R2:** it is at the
  front-right.
- With the **right gripper**, pinch the **driver** by its handle and lift it straight up out of the **driver
  stand**.
- Hold the driver in the **right gripper** blade-down, in line with the screws.

#### 3.2 Close each screw

- With the **right gripper**, set the **blade** down in the **screw slot** of that terminal's screw, in line
  with the slot.
- With the **right gripper**, turn the driver **clockwise** a quarter turn.
- With the **right gripper**, lift the blade clear, set it back down in the slot, and turn another quarter
  turn.
- Repeat these quarter turns with the **right gripper** until the screw stops turning.
- Never turn more than a quarter turn in one grip, and never keep forcing a screw once it has stopped.
- If the blade skates out of the slot, lift it clear with the **right gripper**, set it back down in the slot,
  and turn again.
- Move the **right gripper** on to the next terminal's screw.

#### 3.3 Park the driver

- Once all six screws are closed, put the **driver** back in the **driver stand** with the **right gripper**,
  handle up, and let go.

**Check:** all six screws are closed, each lead's insulation shoulder still touches its terminal face, and the
driver is standing in its stand. If a lead moved out while its screw turned, open that screw with the driver
in the **right gripper**, push the lead home with the **right gripper**, and close the screw again.

**Expected state:** all six screws are closed, all six leads are fully home, and the right gripper is empty.

### Step 4: Tug-test each lead

**Goal:** every one of the six leads is pulled once and holds.

- With the **left gripper**, keep pressing the terminal board down.
- Tug-test **lead 1 first, then 2, 3, 4, 5, 6**. Test every lead, every episode.
- With the **right gripper**, pinch the lead by its **insulation**, a little way in front of the terminal.
- With the **right gripper**, pull the lead straight out, away from the front face of the terminal. Keep the
  pull light and steady, for a count of one.
- Pull straight out only. The **right gripper** never jerks the lead, never pulls it sideways or upward, and
  never twists it.
- Open the **right gripper**, let go, and watch the lead. It must not have moved.
- If the lead **pulls out**, take the **driver** from its stand with the **right gripper**, close that screw
  further in quarter turns until it stops, park the driver, then tug-test that same lead again.
- If the same lead pulls out after two re-screws, leave that terminal as it is, go on to Step 5, and log the
  strip for a station check.

**Check:** all six leads were pulled, and none of them moved. If any lead was not pulled, pull it with the
**right gripper** before going on to Step 5.

**Expected state:** all six leads hold, all six screws are closed, and the driver is standing in its stand.

### Step 5: Dress the six wires

**Goal:** all six leads lie in their own channel slots, pressed down, with no crossings.

- With the **left gripper**, keep pressing the terminal board down.
- Dress **lead 1 first, then 2, 3, 4, 5, 6**.
- With the **right gripper**, pinch the lead by its **insulation** in front of the terminal, lay it straight
  forward to the **wire comb**, and press it down into the **channel slot** with the same number as its
  terminal.
- Press the lead down until it sits below the top of the comb, then open the **right gripper** and let go.
- Lay each lead straight forward with the **right gripper**. While dressing, never pull a lead along its
  length and never lift it away from its terminal.
- If a lead pops back out of its slot, press it down again with the **right gripper**.

**Check:** each of the six leads sits in the channel slot with its own number, below the top of the comb, and
no two leads lie over each other between the strip and the comb. If two leads cross, lift the upper one out
of its slot with the **right gripper**, lay it straight forward, and press it back down.

**Expected state:** all six leads are dressed in their matching channel slots, all six screws are still
closed, and every insulation shoulder still touches its terminal face.

### Step 6: End the episode

**Goal:** recording ends with all six terminals wired, screwed, tug-tested, and dressed.

1. Confirm the end state:
   - all six terminals hold the lead color the color map calls for;
   - every insulation shoulder touches its terminal face;
   - all six screws are closed;
   - all six leads are dressed in their matching channel slots;
   - the lead rack is empty and the driver is standing in its stand;
   - the terminal board is still **square** on the assembly spot.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

### After each episode

1. Open all six screws with the driver until each lead slides out freely.
2. Lift each lead out of its channel slot and out of its terminal, and lay it back in its own rack slot by
   color.
3. Back each screw off until a stripped end slides into the hole below it without being forced.
4. Blow or brush copper bits and dust out of the six holes and off the comb.
5. Set the terminal board **square** on the assembly spot, flat against the table. Put the lead rack in the
   start zone for the next episode's config — back-center (Config M), front-right (Config R1), or back-right
   (Config R2) — and leave the other two zones empty. Stand the driver in its stand, handle up, at the
   back-right, or at the front-right if the next episode is Config R2.
6. Run both Setup checklists before the next episode.

### At the end of the session

1. Inspect the parts. Replace a lead whose stripped end is kinked, shortened, or broken off. Replace the strip
   if a screw no longer holds a lead, a screw slot is chewed out, or the plastic is cracked. Replace the
   driver if its blade is rounded or chipped. Replace the comb if a channel slot no longer holds a lead.
2. Leave the board square on the assembly spot with all six screws open, all six leads in their rack slots by
   color, and the driver standing in its stand.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

- the **start timestamp** in the video;
- the **violation name** from the list below; and
- the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain multiple violations; tag each
separately. Retain the episode in training data with its violation tags. Do not delete a recorded episode
solely because it contains a violation.

### Violations

**Note on the start position:** the violations below were written for Config R1 (lead rack at the
front-right, driver stand at the back-right). The pickup and arm-role cues will be rewritten later to cover
all three start positions; they are left as they are for now. Until then, anything that does not match the
episode's config goes under **Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the lead rack is not in
  the start zone for the config, or the driver stand is not where that config puts it; a gripper reaches
  across the board for a lead or for the driver; or the wrong IF line is followed.
- **SOP rule broken:** the start position and the same-side rule (the rack starts in one of the three zones
  and stays there; the right gripper takes every lead and the driver from the right of the table, and the
  left gripper never leaves the board's left edge; the IF line followed is the one for the config on the
  table).
- **Coaching note:** look where the rack is before the first reach, then follow that config's IF lines
  through Steps 2 and 3.

**Violation: Terminal board not held**
- **Visible cue:** the left gripper is off the left edge of the terminal board while the right gripper
  inserts a lead, turns a screw, pulls a lead, or presses a wire into the comb, and the board slides, lifts,
  or is chased across the spot.
- **SOP rule broken:** Step 1 (the left gripper presses the terminal board down by its left edge and holds it
  there through Steps 2, 3, 4, and 5).
- **Coaching note:** left gripper on the board first, and leave it there until the episode ends.

**Violation: Terminal board moved off the assembly spot**
- **Visible cue:** either gripper lifts, turns, or drags the terminal board, or the board ends the episode out
  of square with the front edge.
- **SOP rule broken:** Steps 1–5 (the terminal board stays flat and square on the assembly spot for the whole
  episode and is never lifted).
- **Coaching note:** bring the lead and the driver to the board; never move the board to them.

**Violation: Lead put in the wrong terminal**
- **Visible cue:** the right gripper pushes a lead into a terminal the color map gives a different color, and
  the episode moves on.
- **SOP rule broken:** Step 2 (read the color map for the terminal being wired and insert that color).
- **Coaching note:** read the map for the terminal, then find the color in the rack. Map first, rack second.

**Violation: Leads inserted out of order**
- **Visible cue:** the right gripper inserts the leads in some order other than terminal 1, 2, 3, 4, 5, 6.
- **SOP rule broken:** Step 2 (work terminal 1 first, then 2, 3, 4, 5, 6, one lead at a time).
- **Coaching note:** left to right, one at a time. Say the terminal number before you pick the lead.

**Violation: Lead mishandled on the way in**
- **Visible cue:** the right gripper pinches the bare stripped end, bends or kinks it, carries two leads at
  once, or sets a lead down on the board or the table on the way from the rack.
- **SOP rule broken:** Step 2 (carry each lead in one go straight from the rack to its terminal, held by its
  insulation only, without bending or kinking the stripped end).
- **Coaching note:** one lead, insulation only, straight to the hole.

**Violation: Lead not fully home**
- **Visible cue:** bare copper shows outside the hole, or the insulation shoulder stands off the front face of
  the terminal, or the lead falls out when the right gripper lets go, and the episode moves on.
- **SOP rule broken:** Step 2 (push the lead straight in until the insulation shoulder touches the front face,
  with no bare copper showing, and let go only once the lead stays in the hole).
- **Coaching note:** shoulder against the face, no copper showing. Let go and look before the next lead.

**Violation: Lead forced or twisted into the hole**
- **Visible cue:** the right gripper pushes a lead in at an angle, twists it while pushing, or forces an end
  that will not enter, instead of pulling it back out and straightening it.
- **SOP rule broken:** Step 2 (push straight in only; if the end will not go in, pull it out, straighten it,
  and push it straight in again).
- **Coaching note:** straight in, no twist. If it fights you, back it out and straighten it.

**Violation: Terminal left empty**
- **Visible cue:** the right gripper never puts a lead in one of the six terminals, and the episode goes on to
  screw that terminal down or to end.
- **SOP rule broken:** Step 2 (all six terminals hold a lead before any screw is turned).
- **Coaching note:** count six leads in six holes before you pick up the driver.

**Violation: Screws driven out of order, or a screw skipped**
- **Visible cue:** the right gripper closes the screws in some order other than terminal 1, 2, 3, 4, 5, 6, or
  never turns one of them.
- **SOP rule broken:** Step 3 (screw terminal 1 first, then 2, 3, 4, 5, 6, skipping none).
- **Coaching note:** left to right, all six. Count the screws you closed.

**Violation: Screw left loose**
- **Visible cue:** the right gripper parks the driver, or the episode ends, with a screw never turned or
  turned only part way, so it still stands proud of the terminal.
- **SOP rule broken:** Step 3 (turn each screw clockwise in quarter turns until it stops turning).
- **Coaching note:** quarter turn, re-grip, again, until it stops.

**Violation: Screw turned the wrong way or forced**
- **Visible cue:** the right gripper turns a screw counter-clockwise, turns more than a quarter turn in one
  grip, or keeps forcing a screw after it has stopped.
- **SOP rule broken:** Step 3 (clockwise, a quarter turn per grip, and stop once the screw stops).
- **Coaching note:** clockwise, small bites, let go and re-grip. Stop when it stops.

**Violation: Driver blade not seated**
- **Visible cue:** the right gripper holds the blade across the screw head instead of down in the slot, lets
  it skate out of the slot while turning, or pries it against the terminal, and turning goes on anyway.
- **SOP rule broken:** Step 3 (set the blade down in the screw slot in line with it; if it skates out, lift it
  clear, set it back in the slot, and turn again).
- **Coaching note:** blade down in the slot, in line, before you turn.

**Violation: Driver not used or not parked**
- **Visible cue:** a screw is turned with the gripper tip instead of the driver, or the driver is still in the
  right gripper during the tug tests or the dressing, or it is left lying on the board or the table.
- **SOP rule broken:** Step 3 (turn screws with the driver only, and put the driver back in the driver stand
  once all six screws are closed).
- **Coaching note:** driver for screws, stand for the driver, empty gripper for the tug tests.

**Violation: Tug test skipped**
- **Visible cue:** the right gripper pulls fewer than six leads, or no lead at all, before the episode moves
  on to the dressing or the ending.
- **SOP rule broken:** Step 4 (tug-test lead 1 through lead 6; test every lead, every episode).
- **Coaching note:** six leads, six pulls. Count them out as you go.

**Violation: Tug test done the wrong way**
- **Visible cue:** the right gripper jerks a lead, pulls it sideways or upward, twists it, or pinches it on
  the bare stripped end instead of a light steady pull straight out on the insulation.
- **SOP rule broken:** Step 4 (pinch the insulation in front of the terminal and pull straight out, light and
  steady, for a count of one).
- **Coaching note:** light, steady, straight out. A yank tells you nothing and wrecks the joint.

**Violation: Failed tug test not fixed and re-tested**
- **Visible cue:** a lead slides out or its shoulder lifts during the tug test and the episode moves on; or
  the right gripper closes that screw further and never pulls that lead again.
- **SOP rule broken:** Step 4 (on a lead that pulls out, close that screw further with the driver, park the
  driver, then tug-test that same lead again).
- **Coaching note:** every re-screw earns another pull on that same lead.

**Violation: Wires left undressed**
- **Visible cue:** the right gripper never lays one or more leads into the comb, and the episode ends with
  them lying loose across the board or hanging off it.
- **SOP rule broken:** Step 5 (lay each of the six leads forward and press it into its channel slot).
- **Coaching note:** all six leads end up in the comb. Nothing hangs loose at the end.

**Violation: Lead dressed in the wrong slot**
- **Visible cue:** the right gripper presses a lead into a channel slot whose number does not match its
  terminal, or dresses the leads in some order other than 1, 2, 3, 4, 5, 6.
- **SOP rule broken:** Step 5 (dress lead 1 first, then 2 through 6, each into the channel slot with the same
  number as its terminal).
- **Coaching note:** same number, straight ahead. Lead 3 goes in slot 3.

**Violation: Wires left crossing**
- **Visible cue:** two leads lie over each other between the strip and the comb at the end of the episode.
- **SOP rule broken:** Step 5 (no two leads lie over each other between the strip and the comb).
- **Coaching note:** lay each lead straight forward, and fix a crossing as soon as you see it.

**Violation: Lead not pressed down into the comb**
- **Visible cue:** a lead sits on top of the comb or stands above the top of its channel slot, or it pops out
  and the right gripper leaves it out.
- **SOP rule broken:** Step 5 (press each lead down until it sits below the top of the comb and stays there
  when the right gripper lets go).
- **Coaching note:** press until it sits below the comb, then let go and check it stayed.

**Violation: Dressing disturbed a terminal**
- **Visible cue:** while dressing a wire, the right gripper pulls the lead along its length or lifts it away
  from the terminal, and its insulation shoulder lifts off the terminal face or the lead comes out of the hole.
- **SOP rule broken:** Step 5 (lay each lead straight forward; do not pull the lead along its length or lift
  it away from the terminal while dressing it).
- **Coaching note:** dress from in front of the terminal, and push the wire down, never pull it forward.

**Violation: Work done out of order**
- **Visible cue:** the phases run out of sequence — the right gripper takes the driver out before all six
  leads are in, pulls a lead before its screw is closed, dresses a lead before it has been pulled, or closes a
  screw after the dressing has started.
- **SOP rule broken:** Steps 2–5 (insert all six, screw all six, tug-test all six, then dress all six, in
  that order).
- **Coaching note:** finish the phase before you start the next one. Say the phase name before you move.

**Violation: Wrong arm used**
- **Visible cue:** an action assigned to one gripper is done by the other, including the left gripper picking
  or inserting a lead, holding the driver, turning a screw, pulling a lead, or pressing a wire into the comb,
  or the right gripper holding down the board.
- **SOP rule broken:** Steps 1–5 (the right gripper picks, inserts, screws, tug-tests, and dresses; the left
  gripper holds the board).
- **Coaching note:** right gripper does the work, left gripper holds the board. It does not swap.

**Violation: Lead, driver, or rack knocked off its spot**
- **Visible cue:** either gripper drops a lead on the board, the table, or the floor, drops the driver, or
  tips, pushes, or spills the lead rack or the driver stand off its spot.
- **SOP rule broken:** Steps 2–5 (keep the leads, the driver, the lead rack, and the driver stand on their
  spots through the whole episode).
- **Coaching note:** work slower and lower over the table, and keep each carry short.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before the six terminals and the dressing are confirmed, an arm is not
  home, a gripper is closed, or an arm does something else after homing.
- **SOP rule broken:** Step 6 (confirm the end state, return both arms home with grippers open as their final
  action, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than
tagging them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- A lead arrives stripped too short, stripped too long, or with the copper already broken off, so it cannot go
  fully home.
- A terminal screw's thread is stripped, so a fully closed screw does not hold the lead.
- A screw slot is chewed out before the episode, so the blade cannot seat in it.
- The terminal strip is cracked or loose on the board, so a lead cannot be clamped.
- A channel slot in the comb is broken, so a correctly pressed lead will not stay in it.

## Annotation subtasks (from SOP)

1. Press the terminal board flat and hold it with the left gripper
2. Pick a lead from the rack by the color the map calls for
3. Push the lead fully home into its terminal
4. Repeat the pick and insert for all six terminals
5. Take the driver from the stand
6. Close each terminal screw in quarter turns, terminal 1 through 6
7. Park the driver back in the stand
8. Tug-test each lead, terminal 1 through 6
9. Re-screw and re-test any lead that pulls out
10. Lay each lead forward and press it into its matching channel slot
11. Confirm the end state, return both arms home, and end the episode
