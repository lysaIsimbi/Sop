# Assemble a Flat-Pack Stool SOP (Four Legs and Braces)

This SOP covers assembling a single flat-pack stool from one kit using a two-arm robot system. Both arms
are used throughout: the grippers cooperate to carry the kit tote, open the hardware pouch, load the seat
into the seat fixture, fit the four legs and four braces and drive their bolts with a powered driver,
roll the stool over in a cradle, level-check it and seat every bolt in sequence, with the left and right
grippers taking the specific roles called out in each step. The task runs from a kit tote in the start
zone to a finished stool standing in the output zone.

The table is set up in one of three ways. Only the kit tote moves; the seat fixture, the cradle, the stand
plate, the two trays and the holders are in the same place in all three.

- **Config L1:** the kit tote is at the back-left. The finished stool goes to the back-right.
- **Config L2:** the kit tote is at the left edge, midway between the back-left corner and the parts tray.
  The finished stool goes to the back-right.
- **Config R:** the kit tote is at the back-right. The finished stool goes to the back-left instead.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line
that matches.

What stays constant across all sessions:

- **Start position:** the kit tote starts at the back-left (**Config L1**), the left edge (**Config L2**) or
  the back-right (**Config R**). One config per episode, chosen before recording and never changed
  mid-episode.
- **Two grippers on the tote:** the kit is never lifted by one arm. Both grippers take opposite tote
  handles wherever the tote starts, and the loaded tote is confirmed inside the two-arm payload during
  setup. No single gripper ever fetches the tote from the other side of the table.
- **Fixed roles:** the config changes only the carry direction in Step 1, where the empty tote goes back
  in Step 3.2, and which back corner the finished stool goes to in Step 9. Every other grip, place and
  tool is the same in all three.
- **Arm zones:** the left arm works the input zone on the left (Config L1 and L2), the back-center unload
  position and the front-left parts tray. The right arm works the back-center unload position, the
  front-right hardware tray and the right edge. Neither arm reaches across the table midline for a part
  on the other side. Two-arm carries and the shared work positions on the midline are the only places
  both arms work the same object.
- **Bolts are driven, never finger-turned:** every bolt is picked from the bolt card by the driver's
  magnetic bit and driven with the driver. No gripper ever turns a bolt in its jaws.
- **Bring the work to the arms:** every leg and every brace is fitted and bolted at the assembly
  position, and every corner press and every bolt in Step 8 happens at the drive position. Both sit on
  the table midline. The fixture and the stand plate are indexed to bring each corner, side and leg to
  those positions; the arms never reach around the work.
- **Never unheld:** a leg is held by the left gripper from the moment it enters its socket until its
  first bolt is run down. A brace is held from the moment its first end enters a slot until that end's
  bolt is run down. Only one leg is ever moved at a time.
- **No loose hardware:** the sixteen bolts arrive as bolt-washer sets standing head-up in the bolt card.
  Hardware is never poured, tipped or spread on the table, and a washer is never picked as a separate
  part.
- **Seat target:** the seat is seated face down in the seat fixture against all four corner stops, with
  all four leg sockets visible, before any leg is fitted.
- **Proud until levelled:** every bolt is run down only until its head stands about 2 mm proud through
  Steps 4-7. No bolt is seated until the stool is rolled over and the level-check passes.
- **Supported roll-over:** the stool is turned over in two 90° moves through the roll-over cradle, and is
  held by both grippers or resting in the cradle at every moment. It is never turned 180° in one move and
  never released in mid-turn.
- **Tighten sequence:** the legs are seated in cross order, alternating between the two bolts at each
  leg, then each leg's two brace-end bolts as that leg comes forward, then a final pass over the legs.

## Setup

Go through both checklists before starting the episode.

### Hardware checklist

- Cameras are on and recording
- Env camera frame includes the front and back edges of the table and is centered on the table's
    midpoint
- Both arms are at the home position with grippers open
- The seat fixture is bolted at the center of the table, empty, and its base turns freely and clicks
    at all four detents
- The seat fixture is at its start index, with one corner stop facing the operator at the assembly
    position
- The roll-over cradle is fixed at the front-center, empty, and its pads are clean
- The stand plate is fixed at the near-center, empty, flat, level, and locks at each of its four
    detents
- The driver is charged, its bit is magnetized and holds a bolt-washer set, and its clutch is set to
    the station's stool setting and releases at that setting on a test bolt
- Table surface is clear of any objects other than the kit tote(s), the fixture, the cradle, the
    stand plate and the two trays

### Materials checklist

- Kit tote(s) are placed in the start zone for this episode's config, one kit per tote, each tote with
    its two handles on the left and right sides and its long edge parallel to the back edge of the table
    - **Config L1:** back-left
    - **Config L2:** left edge, midway between the back-left corner and the parts tray
    - **Config R:** back-right
- Each tote holds 1 seat face up on top, 4 legs, 4 braces and 1 sealed hardware pouch, and nothing
    else
- Each hardware pouch holds one bolt card carrying 16 bolt-washer sets, each set standing head-up in
    its own hole
- Loaded tote weight is confirmed at or under the two-arm payload limit for the station (checked off
    record during station setup, not during the episode)
- The parts tray is at the front-left, with its leg compartment, brace compartment and shim
    compartment empty except for 4 shims in the shim compartment
- The hardware tray is at the front-right and is empty
- The driver and the level are at the right edge, in their holders
- The back-center unload position is clear (working area for the kit tote)
- The output location for the finished stool / row is clear: back-right (Config L1 and L2) or back-left
    (Config R)

## Workspace layout

- **Start zone**: kit tote(s), seat face up on top (input) — back-left (Config L1), left edge (Config L2)
  or back-right (Config R)
- **Back-center**: unload position, where the kit tote is unloaded in Step 2
- **Center**: seat fixture on its indexing base, holding the seat face down during assembly
- **Assembly position**: the near corner of the seat fixture, at the table midline, where every leg and
  every brace is fitted and bolted
- **Front-center**: roll-over cradle, where the stool is turned over in two 90° moves
- **Near-center**: stand plate on its indexing base, where the stool stands for the level-check and the
  tightening
- **Drive position**: the front corner of the stand plate, at the table midline, where every corner press
  and every bolt in Step 8 happens
- **Front-left**: parts tray, with a leg compartment, a brace compartment and a shim compartment
- **Front-right**: hardware tray, holding the bolt card
- **Right edge**: driver and level, in their holders
- **Back-right**: finished stool / row of finished stools (output) — in Config R the output is the
  back-left instead

## Vocabulary

These are the terms used in this SOP. Operators and annotators must use this language consistently. One
term per concept, used throughout.

### Stool anatomy

- **Stool:** a single finished assembly of one seat, four legs and four braces.
- **Kit:** the unassembled parts for one stool, as delivered in one tote in the start zone.
- **Kit tote:** the shallow handled tote the kit is delivered in. It has one handle on its left side and
  one on its right side.
- **Tote handle:** one of the two grasp points on the kit tote. A tote is only ever lifted by both
  handles, one gripper on each.
- **Seat:** the flat square top that the four legs attach to.
- **Face:** the finished side of the seat. It points down during assembly.
- **Underside:** the side of the seat opposite the face. The legs go here.
- **Seat corner:** one of the four corners of the seat. The seat is always held corner-forward, so one
  corner faces the operator, one faces away, and one faces each arm. Grips on the seat are taken at the
  **left seat corner** and the **right seat corner**.
- **Leg socket:** one of the four recesses in the underside that a leg top sits in.
- **Mounting corner:** the corner of the underside holding one leg socket.
- **Leg:** one of the four uprights that carry the seat.
- **Leg top:** the squared end of a leg that sits in a leg socket.
- **Foot:** the bottom end of a leg that rests on the table.
- **Brace slot:** one of the two notches part way down a leg that a brace end sits in.
- **Brace:** one of the four cross rails that tie two adjacent legs together.
- **Brace end:** the shaped end of a brace that sits in a brace slot.
- **Brace ring:** the four braces in place, forming a closed square between the legs.

### Fixture anatomy

- **Seat fixture:** the low-profile square fixture at the center of the table that holds the seat face
  down and level during assembly. Its four corner stops register the seat so the seat never has to be
  squared to the table by hand.
- **Corner stop:** one of the four pads in the fixture that a seat corner sits against. The stops sit
  under the seat and leave the corner tips free, so a gripper can still take the seat by a corner.
- **Seated in the fixture:** the seat lies flat in the fixture with all four corners against their corner
  stops and no gap at any corner.
- **Indexing base:** the turntable under the fixture, and the one under the stand plate. Each turns in
  90° detents and clicks at every one.
- **Assembly position:** the near corner of the fixture, at the table midline. Both arms reach it. Every
  leg and every brace is fitted and bolted here.
- **Working corner:** the mounting corner of the seat that is at the assembly position right now.
- **Working side:** the seat side facing the operator at the assembly position right now, between the two
  front corners of the fixture. Each brace goes on a working side.
- **Index:** turn an indexing base one detent, so the next corner, side or leg comes to the assembly
  position or the drive position. Unless a step says otherwise, index clockwise.
- **Start index:** the detent the fixture and the stand plate are left at during setup and returned to at
  the end of the episode.
- **Roll-over cradle:** the padded vee at the front-center that the stool rests on its side in, between
  the two 90° moves of the roll-over.
- **Stand plate:** the flat, level plate at the near-center, on its own indexing base, that the stool
  stands on for the level-check and the tightening. It locks at each detent.
- **Drive position:** the front corner of the stand plate, at the table midline.
- **Working leg:** the leg standing at the drive position right now. The seat corner directly above it is
  the corner that gets pressed in the level-check.

### Hardware anatomy

- **Hardware pouch:** the sealed zip-top pouch in the kit holding the bolt card.
- **Pouch tab:** the pull tab at the right end of the hardware pouch seal.
- **Bolt card:** the moulded card that holds the 16 bolt-washer sets standing head-up, two rows of eight.
  It is the only place hardware is picked from.
- **Bolt-washer set:** one bolt with its washer already captive on the shank under the head. Two sets per
  leg, one per brace end. Hardware is only ever handled on the driver bit; a loose washer is never
  picked.
- **Bolt head:** the socketed top of a bolt, the part the driver bit sits in.
- **Driver:** the powered hex driver held in the right gripper. It is the only thing that turns a bolt.
- **Bit:** the magnetic hex bit on the driver. It picks a bolt-washer set off the card by its head and
  holds it while the bolt is set in its hole.
- **Clutch:** the driver's torque limiter. It clicks and stops driving when the bolt head is seated.
- **Run down:** drive a bolt until its head stands about 2 mm proud, then stop. This is what every bolt
  gets in Steps 4 and 5.
- **Seat (a bolt):** drive a bolt until its head sits flat and the clutch clicks. This happens only in
  Step 8.
- **Proud:** a bolt head stands above the leg or brace with a visible gap.
- **Draw down:** a bolt turns into its thread and pulls itself into the hole. A bolt that does not draw
  down on its first turn is not in its thread.
- **Cross-threaded:** a bolt that has entered its thread at an angle and binds.
- **Shim:** a thin pad placed under one foot to remove wobble. Shims live in the parts tray and are not
  part of the kit.
- **Level:** the bubble level laid on the seat to check the stool sits level.
- **Bubble:** the air bubble in the level; centred between the marks means level.
- **Wobble:** movement of a foot off the plate when the seat corner above another leg is pressed.
- **Short leg:** the leg whose foot lifts off the plate during the level-check.

### Workspace zones

- **Start zone:** input zone holding the kit totes — back-left (**Config L1**), left edge (**Config L2**)
  or back-right (**Config R**). One per episode, chosen before recording and never changed mid-episode.
- **Back-center unload position:** the clear patch behind the fixture where the kit tote is unloaded.
- **Front-left tray:** the parts tray holding the sorted legs, braces and shims. The left arm serves it.
- **Front-right tray:** the hardware tray holding the bolt card. The right arm serves it.
- **Right edge:** the holders for the driver and the level.
- **Back-right edge:** output zone where the finished stool is placed at the back-right of the table in
  Config L1 and L2. In Config R the output zone is the back-left edge.
- **Table midline:** the front-to-back line through the center of the table. It divides the left arm's
  zone from the right arm's zone. The unload position, the assembly position, the cradle and the drive
  position all sit on it.
- **Home position:** the default resting pose for each arm: gripper open and clear of the table.

### Actions

- **Carry:** move the kit tote with both grippers on its two handles, lifted clear of the table.
- **Unload:** take the parts out of the kit tote and place each one in its assigned compartment or tray.
- **Open:** draw the pouch tab across the seal while the other gripper holds the pouch flat.
- **Load:** set the seat face down into the seat fixture against all four corner stops.
- **Fit:** set a leg top in its leg socket, or a brace end in its brace slot, at the assembly position.
- **Hold:** keep a gripper closed on a leg or brace so it cannot fall or rotate before its bolt is run
  down.
- **Pick a bolt:** lower the driver bit onto the head of the next bolt-washer set in the card until the
  magnet holds it, then lift it straight out.
- **Run down:** drive a bolt until its head stands about 2 mm proud, then stop.
- **Index:** turn an indexing base one detent to bring the next corner, side or leg to the assembly
  position or the drive position.
- **Roll over:** turn the stool from face down to standing on its feet, in two 90° moves through the
  roll-over cradle.
- **Level-check:** press the seat corner above each leg in turn at the drive position, then read the
  level in two directions.
- **Shim:** place one shim under a short leg at the drive position.
- **Seat (a bolt):** drive a bolt with the driver until the bolt head sits flat and the clutch clicks.
- **Stage:** place the finished stool in the output zone (batch sessions place them in a row).

## Steps

Steps 1, 3.2 and 9 depend on where the kit tote starts: Step 1's grasp and carry direction, where the empty
tote goes back in 3.2, and in Config R which back corner the finished stool goes to in Step 9. Both
grippers carry the tote in every config. Every other line is the same in all three configs.

### Step 1: Carry a kit tote to the unload position

**Goal:** one kit tote sits at the back-center unload position, ready to be unloaded, carried there by
both grippers.

Look where the kit tote is before reaching for it.

- **IF the kit tote is at the back-left (Config L1):** with the left gripper, grasp the left handle of the
  front tote in the back-left pile, and with the right gripper, grasp its right handle. Carry it straight
  right along the back edge to the unload position.
- **IF the kit tote is at the left edge (Config L2):** with the left gripper, grasp the left handle of the
  front tote at the left edge, and with the right gripper, grasp its right handle. Carry it back and to the
  right, behind the fixture, to the unload position.
- **IF the kit tote is at the back-right (Config R):** with the left gripper, grasp the left handle of the
  front tote in the back-right pile, and with the right gripper, grasp its right handle. Carry it straight
  left along the back edge to the unload position.

Then, in all three:

- Confirm both grippers are closed on the handles before any lift, then lift the tote clear of the table
  with both arms together; do not drag or slide it.
- Set it down flat at the back-center unload position with its handles still to the left and right, and
  release both grippers.
- Move one tote only. Do not lift a tote by its rim, by its edge or with one gripper.

**Warning:** A loaded tote is a two-arm object. A one-arm grasp on an edge or a rim can spill the kit or
rotate the tote out of the gripper, and a loaded kit can exceed the single-arm payload.

### Step 2: Unload and sort the kit

**Goal:** the legs, braces and bolt card are in their assigned compartments, every group is counted
against the parts list, and only the seat is left in the tote.

#### 2.1 Unload the legs and braces

- With the left gripper, lift the seat off the top of the kit and set it face up on the table just left
  of the tote, clear of the fixture.
- With the left gripper, move the four legs one at a time from the tote to the leg compartment of the
  parts tray at the front-left, and lay them in one group, all feet pointing the same way.
- With the left gripper, move the four braces one at a time to the brace compartment of the parts tray.
- Confirm no part sits across a compartment wall or outside the tray.

#### 2.2 Open the hardware pouch with both grippers

- With the right gripper, lift the hardware pouch out of the tote and lay it flat at the unload position,
  seal to the back and pouch tab to the right.
- With the left gripper, close on the body of the pouch below the seal and hold the pouch flat against
  the table. Keep it held for the whole of 2.2.
- With the right gripper, close on the pouch tab and draw it to the right along the seal until the pouch
  is open across its full width.
- With the right gripper, take the bolt card by its right edge, lift it straight out of the pouch, and
  set it in the hardware tray at the front-right with the bolt heads up.
- With the left gripper, release the pouch.
- Do not tip, shake or empty the pouch, and do not pour the bolt-washer sets out of the card. Every bolt
  is picked off the card by the driver bit in Steps 4 and 5.

**Warning:** The pouch is only ever opened with both grippers, one holding and one drawing the tab. A
one-gripper pull on an unheld pouch tears the pouch and scatters the hardware.

#### 2.3 Count against the parts list

- Count each group in turn: 4 legs in the leg compartment, 4 braces in the brace compartment, 16
  bolt-washer sets standing in the bolt card, 4 shims in the shim compartment.
- Confirm the legs are all the same length and the braces are all the same length.
- Confirm every bolt in the card carries its washer under the head and stands head-up in its hole.
- If any group is short, holds an extra part, holds a part of the wrong length, or holds a bolt with no
  washer → stop the episode and report a defective kit.

#### 2.4 Clear the unload position

- With the left gripper, put the empty hardware pouch and any packaging into the empty tote.
- Confirm the unload position holds the tote only, with the seat beside it, and every other part is in
  its compartment.

### Step 3: Load the seat into the fixture

**Goal:** the seat is seated face down in the seat fixture against all four corner stops, corner-forward,
the underside is clear and the four leg sockets are readable, and the empty tote is off the working area.

#### 3.1 Turn the seat face down and load it

- With the left gripper, grasp the left seat corner, and with the right gripper, grasp the right seat
  corner.
- Lift the seat 5 cm clear of the table, turn it over in one smooth motion so the underside is up, and
  carry it over the fixture.
- Lower it into the fixture, corner-forward, so one seat corner faces the operator at the assembly
  position, and release both grippers.
- If the seat is already underside up when it comes out of the tote → carry it straight to the fixture
  without the turn.

#### 3.2 Return the empty tote

- With both grippers on its two handles, lift the empty tote clear of the table, carry it back to the
  start zone for this episode's config, and set it down beside the kit pile.
- Confirm the unload position is now clear.

#### 3.3 Confirm the seat is seated in the fixture

- Confirm all four seat corners sit against their corner stops with no gap at any corner.
- Confirm the seat lies flat in the fixture with no rock at any corner.
- If a corner stands off its stop → with both grippers on the left and right seat corners, lift the seat
  2 cm, lower it again, and re-check. Do not push a corner down onto a stop with one gripper.

#### 3.4 Clear and read the underside

- Confirm the underside is clear and one leg socket is visible at each of the four mounting corners.
- If a kit part is lying on the underside → with the left gripper, pick that part up on its own and place
  it in its assigned compartment in the parts tray. Do not sweep, drag or push parts across the seat.
- If anything that is not a kit part is on the seat or in the fixture → stop the episode. This is a
  station setup failure: reset the station off record and start a new episode.
- Confirm each socket shows two bare bolt holes through it.
- If a socket or a bolt hole is blocked, split or unreadable → stop the episode and report a defective
  seat.

### Step 4: Attach the four legs at the assembly position

**Goal:** four legs stand square to the seat, each held by two bolts run down to about 2 mm proud, every
one fitted at the assembly position, with no bolt seated.

#### 4.1 Take up the driver

- With the right gripper, take the driver from its holder at the right edge and keep it for the whole of
  Steps 4 and 5.
- Confirm the bit is clear and holds nothing.

#### 4.2 Fit the leg at the working corner

- With the left gripper, take one leg from the leg compartment of the parts tray and bring it to the
  assembly position.
- Set its leg top in the leg socket at the working corner and turn the leg until its two brace slots face
  the two adjacent mounting corners.
- Press the leg top down until it sits flat in the socket, and **keep the left gripper closed on the
  leg**.
- Confirm the two bolt holes in the leg top line up with the two holes in the socket.
- If the leg top rocks in the socket → lift it clear, look at what is under it, deal with it under 3.4,
  and fit the leg again.

#### 4.3 Run down the two bolts

- With the driver in the right gripper, lower the bit onto the head of the next bolt-washer set in the
  bolt card until the magnet holds it, then lift the bolt straight out of the card.
- Bring the bolt to the assembly position, set its tip in one bolt hole square to the seat, and press the
  trigger briefly to turn it one turn.
- Confirm the bolt draws down into the hole. If it does not draw down, or the driver stalls → lift the
  driver straight up so the magnet brings the bolt back out, set the bolt in the hole again square, and
  try again. If the bolt has bitten and will not lift out → stop the episode and report a cross-threaded
  bolt.
- Once the bolt draws down, drive it until its head stands about 2 mm proud, then stop. Do not seat it
  and do not let the clutch click.
- Keep the left gripper closed on the leg until this first bolt is run down, then release it.
- Pick a second bolt-washer set off the card the same way and run it down in the second bolt hole in the
  same leg.

**Warning:** The leg must be held by the left gripper or by a run-down bolt at every moment. Never
release the leg to go and pick a bolt while nothing else holds it.

#### 4.4 Index and fit the remaining three legs

- Index the fixture one detent so the next mounting corner comes to the assembly position.
- Repeat 4.2 and 4.3 at that corner, then index and repeat twice more, until all four legs are fitted.
- After the fourth leg, index once more so the fixture is back at its start index.
- Confirm four legs are fitted, 8 bolts stand about 2 mm proud, and each leg stands within 5° of square
  to the seat.

**Warning:** Every leg is fitted at the assembly position. Do not reach around the fixture to a corner
that has not been indexed round, and do not fit two legs at one index.

### Step 5: Add the braces at the assembly position

**Goal:** four braces form a closed brace ring between the legs, each brace end held by one bolt run down
to about 2 mm proud, every one fitted at the assembly position, with only one leg moved at a time.

#### 5.1 Set and bolt the first brace end

- With the left gripper, take one brace from the brace compartment of the parts tray and bring it to the
  assembly position.
- Set one brace end in the brace slot on the left leg of the working side, and **keep the left gripper
  closed on the brace** so it cannot drop or swing.
- With the driver in the right gripper, pick a bolt-washer set off the card, set it in the hole at that
  brace end, confirm it draws down, and run it down to about 2 mm proud.
- Release the brace only once that bolt is run down. The brace now hangs from one bolt and cannot fall.

#### 5.2 Swing the second leg onto the free brace end

- With the left gripper, close on the right leg of the working side and move that one leg until the free
  brace end drops fully into its brace slot. Move one leg only; do not try to draw both legs together at
  once.
- **Keep the left gripper closed on that leg**, holding the joint closed.
- With the driver in the right gripper, pick a bolt-washer set off the card, set it in the hole at the
  second brace end, confirm it draws down, and run it down to about 2 mm proud.
- Release the leg only once that bolt is run down.
- Confirm the brace runs straight between the two legs with no gap at either end.

**Warning:** One gripper cannot control two legs at once. The brace is anchored at one end first, then a
single leg is swung onto the free end while the other gripper drives. Never let go of both the brace and
the leg at the same time.

#### 5.3 Index and add the remaining three braces

- Index the fixture one detent so the next side comes to the assembly position.
- Repeat 5.1 and 5.2 on that side, then index and repeat twice more, until the ring is closed.
- After the fourth brace, index once more so the fixture is back at its start index.
- Confirm the four braces form a closed ring and 16 bolts in total stand about 2 mm proud.
- With the right gripper, return the driver to its holder at the right edge.

**Warning:** All 16 bolts must be run down and no bolt seated before the stool is rolled over. The play
in the joints is what lets the stool sit level.

### Step 6: Roll the stool over onto its feet

**Goal:** the stool stands on its four feet on the stand plate at the near-center, one leg at the drive
position, having been supported through two 90° moves.

#### 6.1 Lift the stool out of the fixture

- With the left gripper, grasp the left seat corner and with the right gripper, grasp the right seat
  corner.
- Lift straight up until the seat is clear of the corner stops, then 5 cm higher. The four legs stand up
  above the seat.
- Do not turn the stool while it is over the fixture.

#### 6.2 First 90°: lay the stool in the cradle

- Carry the stool forward to the roll-over cradle at the front-center.
- Turn it 90° to the right so the seat stands vertical and the four legs point sideways, and lower it
  until the seat and the two lower legs rest in the cradle.
- Release both grippers only once the stool is resting in the cradle.
- Do not turn the stool more than 90° in this move and do not release it in mid-turn.

#### 6.3 Second 90°: stand the stool on the plate

- With the left gripper, grasp the upper seat corner and with the right gripper, grasp the upper leg pair
  just above the feet.
- Lift the stool clear of the cradle and turn it a further 90° in the same direction, so the four feet
  come down and the seat comes level on top.
- Carry it forward and lower it onto the stand plate at the near-center until all four feet touch, then
  release both grippers.
- Confirm one leg stands at the drive position at the front corner of the stand plate. If none does →
  index the stand plate until one does.
- If the stool lands on an edge, a leg folds under, or a bolt backs out → lift it clear, return it to the
  cradle, and do the roll-over again from 6.2.

**Warning:** The stool is held by both grippers or resting in the cradle at every moment of the
roll-over. A single 180° turn in the air runs the wrist out of range and lets the loose joints fold.

### Step 7: Level-check the stool

**Goal:** the stool is confirmed steady on all four feet and level in both directions, with every bolt
still about 2 mm proud, every press taken at the drive position.

#### 7.1 Press each corner at the drive position

- With the right gripper, press down on the seat corner above the working leg with a steady press, and
  watch all four feet.
- Index the stand plate one detent so the next leg becomes the working leg, and press again.
- Repeat until all four corners have been pressed, then index once more so the plate is back where it
  started.
- Keep the left gripper clear of the stool during each press.
- If a foot lifts off the plate → name that leg the short leg and continue to 7.3.

#### 7.2 Read the level

- With the right gripper, take the level from the right edge and lay it across the seat from the near
  corner to the far corner.
- Read the bubble, then lay the level across the seat from the left corner to the right corner and read
  it again.
- If the bubble is centred between the marks in both directions → return the level to the right edge and
  continue to Step 8.
- If the bubble is off centre in either direction → return the level to the right edge and continue to
  7.3.

#### 7.3 Correct a wobble or an off-level seat

- With the left gripper, press down on the center of the seat so every leg top pulls into its socket and
  every brace end pulls into its slot.
- Index the stand plate until the short leg is the working leg.
- With the right gripper, press the short leg down until its foot rests on the plate.
- Repeat 7.1 and 7.2.
- If the same foot still lifts → index the plate until the short leg is the working leg, then with the
  left gripper take one shim from the shim compartment of the parts tray and slide it under that foot at
  the drive position. Repeat 7.1 and 7.2. Use no more than two shims under one foot.
- If a different foot lifts → take the shims out and return to 7.1.
- If the stool still wobbles or reads off level with two shims under one leg → stop the episode and
  report a defective leg.

**Warning:** The stool must stand on all four feet with a centred bubble in both directions before any
bolt is seated. Seating bolts on a wobble locks the wobble in.

### Step 8: Seat the bolts in sequence

**Goal:** all 16 bolt heads are seated flat, driven in the cross order, each one at the drive position,
with no proud bolt and no bolt driven past the clutch.

#### 8.1 First pass: snug the leg bolts

- With the right gripper, take the driver from its holder at the right edge.
- With the left gripper, hold the center of the seat down against the legs. Keep it there through 8.1 to
  8.3.
- Seat the bit in one leg bolt head at the working leg, drive it half a turn, then move to the second
  bolt at the same leg and drive it half a turn; alternate between the two until both are snug.
- Work the four legs in cross order, bringing each to the drive position by indexing the stand plate:
  index two detents to bring the leg opposite the first one forward, then one detent back to the leg
  beside the first, then two detents forward again for the last leg.
- Never reach around the stool to a leg that is not at the drive position.
- If the bit slips out of a bolt head → stop, re-seat the bit square in the bolt head, and drive again.

#### 8.2 Second pass: seat the brace bolts

- Index the stand plate back to the first leg, then work the four legs in the same cross order again.
- At each leg, seat the two brace-end bolts carried by that leg: drive each until its head sits flat and
  the clutch clicks, then stop.
- Keep the left gripper on the seat so the brace ring stays square while each bolt is driven.

#### 8.3 Final pass: seat the leg bolts

- Index the stand plate back to the first leg and work the four legs in the same cross order once more.
- At each leg, seat both leg bolts until each head sits flat against the leg top and the clutch clicks,
  then stop.

#### 8.4 Confirm every bolt is seated

- With the right gripper, return the driver to its holder at the right edge.
- Index the stand plate round one detent at a time and, at each stop, confirm the four bolt heads at the
  working leg sit flat with no gap. Sixteen bolt heads in four stops.
- If a bolt head is proud → take up the driver, seat that bolt at the drive position, and return the
  driver.
- Repeat 7.1 once: if a foot now lifts off the plate → loosen the two leg bolts at that leg by one turn,
  press the seat down, and repeat Step 8 from 8.1.
- Confirm the stand plate is back at its start index.

### Step 9: Move the finished stool to the output zone

**Goal:** the finished stool stands in the designated output zone — back-right (Config L1 and L2) or
back-left (Config R).

- With the left gripper, grasp the left seat corner and with the right gripper, grasp the right seat
  corner.
- Lift the stool clear of the stand plate with both arms together. **IF Config L1 or L2:** carry it back and
  to the right into the output location at the back-right of the table. **IF Config R:** carry it back and
  to the left into the output location at the back-left of the table.
- Set it down on all four feet and release both grippers.
- Batch sessions only: set it beside the stools already there, all seats up, within 10-20 cm and not
  touching. Never set a stool on top of another stool.

### Step 10: Return to home and end the episode

- With the right gripper, confirm the driver and the level are in their holders at the right edge, and
  return the empty bolt card to the hardware tray.
- With the left gripper, return any unused part to its compartment in the parts tray at the front-left.
- Confirm the fixture and the stand plate are both empty and at their start index, and the cradle is
  empty.
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

**Note on the start position:** the violations below were written for Config L1 (kit tote at the
back-left, finished stool to the back-right). The pickup and arm-role cues will be rewritten later to
cover all three start positions; they are left as they are for now. Until then, anything that does not
match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned.**

- **Visible cue:** what the operator does does not match the config on the table — the kit tote is not in
  the start zone for the config; a single gripper reaches across the table to fetch the tote instead of
  both grippers taking its two handles; the empty tote is returned to a different zone; the finished stool
  goes to the wrong back corner; or the wrong IF line is followed.
- **SOP rule broken:** the start position and the two-gripper carry (the tote starts at the back-left in
  Config L1, the left edge in Config L2 or the back-right in Config R, both grippers carry it wherever it
  starts, the empty tote goes back to the start zone, and the finished stool goes to the back-right in
  Config L1 and L2 or the back-left in Config R; the IF line followed is the one for the config on the
  table).
- **Coaching note:** look where the kit tote is before the first reach, then follow that config's IF lines
  through Steps 1, 3.2 and 9.

**Violation: Wrong kit pickup.**

- **Visible cue:** the kit tote is started from the center or the right instead of the back-left pile
  (input pile), it is set down somewhere other than the back-center unload position, or it is dragged or
  slid across the table instead of being lifted clear and carried.
- **SOP rule broken:** Step 1 (take the front tote from the back-left pile and carry it to the
  back-center unload position). Carry means lift and carry, not drag.
- **Coaching note:** always start each kit from the back-left pile and bring it to the unload position.
  Lift the tote clear of the table. Do not drag or slide it.

**Violation: Kit tote lifted with one gripper or off the handles.**

- **Visible cue:** one gripper alone lifts or moves the loaded tote, or a gripper closes on the tote rim,
  edge or a part inside it instead of on a handle, or one arm starts to lift before the second gripper is
  closed on its handle.
- **SOP rule broken:** Two grippers on the tote, Step 1 (both grippers on opposite tote handles,
  confirmed closed before the lift).
- **Coaching note:** a loaded tote is a two-arm object. Close both grippers on the two handles, confirm
  the grip, then lift with both arms together.

**Violation: Picked more than one kit at once.**

- **Visible cue:** two or more totes are lifted or moved from the input pile in a single carry.
- **SOP rule broken:** Step 1 (move one tote).
- **Coaching note:** pick exactly one kit per episode.

**Violation: Hardware pouch opened without support.**

- **Visible cue:** the right gripper pulls the pouch tab while the left gripper is not closed on the
  pouch body, the pouch is lifted off the table while being opened, or the pouch is torn, bitten open on
  a fixture edge, or pulled apart between the two grippers.
- **SOP rule broken:** Step 2.2 (the left gripper holds the pouch flat against the table for the whole of
  the opening; the right gripper draws the tab along the seal).
- **Coaching note:** one gripper holds, one gripper opens. An unheld pouch tears and the hardware ends up
  on the table.

**Violation: Loose hardware created.**

- **Visible cue:** the pouch is tipped, shaken or emptied out, the bolt-washer sets are poured out of the
  bolt card, or bolts end up lying loose in a tray or on the table instead of standing in the card.
- **SOP rule broken:** No loose hardware, Step 2.2 (lift the bolt card out whole and pick each bolt off
  it with the driver bit).
- **Coaching note:** hardware stays in the card. Every bolt is picked head-up off the card by the bit;
  nothing is ever poured out.

**Violation: Bolt handled or turned by a gripper.**

- **Visible cue:** a gripper closes its jaws on a bolt-washer set to carry it, to start it in a hole, or
  to turn it, instead of the bolt being picked and turned by the driver bit; or the operator finger-turns
  a bolt with repeated wrist rotations and re-grasps.
- **SOP rule broken:** Bolts are driven, never finger-turned, Steps 4.3, 5.1 and 5.2 (pick the bolt with
  the magnetic bit and turn it with the driver).
- **Coaching note:** the jaws never touch a bolt. Drop the bit onto the bolt head, let the magnet take
  it, and drive it. Wrist-turning a bolt in the jaws is slow and cross-threads it.

**Violation: Part not put in its assigned compartment.**

- **Visible cue:** a leg, brace or shim is left on the table, dropped in the wrong compartment, laid
  across a compartment wall, or put in the hardware tray, at the end of Step 2.
- **SOP rule broken:** Steps 2.1 and 2.4 (legs to the leg compartment, braces to the brace compartment,
  bolt card to the hardware tray, nothing outside a compartment).
- **Coaching note:** every part has one compartment. Place it there, fully inside the walls, before the
  next part is moved.

**Violation: Parts not counted against the parts list.**

- **Visible cue:** the operator begins Step 3 or Step 4 without counting the groups, or counts only some
  of them, so a short part or a bolt with no washer is never found.
- **SOP rule broken:** Step 2.3 (count 4 legs, 4 braces, 16 bolt-washer sets and 4 shims, confirm the
  lengths match, confirm every bolt carries its washer).
- **Coaching note:** count every group against the parts list. A missing bolt found at Step 8 costs the
  whole episode.

**Violation: Arm crossed the midline for a part.**

- **Visible cue:** the right arm reaches into the front-left parts tray or the back-left input zone, or
  the left arm reaches into the front-right hardware tray or to the driver and level at the right edge.
- **SOP rule broken:** Arm zones (the left arm serves the back-left and the front-left tray, the right
  arm serves the front-right tray and the right edge; only two-arm carries and the midline work positions
  are shared).
- **Coaching note:** each arm stays on its own side for parts. If a part is on the other side, it is the
  other arm's job.

**Violation: Empty tote or packaging left on the table.**

- **Visible cue:** the empty tote is left at the unload position, or the hardware pouch or packaging is
  left in the working area, after Step 3.2.
- **SOP rule broken:** Steps 2.4 and 3.2 (packaging goes into the empty tote, the tote goes back to the
  back-left, the unload position ends clear).
- **Coaching note:** the unload position must be clear before the roll-over. Put the packaging in the
  tote and carry the tote back with both grippers.

**Violation: Seat loaded face up.**

- **Visible cue:** the seat goes into the fixture with the face up, or a leg is set on the face of the
  seat, instead of the seat being turned underside up before it is loaded.
- **SOP rule broken:** Seat target and Step 3.1 (the seat is loaded face down with all four leg sockets
  visible before any leg is fitted).
- **Coaching note:** never fit a leg on the face. Turn the seat over before it goes into the fixture and
  check all four leg sockets.

**Violation: Seat not seated in the fixture.**

- **Visible cue:** assembly starts with a seat corner standing off its corner stop, the seat sitting on
  top of a stop, or the seat rocking in the fixture, or the operator pushes one corner down with a single
  gripper instead of lifting and re-seating the seat.
- **SOP rule broken:** Step 3.3 (all four corners against their corner stops with no gap; re-seat by
  lifting with both grippers).
- **Coaching note:** the fixture is what squares the seat. If a corner is off its stop, lift the seat
  with both grippers and set it down again.

**Violation: Loose part swept instead of picked.**

- **Visible cue:** a gripper sweeps, drags or pushes a loose part across the underside of the seat or off
  the seat into a tray, instead of picking that part up on its own.
- **SOP rule broken:** Step 3.4 (pick any loose part individually and place it in its assigned
  compartment).
- **Coaching note:** pick each loose part up on its own and put it where it belongs. Sweeping scatters
  hardware and scratches the seat.

**Violation: Work done away from the assembly or drive position.**

- **Visible cue:** a leg is fitted at a corner that is not at the assembly position, a brace is fitted on
  a side that is not the working side, a corner is pressed or a bolt driven at a leg that is not at the
  drive position, the operator reaches around the fixture or the stool, or the base is not indexed
  between corners so two legs are worked at one index.
- **SOP rule broken:** Bring the work to the arms, Steps 4.2, 4.4, 5.1, 5.3, 7.1 and 8.1 (work at the
  assembly position and the drive position; index between corners, sides and legs).
- **Coaching note:** index the base one click, do one corner, index again. Do not stretch around the work
  to save an index.

**Violation: Leg or brace left unheld.**

- **Visible cue:** the left gripper releases a leg in its socket, or a brace at its first end, before that
  part's bolt is run down — typically to go and pick a bolt — and the part is free to fall or rotate.
- **SOP rule broken:** Never unheld, Steps 4.2, 4.3, 5.1 and 5.2 (hold until the bolt is run down).
- **Coaching note:** the left gripper stays on the leg or brace while the driver picks and runs down the
  first bolt. Release only once that bolt is in.

**Violation: Two legs moved at once for a brace.**

- **Visible cue:** the operator tries to draw both legs of the working side together with one gripper, or
  sets both brace ends in their slots before either bolt is run down, so the brace or a leg swings free.
- **SOP rule broken:** Steps 5.1 and 5.2 (anchor one brace end first, then move one leg only onto the
  free end).
- **Coaching note:** bolt one end, then swing one leg onto the other end. One gripper cannot control two
  legs.

**Violation: Leg turned the wrong way in its socket.**

- **Visible cue:** a leg is fitted with its brace slots facing outward or facing the diagonal instead of
  facing the two adjacent mounting corners, so a brace cannot reach its slot.
- **SOP rule broken:** Step 4.2 (turn the leg until its two brace slots face the two adjacent mounting
  corners).
- **Coaching note:** aim the brace slots at the neighbouring corners before pressing the leg top home. A
  turned leg has to come off again at Step 5.

**Violation: Debris left under a leg top.**

- **Visible cue:** a leg is fitted over a loose part or a piece of debris, or the leg top visibly rocks in
  its socket instead of sitting flat, and the leg is bolted anyway.
- **SOP rule broken:** Steps 3.4 and 4.2 (clear the underside, and the leg top sits flat in the socket).
- **Coaching note:** if the leg top rocks, lift it and look under it. Never bolt down a rocking leg.

**Violation: Bolt-washer set used with the washer missing.**

- **Visible cue:** a bolt with no washer under its head is picked off the card and driven into a hole,
  instead of the kit being reported at Step 2.3.
- **SOP rule broken:** Steps 2.3 and 4.3 (every bolt carries its washer; a bolt without one means a
  defective kit).
- **Coaching note:** check the card at the count. A bolt with no washer is a kit fault, not something to
  work around.

**Violation: Driven on a bolt that did not draw down.**

- **Visible cue:** a bolt does not pull into its hole on the first turn, or the driver stalls, and the
  operator keeps driving instead of lifting the bolt back out on the magnet and setting it square again.
- **SOP rule broken:** Steps 4.3, 5.1 and 5.2 (confirm the bolt draws down on its first turn; lift it out
  and re-set it if it does not).
- **Coaching note:** one short trigger pull, then look. A bolt that does not draw down is not in its
  thread, and driving it cross-threads the socket.

**Violation: Bolt seated before the level-check.**

- **Visible cue:** a bolt head is driven flat, or the clutch clicks, during Steps 4-7, or the driver is
  taken out of its holder between the end of Step 5 and the start of Step 8.
- **SOP rule broken:** Proud until levelled, Steps 4.3, 5.3 Warning and 8 (bolts are run down to about 2
  mm proud until the level-check passes).
- **Coaching note:** run every bolt down to a visible gap and stop. The play in the joints is what lets
  the feet all reach the plate.

**Violation: Brace end not seated in its slot.**

- **Visible cue:** a brace is bolted with one end sitting on the outside of the brace slot, part way in,
  or with a visible gap between the brace end and the leg.
- **SOP rule broken:** Steps 5.1 and 5.2 (both brace ends sit fully in their slots with no gap at either
  end).
- **Coaching note:** swing the leg until the end drops fully into the slot, then drive. A part-seated
  brace splits at the bolt.

**Violation: Brace ring not closed.**

- **Visible cue:** fewer than four braces are fitted, or a brace is fitted between two diagonal legs
  instead of two adjacent legs, so the ring is not closed.
- **SOP rule broken:** Step 5.3 (four braces forming a closed ring between adjacent legs).
- **Coaching note:** each brace ties two neighbouring legs. Check the ring is closed before the
  roll-over.

**Violation: Rolled over before all 16 bolts are run down.**

- **Visible cue:** the stool is lifted out of the fixture in Step 6 with a leg or brace bolt still missing
  or standing loose in its hole.
- **SOP rule broken:** Step 5.3 Warning (all 16 bolts run down before the roll-over).
- **Coaching note:** count the bolts before the roll-over. A stool rolled on a missing bolt drops a leg.

**Violation: Unsupported roll-over.**

- **Visible cue:** the stool is turned more than 90° in one move, is turned in the air without going
  through the cradle, is released in mid-turn, is dropped, tipped or rolled loose into or out of the
  cradle, or is dragged off the fixture rather than lifted clear.
- **SOP rule broken:** Supported roll-over, Step 6.1-6.3 (lift clear, one 90° into the cradle, release
  only when it is resting, one 90° out onto the stand plate).
- **Coaching note:** two 90° moves with the cradle taking the weight in between. A single 180° turn in
  the air runs the wrist out of range and folds the loose joints.

**Violation: Stool not landed at the drive position.**

- **Visible cue:** the stool is left on the stand plate with no leg at the front corner of the plate, and
  the operator presses corners or drives bolts from that orientation instead of indexing the plate.
- **SOP rule broken:** Step 6.3 (confirm one leg stands at the drive position; index the plate until one
  does).
- **Coaching note:** set the stool down leg-forward. Everything in Steps 7 and 8 happens at the front
  corner of the plate.

**Violation: Level-check skipped or partial.**

- **Visible cue:** the operator goes to Step 8 without pressing all four corners at the drive position,
  or without reading the level in both directions.
- **SOP rule broken:** Steps 7.1 and 7.2 (four corner presses, one per index, then the level read
  corner-to-corner both ways).
- **Coaching note:** all four presses and both level reads, every episode. A single read misses a
  diagonal wobble.

**Violation: Bolts seated on a wobble or off level.**

- **Visible cue:** the driver is used in Step 8 while a foot still lifts on a press or the bubble is off
  centre in either direction.
- **SOP rule broken:** Step 7.3 Warning (all four feet down and the bubble centred in both directions
  before any bolt is seated).
- **Coaching note:** correct the wobble while the bolts are still proud. Seating on a wobble locks the
  wobble in and the stool is scrapped.

**Violation: Shim used before re-seating the joints.**

- **Visible cue:** a shim goes under a foot in Step 7.3 before the operator presses the seat down to pull
  the leg tops and brace ends home.
- **SOP rule broken:** Step 7.3 (press the joints home first, then shim only if the same foot still
  lifts).
- **Coaching note:** re-seat the joints first. Most wobble at this stage is an unseated leg top, not a
  short leg.

**Violation: More than two shims under one leg.**

- **Visible cue:** a third shim is added under the same foot instead of stopping the episode and
  reporting a defective leg.
- **SOP rule broken:** Step 7.3 (no more than two shims under one foot).
- **Coaching note:** stop at two shims and report the leg. A stacked shim pile is not a fix.

**Violation: Wrong tighten sequence.**

- **Visible cue:** the legs are worked around the stool in index order instead of the cross order, the
  two bolts at a leg are taken one to a stop before the other is touched instead of being alternated, or
  the brace bolts are seated before the leg bolts are snug.
- **SOP rule broken:** Step 8.1-8.3 (cross order by indexing the plate; alternate the two bolts at each
  leg; legs snug, then brace bolts, then a final leg pass).
- **Coaching note:** work across the stool, not around it, and alternate the pair at each leg so the seat
  pulls down square.

**Violation: Bolt left proud.**

- **Visible cue:** at the end of Step 8 a bolt head stands above its leg top or brace end with a visible
  gap, or the joint lifts at that bolt.
- **SOP rule broken:** Step 8.4 (all 16 bolt heads seated flat with no gap, checked four at a time round
  the plate).
- **Coaching note:** index the plate right round at the end of Step 8 and check all 16 heads. Seat any
  proud bolt at the drive position.

**Violation: Driver re-triggered after the clutch.**

- **Visible cue:** the driver keeps running, or is triggered again, after the clutch has clicked on a
  bolt; the bolt head sinks into the leg or brace, or the bolt spins without pulling down.
- **SOP rule broken:** Steps 8.2 and 8.3 (drive until the head sits flat and the clutch clicks, then
  stop).
- **Coaching note:** the click is the end of that bolt. Re-triggering after the clutch strips the leg and
  the stool is scrapped.

**Violation: Final level-check skipped.**

- **Visible cue:** the operator moves the stool to the output zone without repeating the corner presses
  after the bolts are seated.
- **SOP rule broken:** Step 8.4 (repeat 7.1 once after every bolt is seated).
- **Coaching note:** one last press round after tightening. Seating the bolts can pull a foot off the
  plate.

**Violation: Finished stool placement off zone.**

- **Visible cue:** in Step 9 the stool is left on the stand plate instead of being carried to the
  back-right output zone, is set down on an edge or a leg rather than on all four feet, is dragged rather
  than carried, or is released at the back-right but ends up noticeably off from the designated zone,
  without falling or requiring further correction.
- **SOP rule broken:** Step 9 (carry the stool back and to the right into the back-right output zone and
  set it down on all four feet).
- **Coaching note:** carry the finished stool to the back-right output zone with both grippers. Do not
  leave it on the plate and aim the release point more precisely; push it deep into the back-right
  corner.

**Violation: Wrong batch placement (batch sessions).**

- **Visible cue:** in Step 9 the new stool is set on top of an earlier stool, is set down touching it, is
  more than 10-20 cm away, or is left seat-down among stools that are seat-up.
- **SOP rule broken:** Step 9 (batch sessions: alongside, all seats up, within 10-20 cm, not touching).
- **Coaching note:** lay the finished stools out in a row, all seats up; do not stack them.

**Violation: Tools, card or bases not returned.**

- **Visible cue:** the driver or the level is left on the seat, on a plate or in the working area instead
  of in its holder, the empty bolt card is left outside the hardware tray, or the fixture or the stand
  plate is left away from its start index at the end of the episode.
- **SOP rule broken:** Steps 5.3, 8.4 and 10 (driver and level to their holders, bolt card to the
  hardware tray, both bases at their start index).
- **Coaching note:** the driver and the level live in their holders and both bases end where they
  started. Anything left out shows up in the next episode's setup check.

**Violation: Wrong arm used for an action.**

- **Visible cue:** any step that specifies the left gripper or the right gripper is performed with the
  opposite gripper, including the driver being taken in the left gripper.
- **SOP rule broken:** any step that specifies a gripper, including Steps 1, 2, 3, 4, 5, 6, 7, 8, 9 and
  10.
- **Coaching note:** operator confusion about left vs right roles. The driver is a right-gripper tool.
  Walk through the SOP step by step with the operator.

**Violation: Re-grip on a pick or grasp.**

- **Visible cue:** the operator closes on a tote handle, a seat corner, a leg, a brace or the driver,
  finds the grip off, opens, and re-grips before lifting more than two times; or the bit is dropped onto
  a bolt head more than twice before the magnet takes it.
- **SOP rule broken:** Steps 1/2.1/3.1/4.1/4.2/4.3/5.1 (grasp securely: the handle, the seat corner, the
  body of a part, the driver grip, or the bolt head under the bit).
- **Coaching note:** approach angle off. Practice the from-above approach so the first grip catches the
  right point.

**Violation: Repeated fiddling with a part or a joint.**

- **Visible cue:** the operator makes many small adjustments (more than about two) to settle a leg, a
  brace, a shim, the seat in the fixture or the level, rather than settling it in one or two corrections.
- **SOP rule broken:** the unload/load/fit/brace/level sub-steps (settle in one or two small
  adjustments).
- **Coaching note:** grip or approach is off, forcing repeated correction. Tighten the approach so each
  part lands close to target.

**Violation: Arms not fully at home position at episode end.**

- **Visible cue:** in the final frame, both arms are close to the home position but not exactly at it
  (gripper not fully open, or arm position visibly off home).
- **SOP rule broken:** Step 10 (return to home position with grippers open).
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
- **Driver fault:** Cause: flat battery, a bit that no longer holds a bolt on the magnet, or a clutch
  that will not release at the station setting. Swap or recharge the driver before the next episode.
- **Debris in the working area:** Cause: something that is not a kit part is on the seat, in the fixture,
  in the cradle or on the stand plate. This is a station setup failure. Reset the station off record; the
  episode is not recorded around it.
- **Fixture, cradle or plate fault:** Cause: an indexing base that will not click into a detent or turns
  under load, a stand plate that will not lock or does not sit level, a loose corner stop, or a cradle
  pad that has come away. Repair before the next episode.
- **Tote over payload:** Cause: a loaded tote heavier than the two-arm payload limit reaches the table.
  Re-pack the kit off record before the next episode.
- **Defective kit:** Cause: a short or extra part, a leg or brace of the wrong length, a bolt with no
  washer, or a bolt that cross-threads and will not lift back out, through no fault of the operator.
  Replace before the next episode.
- **Defective seat or leg:** Cause: a split leg socket, a blocked bolt hole, or a leg that leaves the
  stool wobbling with two shims under it. Replace before the next episode.

## After each episode: repeat or reset

- **Batch sessions (e.g., 5x):** if fewer than the target number are assembled, return to Step 1 with the
  next kit tote. Once the target number are assembled and staged in the output row, reset the workspace
  before the next session.
- Clear the working area and re-run the Setup checklist before the next session.

### After the episode: reset the workspace

This part is not recorded. It is just how you reset the table for the next episode.

- With recording off, move the finished stool(s) from the output zone back to the start zone for the
  next episode's config — back-left (Config L1), left edge (Config L2) or back-right (Config R).
- Back out all 16 bolts from each stool, take off the four braces and the four legs, and pull out any
  shims.
- Stand the 16 bolt-washer sets back in the bolt card head-up, confirm each carries its washer, and seal
  the card in a hardware pouch.
- Load one tote per stool: the four legs, the four braces and the hardware pouch in the bottom, the seat
  face up on top, matching the initial setup state. Confirm the loaded tote is inside the two-arm payload
  limit.
- Return the shims to the shim compartment, empty the rest of the parts tray and the hardware tray, and
  return the driver and the level to their holders at the right edge.
- Check the driver's charge and clutch setting on a test bolt.
- Turn the fixture and the stand plate back to their start index, and confirm the fixture, the cradle and
  the plate are empty and that both bases click at each detent.
- Confirm the table surface is clear of any objects other than the kit tote(s), the fixture, the cradle,
  the stand plate and the two trays.
- Go through the Setup checklist again before starting the next episode.

**Warning:** The table must be clear except for the kit tote(s) in the start zone, the seat fixture at the
center, the roll-over cradle at the front-center, the stand plate at the near-center, the parts tray at
the front-left and the hardware tray at the front-right.

## Annotation subtasks

1. Carry one kit tote from the input area to the unload position with both grippers
2. Unload the legs and braces into the parts tray
3. Open the hardware pouch with both grippers and load the bolt card into the hardware tray
4. Count the parts against the parts list
5. Load the seat face down into the seat fixture and clear the underside
6. Attach the four legs at the assembly position with the driver, indexing the fixture between corners
7. Add the four braces at the assembly position to close the brace ring
8. Roll the stool over through the cradle onto the stand plate
9. Level-check the stool (four corner presses at the drive position, level read both ways)
10. Seat all 16 bolts in the cross sequence at the drive position
11. Move the finished stool to the output area
12. Home the arms
