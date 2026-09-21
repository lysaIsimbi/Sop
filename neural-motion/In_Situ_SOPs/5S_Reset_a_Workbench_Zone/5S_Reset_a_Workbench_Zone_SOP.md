# 5S Reset a Workbench Zone SOP (1x Episode: one zone, in situ)

One episode resets one workbench zone, at the bench where it stands. The base is **passive**: it has no
drive of its own, so it is pushed by hand to the front of the bench and locked there, and nothing is
carried away to a table. Everything the episode touches is already on the bench when recording starts:
the three strays, the three tools, the two consumable packs, the two cloths, the returns bin, the
checklist card in its bracket, and the marker in its clip.

The episode runs these six actions in this order and no other: **read the zone at the tag, sort the
strays into the returns bin, set the three tools in their slots, wipe the working area, restage the two
consumable packs, mark the checklist.**

The bench is worked **as found**. It is the bench at the end of a shift: three things that do not belong
here are lying on it, three tools are out of their trough, and two consumable packs have been left
standing on the back of the bench instead of in their rack. The episode ends with the strays in the
returns bin, all three tools in their own slots, the working area wiped, both packs seated in their bays,
and today's row on the checklist marked.

**This is an in-situ task, and three things follow from that.** First, a **shelf runs along the wall
directly above the back of the bench**, so **every approach to the back of the bench is from the front,
straight in, level**. No gripper comes down onto the tool trough, the consumable rack, or a pack from
above. Second, the **bench is never leaned on and never pushed**: no gripper, wrist, or forearm rests on
the bench top, the shelf, or the checklist bracket, and no push is ever hard enough to shift the bench or
the bin. Third, the **bench stays as it stands**: nothing is unbolted, the trough and the rack are never
moved, and nothing is turned to make a reach easier.

The bench is set up in one of three ways. Only the **two consumable packs** move. The strays, the tools,
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
* **Fixed roles:** the left gripper bins the strays and wipes the left half. The right gripper sets the
  tools in their slots, wipes the right half, seats both packs, and marks the checklist. The six actions
  run in the same order in every config.

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
6. Check the **left side**: the **left gripper** reaches all three strays in the left half of the working
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
6. The camera reads the **checklist card**, so which row is marked and how many marks are in it are readable.
7. The camera reads the **zone tag** on the checklist bracket and the **power strip switch** on the front
   edge of the bench.
8. Both arms are at home with grippers open.
9. The **right arm** reaches the three tools, the three slots, the two bays, the right cloth, the middle of
   the working area, the card, and the marker without extending to a joint limit.
10. The **left arm** reaches the three strays, the bin mouth, the left cloth, and the middle of the working
    area without extending to a joint limit. It reaches no slot and no bay.
11. Both grippers come in and go out of the back strip **from the front and level**. Neither comes down onto
    the trough, the rack, or a pack from above, and neither wrist nor forearm touches the shelf above on the
    way in or out.
12. The two arms do not collide, and neither arm passes in front of the other.
13. If a place cannot be reached, re-park the base by the Base positioning steps until lines 9 to 12 hold.

### Materials checklist

1. The **workbench** stands where it lives, bolted or braced to the floor or the wall. It is not moved, not
   leaned on, and not pushed at any point.
2. A **shelf** runs along the wall directly above the back of the bench, so the only way to the back strip is
   straight in from the front and never from the top. The shelf is high enough for a gripper to come in level
   under it and low enough that nothing can be lifted over it.
3. The **power strip** is fixed to the front edge of the bench. Its switch is at **OFF** and its light is out.
   Nothing on the bench is powered or running during the episode.
4. The **zone tag** hangs on the checklist bracket. It says the zone is released for reset.
5. The **back strip** is the part of the bench top under the shelf. It carries the tool trough, the consumable
   rack, and this config's pack spot, and nothing else.
6. The **tool trough** is fixed along the middle of the back strip. It has **three slots**, open at the front,
   left to right: the **driver slot**, the **pliers slot**, and the **wrench slot**. Each slot carries its name
   on a label on its front face. All three slots start empty.
7. Each slot is cut so its tool slides straight in from the front, lies flat in it, and stays put when the
   gripper opens. No slot needs a tool to be dropped in from above.
8. The **consumable rack** is fixed on the back strip at its right end. It has **two bays**, open at the front:
   the **glove bay** on the left and the **wipe bay** on the right. Each bay carries its name on a label on its
   front face. Both bays start empty.
9. Each bay is deep enough to take its pack all the way in, and wide enough that the pack slides in without
   being squeezed or forced.
10. The **front strip** is the part of the bench top in front of the shelf. Nothing stands above it.
11. The **returns bin** is an open-top tote standing on the front strip at its left end. It is empty, it is
    heavy or braced enough not to slide when something is put in it, and its mouth is clear.
12. The **working area** is the clear middle of the front strip, between the returns bin and the checklist
    bracket. It is the only part of the bench that gets wiped.
13. **Three strays** lie in the **left half of the working area**, left to right: the **mug**, the **stapler**,
    and the **parts box**. None of them belongs at this bench. Each one lies clear of the others, and each one
    can be picked up in one grip.
14. **Three tools** lie in the **right half of the working area**, left to right: the **screwdriver**, the
    **pliers**, and the **wrench**. Each lies flat with its handle toward the front, and each one matches one
    slot in the trough.
15. **Two consumable packs** stand on the back strip, side by side, the **glove box** on the left and the
    **wipe pack** on the right. They stand at the left end of the back strip in **Config L**, between the
    trough and the rack in **Config M**, and at the right end in **Config R**.
16. Both packs are closed, square-sided, and light enough for one gripper to hold in one grip.
17. The **left cloth** lies folded flat on the **left cloth home**, a marked spot at the front-left corner of
    the front strip, in front of the returns bin.
18. The **right cloth** lies folded flat on the **right cloth home**, a marked spot at the front-right corner
    of the front strip, in front of the checklist bracket.
19. Both cloths are damp and wrung out, so they pick dust up and do not drip.
20. There is loose dust on the working area, spread over both halves, so whether a half has been wiped is
    readable from the front.
21. The **checklist bracket** is bolted to the bench top at the right end of the front strip. It is open at the
    front, so the card can be marked where it sits.
22. The **checklist card** in the bracket is ruled into rows of **four boxes**, headed left to right **sort**,
    **order**, **wipe**, and **restage**. At least one row is completely empty.
23. The **marker** stands in its clip beside the bracket, point down, and it marks the card without being
    shaken or uncapped.
24. Nothing else stands anywhere in the zone within either arm's reach.

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
* **Working area:** the clear middle of the front strip. Its **left half** holds the three strays and is wiped
  by the left gripper. Its **right half** holds the three tools and is wiped by the right gripper.
* **Left cloth home:** the marked spot at the front-left corner of the front strip. **Left gripper only.**
* **Right cloth home:** the marked spot at the front-right corner of the front strip. **Right gripper only.**
* **Checklist bracket:** bolted to the bench at the right end of the front strip. It holds the checklist card
  and carries the zone tag. **Right gripper only.**
* **Marker clip:** beside the bracket, holding the marker point down. **Right gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the left end and the left half: the three strays, the returns bin, the left cloth,
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
  area with the right cloth. Seats the glove box and the wipe pack in their bays. Marks the checklist card with
  the marker.
* **Left gripper.** Moves the three strays into the returns bin. Wipes the left half of the working area with the
  left cloth. In **Config L** only, picks each pack off the back strip and hands it over to the right gripper.
* Nothing else is handed between grippers, and only one thing is moved at a time.

## Vocabulary

* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down onto the
  back strip, the tool trough, the consumable rack, or a pack from above. Every reach into the back strip is a
  front approach.
* **Zone:** the stretch of bench the base is parked at, from the returns bin at the left end to the checklist
  bracket at the right end.
* **Zone tag:** the tag hanging on the checklist bracket that says the zone is released for reset.
* **Stray:** a thing on the bench that does not belong at this bench. This episode has three: the mug, the
  stapler, and the parts box. A tool, a pack, a cloth, and the marker are not strays.
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
* **Today's row:** the first row on the checklist card whose four boxes are all empty. It is the row that gets
  marked, every time.
* **Clear of the bench:** the arm is drawn back so that no part of it is over the front strip, the back strip, or
  the returns bin.

## Steps

Run Step 1, then Step 2. Then run Step 3 three times: once for the **screwdriver**, once for the **pliers**,
and once for the **wrench**, in that order. Then Steps 4, 5, and 6, and end the episode with Step 7. Only
Step 5 depends on the config. Every other step is the same in all three.

### Step 1: Read the zone at the tag

**Goal:** the zone is released and dead, and both arms have touched nothing yet.

* Hold both arms **clear of the bench**. Touch nothing.
* Read the **power strip** on the front edge: its switch is at **OFF** and its light is out.
* Read the **zone tag** on the checklist bracket: it is there, and it says the zone is released for reset.
* Look across the working area: the three strays lie in the left half, the three tools lie in the right half.
* Look across the back strip: all three slots are empty, both bays are empty, and the two packs stand at this
  config's pack spot.

**Check:** the switch reads OFF, the light is out, the tag is on the bracket, and nothing on the bench is
running. If the switch is not at OFF, if the light is on, if there is no tag, or if anything on the bench is
running, do not touch the bench. End the episode and report it.

**Expected state:** nothing has moved, both grippers are open and clear of the bench, and there is loose dust
on both halves of the working area.

### Step 2: Sort the strays into the returns bin

**Goal:** all three strays are in the returns bin, and the left half of the working area holds nothing.

* With the **left gripper**, close on the **mug** and lift it straight up off the bench.
* With the **left gripper**, carry it level to the **returns bin** and bring it down through the mouth until it
  is just above the bottom of the bin.
* Open the **left gripper** and let the mug go. Draw the **left gripper** straight up and out of the bin mouth.
* With the **left gripper**, do the same for the **stapler**, then for the **parts box**, in that order. Go back
  to the top of this step for each one.
* Move one stray at a time. With the **left gripper**, do not carry two together and do not drop one in from
  above the mouth.
* With the **left gripper**, touch no tool, no pack, no cloth, and no part of the trough or the rack.
* Hold the **right gripper** open and **clear of the bench** for the whole of this step.

**Check:** after each one, the stray is in the bin and the bin has not slid or tipped. If a stray lands outside
the bin, pick it up with the **left gripper** and put it in the bin.

**Expected state:** the mug, the stapler, and the parts box are in the returns bin. The left half of the working
area holds nothing but dust. The three tools are still in the right half.

### Step 3: Set one tool in its slot

Run this step once for the **screwdriver**, then once for the **pliers**, then once for the **wrench**.

**Goal:** the tool is **seated** in its own slot, handle toward the front.

#### 3.1 Pick the tool up

* With the **right gripper**, close on the **handle** of the tool, not on its working end, and lift it straight
  up off the bench.
* With the **right gripper**, hold it level, with its handle toward the front and its working end away from the
  front.
* Hold the **left gripper** open and **clear of the bench**.

**Check:** the **right gripper** holds one tool by its handle, level, and nothing else has been lifted with it.

#### 3.2 Slide it into its slot

* With the **right gripper**, carry the tool level to the front of its own slot: the **driver slot** for the
  screwdriver, the **pliers slot** for the pliers, the **wrench slot** for the wrench.
* Read the label on the front of the slot before going in.
* With the **right gripper**, line the tool up straight with the slot and push it straight back into the slot,
  level, in one push, until it is all the way in.
* Push straight in only. With the **right gripper**, do not come down onto the trough from above, do not turn
  the tool into the slot, and do not force it against the side of a slot.
* Open the **right gripper**, draw it straight out to the front, and take it **clear of the bench**.

**Check:** the tool is **seated**: it lies flat, all the way in, handle toward the front, and it stays put with
the **right gripper** off it. It is in the slot whose label matches it, and it lies in one slot only. If it
stands proud, lies across two slots, or is in the wrong slot, pick it up again with the **right gripper**, line
it up, and push it straight into the right slot.

**Expected state:** this tool is in its slot. Go back to 3.1 for the next tool. After the wrench, the right half
of the working area holds nothing but dust, and all three slots are full.

### Step 4: Wipe the working area

**Goal:** both halves of the working area are wiped, and both cloths are back on their home spots.

#### 4.1 Wipe the right half

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

#### 4.2 Wipe the left half

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

#### 4.3 Put both cloths back

* With the **right gripper**, carry the right cloth back and lay it flat on the **right cloth home**, then open the
  gripper and draw it **clear of the bench**.
* With the **left gripper**, carry the left cloth back and lay it flat on the **left cloth home**, then open the
  gripper and draw it **clear of the bench**.

**Check:** each cloth lies flat on its own home spot, and neither gripper holds anything.

**Expected state:** the whole working area is wiped and empty, both cloths are on their home spots, the three tools
are in their slots, and the two packs still stand at the pack spot.

### Step 5: Restage the two consumable packs

**Goal:** the **glove box** is seated in the **glove bay** and the **wipe pack** is seated in the **wipe bay**.

#### 5.1 Put the glove box in its bay

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

#### 5.2 Put the wipe pack in its bay

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

**Expected state:** both bays are full, the pack spot on the back strip is empty, the three slots are full, the working
area is empty and wiped, and both grippers are clear of the bench.

### Step 6: Mark the checklist

**Goal:** **today's row** on the checklist card carries four marks, and the marker is back in its clip.

#### 6.1 Take the marker

* With the **right gripper**, close on the **barrel** of the marker, not on its point, and lift it straight up out of
  its clip.
* With the **right gripper**, carry it level to the card, from the front.
* Hold the **left gripper** open and **clear of the bench** for the whole of this step.

**Check:** the **right gripper** holds the marker by its barrel and the point hangs clear.

#### 6.2 Mark today's row

* Find **today's row** on the card: the first row whose four boxes are all empty.
* With the **right gripper**, draw one straight downward mark in the **sort** box of that row.
* With the **right gripper**, mark the **order** box, then the **wipe** box, then the **restage** box, in that order.
* With the **right gripper**, keep each mark inside its own box. Press only hard enough to leave a mark, not hard enough
  to move the card, the bracket, or the bench.

**Check:** today's row carries **four marks**, one in each box, each inside its box, and no other row on the card has
been marked. If a mark has run outside its box, leave it. Do not mark over it and do not mark a second row.

#### 6.3 Put the marker back

* With the **right gripper**, carry the marker back and stand it in its clip, point down, where it started.
* Open the **right gripper** and draw it back **clear of the bench**.

**Check:** the marker stands in its clip point down, and it stays there with the **right gripper** off it.

**Expected state:** the reset is marked, the marker is in its clip, and both arms are clear of the bench.

### Step 7: End the episode

* Confirm the sort: the mug, the stapler, and the parts box are all in the returns bin, and nothing else is in it.
* Confirm the tools: the screwdriver, the pliers, and the wrench are each seated in their own named slot, handles toward
  the front.
* Confirm the wipe: both halves of the working area are clear of loose dust, and both cloths lie flat on their home spots.
* Confirm the packs: the glove box is seated in the glove bay, the wipe pack is seated in the wipe bay, and the pack spot
  is empty.
* Confirm the card: today's row carries four marks, no other row is marked, and the marker stands in its clip.
* Confirm nothing has been dropped, nothing has been knocked over, and no dust has been pushed onto the floor.
* Confirm the bench: the power strip is still at OFF, the zone tag is still on the bracket, and the bench has not shifted.
* Confirm the base has not moved.
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
10. Take the card out of the bracket and put in a card with at least one completely empty row.
11. Check the power strip is still at OFF with its light out, and the zone tag is still on the bracket.
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
* **SOP rule broken:** Steps 1 to 7, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Approached from above or fouled the shelf**

* **Visible cue:** a gripper comes down onto the back strip, the tool trough, the consumable rack, or a pack from above
  instead of coming in level from the front, or a wrist, forearm, tool, pack, or cloth knocks, scrapes, or rests on the
  shelf on the way in or out.
* **SOP rule broken:** Steps 3.2, 4.1, and 5.1 to 5.2, every reach into the back strip is a front approach, level, straight
  in and straight out.
* **Coaching note:** straight in from the front, straight out the same way. There is no way in from the top.

**Violation: Leaned on or pushed the bench**

* **Visible cue:** a gripper, wrist, or forearm rests on the bench top, the trough, the rack, the returns bin, or the
  checklist bracket; the bench or the bin rocks, slides, or shifts; or a push, a wipe, or a mark presses hard enough to move
  the bin, the card, or the bracket.
* **SOP rule broken:** Steps 2, 3.2, 4.1, 4.2, 5.1, 5.2, and 6.2, the bench carries no weight and nothing fixed to it is
  pushed out of place.
* **Coaching note:** the arm holds itself up. Press only as hard as the push, the wipe, or the mark needs.

**Violation: Worked a zone that was not released**

* **Visible cue:** an arm goes in to the bench while the power strip switch is not at OFF, while its light is on, while no
  zone tag hangs on the bracket, or while something on the bench is running.
* **SOP rule broken:** Step 1, read the switch and the tag first and only reset a zone whose switch is at OFF, whose light is
  out, and whose tag is on the bracket.
* **Coaching note:** read the switch and the tag before the arms move. A live bench is not a released zone.

**Violation: Stray left out or put somewhere other than the returns bin**

* **Visible cue:** the episode ends with the mug, the stapler, or the parts box still on the bench; a stray is put on the back
  strip, in a slot, in a bay, or on a cloth home instead of in the returns bin; or a stray is let go above the bin mouth and
  falls in.
* **SOP rule broken:** Step 2, the **left gripper** carries each stray into the bin and lets it go just above the bottom, one
  at a time.
* **Coaching note:** three strays, three trips, and let each one go low in the bin. Something dropped from the rim bounces out.

**Violation: Something binned that is not a stray**

* **Visible cue:** a tool, a consumable pack, a cloth, or the marker goes into the returns bin.
* **SOP rule broken:** Step 2, only the mug, the stapler, and the parts box go in the returns bin. Tools go in their slots and
  packs go in their bays.
* **Coaching note:** the bin takes what does not live here. A tool in the bin is a tool the next shift cannot find.

**Violation: Tool put in the wrong slot**

* **Visible cue:** the screwdriver, the pliers, or the wrench goes into a slot whose label names a different tool, or a tool
  lies across two slots.
* **SOP rule broken:** Step 3.2, read the label and push each tool into its own named slot, the driver slot, the pliers slot,
  or the wrench slot.
* **Coaching note:** read the label before the push. The trough is the whole point of setting tools in order.

**Violation: Tool not seated, or forced in**

* **Visible cue:** a tool stands proud of the front of its slot, sits crooked in it, falls out when the **right gripper**
  opens, is turned or levered into the slot, or is pushed hard against the side of a slot.
* **SOP rule broken:** Step 3.2, line the tool up straight and push it straight back into the slot in one level push until it
  is seated.
* **Coaching note:** line it up first, then one straight push. A tool that will not go in straight is in the wrong slot.

**Violation: Tool held by its working end or laid in the wrong way round**

* **Visible cue:** the **right gripper** closes on the blade, the jaws, or the head of a tool instead of its handle, or a tool
  ends up in its slot with its handle away from the front.
* **SOP rule broken:** Steps 3.1 and 3.2, the **right gripper** takes each tool by its handle and puts it in its slot handle
  toward the front.
* **Coaching note:** handle in the gripper, handle to the front. The next shift picks it up the same way every time.

**Violation: Wipe pattern wrong**

* **Visible cue:** a half gets fewer or more than three passes; a pass runs from the middle out instead of from the outer edge
  in; the cloth lifts partway through a pass; the passes do not step forward from the back line to the front line; or part of a
  half is never covered.
* **SOP rule broken:** Steps 4.1 and 4.2, wipe each half with three passes, the back line, the middle line, then the front line,
  each drawn from the outer edge in to the middle without lifting.
* **Coaching note:** three passes, outer edge to the middle, back to front. Count them as you go.

**Violation: Dust pushed off the bench**

* **Visible cue:** a pass carries dust over the front edge, over the left or right end of the bench, onto the floor, or into
  the returns bin.
* **SOP rule broken:** Steps 4.1 and 4.2, each pass is drawn in to the middle so the cloth keeps the dust, and nothing is pushed
  off an edge.
* **Coaching note:** the cloth holds the dust. Anything that goes over the edge, someone else has to sweep.

**Violation: Wrong cloth on a half**

* **Visible cue:** the **right gripper** wipes with the left cloth, the **left gripper** wipes with the right cloth, one cloth
  is used on both halves, or a gripper takes a cloth from the other end's home spot.
* **SOP rule broken:** Steps 4.1 and 4.2, the **right gripper** wipes the right half with the right cloth and the **left
  gripper** wipes the left half with the left cloth.
* **Coaching note:** each end has its own cloth. Carrying one across the bench carries the dust with it.

**Violation: Cloth not put back on its home spot**

* **Visible cue:** a cloth is left on the working area, on the back strip, in the returns bin, or still in a gripper at the end
  of the episode; a cloth is laid down somewhere other than its own home spot; or a cloth is left bunched instead of flat.
* **SOP rule broken:** Step 4.3, each gripper lays its own cloth flat on its own home spot before the step ends.
* **Coaching note:** same spot, flat, every time. A cloth left on the bench is dust back on the bench.

**Violation: Pack put in the wrong bay**

* **Visible cue:** the glove box goes into the wipe bay, the wipe pack goes into the glove bay, or a pack goes into a slot in
  the tool trough.
* **SOP rule broken:** Steps 5.1 and 5.2, read the bay label and push the glove box into the glove bay and the wipe pack into
  the wipe bay.
* **Coaching note:** read the bay label before the push, the same way you read the slot label.

**Violation: Pack not seated, or left on the back strip**

* **Visible cue:** a pack stands proud of the front of its bay, sits crooked in it, falls out when the **right gripper** opens,
  is turned or forced into the bay, or is still standing at the pack spot when the episode ends.
* **SOP rule broken:** Steps 5.1 and 5.2, each pack is drawn straight out to the front, lined up square, and pushed straight
  into its bay until it is seated.
* **Coaching note:** square it up, one straight push, all the way in. A pack left on the bench is a pack nobody can find.

**Violation: Hand-over done wrong**

* **Visible cue:** in Config L the **left gripper** opens before the **right gripper** has closed on the pack; the pack is still
  moving when the **right gripper** closes, with no half-second hold; the pack is dropped or passed below the middle of the
  working area; or a hand-over happens in Config M or Config R, where none is called for.
* **SOP rule broken:** Steps 5.1 and 5.2, in Config L the **left gripper** brings the pack to the middle, holds it still for a
  half-second hold, and opens only after the **right gripper** has closed on the far side.
* **Coaching note:** stop, hold still, let the other gripper take it, then open. In Config M and R nothing changes hands.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the bench is not set up in: the wrong gripper picks a pack up, the **left gripper**
  reaches for the packs in Config M or R, the **right gripper** reaches for them in Config L, an arm reaches for a pack spot
  that is empty, or the packs are moved to a different spot on the back strip before being picked up.
* **SOP rule broken:** Steps 5.1 and 5.2, look at the bench, find the pack spot, and follow the IF line that matches the config
  the episode is set up in.
* **Coaching note:** look at the bench before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** an arm touches the bench before the switch and the tag are read; a tool goes in its slot before all three
  strays are in the bin; a cloth touches the bench before all three tools are in their slots; a pass goes around a stray or a
  tool still lying on the working area; a pack goes in its bay before the working area is wiped; the card is marked before the
  packs are seated; or a tool or a pack goes in out of its named order.
* **SOP rule broken:** Steps 1 to 6, read the zone, sort the strays, set the tools in their slots, wipe the working area,
  restage the packs, then mark the card.
* **Coaching note:** the order is the task. Each phase leaves the bench ready for the next one.

**Violation: Checklist marked wrong**

* **Visible cue:** the card is not marked at all; a row gets fewer or more than four marks; a row that already carried marks is
  marked instead of today's row; more than one row is marked; the four boxes are marked out of order; or a mark drawn outside
  its box is marked over.
* **SOP rule broken:** Step 6.2, find today's row and mark the sort box, the order box, the wipe box, and the restage box, in
  that order, one mark each.
* **Coaching note:** first empty row, four boxes, left to right, once each. The card is the only record the reset happened.

**Violation: Marker not put back in its clip**

* **Visible cue:** the marker is left on the bench, on the card, in the bracket, in the returns bin, or in a gripper at the end;
  it is put back point up; or the **right gripper** closes on its point instead of its barrel.
* **SOP rule broken:** Steps 6.1 and 6.3, the **right gripper** takes the marker by its barrel and stands it back in its clip
  point down.
* **Coaching note:** barrel in the gripper, point down in the clip. A marker left out dries out.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two strays, two tools, or both packs together; both grippers carry different things at the
  same time; or a gripper holds something while the other gripper works instead of being drawn clear of the bench.
* **SOP rule broken:** Steps 2 to 6, one gripper holds one thing, and while it does the other gripper is empty or clear of the
  bench.
* **Coaching note:** one thing, one trip. Two at once is what puts something on the floor.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a stray
  outside the bin, a tool standing proud or in the wrong slot, a line of dust left on a half, a pack sitting crooked, a cloth off
  its home spot, or the marker not in its clip.
* **SOP rule broken:** Steps 1 to 6.3, run each check and correct what it finds by the retry written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a stray, a tool, a pack, a cloth, or the marker is dropped on the bench or the floor; the returns bin is
  knocked over or slid out of place; the card is knocked out of its bracket; or an arm knocks a tool out of its slot or a pack out
  of its bay.
* **SOP rule broken:** Steps 2 to 6, nothing is dropped or knocked out of its place, and every gripper comes out to the front the
  way it went in.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong arm used**

* **Visible cue:** the **right gripper** touches a stray, the returns bin, or the left cloth; the **left gripper** touches a tool,
  a slot, a bay, the right cloth, the card, or the marker; the **left gripper** goes right of the middle of the working area, or
  the **right gripper** goes left of it, other than for a Config L hand-over at the middle; or either arm passes in front of the
  other.
* **SOP rule broken:** Steps 2 to 6, the **left gripper** bins the strays and wipes the left half, the **right gripper** does the
  tools, the right half, the packs, and the card, and the arms never cross.
* **Coaching note:** left arm works the left end, right arm works the right end, and only a Config L hand-over meets at the middle.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a stray on the bench, a tool out of its slot, a half unwiped, a cloth off its home spot, a
  pack on the back strip, the card unmarked, the marker out of its clip, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 7, confirm the sort, the tools, the wipe, the packs, the card, the drops, the bench, and the base, then
  return both arms home with grippers open and stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for
coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a slot label, a bay label, the working area, the bin mouth, or the card**, so which slot a tool went into,
  which bay a pack went into, whether a half came clean, or which row was marked cannot be judged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Faulty trough or rack:** a slot that will not hold its tool after a correct straight push, a bay that will not take its pack all
  the way in, or a trough or rack that comes loose from the bench.
* **Faulty returns bin:** one that tips or slides under a correctly placed stray.
* **Damaged item:** a tool that arrives bent or broken, a pack that is burst or crushed, a mug or parts box that comes apart in the
  gripper, or a cloth that falls apart.
* **Consumables out:** no damp cloth, no card with an empty row, or a marker that will not mark.
* **Zone not released:** the power strip not at OFF, its light on, no zone tag on the bracket, or something on the bench running when
  the episode starts.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a stray, the bin mouth, a tool,
  a slot, a bay, a cloth home, the pack spot, the card, or the marker cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Read the power switch and the zone tag
2. Move one stray into the returns bin
3. Pick one tool up by its handle
4. Push one tool into its slot
5. Take a cloth off its home spot
6. Wipe one pass across a half of the working area
7. Lay a cloth back on its home spot
8. Draw one consumable pack out from the back strip
9. Hand one pack over at the middle of the working area
10. Push one pack into its bay
11. Take the marker out of its clip
12. Mark one box on the checklist card
13. Stand the marker back in its clip
14. Return both arms home and end the episode
