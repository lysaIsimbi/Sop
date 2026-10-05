# 5S Reset a Workbench Zone SOP (1x Episode: one zone, in situ)

One episode resets one workbench zone, at the bench where it stands. The base is **passive**: it has no
drive of its own, so it is pushed by hand to the front of the bench and locked there, and nothing is
carried away to a table. Everything the episode touches is already on the bench when recording starts:
the stray items, the scattered tools, the tool box, the consumables, the cloth, the checklist
card in its bracket, and the marker in its clip.

The episode runs these five actions in this order and no other: **sort the stray items, set the tools in
order, wipe the bench, restage the consumables, sign the checklist.** Each one is a step, and the steps run
in that order.

The bench is worked **as found**. It is the bench at the end of a shift: stray items that do not belong
here are lying on it, how many varies per episode, the tools are out of their tool box and scattered over
the bench, and the consumables have been left standing on the back of the bench instead of in their
rack. The episode ends with the stray items sorted into a row on the sort spot, every tool in the tool box on
its own outline, the bench wiped, the consumables seated in their bays, and every tool ticked off on the checklist.

**Sorting is done on the bench.** Nothing leaves the bench and nothing goes in a bin. The stray items are
separated from the things that belong here by moving them, one at a time, to the **sort spot** at the left
end of the bench and laying them there in one straight row, each one clear of the next.

**Setting the tools in order is done in two passes.** First the scattered tools are **staged**: gathered
one at a time and laid in one straight row on the staging line, in the same left-to-right order as their
outlines in the tool box, handles toward the front. Only then are they put in the tool box, one at a time,
in that order, each onto its own outline. No tool goes from where it lay straight into the box.

**This is an in-situ task, and three things follow from that.** First, a **shelf runs along the wall
directly above the back of the bench**, so **every approach to the back of the bench is from the front,
straight in, level**. No gripper comes down onto the consumable rack or a consumable from above. The tool box
stands on the front of the bench, under open air, and is the one place a tool is lowered into from above.
Second, the **bench is never leaned on and never pushed**: no gripper, wrist, or forearm rests on the bench
top, the shelf, the tool box, or the checklist bracket, and no push is ever hard enough to shift the bench
or the box. Third, the **bench stays as it stands**: nothing is unbolted, the rack and the tool box
are never moved, and nothing is turned to make a reach easier.

The bench is set up in one of three ways. Only the **consumables** move. The stray items, the
tools, the tool box, the rack, the sort spot, the cloth, the bracket, and the marker are in the same place in
all three.

* **Config L:** the consumables stand on the back strip at its **left end**.
* **Config M:** the consumables stand on the back strip in its **middle**, to the left of the consumable rack.
* **Config R:** the consumables stand on the back strip at its **right end**, to the right of the consumable
  rack.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on
the setup it says so on an **IF** line. Look at the bench and follow the line that matches.

What stays constant across all sessions:

* **Same-side rule:** the gripper on the consumables' side picks each consumable up. That is the **left gripper** in
  Config L and the **right gripper** in Config M and R. No arm reaches across the bench.
* **Hand-over rule:** the consumable rack sits at the right end of the back strip, too far for the left
  gripper. So in Config L the left gripper **hands each consumable over** to the right gripper above the middle
  of the working area, and the right gripper puts it in its bay. Nothing is handed over in Config M or R.
* **Fixed roles:** the left gripper sorts the stray items onto the sort spot. The right gripper stages the
  tools, puts them in the tool box, wipes the whole working area with the one cloth, seats the consumables, and
  signs the checklist. The five actions run in the same order in every config.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm
reaches over, under, around, or past the other. The one time the right gripper works left of the middle is
the wipe, and the left gripper is clear of the bench for all of it. Nothing is moved two at a time: one gripper holds one
thing, and the other gripper is empty or clear of the bench.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never
steered, nudged, or repositioned once recording starts. It is parked once, before recording, and does not
move again until the episode is over.

1. Push the base by hand up to the bench and stop it **square to the front edge**, so the back strip runs
   straight across the frame of the camera and neither end of the zone sits nearer than the other.
2. Stop it **centered on the zone**, so the sort spot at the left end and the tool box at the right end
   are the same distance out from the middle of the base.
3. Stop it **close enough** that both grippers reach the back strip straight in and level without either
   arm extending, and **far enough** that neither arm, wrist, nor any part of the base touches the bench,
   the box, the bracket, or the shelf above while both arms work.
4. Check the **height band**: with the base parked, both grippers come level onto the back strip and into
   the consumable rack without a wrist or forearm fouling the shelf above, and the **right gripper** comes
   down into the tool box from above without touching its rim or its lid.
5. Check the **right side**: the **right gripper** reaches every tool in the right half of the working area,
   the whole staging line, every outline on the floor of the tool box, both bays in the consumable rack,
   the cloth on the cloth home, the whole working area out to its left edge, the checklist card in its bracket, and
   the marker in its clip, all without extending and without knocking anything.
6. Check the **left side**: the **left gripper** reaches every stray item in the left half of the working
   area, the whole sort spot, and the middle of the working area, all without extending. It reaches no
   part of the tool box, no bay, the cloth home, and no part of the bracket.
7. Check the **consumable spot** for the config this episode runs: in **Config L** the **left gripper** reaches
   the consumables at the left end of the back strip straight in and level; in **Config M** and **Config R** the
   **right gripper** reaches the consumables straight in and level.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not work
   a bench the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the bench hard
enough to shift it, nothing touches it by hand, and it is never repositioned mid-task. A base that moves
after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the bench and its frame includes the whole zone: the sort spot,
   the working area, the staging line, the cloth home, the open tool box, the consumable rack, the
   consumable spot this config uses, the checklist bracket, and the marker clip.
3. The camera reads the **outlines on the floor of the tool box** and the **bay outlines**, so which
   outline a tool was laid on and which bay a consumable went into are readable.
4. The camera reads the **working area** well enough to see loose dust on it before and after the wipe, and
   the **staging line** well enough to see the order the tools lie in.
5. The camera reads the **sort spot**, so the row of stray items and the order they lie in are readable.
6. The camera reads the **checklist card**, so which lines are ticked and whether each tick sits inside its box
   are readable.
7. Both arms are at home with grippers open.
8. The **right arm** reaches every tool, the staging line, every outline in the tool box, every bay, the
   cloth, the whole working area out to its left edge, the card, and the marker without extending to a joint
   limit.
9. The **left arm** reaches every stray item, the whole sort spot, and the middle of the working area without
   extending to a joint limit. It reaches no part of the tool box, no bay, and not the cloth home.
10. Both grippers come in and go out of the back strip **from the front and level**. Neither comes down onto
    the rack or a consumable from above, and neither wrist nor forearm touches the shelf above on the way in or out.
11. The **right gripper** comes straight down into the tool box and straight up out of it without touching
    its rim, its sides, or its lid.
12. The two arms do not collide, and neither arm passes in front of the other.
13. If a place cannot be reached, re-park the base by the Base positioning steps until lines 8 to 12 hold.

### Materials checklist

1. The **workbench** stands where it lives, bolted or braced to the floor or the wall. It is not moved, not
   leaned on, and not pushed at any point.
2. A **shelf** runs along the wall directly above the back of the bench, so the only way to the back strip is
   straight in from the front and never from the top. The shelf is high enough for a gripper to come in level
   under it and low enough that nothing can be lifted over it.
3. Nothing on the bench is powered or running. If a power strip is fixed to the bench, its switch is at **OFF**
   before recording starts.
4. The **back strip** is the part of the bench top under the shelf. It carries the consumable rack and this
   config's consumable spot, and nothing else.
5. The **consumable rack** is fixed on the back strip at its right end. It has **one bay for each consumable**,
   open at the front, side by side. Each bay carries the **outline** of the one consumable that lives in it,
   drawn on its floor and readable from the front, so a consumable matches one bay and no other. Every bay
   starts empty.
6. Each bay is deep enough to take its consumable all the way in, and wide enough that it slides in without
   being squeezed or forced.
7. The **front strip** is the part of the bench top in front of the shelf. Nothing stands above it.
8. The **sort spot** is the left end of the front strip. It is bare bench, not marked, and it starts empty. It is where the stray items are laid in a row.
9. The **tool box** stands on the front strip at its right end, against the back strip, with its **lid open**
   and folded back so its whole floor is in view from above. It is heavy or braced enough not to slide when a
   tool is laid in it, and it does not move at any point.
10. The floor of the tool box carries **one outline for each tool**, drawn left to right, so every tool matches
    one outline and no other, and the outlines set the order the tools go in. All the outlines start empty.
11. The **working area** is the clear middle of the front strip, between the sort spot and the tool box. It is
    the part of the bench that gets wiped.
12. **Stray items** lie in the **left half of the working area**, for example a mug, a stapler, or a small parts
    box. How many there are varies per episode and is never fixed. None of them belongs at this bench, each one
    lies clear of the others, and each one can be picked up in one grip.
13. The **tools** lie **scattered over the right half of the working area**, one for each outline in the tool
    box, at any angle and in no order, some with their handles away from the front. No tool lies on top of
    another, none lies in the left half, and each one can be picked up by its handle in one grip. Which tools
    they are is not fixed.
14. The **staging line** is the back line of the right half of the working area, along the front edge of the
    back strip. It is bare bench, not marked, and it is where the tools are laid in a row before they go in the
    box.
15. The **consumables** stand on the back strip, side by side, one for each bay in the rack and in the same
    left-to-right order as their bays. Which consumables they are is not fixed. They stand at the left end of
    the back strip in **Config L**, in the middle of the back strip in **Config M**, and at the right end in
    **Config R**.
16. Every consumable is closed, square-sided, and light enough for one gripper to hold in one grip.
17. There is **one cloth**. It lies folded flat on the **cloth home**, a marked spot at the front-right corner
    of the front strip, in front of the tool box.
18. The cloth is damp and wrung out, so it picks dust up and does not drip.
19. There is loose dust on the working area, spread over both halves, so whether a half has been wiped is
    readable from the front.
20. The **checklist bracket** is bolted to the front edge of the bench at its right end, below the cloth
    home. It is open at the front, so the card can be signed where it sits.
21. The **checklist card** in the bracket is the **list of tools** that live in the tool box: one line per tool,
    top to bottom in the same order as the outlines run left to right in the box, each line ending in an empty
    **tick box** at its right end. The card is fresh: no box on it is ticked.
22. The **marker** stands in its clip beside the bracket, point down, and it marks the card without being
    shaken or uncapped.
23. Nothing else stands anywhere in the zone within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the cloth home. You judge every other place by eye against
the bench itself: the back strip, the front strip, and the front edge.

* **Bench:** the workbench the base is parked at. It is never moved, never leaned on, and never pushed.
* **Shelf above:** the shelf on the wall directly over the back of the bench. It is what makes every reach into
  the back strip a front approach. Nothing ever touches it.
* **Back strip:** the bench top under the shelf. It carries the consumable rack and the consumable spot. It is never
  wiped.
* **Consumable rack:** fixed at the right end of the back strip, one open-front bay per consumable, each with the
  outline of its own consumable. **Right gripper only.**
* **Consumable spot:** where the consumables stand on the back strip in this episode's config. Left end in Config L,
  middle in Config M, right end in Config R.
* **Front strip:** the bench top in front of the shelf, with open air above it.
* **Sort spot:** the left end of the front strip. Everything that does not belong
  at this bench is laid here in one straight row. It is never wiped. **Left gripper only.**
* **Working area:** the clear middle of the front strip, between the sort spot and the tool box. Its **left
  half** holds the stray items. Its **right half** holds the scattered tools and the staging line. The whole of it
  is wiped by the right gripper.
* **Staging line:** the back line of the right half of the working area, where the tools are laid in a row in
  the order of their outlines. **Right gripper only.**
* **Tool box:** the open box at the right end of the front strip, lid folded back, one outline per tool on its
  floor. It is the one place a gripper comes down into from above. **Right gripper only.**
* **Cloth home:** the marked spot at the front-right corner of the front strip, in front of the tool box, where
  the one cloth lies. **Right gripper only.**
* **Checklist bracket:** bolted to the front edge of the bench at the right end. It holds the checklist card.
  **Right gripper only.**
* **Marker clip:** beside the bracket, holding the marker point down. **Right gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the left end and the left half: the stray items, the sort spot, and, in Config L
  only, the consumables and the hand-over at the middle.
* The **right gripper** works the right end and the right half: the scattered tools, the staging line, the tool
  box, the consumable rack, the cloth, the right half of the working area, the card, and the marker.
* The **left gripper never goes right of the middle of the working area**, and the **right gripper never goes
  left of it**, with two exceptions: the hand-over at the middle in Config L, and the **wipe**, where the right
  gripper wipes the left half with the cloth while the left gripper is drawn clear of the bench.
* Neither arm reaches over, under, around, or past the other, and neither reaches across the front of the other
  arm's body.
* Only one thing is moved at a time. A gripper holds one thing, and while it does, the other gripper is either
  empty or drawn **clear of the bench**.

### Arm assignments

* **Right gripper.** Gathers the scattered tools onto the staging line in order, then lays each one in the tool
  box on its outline. Wipes the whole working area, right half then left half, with the one cloth. Seats both
  consumables in their bays. Signs the checklist card with the marker.
* **Left gripper.** Sorts every stray item onto the sort spot, in a row. In **Config L** only, picks each consumable off
  the back strip and hands it over to the right gripper. Stays clear of the bench for the wipe.
* Nothing else is handed between grippers, and only one thing is moved at a time.

## Vocabulary

* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down onto the
  back strip, the consumable rack, or a consumable from above. Every reach into the back strip is a front approach.
* **Zone:** the stretch of bench the base is parked at, from the sort spot at the left end to the tool box at
  the right end.
* **Stray item:** anything lying in the working area that is not a tool, a consumable, a cloth, or the marker, for
  example a mug, a stapler, or a parts box. It does not belong at this bench. How many there are varies per
  episode. No other test is applied.
* **Sorted:** the stray item lies on the sort spot, in the row, flat or upright as it stands best, clear of the
  item beside it, and nowhere on the working area.
* **Handle / working end:** the handle is the end of a tool made to be held. The working end is the other end.
  The gripper takes every tool by its handle.
* **Outline:** the drawn shape of one tool on the floor of the tool box, or of one consumable on the floor of a bay.
  Each outline takes one thing, the one that matches it.
* **In order:** the left-to-right order of the outlines on the floor of the tool box. The tools are staged in
  that order and go into the box in that order, leftmost first.
* **Staged:** the tool lies flat on the staging line, straight, handle toward the front, in its place in the
  order, clear of the tools beside it.
* **In the box:** the tool lies flat on the floor of the tool box, inside its own outline, handle toward the
  front, and stays put when the gripper opens. A tool on the rim, across two outlines, or on top of another tool
  is not in the box.
* **Bay:** one of the open-front spaces in the consumable rack. Each one takes one consumable.
* **Seated:** the consumable has gone all the way into its bay, on its outline, its front face is level with the front
  of the bay, and it stays put when the gripper opens. Anything standing proud of the front is not seated.
* **Pass:** one wipe. The gripper lays the cloth flat on the bench, presses it down, draws it straight in one line
  without lifting, and stops. A wipe that lifts halfway is not a pass.
* **Hand over:** one gripper gives a thing to the other above the middle of the working area. The giving gripper
  brings it to the middle and holds it still for a **half-second hold**. The taking gripper then closes on the far
  side of it. Only after the taking gripper is closed does the giving gripper open and draw back.
* **Half-second hold:** the giving gripper stops moving and stays still for about half a second, so the thing is
  not moving when the other gripper closes on it.
* **Cloth home:** the marked spot the one cloth lies on, at the front-right corner of the front strip.
* **Checklist:** the card in the bracket, listing the tools of the tool box one line each, top to bottom in the
  order of the outlines, each line with a tick box at its right end.
* **Tick:** one mark with the marker inside a tick box: a short stroke down and to the right then a longer stroke
  up and to the right, drawn without lifting.
* **Sign the checklist:** tick the box of every tool on the list, top line first, one tick each, after every tool
  is in the box. The ticks are the only marks the episode puts on the card.
* **Clear of the bench:** the arm is drawn back so that no part of it is over the front strip, the back strip, the
  tool box, or the sort spot.

## Steps

Run Steps 1 to 5 in order, and end the episode with Step 6. The five steps are the five actions of the task, in
the task's own order: **sort the stray items, set the tools in order, wipe the bench, restage the consumables,
sign the checklist.** Only Step 4 depends on the config. Every other step is the same in all three.

### Step 1: Sort the stray items

**Goal:** every stray item is **sorted** into one straight row on the sort spot, and the left half of the working
area holds nothing.

* Apply the stray item test in Vocabulary: anything lying in the working area that is not a tool, a consumable, a cloth,
  or the marker is a stray item. Leave the tools where they lie.
* Work one stray item at a time. Start with the stray item nearest the left end of the working area and work to
  the right.
* With the **left gripper**, close on the stray item at its widest point and lift it straight up off the bench.
* With the **left gripper**, carry it level to the **sort spot** and set it down in the row: the first item at the
  back-left corner of the sort spot, each next item to the right of the last, clear of it, along the back line of
  the sort spot. If the row reaches the working area, start a second row in front of the first, from the left.
* Open the **left gripper** and draw it straight up off the item.
* With the **left gripper**, carry one stray item at a time, lift it clear of the bench before the carry, and do
  not slide or drag one across the bench. Do not stack one item on another.
* With the **left gripper**, touch no tool, no consumable, no cloth, and no part of the tool box or the rack.
* Repeat for the next stray item until none is left on the working area, then open the **left gripper** and draw
  it **clear of the bench**.
* Hold the **right gripper** open and **clear of the bench** for the whole of this step.

**Check:** after each one, the stray item stands or lies on the sort spot in the row, clear of the item beside it,
and nothing has tipped over. If a stray item lands off the sort spot or against another, lift it with the **left
gripper** and set it down again in its place. Look across the working area once more: if any stray item is still
on it, sort it before Step 2.

**Expected state:** every stray item is in the row on the sort spot. The left half of the working area holds
nothing but dust. The tools still lie scattered over the right half.

### Step 2: Set the tools in order

**Goal:** every tool is **in the box**, flat on its own outline, handle toward the front, and the right half of the
working area holds no tool.

This step is two passes. First every tool is **staged** on the staging line, in order. Then the staged tools go
into the tool box, in that order. Hold the **left gripper** open and **clear of the bench** for the whole of this
step.

#### 2.1 Stage the tools

* Look at the outlines on the floor of the tool box. They run left to right, and every tool on the bench has one.
  That left-to-right order is the order the tools are staged in.
* Work one tool at a time. Start with the tool nearest the front edge of the right half and work back.
* With the **right gripper**, close on the **handle** of the tool, not on its working end, and lift it straight up
  off the bench.
* With the **right gripper**, carry it level to the **staging line** and lay it flat, straight, with its handle
  toward the front, in its place in the order: the tool of the leftmost outline goes at the left end of the line,
  the tool of the next outline to its right, and so on, each one clear of the tool beside it.
* Open the **right gripper**, lift it straight up off the tool, and take it **clear of the bench**.
* With the **right gripper**, carry one tool at a time, lift it clear of the bench before the carry, and do not
  slide or drag a tool across the bench.
* Repeat for the next tool until no tool lies loose in the right half and every tool is on the staging line.

**Check:** the tools lie in one straight row on the staging line, in the order of the outlines, none touching
another, every handle toward the front. If a tool is out of order, crooked, touching another, or the wrong way
round, lift it with the **right gripper** and lay it again in its place. Look across the right half once more: if
a tool still lies loose, stage it before 2.2.

#### 2.2 Put the tools in the tool box

* Take the staged tools **in order**, the leftmost first.
* With the **right gripper**, close on the **handle** of the tool and lift it straight up off the staging line.
* With the **right gripper**, carry it level over the tool box and stop above its own outline.
* Look at the outline before going down: it matches the tool in the gripper.
* With the **right gripper**, bring the tool straight down into the box, handle toward the front, until it lies
  flat on the floor of the box inside its outline.
* Open the **right gripper**, draw it straight up out of the box without touching the rim, the sides, or the lid,
  and take it **clear of the bench**.
* With the **right gripper**, do not let a tool go from above the rim, do not lay one tool on top of another, and
  do not push a tool along the floor of the box.
* Repeat for the next tool to the right on the staging line until the line is empty and every outline is covered.

**Check:** after each one, the tool is **in the box**: flat, inside its own outline, handle toward the front, and it
stays put with the **right gripper** off it. The box has not slid. If a tool lies on the wrong outline, across two
outlines, crooked, or on the rim, lift it with the **right gripper** and lay it again on its own outline.

**Expected state:** every outline in the tool box is covered by its own tool, in order. The staging line is empty,
and the right half of the working area holds nothing but dust.

### Step 3: Wipe the bench

**Goal:** the bench top is wiped, half by half, with the one cloth, and the cloth is back on the cloth home.

The part of the bench that is wiped is the **working area**, the open bench top between the sort spot and the
tool box, including the staging line. The back strip under the shelf carries the rack and is not wiped, and the
sort spot and the tool box are not wiped. The **right gripper** does the whole wipe: the right half first, then
the left half. The **left gripper** stays open and **clear of the bench** for the whole of this step.

#### 3.1 Wipe the right half

* With the **right gripper**, close on the middle of the **cloth** and lift it straight up off the **cloth home**.
* With the **right gripper**, lay the cloth flat on the working area at its **right edge**, on the back line, just
  in front of the back strip, beside the tool box.
* With the **right gripper**, press the cloth flat and draw it straight from the right edge in to the **middle of
  the working area**, in one **pass**, without lifting it.
* With the **right gripper**, lift the cloth just off the bench, carry it back out to the right edge, and set it
  down one cloth width forward of the last pass. Draw it in to the middle again.
* With the **right gripper**, do this a third time, along the front line of the right half.
* Three passes in all: the back line, the middle line, then the front line, each drawn from the right edge in to
  the middle.
* With the **right gripper**, keep the cloth below the shelf and off the rack and the tool box, and do not push dust
  off the front edge, into the tool box, or off the right end of the bench.

**Check:** the right half shows no loose dust, the three passes have covered it from the back strip to the front
edge, and no dust has gone over an edge or into the box. If a line of dust is left, wipe that line again with the
**right gripper**.

#### 3.2 Wipe the left half

* With the **right gripper**, carry the cloth just off the bench across the middle and lay it flat on the working
  area at its **left edge**, on the back line, beside the sort spot.
* With the **right gripper**, press the cloth flat and draw it straight from the left edge in to the **middle of the
  working area**, in one **pass**, without lifting it.
* With the **right gripper**, lift the cloth just off the bench, carry it back out to the left edge, set it down one
  cloth width forward, and draw it in to the middle again.
* With the **right gripper**, do this a third time, along the front line of the left half.
* Three passes in all: the back line, the middle line, then the front line, each drawn from the left edge in to the
  middle.
* With the **right gripper**, keep the cloth clear of the sort spot and the row on it, and do not push dust off the
  front edge or the left end of the bench.
* The **left gripper** is open and **clear of the bench** for all of this. The right arm is the only arm over the
  left half.

**Check:** the left half shows no loose dust, the three passes have covered it, and no dust has gone over an edge or
onto the sort spot. If a line of dust is left, wipe that line again with the **right gripper**.

#### 3.3 Put the cloth back

* With the **right gripper**, carry the cloth just off the bench back to the right end and lay it flat on the
  **cloth home**, then open the gripper and draw it **clear of the bench**.

**Check:** the cloth lies flat on the cloth home, and neither gripper holds anything.

**Expected state:** the bench top is wiped and empty, the cloth is on the cloth home, every tool is in the box, and
the consumables still stand at the consumable spot.

### Step 4: Restage the consumables

**Goal:** every consumable is **seated** in the bay whose outline matches it, and the consumable spot is empty.

* Work one consumable at a time, in the order they stand, left to right.
* **IF Config L:** with the **left gripper**, close on the sides of the consumable at the left end of the back
  strip and draw it straight out to the front, level, from under the shelf. With the **left gripper**, carry it to
  the **middle of the working area** and hold it still for a **half-second hold**. With the **right gripper**, close
  on the far side of it. With the **left gripper**, open and draw back **clear of the bench**.
* **IF Config M or Config R:** with the **right gripper**, close on the sides of the consumable where it stands on
  the back strip and draw it straight out to the front, level, from under the shelf. There is no hand-over.
* Then, in all three: with the **right gripper**, carry the consumable level to the front of its bay, the one whose
  outline matches it.
* Look at the outline in the bay before going in: it matches the consumable in the gripper.
* With the **right gripper**, line the consumable up square with the bay and push it straight back into the bay,
  level, in one push, until it is all the way in.
* Push straight in only. With the **right gripper**, do not come down onto the rack from above, do not turn the
  consumable into the bay, and do not force it.
* Open the **right gripper**, draw it straight out to the front, and take it **clear of the bench**.
* Repeat for the next consumable until every bay is full.
* While either gripper carries a consumable, the other gripper is empty and, outside the hand-over, **clear of the
  bench**.

**Check:** after each one, the consumable is **seated**: all the way in, on its outline, square, its front face level
with the front of the bay, and it stays put with the **right gripper** off it. If it stands proud or sits crooked,
close on it again with the **right gripper**, draw it out, line it up, and push it straight in.

**Expected state:** every bay is full, the consumable spot on the back strip is empty, every tool is in the box, the
bench top is empty and wiped, and both grippers are clear of the bench.

### Step 5: Sign the checklist

**Goal:** every tool on the checklist is **ticked**, one tick per line, and the marker is back in its clip.

#### 5.1 Take the marker

* With the **right gripper**, close on the **barrel** of the marker, not on its point, and lift it straight up out of
  its clip.
* With the **right gripper**, carry it level to the card, from the front.
* Hold the **left gripper** open and **clear of the bench** for the whole of this step.

**Check:** the **right gripper** holds the marker by its barrel and the point hangs clear.

#### 5.2 Tick every tool on the list

* Start at the **top line** of the card and work down, one line at a time. Each line is one tool, in the same order
  as the outlines in the box, so the top line is the tool on the leftmost outline.
* Before ticking a line, look at the tool box: the outline that line stands for is covered by its tool.
* With the **right gripper**, bring the point of the marker down inside that line's **tick box**, left of its middle.
* With the **right gripper**, draw one **tick**: a short stroke down and to the right to the bottom of the box, then
  a longer stroke up and to the right toward its top-right corner, without lifting, then lift the marker straight
  off the card.
* With the **right gripper**, keep the tick inside its box. Press only hard enough to leave a mark, not hard enough
  to move the card, the bracket, or the bench.
* Repeat for the next line down until every line on the card is ticked.

**Check:** every line on the card carries **one tick**, inside its box, and no line is skipped or ticked twice. If
a tick has run outside its box or come out short, leave it. Do not draw over it, do not draw a second tick in the
same box, and do not tick a line whose tool is not in the box.

#### 5.3 Put the marker back

* With the **right gripper**, carry the marker back and stand it in its clip, point down, where it started.
* Open the **right gripper** and draw it back **clear of the bench**.

**Check:** the marker stands in its clip point down, and it stays there with the **right gripper** off it.

**Expected state:** the checklist is signed, every tool ticked, the marker is in its clip, and both arms are clear of
the bench.

### Step 6: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the bench reset.

* Look once across the bench: the stray items are in a row on the sort spot, every outline in the tool box is covered,
  the working area is clean, the consumables are seated, every line on the card is ticked, and the cloth and the marker are
  back where they live.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the bench is reset and still, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Clear the sort spot and lay stray items back in the left half of the working area, each clear of the others and
   none on a tool, the cloth home, or the back strip. Vary how many and which items between episodes.
2. Take every tool out of the tool box and scatter them over the right half of the working area, at any angle and in
   no order, some with handles away from the front, none on top of another, and none on the staging line in a row.
   Vary the scatter between episodes.
3. Take the consumables out of their bays and stand them side by side at the consumable spot for the next episode's
   config, in the same order as their bays.
4. Spread fresh loose dust over both halves of the working area, so the next episode starts with something to wipe.
5. Rinse the cloth, wring it out, and lay it folded flat on the cloth home. Replace it when it has stopped picking dust
   up.
6. Check the sort spot is bare and nothing has been left on it.
7. Check the tool box is empty, its lid is open and folded back, it has not slid, and it is still heavy or braced enough
   not to slide when a tool is laid in it.
8. Check every bay is empty, clean, and not chipped or bent, and that each one still takes its consumable without it
   being forced.
9. Check the outlines on the floor of the tool box and the bay outlines are still readable, and redraw any that has
   faded.
10. Check the marker still marks, and replace it when it has dried out.
11. Take the ticked card out of the bracket and put in a fresh checklist card with no box ticked.
12. Check nothing on the bench has been powered up or left running.
13. Pick up anything that landed on the bench or the floor, and sweep up dust that went over an edge or into the box.
14. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what
the reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a
rule was broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the bench shifts in frame, the back strip changes angle or size in frame, or the base rolls, creeps, or
  turns at any point after recording starts.
* **SOP rule broken:** Steps 1 to 6, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Approached from above or fouled the shelf**

* **Visible cue:** a gripper comes down onto the back strip, the consumable rack, or a consumable from above instead of coming
  in level from the front, or a wrist, forearm, tool, consumable, or cloth knocks, scrapes, or rests on the shelf on the way in
  or out.
* **SOP rule broken:** Steps 3.1 and 4, every reach into the back strip is a front approach, level, straight in
  and straight out. Only the tool box is entered from above.
* **Coaching note:** straight in from the front, straight out the same way. There is no way in from the top, except into
  the box.

**Violation: Leaned on or pushed the bench**

* **Visible cue:** a gripper, wrist, or forearm rests on the bench top, the tool box, the rack, or the checklist bracket;
  the bench or the box rocks, slides, or shifts; or a push, a wipe, or the tick presses hard enough to move the box, the
  card, or the bracket.
* **SOP rule broken:** Steps 1 to 5, the bench carries no weight and nothing standing or fixed on it is pushed out of place.
* **Coaching note:** the arm holds itself up. Press only as hard as the push, the wipe, or the tick needs.

**Violation: Stray item left out or put somewhere other than the sort spot**

* **Visible cue:** the episode ends with a stray item still on the working area; a stray item is put on the back strip,
  in the tool box, in a bay, on the cloth home, or off the bench instead of on the sort spot; or a stray item is dropped
  onto the sort spot from a height instead of being set down.
* **SOP rule broken:** Step 1, the **left gripper** carries each stray item to the sort spot and sets it down in the row,
  one at a time, until none is left on the working area.
* **Coaching note:** one stray item, one trip, and set each one down in the row. Nothing leaves the bench.

**Violation: Row on the sort spot not in order, or something sorted that is not a stray item**

* **Visible cue:** a stray item is set down anywhere on the sort spot other than the next place in the row; items touch,
  overlap, or are stacked; a stray item is slid or dragged across the bench instead of lifted; or a tool, a consumable,
  a cloth, or the marker is put on the sort spot.
* **SOP rule broken:** Step 1, only stray items go on the sort spot, each one lifted, carried, and set down in one straight
  row, each clear of the last. Tools go in the tool box and consumables go in their bays.
* **Coaching note:** the sort spot takes what does not live here, in a row. A tool on the sort spot is a tool the next shift
  cannot find.

**Violation: Tool not staged, or staged out of order**

* **Visible cue:** a tool goes from where it lay straight into the tool box without being laid on the staging line
  first; the staged row is not in the order of the outlines; a staged tool is crooked, touching another, or lying with
  its handle away from the front; or a tool is slid or dragged across the bench onto the line instead of being lifted.
* **SOP rule broken:** Step 2.1, every tool is lifted, carried, and laid flat on the staging line in its place in the
  order, before any tool goes in the box.
* **Coaching note:** gather first, box second. The row on the line is the order, and it is read before the box is touched.

**Violation: Tool laid on the wrong outline or boxed out of order**

* **Visible cue:** a tool is laid on an outline that does not match it, across two outlines, or on top of another tool;
  or the staged tools go into the box out of order, a tool to the right taken before a tool to its left.
* **SOP rule broken:** Step 2.2, take the staged tools leftmost first, look at the outline, and lay each tool inside
  its own outline.
* **Coaching note:** leftmost first, look at the outline, then go down. The outlines are the whole point of setting
  tools in order.

**Violation: Tool not flat in the box, dropped in, or pushed along the floor**

* **Visible cue:** a tool ends up on the rim, leaning on a side of the box, crooked on its outline, or not flat; a tool is
  let go from above the rim and falls in; a tool is pushed along the floor of the box into place; or a gripper touches the
  rim, the sides, or the lid on the way in or out.
* **SOP rule broken:** Step 2.2, bring each tool straight down inside its outline until it lies flat, open, and draw
  straight up without touching the box.
* **Coaching note:** straight down, let go flat, straight up. Nothing is dropped and nothing is shoved.

**Violation: Tool held by its working end or laid in the wrong way round**

* **Visible cue:** the **right gripper** closes on the working end of a tool instead of its handle, or a tool ends up on
  the staging line or in the box with its handle away from the front.
* **SOP rule broken:** Steps 2.1 and 2.2, the **right gripper** takes each tool by its handle and lays it handle toward
  the front, on the line and in the box.
* **Coaching note:** handle in the gripper, handle to the front. The next shift picks it up the same way every time.

**Violation: Wipe pattern wrong**

* **Visible cue:** a half gets fewer or more than three passes; a pass runs from the middle out instead of from the outer edge
  in; the cloth lifts partway through a pass; the passes do not step forward from the back line to the front line; or part of a
  half is never covered.
* **SOP rule broken:** Steps 3.1 and 3.2, wipe each half with three passes, the back line, the middle line, then the front line,
  each drawn from the outer edge in to the middle without lifting.
* **Coaching note:** three passes, outer edge to the middle, back to front. Count them as you go.

**Violation: Dust pushed off the bench**

* **Visible cue:** a pass carries dust over the front edge, over the left or right end of the bench, onto the floor, into
  the tool box, or onto the sort spot.
* **SOP rule broken:** Steps 3.1 and 3.2, each pass is drawn in to the middle so the cloth keeps the dust, and nothing is pushed
  off an edge, into the box, or onto the sort spot.
* **Coaching note:** the cloth holds the dust. Anything that goes over the edge, someone else has to sweep.

**Violation: Cloth not put back on the cloth home**

* **Visible cue:** the cloth is left on the working area, on the back strip, in the tool box, on the sort spot, or still in
  the gripper at the end of the episode; the cloth is laid down somewhere other than the cloth home; or the cloth is left
  bunched instead of flat.
* **SOP rule broken:** Step 3.3, the **right gripper** lays the cloth flat on the cloth home before the step ends.
* **Coaching note:** same spot, flat, every time. A cloth left on the bench is dust back on the bench.

**Violation: Consumable put in the wrong bay**

* **Visible cue:** a consumable goes into the bay whose outline does not match it, two consumables are swapped, or a
  consumable goes into the tool box.
* **SOP rule broken:** Step 4, match each consumable to its outline and push it into that bay.
* **Coaching note:** look at the outline before the push, the same way you look at the outline in the box.

**Violation: Consumable not seated, or left on the back strip**

* **Visible cue:** a consumable stands proud of the front of its bay, sits crooked in it, falls out when the **right gripper** opens,
  is turned or forced into the bay, or is still standing at the consumable spot when the episode ends.
* **SOP rule broken:** Step 4, each consumable is drawn straight out to the front, lined up square, and pushed straight
  into its bay until it is seated.
* **Coaching note:** square it up, one straight push, all the way in. A consumable left on the bench is one nobody can find.

**Violation: Hand-over done wrong**

* **Visible cue:** in Config L the **left gripper** opens before the **right gripper** has closed on the consumable; the consumable is still
  moving when the **right gripper** closes, with no half-second hold; the consumable is dropped or passed below the middle of the
  working area; or a hand-over happens in Config M or Config R, where none is called for.
* **SOP rule broken:** Step 4, in Config L the **left gripper** brings the consumable to the middle, holds it still for a
  half-second hold, and opens only after the **right gripper** has closed on the far side.
* **Coaching note:** stop, hold still, let the other gripper take it, then open. In Config M and R nothing changes hands.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the bench is not set up in: the wrong gripper picks a consumable up, the **left gripper**
  reaches for the consumables in Config M or R, the **right gripper** reaches for them in Config L, an arm reaches for a consumable spot
  that is empty, or the consumables are moved to a different spot on the back strip before being picked up.
* **SOP rule broken:** Step 4, look at the bench, find the consumable spot, and follow the IF line that matches the config
  the episode is set up in.
* **Coaching note:** look at the bench before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** a tool is touched before every stray item is on the sort spot; a tool goes in the box before every tool is
  staged; the cloth touches the bench before every tool is in the box; the left half is wiped before the right half; a pass goes around a stray item or a tool still lying
  on the working area; a consumable goes in its bay before the bench is wiped; the card is signed before every consumable is seated;
  a stray item is taken out of left-to-right order; or a consumable is taken out of left-to-right order.
* **SOP rule broken:** Steps 1 to 5, sort the stray items, stage the tools then box them, wipe the bench, restage the
  consumables, then sign the checklist.
* **Coaching note:** the order is the task. Each step leaves the bench ready for the next one.

**Violation: Checklist signed wrong**

* **Visible cue:** the card is not ticked at all; a line is skipped; the lines are ticked out of order, not top to
  bottom; a line is ticked twice; a tick goes outside its box, over the printed list, or between lines; a mark other than a
  tick is drawn; a line is ticked while its tool is not in the box; or a tick that ran outside its box is drawn over.
* **SOP rule broken:** Step 5.2, tick every line top to bottom, one tick inside each box, only once every tool is in the box.
* **Coaching note:** top to bottom, one tick per tool, and leave it. The card is the only record the tools came back.

**Violation: Marker not put back in its clip**

* **Visible cue:** the marker is left on the bench, on the card, in the bracket, in the tool box, on the sort spot, or in a
  gripper at the end; it is put back point up; or the **right gripper** closes on its point instead of its barrel.
* **SOP rule broken:** Steps 5.1 and 5.3, the **right gripper** takes the marker by its barrel and stands it back in its clip
  point down.
* **Coaching note:** barrel in the gripper, point down in the clip. A marker left out dries out.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two stray items, two tools, or the consumables together; both grippers carry different things at
  the same time; or a gripper holds something while the other gripper works instead of being drawn clear of the bench.
* **SOP rule broken:** Steps 1 to 5, one gripper holds one thing, and while it does the other gripper is empty or clear of the
  bench.
* **Coaching note:** one thing, one trip. Two at once is what puts something on the floor.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a stray
  item off the sort spot or against another, a staged tool out of order or crooked, a tool on the wrong outline or not flat, a line of dust left
  on a half, a consumable sitting crooked, the cloth off the cloth home, or the marker not in its clip.
* **SOP rule broken:** Steps 1 to 5.3, run each check and correct what it finds by the retry written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a stray item, a tool, a consumable, a cloth, or the marker is dropped on the bench or the floor; a sorted stray
  item is knocked over or off the sort spot; the tool box is knocked over or slid out of place; the lid of the tool box is knocked shut; the card is knocked out of its
  bracket; or an arm knocks a tool off the staging line or out of the box, or a consumable out of its bay.
* **SOP rule broken:** Steps 1 to 5, nothing is dropped or knocked out of its place, and every gripper comes out the way it
  went in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **right gripper** touches a stray item or the sort spot; the **left gripper** touches a tool, the
  staging line, the tool box, a bay, the cloth, the card, or the marker; the **left gripper** goes right of the middle of the
  working area; the **right gripper** goes left of it other than for a Config L hand-over at the middle or the wipe of the
  left half; the **left gripper** is over the bench while the right gripper wipes; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 5, the **left gripper** sorts the stray items, the **right gripper** does the tools, the
  wipe, the consumables, and the card, and the arms never cross.
* **Coaching note:** left arm works the left end, right arm works the right end and the whole wipe, and only a Config L
  hand-over meets at the middle.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a stray item on the working area, a tool on the bench or on the staging line, an outline in
  the box uncovered, a half unwiped, the cloth off the cloth home, a consumable on the back strip, the card unsigned, the marker out of
  its clip, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 6, look once across the bench, then return both arms home with grippers open and stop
  recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for
coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read an outline in the tool box, a bay outline, the staging line, the working area, the sort spot, or the
  card**, so which outline a tool was laid on, the order the tools were staged in, the row on the sort spot, which bay a consumable
  went into, whether a half came clean, or which lines were ticked cannot be judged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Faulty tool box or rack:** a lid that will not stay open, a box that slides under a correctly laid tool, a bay that will not
  take its consumable all the way in, or a rack that comes loose from the bench.
* **Damaged item:** a tool that arrives bent or broken, a consumable that is burst or crushed, a stray item that comes apart in the
  gripper, or the cloth falling apart.
* **Consumables out:** no damp cloth, no fresh checklist card, or a marker that will not mark.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a stray item, the sort spot,
  a tool, the staging line, an outline in the box, a bay, the cloth home, the left edge of the working area, the consumable spot, the card, or the marker cannot be reached
  without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Set one stray item down in the row on the sort spot
2. Pick one tool up by its handle
3. Lay one tool on the staging line in its place
4. Lay one tool in the tool box on its outline
5. Take the cloth off the cloth home
6. Wipe one pass across a half of the bench
7. Lay the cloth back on the cloth home
8. Draw one consumable out from the back strip
9. Hand one consumable over at the middle of the working area
10. Push one consumable into its bay
11. Take the marker out of its clip
12. Tick one tool on the checklist card
13. Stand the marker back in its clip
14. Return both arms home and end the episode
