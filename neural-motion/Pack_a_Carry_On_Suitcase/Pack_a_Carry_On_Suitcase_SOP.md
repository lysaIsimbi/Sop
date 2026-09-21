# Pack a Carry-On Suitcase SOP (1x Episode: 1 Suitcase, 6 Clothing Units)

One episode packs one carry-on suitcase. Two pairs of shorts and two towels are folded one at a time in
the fold area, and two pairs of socks are stacked and folded there one pair at a time. Each towel gets
exactly **three folds**. Each pair of shorts gets exactly **two folds**. For each sock pair, one sock is stacked flat on the other and the stacked pair
gets exactly **one fold**. The sock stack is made before the fold and is not itself counted as a fold.

The case lies **open flat** at the back of the table with its hinge running front to back: the **base**
is the left half, floor up, and the **lid** is the right half, lying flat open on the tabletop to the
right of the base. Everything is packed into the base and the lid stays empty until it is closed over.

All six clothing units wait in one **garment pile** in one corner of the table, stacked in the order they
are worked so the unit on turn is always the one on top. The order never changes: **shorts 1, shorts 2,
towel 1, towel 2, sock pair 1, sock pair 2**, then the **toiletry tote**, then the **shoe tote**, then
the press, then the lid, then the zip. The clothing goes in one type per step: the two pairs of shorts in
Step 1, the two towels in Step 2, and the two sock pairs in Step 3. Each clothing unit is laid out,
folded, and laid in the base before the next one is taken off the pile. The toiletries go into the
toiletry tote one at a time and the tote goes into the base on top of the whole load; the two shoes go
into the shoe tote one at a time and the tote goes in on top of the toiletry tote. Nothing already laid
in the base is touched again except by the press.

The six finished packets lie in the base in three stacks: the two towels laid in the **left column**
along the base's left side edge, towel 2 on towel 1, in no set alignment; the two shorts stacked in the **right
column** along the hinge, shorts 2 on top of shorts 1; and the two sock pairs laid **side by side on top
of the shorts stack**, sock pair 1 on the right and sock pair 2 on the left.

The table is set up in one of four ways. Only the garment pile moves, and the toiletries, the shoes, and
the two totes follow it to the sides described below; the case and the fold area are in the same place
in all four.

* **Config L1:** the garment pile is in the front-left corner.
* **Config L2:** the garment pile is in the back-left corner, left of the case.
* **Config R1:** the garment pile is in the front-right corner.
* **Config R2:** the garment pile is in the back-right corner, right of the open lid.

Where a step depends on the setup it says so on an **IF** line. Look at the table and follow the line
that matches.

What stays constant across all sessions:

* **Pile side:** the side of the table the garment pile is on: left in Config L1 and L2, right in
  Config R1 and R2. One config per episode, chosen before recording and never changed mid-episode.
* **Supply side:** the side opposite the pile. The **toiletry spot** is midway along the supply side and
  the **shoe spot** is in the front corner of the supply side. The two totes stand on the **tote spot**
  beside the case on the pile side.
* **Same-side rule:** the gripper on the pile side takes every clothing unit off the pile and lays it in
  the fold area. The gripper on the supply side puts every toiletry and shoe into its tote while the
  pile-side gripper holds the tote open. No arm reaches across the table for a staged item.
* **Fixed roles:** everything else is the same in all four configs: the left gripper takes the left
  end of every two-gripper edge and the right gripper the right end, the right gripper makes the
  shorts' second fold, the towel's last two folds, and the sock fold against the left gripper's pin,
  the left gripper alone lays every towel packet
  in the left column and every sock packet on the shorts stack, both grippers carry every shorts
  packet and every filled tote, both press, the right gripper closes the lid while the left anchors, and the zip is
  drawn in two legs, the right gripper first and then the left.
* **Order:** shorts 1, shorts 2, towel 1, towel 2, sock pair 1, sock pair 2, toiletry tote, shoe tote,
  press, lid, zip. The pile is bare before the first toiletry is touched.

Every towel and every pair of shorts is laid out, **straightened**, and **flung** flat by both grippers
before its first fold. Socks are laid out and stacked without a fling.

The case is never lifted. It lies where it was set for the whole episode, a gripper anchors it while the
lid is closed and while the zip is drawn, and it is turned once, on the tabletop, by the right gripper's
anchor hold during the second leg of the zip. Every fold is made flat in the fold area, nothing is folded
in the air, nothing is pushed or shoved into place, the fling is the only time cloth leaves the tabletop
on purpose, and a gripper opens only over the place the item is going.

## Setup

Complete both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole tabletop: the case lying open flat at the back with the base on
   the left and the lid on the right, the fold area at the front center, the garment pile in its corner
   for this episode's config, the two totes leaning against the case on the pile side, and the toiletry
   spot and the shoe spot on the supply side.
3. The overhead camera shows the whole fold area, so every fold edge can be seen landing, and the whole
   base mouth, so every packet and both totes can be seen resting in their places, and the inside of
   each tote where it stands, so every toiletry and shoe can be seen landing in it.
4. The whole zip track is in frame end to end, with the **start stop**, the **swap corner**, and the
   **end stop** visible, and it stays in frame while the case is turned in Step 8.
5. Both arms are at home with grippers open.
6. The tabletop holds nothing except the case, the garment pile, the two totes, the toiletries, the pair
   of shoes, and robot hardware. The fold area is bare tabletop.
7. Nothing blocks the paths between the staging places, the fold area, and the base mouth.
8. The right arm reaches the whole fold area, the whole base floor, the top of the load, the lift loop
   on the lid's free edge, the top of the closed lid, the start stop and the front edge of the track as
   far as the swap corner, the tote spot on either side and the inside of each tote where it stands,
   and the two right-hand pile corners, the toiletry spot, and the shoe spot when they are on the right.
   It does not lean out or stretch to a joint limit to get there.
9. The left arm reaches the whole fold area, the whole base floor including the left column, the top of
   the load, the base's left side panel, the swap corner and the track from there to the end stop as
   the case is turned, the tote spot on either side and the inside of each tote where it stands, and
   the two left-hand pile corners, the toiletry spot, and the shoe spot when they are on the left. It
   does not lean out or stretch to a joint limit to get there.

### Materials checklist

1. One carry-on suitcase lies **open flat** on the **case spot** at the back of the tabletop, hinge
   running front to back and squared to the front edge: the base on the left with its floor up and
   empty, the lid on the right lying flat open on the tabletop, inside up and empty. Both halves rest on
   the tabletop and nothing holds the case but the tabletop it lies on.
2. The lid carries a **lift loop** stitched at the middle of its free (right) edge, standing clear of the
   shell so the right gripper can pinch it from above.
3. The zip is a single track with **one slider**, parked at the **start stop** at the front-right corner
   of the base, at the hinge end of the front edge. The slider carries a fabric loop tab big enough for
   a gripper to pinch. Once the lid is closed the track runs from the start stop along the front edge,
   up the left side edge, and along the back edge to the **end stop** at the back-right corner, and the
   slider runs the whole way in two smooth draws with no gap left in the teeth.
4. All six clothing units sit in one **garment pile** in the corner for this episode's config, stacked
   in work order from the top down: **shorts 1** on top, then **shorts 2**, then **towel 1**, then
   **towel 2**, then **sock pair 1**, then **sock pair 2** at the bottom. Each unit is one layer of
   the pile, lying on the one below it, so the unit on turn is always the one on top and lifts off
   without disturbing the layers under it.
   * **Config L1:** front-left corner
   * **Config L2:** back-left corner, left of the tote spot
   * **Config R1:** front-right corner
   * **Config R2:** back-right corner, right of the open lid and behind the tote spot
5. Each **pair of shorts** in the pile lies loose, face up or face down and turned any way, with both
   legs side by side and neither leg on top of the other. The straighten and fling in 1.2 and 1.3 lay
   it flat.
6. Each **towel** in the pile lies loosely crumpled, not spread flat. The straighten and fling in 2.2
   and 2.3 lay it flat.
7. Each **sock pair** in the pile is one layer of two matching socks lying side by side, face up, with
   cuffs at one end and toes at the other, either way round, and neither sock touching or covering its
   mate.
8. Every towel, pair of shorts, and sock is dry, clean, and free of tears and open seams. It holds a
   fold instead of springing open, and it shows no fold line from an earlier episode.
9. The **fold area** at the front center of the table is bare, clean, and dry. It is big enough that one
   spread towel lies inside it with clear tabletop all round.
10. The **toiletry tote** and the **shoe tote** stand together on the **tote spot** beside the case on
    the pile side, open side up and empty, leaning against the case's outer side and against each other:
    the shoe tote against the case and the toiletry tote leaning on the shoe tote, so the toiletry tote
    is the outer one and is taken first. Each stands with a long wall toward the case, so a short wall
    faces the robot. Each is a soft open-top tote whose walls stand up so a gripper can pinch their
    rims. Each is small enough to lie flat on top of the
    load inside the base walls, and the shoe tote is long enough for both shoes to lie inside it side by
    side.
11. The **toiletries** sit on the **toiletry spot** midway along the supply side of the table, laid in a
    row one behind the other. Each lies flat on the tabletop the long way front to back, closed, dry,
    and not touching its neighbour. Each is short enough to lie flat inside the toiletry tote, and
    together they fit inside it without standing above its walls. The same toiletries sit in the same
    places every episode.
12. One **pair of shoes** sits on the **shoe spot** in the front corner of the supply side, soles down,
    side by side and not touching, toes toward the far edge, **left shoe on the left and right shoe on
    the right**. Laces, if any, are tucked inside the shoe.
13. Before collection, confirm the whole load fits: the towel stack, the shorts stack, and the two sock
    packets lie flat in the base, the filled toiletry tote lies flat on top of them and the filled shoe
    tote flat on top of the toiletry tote without the load standing above the base walls, and the lid
    closes without being forced.

### Workspace layout

* **Case spot:** a clear area of bare tabletop at the back, centered between the two arms. It is not
  marked. The case lies open flat with the base on the left and the lid on the right, squared to the
  front edge, and lies there for the whole episode. Nothing holds it in place, no gripper ever lifts it,
  a gripper anchors it for the lid and for each leg of the zip, and the right gripper turns it on the
  tabletop during the second leg.
* **Case places:** the bare base floor is split into a **left column** along the base's left side edge
  and a **right column** along the hinge. The towels are laid in the left column, one on the other and
  in no set alignment, the shorts are
  stacked in the right column, and the two sock packets lie side by side on top of the shorts stack,
  sock pair 1 on the right and sock pair 2 on the left. The columns are not marked.
* **Fold area:** a clear area of bare tabletop at the front center, where both arms reach all of it.
  It is not marked. Every lay-out, pin, stack, fold, and stroke happens here, one clothing unit at a
  time. The bare tabletop does not hold cloth, so nothing is ever dragged across it and every edge is
  carried.
* **Garment pile:** one pile in one corner of the table: front-left (**Config L1**), back-left
  (**Config L2**), front-right (**Config R1**), or back-right (**Config R2**). One per episode. It holds
  all six clothing units in work order from the top down: shorts 1, shorts 2, towel 1, towel 2, sock
  pair 1, sock pair 2. The unit on turn is always the top layer, and the corner is bare when the episode
  ends.
* **Tote spot:** beside the case on the pile side: against the base's left side panel in Config L1 and
  L2, against the lid's right rim in Config R1 and R2. Both totes stand there open side up, leaning
  against the case and against each other, the toiletry tote outermost. Each tote is filled where it
  stands, turned so its sides face the grippers, and then carried into the base.
* **Toiletry spot:** a clear area of bare tabletop midway along the supply side, within reach of the
  supply-side arm. It holds the toiletries in a row.
* **Shoe spot:** a clear area of bare tabletop in the front corner of the supply side, within reach of
  the supply-side arm. It holds the pair of shoes.
* **Tote places:** the top of the load. The filled toiletry tote lies flat on top of the packets, and
  the filled shoe tote lies flat on top of the toiletry tote, each inside the base walls.

The garment pile and the tote spot are on the pile side, so the pile-side arm takes every clothing unit
off the pile and holds each tote open. The toiletry spot and the shoe spot are on the supply side, so the
supply-side arm puts every toiletry and every shoe into its tote. Each arm takes staged items from its
own side only, and both arms together carry each tote into the base.

### Arm assignments

* **Right gripper:** works from the right. It takes the right end of the shorts' first-fold edge and
  of the towel's first-fold edge, makes the shorts' second fold, the towel's second and third folds,
  and the sock fold on its own, may stroke any fold edge,
  presses the right half of the load, closes the lid, draws the first leg of the zip, and anchors and
  turns the case while the second leg is drawn. In Config R1 and R2 it also takes every clothing unit
  off the pile and lays it in the fold area and holds each tote open; in Config L1 and L2 it puts each toiletry and each shoe into its tote instead.
* **Left gripper:** works from the left. It takes the left end of the shorts' first-fold edge and of
  the towel's first-fold edge, pins the shorts for their second fold and the towel for its second and
  third folds, and the stacked socks for their fold, lays every towel packet in the left column and
  every sock packet on the shorts stack on its own, presses the left half of the load, anchors
  the case while the lid is closed and while the first leg of the zip is drawn, and draws the second
  leg. In Config L1 and L2 it also takes every clothing unit off the pile and lays it in the fold area
  and holds each tote open; in Config R1 and R2 it
  puts each toiletry and each shoe into its tote instead.
* **Both grippers together:** straighten and fling every towel and pair of shorts, make the shorts'
  first fold and the towel's first fold, each holding one end of the moving edge, for the towel without
  letting go between the straighten, the fling, and the fold, bring each sock to the fold area
  and stack the pair, carry each shorts packet from the fold area into the base, each taking one carry
  edge, carry each filled tote into the base, each taking one side, and press the load flat,
  each on its own half.
* In the shorts' second fold and the towel's second and third folds the left gripper pins while the
  right gripper folds, and so it is in the sock fold. The pin is not released before the working
  gripper is off the cloth.
* Wherever one gripper holds, the other works clear of it. The two grippers never crowd the same spot.

## Vocabulary

* **Case spot:** the bare tabletop the open case lies on. Nothing holds the case, so it is held square
  by an anchor whenever the lid or the zip is worked, and by nothing else at any other time.
* **Base:** the left half of the open case, the deep half with its floor up. Every packet and both totes
  go into it.
* **Lid:** the right half of the open case, lying flat on the tabletop to the right of the base, inside
  up. It is empty until it is closed over onto the base in Step 7.
* **Hinge:** the joint between the two halves, running front to back down the middle of the open case.
  The right column of the base lies along it.
* **Lift loop:** the loop at the middle of the lid's free edge. It is the only part of the lid a gripper
  ever touches.
* **Track:** the line of teeth the slider runs along once the lid is closed. It has a **start stop** at
  the front-right corner of the closed case, at the hinge end of the front edge; a **swap corner** at
  the front-left corner, where the front edge meets the left side edge; and an **end stop** at the
  back-right corner, at the hinge end of the back edge.
* **Slider** and **loop tab:** the one slider on the track, and the fabric loop on it. The loop tab is
  the only part of the zip a gripper ever touches.
* **Anchor:** a closed gripper pressed down on the case, holding it still and square on the tabletop
  while the other gripper closes the lid or draws the zip. The **left gripper anchors** on the base's
  left side panel, level with the back of the case, while the lid is closed and while the first leg of
  the zip is drawn; the **right gripper anchors** on top of the closed lid, near the hinge, while the
  second leg is drawn. An anchor never sits on an edge where the slider runs.
* **Draw:** a gripper pinching the loop tab and pulling the slider along the track in one continuous
  motion along the line of the track. The zip is drawn in two legs: the right gripper draws the **first
  leg** from the start stop along the front edge to the swap corner, and the left gripper draws the
  **second leg** from the swap corner up the left side edge and along the back edge to the end stop.
* **Turn the case:** the right gripper, anchoring on top of the closed lid, turns the whole case on the
  tabletop anticlockwise, seen from above, so the track keeps coming round to the left gripper as the
  second leg is drawn. The case slides flat on the tabletop and is never lifted or tipped. It is the
  only time the case moves.
* **Pile side:** the side of the table the garment pile is on: left in Config L1 and L2, right in
  Config R1 and R2. The **pile-side gripper** is the gripper on that side.
* **Supply side:** the side opposite the pile, where the toiletry spot and the shoe spot are. The
  **supply-side gripper** is the gripper on that side.
* **Clothing unit:** one towel, one pair of shorts, or one matched pair of socks. There are six units
  in one episode.
* **Garment pile:** the one pile that holds all six clothing units, stacked in work order with the
  unit on turn on top. Only the top layer is ever taken.
* **Fold run:** the fixed set of folds for one clothing type. The **towel fold** contains exactly
  three folds and the **shorts fold** exactly two. The **sock-pair fold** starts only after the two
  socks are stacked and contains exactly one fold. The run is set by the clothing type, never chosen
  during the episode.
* **Fold count:** the number of completed edge-over-edge fold motions in a run. Laying an item out,
  stacking one sock on another, carrying a packet, and repeating a wrongly landed fold before moving
  on do not add to the fold count.
* **Spread flat:** the unit lies square in the fold area with no part folded under and nothing outside
  the fold area. A towel shows all four edges; shorts lie sideways with the longer sides running left
  to right and both legs side by side, face up or face down; two socks lie face up and side by side with their cuffs, heels,
  and toes level.
* **Straighten:** both grippers pinch the near edge of the towel or shorts, one just in from each end,
  and draw apart gently, without lifting, until the near edge is taut and straight and the item lies
  square to the front edge of the table. The grippers stop as soon as the edge is straight and never
  pull hard enough to slide the whole item.
* **Fling:** with the same two holds on the near edge, both grippers lift the edge together so the
  whole item rises clear of the tabletop, swing it up and back toward themselves, then forward and
  down so the free edge flies out toward the far side and lands flat, and lower the near edge onto the
  tabletop. The swing is repeated as many times as it takes for the item to land flat; the number of
  swings is not limited. For shorts, both open together once the edge is resting; for a towel, both
  keep their holds and go straight into the first fold. The grippers do not let go in the air.
* **Pin:** the gripper closes, comes straight down, and presses on the cloth to hold it still. It
  stays there without moving until the step says it can lift. A pin does not squeeze the cloth between
  the fingers and it does not slide along. The left gripper pins for the shorts' second fold and the
  towel's second and third folds, and the sock-pair fold.
* **Press:** both grippers close, come straight down flat together, one on each half of the top of the
  load, hold still, and lift straight up together. It may be repeated. A press does not slide, rub,
  pinch, or shove.
* **Stroke:** the gripper closes, presses down, and runs along in one smooth line from one end of the
  new fold edge to the other, staying in contact the whole way. It never lifts off in the middle. The
  stroke is optional after every fold: the right gripper may stroke or not, and an unstroked fold is
  not a violation.
* **Fold:** the moving edge is pinched, lifted clear of the cloth under it, carried across, lowered
  onto the edge it is going to, and released. For the shorts' first fold and the towel's first fold
  **both grippers** take the moving edge, one near each end, just in from the corner, and they lift,
  carry, lower, and open together so the edge stays straight and level the whole way. For the shorts'
  second fold and the towel's second and third folds the **right gripper** takes the moving edge at
  its middle while the left gripper pins, and for the sock pair the right gripper takes the right end of
  both socks together while the left gripper pins. Nothing is ever folded by
  pushing it along the tabletop.
* **Stack:** one sock lifted whole with both grippers and laid directly on top of its mate, cuff on
  cuff, heel on heel, side on side, and toe on toe. A stack is not a fold and does not count as the
  sock pair's one fold.
* **Towel fold:** three folds in this order: near edge to far edge, made by both grippers straight
  out of the fling without letting go; right edge to left edge; right edge to left edge again, the
  second and third made by the right gripper alone while the left gripper pins.
* **Longer sides of the shorts:** the two outside edges running from the waistband to the leg
  openings. With the shorts sideways in the fold area, one longer side lies at the near edge and the
  other at the far edge. The near longer side is carried onto the far longer side for the first fold.
* **Shorter sides of the shorts:** the waistband and the leg openings, one at the left and one at the
  right; which is which does not matter. The right shorter side is carried onto the left shorter side
  for the second fold.
* **Shorts fold:** two folds in this order: near longer side onto the far longer side, made by both
  grippers; right shorter side over to the left shorter side, made by the right gripper alone while
  the left gripper pins the left shorter side.
* **Sock-pair fold:** after the socks are stacked, the right end of the stacked pair, cuffs or toes
  whichever lies at the right, is carried over to the left end. The cuffs stay flat and are never
  rolled around the packet.
* **Packet:** one clothing unit once its fold run is done. It is a squared block of layers that lies
  flat in its place in the base.
* **Carry edges:** the two opposite long edges of a finished shorts packet, one taken by each gripper
  for the carry into the base. A towel packet and a sock packet are carried by the left gripper alone,
  pinched through every layer at the middle of its closed edge: the near edge of the towel packet,
  made by the towel's first fold, and the right edge of the sock packet, made by its one fold.
* **Lift clear:** raise the item straight up until there is daylight under it, before anything moves
  sideways.
* **Load:** carrying an item level to its place, lowering it straight down until it is resting, and
  letting go.
* **The load:** all six packets lying in the base in their stacks, with the filled toiletry tote on
  top of them and the filled shoe tote on top of the toiletry tote once Steps 4 and 5 are done.
* **Tote:** a soft open-top fabric box with a stiff flat base and four walls, called its **sides**. The
  toiletry tote and the shoe tote are the same shape. A tote is only ever taken by the rim of a side:
  the **near side** is the wall facing the robot where the tote stands, and the **left side** and
  **right side** are the walls facing each gripper after the turn. It is carried level with its open
  side up.
* **Turn the tote:** the gripper holding the near side turns the tote a quarter turn on the tote spot
  toward its own side, standing it upright and clear of the case, so the wall it holds faces it and the
  opposite wall faces the other gripper. The gripper does not let go: the tote never stands on its own
  between the turn and the lift. The tote is not lifted or dragged in the turn.
* **Toiletries:** the closed items in the row on the toiletry spot. Each is taken by its middle and
  laid flat inside the toiletry tote.
* **Hold open:** the pile-side gripper pinches the rim of a tote's near side where the tote stands on the tote
  spot and holds it upright and still, without lifting the tote or dragging it, so the tote mouth stays
  open while the supply-side gripper loads it. The hold does not release until the loading gripper is
  out of the tote.
* **Settled:** the item stays put when the gripper lifts clear, with nothing sliding, falling over, or
  springing open.
* **Release point:** over the fold area, the packet's place in the base, the inside of a tote, or a
  tote place on the load, once the item is already resting. A gripper opens nowhere else.

## Steps

Steps 1 to 3 pack the clothing one type at a time, each step run twice, and only 1.1, 2.1, and the tote
fills in 4.1 and 5.1 depend on the config: the **pile-side gripper** takes each unit off the pile (left
in Config L1 and L2, right in Config R1 and R2), and the **supply-side gripper** puts the toiletries and
shoes in while the pile-side gripper holds the tote open. Every other line is the same in all four
configs. Then run Steps 4 to 8 once, and Step 9 ends the episode.

### Step 1: Fold and pack the two pairs of shorts

**Goal:** shorts 1 and shorts 2 each laid out, straightened, flung flat, folded with exactly **two
folds**, and stacked flat in the **right column** of the base, along the hinge, shorts 2 on top of
shorts 1.

Run 1.1 to 1.6 for **shorts 1**, then run 1.1 to 1.6 again for **shorts 2**. Shorts 1 is lying in the
base before shorts 2 is taken off the pile. After shorts 2 is in the base, go on to Step 2.

#### 1.1 Lay the shorts out

* **IF the pile is on the left (Config L1 or L2):** the **left gripper** closes on the top layer of the
  garment pile, the next pair of shorts, anywhere on it. **IF the pile is on the
  right (Config R1 or R2):** the **right gripper** closes on it the same way.
* The pile-side gripper lifts the shorts straight up clear of the pile, carries them level to the fold
  area, and lowers them **sideways**, so the two longer sides run left to right with one at the near
  edge and one at the far edge, and both legs side by side. Face up or face down, and which end the
  waistband is at, do not matter.
* The pile-side gripper opens once the shorts are resting, and lifts away.

Take only the top layer of the pile. Never pull a unit out from under another, and never lift or slide
the layers below. The fling in 1.3 is the only time cloth is moved through the air on purpose.

#### 1.2 Straighten the shorts

* The **left gripper** pinches the near longer side just in from its left end, and the **right
  gripper** pinches it just in from its right end.
* Both grippers **straighten** the shorts: they draw apart gently along the line of the edge, without
  lifting, until the near longer side is taut and straight and the shorts are square to the front edge
  of the table. They keep their holds.

#### 1.3 Fling the shorts flat

* With the same two holds, both grippers **fling** the shorts: they lift the near longer side together
  so the whole pair rises clear, swing it up and back, then forward and down so the free edge flies out
  toward the far side and lands flat, swinging again as many times as it takes, and lower the near
  longer side onto the tabletop inside the fold area.
* Both grippers open together once the near edge is resting, and lift away.

If the shorts land crooked, bunched, outside the fold
area, or with a leg folded under, both grippers take the same two holds on the near longer side and
straighten and fling them again. Nothing is pulled, patted, or pushed flat by hand.

**Check:** the shorts lie **spread flat** and square inside the fold area, sideways with the longer
sides running left to right and both legs side by side. They have been straightened and flung and the
near longer side lies straight. The rest of the garment pile is
undisturbed.

#### 1.4 Fold 1 of 2: near longer side onto the far longer side

* The **left gripper** pinches the near longer side just in from its left end, and the **right
  gripper** pinches it just in from its right end.
* Both grippers lift the edge clear together, carry it toward the far edge level and straight, and
  lower it on top of the other side so the near longer side lands level with the far longer side. Both
  open together once the panel is resting.
* The **right gripper** may close and **stroke** the new fold edge, at the near side, from left to
  right. The stroke is optional on the shorts.
* Both grippers lift away.

#### 1.5 Fold 2 of 2: right shorter side over to the left shorter side

* The **left gripper** closes and **pins** the shorts just in from the left shorter side, at the middle
  of that side. It holds there for the whole fold.
* The **right gripper** pinches the right shorter side at its middle, lifts it clear of the cloth under
  it, carries it across to the left level and straight, and lowers it until the right shorter side
  lands level with the left shorter side. It opens once the panel is resting.
* The **right gripper** may close and **stroke** the second fold edge, at the right side, from its far
  end to its near end. The stroke is optional on the shorts.
* Both grippers lift away.

**Check:** the shorts have exactly two folds. The near longer side landed on top of the far longer side,
the right shorter side landed level with the left shorter side, and neither leg, the crotch panel, nor
the waistband projects outside the squared packet.

#### 1.6 Stack the shorts packet in the right column of the base

* Each gripper pinches its own **carry edge** of the shorts packet halfway along its length.
* Both grippers lift the packet level off the tabletop, carry it level to the base, and lower it
  straight down into the **right column**, along the hinge: **shorts 1** flat on the base floor,
  **shorts 2** flat on top of shorts 1, square with it, edge on edge. They open together once it is
  resting.
* Both grippers lift away.
* After shorts 1, go back to 1.1 for shorts 2. After shorts 2, go on to Step 2.

**Check:** the packet lies flat and settled in the right column of the base, inside the base walls, no
part against or over a base wall or the hinge, and no layer sprung open. Shorts 2 lies square on top of
shorts 1 with no edge hanging off it. The fold area is bare before the next unit is taken. After shorts
2, the top of the garment pile is towel 1 and the shorts stack lies in the right column of the base.

If a packet landed crooked, off the right column, off the packet under it, or with a layer open, both
grippers take the same two carry edges, lift it clear, and lay it down again.

### Step 2: Fold and pack the two towels

**Goal:** towel 1 and towel 2 each laid out, straightened, flung flat, and folded with exactly **three
folds**, the first straight out of the fling without letting go, then two right-to-left folds by the
right gripper against the left gripper's pin, and laid in the **left column** of the base, along its
left side edge, towel 2 on towel 1.

Run 2.1 to 2.7 for **towel 1**, then run 2.1 to 2.7 again for **towel 2**. Towel 1 is lying in the base
before towel 2 is taken off the pile. After towel 2 is in the base, go on to Step 3.

#### 2.1 Lay the towel out

* **IF the pile is on the left (Config L1 or L2):** the **left gripper** closes on the top layer of the
  garment pile, the next towel, anywhere on it. **IF the pile is on the right (Config
  R1 or R2):** the **right gripper** closes on it the same way.
* The pile-side gripper lifts the towel straight up clear of the pile, carries it level to the fold
  area, and lowers it with its long edges running front to back.
* The pile-side gripper opens once the towel is resting, and lifts away.

Take only the top layer of the pile. Never pull a unit out from under another, and never lift or slide
the layers below. The fling in 2.3 is the only time cloth is moved through the air on purpose.

#### 2.2 Straighten the towel

* The **left gripper** pinches the near edge of the towel just in from its left end, and the **right
  gripper** pinches it just in from its right end.
* Both grippers **straighten** the towel: they draw apart gently along the line of the edge, without
  lifting, until the near edge is taut and straight and the towel is square to the front edge of the
  table. They keep their holds.

#### 2.3 Fling the towel flat

* With the same two holds, both grippers **fling** the towel: they lift the near edge together so the
  whole towel rises clear, swing it up and back, then forward and down so the free edge flies out
  toward the far side and lands flat, swinging again as many times as it takes, and lower the near
  edge onto the tabletop inside the fold area.
* Both grippers keep their holds on the near edge. They do not open, and they go straight on into 2.4.

If the towel lands crooked, bunched, outside the fold area, or
with a corner folded under, both grippers, still holding, straighten and fling it again. Nothing is
pulled, patted, or pushed flat by hand.

**Check:** the towel lies **spread flat** and square inside the fold area, showing all four edges, with
its long edges front to back, and both grippers still hold its near edge. It has been straightened and
flung and its near edge lies straight. The rest of the garment pile is undisturbed.

#### 2.4 Fold 1 of 3: near edge to far edge, without letting go

* With the same two holds from the straighten and the fling, both grippers lift the near edge clear
  together, carry it toward the far side level and straight, and lower it until the near edge lands
  level with the far edge. Both open together once the panel is resting.
* Both grippers lift away.

The straighten, the fling, and this first fold are one continuous hold: the towel is not released, and
neither gripper regrips, between the moment the near edge is first pinched in 2.2 and the moment the
near edge is resting on the far edge.

#### 2.5 Fold 2 of 3: right edge to left edge

* The **left gripper** closes and **pins** the towel just in from its left edge, at the middle of that
  edge. It holds there for the whole fold.
* The **right gripper** pinches the right edge at its middle, lifts it clear of the cloth under it,
  carries it across to the left level and straight, and lowers it until the right edge lands level with
  the left edge. It opens once the panel is resting.
* Both grippers lift away.

#### 2.6 Fold 3 of 3: right edge to left edge again

* The **left gripper** closes and **pins** the folded towel just in from its left edge, at the middle
  of that edge. It holds there for the whole fold.
* The **right gripper** pinches the new right edge at its middle, lifts it clear, carries it across to
  the left level and straight, and lowers it until it lands level with the left edge. It opens once the
  panel is resting.
* The **right gripper** may close and **stroke** the third fold edge, at the right side, from the far
  end to the near end. The stroke is optional.
* Both grippers lift away.

**Check:** the towel has exactly three folds. Each landed edge lies level with its target edge, and the
packet is one squared block of layers with no corner misaligned and no layer sprung open.

#### 2.7 Lay the towel packet in the left column of the base

* The **left gripper** pinches the towel packet through every layer at the middle of its near edge, the
  closed edge made by the first fold.
* The **left gripper** lifts the packet off the tabletop, carries it to the base, and lowers it into the
  **left column**, along the base's left side edge: **towel 1** on the base floor, **towel 2** on
  towel 1.
* The left gripper lifts away. The right gripper stays clear of the base for the whole substep.
* After towel 1, go back to 2.1 for towel 2. After towel 2, go on to Step 3.

**Check:** the packet lies settled in the left column of the base, inside the base walls, not on the
shorts stack, and with no layer sprung open. The fold area is bare before the next unit is taken. After towel 2, the top of the garment pile is sock pair 1, the shorts stack lies in the right
column, and the towel stack lies in the left column.

If a packet landed off the left column, on the shorts stack, or with a layer open, the left gripper
takes the same hold, lifts it clear, and lays it down again.

### Step 3: Stack, fold, and pack the two sock pairs

**Goal:** sock pair 1 and sock pair 2 each brought to the fold area, stacked, folded with exactly **one
fold**, and lying flat **side by side on top of the shorts stack**, sock pair 1 on the right and sock
pair 2 on the left.

Run 3.1 to 3.4 for **sock pair 1**, then run 3.1 to 3.4 again for **sock pair 2**. Sock pair 1 is lying
in the base before sock pair 2 is taken off the pile. Socks are laid out and stacked without a
straighten or a fling. After sock pair 2 is in the base, go on to Step 4.

#### 3.1 Bring the first sock to the middle and square it

* Choose any pair of socks to begin.
* With both grippers, take any one sock of the chosen pair from its initial position. **IF the pile is
  in a back corner (Config L2 or R2):** the pile-side gripper takes the sock alone, lifts it clear of
  the pile, and holds it still over the tabletop; the other gripper then takes the other end of the
  sock, and only then do both carry it.
* Carry it level to the middle of the work area using both grippers.
* Lay it flat on the table in the middle and square it so its body, cuff, and toe lie flat and aligned.
* Both grippers release and lift clear.

#### 3.2 Stack its matching mate directly on top

* With both grippers, take the matching mate of the chosen pair, the same way as the first sock: in
  Config L2 or R2 the pile-side gripper lifts it first and the other gripper takes the other end.
* Carry the mate level directly over the first sock lying in the middle.
* Lower it straight down and lay it flat on top of the base sock, matching its orientation.
* Square the pair in the middle so the edges, cuffs, and toes align flush.
* Both grippers release and lift clear.
* **Check:** The two socks form one flat, neat, aligned two-layer pair squared in the middle of the work
  zone.

Take both socks from the top layer of the pile only, and finish that layer before the next one is
uncovered. Never mix the two sock pairs, never lift or slide the layer below, and never straighten or
fling a sock. This action is a **stack**, not a fold. Do not count it as the sock pair's fold, roll one
cuff over the other, or tuck either sock inside its mate.

#### 3.3 Fold 1 of 1: right end over to the left end

The stacked pair lies with its cuffs at one end and its toes at the other, one end at the left and one
at the right. Which end is which does not matter.

* The **left gripper** closes and **pins** the stacked pair just in from its left end. It holds there
  for the whole fold.
* The **right gripper** pinches the right end of both socks together, lifts it clear, carries it across
  to the left level and straight, and lowers it until the right end lands level with the left end. It
  opens once the panel is resting.
* The **right gripper** may close and **stroke** the new fold edge, at the right side. The stroke is
  optional.
* Both grippers lift away.

There is one fold and only one. The cuffs stay flat and are not rolled over the packet, and the packet
is not folded again.

**Check:** the two socks were stacked before folding and the stack has exactly one fold. The socks stay
aligned, the right end lies level with the left end, the cuffs remain unrolled, and no heel, toe, or
cuff projects outside the packet.

#### 3.4 Lay the sock packet on top of the shorts stack

* The **left gripper** pinches the sock packet through every layer at the middle of its right edge, the
  closed edge made by the fold.
* The **left gripper** lifts the packet level off the tabletop, carries it level to the base, and lowers
  it straight down onto the **top of the shorts stack** in the right column: **sock pair 1** on the
  **right half** of the shorts stack, **sock pair 2** on the **left half**, beside sock pair 1 and not
  on it. It opens once the packet is resting.
* The left gripper lifts away. The right gripper stays clear of the base for the whole substep.
* After sock pair 1, go back to 3.1 for sock pair 2. After sock pair 2, go on to Step 4.

**Check:** the packet lies flat and settled on top of the shorts stack, on its own side, not hanging off
the shorts, not on the towel stack, not against a base wall, and with no layer sprung open. After sock
pair 2, the garment pile and the fold area are bare, and the load lies in the base as the towel stack in
the left column and the shorts stack in the right column with the two sock packets side by side on it.

If a packet landed crooked, off the shorts stack, on the other sock packet, or with a layer open, the
left gripper takes the same hold, lifts it clear, and lays it down again.

### Step 4: Fill the toiletry tote and load it

**Goal:** every toiletry lying in the toiletry tote, and the tote lying flat on top of the whole load.

The toiletry tote is filled where it stands on the tote spot, leaning against the shoe tote. The
pile-side gripper holds it open for the whole fill and the supply-side gripper puts the toiletries in
one at a time. Then the tote is turned so its sides face the grippers and carried into the base by both.

#### 4.1 Put the toiletries in

* **IF the pile is on the left (Config L1 or L2):** the **left gripper** pinches the rim of the toiletry
  tote's **near side** and **holds the tote open**, and the **right gripper** loads it. **IF the pile is on
  the right (Config R1 or R2):** the **right gripper** holds the tote open and the **left gripper**
  loads it.
* The holding gripper keeps the tote upright and still on the tote spot for the whole substep.
* The loading gripper closes on the nearest toiletry on the toiletry spot at its middle, lifts it
  straight up clear, carries it level over the tote, lowers it into the tote until it rests flat on the
  tote base, and opens.
* The loading gripper takes the next toiletry the same way and lays it in the tote beside the one
  already there, and goes on one toiletry at a time until the toiletry spot is bare.
* The loading gripper lifts clear of the tote, and only then does the holding gripper open and lift
  away.

Each toiletry is lowered until it is resting before the gripper opens. Nothing is dropped into the tote
from above, a toiletry already in the tote is not pushed aside to make room for the next one, and the
holding gripper does not lift or drag the tote while holding it open.

**Check:** every toiletry lies flat in the tote, none standing up and none on top of another, and none
stands above the tote walls. The tote still stands on the tote spot, open side up, and the toiletry spot
is bare.

If a toiletry rolled over, stood up, or landed on another, the loading gripper takes it by its middle,
lifts it clear, and lays it flat in the tote again while the holding gripper keeps the tote open.

#### 4.2 Turn the toiletry tote and carry it onto the load

* The pile-side gripper pinches the rim of the tote's **near side** again and **turns the tote** a
  quarter turn on the tote spot toward its own side, standing it upright and clear of the case, so the
  wall it holds now faces it and the opposite wall faces the other gripper. It keeps its hold.
* The other gripper pinches the rim of the opposite **side** at its middle, so the **left gripper**
  holds the tote's **left side** and the **right gripper** its **right side**.
* Both grippers lift the tote level off the tote spot together, carry it level to the base, and lower
  it straight down onto the **top of the load**, long sides running front to back, until its base
  rests flat across the towel stack and the sock packets. They open together once it is resting.
* Both grippers lift away.

**Check:** the toiletry tote lies flat on top of the load, inside the base walls, open side up, with
every toiletry still lying flat in it. It does not rest on a base wall and does not stand above the base
walls. The shoe tote still stands on the tote spot, leaning against the case.

If the tote landed tilted, on a base wall, or off the load, both grippers take the same two sides, lift
it clear, and lower it again.

### Step 5: Fill the shoe tote and load it

**Goal:** both shoes lying in the shoe tote side by side, and the tote lying flat on top of the toiletry
tote.

The shoe tote is filled where it stands on the tote spot, leaning against the case. The pile-side
gripper holds it open for the whole fill and the supply-side gripper puts the shoes in, **left shoe,
then right shoe**. Then the tote is turned so its sides face the grippers and carried into the base by
both.

#### 5.1 Put the shoes in

* **IF the pile is on the left (Config L1 or L2):** the **left gripper** pinches the rim of the shoe
  tote's **near side** and **holds the tote open**, and the **right gripper** loads it. **IF the pile is on the
  right (Config R1 or R2):** the **right gripper** holds the tote open and the **left gripper** loads
  it.
* The holding gripper keeps the tote upright and still on the tote spot for the whole substep.
* The loading gripper closes on the **left shoe** on the shoe spot at the back of its heel, lifts it
  straight up clear, carries it level over the shoe tote, lowers it sole down into the **left side** of
  the tote with its toe toward the far side, until it rests on the tote base, and opens.
* The loading gripper takes the **right shoe** the same way, by the back of its heel, and lays it sole
  down in the **right side** of the tote, toe toward the far side, beside the left shoe and not on top
  of it.
* The loading gripper lifts clear of the tote, and only then does the holding gripper open and lift
  away.

Each shoe is lowered until it is resting before the gripper opens. A shoe is never dropped in, wedged in
on its side, or pushed against the other shoe.

**Check:** both shoes lie sole down in the tote, left shoe on the left and right shoe on the right, toes
toward the far side, side by side and not touching, with neither shoe on its side or on the other. The
tote still stands on the tote spot, open side up, and the shoe spot is bare.

If a shoe landed on its side, on the other shoe, or toe the wrong way, the loading gripper takes it by
the back of its heel, lifts it clear, and lays it in the tote again while the holding gripper keeps the
tote open.

#### 5.2 Turn the shoe tote and carry it onto the toiletry tote

* The pile-side gripper pinches the rim of the tote's **near side** again and **turns the tote** a
  quarter turn on the tote spot toward its own side, standing it upright and clear of the case, so the
  wall it holds now faces it and the opposite wall faces the other gripper. It keeps its hold.
* The other gripper pinches the rim of the opposite **side** at its middle, so the **left gripper**
  holds the tote's **left side** and the **right gripper** its **right side**.
* Both grippers lift the tote level off the tote spot together, carry it level to the base, and lower
  it straight down onto the **top of the toiletry tote**, long sides running front to back, square
  with the tote under it, until its base rests flat on the toiletry tote. They open together once it is
  resting.
* Both grippers lift away.

**Check:** the shoe tote lies flat on top of the toiletry tote, inside the base walls, open side up,
with both shoes still lying sole down in it. It does not hang off the toiletry tote or rest on a base
wall. The tote spot is bare.

If the tote landed tilted, on a base wall, or off the toiletry tote, both grippers take the same two
sides, lift it clear, and lower it again.

### Step 6: Press the load flat

**Goal:** the whole load, with both totes on it, pressed flat in the base by both grippers together.

* Both grippers close. The **left gripper** comes straight down flat onto the **left half** of the top
  of the shoe tote and the **right gripper** comes straight down flat onto the **right half**, at the
  same time.
* Both grippers **press** together: they hold still, then lift straight up together.
* The press may be repeated in the same way; the number of presses is not limited.
* Both grippers lift away.

A press comes straight down and holds. It never shoves sideways, never rocks, and never squashes the
load to make room for something that has not gone in yet. The two grippers come down together and lift
together so the load is pressed level, not tipped to one side.

**Check:** the load has been pressed by both grippers, once or more, both totes still lie flat and square in
their places with every toiletry and shoe still lying in its tote, every packet still lies flat in its
stack with no layer sprung open, and no part of the load stands above the base walls.

If a tote shifted or tilted under the press, both grippers take its two sides, lift it clear, and lower
it again. If a toiletry or shoe left its place, the supply-side gripper takes it by the same hold and
lays it in its tote again.

### Step 7: Close the lid

**Goal:** the lid down flat on the base, meeting the base all round.

* The **left gripper**, closed, **anchors** the case on the base's **left side panel**, level with the
  back of the case, and holds it there for the whole step.
* The **right gripper** comes down onto the **lift loop** at the middle of the lid's free edge and
  pinches it.
* The **right gripper** carries the loop up off the tabletop, over the hinge, and down onto the base in
  one continuous motion, until the lid lies flat on the base. Then it opens and lifts clear.
* The **left gripper** lifts clear only once the right gripper is off the lid.

Follow the lid with the loop rather than pushing against the hinge. The loop is flexible, so the gripper
never has to turn as the lid swings.

**Check:** the lid lies flat on the base and meets it all round the front, left, and back edges, with no
towel, shorts, sock, or tote caught between the lid and the base walls. The two zip tapes lie beside each
other along the whole track, the slider is still parked at the start stop, and the case has not shifted.

If the lid will not sit down flat, or something is caught under it, the **right gripper** takes the lift
loop again, carries the lid back over the hinge and lays it flat open on the tabletop, lifts the caught
item clear, lays it down again, and closes the lid again.

### Step 8: Draw the zip shut

**Goal:** the slider at the end stop, the track joined all the way round, with nothing caught in the
teeth.

The slider starts at the start stop at the front-right corner. The **right gripper draws the first
leg**, along the front edge, until the slider gets to the **swap corner**, the left corner of the half
holding the shorts, socks, and shoes. Then the grippers swap roles: the **right gripper anchors** the
case and keeps turning it as the **left gripper draws the second leg** all the way to the end stop. One
gripper is anchoring the case the whole time.

#### 8.1 Right gripper draws the first leg to the swap corner

* The **left gripper**, closed, **anchors** the case on the base's **left side panel**, level with the
  back of the case, and holds it there for the whole substep.
* The **right gripper** comes down onto the **loop tab** at the **start stop** and pinches it.
* The **right gripper draws** the slider straight along the front edge, right to left, in one
  continuous motion, until the slider gets to the **swap corner**. It holds the tab there.
* The **left gripper** lifts off the side panel and comes round to the swap corner. Only once it is
  there does the **right gripper** open and lift clear of the tab.

#### 8.2 Left gripper draws the second leg while the right gripper turns the case

* The **right gripper**, closed, comes straight down onto the **top of the closed lid** near the hinge
  and **anchors** the case there for the whole substep.
* The **left gripper** comes down onto the **loop tab** at the swap corner and pinches it.
* The **left gripper draws** the slider up the left side edge, front to back, in one continuous motion.
  As the slider nears the back-left corner the **right gripper turns the case** on the tabletop,
  anticlockwise seen from above, keeping its hold, so the back edge comes round to the left gripper,
  and the left gripper keeps drawing along the back edge until the slider reaches the **end stop** and
  will not travel further. Then it opens and lifts clear.
* The **right gripper** lifts clear only once the left gripper is off the track.

Each draw pulls the case toward the gripper doing the drawing, and the anchor is the only thing keeping
it square. The turn is made by the anchor hold alone: the case slides flat on the tabletop and is never
lifted, tipped, or pushed by the drawing gripper.

**Check:** the slider sits at the end stop. The track is joined along its whole length, with no cloth
caught in the teeth. The lid still lies flat on the base and the case has not lifted or tipped.

If the slider stopped short, the gripper on that leg takes the loop tab again and draws it the rest of
the way. Do not force the slider against an obstruction: draw it back to the start stop, open the lid,
lift the caught item clear, lay it down again, close the lid, and draw both legs again.

### Step 9: End the episode

* Confirm the case is zipped shut with the slider at the end stop, the lid flat on the base, and the
  garment pile corner, tote spot, toiletry spot, shoe spot, and fold area all bare.
* Return both arms home with grippers open.
* Stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Draw the slider back to the start stop, open the lid over the hinge so it lies flat on the tabletop
   to the right of the base, and turn the case back square on the case spot.
2. Lift out the shoe tote, then the toiletry tote, and stand them back on the tote spot beside the case
   on the pile side for the next episode's config, open side up and a long wall toward the case: the
   shoe tote leaning against the case and the toiletry tote leaning against the shoe tote.
3. Take both shoes out of the shoe tote and set them on the shoe spot in the front corner of the supply
   side, soles down, side by side and not touching, toes toward the far edge, left shoe on the left and
   right shoe on the right. Take the toiletries out of the toiletry tote and set them in a row on the
   toiletry spot midway along the supply side, one behind the other, each flat the long way front to
   back. Check each one is closed and nothing has leaked into the tote.
4. Remove the packets in reverse order: sock pair 2, sock pair 1, towel 2, towel 1, shorts 2, shorts 1.
5. Unfold each sock pair once and separate its two socks. Smooth each sock flat so the fold from the
   last episode is gone. Unfold each towel three times and each pair of shorts twice and smooth them
   flat so no fold line from the last episode is left in the cloth.
6. Rebuild the garment pile in the corner for the next episode's config, front-left (Config L1),
   back-left (Config L2), front-right (Config R1), or back-right (Config R2), from the bottom up, so it
   reads in work order from the top down: sock pair 2 at the bottom, then sock pair 1, then towel 2,
   then towel 1, then shorts 2, then shorts 1 on top. Lay each sock pair as one layer of two socks side
   by side and face up, cuffs at one end and toes at the other, either way round, not touching. Lay each
   towel loosely crumpled, not spread flat. Lay each pair of shorts loose, turned any way, with both
   legs side by side and neither leg overlapping. Lay every layer on the one below it so the top unit
   lifts off clean.
7. Check the loop tab and the lift loop are attached, and that the slider runs freely from the start
   stop round to the end stop. Replace a zip that is starting to catch.
8. Replace anything damaged: a towel, pair of shorts, or sock that is torn, stained, damp, still shows
   an old fold, or will not hold a new fold; a tote with a torn wall or a base that will not lie
   flat; a toiletry that leaks or will not stay closed; a shoe that will not sit sole down; or a case
   that will not lie flat and square.
9. Set the case back square on the case spot, open flat with the base on the left and the lid on the
   right, and stand both totes back against it on the pile side.
10. Wipe the tabletop and leave the fold area and the three unused pile corners bare and dry.
11. Run both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The
visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation
label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain several violations; tag each one
separately. Keep the episode with its violation tags. Do not delete it just because a rule was broken.

### Violations

**Note on the start position:** the violations below were written for Config L1 (garment pile in the
front-left corner, toiletries and shoes on the right). The pickup, tote-fill, and arm-role cues will be
rewritten later to cover all four configs; they are left as they are for now. Until then, anything that
does not match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the operator does does not match the config on the table: the garment pile,
  the totes, the toiletries, or the shoes are not in the places for the config; a gripper reaches
  across the table to take a clothing unit off the pile, a toiletry, or a shoe; the supply-side gripper
  holds a tote open or the pile-side gripper loads it; or the wrong IF line is followed.
* **SOP rule broken:** the pile side, the supply side, and the same-side rule (the pile-side gripper
  takes every clothing unit off the pile and holds every tote open; the supply-side gripper puts every
  toiletry and shoe in; no arm reaches across the table for a staged item; the IF line followed is the
  one for the config on the table).
* **Coaching note:** look where the pile is before the first reach, then follow that config's IF lines
  through Steps 1, 2, 4, and 5.

**Violation: Wrong item order**

* **Visible cue:** an item is worked before the preceding item has been laid in the base; the order
  differs from shorts 1, shorts 2, towel 1, towel 2, sock pair 1, sock pair 2; number 2 of a type is
  started while number 1 is still in the fold area; a towel is taken before both shorts packets are in
  the base, or a sock pair before both towel packets are in; a toiletry or shoe is handled before all
  six packets are in; the shoe tote is filled or loaded before the toiletry tote is on the load; the
  shoes go in out of their named order; the load is pressed before both totes are on it; the lid is
  lifted before the load is pressed; the zip is drawn before the lid lies flat; or the left gripper
  takes the loop tab before the slider has reached the swap corner.
* **SOP rule broken:** Steps 1 to 8, the two pairs of shorts in Step 1, then the two towels in Step 2,
  then the two sock pairs in Step 3, each unit finished into the base before the next is taken, then
  the toiletry tote, then the shoe tote, then the press, then the lid, then the first leg of the zip,
  then the second leg, in that order and no other.
* **Coaching note:** finish what you are on, all the way into the base, before you start the next
  thing.

**Violation: Item dug out of the pile or pair mixed**

* **Visible cue:** a gripper works a unit out from under the top layer of the garment pile, slides one
  sideways out of the pile, lifts the upper layers to get at a lower one, shakes cloth open on the way
  from the pile, takes one sock from a layer and leaves its mate, or combines one sock from each pair.
* **SOP rule broken:** Steps 1.1, 2.1, and 3.1, only the top layer of the garment pile is taken and
  the two socks of one layer stay together as one pair.
* **Coaching note:** top of the pile only, and finish one sock layer before uncovering the next.

**Violation: Clothing not spread flat before folding**

* **Visible cue:** folding or stacking begins with cloth crooked, bunched, turned the wrong way,
  folded under itself, outside the fold area, with one shorts leg on the other, with the shorts not
  sideways, or with either sock not flat.
* **SOP rule broken:** Steps 1.1 to 1.3, 2.1 to 2.3, and 3.1, every clothing unit lies spread flat in
  its prescribed orientation before the fold run or stack begins.
* **Coaching note:** lay it out properly first. A bad lay-out makes every fold after it crooked.

**Violation: Straighten or fling skipped or done wrong**

* **Visible cue:** a towel or pair of shorts goes into its first fold without being straightened and
  flung; the straighten lifts the item or slides it whole; the fling is made by one gripper, with the
  holds anywhere but the two ends of the near edge, or with a hold released in the air; the fling lands
  the item outside the fold area and it is not flung again;
  a towel is released or regripped between the straighten, the fling, and its first fold; or a sock is
  straightened or flung.
* **SOP rule broken:** Steps 1.2, 1.3, and 2.2 to 2.4, both grippers straighten the near edge without
  lifting, then fling with as many swings as it takes and lower the near edge, for every pair of shorts
  and every towel and for nothing else, and for a towel keep the same holds through the first fold.
* **Coaching note:** two holds on the near edge, pull it straight, swing until it lands flat, lay it
  down. Socks are never flung.

**Violation: Wrong number of folds**

* **Visible cue:** a towel receives fewer or more than three folds; a pair of shorts receives fewer or
  more than two folds; a sock pair receives no fold or more than one fold; or folding continues after
  the prescribed packet is formed.
* **SOP rule broken:** Steps 1.4 and 1.5 require exactly two folds per shorts, Steps 2.4 to 2.6
  exactly three folds per towel, and Step 3.3 exactly one fold per stacked sock pair.
* **Coaching note:** count the fold as its moving edge lands: three for a towel, two for shorts, one
  after the socks are stacked.

**Violation: Wrong fold run for the clothing type**

* **Visible cue:** a towel is given the two-fold shorts run; shorts are given a third fold or are
  folded without first laying the near longer side on top of the far longer side; socks are given the
  towel or shorts run; or the correct count is reached with the wrong moving edges or landing edges.
* **SOP rule broken:** Steps 1 to 3, each clothing type has its own step, its own fixed run, and its
  own fixed sequence.
* **Coaching note:** name the clothing type before the first fold. The type picks the run.

**Violation: Sock stack and fold out of order**

* **Visible cue:** either sock is folded alone; the end-over-end fold starts while the socks remain
  side by side; one sock is tucked into the other instead of being laid on top; or the aligned sock
  stack is loaded without its right end ever being brought to its left end.
* **SOP rule broken:** Steps 3.1 to 3.3, the two socks are stacked and aligned first, and then the
  stacked pair gets its one right-over-left fold before it is carried.
* **Coaching note:** the stack makes the pair; the right-over-left motion is the fold. Stack first, then
  fold, then carry.

**Violation: Wrong fold direction or landing**

* **Visible cue:** a prescribed edge moves in the opposite direction, corresponding edges do not meet,
  the longer shorts sides do not meet on Fold 1, the shorts' second fold or a towel's second or third
  fold moves left to right instead of right to left, the towel's first fold moves any edge but the
  near edge, the sock fold moves left to right or its ends do not meet, or a loose part projects
  outside the finished packet.
* **SOP rule broken:** Steps 1 to 3 define the moving edge and its landing for every fold.
* **Coaching note:** line the moving edge up with its named landing edge before you let go.

**Violation: Edge carried by the wrong number of grippers, or fold without a pin**

* **Visible cue:** the shorts' first-fold edge or the towel's first-fold edge is lifted, carried, or
  laid down by one gripper alone; the two grippers lift or open at different times so the edge lands
  twisted or one corner short; the shorts' second fold or the towel's second or third fold is made with
  both grippers, or by the left gripper; the sock fold is made with both grippers, or by the left
  gripper; or in any pinned fold the cloth under the moving edge shifts because the left gripper did
  not pin it, or the pin releases before the right gripper clears the cloth.
* **SOP rule broken:** Steps 1 to 3, the first fold of the shorts and of the towel is carried by both
  grippers together, one at each end, and every later fold, the sock fold included, is made by the
  right gripper against a held left pin.
* **Coaching note:** two hands on the first fold, lift together and let go together. After that, left
  pins first and lets go last while the right hand folds.

**Violation: Sock stack misaligned or rolled**

* **Visible cue:** the upper sock does not cover the lower sock cuff to toe, the upper sock is slid
  into place instead of lifted and relaid, one sock is tucked inside the other, or a cuff is rolled
  over the finished packet.
* **SOP rule broken:** Steps 3.2 and 3.3, one whole sock is laid directly on the other, the stack is
  aligned before its one fold, and both cuffs remain flat.
* **Coaching note:** sock on sock, edge on edge. No tuck and no cuff roll.

**Violation: Packet carried or released incorrectly**

* **Visible cue:** one gripper carries a shorts packet alone; a towel packet or a sock packet is
  carried by the right gripper or by both grippers, or taken anywhere but the middle of its near
  edge; a shorts packet tilts or opens in transit; or any packet is dropped into the base from above.
* **SOP rule broken:** Step 1.6 requires both grippers to carry the shorts packet level, lower it until
  resting, and release together; Steps 2.7 and 3.4 require the left gripper alone to carry the towel
  packet and the sock packet by the near edge and lower it until resting.
* **Coaching note:** shorts, one hold each side; towels and socks, the left hand only. Keep it level,
  all the way down, then let go.

**Violation: Packet loaded in the wrong place**

* **Visible cue:** a towel packet is laid anywhere but the left column of the base; a shorts packet is laid anywhere but the right column, or not square on the
  shorts under it; a sock packet is laid anywhere but on top of the shorts stack, on the wrong side, or
  on the other sock packet; any packet is laid in the lid; or any packet rests against or over a base
  wall or hangs off the packet under it.
* **SOP rule broken:** Steps 1.6, 2.7, and 3.4, towels are laid in the left column, shorts in the
  right column along the hinge, and the sock pairs lie side by side on the shorts stack, sock pair 1
  right and sock pair 2 left.
* **Coaching note:** towels left, shorts right, socks on the shorts. Same three stacks every episode,
  and nothing in the lid.

**Violation: Contents forced or rearranged**

* **Visible cue:** an already loaded packet, tote, toiletry, or shoe is shoved, compressed, slid, or
  moved to make room for the next item.
* **SOP rule broken:** Steps 1 to 6, each packet, toiletry, shoe, and tote must fit its place and is
  not touched again after placement except by the press.
* **Coaching note:** lift it and lay it again. If it does not fit, that is data; forcing it is not.

**Violation: Toiletry or shoe put in wrong**

* **Visible cue:** a toiletry lands standing up or on top of another; a tote is loaded while the left
  gripper is not holding it open, or the left gripper lifts, drags, or releases the tote before the
  right gripper is out of it; a shoe lands on the wrong side of the tote, on its side, on the other
  shoe, or toe toward the near side; an item is dropped into a tote from above instead of lowered
  until resting; or a toiletry or shoe goes into the wrong tote.
* **SOP rule broken:** Steps 4.1 and 5.1, the left gripper holds the tote open for the whole fill, and
  the right gripper lowers each toiletry flat into the toiletry tote and each shoe sole down into its
  side of the shoe tote, left shoe then right shoe, until it rests, and only then releases.
* **Coaching note:** left holds the tote open, right loads. One item at a time, lowered all the way
  in. Left shoe, then right shoe.

**Violation: Tote carried or set down wrong**

* **Visible cue:** a tote is lifted without first being turned so its sides face the grippers, is
  lifted or dragged during the turn, or is let go between the turn and the lift; a tote is carried by one gripper, tilted or swung in the carry,
  set down on the base floor or beside the load instead of on top of it, the shoe tote set down
  anywhere but on the toiletry tote, a tote set down on a base wall or in the lid, dropped the last
  part of the way, or released before its base is resting.
* **SOP rule broken:** Steps 4.2 and 5.2, the tote is turned by its near side, then both grippers
  carry it level by its two sides and lower it straight down until its base rests flat, the toiletry
  tote on top of the load and the shoe tote on top of the toiletry tote, and open together.
* **Coaching note:** turn it, one side each, keep it level, all the way down onto the top of the load,
  then let go together. Toiletries on the clothes, shoes on the toiletries.

**Violation: Press skipped, one-handed, dabbed, or shoved**

* **Visible cue:** the load is not pressed at all, only one gripper presses, the two grippers come
  down or lift at different times so the load tips, the press lands beside the shoe tote instead of on
  it, a gripper taps or dabs instead of coming down flat and holding, the press slides sideways or
  rocks, or the press is used to make room for something that has not gone in yet.
* **SOP rule broken:** Step 6, at least one flat press by both grippers together, one on each half of
  the top of the load, held still and lifted straight up together, and never shoved sideways.
* **Coaching note:** both hands down flat together, hold, straight up together.

**Violation: Lid forced or dropped**

* **Visible cue:** the lid is pushed by its shell, released before it rests, or pressed down on cloth
  caught between lid and base.
* **SOP rule broken:** Step 7, the right gripper carries the lift loop until the lid lies flat, and a
  caught item is cleared before closing again.
* **Coaching note:** carry the loop the whole way and look at the rim before letting go.

**Violation: Zip drawn wrong or left short**

* **Visible cue:** the slider is pulled off the line of the track, drawn in an arc or in the wrong
  direction, forced against an obstruction, or left short of the end stop; the right gripper draws
  past the swap corner, or the left gripper draws the front edge; the tab is let go at the swap corner
  before the left gripper is there to take it; or the second leg is drawn without the case being
  turned so that the track comes to the left gripper.
* **SOP rule broken:** Step 8, the right gripper draws the first leg from the start stop to the swap
  corner, the grippers swap roles there, and the left gripper draws the second leg to the end stop
  while the right gripper anchors and turns the case.
* **Coaching note:** front edge right hand, the rest left hand, tab down on the teeth and moving. Look
  at the end stop before moving on.

**Violation: Case moved or not anchored**

* **Visible cue:** the case slides, rotates, tips, or lifts at any time other than the turn during the
  second leg of the zip; the lid or a leg of the zip is worked without the other gripper holding the
  prescribed anchor; the anchor sits on an edge where the slider runs; or the case is turned by
  anything other than the right gripper's anchor hold on the lid.
* **SOP rule broken:** Steps 7 and 8, the case lies on its spot, is anchored during lid closure and
  both legs of the zip, and is turned only by the right gripper's anchor during the second leg.
* **Coaching note:** anchor first, then work. The anchor turns the case; nothing else moves it.

**Violation: Item dragged, folded in the air, or regripped in the air**

* **Visible cue:** cloth or a packet slides along the tabletop or base floor with no daylight under
  it; a fold edge is pushed across the cloth instead of being lifted and laid down; a fold is completed
  while the item is suspended; an item is flipped, swung, or shaken during a carry or anywhere other
  than the one fling in Step 1.3 or 2.3; a clothing unit or packet is turned or flipped in the air; or
  a gripper shifts its hold without setting the item down first.
* **SOP rule broken:** Steps 1 to 8, every fold is made flat in the fold area, every item and edge is
  lifted clear before moving sideways, kept in its picked orientation, and set down before a new hold
  is taken.
* **Coaching note:** up first, then across, then down. Nothing gets pushed, and a new hold is taken
  only after setting it down.

**Violation: Arms swapped roles or crowded the same spot**

* **Visible cue:** the right gripper takes a clothing unit off the garment pile; a towel is taken off
  the pile, or a towel or sock packet carried into the base, by both grippers; the left gripper takes
  the right end of a moving edge, makes a towel's second or third fold or the sock fold, strokes a
  fold edge, puts a toiletry or a shoe into a tote, closes the lid, or draws the first leg of the zip;
  the right gripper takes the left end of a moving edge, pins the shorts, the towel, or the socks,
  carries a towel or sock packet, holds a tote open, or draws the second leg of the zip; a tote is carried by one gripper or with the sides swapped; the load is pressed by
  one gripper; or the grippers touch or block each other.
* **SOP rule broken:** Steps 1 to 8, the arm assignments fix every pick, fold, carry, tote fill, press,
  lid, and zip action.
* **Coaching note:** left takes every unit off the pile and holds each tote open; right puts every
  toiletry and shoe in. Each gripper holds its own end of every towel and shorts edge, its own tote
  side, and its own half of the press.

**Violation: Item dropped or something knocked over**

* **Visible cue:** cloth, a packet, a toiletry, a shoe, or a tote falls onto the table or floor; a
  gripper strikes the case or a tote; the garment pile, a tote on the tote spot, or a toiletry is
  knocked over; an already placed packet or tote is dragged out of place; or the arms strike each other.
* **SOP rule broken:** Steps 1 to 8, every item follows a clear path and a gripper opens only over a
  settled placement.
* **Coaching note:** check the path and the landing spot before you move.

**Violation: Wrong episode ending**

* **Visible cue:** a staging item remains, the fold area is not bare, the suitcase is not fully zipped,
  the slider is short of the end stop, either arm is away from home, or a gripper remains closed.
* **SOP rule broken:** Step 9, confirm the zipped case and bare staging places, return both arms home
  with grippers open, then stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

These failures are not caused by how the task was run. Log them as system issues, discard the episode,
and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller-caused collision, or motor error.
* **Zip jammed or the slider derailed** under a straight draw along the track. Replace the case before
  the next episode.
* **The loop tab or the lift loop missing or torn off** when the step begins.
* **Lid will not lie flat open** and swings back onto the base under its own weight before Step 7.
  Replace the case before the next episode.
* **Defective clothing:** a towel, pair of shorts, or sock that comes apart in the gripper, is damp or
  strongly pre-creased, or will not hold a fold after its edge is stroked end to end.
* **Clothing too big for the fold area:** a spread towel, pair of shorts, or two socks cannot lie
  inside the fold area with clear tabletop all round.
* **Load will not fit:** the towel stack, shorts stack, and two sock packets cannot lie flat in the
  base, the two filled totes cannot lie flat on top of the load inside the base walls, or the lid will
  not close without being forced.
* **Tote or contents defective:** a tote wall tears, a tote base will not lie flat, a
  toiletry leaks or comes open in the gripper, or a shoe will not sit sole down. Replace it before the
  next episode.
* **Case will not lie still:** it will not lie flat and square on the tabletop, or it rocks or creeps
  on its own before any gripper touches it.

## Annotation subtasks (from SOP)

1. Take one pair of shorts off the garment pile and lay it out
2. Straighten and fling one pair of shorts flat
3. Fold the near longer side of the shorts onto the far longer side with both grippers
4. Fold the right shorter side of the shorts over to the left against the left pin
5. Carry one shorts packet into the right column of the base
6. Take one towel off the garment pile and lay it out
7. Straighten and fling one towel and fold its near edge to its far edge without letting go
8. Fold the towel's right edge to its left edge against the left pin
9. Carry one towel packet into the left column of the base with the left gripper
10. Bring one sock to the middle and square it
11. Stack its mate on top and square the pair
12. Fold one stacked sock pair once
13. Carry one sock packet onto the shorts stack with the left gripper
14. Put one toiletry into the toiletry tote
15. Turn the toiletry tote and carry it onto the load
16. Put one shoe into the shoe tote
17. Turn the shoe tote and carry it onto the toiletry tote
18. Press the load flat with both grippers
19. Anchor the case and close the lid
20. Draw the slider along the front edge to the swap corner
21. Turn the case and draw the slider round to the end stop
22. Return both arms home and end the episode
