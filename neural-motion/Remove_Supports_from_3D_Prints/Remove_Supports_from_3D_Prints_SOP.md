# Remove Supports from 3D Prints SOP (1x Episode: 3 Prints)

One episode clears all three prints. The table begins with three **prints** standing in a row on the **print
strip**, each one a **part** still sitting on its own **raft** with three **support trees** under its
**shelf**. The prints are worked **along the strip in order**, one at a time, and each one is finished and in
the tray before the next one is picked up.

The order never changes for a print: clip its three support trees flush under the shelf, peel the part off the
raft, drop the raft in the scrap bin, deburr the three nubs and the raft patch, then read the part's letter and
put it in the matching pocket of the finished tray. No tree is pulled or twisted off. No peel starts until all
three trees are clipped. No part goes in the tray until every contact point has been scraped.

The right gripper does all the tool work: it holds the flush cutters and makes every cut, peels each part off
its raft, and holds the deburr tool and makes every stroke. The left gripper does the supporting work: it
holds the raft down while the trees are clipped and the part is peeled, carries the empty raft to the scrap
bin, and holds the part down while it is deburred. The left gripper stays on the left side of the work spot
and never reaches across it. Which gripper brings each print in, and which places each finished part in the
tray, depends on the config below.

The table is set up in one of three ways. Only the print strip moves (and, in one of the three, the finished
tray swaps sides with it); the work spot, the deburr spot, the scrap bin, and both cradles are in the same
place in all three.

- **Config L:** the print strip is at the left, in front of the scrap bin, running front to back.
- **Config M:** the print strip is at the back-centre, behind the work spot, running left to right.
- **Config R:** the print strip is at the right, behind the cradles, running front to back; the finished tray
  stands at the left, in front of the scrap bin.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

- **Start position:** the prints start at the left (**Config L**), the back-centre (**Config M**) or the
  right (**Config R**). One config per episode, chosen before recording and never changed mid-episode.
- **Same-side rule:** the gripper on the print strip's side brings each print in — the left gripper in
  Config L and M, the right gripper in Config R. No arm reaches across the table.
- **Tray side:** the finished tray is at the right in Config L and M and the right gripper places every part;
  in Config R it is at the left and the left gripper places every part.
- **Fixed roles:** in every config the right gripper makes every cut, every peel, and every stroke, and the
  left gripper holds the raft and the part down and bins every raft. The order for a print never changes.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the print strip with all three prints in the start zone for
   this episode's config, the work spot, the deburr spot, the scrap bin at the back-left, the finished tray,
   and both tool cradles at the front-right.
3. The work spot and the deburr spot are seen from above, so the support trees, the cut ends, the nubs, and the
   raft patch can all be seen for the whole episode.
4. Both arms are at home with grippers open.
5. The **flush cutters** sit in the **cutter cradle** with their jaws closed and their flat face up. The
   **deburr tool** sits in the **tool cradle** beside them with its blade down.
6. The table is bare apart from the three prints on the strip, the scrap bin, the finished tray, the two tools
   in their cradles, and robot hardware.
7. The right arm reaches the work spot, the deburr spot, both cradles, (Config L and M) all three tray
   pockets, and (Config R) all three places on the print strip without stretching. The left arm reaches
   (Config L and M) all three places on the print strip, the left side of the work spot, the deburr spot, the
   scrap bin, and (Config R) all three tray pockets without stretching.

### Materials checklist

1. Three **prints** stand in a row on the **print strip** in the start zone for this episode's config, rafts
   flat on the table, parts up, each with its **shelf** pointing to the right, and the other two zones are
   bare:
   * **Config L:** the left side, in front of the scrap bin, the row running front to back
   * **Config M:** the back-centre, behind the work spot, the row running left to right
   * **Config R:** the right side, behind the cradles, the row running front to back
2. The prints sit on the strip in the order they came off the printer bed, which is not the tray order. Front
   to back (left to right in Config M) they are **B**, then **C**, then **A**.
3. Each print has exactly **three support trees** standing between its raft and the underside of its shelf: a
   **front tree**, a **middle tree**, and a **back tree**.
4. Each part carries its **letter** in raised type on the side face away from the shelf, so it can be read with
   the part either way up.
5. The **work spot** is bare, in the middle of the table. The **deburr spot** is bare, just in front of it.
6. The **scrap bin** at the back-left is empty.
7. The **finished tray** is empty — at the right in Config L and M, at the left in front of the scrap bin in
   Config R. Its three **pockets** are marked **A**, **B**, and **C**, left to right.
8. The **flush cutters** are in the **cutter cradle** at the front-right, jaws closed, flat face up. The
   **deburr tool** is in the **tool cradle** beside it, blade down.
9. All three prints are clean and sound: no tree already snapped, no raft cracked or curled off the table, no
   part cracked, and no letter too shallow to read.
10. Keep the middle of the table clear. Only the print being worked is on the work spot, and only the part
    being deburred is on the deburr spot.
11. Before collection, confirm by hand that each raft lies flat with no rock; that each part comes off its raft
    with a steady peel once its three trees are cut; that the cutters close on a tree with their flat face laid
    against the shelf; and that the deburr tool takes a nub down level in two strokes.

### Workspace layout

- **Print strip:** the three prints, **B**, **C**, **A** — the left side, front to back (**Config L**); the
  back-centre, left to right (**Config M**); or the right side, front to back (**Config R**)
- **Middle of the table:** the work spot, where each print is clipped and peeled
- **Just in front of the work spot:** the deburr spot, where each part is scraped
- **Back-left:** the scrap bin, for the empty rafts
- **Front-right zone:** the cutter cradle and the tool cradle
- **Finished tray:** pockets **A**, **B**, **C** left to right — the right side (**Config L and M**) or the
  left side, in front of the scrap bin (**Config R**)

### Arm assignments

- **Left gripper:** brings each print in from the print strip to the work spot in Config L and M; holds the
  raft down while the trees are clipped and while the part is peeled off; carries each empty raft to the
  scrap bin; holds each part down on the deburr spot while it is scraped; and in Config R puts each finished
  part in its tray pocket at the left.
- **Right gripper:** holds the flush cutters and makes all three cuts on each print, peels each part off its
  raft, holds the deburr tool and makes every scraping stroke, and in Config L and M puts each finished part
  in its tray pocket; in Config R it brings each print in from the print strip at the right.

## Vocabulary

- **Print:** one part, its raft, and its three support trees, all still joined, the way it came off the printer
  bed. There are three prints in an episode.
- **Part:** the printed piece on its own, once its raft is off. This is what goes in the tray.
- **Raft:** the flat printed base the part is built on. It is wider than the part and lies flat on the table.
- **Raft skin:** the thin joint between the raft and the part's bottom face. It is what lets go during the
  peel.
- **Support tree:** a thin printed pillar standing from the raft up to the underside of the shelf. Each print
  has three.
- **Tree base:** where a tree is rooted in the raft. Trees are never cut here, so each cut tree stays on the
  raft and leaves with it.
- **Front tree / middle tree / back tree:** the three trees under one shelf, named by where they stand from the
  front edge of the table backwards. They are always cut in that order.
- **Shelf:** the ledge that sticks out from one side of the part. The trees stand under it. It points to the
  right whenever the print is on the work spot.
- **Shelf underside:** the face of the shelf the trees are joined to. It faces down on the work spot and faces
  up once the part is tipped over on the deburr spot.
- **Flush cutters:** the hand cutters with one **flat face** and one bevelled face. They cut the trees and
  nothing else.
- **Flat face:** the side of the cutter jaws that is flat. It is laid against the part so the cut is left
  level.
- **Flush cut:** the cut made with the flat face laid against the shelf underside and the tree between the
  jaws, so what is left behind is a nub and not a stub.
- **Stub:** what is left when the cut is made away from the shelf. It stands up clearly off the face and casts
  its own shadow.
- **Nub:** the small bump left on the shelf underside where a tree was cut. There are three per part.
- **Raft patch:** the rough patch in the middle of the part's bottom face where the raft skin was. There is one
  per part.
- **Contact point:** any place the print touched itself — the three nubs and the raft patch. All four are
  scraped.
- **Clean nub:** no bump stands up above the face around it, the spot looks level with what is beside it, and
  no loose curl is left sitting on it.
- **Deburr tool:** the hand scraper with a flat blade. It scrapes the nubs and the raft patch and is used for
  nothing else.
- **Stroke:** one draw of the blade across a contact point, from the left side of the part to the right side,
  with the blade laid low against the face.
- **Curl:** the thin shaving the blade lifts off a nub or the raft patch. Curls fall on the table and are left
  where they fall.
- **Peel:** lifting the part's right edge first and rocking it up, so the raft skin lets go a little at a time
  along its length. The opposite of pulling the part straight up.
- **Tip over:** pushing a part over onto its top face with the side of the closed right gripper, while it sits
  on the table, so its bottom face and shelf underside come up.
- **Work spot:** the bare square in the middle of the table where one print at a time is clipped and peeled.
- **Deburr spot:** the bare square just in front of the work spot where one part at a time is scraped.
- **Print strip:** the row where the three prints wait at the start of the episode — the left side, front to
  back (**Config L**); the back-centre, left to right (**Config M**); or the right side, front to back
  (**Config R**). One per episode, chosen before recording and never changed mid-episode.
- **Scrap bin:** the open bin at the back-left that the empty rafts go into.
- **Finished tray:** the tray with three marked pockets, **A**, **B**, **C**, left to right.
- **Tray side:** where the finished tray stands — the right in Config L and M, the left in Config R. The
  gripper on the tray's side places every part.
- **Letter:** the raised **A**, **B**, or **C** on the part's side face. It says which pocket the part goes in.
- **Cradled:** the tool is back in its own cradle and the gripper has let go of it.
- **Clear of the part:** the gripper is open and moved off the part, so the whole part can be seen from above.

## Steps

Run Steps 1–6 in order on one print, then Step 7 sends you back for the next one. End the episode with Step 8.

Step 1's pick, Step 6's placing, and Step 7's choice of the next print depend on the config: in Config L and M
the **left gripper** brings each print in and the **right gripper** places each part in the tray at the right;
in Config R the **right gripper** brings each print in and the **left gripper** places each part in the tray
at the left. Every other line is the same in all three configs.

### Step 1: Bring the next print to the work spot

**Goal:** one print sits on the work spot, raft flat and shelf pointing right, held down by the left gripper.

Look where the print strip is before reaching for the first print.

- **IF the print strip is at the left (Config L):** work the strip **front to back** — the print nearest the
  front edge first, then the middle one, then the back one. With the **left gripper**, pinch the **left end
  of the raft**, lift the print straight up off the strip, and carry it low and level to the right, to the
  **work spot**.
- **IF the print strip is at the back-centre (Config M):** work the strip **left to right** — the print
  nearest the left end first, then the middle one, then the right one. With the **left gripper**, pinch the
  **left end of the raft**, lift the print straight up off the strip, and carry it low and level forward, to
  the **work spot**.
- **IF the print strip is at the right (Config R):** work the strip **front to back** — the print nearest the
  front edge first, then the middle one, then the back one. With the **right gripper**, pinch the **right
  end of the raft**, clear of the trees, lift the print straight up off the strip, and carry it low and level
  to the left, to the **work spot**.

Then, in all three:

- Set the raft flat on the table and turn the print with the gripper that carried it until its **shelf**
  points to the **right**. In Config R, open the **right gripper** and move it clear, then pinch the **left
  end of the raft** with the **left gripper**.
- Keep the **left gripper** pressing the **left end of the raft** through Steps 2 and 3.
- Hold the print by the raft only. Never lift or carry a print by its part, its shelf, or a tree.

**Check:** the raft lies flat with no rock, the shelf points right, all three trees can be seen standing
under the shelf, and the **left gripper** is on the left end of the raft. If the raft rocks or the shelf
points the wrong way, set the print down again with the **left gripper** and straighten it before anything is
cut.

**Expected state:** one print is on the work spot, the deburr spot is bare, both tools are cradled, and the
strip holds the prints not yet worked.

### Step 2: Clip the three support trees

**Goal:** all three trees are cut flush under the shelf, front tree first, and each cut tree is still rooted in
the raft.

#### 2.1 Take the flush cutters

- With the **right gripper**, take the **flush cutters** from the **cutter cradle** by the handles and lift
  them straight up.
- Hold them with the jaws pointing **left** and the **flat face up**.
- Keep the cutters in the **right gripper** until 2.3. Do not pick anything else up while holding them.

**Check:** the jaws point left, the flat face is up, and the jaws are open. If the cutters sit turned over in
the gripper, put them back in the cradle with the **right gripper** and take them again.

#### 2.2 Cut the trees, front to back

- With the **left gripper**, keep pressing the **left end of the raft** down.
- With the **right gripper**, bring the cutters in **from the right, level**, under the shelf.
- Lay the **flat face** against the **shelf underside** beside the **front tree**, so the tree sits between the
  jaws right where it meets the shelf.
- Close the jaws in one squeeze until the tree parts.
- Open the jaws and draw the cutters straight back out to the right.
- Do the **middle tree** the same way, then the **back tree**.
- Cut each tree **once**, at the shelf. Never cut a tree at its base, and never cut it part way and then bend
  it off.
- Never pull, twist, or lever a tree off with the cutters or with either gripper.
- Bring the cutters in level from the right every time. Do not come down on a tree from above.

**Check:** after each cut the tree is parted, the piece that came off is still rooted in the raft, and what is
left on the shelf is a **nub** and not a **stub**. If a stub is left, lay the flat face against the shelf again
with the **right gripper** and take the stub down with one more cut. If a tree bends instead of parting, open
the jaws, re-seat the flat face against the shelf, and squeeze again.

#### 2.3 Cradle the cutters

- With the **right gripper**, put the **flush cutters** back in the **cutter cradle**, jaws closed and flat
  face up, and let go.

**Expected state:** all three trees are cut at the shelf, all three cut pieces are still standing in the raft,
the part is held to the raft only by the raft skin, and the cutters are cradled.

### Step 3: Peel the part off the raft

**Goal:** the part is off its raft with a steady peel and sits tipped over on the deburr spot, contact points
up.

- With the **left gripper**, keep pressing the **left end of the raft** down against the table.
- With the **right gripper**, take the part by its **right side**, below the shelf.
- Lift the part's **right edge** first and rock it upward, so the **raft skin** lets go a little at a time
  across the bottom face.
- Keep rocking until the skin has let go along its whole length, then lift the part clear of the raft.
- Peel from the right edge only. Never pull the part straight up off the raft, and never rock it side to side
  to snap it free.
- With the **right gripper**, set the part down on the **deburr spot**, the same way up as it was on the raft.
- With the closed **right gripper**, **tip it over** onto its top face, so its **bottom face** and its **shelf
  underside** both face up.
- Open the **right gripper** and move it **clear of the part**.

**Check:** the part is off the raft with no piece of the part left behind on the raft skin, the part lies still
on its top face, and the three nubs and the raft patch can all be seen from above. If the part is still joined
anywhere, set it back down, hold the raft with the **left gripper**, and carry on peeling from the right edge.
If a tree is found still joined to the shelf, put the part back on the raft, take the cutters with the **right
gripper**, and cut that tree as in 2.2 before peeling again.

**Expected state:** the part sits tipped over on the deburr spot with its contact points up, and the empty raft
is still on the work spot under the left gripper.

### Step 4: Put the raft in the scrap bin

**Goal:** the work spot is bare and the raft, with its three cut trees, is in the scrap bin.

- With the **left gripper**, pinch the **left end of the raft** and lift it straight up off the work spot.
- Carry it low to the **scrap bin** at the back-left and let go over the bin so it drops in.
- Carry the raft in one go. Do not set it down anywhere on the way, and do not carry it over the part on the
  deburr spot.

**Check:** the raft is inside the bin and not on its rim, the work spot is bare, and no cut tree has come off
the raft onto the table. If a tree has come off, pick it up with the **left gripper** and drop it in the bin
before going on.

**Expected state:** the work spot is bare, the scrap bin holds the raft, and the part waits tipped over on the
deburr spot.

### Step 5: Deburr the contact points

**Goal:** all three nubs and the raft patch are scraped clean, with the part held down and every stroke drawn
away from the left gripper.

#### 5.1 Hold the part and take the tool

- With the **left gripper**, press down on the **left side of the part** and hold it against the table.
- Keep the **left gripper** there for the whole of Step 5.
- With the **right gripper**, take the **deburr tool** from the **tool cradle** by its handle and hold it
  blade down.

**Check:** the part does not slide when the left gripper presses, and the blade points down. If the part slides
under the blade, press it down harder with the **left gripper** before any stroke.

#### 5.2 Scrape the three nubs

- With the **right gripper**, lay the blade low against the **shelf underside**, just left of the **front
  nub**.
- Draw the blade across the nub in one **stroke**, from the left side of the part to the right side, away from
  the **left gripper**.
- Give the front nub **two strokes**. Then do the **middle nub**, then the **back nub**, two strokes each.
- Every stroke runs left to right, away from the left gripper. Never draw the blade back toward the left
  gripper, and never stroke toward the gripper that is holding.
- Keep the blade low against the face. Do not stand it up on its corner and do not lever with it.

**Check:** each nub is a **clean nub** — no bump standing up above the face, the spot level with what is beside
it, and no curl left sitting on it. If a nub still stands up, give it **two more strokes**. If it still stands
up after that, stop, go to Step 8 with the part as it is, and log the tool for a station check.

#### 5.3 Scrape the raft patch

- With the **right gripper**, lay the blade low on the **bottom face**, at the front of the **raft patch**.
- Draw **three strokes** across the patch, left to right, working from the front of the patch to the back, each
  stroke overlapping the one before so no rough strip is left between them.
- Leave the **curls** where they fall on the table. They are cleared at reset, not during the episode.

**Check:** the raft patch is level with the bottom face around it, with no rough strip left between strokes and
no curl still standing on it. If a rough strip is left, draw one more stroke over it, left to right.

#### 5.4 Cradle the deburr tool

- With the **right gripper**, put the **deburr tool** back in the **tool cradle**, blade down, and let go.
- Open the **left gripper** and move it **clear of the part**.

**Expected state:** the part sits on the deburr spot with three clean nubs and a level raft patch, both tools
are cradled, and both grippers are off the part.

### Step 6: Put the part in its tray pocket

**Goal:** the part is resting in the pocket that matches its letter, bottom face up.

- Read the **letter** on the part's side face.
- **IF Config L or M:** with the **right gripper**, take the part by its **right side**, lift it straight up
  off the deburr spot, and carry it low and level to the **finished tray** at the right. **IF Config R:** with
  the **left gripper**, take the part by its **left side**, lift it straight up off the deburr spot, and carry
  it low and level to the **finished tray** at the left.
- Lower it into the pocket marked with that **letter** — **A**, **B**, or **C**.
- Put it in **bottom face up**, the way it came off the deburr spot. Do not turn it over on the way.
- Lower the part until it rests in the pocket, then open the gripper and move it clear.
- Let go only once the part is resting. Never drop or toss a part into a pocket.
- Carry the part over the table, not over the scrap bin.

**Check:** the letter on the part matches the mark on the pocket, the part sits flat in the pocket bottom face
up, and it is inside the pocket and not resting on a divider. If the part is in the wrong pocket, take it out
with the gripper that placed it and put it in the right one. If it sits on a divider, lift it and lower it again.

**Expected state:** one more part is in the tray, the deburr spot is bare, the work spot is bare, both tools
are cradled, and one fewer print is on the strip.

### Step 7: Repeat for the remaining prints

**Goal:** all three prints are worked, one at a time, along the strip in order.

- If a print is still on the **print strip**, go back to **Step 1**. **IF Config L or R:** take the one
  nearest the front edge. **IF Config M:** take the one nearest the left end.
- If the **print strip** is empty, go on to **Step 8**.
- Finish one print completely, all the way into its tray pocket, before the next print is picked up. Never have
  two prints on the work spot, and never bring the next print in while a part is still on the deburr spot.

**Expected state:** after the third print, the strip is empty, all three parts are in the tray, and all three
rafts are in the scrap bin.

### Step 8: End the episode

**Goal:** recording ends with all three parts desupported, deburred, and sorted into their pockets.

1. Confirm all three parts are in the finished tray, each in the pocket that matches its letter, bottom face
   up; each part has three clean nubs and a level raft patch; all three rafts, with their cut trees, are in the
   scrap bin; the print strip, the work spot, and the deburr spot are bare; and the flush cutters and the
   deburr tool are both cradled.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

### After each episode

1. With recording off, lift the three parts out of the tray and put them in the finished-parts crate off the
   table. A desupported part is never re-run.
2. Empty the scrap bin of rafts and cut trees.
3. Brush the curls and any loose crumbs off the table, out of the work spot, the deburr spot, the tray pockets,
   and both cradles.
4. Stage three fresh prints on the print strip for the next episode's config — the left side (Config L), the
   back-centre (Config M), or the right side (Config R) — rafts flat, parts up, shelves pointing right, in the
   order **B**, then **C**, then **A**, front to back (left to right in Config M). Stand the finished tray at
   the right for Config L or M, or at the left in front of the scrap bin for Config R.
5. Check each fresh print: three trees under the shelf, none already snapped, raft flat with no rock, part not
   cracked, letter deep enough to read. Replace any print that fails.
6. Wipe the cutter jaws and the tool blade clean of stuck plastic, and put both tools back in their cradles —
   cutters jaws closed and flat face up, deburr tool blade down.
7. Run both Setup checklists before the next episode.

### At the end of the session

1. Replace the **flush cutters** when a cut leaves a stub with the flat face properly laid against the shelf,
   or when the jaws no longer close on a tree in one squeeze.
2. Replace the **deburr tool** when a nub needs more than two extra strokes to come level, or when the blade
   tears the face instead of lifting a curl.
3. Replace the **finished tray** if a pocket mark can no longer be read, and the **print strip** marks if they
   have worn off.
4. Empty the scrap bin and the finished-parts crate, and leave the table bare.

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

**Note on the start position:** the violations below were written for Config L (print strip at the left,
finished tray at the right). The pickup and arm-role cues will be rewritten later to cover all three start
positions; they are left as they are for now. Until then, anything that does not match the episode's config
goes under **Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the prints are not in the
  start zone for the config, or the finished tray is not on its side for the config; a gripper reaches across
  the table for a print or for the tray; or the wrong IF line is followed.
- **SOP rule broken:** the start position, the same-side rule, and the tray side (the gripper on the strip's
  side brings each print in and the gripper on the tray's side places each part; no arm reaches across the
  table; the IF line followed is the one for the config on the table).
- **Coaching note:** look where the print strip and the tray are before the first reach, then follow that
  config's IF lines through Steps 1, 6 and 7.

**Violation: Prints worked out of order**
- **Visible cue:** the left gripper takes a print from the middle or the back of the strip while a print is
  still standing nearer the front edge.
- **SOP rule broken:** Steps 1 and 7 (work the strip front to back, taking the print nearest the front edge
  each time).
- **Coaching note:** always take the one nearest you. Do not pick by which print looks easiest.

**Violation: Print lifted or carried by the part**
- **Visible cue:** the left gripper pinches the part, the shelf, or a tree to lift or turn a print, instead of
  pinching the left end of the raft.
- **SOP rule broken:** Step 1 (hold the print by the raft only, and never lift or carry it by its part, its
  shelf, or a tree).
- **Coaching note:** the raft is the handle until it comes off. Nothing else is.

**Violation: Print set down rocking or shelf-wrong**
- **Visible cue:** cutting starts with the raft rocking on the work spot, or with the shelf pointing to the
  front, the back, or the left instead of to the right.
- **SOP rule broken:** Step 1 (the raft lies flat with no rock and the shelf points right before anything is
  cut).
- **Coaching note:** flat and shelf right, then look at the three trees. Straighten it before the cutters come
  out.

**Violation: Raft not held while the trees are cut or the part is peeled**
- **Visible cue:** the left gripper is off the raft while the right gripper cuts or peels, and the raft slides,
  turns, or lifts off the table.
- **SOP rule broken:** Steps 2.2 and 3 (the left gripper presses the left end of the raft down through the
  cutting and the peel).
- **Coaching note:** left gripper on the raft before the cutters go in, and keep it there until the part is
  off.

**Violation: Trees cut out of order, or a tree left uncut**
- **Visible cue:** the middle or the back tree is cut before the front tree, or the peel starts with a tree
  still joined to the shelf.
- **SOP rule broken:** Steps 2.2 and 3 (cut the front tree, then the middle tree, then the back tree, and start
  the peel only once all three are cut).
- **Coaching note:** front, middle, back. Count three cuts before you touch the part.

**Violation: Cut not flush**
- **Visible cue:** the cutters close away from the shelf and leave a stub standing up off the face, or the
  cutters are laid bevel-side against the shelf, or the jaws are pressed into the shelf so the blade bites the
  part itself.
- **SOP rule broken:** Step 2.2 (lay the flat face against the shelf underside with the tree between the jaws
  where it meets the shelf, and cut once).
- **Coaching note:** flat face on the shelf first, then squeeze. Look at what is left before moving to the next
  tree.

**Violation: Tree pulled, twisted, or bent off**
- **Visible cue:** a tree is snapped off by pulling or twisting it with a gripper or with the cutter jaws, or
  it is cut part way and then bent until it breaks.
- **SOP rule broken:** Step 2.2 (cut each tree once at the shelf, and never pull, twist, or lever it off).
- **Coaching note:** the cutters part it. If it bends instead, re-seat the flat face and squeeze again.

**Violation: Tree cut at its base instead of at the shelf**
- **Visible cue:** the cutters close down at the raft, so the tree comes away loose in the jaws or falls on the
  table, and a full-height tree is left hanging from the shelf.
- **SOP rule broken:** Step 2.2 (cut each tree at the shelf, so the cut piece stays rooted in the raft).
- **Coaching note:** cut at the top, never at the bottom. The raft carries the scrap away.

**Violation: Cutters brought down from above**
- **Visible cue:** the right gripper comes down on a tree from over the top of the shelf, or reaches over the
  part to cut, instead of coming in level from the right.
- **SOP rule broken:** Step 2.2 (bring the cutters in level from the right for every cut).
- **Coaching note:** in from the right, level, every time. Never over the top.

**Violation: Tool not cradled before the next move**
- **Visible cue:** the right gripper still holds the flush cutters or the deburr tool while it peels a part,
  picks a part up, or places a part in the tray; or a tool is put down on the table instead of in its cradle.
- **SOP rule broken:** Steps 2.3, 5.4 and 6 (put each tool back in its own cradle and let go before the right
  gripper takes anything else).
- **Coaching note:** one thing in the hand. Cradle the tool, then pick up the part.

**Violation: Part pulled straight up off the raft**
- **Visible cue:** the right gripper lifts the part vertically off the raft, or rocks it side to side to snap
  it free, instead of lifting the right edge first and rocking it up.
- **SOP rule broken:** Step 3 (peel from the right edge, rocking upward so the raft skin lets go a little at a
  time).
- **Coaching note:** right edge up first, then roll it off. Never yank it.

**Violation: Part not tipped over, or tipped in the air**
- **Visible cue:** the part is left on its bottom face on the deburr spot with the nubs and the raft patch
  facing down, or the right gripper turns it over in mid-air instead of setting it down and pushing it over on
  the table.
- **SOP rule broken:** Step 3 (set the part down on the deburr spot, then tip it over on the table with the
  closed right gripper so the bottom face and the shelf underside face up).
- **Coaching note:** set it down, then push it over. Never turn it over in the air.

**Violation: Raft left on the work spot or dropped short of the bin**
- **Visible cue:** the deburring starts with the empty raft still on the work spot, or the raft is set down on
  the table, left on the bin rim, or dropped beside the bin.
- **SOP rule broken:** Step 4 (lift the raft off the work spot and carry it in one go until it drops inside the
  scrap bin).
- **Coaching note:** raft straight to the bin, and look that it went in.

**Violation: Scrap left loose on the table**
- **Visible cue:** a cut tree comes off the raft onto the table or the work spot and the episode carries on
  without it being picked up and dropped in the bin.
- **SOP rule broken:** Step 4 (pick up any cut tree that comes off the raft with the left gripper and drop it
  in the bin before going on).
- **Coaching note:** trees ride out on the raft. If one comes loose, bin it before the next step.

**Violation: Part not held while it is deburred**
- **Visible cue:** the left gripper is off the part while the right gripper strokes, and the part slides,
  turns, or skates on the deburr spot.
- **SOP rule broken:** Step 5.1 (the left gripper presses the left side of the part down for the whole of
  Step 5).
- **Coaching note:** left gripper down first, then the blade. Hold it the whole way through.

**Violation: Stroke drawn toward the holding gripper**
- **Visible cue:** the blade is drawn right to left, back toward the left gripper, or scrubbed back and forth
  across a contact point instead of drawn left to right in single strokes.
- **SOP rule broken:** Steps 5.2 and 5.3 (every stroke runs left to right, away from the left gripper).
- **Coaching note:** one way only, away from the hand that holds. Lift and reset between strokes.

**Violation: Blade stood up or used as a lever**
- **Visible cue:** the blade is stood on its corner, dug into the face, or levered under a nub to flick it off,
  instead of being laid low and drawn across.
- **SOP rule broken:** Step 5.2 (keep the blade low against the face, and do not stand it up on its corner or
  lever with it).
- **Coaching note:** low and flat. The blade shaves; it does not pry.

**Violation: Contact point skipped or short-stroked**
- **Visible cue:** a nub gets fewer than two strokes or none at all, the nubs are done out of order, or the
  raft patch gets fewer than three overlapping strokes and a rough strip is left across it.
- **SOP rule broken:** Steps 5.2 and 5.3 (two strokes on each nub, front then middle then back, and three
  overlapping strokes across the raft patch).
- **Coaching note:** three nubs and the patch, every part. Count the strokes.

**Violation: Part put in the wrong pocket**
- **Visible cue:** the part goes into a pocket whose mark does not match the letter on its side face, or the
  right gripper carries it straight to a pocket with no look at the letter.
- **SOP rule broken:** Step 6 (read the letter, then lower the part into the pocket marked with that letter).
- **Coaching note:** read the letter every time. Do not go by which print you think you picked up.

**Violation: Part dropped into the pocket or put in the wrong way up**
- **Visible cue:** the right gripper opens above the tray and the part falls into the pocket, the part is
  tossed in, it is turned over on the way so it lands top face up, or it is left resting on a divider.
- **SOP rule broken:** Step 6 (lower the part bottom face up until it rests in the pocket, then let go).
- **Coaching note:** lower it in, feel it rest, then open. Do not turn it over on the way.

**Violation: Two prints in play at once**
- **Visible cue:** a second print is brought to the work spot while a part is still on the deburr spot, or two
  prints sit on the work spot together, or the left gripper goes to the strip before the finished part is in
  its pocket.
- **SOP rule broken:** Step 7 (finish one print completely into its pocket before the next print is picked up).
- **Coaching note:** one print at a time, all the way to the tray, then the next.

**Violation: Part or raft dropped or knocked off the table**
- **Visible cue:** a print, a part, a raft, a cut tree, or a tool falls off the table, is knocked off the work
  spot or the deburr spot, or is knocked out of the tray or a cradle, at any point in the episode.
- **SOP rule broken:** Steps 1 through 6 (each piece is taken, carried low and level, set down where the step
  says, and released only once it is resting).
- **Coaching note:** low and slow, and let go only once it is down.

**Violation: Check made but not confirmed**
- **Visible cue:** the gripper moves straight on from a cut, a peel, a stroke, or a placement with no pause to
  look — no look at what is left on the shelf, at the nubs, at the raft patch, or at the pocket mark — and a
  fault a look would have caught is left in.
- **SOP rule broken:** Steps 1, 2.1, 2.2, 3, 4, 5.1, 5.2, 5.3 and 6 (each check is looked at, and its retry is
  run when the check fails).
- **Coaching note:** stop and look at each check. A check you do not look at is a check you did not do.

**Violation: Wrong arm used**
- **Visible cue:** the left gripper takes the cutters, the deburr tool, or a finished part; the right gripper
  holds a raft or a part down while the other works, or carries a raft to the scrap bin; or either gripper
  reaches across to the far side of the work spot.
- **SOP rule broken:** Steps 1 through 6 (the right gripper cuts, peels, deburrs, and places; the left gripper
  fetches prints, holds the raft and the part, and bins the raft).
- **Coaching note:** right gripper works, left gripper holds and fetches. Neither reaches across.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before the end state is confirmed, the arms are sent home before the
  confirm, or a gripper touches a part, a raft, or a tool after the arms have gone home.
- **SOP rule broken:** Step 8 (confirm the end state, return both arms home, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than tagging
them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- A print arrives with a tree already snapped, so there is nothing to cut.
- A raft is cracked or curled up off the table, so it cannot be held flat.
- The raft skin is fused so hard that a correct peel will not part it, or the part cracks during a correct
  peel.
- A part arrives cracked from the printer, or its letter is too shallow to read.
- The flush cutters are dull or their jaws are sprung, so a correctly laid flat face still leaves a stub.
- The deburr tool's blade is dull or chipped, so a nub will not come level in two extra strokes.
- A tray pocket is broken or its mark has worn away, so no part can be sorted into it.

## Annotation subtasks (from SOP)

1. Take the next print from the print strip and set it on the work spot, shelf right
2. Pick up the flush cutters
3. Cut the front, middle, and back support trees flush under the shelf
4. Cradle the flush cutters
5. Peel the part off the raft from its right edge
6. Set the part on the deburr spot and tip it over
7. Carry the empty raft to the scrap bin
8. Pick up the deburr tool
9. Scrape the three nubs, two strokes each
10. Scrape the raft patch, three overlapping strokes
11. Cradle the deburr tool
12. Read the part's letter and place it in the matching tray pocket
13. Confirm the end state, return both arms home, and end the episode
