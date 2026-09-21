# Wire a Lamp Circuit on a Board SOP (1x Board)

One episode wires one board. Work the six phases in this fixed order: **mount the three parts on
their outlines, land and dress the three leads, close the six terminal screws, tug-test the six lead
ends, fit the bulb, test the switch.** The three parts, the three leads, the six terminals, the
fixtures, and the order of the phases never vary.

**This is a single-arm task.** Only the **right arm** works. The **left arm stays at home with its
gripper open for the whole episode** and touches nothing. Because there is no second gripper to hold
or steady anything, the fixtures do that job: the **wiring board** is heavy and non-slip and stands
on its mark all episode, so every push, every turn of a screw, and the quarter turn of the bulb goes
straight into the table instead of shoving the board sideways; each part is **locked to the board by
its own mount pins and lock tab**, so nothing is ever held while something is done to it; the
**parts tray**, the **lead rack**, the **bulb nest**, and the **driver stand** each hold their item
upright so the right gripper lifts it already in the right attitude; and the **wire comb** holds each
lead in place, which is why every lead is dressed into its channel slot **before** any screw is
turned. The comb is what keeps the stripped ends home while the right gripper puts the lead down and
picks the driver up. Nothing is held in the air while something else is done to it.

The **diagram is printed on the board**: three labeled outlines, a terminal label beside every
terminal, and the wiring table at the back edge. The three parts are mounted in this fixed order:
**switch, lamp holder, terminal strip.** The strip goes on last, so the board is only joined to the
bench supply once the other two parts are already locked down.

The three leads run round the circuit like this:

- **W1 red:** terminal strip **1** → channel slot **1** → switch **A**.
- **W2 black:** switch **B** → channel slot **2** → lamp holder **L**.
- **W3 blue:** lamp holder **N** → channel slot **3** → terminal strip **2**.

Screws are closed and leads are tug-tested in **loop order: 1, A, B, L, N, 2.**

The table is set up in one of three ways. Only the **parts tray** moves; the wiring board, the lead rack,
and the driver stand are in the same place in all three. In Config R1 the parts tray takes the bulb
nest's place, so the bulb nest stands at the back right instead.

- **Config M:** the parts tray is at the front center, in front of the board, no part of it left of the
  table's center line.
- **Config R1:** the parts tray is at the front right, in front of the lead rack, and the bulb nest is at
  the back right.
- **Config R2:** the parts tray is at the back right.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line
that matches.

What stays constant across all sessions:

- **Start position:** the parts tray starts at the front center (**Config M**), the front right
  (**Config R1**), or the back right (**Config R2**). One config per episode, chosen before recording and
  never changed mid-episode.
- **Same-side rule:** this is a single-arm task, so the **right gripper** lifts every part out of the tray
  in every config; the config changes only the direction of the reach. The left side of the table is not
  used, because the left arm is parked and the right arm never leans across the table's center line, so
  no left zone is reachable. Nothing is handed over.
- **Fixed roles:** everything else is the same in all three configs — the board stays on its mark, the
  leads come from the rack right of the board, the driver from the stand at the far right, the bulb from
  the nest (front right, or back right in Config R1), the left arm stays at home, and the parts are
  mounted switch, lamp holder, terminal strip.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** single_arm

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the parts tray in the start zone for this episode's
   config, the wiring board on its mark just right of the table's center line, the lead rack right of
   the board, the driver stand at the far right, the bulb nest at the front right (back right in
   Config R1), and both arms.
3. The wiring board is visible from above, so all three outlines, all six terminal labels, the three
   channel slots, and the printed wiring table can be seen.
4. The wiring board is visible from the front, so the gap under a part's foot, the lock tab on each
   foot, and the bulb sitting down on the holder rim can be seen.
5. The bulb is visible in the lamp holder from the front, so a reviewer can see whether it is lit.
6. Both arms are at home with grippers open.
7. The table is bare apart from the wiring board, the parts tray, the lead rack, the driver stand,
   the bulb nest, and robot hardware.
8. The right arm reaches all three outlines, all six terminals, all three channel slots, all three
   parts-tray bays in the start zone for this episode's config, all three rack slots, the driver stand,
   and the bulb nest in its place for the config without stretching and without leaning across the
   table's center line.
9. The left arm is at home, gripper open, and stays there.

### Materials checklist

1. One **wiring board**, a flat board standing on the **board mark**, a taped outline just right of
   the table's center line, square to the front edge and flat on the table. It is heavy with a
   non-slip underside, so a part can be pushed back, a screw turned, and a bulb turned without the
   board sliding or lifting. It is never gripped and never lifted.
2. The board is narrow enough that the switch outline, at its back-left, still sits right of the
   table's center line, so the right arm reaches everything on the board without leaning across the
   table.
3. The **diagram** is printed on the board face: the **switch outline** at the back-left, the **lamp
   holder outline** at the back-right, the **terminal strip outline** across the front, and the
   **wiring table** printed at the back edge listing the three leads and their terminals.
4. Each outline has **two mount pins** standing in the board and a printed part name.
5. The **wire comb** is a bar fixed across the middle of the board, between the strip outline and the
   other two, with three **channel slots** numbered **1**, **2**, **3** from left to right.
6. The **supply lead** runs from the bench supply into the back edge of the board and sits in the
   **strain clip** there. It carries 12 V to the two mount pins in the terminal strip outline, so the
   strip is joined to the supply the moment it locks down. The supply is switched on before recording
   and the lead is never gripped, moved, or unclipped.
7. **One rocker switch**, standing in **bay 1** of the parts tray, right way up. Its top face carries
   a rocker marked **I** on its back half and **O** on its front half. Its two screw terminals are
   labeled **A** and **B**, A on the left.
8. **One lamp holder**, standing in **bay 2** of the parts tray, opening up. Its two screw terminals
   are labeled **L** and **N**, L on the left. Inside the opening are two **L-slots** that take the
   bulb pins.
9. **One terminal strip**, standing in **bay 3** of the parts tray, right way up, with two screw
   terminals labeled **1** and **2**, 1 on the left.
10. Every part has a **foot** with two **keyhole slots** that drop over the two mount pins, and a
    **lock tab** at the front of the foot that springs up when the part is pushed back onto the pins.
11. All three parts are undamaged: no cracked body, no chewed screw head, no bent mount pin, no lock
    tab that will not spring up.
12. All six terminal screws are **open** at the start, far enough that a stripped end goes into the
    hole below without touching the screw.
13. The parts tray is a heavy block with three numbered bays, standing in the start zone for this
    episode's config, with the other two zones bare. Each bay holds its part upright and does not move
    when the part is lifted out.
    - **Config M:** front center, in front of the board, no part of it left of the center line.
    - **Config R1:** front right, in front of the lead rack, where the bulb nest normally stands.
    - **Config R2:** back right.
14. **Three leads**, each pre-stripped at both ends, standing in the **lead rack** right of the board
    in three numbered slots: slot 1 holds **W1**, the red lead; slot 2 holds **W2**, the black lead;
    slot 3 holds **W3**, the blue lead. Each slot is labeled with its lead color.
15. The lead rack is heavy and non-slip, so a lead can be lifted straight out without the rack moving.
16. Every lead is straight, with clean bare copper at both ends, no kink, and no splayed strands.
17. Each lead is long enough to reach both of its terminals with a little slack once it is dressed in
    its channel slot, and short enough that the slack does not reach the board's edge.
18. One **driver**, a slotted screwdriver that fits the six terminal screws, standing handle up in
    the **driver stand** at the far right. The stand is heavy and holds the driver upright, blade
    down, so the right gripper closes on the handle and lifts it out already in line.
19. One **bulb**, a two-pin bayonet bulb, standing **base down** in the cup of the **bulb nest** at
    the front right (Config M and R2) or the back right (Config R1). Its **base collar** stands proud of
    the cup, so the right gripper closes on the collar without touching the glass.
20. The bulb nest is heavy and non-slip, so the bulb can be lifted straight up out of it without the
    nest moving. The bulb glass is clean, unbroken, and free of grease.
21. The switch rocker is pressed to **O**, off, before recording starts, and stays off until Step 6.
22. Before collection, confirm by hand that:
    - each part drops over its two mount pins and locks with one straight push back;
    - a locked part does not lift on a light pull and does not move when a screw is turned;
    - each stripped end goes fully home in its terminal without force;
    - each lead presses down into its channel slot and stays there;
    - each terminal screw closes on a lead by hand and stops solid;
    - the bulb drops into the holder and locks with a quarter turn clockwise;
    - the bulb lights when the rocker is pressed to I, and goes dark when it is pressed to O.

### Workspace layout

Everything below is a fixed area of the table, judged by eye against the table edges, the taped
outline, and the fixtures standing on it. The areas sit in a short arc, all inside the right arm's
reach.

- **Start zone, parts tray:** bay 1 holds the switch, bay 2 the lamp holder, bay 3 the terminal strip.
  At the front center in front of the board (**Config M**), the front right (**Config R1**), or the back
  right (**Config R2**).
- **Just right of center, board mark:** one taped outline. The wiring board stands here and does not
  move.
- **On the board, back-left:** the switch outline, with terminals A and B.
- **On the board, back-right:** the lamp holder outline, with terminals L and N.
- **On the board, across the front:** the terminal strip outline, with terminals 1 and 2.
- **On the board, across the middle:** the wire comb, channel slots 1, 2, 3 from left to right.
- **Right of the board, lead rack:** slot 1 holds W1 red, slot 2 holds W2 black, slot 3 holds W3 blue.
- **Far right, driver stand:** the driver standing handle up, blade down.
- **Front right, bulb nest:** the bulb standing base down in its cup, collar proud. In **Config R1** the
  nest stands at the back right instead, where the parts tray stands in Config R2.

### Arm assignment

- **Right gripper, all of the work:** lifts each part out of the parts tray and locks it on its
  outline, carries each lead from its rack slot and pushes both ends home, presses each lead into its
  channel slot, takes the driver and closes all six screws, tug-tests all six ends, fits the bulb,
  and presses the rocker on and off. It reaches forward in front of the board for the parts tray in
  Config M, forward to the right in Config R1, and back past the lead rack in Config R2; in Config R1 it
  takes the bulb from the back right instead of the front right.
- **Left arm, parked:** stays at home with its gripper open from the start of recording to the end, in
  every config. It holds nothing, steadies nothing, and reaches for nothing.

## Vocabulary

- **Board mark:** the taped outline just right of the table's center line where the wiring board
  stands. The board stays inside it for the whole episode. A correctly placed board shows a thin band
  of tape all the way around its edge.
- **Square:** the front edge of the wiring board lines up with the front edge of the table, so neither
  end of the board sits nearer the front.
- **Wiring board:** the heavy board with the diagram printed on it. Its underside is non-slip, so it
  holds itself still while a part is pushed back, a screw is turned, or the bulb is turned. It is
  never gripped and never lifted.
- **Diagram:** everything printed on the board face: the three outlines, the terminal labels, and the
  wiring table. It is the only source for which part goes where and which lead goes to which terminal.
- **Outline:** the printed shape on the board that one part sits inside, with the part's name printed
  beside it.
- **Mount pin:** one of the two posts standing in an outline. The part's keyhole slots drop over them.
- **Keyhole slot:** the slot in a part's foot with a wide end and a narrow end. The pin goes in at the
  wide end, and the part is pushed back so the pin ends up in the narrow end.
- **Lock tab:** the small springy tab at the front of a part's foot. It stays pressed down while the
  part slides back and springs up at the end of the slide.
- **Locked:** the lock tab stands up in front of the foot, the foot sits flat on the board with no gap
  showing under it, and the part does not lift on a light pull.
- **Body flats:** the two bare side faces of a part. These are the only places the right gripper
  closes on a part.
- **Terminal:** one wiring position. Each one has its own label, its own screw, and its own hole.
- **Terminal label:** the letter or number printed beside a terminal: **A** and **B** on the switch,
  **L** and **N** on the lamp holder, **1** and **2** on the terminal strip.
- **Loop order:** the order the circuit runs, and the order screws are closed and ends are
  tug-tested. Written out: **1, A, B, L, N, 2.**
- **Screw:** the small slotted screw on top of a terminal. Turning it clockwise clamps the lead in the
  hole below it.
- **Screw slot:** the straight groove across the head of a screw that the driver blade sits in.
- **Screw open:** the screw is backed off far enough that a stripped end goes into the hole below
  without touching it.
- **Screw closed:** the screw has been turned clockwise until it stops turning.
- **Hole:** the opening in the face of a terminal that a stripped end goes into.
- **Lead:** one colored wire. Three leads are wired in one episode: **W1** red, **W2** black, **W3**
  blue.
- **Insulation:** the colored plastic covering along the lead.
- **Stripped end:** the bare copper at one end of a lead, with the insulation removed.
- **Insulation shoulder:** the step where the insulation ends and the bare copper begins.
- **Fully home:** the stripped end is all the way inside the hole and the insulation shoulder touches
  the face of the terminal, so no bare copper shows outside the hole.
- **Kink:** a sharp bend in the bare copper of a stripped end. A kinked end does not go fully home.
- **Wire comb:** the bar fixed across the middle of the board with three open channel slots.
- **Channel slot:** one numbered slot in the comb. W1 goes in slot 1, W2 in slot 2, W3 in slot 3.
- **Dressed:** the lead is pressed down into its channel slot, below the top of the comb, and stays
  there when the right gripper lets go. A dressed lead holds both of its ends where they were put.
- **Crossing:** two leads lie over each other anywhere on the board.
- **Driver:** the slotted screwdriver used to turn the terminal screws.
- **Driver stand:** the heavy holder at the far right the driver stands in when it is not in the right
  gripper.
- **Blade seated:** the driver blade sits down in the screw slot, in line with it, and does not skate
  out when the screw is turned.
- **Tug test:** a light, steady pull on a lead, straight out away from the face of the terminal, for a
  count of one.
- **Holds:** the lead does not move at all during its tug test.
- **Pulls out:** the lead slides out of the hole, or the insulation shoulder lifts off the terminal
  face, during its tug test.
- **Bulb:** the two-pin bayonet bulb that goes in the lamp holder.
- **Base collar:** the metal band around the bottom of the bulb, below the glass. It is the only place
  the right gripper closes on the bulb.
- **L-slot:** one of the two slots inside the lamp holder opening. A bulb pin goes down one, then
  round it when the bulb is turned.
- **Bulb locked:** the bulb sits down on the holder rim all the way around, it does not lift on a
  light pull, and it does not turn back on its own.
- **Rocker:** the pad on top of the switch. Its back half is marked **I**, on. Its front half is
  marked **O**, off.
- **Closed jaws:** the right gripper is fully closed before it touches something, so it pushes with a
  flat face instead of pinching.
- **Lit:** the bulb glows and can be seen glowing from the front camera.
- **Dark:** the bulb does not glow.
- **Light pull:** the right gripper takes the item, pulls straight up once, gently, then releases. A
  locked part or a locked bulb does not lift.
- **Straight down:** the item comes down in line with what it goes into and does not lean, tilt, or
  come in from the side.
- **Stable:** the item stays still for 2 seconds after release and does not rock, roll, tip, or
  slide.
- **Front edge:** the edge of the table nearest the collector.
- **Start zone:** where the parts tray stands at the start of the episode — front center (**Config M**),
  front right (**Config R1**), or back right (**Config R2**). One per episode, chosen before recording and
  never changed mid-episode.
- **Nest place:** where the bulb nest stands — the front right in Config M and R2, the back right in
  Config R1, where the parts tray takes its usual place.
- **Parked arm:** the left arm, at home with its gripper open. It does not move during the episode.

## Steps

Step 1 depends on where the parts tray is: the **right gripper** reaches forward in front of the board in
Config M, forward to the right in Config R1, or back past the lead rack in Config R2. Step 5 depends on
where the bulb nest is: the front right in Config M and R2, the back right in Config R1. Every other line
is the same in all three configs.

### Step 1: Mount the three parts on their outlines

**Goal:** the switch, the lamp holder, and the terminal strip each sit locked on their own outline,
feet flat, lock tabs up.

Mount them in this fixed order: **switch, then lamp holder, then terminal strip.** Do not grip, lift,
or push the wiring board at any point. Close the **right gripper** on a part's body flats only, never
on the rocker, the holder opening, a terminal, or the foot.

Look where the parts tray is before reaching for the first part.

- **IF the parts tray is at the front center (Config M):** the **right gripper** reaches forward, in front
  of the board, for each part, lifts it straight up out of its bay, high enough to clear the board's front
  edge, and carries it back onto the board to its outline.
- **IF the parts tray is at the front right (Config R1):** the **right gripper** reaches forward and to
  the right, in front of the lead rack, for each part, lifts it straight up out of its bay, and carries it
  back and to the left onto the board to its outline.
- **IF the parts tray is at the back right (Config R2):** the **right gripper** reaches back, past the
  lead rack, for each part, lifts it straight up out of its bay, and carries it forward onto the board to
  its outline.

Then, in all three, mount the parts as 1.1 to 1.3 say.

#### 1.1 Mount the switch

- With the **right gripper**, close on the body flats of the switch in bay 1 and lift it straight up
  out of the tray.
- Carry it over the switch outline at the board's back-left, keeping it level and the rocker facing up.
- Turn it until terminal A is on the left and terminal B is on the right.
- Lower it straight down until both mount pins come up through the wide ends of its keyhole slots and
  the foot lands on the board.
- Push the part straight back, toward the back edge, until the lock tab springs up.
- Open the **right gripper** and lift it clear.

**Check:** the lock tab stands up in front of the foot, the foot sits flat with no gap under it, and
the rocker is still pressed to O. Give it a light pull with the **right gripper**: it does not lift.
If the tab is still down, close the **right gripper** on the body flats and push the part straight
back again. If the part lifts on the pull, lift it off the pins, lower it straight down again, and
push it back.

#### 1.2 Mount the lamp holder

- With the **right gripper**, close on the body flats of the lamp holder in bay 2 and lift it straight
  up out of the tray.
- Carry it over the lamp holder outline at the board's back-right, keeping it level and the opening
  facing up.
- Turn it until terminal L is on the left and terminal N is on the right.
- Lower it straight down until both mount pins come up through the wide ends of its keyhole slots and
  the foot lands on the board.
- Push the part straight back, toward the back edge, until the lock tab springs up.
- Open the **right gripper** and lift it clear.

**Check:** the lock tab stands up, the foot sits flat with no gap under it, and the opening faces
straight up with both L-slots clear. Give it a light pull with the **right gripper**: it does not
lift. If the tab is still down, close the **right gripper** on the body flats and push the part
straight back again.

#### 1.3 Mount the terminal strip

- With the **right gripper**, close on the body flats of the terminal strip in bay 3 and lift it
  straight up out of the tray.
- Carry it over the terminal strip outline across the board's front, keeping it level.
- Turn it until terminal 1 is on the left and terminal 2 is on the right.
- Lower it straight down until both mount pins come up through the wide ends of its keyhole slots and
  the foot lands on the board.
- Push the part straight back, toward the back edge, until the lock tab springs up.
- Open the **right gripper** and lift it clear.

**Check:** the lock tab stands up, the foot sits flat with no gap under it, and terminal 1 is on the
left. Give it a light pull with the **right gripper**: it does not lift.

**Expected state:** all three parts stand locked on their own outlines, all three lock tabs are up,
all six screws are still open, the parts tray is empty, the rocker is pressed to O, and the wiring
board is still inside its mark.

### Step 2: Land and dress the three leads

**Goal:** all six stripped ends are fully home in the terminals the diagram names, and each lead is
dressed in its own channel slot, with no screw turned yet.

Work the leads in this fixed order: **W1, then W2, then W3.** Finish one lead before starting the
next. Turn no screw in this step: the **driver** stays in its stand. Hold each lead by its
**insulation** with the **right gripper** only. Never pinch a **stripped end** and never bend or kink
one.

Dress each lead into its channel slot **before** landing its second end. The comb is what holds the
lead, so the first end stays home while the **right gripper** works on the second.

#### 2.1 Pick the right lead

- Read the wiring table printed at the back of the board for the lead being run.
- With the **right gripper**, pinch that lead by its insulation, a little way back from one stripped
  end, and lift it straight up out of its rack slot.
- Carry it in one go, straight from the rack to the board. Do not set it down on the board or the
  table on the way.

#### 2.2 Push the first end fully home

- Bring the stripped end to the hole of the first terminal for that lead: **W1 to strip terminal 1**,
  **W2 to switch terminal B**, **W3 to lamp holder terminal N**.
- Line the end up with the hole and push it straight in with the **right gripper** until the
  insulation shoulder touches the face of the terminal.
- Push straight in only. The **right gripper** never twists the lead and never forces it in at an
  angle.
- Open the **right gripper** and let go. The end stays in the hole.

**Check:** no bare copper shows outside the hole, and the insulation shoulder touches the terminal
face. If bare copper shows, push the lead in further with the **right gripper**. If the end will not
go in, pull it back out with the **right gripper**, straighten it, and push it straight in again. If
the lead falls out, pick it up and push it home again.

#### 2.3 Dress the lead into its channel slot

- With the **right gripper**, pinch the lead by its insulation between the two terminals it runs
  between.
- Lay it into its own channel slot: **W1 in slot 1**, **W2 in slot 2**, **W3 in slot 3**.
- Press it straight down until it sits below the top of the comb.
- Open the **right gripper** and let go.

**Check:** the lead sits down in its own numbered slot, stays there when the **right gripper** lets
go, and does not lie over another lead. The first end is still fully home. If the lead lifts back out
of the slot, press it down again. If it lies over another lead, lift it clear with the **right
gripper** and lay it back in its own slot.

#### 2.4 Push the second end fully home

- With the **right gripper**, pinch the free end of that lead by its insulation, a little way back
  from the stripped end.
- Bring it to the hole of the second terminal for that lead: **W1 to switch terminal A**, **W2 to
  lamp holder terminal L**, **W3 to strip terminal 2**.
- Push it straight in with the **right gripper** until the insulation shoulder touches the face of the
  terminal.
- Open the **right gripper** and let go. The end stays in the hole.

**Check:** no bare copper shows outside the hole, the insulation shoulder touches the terminal face,
the lead is still down in its channel slot, and the first end is still home. Then go back to 2.1 for
the next lead.

**Expected state:** all six terminals hold a stripped end, each lead runs between the two terminals
the wiring table names, all three leads sit down in their own channel slots with no crossing, the
lead rack is empty, every screw is still open, the driver is still in its stand, and the rocker is
still pressed to O.

### Step 3: Close the six terminal screws

**Goal:** all six screws are closed on their leads, turned with the driver, in loop order.

Close the screws in **loop order: 1, A, B, L, N, 2.** Do not skip a terminal and do not come back out
of order. The **right gripper** turns screws with the **driver** only, never with its own tip. Hold
the driver in the **right gripper** for the whole step, and do not stand it back up between screws.
Do not hold, press, or steady a part or a lead with the gripper at any point: the lock tabs hold the
parts and the comb holds the leads.

#### 3.1 Take the driver

- With the **right gripper**, close on the handle of the driver and lift it straight up out of the
  driver stand.
- Hold it blade down, in line with the screws.

**Check:** the driver is held upright and the blade points straight down. If it leans in the gripper,
lower it back into the stand, open the **right gripper**, and pick it up again.

#### 3.2 Close each screw

- With the **right gripper**, set the blade down in the screw slot of that terminal's screw, in line
  with the slot.
- With the **right gripper**, turn the driver **clockwise** a quarter turn.
- With the **right gripper**, lift the blade clear, set it back down in the slot, and turn another
  quarter turn.
- Repeat these quarter turns with the **right gripper** until the screw stops turning.
- Never turn more than a quarter turn in one grip, and never keep forcing a screw once it has stopped.
- If the blade skates out of the slot, lift it clear with the **right gripper**, set it back down in
  the slot, and turn again.
- Move the **right gripper** on to the next terminal in loop order.

**Check:** after each screw, the screw has stopped turning, the lead's insulation shoulder still
touches its terminal face, and the lead is still down in its channel slot. If a lead moved out while
its screw turned, open that screw with the driver, push the lead home with the **right gripper**,
then close the screw again.

#### 3.3 Park the driver

- Once all six screws are closed, carry the driver back to the driver stand with the **right
  gripper**.
- Lower it straight in, handle up, and release it when it is stable.

**Check:** all six screws are closed, all six ends are still fully home, the driver stands upright in
its stand, and the **right gripper** is empty.

**Expected state:** the circuit is wired: three leads, six ends home, six screws closed, all three
leads dressed in their own channel slots. The rocker is still pressed to O.

### Step 4: Tug-test the six lead ends

**Goal:** every one of the six ends is pulled once and holds.

Tug-test in **loop order: 1, A, B, L, N, 2.** Test every end, every episode.

- With the **right gripper**, pinch the lead by its insulation, a little way in front of the terminal
  being tested.
- Pull the lead straight out with the **right gripper**, away from the face of that terminal. Keep the
  pull light and steady, for a count of one.
- Pull straight out only. The **right gripper** never jerks the lead, never pulls it sideways or
  upward, and never twists it.
- Open the **right gripper**, let go, and look at the end. It must not have moved.
- If the end **pulls out**, take the driver from its stand with the **right gripper**, push the end
  home again, close that screw in quarter turns until it stops, park the driver, and tug-test that
  same end again.
- If the same end pulls out after two re-screws, leave that terminal as it is, go on to Step 5, and
  log the board for a station check.

**Check:** all six ends were pulled and none of them moved, and every lead is still down in its
channel slot. If an end was not pulled, pull it with the **right gripper** before going on to Step 5.

**Expected state:** all six ends hold, all six screws are closed, the driver stands in its stand, and
the rocker is still pressed to O.

### Step 5: Fit the bulb

**Goal:** the bulb sits locked in the lamp holder, down on the rim all the way around.

- **IF Config M or R2:** the bulb nest is at the front right; reach forward and to the right for it.
  **IF Config R1:** the bulb nest is at the back right, where the parts tray stood; reach back, past the
  lead rack, and lift the bulb high enough to clear the rack and the mounted parts.
- With the **right gripper**, close on the base collar of the bulb in the nest. Never close on the
  glass.
- Lift it straight up out of the nest, keeping it upright, base down.
- Carry it over the lamp holder opening.
- Before lowering, turn the wrist a quarter turn counter-clockwise, so the quarter turn clockwise that
  locks the bulb finishes with the wrist straight.
- Lower the bulb straight down until both pins drop into the two L-slots and the bulb meets the
  holder.
- Push straight down a little, turn a **quarter turn clockwise** until it stops, then let the bulb
  rise back onto the rim.
- Open the **right gripper** and lift it clear.

**Check:** the bulb sits down on the holder rim all the way around with no gap, and it stands
upright, not leaning. Give it a light pull with the **right gripper** on the base collar: it does not
lift. If the bulb lifts, or a gap shows under it, close the **right gripper** on the base collar,
push straight down, and turn to the stop again. If the pins will not drop in, lift the bulb clear,
line the pins up with the two L-slots, and lower it straight down again. Do not force a leaning bulb
and do not turn it counter-clockwise once it is in.

**Expected state:** the bulb stands locked in the lamp holder, the bulb nest is empty, and the rocker
is still pressed to O.

### Step 6: Test the switch

**Goal:** the switch is pressed on once and off once, with the bulb seen lit and then dark.

Do exactly one on and off cycle. Press the rocker with **closed jaws** only: close the **right
gripper** fully before it touches the rocker.

#### 6.1 Press the switch on

- With the **right gripper** closed, come down straight onto the back half of the rocker, the half
  marked **I**, and press it down until it clicks over.
- Lift the **right gripper** straight up clear of the switch.

**Check:** the rocker stands pressed to I and the bulb is **lit**. If the rocker did not click over,
press the I half straight down again with closed jaws. If the bulb is not lit, go straight to 6.2,
press the rocker to O, and log the board for a station check. Do not turn a screw, push a lead, or
touch the bulb while the rocker is pressed to I.

#### 6.2 Press the switch off

- With the **right gripper** closed, come down straight onto the front half of the rocker, the half
  marked **O**, and press it down until it clicks over.
- Lift the **right gripper** straight up clear of the switch.

**Check:** the rocker stands pressed to O and the bulb is **dark**. If the rocker did not click over,
press the O half straight down again with closed jaws.

**Expected state:** the circuit has been switched on once and off once, the rocker is pressed to O,
the bulb is dark and still locked in the holder, and nothing on the board has moved.

### Step 7: End the episode

**Goal:** recording ends with the circuit wired, the bulb fitted, and the switch tested and off.

1. Confirm the end state:
   - all three parts stand locked on their own outlines, lock tabs up, feet flat;
   - all three leads run between the terminals the wiring table names, each dressed in its own
     channel slot, with no crossing;
   - all six ends are fully home with no bare copper showing, and all six screws are closed;
   - all six ends held their tug test;
   - the bulb is locked in the lamp holder, down on the rim, and dark;
   - the rocker is pressed to O;
   - the parts tray, the lead rack, and the bulb nest are all empty, and the driver stands in its
     stand;
   - the wiring board is still inside its mark and the supply lead is still in its strain clip;
   - no part, lead, or bulb is loose on the table.
2. Return the right arm home with its gripper open. The left arm is already home. Homing is the last
   thing the arm does.
3. Stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Check that the rocker is pressed to O.
2. Turn the bulb a quarter turn counter-clockwise, lift it out of the lamp holder, and stand it base
   down in the bulb nest cup, collar proud.
3. Take the driver and open all six screws, in the order 2, N, L, B, A, 1, far enough that a stripped
   end passes the screw. Stand the driver back in its stand, handle up.
4. Lift each lead out of its channel slot, pull both ends out of their terminals, and lay each lead in
   its own rack slot: W1 red in slot 1, W2 black in slot 2, W3 blue in slot 3. Straighten any bend and
   check both stripped ends for kinks and splayed strands.
5. Press each part's lock tab down, slide the part forward off its mount pins, lift it off, and stand
   it in its own bay: switch in bay 1, lamp holder in bay 2, terminal strip in bay 3.
6. Wipe the terminals, the stripped ends, the mount pins, the driver blade, and the bulb collar and
   glass clean and dry.
7. Stand the wiring board inside its mark, square to the front edge, with a thin band of tape showing
   all the way around it, and the supply lead in its strain clip. Stand the parts tray in the start zone
   for the next episode's config — front center (Config M), front right (Config R1), or back right
   (Config R2) — leaving the other two zones bare, and the bulb nest at the front right, or at the back
   right in Config R1.
8. Clear away anything loose on the table.
9. Check the board mark and re-tape it if it is lifting, torn, or unreadable. Check that the printed
   diagram and the wiring table are still readable.
10. Inspect the three parts, the three leads, the six screws, the mount pins, the lock tabs, the comb,
    the bulb, the driver, and every fixture for damage. Replace damaged items.
11. Run both Setup checklists again.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

- the **start timestamp** in the video;
- the **violation name** from the list below; and
- the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an
annotation label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain several violations; tag each
one separately. Retain the episode in training data with its violation tags. Do not delete a recorded
episode solely because it contains a violation.

### Violations

**Note on the start position:** the violations below were written for Config R2 (parts tray at the back
right, bulb nest at the front right). The pickup and arm-role cues will be rewritten later to cover all
three start positions; they are left as they are for now. Until then, anything that does not match the
episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

- **Visible cue:** what the operator does does not match the config on the table — the parts tray is not
  in the start zone for the config, or the bulb nest is not in its place for the config; the right
  gripper reaches across the table's center line for a part or the bulb, or the left arm reaches for one;
  or the wrong IF line is followed.
- **SOP rule broken:** the start position and the same-side rule (the parts tray starts at the front
  center in Config M, the front right in Config R1, or the back right in Config R2, and the bulb nest
  stands at the back right in Config R1; the right gripper lifts every part and the bulb in every config
  and never leans across the center line; the IF line followed is the one for the config on the table).
- **Coaching note:** look where the parts tray is before the first reach, then follow that config's IF
  lines through Steps 1 and 5.

**Violation: Wrong phase order**

- **Visible cue:** a lead is landed before all three parts are locked down, a screw is turned before
  all six ends are home and all three leads are dressed, a lead is tug-tested before its screw is
  closed, the bulb goes in before the tug tests are done, or a part is mounted after the wiring has
  started.
- **SOP rule broken:** Steps 1 to 6, work the six phases in the fixed order: mount the three parts,
  land and dress the three leads, close the six screws, tug-test the six ends, fit the bulb, test the
  switch.
- **Coaching note:** finish each phase and its check before starting the next one.

**Violation: Wrong mount order**

- **Visible cue:** the lamp holder or the terminal strip is mounted before the switch, or the strip is
  mounted before the lamp holder.
- **SOP rule broken:** Step 1, mount in the fixed order switch, lamp holder, terminal strip.
- **Coaching note:** switch, holder, strip, every episode. The strip is last so the board is not on
  the supply while the other two are pushed down.

**Violation: Part on the wrong outline or the wrong way round**

- **Visible cue:** a part is lowered onto an outline printed with another part's name, sits across two
  outlines, or is locked down turned so terminal A, L, or 1 is on the right instead of the left.
- **SOP rule broken:** Step 1 (each part goes on its own printed outline, turned so A, L, and 1 are on
  the left).
- **Coaching note:** read the name printed beside the outline and check the terminal labels before
  lowering the part.

**Violation: Part not locked down**

- **Visible cue:** the episode moves on with a lock tab still lying down, a gap showing under a foot,
  or a part that lifts, rocks, or slides when it is pulled or when a screw is turned near it.
- **SOP rule broken:** Step 1 (push the part straight back until the lock tab springs up, then confirm
  with a light pull).
- **Coaching note:** look at the tab from the front after every part. Down means the part has not gone
  back far enough.

**Violation: Part gripped wrong**

- **Visible cue:** the right gripper closes on the rocker, inside the lamp holder opening, on a
  terminal, on a screw, or on the foot instead of on the part's body flats; or it drags a part out of
  its bay sideways.
- **SOP rule broken:** Step 1, close on the part's body flats only, and lift it straight up out of its
  bay.
- **Coaching note:** the two bare side faces are the only handles. Straight up out of the bay, never
  dragged.

**Violation: Lead run to the wrong terminal**

- **Visible cue:** a lead ends up in a terminal the wiring table does not name for it, the two ends of
  a lead are landed the wrong way round, or the leads are worked in an order other than W1, W2, W3.
- **SOP rule broken:** Step 2 (run W1 from strip 1 to switch A, W2 from switch B to holder L, W3 from
  holder N to strip 2, in that order).
- **Coaching note:** read the wiring table printed at the back of the board before lifting a lead out
  of the rack, not after.

**Violation: End not fully home**

- **Visible cue:** the episode moves on with bare copper showing outside a hole, with an insulation
  shoulder standing off the terminal face, or with an end that fell out of its hole and was left out.
- **SOP rule broken:** Step 2 (push each stripped end in until the insulation shoulder touches the
  terminal face, and push it in further if bare copper shows).
- **Coaching note:** look along the terminal face after every end. Any copper showing means it is not
  home.

**Violation: Stripped end pinched, bent, or forced**

- **Visible cue:** the right gripper closes on the bare copper instead of the insulation, a stripped
  end is kinked or splayed, an end is pushed in at an angle, or a lead is twisted while it is pushed.
- **SOP rule broken:** Step 2, hold each lead by its insulation, and push each end straight in without
  twisting or forcing.
- **Coaching note:** hold the plastic, come in straight. If it will not go in, pull back and
  straighten the end instead of pushing harder.

**Violation: Lead not dressed or dressed wrong**

- **Visible cue:** a lead is left lying on top of the comb, sits in a slot with another lead's number,
  lies over another lead, or lifts back out of its slot and is left there; or the second end is landed
  before the lead is pressed into its slot.
- **SOP rule broken:** Steps 2.3 and 2.4 (press each lead into its own numbered channel slot, below
  the top of the comb, before landing its second end).
- **Coaching note:** the comb is what holds the lead while the gripper lets go. Press it down and
  watch it stay before moving on.

**Violation: Driver picked up or held wrong**

- **Visible cue:** the right gripper drags the driver out of its stand sideways, closes on the blade
  end instead of the handle, holds it leaning so the blade is not in line with the screw, or stands it
  back up part way through the six screws.
- **SOP rule broken:** Steps 3.1 and 3.3 (lift the driver straight up by its handle, hold it blade
  down and in line, keep it in the gripper for all six screws, and park it only at the end).
- **Coaching note:** straight up by the handle, blade down, and it stays in the gripper until all six
  screws are closed.

**Violation: Blade not seated**

- **Visible cue:** the blade sits across the screw slot instead of down in it, skates out of the slot
  while turning, chews the screw head, or the right gripper turns a screw with its own tip instead of
  the driver.
- **SOP rule broken:** Step 3.2 (set the blade down in the screw slot, in line with it, and reseat it
  if it skates out).
- **Coaching note:** down in the groove and in line before any turn. Reseat instead of pushing
  through a slipping blade.

**Violation: Wrong screw order**

- **Visible cue:** the six screws are closed in any order other than 1, A, B, L, N, 2 — most often
  part by part, or nearest first.
- **SOP rule broken:** Step 3, close the screws in loop order 1, A, B, L, N, 2.
- **Coaching note:** follow the circuit round: strip, switch, holder, back to the strip.

**Violation: Screw left open or forced past its stop**

- **Visible cue:** the episode moves on with a screw that still turns freely or was given only one
  quarter turn; or the driver keeps turning a screw that has already stopped, or turns more than a
  quarter turn in one grip.
- **SOP rule broken:** Step 3.2 (turn in quarter turns until the screw stops, and stop turning once it
  has stopped).
- **Coaching note:** quarter turn, lift, reseat, repeat, and stop the moment it goes solid.

**Violation: Tug test skipped or done wrong**

- **Visible cue:** an end is never pulled, the pull is a jerk, the lead is pulled sideways, upward, or
  twisted, the pull is made by the bare copper, or the ends are tested in an order other than 1, A, B,
  L, N, 2.
- **SOP rule broken:** Step 4 (pinch the insulation in front of the terminal and pull straight out,
  light and steady, for a count of one, in loop order).
- **Coaching note:** straight out, gently, one count, every end. A jerk tells you nothing and can pull
  a good end loose.

**Violation: Failing end left as it is**

- **Visible cue:** an end slides out or its insulation shoulder lifts during the tug test, and the
  episode moves on without pushing the end home and closing the screw again.
- **SOP rule broken:** Step 4 (an end that pulls out is pushed home, its screw is closed again, and
  the end is tug-tested a second time).
- **Coaching note:** a failed tug is fixed there and then, not noted and left.

**Violation: Bulb gripped by the glass**

- **Visible cue:** the right gripper closes on the glass of the bulb, anywhere above the base collar,
  in the nest or in the holder.
- **SOP rule broken:** Step 5, close on the base collar only, never on the glass.
- **Coaching note:** the metal band at the bottom is the only handle, going in and coming out.

**Violation: Bulb not locked**

- **Visible cue:** the episode moves on with the bulb standing high off the holder rim, leaning, or
  lifting on the light pull; or the bulb is turned counter-clockwise, forced while leaning, or pushed
  in without a quarter turn.
- **SOP rule broken:** Step 5 (drop both pins into the L-slots, push down, turn a quarter turn
  clockwise to the stop, and confirm with a light pull).
- **Coaching note:** pins in, push, quarter turn clockwise to the stop, then pull once to check.

**Violation: Switch pressed before the bulb is in**

- **Visible cue:** the rocker is pressed to I at any point before the bulb is locked in the holder, or
  a lead, screw, or the bulb is touched while the rocker stands at I.
- **SOP rule broken:** Steps 1 to 5, the rocker stays pressed to O until Step 6, and Step 6.1, nothing
  on the board is touched while the rocker is at I.
- **Coaching note:** the board is on the supply from the moment the strip locks down. The rocker only
  moves in Step 6, and nothing on the board is touched while it is at I.

**Violation: Switch pressed wrong**

- **Visible cue:** the right gripper presses the rocker with open jaws, pinches or grips the rocker,
  pushes it sideways, presses both halves at once, or runs more than one on and off cycle.
- **SOP rule broken:** Step 6 (press with closed jaws, straight down on one half, one on and off cycle
  only).
- **Coaching note:** close the gripper first, come straight down on one half, once on and once off.

**Violation: Fixture moved**

- **Visible cue:** the wiring board shifts off its taped mark, or is gripped, lifted, or pushed; the
  parts tray, the lead rack, the driver stand, or the bulb nest is pushed, dragged, or knocked out of
  place; or the supply lead is gripped, pulled, or lifted out of its strain clip.
- **SOP rule broken:** Steps 1 to 6, the wiring board stays inside its mark and every fixture stays
  where it is. None of them is ever gripped or pushed, and the supply lead is never touched.
- **Coaching note:** come down onto the board or a fixture from straight above, and do not lean the
  gripper or the driver body against one.

**Violation: Parked arm moved**

- **Visible cue:** the left arm leaves home, its gripper closes, or it reaches toward, holds, or
  steadies anything at any point in the episode.
- **SOP rule broken:** Steps 1 to 7, this is a single-arm task. The left arm stays at home with its
  gripper open from the start of recording to the end.
- **Coaching note:** the fixtures do the holding. If a step feels like it needs a second gripper, stop
  and report the fixture, do not use the left arm.

**Violation: Item dropped or knocked over**

- **Visible cue:** a part, lead, driver, or the bulb falls from the right gripper onto the board, the
  table, or the floor; a part is knocked over in its tray bay; a lead is pulled out of the rack and
  left on the table; or a dropped item is left where it fell.
- **SOP rule broken:** Steps 1 to 6 (lift each item clear, carry it on the path its step names, and
  release it only when it is stable).
- **Coaching note:** lift higher over the board and the fixtures, and slow the carry near the mounted
  parts.

**Violation: Finished work disturbed later**

- **Visible cue:** a locked part is pushed, turned, or unlocked during a later step; a landed end is
  pulled out or a dressed lead lifted out of its slot for no reason; a closed screw is reopened or
  turned again with no failed tug test; or the bulb is turned or lifted after Step 5.
- **SOP rule broken:** Steps 2 to 6, once a part, an end, a screw, a dressed lead, or the bulb is in
  place it stays there, untouched, for the rest of the episode.
- **Coaching note:** route the arm around the finished side of the board once a phase is done.

**Violation: Check skipped**

- **Visible cue:** the right arm moves straight on with no look at the step's end state: no light pull
  after a part, no look along a terminal face after an end, no look at a lead sitting in its slot, no
  look at the screw stopping, no light pull after the bulb, or no look at the bulb after the rocker is
  pressed to I or to O.
- **SOP rule broken:** Steps 1 to 6, each step's check is done before the next step starts, including
  the look at the bulb after each press of the rocker in Step 6.
- **Coaching note:** every step ends with a look, and the fix happens in that step, not later.

**Violation: Wrong episode ending**

- **Visible cue:** the episode ends with a part unlocked or on the wrong outline, an end not home, a
  screw open, a lead out of its slot, the bulb missing or loose, the rocker still at I, the driver out
  of its stand, a bay or rack slot not empty, or a loose item on the table; or the right arm is away
  from home, a gripper is closed, or an arm makes a correction after homing.
- **SOP rule broken:** Step 7 (confirm the end state, return the right arm home with its gripper open,
  then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arm does.

### Non-violation failures

Failures that are not caused by how the task was run do not go in the violation set. Log them as
system issues, discard the episode, and do not use them for coaching.

- **Recording stopped or paused during the episode** (recording system).
- **Camera dropped frames or lost feed** (capture system).
- **Hardware fault on an arm:** gripper failure, drift, collision caused by controller error, or motor
  error.
- **Supply fault:** the bench supply is off or trips during the episode, or the supply lead has come
  away from the back of the board.
- **Defective item:** a stripped terminal screw, a chewed screw head, a broken lock tab or bent mount
  pin, a lead with splayed or broken strands, a lamp holder with a damaged L-slot, a bulb that does
  not light in a known-good holder, a switch that will not click over, a fixture that slides on its
  own, or a taped outline that lifts off the table during the episode. Replace before the next
  episode.

## Annotation subtasks (from SOP)

1. Lift one part out of its tray bay and lock it on its outline
2. Light-pull one mounted part
3. Pick one lead from its rack slot
4. Push one stripped end fully home into its terminal
5. Press one lead down into its channel slot
6. Take the driver from its stand
7. Close one terminal screw
8. Park the driver in its stand
9. Tug-test one lead end
10. Fit the bulb into the lamp holder
11. Press the switch on and look at the bulb
12. Press the switch off and look at the bulb
13. Return the right arm home and end the episode
