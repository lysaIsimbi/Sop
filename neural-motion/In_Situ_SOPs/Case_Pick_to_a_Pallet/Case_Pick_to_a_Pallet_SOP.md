# Case-Pick to a Pallet SOP (1x Episode: six cases, in situ)

One episode pulls six cases off a fixed rack and builds them into one stable load on a pallet, at the rack where the cases
live. The base is **passive**: it has no drive of its own, so it is pushed by hand to the front of the rack and locked there,
and nothing is carried away to a table. Everything the episode touches is already at the rack when recording starts: the six
cases on the rack levels, the scanner in its holster, and the pallet on its stand with the pick ticket in its clip.

The episode runs these four actions in this order and no other: **pull six cases from the rack levels to the pallet, build them
in the stable pattern, label out, scan each case.** Scanning is not saved for the end: each case is scanned straight after it
comes off the rack, before it goes onto the pallet and before the next line is read.

The rack is worked **as found**. Each of its three levels holds two cases. The **pallet** stands empty on its **pallet stand**
against one end of the rack, and the **pick ticket** sits in the ticket clip on the stand. The episode ends with all six cases on
the pallet in the **3-2-1 pattern**, every label facing the front, every case scanned green, and every rack position empty.

**The pick ticket sets the order.** It is read top to bottom, one line at a time. Each line names a **rack position** and the
case's **SKU**, and the quantity, which is always one. The order of the six lines changes from episode to episode, so the ticket
is read every time and never worked from memory. The ticket decides which case comes next. The pattern decides where it goes:
the cases fill the pallet places in number order, 1 to 6, whatever the rack position they came from.

**This is an in-situ task, and three things follow from that.** First, **each rack level has a beam or deck directly above
it**, so **every reach into a rack position is from the front, straight in, level**. No gripper comes down onto a case on the
rack from above. Second, the **rack, the pallet stand, and the load are never leaned on and never pushed**: no gripper, wrist, or
forearm rests on a beam, an upright, the stand, or a case already on the pallet. Third, **each case goes from its rack position to
its pallet place and nowhere else**: nothing is set down on a beam, another level, the stand, or the floor on the way.

The rack is set up in one of two ways. Only the **pallet stand** moves. The rack positions, the cases on them, and the scanner
holster are in the same place in both.

* **Config L:** the pallet stand stands against the **left end** of the rack.
* **Config R:** the pallet stand stands against the **right end** of the rack.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the setup it says so on
an **IF** line. Look at the rack and follow the line that matches.

What stays constant across all sessions:

* **Column rule:** the **left gripper** pulls from the **left column** (A1, B1, C1) and the **right gripper** from the **right
  column** (A2, B2, C2). The gripper that pulls a case scans it.
* **Pallet-side rule:** the gripper on the pallet's side sets every case on the pallet. That is the **left gripper** in Config L
  and the **right gripper** in Config R. It is called the **pallet gripper**.
* **Hand-over rule:** when a case comes from the column away from the pallet, the pulling gripper scans it and then **hands it
  over** to the pallet gripper at the **hand-over point**. No arm reaches across the rack.

**The two arms never cross.** The **left gripper always stays left of the right gripper**, and neither arm reaches over, under,
around, or past the other. Nothing is moved two at a time: one gripper holds one case, and the other gripper is empty, taking a
hand-over, or clear of the rack.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own, it is pushed into place by hand, and it is never steered, nudged, or
repositioned once recording starts. It is parked once, before recording, and does not move again until the episode is over.

1. Push the base by hand up to the rack and stop it **square to its front**, so the beams run straight across the frame of the
   camera.
2. Stop it **centered on the rack**, so the middle of the base is in line with the middle upright between the two columns.
3. Stop it **close enough** that both grippers reach the back half of a case on every level straight in and level without either
   arm extending, and **far enough** that neither arm, wrist, nor any part of the base touches a beam, an upright, or the pallet
   stand while both arms work.
4. Check the **height band**: both grippers come level onto every case on levels A, B, and C without a wrist or forearm touching
   the beam or deck above it.
5. Check the **left side**: the **left gripper** reaches A1, B1, C1, the scanner window, and the hand-over point, all without
   extending.
6. Check the **right side**: the **right gripper** reaches A2, B2, C2, the scanner window, and the hand-over point, all without
   extending.
7. Check the **pallet** for the config this episode runs: the **pallet gripper** reaches all six pallet places, including place 6
   on top of the finished load, from above without extending.
8. Lock or brake the base. Push it firmly once by hand: it must not roll, creep, or turn.
9. If any of lines 1 to 7 fails, push the base to a new park by hand and start again at line 1. Do not work a rack the arms cannot
   reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it: no arm leans on the rack hard enough to shift it,
nothing touches it by hand, and it is never repositioned mid-task. A base that moves after recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centered on the middle upright and its frame includes the whole rack, all six positions and their
   labels, the scanner and its light, and the pallet stand with the full height of the finished load.
3. The camera reads every **position label** and the **SKU label** on every case, on the rack and on the pallet, so which case
   went to which place is readable.
4. The camera reads the **pick ticket** in its clip well enough to follow its lines.
5. The camera sees the **scanner light**, so each green or red scan is readable.
6. Both arms are at home with grippers open.
7. The **left arm** reaches A1, B1, C1, the scanner window, and the hand-over point without extending to a joint limit.
8. The **right arm** reaches A2, B2, C2, the scanner window, and the hand-over point without extending to a joint limit.
9. The pallet arm for this config reaches all six pallet places without extending to a joint limit.
10. Both grippers come in and go out of every rack position **from the front and level**, and neither wrist nor forearm touches the
    beam above on the way in or out.
11. The two arms do not collide, and neither arm passes in front of the other.
12. If a place cannot be reached, re-park the base by the Base positioning steps until lines 7 to 11 hold.

### Materials checklist

1. The **rack** stands where it lives, fixed to the wall or the floor. It is not moved, not leaned on, and not pushed at any point.
2. It has **three levels**, each with a beam or deck directly above it. **Level A** is the top, **level B** the middle, and **level
   C** the bottom. A **middle upright** splits it into a **left column** and a **right column**.
3. Each level holds **two rack positions**, one per column, numbered left to right: **A1, A2**, **B1, B2**, **C1, C2**. Each position
   has a **position label** on the beam right below it, with its name in large print.
4. Each position holds **one case**: a closed carton, all six the same size, about twice as long as it is wide, light enough for
   one gripper to hold by its sides. Each case has its **SKU label** on one end face.
5. Each case sits on its position with its long sides running front to back, **label end facing out**, its front end in line with
   the beam.
6. The **scanner** stands fixed in its **holster** on the middle upright, between level B and level C, window facing out. It stays in
   its holster for the whole episode. It reads a barcode by itself when the barcode is held about a hand in front of its window: a
   **green** light and one beep if the SKU is the one the current ticket line names, a **red** light and a buzz if it is not.
7. The **pallet** is a small mock pallet, as wide as three cases side by side and as deep as one case is long, on a fixed-height
   **pallet stand** with its top at about the height of level C.
8. The pallet stand stands braked against the **left end** of the rack in **Config L** and against the **right end** in **Config R**,
   the front edge of the pallet in line with the front of the rack.
9. The pallet starts empty. Nothing is taped or marked on it; the places are judged by eye against its edges.
10. The **pick ticket** is a card in the **ticket clip** on the front of the pallet stand, facing the camera. It has six lines, one per
    rack position. Each line reads position, SKU, quantity 1. The line order is shuffled per episode.
11. Every SKU on the ticket matches exactly one case on the rack, and every case is on the ticket once.
12. Nothing else stands on the rack, the stand, or the pallet within either arm's reach.

### Workspace layout

Nothing anywhere is marked or taped out except the position labels. You judge every other place by eye against the rack and the
pallet.

* **Rack:** the fixed rack the base is parked at. Never moved, never leaned on, never pushed.
* **Left column:** A1, B1, C1. **Left gripper only.**
* **Right column:** A2, B2, C2. **Right gripper only.**
* **Scanner:** fixed in its holster on the middle upright between levels B and C. Either gripper holds a case up to it, one at a
  time.
* **Hand-over point:** in front of the middle upright, a hand out from the beam of level B, above the scanner.
* **Pallet stand:** braked against the left end (Config L) or the right end (Config R) of the rack, with the pallet on top and the
  ticket clip on its front. **Pallet gripper only.**

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper.**
* The **left gripper** works the left column and the **right gripper** works the right column. The **pallet gripper** also works the
  pallet.
* The two arms meet only at the **hand-over point**, and both use the scanner, one at a time.
* Neither arm goes into a position in the other column, and neither reaches over, under, around, or past the other.
* Only one thing is moved at a time. A gripper holds one case, and while it does, the other gripper is empty, taking a hand-over, or
  drawn **clear of the rack**.

### Arm assignments

* **Pallet gripper** (**left gripper** in Config L, **right gripper** in Config R). Pulls and scans the cases of its own column,
  takes each hand-over, and sets every case on the pallet.
* **Other gripper.** Pulls and scans the cases of its own column and hands each one over to the pallet gripper. It never touches the
  pallet, the load, or the stand.
* Only cases are handed over. The scanner never leaves its holster and the ticket never leaves its clip.

## Vocabulary

* **Pick ticket:** the card in the ticket clip. It is read top to bottom.
* **Current line:** the top line whose case is not yet on the pallet. Only the case on the current line is ever touched.
* **Rack position:** one space on a rack level, named by the label under it (for example B2): level, then column.
* **SKU label:** the label on a case's end face that names it. It must match the SKU on the current line.
* **Pulling gripper:** the gripper whose column holds the current line's position. It pulls the case and scans it.
* **Pallet gripper:** the gripper on the pallet's side, the **left gripper** in Config L and the **right gripper** in Config R.
* **Front approach:** the gripper comes in and goes out level and from the front, and never comes down onto a case on the rack from
  above.
* **Pull:** close on the two long sides of the case near its front end, lift it just clear of the deck, and draw it straight out to
  the front, level, until its back end is clear of the beam.
* **Scan-confirm:** straight after the pull, the pulling gripper holds the case's **SKU label** about a hand in front of the scanner
  window, still, until the light shows. The scanner is never touched.
* **Green / red:** green light and one beep is a confirmed case. Red light and a buzz means the case is not the SKU the current line
  names.
* **Hand over:** the pulling gripper brings the scanned case to the hand-over point and holds it still for a **half-second hold**.
  The pallet gripper then closes on the long sides of it, nearer the far end. Only after the pallet gripper is closed does the
  pulling gripper open and draw back.
* **3-2-1 pattern:** the stable pattern for six cases. Every case lies flat with its long sides running front to back and its label
  end at the front. **Layer 1:** places 1, 2, 3, side by side across the pallet, left to right, touching, the outer two in line with
  the pallet's side edges. **Layer 2:** places 4 and 5, touching each other, place 4 over the joint between places 1 and 2, place 5
  over the joint between places 2 and 3. **Layer 3:** place 6, over the joint between places 4 and 5.
* **Across the joint:** a case in an upper layer sits half on each of the two cases below it, so no case stands straight on top of
  one other case.
* **Label out:** the case's SKU label end faces the front, toward the base and the camera, and is readable.
* **Front in line:** the front end of every case lines up with the front edge of the pallet, so the whole front of the load is one
  flat face.
* **Set case:** the case lies flat in its place, label out, front in line, touching its neighbours with no gap, and stays put when the
  gripper opens.
* **Clear of the rack:** the arm is drawn back so that no part of it is in front of a rack position, the scanner, or the pallet.

## Steps

Run Steps 1 to 3 in order, and end the episode with Step 4. Steps 1 to 3 are the three layers of the 3-2-1 pattern. Each ticket
line is read, pulled, scanned, and set before the next line is read, and each case goes to the next free place in number order.
Only the pallet gripper and the hand-overs depend on the config.

### Step 1: Build layer 1

**Goal:** the first three cases on the ticket are **set** in places 1, 2, and 3, and each one is scanned green.

Run 1.1 to 1.4 for ticket lines 1 to 3, top to bottom. Line 1 goes to place 1, line 2 to place 2, line 3 to place 3.

#### 1.1 Read the current line

* Read the **current line** on the pick ticket: its rack position and its SKU.
* Find the rack position whose **position label** matches it, and check that the SKU label on the case there matches the line.
  That position's column decides the **pulling gripper**.

**Check:** one position matches the line and its case carries the line's SKU. If no case matches, stop and log a system issue.

#### 1.2 Pull the case

* **IF the position is in the left column:** the **left gripper** is the pulling gripper. **IF it is in the right column:** the
  **right gripper** is the pulling gripper.
* With the **pulling gripper**, come level to the front of the case and close on its two long sides near its front end.
* With the **pulling gripper**, lift the case just clear of the deck and draw it straight out to the front, level, label end first,
  until its back end is clear of the beam.
* With the **pulling gripper**, do not come down onto the case from above, do not turn it, and do not drag it along the deck.
* With the other gripper, stay open and **clear of the rack** unless it is the pallet gripper waiting at the hand-over point.

**Check:** the case is held flat by its long sides, label end out, and the case on the other column of that level has not moved.

#### 1.3 Scan-confirm the case

* With the **pulling gripper**, carry the case level to the scanner and hold its **SKU label** about a hand in front of the scanner
  window, still, until the light shows.
* **IF green:** the case is confirmed. Go on to 1.4.
* **IF red:** with the **pulling gripper**, carry the case back, slide it level onto its rack position, label end out, front in line
  with the beam, then open and draw straight out. Read the line again and go back to 1.1.

**Check:** the scan was green, the case never touched the scanner, and the scanner still stands in its holster.

#### 1.4 Set the case in its layer 1 place

* **IF the pulling gripper is the pallet gripper:** with the **pallet gripper**, carry the case level to the pallet, label end to
  the front.
* **IF the pulling gripper is not the pallet gripper:** with the **pulling gripper**, carry the case to the **hand-over point** and
  hold it still for a **half-second hold**. With the **pallet gripper**, close on the long sides of the case nearer its far end. With
  the **pulling gripper**, open and draw back **clear of the rack**. With the **pallet gripper**, carry the case level to the pallet,
  label end to the front.
* Then, in both: with the **pallet gripper**, bring the case down to just above its place: place 1 at the left edge of the pallet,
  place 2 touching place 1, place 3 touching place 2 and in line with the right edge.
* With the **pallet gripper**, set it down flat, front in line with the pallet's front edge, then open and lift straight up.
* With the **pallet gripper**, do not let the case go from above the pallet and do not push it into the case beside it.

**Check:** the case is **set**. If it sits crooked, short of the front edge, or with a gap to its neighbour, close on its sides with
the **pallet gripper** and push it straight into line.

**Expected state:** layer 1 is three set cases side by side, fronts in line, labels out, each scanned green, with the pallet's side
edges covered.

### Step 2: Build layer 2

**Goal:** the fourth and fifth cases are **set** in places 4 and 5, each **across the joint** below it, and each scanned green.

Run 2.1 to 2.3 for ticket lines 4 and 5. Line 4 goes to place 4, line 5 to place 5.

#### 2.1 Read the current line and pull the case

* Read the **current line**, find its rack position, and check the SKU label on its case.
* With the **pulling gripper** for that column, pull the case: close on its long sides near the front end, lift it just clear of the
  deck, and draw it straight out, level, label end first.
* With the other gripper, stay open and **clear of the rack** unless it is the pallet gripper waiting at the hand-over point.

**Check:** one position matches the line, and the case is held flat by its long sides, label end out.

#### 2.2 Scan-confirm the case

* With the **pulling gripper**, hold the case's **SKU label** about a hand in front of the scanner window, still, until the light
  shows.
* **IF green:** go on to 2.3.
* **IF red:** with the **pulling gripper**, slide the case back onto its rack position, label end out, read the line again, and go
  back to 2.1.

**Check:** the scan was green and the scanner still stands in its holster.

#### 2.3 Set the case across the joint

* **IF the pulling gripper is the pallet gripper:** with the **pallet gripper**, carry the case level to the load, label end to the
  front.
* **IF the pulling gripper is not the pallet gripper:** with the **pulling gripper**, carry the case to the **hand-over point** and
  hold it still for a **half-second hold**. With the **pallet gripper**, close on the long sides nearer the far end. With the
  **pulling gripper**, open and draw back **clear of the rack**. With the **pallet gripper**, carry the case level to the load.
* Then, in both: with the **pallet gripper**, bring the case down to just above its place: place 4 over the joint between places 1
  and 2, place 5 over the joint between places 2 and 3, touching place 4.
* With the **pallet gripper**, set it down flat, front in line with the front of layer 1, then open and lift straight up.
* With the **pallet gripper**, do not press down on the load and do not shift a layer 1 case while setting.

**Check:** the case is **set** and sits half on each case below it. If it sits over one case only or hangs over the side, close on
its sides with the **pallet gripper** and push it into place.

**Expected state:** layers 1 and 2 are five set cases, fronts in line, labels out, each layer 2 case across a joint, all scanned
green.

### Step 3: Top the load

**Goal:** the sixth case is **set** in place 6, across the joint of layer 2, and scanned green, and the rack is empty.

* Read the **current line**, find its rack position, and check the SKU label on its case.
* With the **pulling gripper** for that column, pull the case straight out, level, label end first.
* With the **pulling gripper**, hold its **SKU label** about a hand in front of the scanner window until the light shows. **IF red:**
  with the **pulling gripper**, slide the case back onto its position, read the line again, and start this step again.
* **IF the pulling gripper is not the pallet gripper:** with the **pulling gripper**, hand the case over at the **hand-over point**
  with a **half-second hold**. With the **pallet gripper**, close on it before the **pulling gripper** opens.
* With the **pallet gripper**, carry the case above the load and bring it down to just above place 6, over the joint between places 4
  and 5.
* With the **pallet gripper**, set it down flat, front in line with the load, then open and lift straight up and away from the load.

**Check:** the case is **set** across the joint and the whole front of the load is one flat face with six labels out. If a case in
the load has shifted, close on its sides with the **pallet gripper** and push it back into line, one case at a time, top down.

**Expected state:** all six cases stand on the pallet in the 3-2-1 pattern, labels out, fronts in line, each scanned green. Every
rack position is empty and both grippers are clear of the rack.

### Step 4: End the episode

**Goal:** both arms are home, grippers open, and recording is stopped with the load built.

* Look once across the rack and the pallet: every rack position is empty, the scanner is in its holster, and the load stands in the
  3-2-1 pattern with six labels out.
* Return both arms **home** with grippers open. Homing is the last thing the arms do.
* Stop recording.

**Check:** both arms are at home, both grippers are fully open, and neither holds anything.

**Expected state:** the load is built and still, the base has not moved, and the recording has stopped.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the cases off the pallet, top down, and slide each one back onto its rack position, long sides front to back, label end out,
   front in line with the beam.
2. Check every case sits on the position its label names.
3. Put a different shuffled pick ticket in the ticket clip, facing the camera.
4. Move the pallet stand to the end of the rack for the next episode's config and brake it.
5. Check every label is readable and the scanner stands in its holster and still lights.
6. Pick up anything that landed on a beam, the stand, or the floor.
7. Check the base is still locked and parked square, then run the Base positioning steps and both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is what the reviewer
sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just because a rule was
broken.

### Violations

**Violation: Base moved during the episode**

* **Visible cue:** the rack shifts in frame, the beams change angle or size in frame, or the base rolls, creeps, or turns at any point
  after recording starts.
* **SOP rule broken:** Steps 1 to 4, the base is parked and locked before recording and stays still for the whole episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Approached from above or fouled the beam**

* **Visible cue:** a gripper comes down onto a case on the rack from above instead of coming in level from the front, or a wrist,
  forearm, or case knocks, scrapes, or rests on the beam above a position.
* **SOP rule broken:** Steps 1.2, 2.1, and 3, every reach into a rack position is a front approach, level, straight in and straight out.
* **Coaching note:** straight in from the front, straight out the same way.

**Violation: Leaned on or pushed the rack, stand, or load**

* **Visible cue:** a gripper, wrist, or forearm rests on a beam, an upright, the pallet stand, or the load; the stand rocks or moves; or
  the load is pressed down while a case is set.
* **SOP rule broken:** Steps 1 to 3, the rack, the stand, and the load carry no weight from the arms.
* **Coaching note:** the arm holds itself up. The load is set on, never pressed on.

**Violation: Pick ticket not followed**

* **Visible cue:** a line is skipped, lines are taken out of top-to-bottom order, or a case is touched that is not on the current line.
* **SOP rule broken:** Steps 1.1, 2.1, and 3, read the ticket top to bottom, one current line at a time.
* **Coaching note:** read the line, then move. The ticket is the order, not the rack.

**Violation: Wrong case pulled**

* **Visible cue:** a case is pulled from a position other than the one the current line names, including the case beside it or the
  one above or below it.
* **SOP rule broken:** Steps 1.1, 2.1, and 3, find the position whose label matches the line before the arm goes in.
* **Coaching note:** match the label under the case to the line. Cases that look alike are not the same case.

**Violation: Case held wrong**

* **Visible cue:** a case is held by its top, its label end, one corner, or its back half only; it tilts in the gripper; or the SKU
  label is covered when it reaches the scanner.
* **SOP rule broken:** Steps 1.2, 2.1, and 3, close on the two long sides near the front end and carry the case flat.
* **Coaching note:** long sides in the gripper, flat and level, label free.

**Violation: Case dragged or rack disturbed**

* **Visible cue:** a case is dragged along the deck, turned on the rack, or pulled out at a slant; or the case in the other column or
  on another level is moved, tipped, or pushed crooked.
* **SOP rule broken:** Steps 1.2, 2.1, and 3, lift the case just clear of the deck and draw it straight out, touching nothing else.
* **Coaching note:** lift, then draw. The rack stays as you found it.

**Violation: Scan skipped or done out of turn**

* **Visible cue:** a case goes onto the pallet without a scan; the scan happens after a hand-over or after the case is set; the next line
  is read before the green light; or a position label is scanned instead of the case's SKU label.
* **SOP rule broken:** Steps 1.3, 2.2, and 3, the pulling gripper scans the case's SKU label straight after the pull, and waits for green
  before the case goes on.
* **Coaching note:** pull, scan, green, then the pallet. The scan is the record that the right case was pulled.

**Violation: Red scan ignored**

* **Visible cue:** a red light and buzz is followed by a hand-over or a set on the pallet instead of the case going back to its rack
  position, or the same case is held up again and again until the operator moves on.
* **SOP rule broken:** Steps 1.3, 2.2, and 3, on red, slide the case back onto its position, read the line again, and pull again.
* **Coaching note:** red means the wrong case is in the gripper. Fix the pull, not the scan.

**Violation: Scanner handled or knocked**

* **Visible cue:** a gripper takes the scanner out of its holster, a case or gripper bumps the scanner window, or the scanner is turned or
  knocked in its holster.
* **SOP rule broken:** Steps 1.3, 2.2, and 3, hold the case a hand in front of the scanner window; the scanner stays in its holster and is
  never touched.
* **Coaching note:** bring the label to the scanner and stop a hand short.

**Violation: Hand-over done wrong**

* **Visible cue:** the pulling gripper opens before the pallet gripper has closed; the case is still moving when the pallet gripper
  closes, with no half-second hold; the hand-over happens away from the hand-over point; a case from the pallet's own column is handed
  over; or a case is handed over before its green scan.
* **SOP rule broken:** Steps 1.4, 2.3, and 3, hand over only cases from the column away from the pallet, after the green scan, at the
  hand-over point, held still, and open only after the pallet gripper has closed.
* **Coaching note:** scan, stop, hold still, let the pallet gripper take it, then open.

**Violation: Case dropped onto the pallet**

* **Visible cue:** a case is let go from above its place and falls onto the pallet or the load, lands on its side or end, or bounces
  out of line.
* **SOP rule broken:** Steps 1.4, 2.3, and 3, bring each case down to just above its place and set it flat before opening.
* **Coaching note:** down to the place, then open. A dropped case shifts the whole load.

**Violation: Wrong place in the pattern**

* **Visible cue:** a case goes to a place out of number order, a layer 2 case is set before layer 1 is full, place 6 is set before
  places 4 and 5, or a case is set on the pallet outside the 3-2-1 places.
* **SOP rule broken:** Steps 1 to 3, the cases fill places 1 to 6 in number order, one layer at a time.
* **Coaching note:** next free place, every time. The pattern is built bottom up.

**Violation: Joint not crossed**

* **Visible cue:** a layer 2 or layer 3 case stands straight on top of one case below instead of half on each of two, or hangs over the
  side of the layer below.
* **SOP rule broken:** Steps 2.3 and 3, every upper case sits across the joint of the two cases below it.
* **Coaching note:** half on each. A column of cases falls; a crossed load holds.

**Violation: Label not out**

* **Visible cue:** a case is set with its SKU label end facing back, facing a side, or turned so the label cannot be read from the front;
  or a case is turned in the gripper on the way to the pallet.
* **SOP rule broken:** Steps 1.4, 2.3, and 3, every case lies long sides front to back with its label end at the front.
* **Coaching note:** label end out from rack to pallet. Never turn the case.

**Violation: Case not in line**

* **Visible cue:** a case sits crooked, sticks out past the front face or sits short of it, leaves a gap to its neighbour, or hangs over a
  pallet edge.
* **SOP rule broken:** Steps 1.4, 2.3, and 3, set each case flat, front in line, touching its neighbours, inside the pallet edges.
* **Coaching note:** one flat front face, no gaps. A load out of line leans.

**Violation: Config misaligned**

* **Visible cue:** the arms work a config the rack is not set up in: the gripper away from the pallet sets a case on the pallet or
  touches the stand, a gripper carries a case toward a rack end with no pallet, or the stand is moved before or during the episode.
* **SOP rule broken:** Steps 1.4, 2.3, and 3, look at the rack, find the pallet, and follow the IF line that matches the config the
  episode is set up in.
* **Coaching note:** look at the pallet before the arm moves. One config per episode, and it never changes mid-episode.

**Violation: Wrong order of work**

* **Visible cue:** a case is pulled before its line is read; the next line is read before the case is set; or a case is fixed in the
  load after the next case has been pulled.
* **SOP rule broken:** Steps 1 to 3, each line is read, pulled, scanned, and set, and its check is done, before the next line is read.
* **Coaching note:** the order is the task. Each case leaves the load ready for the next one.

**Violation: More than one thing moved at a time**

* **Visible cue:** a gripper carries two cases; both grippers carry different cases at the same time outside a hand-over; or a gripper
  holds a case while the other works instead of being clear of the rack.
* **SOP rule broken:** Steps 1 to 3, one gripper holds one case, and the other is empty, taking a hand-over, or clear of the rack.
* **Coaching note:** one case, one trip.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped, or a check is made and the fault it finds is left uncorrected: a case crooked, out
  of line, off its joint, or with a gap.
* **SOP rule broken:** Steps 1.1 to 3, run each check and correct what it finds by the fix written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** a case is dropped on a beam, the stand, or the floor; a case on the rack is knocked off; or a case on the load is
  knocked out of place or the load topples.
* **SOP rule broken:** Steps 1 to 3, nothing is dropped or knocked out of its place, and every gripper comes out the way it went in.
* **Coaching note:** check the path and the landing place before the arm moves, and lift away from the load straight up.

**Violation: Wrong arm used**

* **Visible cue:** the **left gripper** pulls from the right column; the **right gripper** pulls from the left column; the gripper away
  from the pallet touches the pallet, the load, or the stand; or either arm passes in front of the other.
* **SOP rule broken:** Steps 1 to 3, each gripper pulls from its own column, only the pallet gripper works the pallet, and the arms never
  cross.
* **Coaching note:** left column, left arm. Right column, right arm. The pallet side decides who builds.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a case on the rack, a case out of the 3-2-1 pattern or out of line, a case not scanned green, a
  label not out, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 4, look once across the rack and the pallet, then return both arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read a position label, an SKU label, the pick ticket, or the scanner light**, so which case went where or whether a scan
  was green cannot be judged.
* **Scanner fault:** no light on a correctly held label, a green on a wrong SKU, or a red on the right one.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Ticket or case fault:** a line with no matching case, a case with no line, a case on the wrong position at the start, a crushed or
  open case, or a torn or unreadable label.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so a rack position, the scanner, the
  hand-over point, or a pallet place cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Read one pick-ticket line
2. Pull one case off the rack
3. Scan one case at the scanner
4. Slide one case back onto the rack after a red scan
5. Hand one case over at the hand-over point
6. Set one case in layer 1
7. Set one case across a joint in layer 2
8. Set the top case in place 6
9. Push one case back into line on the load
10. Return both arms home and end the episode
