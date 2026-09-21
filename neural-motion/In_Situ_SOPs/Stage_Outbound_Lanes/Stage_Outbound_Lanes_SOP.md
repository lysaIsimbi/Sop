# Stage Outbound Lanes SOP (1x Episode: six cases, in situ)

One episode stages six labeled cases into two route lanes, at the dock deck where the lanes live. The
base is **passive**: it has no drive of its own, so it is pushed by hand to the front of the deck and
locked there, and nothing is carried away to a table. Everything the episode touches is already on the
deck when recording starts: the six cases in the feed row, the two lanes with their taped spots, the two
lane flags, and the manifest card in its holder.

The episode runs these five actions in this order and no other: **read the deck at the manifest, stage
the three Route A cases into Lane A, stage the three Route B cases into Lane B, verify the count in Lane A
and flip its flag, verify the count in Lane B and flip its flag.**

The deck is worked **as found**. It is the deck as the pack line left it: six closed cases standing in the
feed row in the order they came off the line, both lanes empty, both lane flags lying flat and reading
OPEN. Three cases are for **Route A** (labels A1, A2, and A3, with A3 the heavy case) and three are for
**Route B** (labels B1, B2, and B3, with B1 the heavy case). The episode ends with each lane holding its
three cases in **lane order**, the feed row empty, and both flags standing and reading STAGED.

**Lane order is the same in both lanes.** Each lane fills from its head. The **heavy case** goes on spot 1,
the head spot, first, whatever its stop number. Then the other two cases go on spot 2 and spot 3 in stop
order, the lower stop number first. So Lane A reads, from its head: **A3 (heavy), A1, A2**. Lane B reads,
from its head: **B1 (heavy), B2, B3**.

**This is an in-situ task, and three things follow from that.** First, an **upper shelf runs directly
above the lane strip**, so **every reach into the lane strip is from the front, straight in, level**. No
gripper comes down onto a lane, a spot, or a case from above. Second, **no case is ever lifted**: every
case is **slid** along the deck with the gripper closed on its sides, from the feed row to its spot, and
it never leaves the deck and never turns. A heavy case is not lifted on this dock, and a slid case stays
flat under the shelf. Third, the **deck is never leaned on and never pushed**: no gripper, wrist, or
forearm rests on the deck, the upper shelf, a flag, or the manifest holder, and no drag is ever hard
enough to shift the deck.

The deck is set up in one of three ways. Only the **order of the six cases in the feed row** changes. The
lanes, the spots, the flags, and the manifest are the same in all three. The feed row stands in two groups
of three on the feed strip, the **left group** at the front-left and the **right group** at the
front-right, with the relay spot empty between them. Each group is listed left to right.

* **Config 1 (sorted):** left group **A1, A2, A3 (heavy)**. Right group **B1 (heavy), B2, B3**.
* **Config 2 (heavies swapped):** left group **A1, A2, B1 (heavy)**. Right group **A3 (heavy), B2, B3**.
* **Config 3 (swapped):** left group **B1 (heavy), B2, B3**. Right group **A1, A2, A3 (heavy)**.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on
where a case stands it says so on an **IF** line. Look at the feed row and follow the line that matches.

What stays constant across all sessions:

* **Same-side rule:** the gripper on the case's side drags it out of the feed row. That is the **left
  gripper** for a case in the left group and the **right gripper** for a case in the right group. No arm
  reaches across the deck.
* **Hand-over rule:** a case whose lane is on the other side of the deck is too far for the gripper that
  drags it out. So that gripper **hands it over** at the **relay spot** in the middle of the feed strip,
  and the lane's own gripper takes it from there. Nothing is handed over when the case's lane is on its
  own side.
* **Fixed roles:** the **left gripper** stages Lane A and flips flag A. The **right gripper** stages Lane
  B and flips flag B. The five actions run in the same order in every config.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm
reaches over, under, around, or past the other. Nothing is moved two at a time: one gripper holds one
case, and the other gripper is empty and clear of the deck.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never
steered, nudged, or repositioned once recording starts. It is parked once, before recording, and does not
move again until the episode is over.

1. Push the base by hand up to the deck and stop it **square to the front edge**, so the lane strip runs
   straight across the frame of the camera and neither lane sits nearer than the other.
2. Stop it **centered on the deck**, so the head of Lane A at the left end and the head of Lane B at the
   right end are the same distance out from the middle of the base.
3. Stop it **close enough** that both grippers reach the lane strip straight in and level without either
   arm extending, and **far enough** that neither arm, wrist, nor any part of the base touches the deck,
   a flag, the manifest holder, or the upper shelf while both arms work.
4. Check the **height band**: with the base parked, both grippers come level onto the feed strip and, with
   a case in the gripper, level onto the lane strip under the upper shelf, without a wrist or forearm
   fouling the shelf.
5. Check the **left side**: the **left gripper** reaches all three cases in the left group, the relay spot,
   all three spots in Lane A including spot 1 at the left end, and the tip of flag A, all without
   extending and without knocking anything. It reaches no Lane B spot and not flag B.
6. Check the **right side**: the **right gripper** reaches all three cases in the right group, the relay
   spot, all three spots in Lane B including spot 1 at the right end, and the tip of flag B, all without
   extending. It reaches no Lane A spot and not flag A.
7. Check the **relay spot**: both grippers reach a case standing on it, each from its own side, straight
   in and level, without either arm passing in front of the other.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not
   work a deck the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the deck hard
enough to shift it, nothing touches it by hand, and it is never repositioned mid-task. A base that moves
after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the deck and its frame includes the whole deck: both lanes with
   all six spots, both lane flags, the feed strip with both groups and the relay spot, and the manifest
   card in its holder.
3. The camera reads the **route label** on the front face of every case, in the feed row and on a spot,
   so which case went where is readable.
4. The camera reads the **heavy mark** on the two heavy cases.
5. The camera reads the **spot numbers** on the tape at the front edge of each spot.
6. The camera reads both **lane flags**, lying flat and standing, so OPEN and STAGED are readable.
7. The camera reads the **manifest card**.
8. Both arms are at home with grippers open.
9. The **left arm** reaches the three cases in the left group, the relay spot, the three Lane A spots, and
   the tip of flag A without extending to a joint limit. It reaches no Lane B spot.
10. The **right arm** reaches the three cases in the right group, the relay spot, the three Lane B spots,
    and the tip of flag B without extending to a joint limit. It reaches no Lane A spot.
11. Both grippers come in and go out of the lane strip **from the front and level**. Neither comes down onto
    a lane or a case from above, and neither wrist nor forearm touches the upper shelf on the way in or out.
12. The two arms do not collide, and neither arm passes in front of the other.
13. If a place cannot be reached, re-park the base by the Base positioning steps until lines 9 to 12 hold.

### Materials checklist

1. The **dock deck** stands where it lives, bolted or braced to the floor or the wall. It is not moved, not
   leaned on, and not pushed at any point.
2. The deck top is **smooth and flat**, so a closed case slides along it with a light pull and does not tip,
   catch, or turn.
3. An **upper shelf** runs directly above the back of the deck, so the only way onto the lane strip is
   straight in from the front and never from the top. The shelf is high enough for a gripper holding a
   case to come in level under it, and low enough that nothing can be lifted over it. The upper shelf is
   empty and stays empty.
4. The **lane strip** is the part of the deck top under the upper shelf. It carries the two lanes and
   nothing else.
5. **Lane A** is the left half of the lane strip. It has **three taped spots** in a row, from the left end:
   **spot 1** at the left end, then **spot 2**, then **spot 3** toward the middle. Spot 1 is the **head**
   of Lane A.
6. **Lane B** is the right half of the lane strip. It has **three taped spots** in a row, from the right
   end: **spot 1** at the right end, then **spot 2**, then **spot 3** toward the middle. Spot 1 is the
   **head** of Lane B.
7. Each spot is a taped box on the deck a little bigger than a case, and carries its number on the tape
   at its front edge. There is a clear gap between one spot and the next. All six spots start empty.
8. A **route sign** hangs on the front edge of the upper shelf above each lane: **ROUTE A** above Lane A
   and **ROUTE B** above Lane B. Nothing ever touches a sign.
9. The **feed strip** is the part of the deck top in front of the upper shelf. Nothing stands above it.
10. **Six cases** stand on the feed strip in the **feed row**: three in the **left group** at the
    front-left and three in the **right group** at the front-right. Within a group the cases stand side by
    side with about a hand's width between one case and the next, so a gripper's fingers go into the gaps.
    The order in each group is the order this episode's config lists.
11. All six cases are the same size, closed and taped shut, about the size of a shoebox, and narrow
    enough for one gripper to close on both sides. Every case stands with its **route label to the
    front**.
12. Each **route label** is one big route letter and stop number on the front face of the case: A1, A2,
    A3, B1, B2, or B3. No two cases carry the same label.
13. The two **heavy cases**, A3 and B1, carry a **heavy mark**, a red band across the route label reading
    HEAVY. They are weighted so they are clearly heavier than the other four, but they still slide on the
    deck under one gripper.
14. The **relay spot** is the clear middle of the feed strip, between the left group and the right group.
    It is empty at the start and at the end. Nothing else ever stands on it.
15. A **lane flag** stands on the front edge of the deck at the head end of each lane: **flag A** at the
    left end, in front of Lane A spot 1, and **flag B** at the right end, in front of Lane B spot 1. Each
    flag is a small stiff plate on a hinge. Lying flat toward the front it reads **OPEN** on its top face.
    Swung up, it stands and reads **STAGED** on its front face, and a catch holds it standing.
16. Both flags start **lying flat and reading OPEN**.
17. The **manifest card** stands in a fixed holder clipped to the front edge of the upper shelf at the
    middle, above the lane strip, facing the front. It reads: **ROUTE A: 3 cases. ROUTE B: 3 cases. Heavy
    first, then by stop.** Nothing ever touches the card or the holder.
18. Nothing else stands anywhere on the deck within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the six lane spots. You judge every other place by eye
against the deck itself: the lane strip, the feed strip, and the front edge.

* **Deck:** the dock deck the base is parked at. It is never moved, never leaned on, and never pushed.
* **Upper shelf:** the shelf directly over the lane strip. It is what makes every reach into the lane strip
  a front approach. Nothing ever touches it, and nothing ever goes on it.
* **Lane strip:** the deck top under the upper shelf. It carries Lane A and Lane B.
* **Lane A:** the left half of the lane strip, spots 1, 2, and 3 from the left end. **Left gripper only.**
* **Lane B:** the right half of the lane strip, spots 1, 2, and 3 from the right end. **Right gripper
  only.**
* **Route signs:** ROUTE A above Lane A, ROUTE B above Lane B, on the front edge of the upper shelf.
* **Feed strip:** the deck top in front of the upper shelf, with open air above it.
* **Left group:** the three cases at the front-left of the feed strip. **Left gripper only.**
* **Right group:** the three cases at the front-right of the feed strip. **Right gripper only.**
* **Relay spot:** the clear middle of the feed strip. It is where a hand-over happens, and nowhere else.
  **Both grippers**, each from its own side, one at a time.
* **Flag A:** on the front edge at the left end, in front of Lane A spot 1. **Left gripper only.**
* **Flag B:** on the front edge at the right end, in front of Lane B spot 1. **Right gripper only.**
* **Manifest holder:** on the front edge of the upper shelf at the middle. It is read, never touched.

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the left half: the left group, Lane A, flag A, and, for a hand-over only, the
  relay spot.
* The **right gripper** works the right half: the right group, Lane B, flag B, and, for a hand-over only,
  the relay spot.
* The **left gripper never goes right of the relay spot**, and the **right gripper never goes left of it**.
  The relay spot is where a hand-over happens, and nowhere else.
* Neither arm reaches over, under, around, or past the other, and neither reaches across the front of the
  other arm's body.
* Only one case is moved at a time. A gripper holds one case, and while it does, the other gripper is
  empty and drawn **clear of the deck**.

### Arm assignments

* **Left gripper.** Drags each case in the left group out of the feed row. Takes every Route A case that
  is handed over at the relay spot. Slides the three Route A cases onto their Lane A spots. Flips flag A.
* **Right gripper.** Drags each case in the right group out of the feed row. Takes every Route B case that
  is handed over at the relay spot. Slides the three Route B cases onto their Lane B spots. Flips flag B.
* A case is handed over only when its lane is on the other side of the deck, only at the relay spot, and
  only one case is moved at a time.

## Vocabulary

* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down
  onto the lane strip, a spot, or a case from above. Every reach into the lane strip is a front approach.
* **Case:** one of the six closed, labeled cartons. A case is always slid and never lifted.
* **Sides of a case:** its left face and its right face, the two faces the gripper closes on. The gripper
  never closes on the front face, the back face, or the top.
* **Slide (drag):** the gripper closes on the sides of a case and pulls it level along the deck. The case
  stays flat on the deck the whole way, and its label stays to the front. A case that comes off the deck,
  even a little, or that turns, is not being slid.
* **Route label:** the big route letter and stop number on the front face of a case: A1 to A3, B1 to B3.
  The letter names the lane. The number is the stop.
* **Heavy mark:** the red band across a route label reading HEAVY. A3 and B1 carry it.
* **Heavy case:** a case with the heavy mark. Each lane has exactly one, and it goes on spot 1 first.
* **Lane:** the row of three taped spots on the lane strip for one route. Lane A is left, Lane B is right.
* **Spot:** one taped box in a lane, numbered 1, 2, or 3 from the head. Each spot takes one case.
* **Head:** the outer end of a lane, where spot 1 is: the left end for Lane A, the right end for Lane B.
* **Lane order:** the heavy case on spot 1, then the other two cases on spot 2 and spot 3 with the lower
  stop number on spot 2. Lane A in lane order reads A3 (heavy), A1, A2. Lane B reads B1 (heavy), B2, B3.
* **Next case:** the case the lane order names next: the heavy case of that route while it is still in the
  feed row, and after that the lowest stop number of that route still in the feed row.
* **On its spot:** the case stands wholly inside the tape of its spot, square to the tape, label to the
  front, and touches no other case. A case on a tape line, across two spots, turned, or touching its
  neighbour is not on its spot.
* **Feed row:** the six cases as they stand at the start, in the left group and the right group.
* **Relay spot:** the clear middle of the feed strip, between the two groups.
* **Hand over:** one gripper gives a case to the other at the relay spot, on the deck. The giving gripper
  drags the case onto the relay spot, stops, and holds it still for a **half-second hold**. The giving
  gripper then opens and draws back **clear of the deck**. Only after that does the taking gripper close on
  the sides of the case. The case rests on the deck the whole time. Nothing is handed over in the air.
* **Half-second hold:** the giving gripper stops moving and stays still for about half a second before it
  opens, so the case is at rest when the other gripper comes for it.
* **Lane flag:** the hinged plate at the head end of a lane. Lying flat it reads OPEN. Standing it reads
  STAGED.
* **Flip:** the gripper closes on the tip of a flag, swings it up until it stands and the catch holds it,
  then opens. A flag pushed part way and left leaning is not flipped.
* **Manifest:** the card in the holder that says how many cases each route has and that the heavy case
  goes first.
* **Clear of the deck:** the arm is drawn back so that no part of it is over the feed strip, the lane strip,
  a flag, or the relay spot.

## Steps

Run Step 1. Then run Step 2 three times: once for the **heavy case A3**, once for **A1**, and once for
**A2**, in that order. Then run Step 3 three times: once for the **heavy case B1**, once for **B2**, and
once for **B3**, in that order. Then Step 4, and end the episode with Step 5. Only 2.2 and 3.2 depend on
where a case stands. Every other step is the same in all three configs.

### Step 1: Read the deck at the manifest

**Goal:** both lanes are open and empty, the manifest is read, and both arms have touched nothing yet.

* Hold both arms **clear of the deck**. Touch nothing.
* Read the **manifest card**: Route A has 3 cases, Route B has 3 cases, heavy first, then by stop.
* Read both **lane flags**: flag A and flag B lie flat and read **OPEN**.
* Look across the lane strip: all six spots are empty.
* Count the **feed row**: six cases, three in the left group and three in the right group, every label to
  the front, and two heavy marks.

**Check:** both flags read OPEN, all six spots are empty, and the feed row holds six cases with labels to
the front. If a flag reads STAGED, if a lane already holds a case, or if the feed row does not hold six
cases with labels to the front, do not touch the deck. End the episode and report it.

**Expected state:** nothing has moved, both grippers are open and clear of the deck, and the relay spot is
empty.

### Step 2: Stage one Route A case

Run this step once for the **heavy case A3**, then once for **A1**, then once for **A2**.

**Goal:** the case is **on its spot** in Lane A: A3 on spot 1, A1 on spot 2, A2 on spot 3.

#### 2.1 Find the next case

* Hold both grippers open and **clear of the deck**.
* Read the route labels in the feed row and find the **next case** for Lane A: A3 with the heavy mark
  first, then A1, then A2.
* Read which group it stands in, the left group or the right group.

**Check:** the case found carries the label this pass is for, and no other Route A case with a lower place
in lane order is still in the feed row.

#### 2.2 Take the case

* **IF the case stands in the left group:** with the **left gripper**, come in level from the front and
  close on the **sides** of the case, fingers in the gaps either side of it. With the **left gripper**,
  drag it straight back until it is clear of the row. There is no hand-over.
* **IF the case stands in the right group:** with the **right gripper**, come in level from the front and
  close on the **sides** of the case. With the **right gripper**, drag it straight back until it is clear
  of the row, then across to the **relay spot**, and stop there. Hold it still for a **half-second hold**.
  Open the **right gripper** and draw it back **clear of the deck**. With the **left gripper**, come in
  level from the front and close on the sides of the case on the relay spot.
* Then, in both: with the **left gripper**, keep the case flat on the deck. Do not lift it and do not turn
  it.
* Drag one case only. With the **left gripper**, do not push, shove, or knock any other case in the feed
  row on the way out.
* Hold the other gripper open and **clear of the deck** whenever it is not the one holding the case.

**Check:** the **left gripper** holds one case by its sides, the case is flat on the deck, its label faces
the front, and every other case in the feed row stands where it was.

#### 2.3 Slide it onto its spot

* With the **left gripper**, drag the case level along the deck, in one slide, back under the upper shelf
  and onto its Lane A spot: **spot 1** for the heavy case A3, **spot 2** for A1, **spot 3** for A2.
* Read the spot number on the tape before stopping.
* With the **left gripper**, keep the case clear of every case already on Lane A, and stop when it stands
  inside the tape, square, label to the front.
* Slide straight and level only. With the **left gripper**, do not come down onto the lane from above, do
  not lift the case over a tape line, and do not push it against the case beside it.
* Open the **left gripper**, draw it straight out to the front, and take it **clear of the deck**.

**Check:** the case is **on its spot**: wholly inside the tape, square, label to the front, touching no
other case, and it stays put with the **left gripper** off it. It is on the spot lane order gives it. If it
sits on a line, across two spots, turned, or on the wrong spot, close on its sides again with the **left
gripper** and drag it into the right spot.

**Expected state:** this case is on its Lane A spot. Go back to 2.1 for the next Route A case. After A2,
Lane A reads A3 (heavy), A1, A2 from its head, and no Route A case is left in the feed row or on the relay
spot.

### Step 3: Stage one Route B case

Run this step once for the **heavy case B1**, then once for **B2**, then once for **B3**.

**Goal:** the case is **on its spot** in Lane B: B1 on spot 1, B2 on spot 2, B3 on spot 3.

#### 3.1 Find the next case

* Hold both grippers open and **clear of the deck**.
* Read the route labels in the feed row and find the **next case** for Lane B: B1 with the heavy mark
  first, then B2, then B3.
* Read which group it stands in, the left group or the right group.

**Check:** the case found carries the label this pass is for, and no other Route B case with a lower place
in lane order is still in the feed row.

#### 3.2 Take the case

* **IF the case stands in the right group:** with the **right gripper**, come in level from the front and
  close on the **sides** of the case, fingers in the gaps either side of it. With the **right gripper**,
  drag it straight back until it is clear of the row. There is no hand-over.
* **IF the case stands in the left group:** with the **left gripper**, come in level from the front and
  close on the **sides** of the case. With the **left gripper**, drag it straight back until it is clear of
  the row, then across to the **relay spot**, and stop there. Hold it still for a **half-second hold**.
  Open the **left gripper** and draw it back **clear of the deck**. With the **right gripper**, come in
  level from the front and close on the sides of the case on the relay spot.
* Then, in both: with the **right gripper**, keep the case flat on the deck. Do not lift it and do not turn
  it.
* Drag one case only. With the **right gripper**, do not push, shove, or knock any other case in the feed
  row on the way out.
* Hold the other gripper open and **clear of the deck** whenever it is not the one holding the case.

**Check:** the **right gripper** holds one case by its sides, the case is flat on the deck, its label faces
the front, and every other case in the feed row stands where it was.

#### 3.3 Slide it onto its spot

* With the **right gripper**, drag the case level along the deck, in one slide, back under the upper shelf
  and onto its Lane B spot: **spot 1** for the heavy case B1, **spot 2** for B2, **spot 3** for B3.
* Read the spot number on the tape before stopping.
* With the **right gripper**, keep the case clear of every case already on Lane B, and stop when it stands
  inside the tape, square, label to the front.
* Slide straight and level only. With the **right gripper**, do not come down onto the lane from above, do
  not lift the case over a tape line, and do not push it against the case beside it.
* Open the **right gripper**, draw it straight out to the front, and take it **clear of the deck**.

**Check:** the case is **on its spot**: wholly inside the tape, square, label to the front, touching no
other case, and it stays put with the **right gripper** off it. It is on the spot lane order gives it. If
it sits on a line, across two spots, turned, or on the wrong spot, close on its sides again with the
**right gripper** and drag it into the right spot.

**Expected state:** this case is on its Lane B spot. Go back to 3.1 for the next Route B case. After B3,
Lane B reads B1 (heavy), B2, B3 from its head, the feed row is empty, and the relay spot is empty.

### Step 4: Verify the lane counts

**Goal:** each lane holds the count the manifest gives, in lane order, and both flags stand and read
STAGED.

#### 4.1 Count Lane A and flip flag A

* Hold both grippers open and **clear of the deck**.
* Count the cases on Lane A: **three**, one on each spot, none on a line, and none left in the feed row or
  on the relay spot.
* Read the labels from the head: spot 1 reads **A3** with the heavy mark, spot 2 reads **A1**, spot 3
  reads **A2**.
* Read the manifest: Route A, 3 cases. The count matches.
* If a case is on the wrong spot, on a line, or turned, close on its sides with the **left gripper** and
  drag it into its right spot. If a Route A case is still in the feed row or on the relay spot, stage it by
  Step 2. If a Route B case is on Lane A, drag it with the **left gripper** to the relay spot, hand it over
  to the **right gripper**, and stage it by Step 3. Do not flip the flag until the lane reads right.
* With the **left gripper**, come in level from the front and close on the **tip of flag A**.
* With the **left gripper**, swing the flag up until it stands and the catch holds it.
* Open the **left gripper** and draw it back **clear of the deck**.
* Hold the **right gripper** open and **clear of the deck** for the whole of this substep.

**Check:** Lane A holds three cases reading A3 (heavy), A1, A2 from its head, each on its spot, and flag A
stands and reads STAGED with the **left gripper** off it. If the flag leans and does not stand, close on
its tip again with the **left gripper** and swing it up until the catch holds.

#### 4.2 Count Lane B and flip flag B

* Hold both grippers open and **clear of the deck**.
* Count the cases on Lane B: **three**, one on each spot, none on a line, and none left in the feed row or
  on the relay spot.
* Read the labels from the head: spot 1 reads **B1** with the heavy mark, spot 2 reads **B2**, spot 3
  reads **B3**.
* Read the manifest: Route B, 3 cases. The count matches.
* If a case is on the wrong spot, on a line, or turned, close on its sides with the **right gripper** and
  drag it into its right spot. If a Route B case is still in the feed row or on the relay spot, stage it by
  Step 3. If a Route A case is on Lane B, drag it with the **right gripper** to the relay spot, hand it over
  to the **left gripper**, and stage it by Step 2. Do not flip the flag until the lane reads right.
* With the **right gripper**, come in level from the front and close on the **tip of flag B**.
* With the **right gripper**, swing the flag up until it stands and the catch holds it.
* Open the **right gripper** and draw it back **clear of the deck**.
* Hold the **left gripper** open and **clear of the deck** for the whole of this substep.

**Check:** Lane B holds three cases reading B1 (heavy), B2, B3 from its head, each on its spot, and flag B
stands and reads STAGED with the **right gripper** off it. If the flag leans and does not stand, close on
its tip again with the **right gripper** and swing it up until the catch holds.

**Expected state:** both lanes are full in lane order, both flags stand and read STAGED, the feed row and
the relay spot are empty, and both grippers are clear of the deck.

### Step 5: End the episode

* Confirm Lane A: A3 with the heavy mark on spot 1, A1 on spot 2, A2 on spot 3, each on its spot.
* Confirm Lane B: B1 with the heavy mark on spot 1, B2 on spot 2, B3 on spot 3, each on its spot.
* Confirm the feed strip: the feed row is empty and nothing stands on the relay spot.
* Confirm the flags: flag A and flag B both stand and read STAGED.
* Confirm nothing has been lifted, dropped, tipped, or pushed off the deck, and no case has turned.
* Confirm the deck: the manifest card is in its holder untouched, the route signs hang where they were, and
  the deck has not shifted.
* Confirm the base has not moved.
* Correct any failed check before ending.
* Return both arms home with grippers open, then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Slide the six cases off their spots and stand them in the feed row for the next episode's config: three
   in the left group and three in the right group, in the order that config lists, side by side with about
   a hand's width between cases, every label to the front.
2. Fold both lane flags down by hand until they lie flat and read OPEN.
3. Check every route label is still stuck flat and readable, and that the two heavy marks are on A3 and B1.
   Replace a label that has peeled or faded.
4. Check every case is still closed and taped, square, and slides on the deck under a light pull. Replace a
   case that is burst, crushed, or that catches on the deck.
5. Check the two heavy cases are still clearly heavier than the other four.
6. Check all six spots are empty and their tape and numbers are still down and readable. Re-tape a spot
   whose line has lifted.
7. Check both flag hinges swing freely and both catches hold a flag standing. Replace a flag whose catch
   will not hold.
8. Check the manifest card is in its holder, facing the front, and readable, and that both route signs hang
   above their lanes.
9. Wipe the deck top if dust or grit has built up, so cases still slide without catching.
10. Pick up anything that landed on the deck or the floor.
11. Check the base is still locked and parked square, then run the Base positioning steps and both Setup
    checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible
cue is what the reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it
just because a rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the deck shifts in frame, the lane strip changes angle or size in frame, or the base
  rolls, creeps, or turns at any point after recording starts.
* **SOP rule broken:** Steps 1 to 5, the base is parked and locked before recording and stays still for the
  whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost
  episode.

**Violation: Case lifted off the deck**

* **Visible cue:** a case comes off the deck in a gripper, even a little; a case is carried through the air
  to its spot or to the relay spot; a case is lifted over a tape line; or a case is handed over in the air
  instead of on the relay spot.
* **SOP rule broken:** Steps 2.2, 2.3, 3.2, 3.3, and 4.1 to 4.2, every case is slid flat along the deck and
  never lifted.
* **Coaching note:** close on the sides and pull. The deck carries the case, the gripper only steers it.

**Violation: Approached from above or fouled the shelf**

* **Visible cue:** a gripper comes down onto a lane, a spot, or a case from above instead of coming in level
  from the front, or a wrist, forearm, or case knocks, scrapes, or rests on the upper shelf, a route sign,
  or the manifest holder on the way in or out.
* **SOP rule broken:** Steps 2.3, 3.3, and 4.1 to 4.2, every reach into the lane strip is a front approach,
  level, straight in and straight out.
* **Coaching note:** straight in from the front, straight out the same way. There is no way in from the
  top.

**Violation: Leaned on or pushed the deck**

* **Visible cue:** a gripper, wrist, or forearm rests on the deck top, the upper shelf, a flag, or the
  manifest holder; the deck rocks or shifts; or a drag or a flip presses hard enough to move the deck, a
  spot's tape, or the holder.
* **SOP rule broken:** Steps 2.2 to 4.2, the deck carries no weight and nothing fixed to it is pushed out of
  place.
* **Coaching note:** the arm holds itself up. Pull only as hard as the slide needs.

**Violation: Lane worked while its flag read STAGED**

* **Visible cue:** a gripper drags a case toward a lane, or onto a spot, while that lane's flag is already
  standing and reading STAGED, or while a case already stands on that lane at the start.
* **SOP rule broken:** Step 1, read both flags first and only stage a lane whose flag lies flat and reads
  OPEN and whose spots are empty.
* **Coaching note:** read the flags before the arms move. A lane that reads STAGED belongs to the loader,
  not to you.

**Violation: Heavy case not first**

* **Visible cue:** a case without the heavy mark is slid onto spot 1 of a lane; the heavy case is slid onto
  spot 2 or spot 3; or a case of that route goes onto a lane while its heavy case is still in the feed row.
* **SOP rule broken:** Steps 2.1 to 2.3 and 3.1 to 3.3, the heavy case of each route is staged first, onto
  spot 1, whatever its stop number.
* **Coaching note:** find the red band first. The heavy case leads its lane every time.

**Violation: Cases out of stop order**

* **Visible cue:** after the heavy case, a higher stop number goes onto a lane before a lower one; A2 goes
  onto spot 2 or A1 onto spot 3; B3 goes onto spot 2 or B2 onto spot 3; or the next case taken from the feed
  row is not the one lane order names.
* **SOP rule broken:** Steps 2.1 to 2.3 and 3.1 to 3.3, after the heavy case the other two cases go on
  spot 2 and spot 3 in stop order, the lower stop number first.
* **Coaching note:** read the labels before the gripper closes. Heavy, then the lowest stop, then the next.

**Violation: Case in the wrong lane**

* **Visible cue:** a Route B case is slid onto a Lane A spot, a Route A case is slid onto a Lane B spot, or
  a gripper drags a case toward the lane under the wrong route sign.
* **SOP rule broken:** Steps 2.3 and 3.3, a Route A case goes only onto a Lane A spot and a Route B case
  only onto a Lane B spot.
* **Coaching note:** the letter on the label is the lane. Read it, then read the sign above the lane.

**Violation: Case not on its spot**

* **Visible cue:** a case is left on a tape line, across two spots, turned so its label does not face the
  front, hanging past the edge of its spot, touching the case beside it, or standing on the lane strip off
  any spot, and the gripper opens and draws back anyway.
* **SOP rule broken:** Steps 2.3 and 3.3, each case stands wholly inside the tape of its own spot, square,
  label to the front, touching no other case.
* **Coaching note:** stop inside the tape, square it up, then open. A case on a line is a case the loader
  has to fix.

**Violation: Feed row disturbed**

* **Visible cue:** a case that is not being staged is pushed, shoved, knocked, turned, or dragged out of its
  place in the feed row; a case is dragged through or against another case; or a gripper closes on the
  front face, the back face, or the top of a case instead of its sides.
* **SOP rule broken:** Steps 2.2 and 3.2, the gripper closes on the sides of the next case only, drags it
  straight back clear of the row, and touches no other case.
* **Coaching note:** fingers in the gaps, straight back, and the others stay where they stand.

**Violation: Hand-over done wrong**

* **Visible cue:** the taking gripper closes on a case before the giving gripper has opened and drawn back;
  the giving gripper opens while the case is still moving, with no half-second hold; a case is handed over
  anywhere but on the relay spot; a case whose lane is on its own side is dragged to the relay spot and
  handed over anyway; or a case whose lane is on the other side is dragged across the deck by the gripper
  that took it out, with no hand-over.
* **SOP rule broken:** Steps 2.2 and 3.2, a case whose lane is on the other side is dragged to the relay
  spot, held still for a half-second hold, and let go before the lane's own gripper closes on it. A case
  whose lane is on its own side is not handed over.
* **Coaching note:** stop, hold still, let go, draw back, then the other gripper takes it. Only the cases
  going to the far lane change hands.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the feed row is not set up in: a gripper reaches into a group for
  a case that is not there, the **left gripper** takes a case from the right group, the **right gripper**
  takes a case from the left group, or the cases are moved to a different order in the feed row before
  being staged.
* **SOP rule broken:** Steps 2.2 and 3.2, read which group the next case stands in and follow the IF line
  that matches.
* **Coaching note:** look at the feed row before the arm moves. One config per episode, and it never changes
  mid-episode.

**Violation: Lane count not verified**

* **Visible cue:** a gripper goes to a flag before the last case of that lane is on its spot; a flag is
  flipped while a spot in that lane is empty, while a case of that route is still in the feed row or on the
  relay spot, while a case on the lane sits on a line or on the wrong spot, or while a case of the other
  route stands on the lane; or a lane is counted, a fault is seen, and the flag is flipped anyway.
* **SOP rule broken:** Steps 4.1 and 4.2, count the cases on the lane, read the labels from the head, match
  the count to the manifest, fix what is wrong, and only then flip the flag.
* **Coaching note:** count, read, match, fix, then flip. The flag says the lane is right, so make it right
  first.

**Violation: Flag not flipped or flipped wrong**

* **Visible cue:** the episode ends with a flag still lying flat; a flag is pushed part way and left
  leaning; a flag is knocked up with a wrist or a case instead of swung up by its tip; a flag is flipped by
  the wrong gripper; or a flag is flipped before both lanes are staged.
* **SOP rule broken:** Steps 4.1 and 4.2, after the lane is verified the lane's own gripper closes on the tip
  of its flag and swings it up until it stands and the catch holds.
* **Coaching note:** tip in the gripper, swing it up until it clicks. A flag half up is a lane nobody can
  read.

**Violation: Manifest card or route sign touched**

* **Visible cue:** a gripper, wrist, forearm, or case touches, moves, knocks, or covers the manifest card,
  its holder, or a route sign.
* **SOP rule broken:** Steps 1 and 4.1 to 4.2, the manifest and the signs are read from the front and never
  touched.
* **Coaching note:** the card is for reading. Nothing on the shelf edge is ever in the gripper's way if the
  reach is level.

**Violation: Wrong order of work**

* **Visible cue:** an arm touches a case before the manifest and the flags are read; a Route B case goes
  onto a lane before all three Route A cases are on their spots; a flag is flipped before both lanes are
  staged; flag B is flipped before flag A; or a Route A case is handled during Step 3 when it should have
  been staged in Step 2.
* **SOP rule broken:** Steps 1 to 4, read the deck, stage Lane A, stage Lane B, verify Lane A and flip its
  flag, then verify Lane B and flip its flag.
* **Coaching note:** the order is the task. One lane fills, then the other, then the counts.

**Violation: More than one case moved at a time**

* **Visible cue:** a gripper drags two cases together; both grippers drag different cases at the same time;
  or a gripper holds a case while the other gripper works instead of being drawn clear of the deck.
* **SOP rule broken:** Steps 2.2 to 4.2, one gripper holds one case, and while it does the other gripper is
  empty and clear of the deck.
* **Coaching note:** one case, one slide. Two at once is what puts a case on the floor.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left
  uncorrected: a case on a line, a case on the wrong spot, a case turned, a case left in the feed row, a
  flag leaning.
* **SOP rule broken:** Steps 1 to 4.2, run each check and correct what it finds by the retry written in that
  step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped, tipped, or pushed off the deck**

* **Visible cue:** a case tips over, is pushed off the front edge or an end of the deck, or lands on the
  floor; a flag is knocked flat or broken off; or an arm knocks a staged case off its spot or into another
  case.
* **SOP rule broken:** Steps 2.2 to 4.2, nothing is tipped, dropped, or knocked out of its place, and every
  gripper comes out to the front the way it went in.
* **Coaching note:** check the path before the pull, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **right gripper** touches a case in the left group, a Lane A spot, or flag A; the
  **left gripper** touches a case in the right group, a Lane B spot, or flag B; the **left gripper** goes
  right of the relay spot, or the **right gripper** goes left of it; or either arm passes in front of the
  other.
* **SOP rule broken:** Steps 2.2 to 4.2, the **left gripper** works the left group, Lane A, and flag A, the
  **right gripper** works the right group, Lane B, and flag B, and the arms meet only at the relay spot.
* **Coaching note:** left arm works the left half, right arm works the right half, and only a hand-over
  meets at the middle.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a case in the feed row or on the relay spot, a spot empty, a case
  off its spot, a lane out of lane order, a flag lying flat, an arm short of home, or a gripper not fully
  open.
* **SOP rule broken:** Step 5, confirm both lanes, the feed strip, the flags, the drops, the deck, and the
  base, then return both arms home with grippers open and stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and
never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a route label, a heavy mark, a spot number, a flag, or the manifest**, so which case
  went where, whether the heavy case led, or whether a flag was flipped cannot be judged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock
  set.
* **Faulty deck:** a top so rough or gritty that a case tips, sticks, or turns under a correct level drag.
* **Faulty flag:** a hinge that will not swing or a catch that will not hold a flag standing after a correct
  flip.
* **Damaged case:** a case that arrives burst, crushed, open, or with a label missing, peeled, or unreadable,
  or a heavy case that is no heavier than the others.
* **Deck not open:** a flag already reading STAGED, a case already on a lane, or a feed row that does not
  hold six cases with labels to the front when the episode starts.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a case
  in its group, the relay spot, a spot at the head end of a lane, or a flag tip cannot be reached without
  extending or folding the arm.

## Annotation subtasks (from SOP)

1. Read the manifest and both lane flags
2. Find the next case in the feed row
3. Drag one case out of the feed row
4. Hand one case over at the relay spot
5. Slide one case onto its lane spot
6. Count one lane against the manifest
7. Flip one lane flag to STAGED
8. Return both arms home and end the episode
