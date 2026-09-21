# Populate a Through-Hole Board SOP (1x Episode: 10 Components)

One episode populates all ten positions on one board. The table begins with the **board frame** on the
assembly spot, just right of the center of the table. The **board** sits in the frame, held a little above the
table so component legs can pass down through the holes. Ten **positions** are printed on the board, each with
its own **designator**, its own **silkscreen outline**, and its own holes. A **bin rack** with ten labeled
**bins** sits in one of three start zones. A **scrap cup** stands at the back-right. Two cards stand at the
back of the table: the **BOM** on the left and the **assembly diagram** on the right.

The order never changes: place all ten components in **BOM row order**, row 1 through row 10; then press all
ten flush, again row 1 through row 10; then verify all ten against the assembly diagram, row 1 through row 10.
No component is pressed until every position is filled. No position is verified until the pressing pass is
done. The episode does not end until all ten positions are filled, flush, and verified.

The right gripper reads the BOM, picks every component, lines up every polarity mark, pushes every component
in, presses every one flush, and fixes anything the verify pass turns up. The left gripper presses the board
frame down by its left rail and holds it there for the whole episode, so the board cannot slide while a
component goes in or gets pressed. The left gripper stays on the left rail and never reaches across the board.
The right gripper works the board, the bin rack, and the scrap cup.

The table is set up in one of three ways. Only the bin rack moves; the board frame, the BOM, the assembly
diagram, and the scrap cup are in the same place in all three, except that in Config R2 the scrap cup trades
places with the bin rack.

* **Config M:** the bin rack is at the front-center, in front of the board frame.
* **Config R1:** the bin rack is at the front-right.
* **Config R2:** the bin rack is at the back-right, and the scrap cup stands at the front-right.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the bin rack starts at the front-center (**Config M**), the front-right (**Config R1**)
  or the back-right (**Config R2**). One config per episode, chosen before recording and never changed
  mid-episode.
* **Same-side rule:** the **right gripper** picks every component in every config. The left gripper holds the
  left rail for the whole episode, so no left zone is used and there is no Config L; the config changes only
  where the right gripper reaches for the bin rack and the scrap cup. No arm reaches across the board.
* **Fixed roles:** everything else is the same in all three configs — the left gripper holds the rail, the
  right gripper reads, picks, lines up, pushes, presses, verifies, and fixes, and the board frame and both
  cards never move.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the board frame with all ten positions, the bin rack in its
   start zone, the scrap cup, and both cards at the back.
3. The board is visible from above and from the front, so every silkscreen outline, every board mark, and the
   gap under every component body can be seen.
4. Both arms are at home with grippers open.
5. The table is bare apart from the board frame, the two cards, the bin rack, the scrap cup, and robot
   hardware.
6. The right arm reaches bin 1 and bin 10 in the bin rack's start zone (Config M, R1, or R2), position R1,
   position J1, and the scrap cup without stretching. The left arm reaches the left rail of the board frame
   without stretching.

### Materials checklist

1. One **board frame** sits on the **assembly spot**, just right of the center of the table, **square** to the
   front edge and flat on the table.
2. One bare **board** sits in the frame, printed side up, with clear space under it for the legs.
3. All ten **positions** are empty. Every hole is clear and nothing is left in it.
4. Each position shows its **designator** and its **silkscreen outline**, both readable from above.
5. The eight positions that go in one way only show their **board mark**: a **band line** at D1 and D2, a
   **flat edge** at LED1, a **minus mark** at C1 and C2, a **notch mark** at U1, and an **open face** printed
   toward the front edge at J1.
6. The **BOM** card stands at the back-left of the table with ten numbered rows:

   | Row | Designator | Bin label | Orientation rule |
   | --- | --- | --- | --- |
   | 1 | R1 | R1 | none — goes in either way |
   | 2 | R2 | R2 | none — goes in either way |
   | 3 | R3 | R3 | none — goes in either way |
   | 4 | D1 | D1 | band toward the band line |
   | 5 | D2 | D2 | band toward the band line |
   | 6 | LED1 | LED1 | flat side toward the flat edge |
   | 7 | C1 | C1 | stripe toward the minus mark |
   | 8 | C2 | C2 | stripe toward the minus mark |
   | 9 | U1 | U1 | notch toward the notch mark |
   | 10 | J1 | J1 | open face toward the front edge |

7. The **assembly diagram** card stands at the back-right of the table. It shows the finished board with all
   ten positions filled, each one named by its designator, and the polarity mark drawn on every component that
   has one.
8. The **bin rack** sits in the start zone for this episode's config, with ten open **bins**, numbered 1 at
   the left to 10 at the right. Each bin carries a printed label. The labels run in the opposite order to the
   BOM: bin 1 J1, bin 2 U1, bin 3 C2, bin 4 C1, bin 5 LED1, bin 6 D2, bin 7 D1, bin 8 R3, bin 9 R2, bin 10 R1.
   - **Config M:** front-center, in front of the board frame
   - **Config R1:** front-right
   - **Config R2:** back-right, in front of the assembly diagram card
9. Every bin holds several of its one part, all the same, legs straight, so a bent one can be swapped out.
10. The **scrap cup** stands at the back-right, empty, mouth up (Config M and R1). **IF Config R2**, it stands
    at the front-right, where the bin rack is in Config R1.
11. Keep the left side of the table clear. The left gripper comes in from there onto the frame's left rail.
12. Before collection, confirm by hand that:
    - every component's legs drop into its position's holes without being forced;
    - a component pushed all the way in sits **seated flush** and stays put when released;
    - a component can be pulled straight up and out again without bending its legs;
    - both cards stand up on their own and are readable from the assembly spot.

### Workspace layout

- **Assembly spot:** just right of the center of the table — the board frame stays here all episode
- **Board in the frame:** the ten positions, R1 through J1
- **Back-left:** the BOM card
- **Back-right:** the assembly diagram card, and the scrap cup in Config M and R1 (the bin rack in Config R2)
- **Start zone:** the bin rack with ten bins — front-center (Config M), front-right (Config R1), or back-right
  (Config R2); in Config R2 the scrap cup stands at the front-right instead
- **Left side:** kept clear, so the left gripper can come in onto the frame's left rail

### Arm assignments

- **Left gripper:** presses the board frame down by its left rail and holds it there for the whole episode, so
  the board cannot slide while the right gripper works. It never reaches for the bin rack, whichever config
  is on the table.
- **Right gripper:** reads off the BOM and the assembly diagram, picks each component from its labeled bin,
  lines up its polarity mark, pushes it into its position, presses every component flush, and backs out and
  re-places anything the verify pass turns up. It reaches forward for the bin rack in Config M, to the
  front-right in Config R1, and to the back-right in Config R2, and drops scrap into the cup at the back-right
  (front-right in Config R2).

## Vocabulary

- **Assembly spot:** the place on the table, just right of center, where the board frame sits. The frame stays
  here for the whole episode.
- **Square:** the front edge of the board frame lines up with the front edge of the table, so neither end of
  the frame sits nearer the front.
- **Board frame:** the low open stand the board sits in. It holds the board a little above the table so
  component legs can pass down through the holes. It stays on the assembly spot and is never lifted.
- **Left rail:** the left-hand bar of the board frame. This is the only part the left gripper touches.
- **Board:** the printed circuit board sitting in the frame. It is never lifted out of the frame.
- **Position:** one printed spot on the board where one component goes. Each position has its own designator,
  its own silkscreen outline, and its own holes.
- **Designator:** the short name printed beside a position — R1, R2, R3, D1, D2, LED1, C1, C2, U1, or J1.
- **Silkscreen outline:** the white shape printed around a position showing where the component body sits.
- **Holes:** the small holes inside a position that the legs go into.
- **Component:** one part fitted to the board. Ten components are fitted in one episode.
- **Body:** the solid part of a component that the legs come out of.
- **Legs:** the metal wires sticking out of the bottom of a component.
- **Bent leg:** a leg that is kinked or splayed so it will not drop into its hole.
- **BOM:** the parts list card at the back-left. It has ten numbered rows. Each row gives a designator, the bin
  to pick from, and the orientation rule.
- **BOM row:** one line of the BOM. Row 1 is done first, row 10 last.
- **BOM row order:** rows 1 to 10 in the order printed on the card, top to bottom.
- **Assembly diagram:** the picture card at the back-right showing the finished board with all ten positions
  filled and every polarity mark drawn.
- **Bin rack:** the holder with ten open bins. It stands in the start zone.
- **Start zone:** where the bin rack stands at the start of the episode — front-center (**Config M**),
  front-right (**Config R1**), or back-right (**Config R2**). One per episode, chosen before recording and
  never changed mid-episode. In Config R2 the scrap cup stands at the front-right.
- **Bin:** one compartment in the rack. Each bin carries a printed label and holds several of that one part.
- **Bin label:** the designator printed on a bin. The BOM row says which bin label to pick from.
- **Polarity mark:** the mark on a component that says which way round it goes — a band, a stripe, a flat side,
  or a notch.
- **Band:** the printed ring around one end of a diode body.
- **Stripe:** the printed strip down one side of a capacitor body.
- **Flat side:** the flattened part of the rim around an LED body.
- **Notch:** the half-moon cut in one end of an IC body.
- **Open face:** the side of the J1 connector where the wire openings are.
- **Board mark:** the matching mark printed at a position — the **band line** at D1 and D2, the **flat edge**
  at LED1, the **minus mark** at C1 and C2, and the **notch mark** at U1.
- **Lined up:** the component's polarity mark points at the same end of the position as the board mark, before
  any leg goes into a hole.
- **Seated flush:** the bottom of the body sits down on the board face all the way round, with no gap you can
  see under it.
- **Standing proud:** part of the body is lifted off the board face, so there is a gap you can see under it.
- **Tilted:** one side of the body touches the board and the other side does not.
- **Stays put:** the component does not move, lift, or fall over when the right gripper opens and lets go.
- **Backed out:** pulled straight up out of the holes with the right gripper, in line with the legs, without
  rocking or levering sideways.
- **Straight in:** the body stays level and square to the board while it goes down, so both legs go into their
  holes together.

## Steps

Run Steps 1–4 in order on the one board, then end the episode with Step 5. Only the pick in 2.1, the scrap-cup
drop in 2.3, and the fixes in Step 4 depend on the config: the **right gripper** reaches to wherever the config
puts the bin rack and the scrap cup. Every other line is the same in all three configs.

### Step 1: Hold the board frame down

**Goal:** the board frame is pinned flat on the assembly spot and cannot slide for the rest of the episode.

- With the **left gripper**, press down on the **left rail** of the board frame and hold it against the table.
- Keep the **left gripper** there through Steps 2, 3, and 4.

**Check:** the frame is flat on the table, **square** to the front edge, and does not slide when the left
gripper presses. If the frame is crooked, straighten it with the **left gripper** first, then press it down.

**Expected state:** the frame is held, the board sits in it printed side up, and all ten positions are empty.

### Step 2: Place all ten components in BOM row order

**Goal:** all ten positions hold the right component, lined up the right way round, with every body pushed
down onto the board.

- With the **left gripper**, keep pressing the board frame down.
- Work **row 1 first, then 2, 3, 4, 5, 6, 7, 8, 9, 10**. Do one component at a time.
- Press nothing flush in this step beyond the push that puts it in. The seating pass is Step 3.
- With the **right gripper**, carry each component in one go, straight from its bin to its position. Do not set
  a component down on the board or the table on the way.
- Hold every component by its **body** with the **right gripper** only. Never pinch the **legs**, and never
  bend them.

#### 2.1 Pick the right component

- Read the **BOM row** and take its **designator** and its **bin label**.
- **IF the bin rack is at the front-center (Config M):** with the **right gripper**, reach forward, in front of
  the board frame, to the bin rack.
- **IF the bin rack is at the front-right (Config R1):** with the **right gripper**, reach to the front-right
  corner, to the bin rack.
- **IF the bin rack is at the back-right (Config R2):** with the **right gripper**, reach past the assembly
  spot to the back-right, to the bin rack in front of the assembly diagram card.

Then, in all three:

- Find the **bin** with that label in the bin rack.
- With the **right gripper**, pinch one component in that bin by its **body** and lift it straight up out of
  the bin.
- Take one component only. Leave the rest of the bin undisturbed.

#### 2.2 Line up the polarity mark

- Find the **position** on the board with the same **designator** as the BOM row.
- If the BOM row gives an orientation rule, turn the component in the **right gripper** until its **polarity
  mark** points at the same end of the position as the **board mark**, following the rule on the row.
- Hold the component just above the position and check the mark is **lined up** before any leg touches a hole.
- R1, R2, and R3 have no polarity mark and go in either way. Still lay them along their outline.
- If the mark is the wrong way round, turn the component in the **right gripper** now, while it is still in
  the air.

#### 2.3 Push the component in

- With the **right gripper**, lower the component **straight in** until both **legs** drop into the holes.
- Keep the body level and square to the board while it goes down. Never turn the component once a leg is in a
  hole.
- With the **right gripper**, push the body straight down until it sits on the board face.
- Open the **right gripper** and let go. The component must **stay put**.
- If a leg will not drop into its hole, back the component out with the **right gripper**, line it up over the
  holes again, and lower it straight in.
- If a leg is **bent** and still will not go in, put that component in the **scrap cup** with the **right
  gripper** and take a fresh one from the same bin.
- **IF Config M or R1:** the scrap cup is at the back-right. **IF Config R2:** it is at the front-right.
- Never force a component in and never push a bent leg into a hole.
- Go back to 2.1 for the next BOM row.

**Check:** after each component, the body sits down on the board inside its outline, the polarity mark points
the way the BOM row says, and the component stays put when the right gripper lets go. If the mark is the wrong
way round, back the component out with the **right gripper**, turn it in the air, and lower it in again. If
the component falls over or comes out, pick it up with the **right gripper** and place it again.

**Expected state:** all ten positions are filled, each with the component its BOM row names, every polarity
mark lined up with its board mark, and the right gripper empty.

### Step 3: Press all ten components flush

**Goal:** every one of the ten bodies is **seated flush** on the board face.

- With the **left gripper**, keep pressing the board frame down.
- Press **row 1 first, then 2, 3, 4, 5, 6, 7, 8, 9, 10**. Press every component, every episode.
- With the **right gripper**, put the flat of the gripper on the **top of the body**, over its middle, and push
  straight down toward the board.
- Push slow and steady. Never press on a **leg**, never press on one end only, never rock the body, and never
  tap or knock it down.
- Push until the body sits down on the board face all the way round, then open the **right gripper** and lift
  clear.
- Look under the body from the front. There must be no gap you can see, and the body must not be **tilted**.
- If the body is still **standing proud** or **tilted**, press it straight down again with the **right
  gripper**.
- If it will not go flush after two presses, back it out with the **right gripper**, lower it straight in
  again, and press it once more.
- If it still will not go flush, leave that position as it is, go on to the next row, and log the board for a
  station check.

**Check:** all ten components were pressed, and every body sits flat on the board with no gap under it. If any
component was not pressed, press it with the **right gripper** before going on to Step 4.

**Expected state:** all ten bodies are seated flush and level, nothing has come loose, and the right gripper is
empty.

### Step 4: Verify the board against the assembly diagram

**Goal:** every one of the ten positions is checked against the **assembly diagram** and matches it.

- With the **left gripper**, keep pressing the board frame down.
- Verify **row 1 first, then 2, 3, 4, 5, 6, 7, 8, 9, 10**. Check every position, every episode.
- Read the **assembly diagram** for that designator, then look at that position on the board. Check three
  things:
  1. the position is filled;
  2. the component matches the one the diagram draws there;
  3. the polarity mark points the way the diagram draws it.
- Use the diagram for every position. Do not check a position from memory.
- If a position is **empty**, go back to 2.1 for that BOM row and place the component, then press it flush with
  the **right gripper**, then verify it again.
- If the wrong component is in a position, back it out with the **right gripper**, put it in the **scrap cup**,
  place the right one from its bin, press it flush, then verify that position again.
- **IF Config M or R1:** the scrap cup is at the back-right. **IF Config R2:** the scrap cup is at the
  front-right and the bin rack at the back-right.
- If a polarity mark is the wrong way round, back the component out with the **right gripper**, turn it in the
  air, lower it straight in, press it flush, then verify that position again.
- Back a component out only by pulling it straight up in line with its legs. Never lever it out sideways and
  never pull it by a leg.
- Every fix earns another look at that same position.

**Check:** all ten positions were checked against the diagram, and every one matches it. If any position was
not checked, check it before ending the episode.

**Expected state:** all ten positions are filled, seated flush, lined up as the diagram draws them, and the
right gripper is empty.

### Step 5: End the episode

**Goal:** recording ends with all ten positions filled, seated flush, and verified.

1. Confirm the end state:
   - all ten positions hold the component their BOM row names;
   - every polarity mark points the way the assembly diagram draws it;
   - every body is seated flush on the board with no gap under it;
   - nothing is left loose on the board, in the frame, or on the table;
   - the bin rack is upright with its parts in their own bins, and both cards still stand at the back;
   - the board frame is still **square** on the assembly spot.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

### After each episode

1. Pull each of the ten components straight up out of the board, in line with its legs, and lay it back in the
   bin with its designator on the label.
2. Empty the scrap cup. Put parts with straight legs back in their own bins, and set parts with bent legs
   aside for the end of the session.
3. Check every hole is clear and nothing is left in it. Brush dust and clipped metal off the board and out of
   the frame.
4. Set the board frame **square** on the assembly spot, flat against the table, with the board printed side up
   in it. Stand both cards up at the back, BOM on the left, diagram on the right. Set the bin rack in the start
   zone for the next episode's config — front-center (Config M), front-right (Config R1), or back-right
   (Config R2) — and set the scrap cup upright and empty at the back-right (front-right in Config R2).
5. Top each bin back up so it holds several parts with straight legs.
6. Run both Setup checklists before the next episode.

### At the end of the session

1. Inspect the parts. Straighten or replace any component with bent legs. Replace a component whose polarity
   mark has rubbed off. Replace the board if a position's holes are loose, torn out, or no longer hold a
   component still, or if a designator or board mark is no longer readable. Replace a card if it is creased
   so it will not stand.
2. Leave the frame square on the assembly spot with an empty board in it, all ten bins stocked and labeled,
   the scrap cup empty, and both cards standing at the back.

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

**Note on the start position:** the violations below were written for Config R1 (bin rack at the front-right,
scrap cup at the back-right). The pickup and arm-role cues will be rewritten later to cover all three start
positions; they are left as they are for now. Until then, anything that does not match the episode's config
goes under **Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the bin rack is not in the
  start zone for the config; the scrap cup is not where that config puts it; a gripper reaches across the
  board for a component; or the wrong IF line is followed.
- **SOP rule broken:** the start position and the same-side rule (the bin rack stands at the front-center,
  front-right, or back-right for the whole episode, and the right gripper picks every component from there in
  every config; the IF line followed is the one for the config on the table).
- **Coaching note:** look where the bin rack is before the first reach, then follow that config's IF lines
  through Steps 2 and 4.

**Violation: Board frame not held**
- **Visible cue:** the left gripper is off the left rail while the right gripper picks, places, presses, or
  backs out a component, and the frame slides, lifts, or is chased across the spot.
- **SOP rule broken:** Step 1 (the left gripper presses the board frame down by its left rail and holds it
  there through Steps 2, 3, and 4).
- **Coaching note:** left gripper on the rail first, and leave it there until the episode ends.

**Violation: Board or frame moved off the assembly spot**
- **Visible cue:** either gripper lifts, turns, or drags the board frame, lifts the board out of the frame, or
  the frame ends the episode out of square with the front edge.
- **SOP rule broken:** Steps 1–4 (the frame stays flat and square on the assembly spot for the whole episode
  and is never lifted; the board is never lifted out of the frame).
- **Coaching note:** bring the component to the board; never move the board to the component.

**Violation: Components placed out of BOM order**
- **Visible cue:** the right gripper places the components in some order other than BOM row 1, 2, 3, 4, 5, 6,
  7, 8, 9, 10.
- **SOP rule broken:** Step 2 (work row 1 first, then 2 through 10, one component at a time).
- **Coaching note:** top of the card down, one at a time. Say the row number before you pick.

**Violation: Component taken from the wrong bin**
- **Visible cue:** the right gripper picks from a bin whose label does not match the designator on the BOM row
  it is working, and carries it to the board.
- **SOP rule broken:** Step 2 (read the BOM row, take its bin label, and pick from the bin with that label).
- **Coaching note:** the bins do not run in BOM order. Read the label on the bin, not its place in the rack.

**Violation: Component put in the wrong position**
- **Visible cue:** the right gripper pushes a component into a position whose designator is not the one on the
  BOM row it is working, and the episode moves on.
- **SOP rule broken:** Step 2 (find the position with the same designator as the BOM row, and put the
  component there).
- **Coaching note:** designator on the row, designator on the board. Match the name before you lower it.

**Violation: Position left empty**
- **Visible cue:** the right gripper never puts a component in one of the ten positions, and the episode goes
  on to press, verify, or end with that outline bare.
- **SOP rule broken:** Step 2 (all ten positions are filled before the pressing pass starts).
- **Coaching note:** count ten components in ten positions before you start pressing.

**Violation: Component mishandled on the way in**
- **Visible cue:** the right gripper pinches a component by its legs, bends a leg, carries two components at
  once, or sets one down on the board or the table on the way from its bin.
- **SOP rule broken:** Step 2 (carry each component in one go straight from its bin to its position, held by
  its body only, without bending a leg).
- **Coaching note:** one part, body only, straight to the position.

**Violation: Polarity mark the wrong way round**
- **Visible cue:** a band, stripe, flat side, notch, or open face ends up pointing at the opposite end of the
  position from its board mark, and the episode moves on.
- **SOP rule broken:** Step 2 (turn the component so its polarity mark points at the same end of the position
  as the board mark, following the rule on the BOM row).
- **Coaching note:** band to the line, stripe to the minus, flat to the flat, notch to the notch.

**Violation: Orientation not checked before the legs went in**
- **Visible cue:** the right gripper drops a component straight into its holes without ever holding it above
  the position, or turns it only after a leg is already in.
- **SOP rule broken:** Step 2 (hold the component above the position and check the mark is lined up before any
  leg touches a hole; never turn a component once a leg is in a hole).
- **Coaching note:** turn it in the air, look, then lower it. Turning it in the holes bends the legs.

**Violation: Component pushed in crooked**
- **Visible cue:** the right gripper lowers a component with the body leaning, so one leg goes in first and the
  other is dragged or scraped into its hole.
- **SOP rule broken:** Step 2 (lower the component straight in, body level and square to the board, so both
  legs go into their holes together).
- **Coaching note:** level and square, both legs together, straight down.

**Violation: Bent component forced in or left loose**
- **Visible cue:** the right gripper keeps pushing a component whose leg will not enter, forces a bent leg into
  a hole, or leaves a rejected component lying on the board, in the frame, or on the table instead of putting
  it in the scrap cup.
- **SOP rule broken:** Step 2 (never force a component and never push a bent leg into a hole; put a bent
  component in the scrap cup and take a fresh one from the same bin).
- **Coaching note:** if it fights you, back it out. Bent parts go in the cup, not on the board.

**Violation: Component let go before it stays put**
- **Visible cue:** the right gripper opens and the component tips, lifts, or comes back out, and the episode
  moves on to the next row anyway.
- **SOP rule broken:** Step 2 (open the gripper only once the component stays put; if it falls over or comes
  out, pick it up and place it again).
- **Coaching note:** let go and look before you move to the next row.

**Violation: Pressing pass skipped or partial**
- **Visible cue:** the right gripper presses fewer than ten components, or none at all, before the episode
  moves on to the verify pass or the ending.
- **SOP rule broken:** Step 3 (press row 1 through row 10; press every component, every episode).
- **Coaching note:** ten parts, ten presses. Count them out as you go.

**Violation: Seating press done the wrong way**
- **Visible cue:** the right gripper presses on a leg, presses on one end of the body, rocks the body side to
  side, or taps or knocks it down instead of a slow straight push on the middle of the top face.
- **SOP rule broken:** Step 3 (put the flat of the gripper on the top of the body over its middle and push
  straight down, slow and steady, without pressing a leg, pressing one end, or rocking).
- **Coaching note:** flat on the middle, straight down, slow. A rock lifts the far side back up.

**Violation: Component left standing proud**
- **Visible cue:** a body is still lifted off the board face with a gap under it, or sits tilted with one side
  down and one side up, and the episode moves on.
- **SOP rule broken:** Step 3 (push until the body sits on the board face all the way round, with no gap you
  can see under it and no tilt).
- **Coaching note:** look under the body from the front before you move on. A gap means it is not seated.

**Violation: Failed seating not re-pressed**
- **Visible cue:** a body stays proud or tilted after a press and the right gripper moves straight on to the
  next row without pressing it again or backing it out.
- **SOP rule broken:** Step 3 (press it again; if it will not go flush after two presses, back it out, lower
  it straight in, and press it once more).
- **Coaching note:** press, look, press again. Back it out on the third try, do not lean on it.

**Violation: Verify pass skipped**
- **Visible cue:** the episode goes from the pressing pass straight to the ending, or fewer than ten positions
  are checked against the diagram.
- **SOP rule broken:** Step 4 (verify row 1 through row 10; check every position, every episode).
- **Coaching note:** ten positions, ten checks, diagram in view each time.

**Violation: Verified without the diagram**
- **Visible cue:** the board is looked over as a whole without the assembly diagram being read, or positions
  are called good from memory.
- **SOP rule broken:** Step 4 (read the assembly diagram for that designator, then look at that position; do
  not check a position from memory).
- **Coaching note:** diagram first, board second, one designator at a time.

**Violation: Fault found at verify but not fixed**
- **Visible cue:** an empty position, a wrong component, or a backwards polarity mark is passed over during
  the verify pass and the episode ends with it still there.
- **SOP rule broken:** Step 4 (fill an empty position, swap a wrong component, or turn a backwards one, then
  press it flush).
- **Coaching note:** what you find, you fix. Verify is not just for looking.

**Violation: Fix not re-verified**
- **Visible cue:** the right gripper places, swaps, or turns a component during the verify pass and moves on
  to the next row without looking at that position against the diagram again.
- **SOP rule broken:** Step 4 (every fix earns another look at that same position).
- **Coaching note:** fix it, press it, then check it again before you move on.

**Violation: Component backed out the wrong way**
- **Visible cue:** the right gripper levers a component out sideways, rocks it out, or pulls it by a leg
  instead of pulling it straight up in line with its legs.
- **SOP rule broken:** Steps 2–4 (back a component out only by pulling it straight up in line with its legs;
  never lever it out sideways and never pull it by a leg).
- **Coaching note:** straight up, body only. Levering bends the legs and tears the holes.

**Violation: Work done out of order**
- **Visible cue:** the phases run out of sequence — the right gripper starts pressing before all ten positions
  are filled, starts verifying before the pressing pass is done, or goes back to place a new component after
  the verify pass has started for a reason other than a fault it just found.
- **SOP rule broken:** Steps 2–4 (place all ten, press all ten, then verify all ten, in that order).
- **Coaching note:** finish the phase before you start the next one. Say the phase name before you move.

**Violation: Wrong arm used**
- **Visible cue:** an action assigned to one gripper is done by the other, including the left gripper picking,
  placing, turning, pressing, or backing out a component, or the right gripper holding down the frame.
- **SOP rule broken:** Steps 1–4 (the right gripper picks, places, presses, verifies, and fixes; the left
  gripper holds the frame).
- **Coaching note:** right gripper does the work, left gripper holds the rail. It does not swap.

**Violation: Component, bin, or card knocked off its spot**
- **Visible cue:** either gripper drops a component on the board, the table, or the floor, tips or spills a
  bin, drops a part into the wrong bin, knocks the bin rack or the scrap cup off its spot, or knocks a card
  over.
- **SOP rule broken:** Steps 2–4 (take one component only, leave the rest of the bin undisturbed, and keep the
  bin rack, the scrap cup, and both cards on their spots through the whole episode).
- **Coaching note:** work slower and lower over the table, and keep each carry short.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before the ten positions and the verify pass are confirmed, an arm is not
  home, a gripper is closed, or an arm does something else after homing.
- **SOP rule broken:** Step 5 (confirm the end state, return both arms home with grippers open as their final
  action, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than tagging
them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- A component arrives with a leg already broken off, so it cannot be fitted at all.
- A position's holes are drilled off pitch or blocked, so a good component cannot go in.
- A hole is torn out or worn loose before the episode, so a correctly placed component will not stay put.
- A designator, silkscreen outline, or board mark is missing or unreadable on the board.
- The BOM card or the assembly diagram card is misprinted, so the two disagree about a position.

## Annotation subtasks (from SOP)

1. Press the board frame flat and hold it by the left rail with the left gripper
2. Read the BOM row and find the bin with that label
3. Pick one component from that bin by its body
4. Turn the component in the air until its polarity mark lines up with the board mark
5. Lower the component straight into its position and let go
6. Swap a bent component into the scrap cup and take a fresh one
7. Repeat the pick, orient, and place for all ten BOM rows
8. Press each component flush, row 1 through 10
9. Re-press or re-place any component left standing proud
10. Verify each position against the assembly diagram, row 1 through 10
11. Back out and re-place any component the verify pass turns up, then check it again
12. Confirm the end state, return both arms home, and end the episode
