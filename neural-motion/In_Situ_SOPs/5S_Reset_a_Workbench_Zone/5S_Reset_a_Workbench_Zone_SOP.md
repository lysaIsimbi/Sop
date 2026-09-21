# 5S Reset a Workbench Zone SOP (1x Episode: one zone, in situ)

One episode resets one workbench zone, at the bench where it stands. The base is **passive**: it has no
drive of its own, so it is pushed by hand to the front of the bench and locked there, and nothing is
carried away to a table. Everything the episode touches is already on the bench when recording starts:
the three stray items, the three tools, the two consumable packs, the two cloths, the returns bin, the
checklist card in its bracket, and the marker in its clip.

The episode runs these five actions in this order and no other: **sort the stray items, set the tools in
order, wipe the bench, restage the consumables, sign the checklist.** Each one is a step, and the steps run
in that order.

The bench is worked **as found**. It is the bench at the end of a shift: three stray items that do not
belong here are lying on it, three tools are out of their trough, and two consumable packs have been left
standing on the back of the bench instead of in their rack. The episode ends with the stray items in the
returns bin, all three tools in their own slots in order, the bench wiped, both packs seated in their bays,
and today's row on the checklist signed.

**This is an in-situ task, and three things follow from that.** First, a **shelf runs along the wall
directly above the back of the bench**, so **every approach to the back of the bench is from the front,
straight in, level**. No gripper comes down onto the tool trough, the consumable rack, or a pack from
above. Second, the **bench is never leaned on and never pushed**: no gripper, wrist, or forearm rests on
the bench top, the shelf, or the checklist bracket, and no push is ever hard enough to shift the bench or
the bin. Third, the **bench stays as it stands**: nothing is unbolted, the trough and the rack are never
moved, and nothing is turned to make a reach easier.

The bench is set up in one of three ways. Only the **two consumable packs** move. The stray items, the tools,
the trough, the rack, the bin, both cloths, the bracket, and the marker are in the same place in all
three.

* **Config L:** the two packs stand on the back strip at its **left end**, to the left of the tool trough.
* **Config M:** the two packs stand on the back strip **between the tool trough and the consumable rack**.
* **Config R:** the two packs stand on the back strip at its **right end**, to the right of the consumable
  rack.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on
the setup it says so on an **IF** line. Look at the bench and follow the line that matches.

What stays constant across all sessions:

* **Same-side rule:** the gripper on the packs' side picks each pack up. That is the **left gripper** in
  Config L and the **right gripper** in Config M and R. No arm reaches across the bench.
* **Hand-over rule:** the consumable rack sits at the right end of the back strip, too far for the left
  gripper. So in Config L the left gripper **hands each pack over** to the right gripper above the middle
  of the working area, and the right gripper puts it in its bay. Nothing is handed over in Config M or R.
* **Fixed roles:** the left gripper bins the stray items and wipes the left half. The right gripper sets
  the tools in order, wipes the right half, seats both packs, and signs the checklist. The five actions run
  in the same order in every config.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm
reaches over, under, around, or past the other. Nothing is moved two at a time: one gripper holds one
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
2. Stop it **centered on the zone**, so the returns bin at the left end and the checklist bracket at the
   right end are the same distance out from the middle of the base.
3. Stop it **close enough** that both grippers reach the back strip straight in and level without either
   arm extending, and **far enough** that neither arm, wrist, nor any part of the base touches the bench,
   the bin, the bracket, or the shelf above while both arms work.
4. Check the **height band**: with the base parked, both grippers come level onto the back strip, into the
   tool trough, and into the consumable rack, without a wrist or forearm fouling the shelf above.
5. Check the **right side**: the **right gripper** reaches all three tools in the right half of the working
   area, all three slots in the tool trough, both bays in the consumable rack, the right cloth on its home
   spot, the middle of the working area, the checklist card in its bracket, and the marker in its clip, all
   without extending and without knocking anything.
6. Check the **left side**: the **left gripper** reaches all three stray items in the left half of the working
   area, the mouth of the returns bin, the left cloth on its home spot, and the middle of the working area,
   all without extending. It reaches no slot, no bay, and no part of the bracket.
7. Check the **pack spot** for the config this episode runs: in **Config L** the **left gripper** reaches
   both packs at the left end of the back strip straight in and level; in **Config M** and **Config R** the
   **right gripper** reaches both packs straight in and level.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not work
   a bench the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the bench hard
enough to shift it, nothing touches it by hand, and it is never repositioned mid-task. A base that moves
after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the bench and its frame includes the whole zone: the returns bin,
   the working area, both cloth home spots, the tool trough, the consumable rack, the pack spot this config
   uses, the checklist bracket, and the marker clip.
3. The camera reads the **three slot labels** and the **two bay labels** from the front, so which slot a
   tool went into and which bay a pack went into are readable.
4. The camera reads the **working area** well enough to see loose dust on it before and after the wipe.
5. The camera reads the **mouth of the returns bin**, so what lands inside it is readable.
6. The camera reads the **checklist card**, so which row is signed and whether the stroke sits inside its sign
   box are readable.
7. Both arms are at home with grippers open.
8. The **right arm** reaches the three tools, the three slots, the two bays, the right cloth, the middle of
   the working area, the card, and the marker without extending to a joint limit.
9. The **left arm** reaches the three stray items, the bin mouth, the left cloth, and the middle of the working
   area without extending to a joint limit. It reaches no slot and no bay.
10. Both grippers come in and go out of the back strip **from the front and level**. Neither comes down onto
    the trough, the rack, or a pack from above, and neither wrist nor forearm touches the shelf above on the
    way in or out.
11. The two arms do not collide, and neither arm passes in front of the other.
12. If a place cannot be reached, re-park the base by the Base positioning steps until lines 8 to 11 hold.

### Materials checklist

1. The **workbench** stands where it lives, bolted or braced to the floor or the wall. It is not moved, not
   leaned on, and not pushed at any point.
2. A **shelf** runs along the wall directly above the back of the bench, so the only way to the back strip is
   straight in from the front and never from the top. The shelf is high enough for a gripper to come in level
   under it and low enough that nothing can be lifted over it.
3. Nothing on the bench is powered or running. If a power strip is fixed to the bench, its switch is at **OFF**
   before recording starts.
4. The **back strip** is the part of the bench top under the shelf. It carries the tool trough, the consumable
   rack, and this config's pack spot, and nothing else.
5. The **tool trough** is fixed along the middle of the back strip. It has **three slots**, open at the front,
   left to right: the **driver slot**, the **pliers slot**, and the **wrench slot**. Each slot carries its name
   on a label on its front face. All three slots start empty.
6. Each slot is cut so its tool slides straight in from the front, lies flat in it, and stays put when the
   gripper opens. No slot needs a tool to be dropped in from above.
7. The **consumable rack** is fixed on the back strip at its right end. It has **two bays**, open at the front:
   the **glove bay** on the left and the **wipe bay** on the right. Each bay carries its name on a label on its
   front face. Both bays start empty.
8. Each bay is deep enough to take its pack all the way in, and wide enough that the pack slides in without
   being squeezed or forced.
9. The **front strip** is the part of the bench top in front of the shelf. Nothing stands above it.
10. The **returns bin** is an open-top tote standing on the front strip at its left end. It is empty, it is
    heavy or braced enough not to slide when something is put in it, and its mouth is clear.
11. The **working area** is the clear middle of the front strip, between the returns bin and the checklist
    bracket. It is the only part of the bench that gets wiped.
12. **Three stray items** lie in the **left half of the working area**, left to right: the **mug**, the **stapler**,
    and the **parts box**. None of them belongs at this bench. Each one lies clear of the others, and each one
    can be picked up in one grip.
13. **Three tools** lie in the **right half of the working area**, left to right: the **screwdriver**, the
    **pliers**, and the **wrench**. Each lies flat with its handle toward the front, and each one matches one
    slot in the trough.
14. **Two consumable packs** stand on the back strip, side by side, the **glove box** on the left and the
    **wipe pack** on the right. They stand at the left end of the back strip in **Config L**, between the
    trough and the rack in **Config M**, and at the right end in **Config R**.
15. Both packs are closed, square-sided, and light enough for one gripper to hold in one grip.
16. The **left cloth** lies folded flat on the **left cloth home**, a marked spot at the front-left corner of
    the front strip, in front of the returns bin.
17. The **right cloth** lies folded flat on the **right cloth home**, a marked spot at the front-right corner
    of the front strip, in front of the checklist bracket.
18. Both cloths are damp and wrung out, so they pick dust up and do not drip.
19. There is loose dust on the working area, spread over both halves, so whether a half has been wiped is
    readable from the front.
20. The **checklist bracket** is bolted to the bench top at the right end of the front strip. It is open at the
    front, so the card can be signed where it sits.
21. The **checklist card** in the bracket is ruled into rows, one row per reset. Each row lists the four reset
    items printed across it, **sort**, **order**, **wipe**, and **restage**, and ends in an empty **sign box** at
    its right end. At least one row's sign box is empty.
22. The **marker** stands in its clip beside the bracket, point down, and it marks the card without being
    shaken or uncapped.
23. Nothing else stands anywhere in the zone within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the two cloth homes. You judge every other place by eye against
the bench itself: the back strip, the front strip, and the front edge.

* **Bench:** the workbench the base is parked at. It is never moved, never leaned on, and never pushed.
* **Shelf above:** the shelf on the wall directly over the back of the bench. It is what makes every reach into
  the back strip a front approach. Nothing ever touches it.
* **Back strip:** the bench top under the shelf. It carries the tool trough, the consumable rack, and the pack
  spot. It is never wiped.
* **Tool trough:** fixed along the middle of the back strip, three open-front slots, left to right the driver
  slot, the pliers slot, and the wrench slot. **Right gripper only.**
* **Consumable rack:** fixed at the right end of the back strip, two open-front bays, the glove bay on the left
  and the wipe bay on the right. **Right gripper only.**
* **Pack spot:** where the two packs stand on the back strip in this episode's config. Left end in Config L,
  between the trough and the rack in Config M, right end in Config R.
* **Front strip:** the bench top in front of the shelf, with open air above it.
* **Returns bin:** the open tote at the left end of the front strip. Everything that does not belong at this
  bench goes in it. **Left gripper only.**
* **Working area:** the clear middle of the front strip. Its **left half** holds the three stray items and is wiped
  by the left gripper. Its **right half** holds the three tools and is wiped by the right gripper.
* **Left cloth home:** the marked spot at the front-left corner of the front strip. **Left gripper only.**
* **Right cloth home:** the marked spot at the front-right corner of the front strip. **Right gripper only.**
* **Checklist bracket:** bolted to the bench at the right end of the front strip. It holds the checklist card.
  **Right gripper only.**
* **Marker clip:** beside the bracket, holding the marker point down. **Right gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the left end and the left half: the three stray items, the returns bin, the left cloth,
  the left half of the working area, and, in Config L only, the two packs and the hand-over at the middle.
* The **right gripper** works the right end and the right half: the three tools, the tool trough, the consumable
  rack, the right cloth, the right half of the working area, the card, and the marker.
* The **left gripper never goes right of the middle of the working area**, and the **right gripper never goes
  left of it**. The middle is where a hand-over happens in Config L, and nowhere else.
* Neither arm reaches over, under, around, or past the other, and neither reaches across the front of the other
  arm's body.
* Only one thing is moved at a time. A gripper holds one thing, and while it does, the other gripper is either
  empty or drawn **clear of the bench**.

### Arm assignments

* **Right gripper.** Picks up the three tools and slides each into its slot. Wipes the right half of the working
  area with the right cloth. Seats the glove box and the wipe pack in their bays. Signs the checklist card with
  the marker.
* **Left gripper.** Moves the three stray items into the returns bin. Wipes the left half of the working area with the
  left cloth. In **Config L** only, picks each pack off the back strip and hands it over to the right gripper.
* Nothing else is handed between grippers, and only one thing is moved at a time.

## Vocabulary

* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down onto the
  back strip, the tool trough, the consumable rack, or a pack from above. Every reach into the back strip is a
  front approach.
* **Zone:** the stretch of bench the base is parked at, from the returns bin at the left end to the checklist
  bracket at the right end.
* **Stray item:** a thing on the bench that does not belong at this bench. This episode has three: the mug, the
  stapler, and the parts box. A tool, a pack, a cloth, and the marker are not stray items.
* **In order:** the tools go into the trough in the order the slots run, left to right: the screwdriver into the
  driver slot, then the pliers into the pliers slot, then the wrench into the wrench slot.
* **Slot:** one of the three open-front cuts in the tool trough. Each one takes one named tool.
* **Bay:** one of the two open-front spaces in the consumable rack. Each one takes one named pack.
* **Seated:** the tool or the pack has gone all the way into its slot or its bay, its front face is level with the
  front of the slot or the bay, and it stays put when the gripper opens. Anything standing proud of the front, or
  lying across two slots, is not seated.
* **Pass:** one wipe. The gripper lays the cloth flat on the bench, presses it down, draws it straight in one line
  without lifting, and stops. A wipe that lifts halfway is not a pass.
* **Hand over:** one gripper gives a thing to the other above the middle of the working area. The giving gripper
  brings it to the middle and holds it still for a **half-second hold**. The taking gripper then closes on the far
  side of it. Only after the taking gripper is closed does the giving gripper open and draw back.
* **Half-second hold:** the giving gripper stops moving and stays still for about half a second, so the thing is
  not moving when the other gripper closes on it.
* **Home spot:** the marked spot a cloth lies on. The left cloth has one, and the right cloth has one.
* **Sign box:** the empty box at the right end of each row on the checklist card.
* **Today's row:** the first row on the checklist card whose sign box is empty. It is the row that gets signed,
  every time.
* **Sign:** draw one straight stroke with the marker across the sign box of today's row, from its left edge to its
  right edge, without lifting. It is the only mark the episode puts on the card.
* **Clear of the bench:** the arm is drawn back so that no part of it is over the front strip, the back strip, or
  the returns bin.

## Steps

Run Steps 1 to 5 in order, and end the episode with Step 6. The five steps are the five actions of the task, in
the task's own order: **sort the stray items, set the tools in order, wipe the bench, restage the consumables,
sign the checklist.** Only Step 4 depends on the config. Every other step is the same in all three.

### Step 1: Sort the stray items

**Goal:** all three stray items are in the returns bin, and the left half of the working area holds nothing.

The three stray items go into the bin one at a time, in the order they lie, left to right: the **mug**, then the
**stapler**, then the **parts box**. Hold the **right gripper** open and **clear of the bench** for the whole of
this step.

#### 1.1 Bin the mug

* With the **left gripper**, close on the **mug** and lift it straight up off the bench.
* With the **left gripper**, carry it level to the **returns bin** and bring it down through the mouth until it is
  just above the bottom of the bin.
* Open the **left gripper** and let the mug go. Draw the **left gripper** straight up and out of the bin mouth.
* With the **left gripper**, touch no tool, no pack, no cloth, and no part of the trough or the rack.

**Check:** the mug is in the bin and the bin has not slid or tipped. If it lands outside the bin, pick it up with
the **left gripper** and put it in the bin.

#### 1.2 Bin the stapler

* With the **left gripper**, close on the **stapler** and lift it straight up off the bench.
* With the **left gripper**, carry it level to the **returns bin** and bring it down through the mouth until it is
  just above the bottom of the bin.
* Open the **left gripper** and let the stapler go. Draw the **left gripper** straight up and out of the bin mouth.
* With the **left gripper**, carry the stapler on its own. Do not carry it together with the parts box, and do not
  let it go from above the mouth.

**Check:** the stapler is in the bin with the mug, and the bin has not slid or tipped. If it lands outside the bin,
pick it up with the **left gripper** and put it in the bin.

#### 1.3 Bin the parts box

* With the **left gripper**, close on the **parts box** and lift it straight up off the bench.
* With the **left gripper**, carry it level to the **returns bin** and bring it down through the mouth until it is
  just above the bottom of the bin.
* Open the **left gripper** and let the parts box go. Draw the **left gripper** straight up and out of the bin
  mouth, open, and take it **clear of the bench**.

**Check:** the parts box is in the bin, and the bin has not slid or tipped. If it lands outside the bin, pick it up
with the **left gripper** and put it in the bin.

**Expected state:** the mug, the stapler, and the parts box are in the returns bin. The left half of the working
area holds nothing but dust. The three tools are still in the right half.

### Step 2: Set the tools in order

**Goal:** the screwdriver, the pliers, and the wrench are each **seated** in their own slot, handle toward the
front, and the trough reads driver, pliers, wrench from left to right.

The tools go in **in order**: the **screwdriver** first, into the driver slot at the left; then the **pliers**, into
the pliers slot in the middle; then the **wrench**, into the wrench slot at the right. That is the order the tools
lie in on the bench and the order the slots run in. Hold the **left gripper** open and **clear of the bench** for
the whole of this step.

#### 2.1 Set the screwdriver

* With the **right gripper**, close on the **handle** of the screwdriver, not on its blade, and lift it straight up
  off the bench.
* With the **right gripper**, hold it level, handle toward the front and blade away from the front, and carry it
  level to the front of the **driver slot**, the left slot of the trough.
* Read the label on the front of the slot before going in.
* With the **right gripper**, line the screwdriver up straight with the slot and push it straight back into the
  slot, level, in one push, until it is all the way in.
* Push straight in only. With the **right gripper**, do not come down onto the trough from above, do not turn the
  screwdriver into the slot, and do not force it against the side of the slot.
* Open the **right gripper**, draw it straight out to the front, and take it **clear of the bench**.

**Check:** the screwdriver is **seated**: it lies flat, all the way in, handle toward the front, in the driver slot
only, and it stays put with the **right gripper** off it. If it stands proud, lies across two slots, or is in the
wrong slot, pick it up again with the **right gripper**, line it up, and push it straight into the driver slot.

#### 2.2 Set the pliers

* With the **right gripper**, close on the **handles** of the pliers, not on their jaws, and lift them straight up
  off the bench.
* With the **right gripper**, hold them level, handles toward the front and jaws away from the front, and carry
  them level to the front of the **pliers slot**, the middle slot of the trough.
* Read the label on the front of the slot before going in.
* With the **right gripper**, line the pliers up straight with the slot and push them straight back into the slot,
  level, in one push, until they are all the way in.
* Push straight in only. With the **right gripper**, do not come down onto the trough from above, do not turn the
  pliers into the slot, and do not force them against the side of the slot.
* Open the **right gripper**, draw it straight out to the front, and take it **clear of the bench**.

**Check:** the pliers are **seated** in the pliers slot, handles toward the front, and the screwdriver is still
seated in the driver slot. If the pliers stand proud, lie across two slots, or are in the wrong slot, pick them up
again with the **right gripper**, line them up, and push them straight into the pliers slot.

#### 2.3 Set the wrench

* With the **right gripper**, close on the **handle** of the wrench, not on its head, and lift it straight up off
  the bench.
* With the **right gripper**, hold it level, handle toward the front and head away from the front, and carry it
  level to the front of the **wrench slot**, the right slot of the trough.
* Read the label on the front of the slot before going in.
* With the **right gripper**, line the wrench up straight with the slot and push it straight back into the slot,
  level, in one push, until it is all the way in.
* Push straight in only. With the **right gripper**, do not come down onto the trough from above, do not turn the
  wrench into the slot, and do not force it against the side of the slot.
* Open the **right gripper**, draw it straight out to the front, and take it **clear of the bench**.

**Check:** the wrench is **seated** in the wrench slot, handle toward the front, and the screwdriver and the pliers
are still seated in their own slots. If the wrench stands proud, lies across two slots, or is in the wrong slot,
pick it up again with the **right gripper**, line it up, and push it straight into the wrench slot.

**Expected state:** all three slots are full, in order, driver, pliers, wrench from left to right. The right half
of the working area holds nothing but dust.

### Step 3: Wipe the bench

**Goal:** the bench top is wiped, half by half, and both cloths are back on their home spots.

The part of the bench that is wiped is the **working area**, the open bench top between the returns bin and the
checklist bracket. The back strip under the shelf carries the trough and the rack and is not wiped. The right half
is wiped first, then the left half.

#### 3.1 Wipe the right half

* With the **right gripper**, close on the middle of the **right cloth** and lift it straight up off the **right
  cloth home**.
* With the **right gripper**, lay the cloth flat on the working area at its **right edge**, on the back line,
  just in front of the tool trough.
* With the **right gripper**, press the cloth flat and draw it straight from the right edge in to the **middle of
  the working area**, in one **pass**, without lifting it.
* With the **right gripper**, lift the cloth just off the bench, carry it back out to the right edge, and set it
  down one cloth width forward of the last pass. Draw it in to the middle again.
* With the **right gripper**, do this a third time, along the front line of the right half.
* Three passes in all: the back line, the middle line, then the front line, each drawn from the right edge in to
  the middle.
* With the **right gripper**, keep the cloth below the shelf and off the trough and the rack, and do not push dust
  off the front edge or the right end of the bench.
* Hold the **left gripper** open and **clear of the bench** while the **right gripper** wipes.

**Check:** the right half shows no loose dust, the three passes have covered it from the trough to the front edge,
and no dust has gone over an edge. If a line of dust is left, wipe that line again with the **right gripper**.

#### 3.2 Wipe the left half

* With the **left gripper**, close on the middle of the **left cloth** and lift it straight up off the **left cloth
  home**.
* With the **left gripper**, lay the cloth flat on the working area at its **left edge**, on the back line.
* With the **left gripper**, press the cloth flat and draw it straight from the left edge in to the **middle of the
  working area**, in one **pass**, without lifting it.
* With the **left gripper**, lift the cloth just off the bench, carry it back out to the left edge, set it down one
  cloth width forward, and draw it in to the middle again.
* With the **left gripper**, do this a third time, along the front line of the left half.
* Three passes in all: the back line, the middle line, then the front line, each drawn from the left edge in to the
  middle.
* With the **left gripper**, keep the cloth clear of the returns bin, and do not push dust off the front edge or the
  left end of the bench.
* Hold the **right gripper** open and **clear of the bench** while the **left gripper** wipes.

**Check:** the left half shows no loose dust, the three passes have covered it, and no dust has gone over an edge or
into the returns bin. If a line of dust is left, wipe that line again with the **left gripper**.

#### 3.3 Put both cloths back

* With the **right gripper**, carry the right cloth back and lay it flat on the **right cloth home**, then open the
  gripper and draw it **clear of the bench**.
* With the **left gripper**, carry the left cloth back and lay it flat on the **left cloth home**, then open the
  gripper and draw it **clear of the bench**.

**Check:** each cloth lies flat on its own home spot, and neither gripper holds anything.

**Expected state:** the bench top is wiped and empty, both cloths are on their home spots, the three tools are in
their slots, and the two packs still stand at the pack spot.

### Step 4: Restage the consumables

**Goal:** the **glove box** is seated in the **glove bay** and the **wipe pack** is seated in the **wipe bay**.

The two consumable packs are restaged one at a time, the glove box first, then the wipe pack.

#### 4.1 Restage the glove box

* **IF Config L:** with the **left gripper**, close on the sides of the **glove box** at the left end of the back
  strip and draw it straight out to the front, level, from under the shelf. With the **left gripper**, carry it to
  the **middle of the working area** and hold it still for a **half-second hold**. With the **right gripper**, close
  on the far side of the box. With the **left gripper**, open and draw back **clear of the bench**.
* **IF Config M or Config R:** with the **right gripper**, close on the sides of the **glove box** where it stands
  on the back strip and draw it straight out to the front, level, from under the shelf. There is no hand-over.
* Then, in all three: with the **right gripper**, carry the box level to the front of the **glove bay**, the left
  bay of the consumable rack.
* Read the label on the front of the bay before going in.
* With the **right gripper**, line the box up square with the bay and push it straight back into the bay, level, in
  one push, until it is all the way in.
* Push straight in only. With the **right gripper**, do not come down onto the rack from above, do not turn the box
  into the bay, and do not force it.
* Open the **right gripper**, draw it straight out to the front, and take it **clear of the bench**.

**Check:** the glove box is **seated** in the glove bay: all the way in, square, its front face level with the front
of the bay, and it stays put with the **right gripper** off it. If it stands proud or sits crooked, close on it again
with the **right gripper**, draw it out, line it up, and push it straight in.

#### 4.2 Restage the wipe pack

* **IF Config L:** with the **left gripper**, close on the sides of the **wipe pack** on the back strip and draw it
  straight out to the front, level. With the **left gripper**, carry it to the **middle of the working area** and hold
  it still for a **half-second hold**. With the **right gripper**, close on the far side of it. With the **left
  gripper**, open and draw back **clear of the bench**.
* **IF Config M or Config R:** with the **right gripper**, close on the sides of the **wipe pack** where it stands on
  the back strip and draw it straight out to the front, level. There is no hand-over.
* Then, in all three: with the **right gripper**, carry the pack level to the front of the **wipe bay**, the right bay
  of the consumable rack, and read the label on the front of the bay.
* With the **right gripper**, line the pack up square with the bay and push it straight back into the bay, level, in
  one push, until it is all the way in.
* Open the **right gripper**, draw it straight out to the front, and take it **clear of the bench**.

**Check:** the wipe pack is **seated** in the wipe bay, and the glove box is still seated in the glove bay. If either
stands proud or sits crooked, close on it again with the **right gripper**, draw it out, line it up, and push it
straight in.

**Expected state:** both bays are full, the pack spot on the back strip is empty, the three slots are full, the bench
top is empty and wiped, and both grippers are clear of the bench.

### Step 5: Sign the checklist

**Goal:** **today's row** on the checklist card is **signed**, and the marker is back in its clip.

#### 5.1 Take the marker

* With the **right gripper**, close on the **barrel** of the marker, not on its point, and lift it straight up out of
  its clip.
* With the **right gripper**, carry it level to the card, from the front.
* Hold the **left gripper** open and **clear of the bench** for the whole of this step.

**Check:** the **right gripper** holds the marker by its barrel and the point hangs clear.

#### 5.2 Sign today's row

* Find **today's row** on the card: the first row whose **sign box** is empty.
* With the **right gripper**, bring the point of the marker down onto the **left edge** of that row's sign box.
* With the **right gripper**, draw one straight stroke across the sign box, from its left edge to its right edge,
  without lifting, then lift the marker straight off the card.
* With the **right gripper**, keep the stroke inside the sign box. Press only hard enough to leave a mark, not hard
  enough to move the card, the bracket, or the bench.

**Check:** today's row carries **one stroke**, inside its sign box, and no other row on the card has been marked. If
the stroke has run outside the box or come out short, leave it. Do not draw over it, do not draw a second stroke, and
do not sign a second row.

#### 5.3 Put the marker back

* With the **right gripper**, carry the marker back and stand it in its clip, point down, where it started.
* Open the **right gripper** and draw it back **clear of the bench**.

**Check:** the marker stands in its clip point down, and it stays there with the **right gripper** off it.

**Expected state:** the checklist is signed, the marker is in its clip, and both arms are clear of the bench.

### Step 6: End the episode

* Confirm the sort: the mug, the stapler, and the parts box are all in the returns bin, and nothing else is in it.
* Confirm the tools: the screwdriver, the pliers, and the wrench are each seated in their own named slot, in order,
  handles toward the front.
* Confirm the wipe: both halves of the bench top are clear of loose dust, and both cloths lie flat on their home spots.
* Confirm the consumables: the glove box is seated in the glove bay, the wipe pack is seated in the wipe bay, and the
  pack spot is empty.
* Confirm the checklist: today's row carries one stroke in its sign box, no other row is marked, and the marker stands
  in its clip.
* Confirm nothing has been dropped, nothing has been knocked over, and no dust has been pushed onto the floor.
* Confirm the bench has not shifted and the base has not moved.
* Correct any failed check before ending.
* Return both arms home with grippers open, then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the mug, the stapler, and the parts box out of the returns bin and lay them back in the left half of the working
   area, left to right in that order.
2. Take the screwdriver, the pliers, and the wrench out of their slots and lay them flat in the right half of the working
   area, left to right in that order, each with its handle toward the front.
3. Take the glove box and the wipe pack out of their bays and stand them side by side at the pack spot for the next
   episode's config, the glove box on the left and the wipe pack on the right.
4. Spread fresh loose dust over both halves of the working area, so the next episode starts with something to wipe.
5. Rinse both cloths, wring them out, and lay each one folded flat on its own home spot. Replace a cloth that has stopped
   picking dust up.
6. Check the returns bin is empty, upright, and still heavy or braced enough not to slide.
7. Check all three slots and both bays are empty, clean, and not chipped or bent, and that each one still holds its tool or
   its pack without it being forced.
8. Check the three slot labels and the two bay labels are still readable from the front, and replace any that has come off
   or faded.
9. Check the marker still marks, and replace it when it has dried out.
10. Take the card out of the bracket and put in a card with at least one row whose sign box is empty.
11. Check nothing on the bench has been powered up or left running.
12. Pick up anything that landed on the bench or the floor, and sweep up dust that went over an edge.
13. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

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

* **Visible cue:** a gripper comes down onto the back strip, the tool trough, the consumable rack, or a pack from above
  instead of coming in level from the front, or a wrist, forearm, tool, pack, or cloth knocks, scrapes, or rests on the
  shelf on the way in or out.
* **SOP rule broken:** Steps 2.1 to 2.3, 3.1, and 4.1 to 4.2, every reach into the back strip is a front approach, level,
  straight in and straight out.
* **Coaching note:** straight in from the front, straight out the same way. There is no way in from the top.

**Violation: Leaned on or pushed the bench**

* **Visible cue:** a gripper, wrist, or forearm rests on the bench top, the trough, the rack, the returns bin, or the
  checklist bracket; the bench or the bin rocks, slides, or shifts; or a push, a wipe, or the signing stroke presses hard
  enough to move the bin, the card, or the bracket.
* **SOP rule broken:** Steps 1 to 5, the bench carries no weight and nothing fixed to it is pushed out of place.
* **Coaching note:** the arm holds itself up. Press only as hard as the push, the wipe, or the stroke needs.

**Violation: Stray item left out or put somewhere other than the returns bin**

* **Visible cue:** the episode ends with the mug, the stapler, or the parts box still on the bench; a stray item is put on
  the back strip, in a slot, in a bay, or on a cloth home instead of in the returns bin; or a stray item is let go above
  the bin mouth and falls in.
* **SOP rule broken:** Steps 1.1 to 1.3, the **left gripper** carries each stray item into the bin and lets it go just
  above the bottom, one at a time.
* **Coaching note:** three stray items, three trips, and let each one go low in the bin. Something dropped from the rim
  bounces out.

**Violation: Something binned that is not a stray item**

* **Visible cue:** a tool, a consumable pack, a cloth, or the marker goes into the returns bin.
* **SOP rule broken:** Step 1, only the mug, the stapler, and the parts box go in the returns bin. Tools go in their slots
  and packs go in their bays.
* **Coaching note:** the bin takes what does not live here. A tool in the bin is a tool the next shift cannot find.

**Violation: Tool put in the wrong slot or out of order**

* **Visible cue:** the screwdriver, the pliers, or the wrench goes into a slot whose label names a different tool; a tool
  lies across two slots; or the tools go in out of order, the pliers or the wrench before the screwdriver, or the wrench
  before the pliers.
* **SOP rule broken:** Steps 2.1 to 2.3, read the label and push each tool into its own named slot, screwdriver first, then
  pliers, then wrench.
* **Coaching note:** read the label before the push, and take the tools left to right. The trough is the whole point of
  setting tools in order.

**Violation: Tool not seated, or forced in**

* **Visible cue:** a tool stands proud of the front of its slot, sits crooked in it, falls out when the **right gripper**
  opens, is turned or levered into the slot, or is pushed hard against the side of a slot.
* **SOP rule broken:** Steps 2.1 to 2.3, line the tool up straight and push it straight back into the slot in one level push
  until it is seated.
* **Coaching note:** line it up first, then one straight push. A tool that will not go in straight is in the wrong slot.

**Violation: Tool held by its working end or laid in the wrong way round**

* **Visible cue:** the **right gripper** closes on the blade, the jaws, or the head of a tool instead of its handle, or a tool
  ends up in its slot with its handle away from the front.
* **SOP rule broken:** Steps 2.1 to 2.3, the **right gripper** takes each tool by its handle and puts it in its slot handle
  toward the front.
* **Coaching note:** handle in the gripper, handle to the front. The next shift picks it up the same way every time.

**Violation: Wipe pattern wrong**

* **Visible cue:** a half gets fewer or more than three passes; a pass runs from the middle out instead of from the outer edge
  in; the cloth lifts partway through a pass; the passes do not step forward from the back line to the front line; or part of a
  half is never covered.
* **SOP rule broken:** Steps 3.1 and 3.2, wipe each half with three passes, the back line, the middle line, then the front line,
  each drawn from the outer edge in to the middle without lifting.
* **Coaching note:** three passes, outer edge to the middle, back to front. Count them as you go.

**Violation: Dust pushed off the bench**

* **Visible cue:** a pass carries dust over the front edge, over the left or right end of the bench, onto the floor, or into
  the returns bin.
* **SOP rule broken:** Steps 3.1 and 3.2, each pass is drawn in to the middle so the cloth keeps the dust, and nothing is pushed
  off an edge.
* **Coaching note:** the cloth holds the dust. Anything that goes over the edge, someone else has to sweep.

**Violation: Wrong cloth on a half**

* **Visible cue:** the **right gripper** wipes with the left cloth, the **left gripper** wipes with the right cloth, one cloth
  is used on both halves, or a gripper takes a cloth from the other end's home spot.
* **SOP rule broken:** Steps 3.1 and 3.2, the **right gripper** wipes the right half with the right cloth and the **left
  gripper** wipes the left half with the left cloth.
* **Coaching note:** each end has its own cloth. Carrying one across the bench carries the dust with it.

**Violation: Cloth not put back on its home spot**

* **Visible cue:** a cloth is left on the working area, on the back strip, in the returns bin, or still in a gripper at the end
  of the episode; a cloth is laid down somewhere other than its own home spot; or a cloth is left bunched instead of flat.
* **SOP rule broken:** Step 3.3, each gripper lays its own cloth flat on its own home spot before the step ends.
* **Coaching note:** same spot, flat, every time. A cloth left on the bench is dust back on the bench.

**Violation: Pack put in the wrong bay**

* **Visible cue:** the glove box goes into the wipe bay, the wipe pack goes into the glove bay, or a pack goes into a slot in
  the tool trough.
* **SOP rule broken:** Steps 4.1 and 4.2, read the bay label and push the glove box into the glove bay and the wipe pack into
  the wipe bay.
* **Coaching note:** read the bay label before the push, the same way you read the slot label.

**Violation: Pack not seated, or left on the back strip**

* **Visible cue:** a pack stands proud of the front of its bay, sits crooked in it, falls out when the **right gripper** opens,
  is turned or forced into the bay, or is still standing at the pack spot when the episode ends.
* **SOP rule broken:** Steps 4.1 and 4.2, each pack is drawn straight out to the front, lined up square, and pushed straight
  into its bay until it is seated.
* **Coaching note:** square it up, one straight push, all the way in. A pack left on the bench is a pack nobody can find.

**Violation: Hand-over done wrong**

* **Visible cue:** in Config L the **left gripper** opens before the **right gripper** has closed on the pack; the pack is still
  moving when the **right gripper** closes, with no half-second hold; the pack is dropped or passed below the middle of the
  working area; or a hand-over happens in Config M or Config R, where none is called for.
* **SOP rule broken:** Steps 4.1 and 4.2, in Config L the **left gripper** brings the pack to the middle, holds it still for a
  half-second hold, and opens only after the **right gripper** has closed on the far side.
* **Coaching note:** stop, hold still, let the other gripper take it, then open. In Config M and R nothing changes hands.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the bench is not set up in: the wrong gripper picks a pack up, the **left gripper**
  reaches for the packs in Config M or R, the **right gripper** reaches for them in Config L, an arm reaches for a pack spot
  that is empty, or the packs are moved to a different spot on the back strip before being picked up.
* **SOP rule broken:** Steps 4.1 and 4.2, look at the bench, find the pack spot, and follow the IF line that matches the config
  the episode is set up in.
* **Coaching note:** look at the bench before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** a tool goes in its slot before all three stray items are in the bin; a cloth touches the bench before all
  three tools are in their slots; a pass goes around a stray item or a tool still lying on the working area; a pack goes in its
  bay before the bench is wiped; the card is signed before both packs are seated; or a stray item or a pack goes in out of its
  named order.
* **SOP rule broken:** Steps 1 to 5, sort the stray items, set the tools in order, wipe the bench, restage the consumables,
  then sign the checklist.
* **Coaching note:** the order is the task. Each step leaves the bench ready for the next one.

**Violation: Checklist signed wrong**

* **Visible cue:** the card is not signed at all; the stroke goes somewhere other than the sign box, over the printed items or
  between rows; a row that is already signed is signed again instead of today's row; more than one row is signed; a second
  stroke is drawn in the same box; or a stroke that ran outside its box is drawn over.
* **SOP rule broken:** Step 5.2, find today's row and draw one stroke across its sign box, left edge to right edge, once.
* **Coaching note:** first row with an empty sign box, one stroke, and leave it. The card is the only record the reset happened.

**Violation: Marker not put back in its clip**

* **Visible cue:** the marker is left on the bench, on the card, in the bracket, in the returns bin, or in a gripper at the end;
  it is put back point up; or the **right gripper** closes on its point instead of its barrel.
* **SOP rule broken:** Steps 5.1 and 5.3, the **right gripper** takes the marker by its barrel and stands it back in its clip
  point down.
* **Coaching note:** barrel in the gripper, point down in the clip. A marker left out dries out.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two stray items, two tools, or both packs together; both grippers carry different things at
  the same time; or a gripper holds something while the other gripper works instead of being drawn clear of the bench.
* **SOP rule broken:** Steps 1 to 5, one gripper holds one thing, and while it does the other gripper is empty or clear of the
  bench.
* **Coaching note:** one thing, one trip. Two at once is what puts something on the floor.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a stray item
  item outside the bin, a tool standing proud or in the wrong slot, a line of dust left on a half, a pack sitting crooked, a
  cloth off its home spot, or the marker not in its clip.
* **SOP rule broken:** Steps 1.1 to 5.3, run each check and correct what it finds by the retry written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a stray item, a tool, a pack, a cloth, or the marker is dropped on the bench or the floor; the returns bin is
  knocked over or slid out of place; the card is knocked out of its bracket; or an arm knocks a tool out of its slot or a pack
  out of its bay.
* **SOP rule broken:** Steps 1 to 5, nothing is dropped or knocked out of its place, and every gripper comes out to the front
  the way it went in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **right gripper** touches a stray item, the returns bin, or the left cloth; the **left gripper** touches
  a tool, a slot, a bay, the right cloth, the card, or the marker; the **left gripper** goes right of the middle of the working
  area, or the **right gripper** goes left of it, other than for a Config L hand-over at the middle; or either arm passes in
  front of the other.
* **SOP rule broken:** Steps 1 to 5, the **left gripper** bins the stray items and wipes the left half, the **right gripper**
  does the tools, the right half, the packs, and the card, and the arms never cross.
* **Coaching note:** left arm works the left end, right arm works the right end, and only a Config L hand-over meets at the
  middle.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a stray item on the bench, a tool out of its slot, a half unwiped, a cloth off its home
  spot, a pack on the back strip, the card unsigned, the marker out of its clip, an arm short of home, or a gripper not fully
  open.
* **SOP rule broken:** Step 6, confirm the sort, the tools, the wipe, the consumables, the checklist, the drops, the bench, and
  the base, then return both arms home with grippers open and stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for
coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a slot label, a bay label, the working area, the bin mouth, or the card**, so which slot a tool went into,
  which bay a pack went into, whether a half came clean, or which row was signed cannot be judged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Faulty trough or rack:** a slot that will not hold its tool after a correct straight push, a bay that will not take its pack all
  the way in, or a trough or rack that comes loose from the bench.
* **Faulty returns bin:** one that tips or slides under a correctly placed stray item.
* **Damaged item:** a tool that arrives bent or broken, a pack that is burst or crushed, a mug or parts box that comes apart in the
  gripper, or a cloth that falls apart.
* **Consumables out:** no damp cloth, no card with an empty sign box, or a marker that will not mark.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a stray item, the bin mouth, a tool,
  a slot, a bay, a cloth home, the pack spot, the card, or the marker cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Move one stray item into the returns bin
2. Pick one tool up by its handle
3. Push one tool into its slot
4. Take a cloth off its home spot
5. Wipe one pass across a half of the bench
6. Lay a cloth back on its home spot
7. Draw one consumable pack out from the back strip
8. Hand one pack over at the middle of the working area
9. Push one pack into its bay
10. Take the marker out of its clip
11. Sign today's row on the checklist card
12. Stand the marker back in its clip
13. Return both arms home and end the episode
