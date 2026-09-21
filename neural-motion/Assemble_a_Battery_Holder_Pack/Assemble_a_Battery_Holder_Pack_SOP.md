# Assemble a Battery Holder Pack SOP (1x Episode: 4 Cells)

One episode builds one whole pack: four cells seated, both holders clipped in, all four leads landed and
torqued, and one meter check. The table begins with the **carrier** on the **assembly spot**, just right of the
center of the table. The **loading cradle** sits at the center of the table, just left of the carrier, and holds
the two empty **cell holders**: **holder A** in the left cradle slot and **holder B** in the right cradle slot.
A **cell tray** with four numbered **cell wells** sits in the **start zone** for the episode's config (see
below). The **terminal block** runs along the back edge of the carrier, its four terminals numbered **1** at the left to **4** at the right, with the **lead
map** card behind it. Two **test pads** sit at the front-right corner of the carrier. A **torque driver** stands
in the **driver stand** at the back-right, and the **probe fork** hangs in the **probe stand** just in front of
it, wired to the **bench meter** at the back-right corner.

The order never changes: seat all four cells, working **cell 1, 2, 3, 4**; then clip **holder A** and then
**holder B** into the carrier; then push all four **leads** into the terminal block per the **lead map**,
working terminal 1 through 4; then torque all four screws, again 1 through 4; then park the driver and take one
meter reading. No holder is clipped into the carrier until all four cells are seated. No lead goes into a
terminal until both holders are clipped home. No screw is turned until all four leads are in. The meter check is
never done with the torque driver still in the gripper, and the episode does not end until one reading has been
taken and read.

The right gripper does all the work: it seats every cell, clips both holders in, pushes every lead home, takes
and parks the torque driver, turns every screw, and holds the probe fork. The left gripper holds things flat. It
presses the loading cradle down by its left edge through Steps 1 and 2, then moves once, in Step 3, onto the
left edge of the carrier and stays there to the end of the episode. The left gripper never seats a cell, never
picks a holder, a lead, or a tool, and never reaches across the carrier.

The table is set up in one of three ways. Only the cell tray moves; the carrier, the loading cradle with both
holders, the driver stand, the probe stand, and the bench meter are in the same place in all three.

* **Config L:** the cell tray is in the back-left corner.
* **Config M:** the cell tray is at the front-center, just in front of the loading cradle.
* **Config R:** the cell tray is at the front-right.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the cell tray starts at the back-left (**Config L**), the front-center (**Config M**) or
  the front-right (**Config R**). One config per episode, chosen before recording and never changed
  mid-episode.
* **Same-side rule:** the gripper on the cell tray's side takes each cell out of its well — the left gripper
  in Config L and M, the right gripper in Config R. No arm reaches across the table.
* **Hand-over rule:** in Config L and M the left gripper never seats a cell and has to go back to holding the
  cradle, so it **hands each cell over** to the right gripper above the loading cradle: the left gripper holds
  the cell still, the right gripper closes on it across its middle, and only then does the left gripper open
  and lift clear. The right gripper seats it. Nothing is handed over in Config R.
* **Fixed roles:** everything else is the same in all three configs — the right gripper seats every cell,
  clips both holders, pushes every lead home, torques every screw, and holds the probe fork; the left gripper
  holds the cradle and then the carrier; the carrier, the cradle, the tools, and the meter never move.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the carrier with its two holder bays, the terminal block and
   the lead map, the test pads, the loading cradle with both holders, the cell tray in its start zone, the
   driver stand, the probe stand, and the face of the bench meter.
3. The carrier is visible from above and from the front, so all four terminal screws, all four terminal holes,
   the holder clips, and the polarity marks in every cell bay can be seen.
4. The face of the bench meter is readable in the recording, without any arm standing in front of it.
5. Both arms are at home with grippers open.
6. The table is bare apart from the carrier, the loading cradle with both holders, the cell tray, the driver
   stand, the probe stand, the bench meter, and robot hardware.
7. The right arm reaches cell well 1 and cell well 4 (Config R), both cradle slots, both holder bays, terminal
   1, terminal 4, the test pads, the driver stand, and the probe stand without stretching. The left arm reaches
   the left edge of the loading cradle, the left edge of the carrier, and cell well 1 and cell well 4 (Config L
   and M) without stretching.

### Materials checklist

1. One **carrier** lies on the **assembly spot**, just right of the center of the table, **square** to the front
   edge and flat on the table.
2. The carrier has two empty **holder bays**: **bay A** on the left and **bay B** on the right. Each bay has two
   **clips**, one on each long side, and each bay is labeled with its letter.
3. The **terminal block** is fixed along the back edge of the carrier. Its four terminals are numbered **1** at
   the left to **4** at the right, and the numbers are printed on the block and readable from above.
4. Every terminal **screw** starts **open**: backed off far enough that a **ferrule** slides into the hole below
   it without being forced.
5. Every terminal **hole** is empty and clear.
6. The **lead map** card is fixed at the back of the carrier, behind the terminal block, and reads: terminal 1
   holder A red, terminal 2 holder A black, terminal 3 holder B red, terminal 4 holder B black.
7. Two bare **test pads** sit at the front-right corner of the carrier, one marked **+** and one marked **−**,
   set apart to match the two tips of the probe fork.
8. The **loading cradle** sits at the center of the table, just left of the carrier, flat and square to the
   front edge. It has two slots: **cradle slot A** on the left and **cradle slot B** on the right. Each slot
   holds one holder snugly, bays facing up.
9. **Holder A** sits in cradle slot A and **holder B** in cradle slot B. Both are empty. Each holder has two
   **cell bays**, numbered **1** at the left and **2** at the right, and each bay is marked **+** at one end and
   **−** at the other. In both holders, bay 1 is marked **+** at its right end and bay 2 is marked **+** at its
   left end.
10. Each holder has one **red lead** and one **black lead**, each ending in a **ferrule**. Both leads of each
    holder lie flat on the table to the right of the cradle, straight, not crossing and not lying over the cell
    bays.
11. The **cell tray** sits in the start zone for the episode's config, with four **cell wells**, numbered 1 at
    the left to 4 at the right, one cell per well. Every cell is the same size and fresh. The cells lie the way
    they go in: in wells **1 and 3** the **button end** points **right**, and in wells **2 and 4** the **button
    end** points **left**.
    - **Config L:** back-left corner, clear of the left edge of the cradle
    - **Config M:** front-center, just in front of the loading cradle
    - **Config R:** front-right
12. One **torque driver** stands in the **driver stand** at the back-right, handle up, blade down, matching the
    terminal screw slots. It is preset for these terminals and **clicks** at torque.
13. The **probe fork** hangs in the **probe stand** just in front of the driver stand, handle up, both tips
    down, and its cable reaches the test pads without pulling the carrier.
14. The **bench meter** sits at the back-right corner, switched on, reading volts, with its display facing the
    environment camera. The **meter card** beside it prints the **pass band** for a good pack: **5.6 to 6.6
    volts**.
15. Keep the left side of the table clear apart from the cell tray in Config L. The left gripper comes in from
    there onto the cradle and then onto the carrier.
16. Before collection, confirm by hand that:
    - a cell presses into a bay against the spring and stays under the clip;
    - a loaded holder pushes into its bay until both clips snap over it;
    - each ferrule slides into its terminal hole without force;
    - a torqued screw holds its lead against a light pull;
    - both probe fork tips touch both test pads at once and the meter reads inside the pass band.

### Workspace layout

- **Assembly spot:** just right of the center of the table — the carrier stays here all episode
- **Back edge of the carrier:** the terminal block, terminals 1 to 4 left to right, lead map card behind it
- **Front-right corner of the carrier:** the two test pads
- **Center of the table:** the loading cradle, cradle slot A on the left and cradle slot B on the right
- **Cell tray start zone:** the cell tray with four cells — back-left (Config L), front-center in front of the
  cradle (Config M), or front-right (Config R)
- **Back-right tool zone:** the driver stand, the probe stand in front of it, the bench meter at the corner
- **Left side:** kept clear apart from the cell tray in Config L, so the left gripper can come in onto the
  cradle and then onto the carrier

### Arm assignments

- **Left gripper:** presses the loading cradle flat by its left edge through Steps 1 and 2, then moves once onto
  the left edge of the carrier in Step 3 and holds it there to the end of the episode. In Config L and M it
  also fetches each cell from the tray and hands it to the right gripper above the cradle.
- **Right gripper:** picks every cell (Config R) or takes it from the left gripper above the cradle (Config L
  and M) and seats it, lifts both holders and clips them into the carrier, pushes
  every lead home, takes and parks the torque driver, turns every screw, and holds the probe fork for the meter
  check.

## Vocabulary

- **Assembly spot:** the place on the table, just right of center, where the carrier sits. The carrier stays
  here for the whole episode.
- **Square:** the front edge of a part lines up with the front edge of the table, so neither end of the part
  sits nearer the front.
- **Carrier:** the flat plate the two holders clip into. It carries the terminal block, the lead map, and the
  test pads, and it is never lifted.
- **Holder bay:** one of the two openings in the carrier that a holder clips into. **Bay A** is on the left,
  **bay B** on the right.
- **Clips:** the two small tabs on the long sides of a holder bay that snap over a holder and keep it down.
- **Clipped home:** the holder sits flat in its bay, both clips are over its edges, and it does not lift or rock
  when the right gripper lets go.
- **Cell holder:** one plastic block that takes two cells. **Holder A** goes in bay A, **holder B** in bay B.
- **Cell bay:** one place inside a holder that takes one cell. Each holder has bay 1 on the left and bay 2 on
  the right.
- **Polarity marks:** the **+** and **−** printed at the two ends of each cell bay.
- **Spring end:** the end of a cell bay with the coiled metal spring in it. It is always the end marked **−**.
- **Button end:** the end of a cell with the small raised metal button. It is the **+** end of the cell.
- **Flat end:** the other end of a cell, with no button. It is the **−** end of the cell.
- **Seated:** the cell lies down inside its bay, its flat end presses the spring, its button end touches the
  metal at the **+** end, it sits under the bay clip, and it does not rock or stand proud when the right gripper
  lets go.
- **Cell tray:** the holder with four numbered wells, one cell per well.
- **Start zone:** where the cell tray sits at the start of the episode — back-left (**Config L**), front-center
  in front of the cradle (**Config M**), or front-right (**Config R**). One per episode, chosen before recording
  and never changed mid-episode.
- **Hand over:** the left gripper holds a cell still above the loading cradle, the right gripper closes on it
  across its middle, and only then does the left gripper open and lift clear. Config L and M only, because the
  right gripper does all the seating and the left gripper goes back to holding the cradle.
- **Cell well:** one numbered slot in the cell tray. Cell 1 goes in holder A bay 1, cell 2 in holder A bay 2,
  cell 3 in holder B bay 1, cell 4 in holder B bay 2.
- **Loading cradle:** the fixture at the center of the table that holds the two holders while their cells go in.
- **Cradle slot:** one of the two slots in the loading cradle. Slot A on the left holds holder A, slot B on the
  right holds holder B.
- **Lead:** one wire coming out of a holder. Each holder has a red lead and a black lead.
- **Insulation:** the colored plastic covering along a lead.
- **Ferrule:** the metal sleeve crimped on the bare end of a lead. It is the end that goes into a terminal.
- **Terminal block:** the row of four screw terminals along the back edge of the carrier.
- **Terminal:** one wiring position on the block. Each one has its own number, screw, and hole.
- **Hole:** the opening in the front face of a terminal that a ferrule goes into.
- **Fully home:** the ferrule is all the way inside the hole and the insulation behind it touches the front face
  of the terminal, so no bare metal shows outside the hole.
- **Lead map:** the card behind the terminal block that says which lead goes in which terminal.
- **Screw slot:** the straight groove across the head of a terminal screw that the driver blade sits in.
- **Blade seated:** the driver blade sits down in the screw slot, in line with it, and does not skate out when
  the screw is turned.
- **Torque driver:** the screwdriver used on the terminal screws. It is preset and clicks at the right
  tightness.
- **Click:** the moment the torque driver head breaks over and gives way. It means that screw is done.
- **Driver stand:** the holder at the back-right the torque driver stands in when it is not in the right
  gripper.
- **Probe fork:** the one-handled tool with two meter tips set apart to match the two test pads. One grip puts
  both tips on both pads.
- **Probe stand:** the holder just in front of the driver stand that the probe fork hangs in.
- **Test pads:** the two bare metal pads at the front-right corner of the carrier, one marked **+** and one
  marked **−**.
- **Bench meter:** the meter at the back-right corner that the probe fork is wired to. Its display faces the
  camera.
- **Pass band:** the range printed on the meter card, **5.6 to 6.6 volts**, that a good pack reads.
- **Reading:** the number shown on the bench meter display while both probe fork tips are held on the test pads.

## Steps

Run Steps 1–6 in order on the one pack, then end the episode with Step 7.

Only Steps 1 and 2 depend on where the cell tray is: in Config R the **right gripper** picks each cell from the
front-right; in Config L and M the **left gripper** lifts off the cradle, fetches each cell, **hands it over**
to the right gripper above the cradle, and goes back onto the cradle before the cell is seated. Every other
line, and all of Steps 3–7, is the same in all three configs.

### Step 1: Hold the loading cradle down

**Goal:** the loading cradle is pinned flat at the center of the table and cannot slide while cells go in.

- With the **left gripper**, press down on the **left edge** of the loading cradle and hold it against the
  table.
- Keep the **left gripper** there through Step 2. **IF Config L or M:** it lifts off only to fetch each cell in
  2.1 and is back on the cradle before the cell is seated.

**Check:** the cradle is flat on the table, **square** to the front edge, and does not slide when the left
gripper presses. Both holders sit in their slots with their bays facing up. If the cradle is crooked, straighten
it with the **left gripper** first, then press it down.

**Expected state:** the cradle is held, both holders are empty, all four cells are in the tray, and the leads
lie flat to the right of the cradle.

### Step 2: Seat the four cells

**Goal:** all four cells are seated the right way round, with no holder moved out of the cradle yet.

- With the **left gripper**, keep pressing the loading cradle down.
- Work **cell 1 first, then 2, 3, 4**. Do one cell at a time.
- Cell 1 goes in **holder A bay 1**, cell 2 in **holder A bay 2**, cell 3 in **holder B bay 1**, cell 4 in
  **holder B bay 2**.
- Carry each cell in one go, straight from its well to its bay — **IF Config L or M**, through one hand-over
  above the cradle. Do not set a cell down on the cradle or the table on the way, and do not carry two cells at
  once.
- Never turn a cell end-for-end in either gripper. The cells lie in the tray the way they go in.

#### 2.1 Pick the cell

- **IF the cell tray is at the back-left (Config L):** the **left gripper** lifts off the cradle, pinches the
  cell in its well near one end, lifts it straight up out of the well, carries it level to above the loading
  cradle, and holds it still. The **right gripper** closes on the cell across its middle; the **left gripper**
  opens, lifts clear, and goes back onto the left edge of the cradle.
- **IF the cell tray is at the front-center (Config M):** the **left gripper** lifts off the cradle, pinches
  the cell in its well near one end, lifts it straight up out of the well, carries it level back to above the
  loading cradle, and holds it still. The **right gripper** closes on the cell across its middle; the **left
  gripper** opens, lifts clear, and goes back onto the left edge of the cradle.
- **IF the cell tray is at the front-right (Config R):** with the **right gripper**, pinch the cell in **cell
  well 1** across its middle, and lift it straight up out of the well.

Then, in all three:

- Keep the cell level and keep the **button end** pointing the same way it pointed in the well.

#### 2.2 Seat the cell

- With the **right gripper**, bring the cell over its bay and line up its **button end** with the end of the bay
  marked **+**.
- With the **right gripper**, put the **flat end** of the cell against the **spring end** of the bay first, and
  push along the cell to press the spring in.
- With the spring still pressed, lower the **button end** into the bay with the **right gripper** and press the
  cell down until it sits under the bay clip.
- Press straight down only. The **right gripper** never levers a cell in sideways and never pries against the
  holder.
- If the cell will not go down, lift it straight out with the **right gripper**, line it up again, and press it
  in again.
- Open the **right gripper** and let go. The cell must stay down and must not rock.
- Go back to 2.1 for the next cell.

**Check:** after each cell, the button end sits at the end marked **+**, the cell lies flat under the clip, and
it does not rock or spring back up when the right gripper lets go. If the cell is the wrong way round, lift it
straight out with the **right gripper** and seat it again the right way round. If it rocks or stands proud,
press it down again with the **right gripper**.

**Expected state:** all four cells are **seated**, every button end is at a **+** mark, the cell tray is empty,
both holders are still in the cradle, and the leads still lie flat to the right of the cradle.

### Step 3: Clip both holders into the carrier

**Goal:** holder A and then holder B are clipped home in the carrier, and the left gripper is on the carrier for
the rest of the episode.

- Clip **holder A first, then holder B**.
- The **right gripper** always holds a holder by its plastic body, never by a lead.

#### 3.1 Move the support to the carrier

- Open the **left gripper** and lift it off the loading cradle.
- With the **left gripper**, press down on the **left edge** of the carrier and hold it against the table.
- Keep the **left gripper** there through Steps 4, 5, and 6.

**Check:** the carrier is flat on the table and **square** to the front edge, and it does not slide when the left
gripper presses. If the carrier is crooked, straighten it with the **left gripper** first, then press it down.

#### 3.2 Clip each holder in

- With the **right gripper**, pinch **holder A** by its plastic body and lift it straight up out of cradle slot
  A.
- With the **right gripper**, bring it over **bay A**, hold it level, and line up its long sides with the two
  **clips**.
- With the **right gripper**, press the holder straight down into the bay until both clips snap over its edges.
- Open the **right gripper** and let go. The holder must stay down.
- Lay the holder's two leads forward with the **right gripper** so they lie flat on the carrier and do not cross
  each other.
- Do the same with the **right gripper** for **holder B** into **bay B**.

**Check:** each holder is **clipped home** — flat in its bay, both clips over its edges, and it does not lift or
rock when the right gripper lets go. All four cells are still seated. If a holder rocks or a clip has not gone
over, press it down again with the **right gripper**. If a cell popped up while the holder went in, lift the
cell straight out with the **right gripper** and seat it again.

**Expected state:** both holders are clipped home in the carrier, the loading cradle is empty, all four leads
lie flat on the carrier without crossing, and every terminal screw is still open.

### Step 4: Route the four leads to the terminal block

**Goal:** all four ferrules are fully home in the right terminals, with no screw turned yet.

- With the **left gripper**, keep pressing the carrier down.
- Work **terminal 1 first, then 2, 3, 4**. Do one lead at a time.
- Turn no screw in this step. The **right gripper** leaves the **torque driver** standing in its stand.
- Read the **lead map** for the terminal being wired, then pick that lead.
- With the **right gripper**, pinch the lead by its **insulation**, a little way back from the **ferrule**.
  Never pinch the ferrule itself.
- With the **right gripper**, bring the ferrule to the **hole** in the front face of that terminal and line it
  up with the hole.
- With the **right gripper**, push the lead straight in until the insulation behind the ferrule touches the
  front face of the terminal.
- Push straight in only. The **right gripper** never twists a lead and never forces it in at an angle.
- If the ferrule will not go in, pull the lead back out with the **right gripper**, line it up again, and push
  it straight in again.
- Open the **right gripper** and let go. The lead must stay in the hole.

**Check:** after each lead, no bare metal shows outside the hole, the insulation touches the terminal face, the
lead matches what the lead map gives for that terminal number, and the lead stays in when the right gripper lets
go. If bare metal shows, push the lead in further with the **right gripper**. If the lead falls out, pick it up
with the **right gripper** and push it home again. If the wrong lead went in, pull it out with the **right
gripper** and put the right one in.

**Expected state:** all four terminals hold the lead the lead map calls for, every lead is **fully home**, all
four screws are still open, and the torque driver is still in its stand.

### Step 5: Torque the four terminal screws

**Goal:** all four screws are turned with the torque driver until it clicks once, in terminal order.

- With the **left gripper**, keep pressing the carrier down.
- Torque **terminal 1 first, then 2, 3, 4**. Do not skip a terminal and do not come back out of order.
- The **right gripper** turns screws with the **torque driver** only, never with its own tip.

#### 5.1 Take the driver

- With the **right gripper**, pinch the **torque driver** by its handle and lift it straight up out of the
  **driver stand**.
- Hold the driver in the **right gripper** blade-down, in line with the screws.

#### 5.2 Torque each screw

- With the **right gripper**, set the **blade** down in the **screw slot** of that terminal's screw, in line
  with the slot.
- With the **right gripper**, turn the driver **clockwise** a quarter turn.
- With the **right gripper**, lift the blade clear, set it back down in the slot, and turn another quarter turn.
- Repeat these quarter turns with the **right gripper** until the driver **clicks**.
- Stop that screw at the first click. Never turn a screw again after it has clicked, and never turn
  counter-clockwise.
- If the blade skates out of the slot, lift it clear with the **right gripper**, set it back down in the slot,
  and turn again.
- Move the **right gripper** on to the next terminal's screw.

#### 5.3 Park the driver

- Once all four screws have clicked, put the **torque driver** back in the **driver stand** with the **right
  gripper**, handle up, and let go.

**Check:** all four screws clicked, one click each, and every lead's insulation still touches its terminal face.
The driver is standing in its stand and the right gripper is empty. If a lead pulled out of a terminal while its
screw was turned, back that screw off with the driver in the **right gripper**, push the lead home again with
the **right gripper**, and torque that screw again to a click.

**Expected state:** all four screws are torqued, all four leads are fully home, the driver is in its stand, and
the right gripper is empty.

### Step 6: Meter-check the pack

**Goal:** one reading is taken across the test pads with the probe fork and read off the bench meter.

- With the **left gripper**, keep pressing the carrier down.
- The **right gripper** must be empty of the driver before the probe fork is picked up.

#### 6.1 Take the reading

- With the **right gripper**, pinch the **probe fork** by its handle and lift it straight up out of the **probe
  stand**.
- With the **right gripper**, bring the fork over the two **test pads** and line up its two tips with the two
  pads.
- With the **right gripper**, press both tips straight down onto both pads at once and hold them there for **2
  seconds**.
- Keep the fork still while it is down. The **right gripper** never drags the tips across the pads, never
  presses with one tip only, and never puts a tip on the carrier away from a pad.
- Read the number on the **bench meter** while the tips are down, then lift the fork straight up with the
  **right gripper**.

#### 6.2 Judge the reading and park the fork

- If the reading is inside the **pass band** on the meter card, put the **probe fork** back in the **probe
  stand** with the **right gripper**, handle up, and go to Step 7.
- If the reading is outside the pass band, or the display shows a minus sign, take the reading one more time:
  repeat 6.1 once with the **right gripper**.
- If the second reading is good, park the fork with the **right gripper** and go to Step 7.
- If the second reading is still outside the band or still shows a minus sign, park the fork with the **right
  gripper**, go to Step 7, and log the pack for a station check. Do not take the pack apart inside the episode.

**Check:** both tips touched both pads at once, the fork was held down for 2 seconds, a number was on the meter
display, and the fork is back in its stand. If the display showed nothing while the tips were down, that counts
as a bad reading — repeat 6.1 once with the **right gripper**.

**Expected state:** one reading has been taken and read, at most one repeat was done, the probe fork is standing
in its stand, and the right gripper is empty.

### Step 7: End the episode

**Goal:** recording ends with the pack built, torqued, and metered.

1. Confirm the end state:
   - all four cells are seated with every button end at a **+** mark;
   - both holders are clipped home in bay A and bay B;
   - all four leads are fully home in the terminals the lead map calls for;
   - all four screws have been torqued to a click;
   - a reading was taken, and any second reading was taken;
   - the cell tray and the loading cradle are empty;
   - the torque driver is in its stand and the probe fork is in its stand;
   - the carrier is still **square** on the assembly spot.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

### After each episode

1. Back all four terminal screws off with the driver until each ferrule slides out freely, then pull the four
   leads out of the block.
2. Press the clips clear and lift both holders out of the carrier. Lift the four cells out of the holders.
3. Put each cell back in its own well: cell 1 in well 1, cell 2 in well 2, cell 3 in well 3, cell 4 in well 4,
   button end pointing right in wells 1 and 3 and left in wells 2 and 4. Replace any cell that has been used for
   more than the agreed number of episodes. Set the tray in the start zone for the next episode's config —
   back-left (Config L), front-center in front of the cradle (Config M), or front-right (Config R).
4. Put holder A in cradle slot A and holder B in cradle slot B, bays facing up, and lay both pairs of leads flat
   to the right of the cradle, straight and not crossing.
5. Back each terminal screw off until a ferrule slides in without being forced. Brush dust off the test pads.
6. Set the carrier **square** on the assembly spot, flat against the table, and set the cradle square beside it.
   Stand the torque driver in its stand, handle up, and hang the probe fork in its stand.
7. Run both Setup checklists before the next episode.

### At the end of the session

1. Inspect the parts. Replace a lead whose ferrule is crushed, loose, or broken off. Replace a holder if a cell
   no longer stays under its clip, a spring is flattened, or the plastic is cracked. Replace the carrier if a
   bay clip no longer snaps over a holder. Replace the torque driver if its blade is rounded or it no longer
   clicks. Replace the probe fork if a tip is bent or its cable is broken.
2. Check the bench meter reads a known good pack inside the pass band. If it does not, flag the meter and stop
   collection on this station.
3. Leave the carrier square on the assembly spot with all four screws open and both bays empty, both holders in
   the cradle, all four cells in their wells, the driver in its stand, and the probe fork in its stand.

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
separately. Retain the episode in training data with its violation tags. Do not delete a recorded episode solely
because it contains a violation.

### Violations

**Note on the start position:** the violations below were written for Config R (cell tray at the front-right,
the right gripper picks every cell). The pickup and arm-role cues will be rewritten later to cover all three
start positions; they are left as they are for now. Until then, anything that does not match the episode's
config goes under **Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the cell tray is not in the
  start zone for the config; a gripper reaches across the table for a cell; in Config L or M the left gripper
  seats a cell itself, or the right gripper reaches to the tray, instead of a hand-over above the cradle; or
  the wrong IF line is followed.
- **SOP rule broken:** the start position, the same-side rule, and the hand-over rule (the right gripper picks
  each cell from the front-right in Config R; in Config L and M the left gripper fetches it and hands it over
  to the right gripper above the cradle; no arm reaches across the table; the IF line followed is the one for
  the config on the table).
- **Coaching note:** look where the cell tray is before the first reach, then follow that config's IF lines
  through Steps 1 and 2.

**Violation: Loading cradle not held**
- **Visible cue:** the left gripper is off the left edge of the loading cradle while the right gripper seats a
  cell, and the cradle or a holder slides, lifts, or is chased across the table; or the left gripper leaves the
  cradle before all four cells are seated.
- **SOP rule broken:** Step 1 (the left gripper presses the loading cradle down by its left edge and holds it
  there through Step 2).
- **Coaching note:** left gripper on the cradle first, and leave it there until the fourth cell is in.

**Violation: Carrier not held**
- **Visible cue:** the left gripper is off the left edge of the carrier while the right gripper clips a holder,
  pushes a lead, turns a screw, or presses the probe fork, and the carrier slides or lifts; or the left gripper
  never moves onto the carrier at all.
- **SOP rule broken:** Step 3.1 (the left gripper moves onto the left edge of the carrier and holds it there
  through Steps 4, 5, and 6).
- **Coaching note:** one move only — cradle, then carrier. Nothing gets clipped or screwed on a loose carrier.

**Violation: Cradle or carrier moved off its spot**
- **Visible cue:** either gripper lifts, turns, or drags the carrier or the loading cradle, or one of them ends
  the episode out of square with the front edge.
- **SOP rule broken:** Steps 1–6 (the carrier stays flat and square on the assembly spot and the cradle stays
  flat and square at the center of the table for the whole episode; neither is ever lifted).
- **Coaching note:** bring the cell, the holder, and the tool to the fixture; never move the fixture to them.

**Violation: Cells taken out of order or from the wrong well**
- **Visible cue:** the right gripper takes the cells in some order other than well 1, 2, 3, 4, or puts a cell in
  a bay other than the one its well number calls for.
- **SOP rule broken:** Step 2 (work cell 1 first, then 2, 3, 4 — cell 1 in holder A bay 1, cell 2 in holder A
  bay 2, cell 3 in holder B bay 1, cell 4 in holder B bay 2).
- **Coaching note:** well number tells you the bay. Say the number before you pick.

**Violation: Cell turned end-for-end or seated backwards**
- **Visible cue:** the right gripper turns a cell around in the air between the well and the bay, or a cell ends
  up with its button end at the **−** mark, and the episode moves on.
- **SOP rule broken:** Step 2 (the cells lie in the tray the way they go in; never turn a cell end-for-end, and
  line the button end up with the end of the bay marked **+**).
- **Coaching note:** the tray already has them the right way round. Lift, carry level, press down.

**Violation: Cell not seated**
- **Visible cue:** a cell rocks, stands proud of the holder, sits on top of the clip, or springs back up when
  the right gripper lets go, and the episode moves on.
- **SOP rule broken:** Step 2 (press the cell down until it sits under the bay clip; let go only once it stays
  down and does not rock).
- **Coaching note:** let go and look at every cell. A cell that rocks is not in.

**Violation: Cell forced or pried into the bay**
- **Visible cue:** the right gripper levers a cell in sideways, pries against the holder, or keeps pushing a
  cell that will not go down, instead of lifting it out and lining it up again.
- **SOP rule broken:** Step 2 (flat end onto the spring first, then press the button end straight down; if it
  will not go down, lift it straight out and line it up again).
- **Coaching note:** spring first, then straight down. If it fights you, take it out and start that cell again.

**Violation: Cell mishandled on the way in**
- **Visible cue:** the right gripper carries two cells at once, sets a cell down on the cradle or the table on
  the way, or drops a cell into the bay from above instead of pressing it in.
- **SOP rule broken:** Step 2 (carry each cell in one go, straight from its well to its bay, one at a time).
- **Coaching note:** one cell, one carry, one press.

**Violation: Holder clipped into the wrong bay or out of order**
- **Visible cue:** the right gripper puts holder A into bay B or holder B into bay A, or clips holder B in
  before holder A.
- **SOP rule broken:** Step 3 (clip holder A into bay A first, then holder B into bay B).
- **Coaching note:** A into A, B into B, in that order. The letters are on the bays.

**Violation: Holder not clipped home**
- **Visible cue:** a holder sits high in its bay, rocks, has a clip that never went over its edge, or lifts when
  the right gripper lets go, and the episode moves on.
- **SOP rule broken:** Step 3.2 (press the holder straight down until both clips snap over its edges, and let go
  only once it stays down).
- **Coaching note:** both clips over, then let go and check it does not rock.

**Violation: Holder picked up by its leads**
- **Visible cue:** the right gripper lifts, drags, or swings a holder by a lead instead of pinching its plastic
  body, or leaves the leads crossing or lying over the cells after clipping.
- **SOP rule broken:** Step 3.2 (hold a holder by its plastic body, never by a lead, and lay its two leads flat
  on the carrier without crossing).
- **Coaching note:** body only. A lead is not a handle — pulling it loosens the joint you have not made yet.

**Violation: Lead in the wrong terminal or a terminal left empty**
- **Visible cue:** the right gripper pushes a lead into a terminal the lead map gives to a different lead, or a
  terminal has no lead in it when the torquing starts or when the episode ends.
- **SOP rule broken:** Step 4 (read the lead map for the terminal being wired and land that lead; all four
  terminals hold their lead before any screw is turned).
- **Coaching note:** map first, lead second. Count four leads in four terminals before you pick up the driver.

**Violation: Lead not fully home**
- **Visible cue:** bare metal shows outside a terminal hole, the insulation stands off the front face, or the
  lead falls out when the right gripper lets go, and the episode moves on.
- **SOP rule broken:** Step 4 (push the lead straight in until the insulation touches the front face, with no
  bare metal showing, and let go only once it stays in).
- **Coaching note:** insulation against the face, no metal showing. Let go and look before the next lead.

**Violation: Lead forced or twisted into the terminal**
- **Visible cue:** the right gripper pushes a lead in at an angle, twists it while pushing, pinches the ferrule
  itself, or forces a ferrule that will not enter.
- **SOP rule broken:** Step 4 (hold the lead by its insulation and push straight in only; if the ferrule will
  not go in, pull it out, line it up, and push it straight in again).
- **Coaching note:** insulation grip, straight push. If it fights you, back it out and line it up again.

**Violation: Torque driver not used or not parked**
- **Visible cue:** a screw is turned with the gripper tip instead of the torque driver, or the driver is still in
  the right gripper during the meter check, or it is left lying on the carrier or the table.
- **SOP rule broken:** Steps 5.1–5.3 and 6 (turn screws with the torque driver only, park it in the driver stand
  once all four screws have clicked, and pick up the probe fork with an empty gripper).
- **Coaching note:** driver for screws, stand for the driver, empty gripper for the meter.

**Violation: Screw not torqued to the click**
- **Visible cue:** the right gripper moves on to the next screw, parks the driver, or the episode ends with a
  screw that was never turned or was turned without the driver ever clicking.
- **SOP rule broken:** Step 5.2 (turn each screw clockwise in quarter turns until the driver clicks) and Step 5
  (torque terminal 1 first, then 2, 3, 4, skipping none).
- **Coaching note:** four screws, four clicks. Count the clicks out loud.

**Violation: Screw turned the wrong way or forced past the click**
- **Visible cue:** the right gripper turns a screw counter-clockwise, turns more than a quarter turn in one
  grip, or keeps turning a screw after the driver has clicked.
- **SOP rule broken:** Step 5.2 (clockwise, a quarter turn per grip, and stop that screw at the first click).
- **Coaching note:** small bites, clockwise, stop at the click. Past the click you are only breaking things.

**Violation: Driver blade not seated**
- **Visible cue:** the right gripper holds the blade across the screw head instead of down in the slot, lets it
  skate out of the slot while turning, or pries it against the terminal block, and turning goes on anyway.
- **SOP rule broken:** Step 5.2 (set the blade down in the screw slot in line with it; if it skates out, lift it
  clear, set it back in the slot, and turn again).
- **Coaching note:** blade down in the slot, in line, before you turn.

**Violation: Meter check skipped**
- **Visible cue:** the episode ends without the right gripper ever taking the probe fork out of its stand, or
  with the tips never touching the test pads.
- **SOP rule broken:** Step 6 (take one reading across the test pads with the probe fork before the episode
  ends).
- **Coaching note:** every pack gets metered. No reading, no end.

**Violation: Meter check done the wrong way**
- **Visible cue:** the right gripper presses with one tip only, puts a tip on the carrier away from a pad, drags
  the tips across the pads, lifts the fork before 2 seconds are up, blocks the meter display with an arm, or
  leaves the fork lying on the table instead of back in its stand.
- **SOP rule broken:** Step 6.1 (press both tips onto both pads at once, hold still for 2 seconds, then lift
  straight up) and Step 6.2 (put the probe fork back in the probe stand).
- **Coaching note:** both tips, both pads, still for two, then straight up and back in the stand.

**Violation: Failed reading not retried and logged**
- **Visible cue:** the reading is outside the pass band, shows a minus sign, or shows nothing, and the episode
  moves straight to the ending with no second reading; or the second reading is bad and the right gripper starts
  pulling the pack apart instead of parking the fork.
- **SOP rule broken:** Step 6.2 (on a bad reading, repeat 6.1 once; if the second reading is still bad, park the
  fork, go to Step 7, and log the pack for a station check without taking it apart).
- **Coaching note:** one retry, then park and log. The pack is not reworked inside the episode.

**Violation: Work done out of order**
- **Visible cue:** the phases run out of sequence — the right gripper clips a holder into the carrier before all
  four cells are seated, pushes a lead into a terminal before both holders are clipped home, takes the driver
  out before all four leads are in, or takes the meter reading before every screw has clicked.
- **SOP rule broken:** Steps 2–6 (seat all four cells, clip both holders, land all four leads, torque all four
  screws, then meter-check, in that order).
- **Coaching note:** finish the phase before you start the next one. Say the phase name before you move.

**Violation: Wrong arm used**
- **Visible cue:** an action assigned to one gripper is done by the other, including the left gripper picking or
  seating a cell, lifting a holder, pushing a lead, holding the driver or the probe fork, or the right gripper
  holding down the cradle or the carrier.
- **SOP rule broken:** Steps 1–6 (the right gripper seats, clips, routes, torques, and meters; the left gripper
  holds the cradle and then the carrier).
- **Coaching note:** right gripper does the work, left gripper holds. It does not swap.

**Violation: Part dropped or knocked off its spot**
- **Visible cue:** either gripper drops a cell, a holder, the torque driver, or the probe fork on the carrier,
  the table, or the floor, or tips, pushes, or spills the cell tray, the loading cradle, the driver stand, or
  the probe stand off its spot.
- **SOP rule broken:** Steps 2–6 (keep the cells, the holders, the tools, and every stand and tray on their
  spots through the whole episode).
- **Coaching note:** work slower and lower over the table, and keep each carry short.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before the pack and the reading are confirmed, an arm is not home, a gripper
  is closed, or an arm does something else after homing.
- **SOP rule broken:** Step 7 (confirm the end state, return both arms home with grippers open as their final
  action, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than tagging
them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- A cell arrives flat or dead, so a correctly built pack cannot read inside the pass band.
- A holder spring is flattened or a bay clip is broken before the episode, so a correctly pressed cell will not
  stay seated.
- A carrier bay clip is broken, so a correctly pressed holder will not stay clipped home.
- A ferrule arrives crushed or already broken off its lead, so it cannot go fully home.
- A terminal screw's thread is stripped, so the driver never reaches a click.
- The torque driver stops clicking, or the bench meter reads nothing on a known good pack.
- The probe fork cable is broken, so both tips on both pads give no reading.

## Annotation subtasks (from SOP)

1. Press the loading cradle flat and hold it with the left gripper
2. Pick a cell from its well with the gripper on the tray's side
3. In Config L and M, hand the cell from the left gripper to the right gripper above the cradle and put the
   left gripper back on the cradle
4. Seat the cell flat end onto the spring, then press the button end down
5. Repeat the pick and seat for all four cells
6. Move the left gripper from the cradle onto the carrier and hold it there
7. Lift holder A from the cradle and clip it into bay A
8. Lift holder B from the cradle and clip it into bay B
9. Push each lead fully home into the terminal the lead map calls for, terminal 1 through 4
10. Take the torque driver from the stand
11. Turn each terminal screw in quarter turns until the driver clicks, terminal 1 through 4
12. Park the torque driver back in the stand
13. Take the probe fork and hold both tips on the test pads for two seconds
14. Read the meter and repeat the reading once if it is bad
15. Park the probe fork back in the stand
16. Confirm the end state, return both arms home, and end the episode
