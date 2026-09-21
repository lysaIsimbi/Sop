# Prepare and Plate a Sandwich SOP

One episode makes one sandwich and puts it on a plate. Two slices of bread and one slice of ham
start out lying on the cutting board. The bottom slice is carried to the middle of the board and
spread. The ham goes on it, then the top slice. The sandwich is cut once on the diagonal. The
two halves are lifted onto the plate one at a time on a cooking turner. The board is wiped clean into
the tool tray. Every tool is back in its place when the episode ends.

The order never changes. Bottom slice to the middle, spread, ham, top slice, cut, plate, wipe.

Three tools are used, and only the right gripper touches them. The knife spreads and cuts. The
cooking turner carries the halves. The cloth wipes the scraps off the board. The knife and the
turner live on the tool tray in front of the board. The cloth has its own spot on the right. Every
tool goes back to its place between uses. Never change your grip on anything while it is in the air.

The food starts in one of three places on the board. Only the bread and the ham move. The tool
tray, the cloth spot, the spread tub, the plate, and the build spot in the middle of the board are
the same in all three. "Back" means the far side of the board, away from the robot.

* **Config L1:** the ham is at the left-center side of the board. The bottom slice is at the back of
  the board, in the middle. The top slice is at the far right.
* **Config L2:** the ham is in the back-left corner of the board. The bottom slice is at the back of
  the board, in the middle. The top slice is at the far right.
* **Config M:** the ham is at the back-center of the board. The bottom slice is in the back-left
  corner. The top slice is in the back-right corner, at the far right.

In every config the top slice is the slice at the far right of the board. The slices and the ham lie
straight with the board. Nothing touches another item, and nothing hangs over an edge. The build
spot is the middle of the board, and it is clear at the start in every config.

The steps are the same in every config, and each arm keeps the same role. Only the place the food
starts from changes, so only the direction of the first carry of the bottom slice and of the ham
changes. Steps 1 and 3 say where to look.

What is the same in every session:

* **Start position:** the ham starts at the middle of the left side (**Config L1**), in the
  back-left corner (**Config L2**), or at the back in the middle (**Config M**). The bottom slice
  starts at the back in the middle (**Config L1** and **Config L2**) or in the back-left corner
  (**Config M**). The top slice starts at the far right in all three. One config per episode, picked
  before recording and never changed during the episode. The knife and the turner lie on the tool
  tray in front of the board, and the cloth lies in its spot on the right, in every config.
* **Who does what:** the **left gripper** handles the food, holds it still, and does the last fix on
  the plate. The **right gripper** handles every tool and does everything that needs one: loading and
  spreading, cutting, carrying the halves on the turner, and wiping. The roles do not swap with the
  config. The right gripper grips food only to hand it over. The left gripper never grips a tool.
* **The slice at the right end of the board is the top slice. The other slice is the bottom
  slice.** This is set before the episode and never swapped.
* **A bread slice is lifted only by the left gripper, and only after the right gripper anchors it.**
  Before the left gripper grips, the right gripper rests on the far side of the slice as an anchor
  so the slice cannot slide. The right gripper lifts off before the slice leaves the board.
* **Hand-over rule:** the left gripper puts every food item down, in every config. The top slice
  starts at the right end of the board, which can be too far for the left gripper. The arms cannot swap
  roles, because the right gripper is the knife gripper. So the right gripper pinches that item by its
  right side, slides it flat along the board toward the left gripper, and hands it over on the board.
  It holds still, the left gripper grips the left side, then the right gripper lets go. The right
  gripper never lifts food.
* **A half moves only on the turner.** No gripper ever picks up a sandwich half.

## Setup

Go through both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole tabletop: the cutting board in the middle with the two
   slices and the ham on it in this episode's config, the tool tray in front of the board, the spread
   tub and the cloth spot on the right, and the plate on the left.
3. Both arms are at home with grippers open.
4. Nothing is on the tabletop except the things listed below.
5. Nothing is in the way between the tray, the spread tub, the cloth spot, the board, and the plate.

### Materials checklist

1. The cutting board lies flat in the middle of the tabletop. Its front edge touches the back lip of
   the tool tray. It carries three things, all lying flat and none on top of another: the **bottom
   slice**, the **ham**, and the **top slice**. The config says where they are:
   * **Config L1:** the ham is at the left-center side of the board. The bottom slice is at the back
     of the board, in the middle. The top slice is at the far right.
   * **Config L2:** the ham is in the back-left corner of the board. The bottom slice is at the back
     of the board, in the middle. The top slice is at the far right.
   * **Config M:** the ham is at the back-center of the board. The bottom slice is in the back-left
     corner. The top slice is in the back-right corner, at the far right.
   The slices and the ham lie straight with the board. Nothing touches another item, and nothing
   hangs over an edge. The build spot is the middle of the board. It is where the sandwich is built.
   It is clear at the start in every config.
2. The two bread slices are the same size and are not torn. The **slice at the right end of the
   board is the top slice** and the **other slice is the bottom slice**, every episode.
3. The tool tray lies along the front edge of the tabletop, right in front of the board, where the
   right arm can reach it. It holds two tools, the **knife** and the **cooking turner**. Each lies
   flat across the tray from side to side, in the front half of the tray, with its handle to the
   right so a gripper can take it from above. The back half of the tray, the strip against the
   board's front edge, is empty. That is where the scraps go. There is no holder or slot for either
   tool. Each is just set down in its place. Both blades are clean and dry.
4. The cloth lies folded flat and dry in its **cloth spot**, a clear patch of tabletop just right of
   the board toward the front, where the right arm can reach it. It is not on the tray.
5. The spread tub sits open on the tabletop right of the board, where the right arm can reach it. It
   is not at the back of the tabletop. The lid is off and set aside. The tub holds enough spread to
   cover a whole slice with some left over, so nothing has to be scraped out. It is heavy enough, or
   sits firmly enough, that the knife comes out without lifting the tub.
6. The plate sits against the left edge of the tabletop, left of the board, empty and the right way
   up.

### Where things are

* **Cutting board:** flat in the middle of the tabletop, where both arms can reach. Every food item
  starts here, where the config says. The whole sandwich is built on the build spot in the middle. At the end the board is empty.
* **Tool tray:** along the front edge, right in front of the board, its back lip against the board's
  front edge. The right arm can reach it. The knife and the turner lie across its front half, each in
  its own place. Its back half, against the board, is empty at the start and holds the scraps at the
  end. The knife and the turner lie flat here whenever they are not in the right gripper.
* **Cloth spot:** the clear patch of tabletop just right of the board toward the front. The right
  arm can reach it. The cloth lies flat here whenever it is not in the right gripper.
* **Spread tub:** open, on the tabletop right of the board. The right arm can reach it.
* **Plate:** against the left edge, left of the board. Both arms can reach it. The right gripper goes
  to it only with the turner. The left gripper goes to it only for the last fix.

**Who owns what, said once.** The left arm owns the food. It does every lift and carry of a slice or
the ham, it holds the bread still whenever a tool is working on it, and it does the last fix on the
plate. The right arm owns the tools and the spread tub, and it carries the halves to the plate on the
turner. Both arms work over the board, but each does only its own work there. Neither arm does the
other arm's work.

## Vocabulary

### Which arm does what

* **The left gripper owns the food.** It carries the bottom slice to the middle of the board, lays
  the ham on it, closes the sandwich with the top slice, holds the bread still for the spread, the
  cut, and both turner pickups, and pushes the halves into place on the plate at the end of Step 6.
  It never touches a tool or the spread tub.
* **The right gripper owns the tools and the tub.** It takes the knife off the tray to load, spread,
  and cut. It takes the turner off the tray to carry each half to the plate. It takes the cloth off
  its spot to wipe the board. It grips food only to hand it over: in Step 4 it pinches the top slice
  at the right end and slides it to the left gripper. It never grips a half, never lifts or carries
  food, and touches the plate only with the turner.
* **Anchored lift.** A bread slice is lifted by the left gripper alone. Before the left gripper
  grips, the right gripper rests on the slice's right side so the slice cannot slide toward the left
  gripper as it pinches. The right gripper lifts off before the slice leaves the board. The right
  gripper may anchor the ham the same way in Step 3.
* **Hand over.** How a food item that starts at the right of the board gets to the left gripper.
  The right gripper pinches it by its right side, slides it flat along the board to the left until
  the left gripper can reach its left side, and holds still for half a second. The left gripper grips
  the left side. The right gripper lets go and lifts off. The item never leaves the board during a
  hand-over. After that only the left gripper lifts it.
* **Nothing is passed in the air.** A hand-over happens on the board, with the item lying flat. No
  tool ever changes grippers.
* A gripper opens only over the board, over the tray in the tool's own place, over the cloth spot,
  or over the plate from the turner. Never open a gripper over bare tabletop, over the spread tub, or
  over the back half of the tray.

### Handling the tools

* **Every tool is taken by the handle, from above.** The right gripper comes straight down on the
  handle and lifts the tool straight up. The tool goes back the same way: laid flat in its own place,
  the knife and the turner on the tray and the cloth on its spot, then let go.
* **The knife is held two ways, and the wrist is what changes them.** The knife is carried **flat**
  for loading and spreading. For the cut the wrist turns it **edge down** on the way over. Turn the
  wrist while carrying, away from the board. Never move the knife around inside the fingers to do
  it.
* **The turner blade stays flat.** It goes under a half flat and comes out from under it flat.
* **A tool is never left lying on the board, never carried over the plate (except the turner), and
  never held while the left gripper is moving food.** Between uses it is in its place.
* **Do not change your grip on a tool while it is in the air.** Lay it back in its place, let go,
  and take it again.

### The build order

* **Layer order.** Layers go on in this order and no other: bottom slice (moved to the middle),
  spread, ham, top slice.
* The **slice at the right end of the board is the top slice** and the **other slice is the bottom
  slice**. This is set before the episode and does not change.
* Every layer lands **in the middle of the layer below it and straight with it**, with the bread
  sides roughly in line, not sticking out.

### How to handle the food

* Move one item at a time.
* Grip the bread and the ham **by a side**, close to the rim, so the gripper is not pressing on the
  middle of the slice.
* Carry every item flat and bring it straight down. Bring each item down until it is resting on the
  layer below, then let go. Never drop an item from above.
* A layer that lands off the middle or turned may be fixed. Push it straight with the gripper closed,
  pushing from the crust without pressing down, or lift it off and set it down again.
* **Do not change your grip while an item is in the air.** Taking a new grip after the item is
  resting is fine.
* A layer is settled when it stays still for 2 seconds after you let go.
* **Holding is not pressing.** When the left gripper holds bread still, it is closed and empty and it
  rests on the crust with just enough weight to stop the bread moving. It never presses down,
  flattens, or pats a layer. For the cut, Step 5.2, it pinches the crust instead of resting on it,
  and pinching is not pressing either. The bread is soft, and a gripper press dents or tears it.

## Steps

The steps are the same in all three configs, and each arm keeps the same role. Only the place the
bottom slice and the ham start from changes, so Steps 1 and 3 say where to look and which way to
carry. The top slice is at the far right in every config, so Step 4 is the same in all three.
Whatever is too far for the left gripper is handed over.

### Step 1: Get the bottom slice to the middle of the board

**Goal:** the bottom slice lies flat in the middle of the board, on the build spot.

The bottom slice starts at the back of the board in the middle (Config L1 and Config L2) or in the
back-left corner (Config M). Look where it is before reaching for it. It is lifted the same way in
every config. A slice lying flat on the board slides when a gripper pinches its side, so the right
gripper anchors it while the left gripper grips, and the left gripper alone lifts it.

* With the **right gripper**, closed and empty, rest on the **right side** of the bottom slice, on
  the crust, with just enough weight to stop the slice moving.
* With the **left gripper**, grip the bottom slice by its **left side**, close to the crust.
* With the **right gripper**, lift straight up off the crust and away.
* With the **left gripper**, lift the slice straight up off the board and carry it flat to the build
  spot in the middle of the board.
* With the **left gripper**, bring the slice straight down until it is resting flat, in the middle,
  and straight with the board. Hold still for half a second.
* With the **left gripper**, let go, then lift away.

**Check:** the bottom slice lies flat in the middle of the board. It is not folded, torn, or hanging
over an edge. The top slice and the ham are still where they started. If it lands off the middle,
the **left gripper**, closed, pushes it to the middle from the crust, or lifts it again the same way
and lays it down again. If it lands folded, lift it again and lay it down again.

### Step 2: Spread the bottom slice

**Goal:** the top of the bottom slice is covered with spread as fully as it can be, and the knife is
back on the tray.

#### 2.1 Load the knife

* With the **right gripper**, come straight down on the knife handle, grip it, and lift the knife
  straight up off the tray.
* With the **right gripper**, carry the knife flat to the spread tub, put the blade into the tub
  flat, press it into the spread, and lift it straight out.
* With the **right gripper**, lift the blade above the rim of the tub before moving toward the
  board.

#### 2.2 Hold the bread down

* With the **left gripper**, closed and empty, rest on the **left side** of the bottom slice, on the
  crust, with just enough weight to stop the slice moving. Do this **before the blade touches the
  bread**. Keep the gripper on the crust so it covers as little of the slice as possible.

#### 2.3 Spread across the slice

* With the **right gripper**, carry the loaded knife flat to the board and lay it on the face of the
  bottom slice so that the **flat side of the blade** touches the bread.
* With the **right gripper**, pull the blade across the top of the slice, keeping it flat.
* With the **right gripper**, keep going across the slice in strokes, aiming to cover the whole top,
  corner to corner and out to the crust. Spread right up to the left gripper. The bit of crust under
  the gripper does not count.
* With the **right gripper**, lift the blade off the slice before moving away.

**Full cover is the aim, not a number of strokes.** Take as many strokes as the slice needs.

**If the knife runs out of spread before the top is done,** the **right gripper** carries it back
to the tub and loads it again as in Step 2.1, then carries on where it stopped. The **left gripper**
keeps holding the slice the whole time. The knife does not go back to the tray between loads.

Keep the spread on the bread. Do not run the blade off the crust onto the board.

#### 2.4 Let go of the bread and put the knife back

* With the **left gripper**, lift straight up off the crust and away from the slice.
* With the **right gripper**, carry the knife back to the tray, lay it down flat in its own place,
  and let go.

**Check:** the top of the bottom slice is covered out to the crust, with at most a few small bare
spots. The knife is lying flat in its place on the tray. The bottom slice is still flat in the middle
of the board. No spread has been dragged onto the board. If a large part is still bare, the right
gripper takes the knife up again and covers it, with the left gripper holding the slice again, before
moving on. If the slice
was pushed out of place, the **left gripper** pushes it back to the middle from the crust, or lifts
it and puts it back in the middle, before going on.

### Step 3: Put the ham on

**Goal:** the ham sits in the middle of the spread on the bottom slice.

The ham lies at the middle of the left side of the board (Config L1), in the back-left corner
(Config L2), or at the back of the board in the middle, behind the build spot (Config M). Look where
it is before reaching for it. It is picked up the same way in every config.

* The right gripper may anchor the ham, the same way it anchors a slice. If the ham slides when it is
  pinched, with the **right gripper**, closed and empty, rest on the **right side** of the ham, on
  the rim, with just enough weight to stop it moving.
* With the **left gripper**, grip the ham by its **left side**, close to the rim.
* If the right gripper is anchoring, with the **right gripper**, lift straight up off the ham and
  away.
* With the **left gripper**, lift the ham straight up off the board and carry it flat over the bottom
  slice: to the right in Config L1, to the right and forward in Config L2, straight forward in
  Config M.
* With the **left gripper**, bring the ham down flat in the middle of the spread, then let go once it
  is resting.
* If the ham lands turned or off the middle, with the **left gripper**, closed, push it straight on
  the slice from its side. Do not press down on it or flatten it.

**Check:** the ham sits on the spread roughly straight with the bread, not turned across it, and it
does not hang off the bread far enough to fall. If it lands folded over on itself or hanging off the
slice, the **left gripper** lifts it off by its side and puts it down again.

**Expected state:** the board holds the spread bottom slice in the middle and the plain top slice at
the right end. The rest of the board is empty. The knife and the turner are lying on the
tray, and the cloth is in its spot.

### Step 4: Close the sandwich

**Goal:** the top slice is straight on the stack and the sandwich is closed.

The top slice is at the right end of the board in every config, which can be too far for the left
gripper. The right gripper anchors it and may slide it toward the left gripper first. The left
gripper grips it and lifts it alone.

* With the **right gripper**, pinch the top slice by its **right side**, close to the crust.
* If the left gripper cannot reach the left side of the slice where it lies, with the **right
  gripper** slide the slice flat along the board to the left, toward the left gripper, until the
  left gripper can reach its left side, and hold still for half a second. Keep the pinch. If the
  left gripper can already reach it, do not slide it.
* With the **left gripper**, grip the top slice by its **left side**, close to the crust.
* With the **right gripper**, let go of the slice and lift off.
* With the **left gripper**, lift the slice straight up off the board and carry it flat over the
  stack.
* With the **left gripper**, bring the slice down flat onto the ham so its sides line up with the
  bottom slice. Hold still for half a second.
* With the **left gripper**, let go, then lift away. The weight of the top slice alone closes the
  sandwich. Nothing presses it down.

**Check:** the sandwich is one straight stack with the two bread sides in line. The ham is not
sticking out past the bread far enough to hang loose. The stack sits flat and is not sliding apart.
If the top slice is clearly off the stack, the **left gripper**, closed, pushes it into line from the
crust without pressing down, or lifts it again and lays it down again.

### Step 5: Cut it on the diagonal

**Goal:** one diagonal cut, leaving a left half and a right half on the board.

The cut runs on the diagonal, from near the **back-left corner** to near the **front-right corner**.
That leaves the **left half** (the piece with the front-left corner) and the **right half** (the
piece with the back-right corner).

#### 5.1 Take the knife

* With the **right gripper**, come straight down on the knife handle, grip it, and lift the knife
  straight up off the tray.
* With the **right gripper**, turn the wrist as the knife comes over so the blade hangs **edge
  down**. Do this on the way, away from the board, and never by moving the knife around inside the
  fingers.

#### 5.2 Hold the sandwich and cut

* With the **left gripper**, pinch the sandwich by the **middle of its left side**, on the crust,
  and hold it still for the whole cut. Pinch just hard enough to stop the stack sliding. Do not press
  down on it. Do this after the knife is up and **before the blade touches the bread**.
* With the **right gripper**, bring the blade over the sandwich, edge down, and put the **tip of the
  knife** on the sandwich at the **back-left corner** or near it.
* With the **right gripper**, cut through the sandwich, bringing the blade down and along on the
  diagonal toward the **front-right corner** until the blade touches the board.
* With the **right gripper**, lift the blade straight up and away.

**The aim is one diagonal cut. Take as many cuts and presses as it takes.** If the
halves are still joined, put the blade back in the same cut and cut or press again, and keep going
until the halves come apart. Do not pull the halves apart. If the blade is clearly not getting
through no matter how many times you cut, the blade is too blunt: stop, end the episode, and write it
down as a knife fault.

#### 5.3 Put the knife back and let go

* With the **right gripper**, carry the knife back to the tray, lay it down flat in its own place,
  and let go.
* With the **left gripper**, lift straight up off the crust and away.

**Check:** the sandwich is in two halves, cut on the diagonal from near the back-left corner to near
the front-right corner. Both halves are still on the board. The knife is lying flat in its place on the
tray.

### Step 6: Put the two halves on the plate with the turner

**Goal:** both halves lie flat on the plate, cut edges facing each other so they roughly make the
square sandwich again, and the turner is back on the tray.

The turner is the only thing that lifts a half. Take the **right half first**, then the left half.
The left gripper holds the sandwich still for both pickups. The plate is on the left, so each half is
carried to the left across the board, high enough to pass over the left gripper. The halves are laid
down so the right half sits on the right side of the plate and the left half on the left side, cut
edges facing each other.

#### 6.1 Take the turner and hold the sandwich

* With the **right gripper**, come straight down on the turner handle, grip it, and lift the turner
  straight up off the tray, blade flat.
* With the **left gripper**, closed and empty, rest on the **front-left corner** of the left half, on
  the crust, with just enough weight to stop it sliding. Do this **before the turner blade touches
  the board**.

#### 6.2 Lift the right half

* With the **right gripper**, set the turner blade flat on the board at the **right side** of the
  right half, and slide it under the half toward the cut line until the whole half rests on the
  blade. The left half, held still, stops the right half sliding away from the blade.
* With the **right gripper**, lift the turner straight up, flat, so the half stays flat and the
  layers stay together.
* With the **right gripper**, carry the half flat to the left, across the back of the board and over
  the left gripper, to the plate. Bring the turner down until the blade rests on the **right side**
  of the plate with its tip pointing left.
* With the **right gripper**, tip the front of the blade down onto the plate and pull the turner
  straight back out to the right, so the half settles on the right side of the plate with its cut
  edge facing left.
* With the **right gripper**, lift the turner off the plate.

#### 6.3 Lift the left half

* With the **left gripper**, lift off the front-left corner and rest again on the **front crust** of
  the left half, in from the corner, so the left side of the half is free for the turner. Keep just
  enough weight to stop the half sliding.
* With the **right gripper**, set the turner blade flat on the board at the **left side** of the left
  half and slide it under the half toward where the cut line was, until the whole half rests on the
  blade.
* With the **left gripper**, once the half is on the blade, lift straight up off the crust and away.
* With the **right gripper**, lift the turner straight up, flat, carry the half flat to the left, to
  the plate, and bring the turner down until the blade rests on the **left side** of the plate with
  its tip pointing right, toward the first half.
* With the **right gripper**, tip the front of the blade down onto the plate and pull the turner
  straight back out to the left, so the half settles next to the first half with its **cut edge
  facing the first half's cut edge**. Together the two halves roughly make the square again.
* With the **right gripper**, lift the turner off the plate.

#### 6.4 Put the turner back and fix the halves

* With the **right gripper**, carry the turner back to the tray, lay it down flat in its own place,
  and let go.
* **Fixing is allowed here.** If a half landed off the middle, hanging over the rim, or with its cut
  edge turned away, the **left gripper**, closed and empty, pushes it into place on the plate so the
  two halves roughly make the square again. This is not a violation. Push from the crust, never from
  the cut edge, and do not press down on the half.

**Check:** both halves lie flat on the plate, cut edges facing each other, so together they roughly
make the square sandwich. Neither half hangs over the rim. Nothing has slid out from between the
bread. The turner is lying flat in its place on the tray.

**Expected state:** the plate holds both halves. The board holds nothing but loose scraps. The knife
and the turner are in their places on the tray, and the cloth is still in its spot.

### Step 7: Wipe the scraps into the tray

**Goal:** every scrap is off the board and in the back half of the tray, against the board. The
board is clean, the cloth is back in its spot, and both arms are safely home.

The cloth is the wiping tool. Nothing is picked up in this step, no matter how big, and the knife is
not used to sweep.

#### 7.1 Wipe

* With the **right gripper**, come straight down on the cloth in its spot, grip it, and lift it
  straight up.
* With the **right gripper**, set the cloth flat on the board at the **back edge**, at the right end
  of the board.
* With the **right gripper**, pull the cloth **from the back to the front** across the board so the
  scraps gather in front of it at the front of the board. Keep the cloth touching the board for the
  whole stroke.
* With the **right gripper**, do this again in strips, working from the right end of the board to
  the left, until everything on the board sits along its front edge.
* With the **right gripper**, push the gathered scraps straight forward over the board's front edge
  so they drop into the **back half of the tray**, the empty strip against the board. Do this again
  until the board is clean.
* Wipe fallen ham and torn bread the same way as crumbs. Do not stop to pick anything up.
* Every stroke goes toward the tray. Do not push scraps over the back, left, or right edge of the
  board onto the tabletop, and do not push them as far as the knife and the turner in the front half
  of the tray.

#### 7.2 Put the cloth away

* With the **right gripper**, lift the cloth off the board, carry it back to the cloth spot on the
  right, lay it flat, and let go.

**Check:** the board is clean. The scraps are in the back half of the tray. Nothing was pushed off
any other edge onto the tabletop. The knife and the turner are lying flat in their places on the
tray, and the cloth is lying flat in its spot.

#### 7.3 End the episode

* Check that the plate holds both halves, the board is empty, the knife and the turner are on the
  tray, and the cloth is in its spot.
* Bring both arms home, then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the two halves off the plate and set them aside to throw away.
2. Tip the scraps out of the tray into the bin and wipe the tray dry.
3. Wipe the board clean and dry, and put it back flat in the middle of the tabletop with its front
   edge against the back lip of the tray.
4. Wipe the knife and the turner clean and dry and lay them flat in their places across the front
   half of the tray, handles to the right. Shake out the cloth or get a new one, and lay it folded
   flat in its spot right of the board.
5. Lay out the food for the next episode's config: two fresh bread slices and one slice of ham,
   flat on the board. Config L1: ham at the middle of the left side, bottom slice at the back in the
   middle, top slice at the far right. Config L2: ham in the back-left corner, bottom slice at the
   back in the middle, top slice at the far right. Config M: ham at the back in the middle, bottom
   slice in the back-left corner, top slice in the back-right corner. Change the config between
   episodes instead of laying out the same one every time.
6. Top up the spread tub if it no longer holds enough to cover a whole slice. Leave it open in its
   place right of the board, with the lid set aside.
7. Swap out any slice that is torn, dried out, or stuck to another slice.
8. Wipe the tabletop and put the plate back, empty, against the left edge.
9. Go through both Setup checklists again.

## SOP violations

These are things that break the SOP. They are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, write down the **start timestamp**, the **violation name**, and the **SOP rule
broken**. The visible cue is what the reviewer sees. The coaching note is for training and is not an
annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not
delete it just because a rule was broken.

### Violations

**Note on the start position:** the violations below were written for Config L1 (the ham at the
middle of the left side, the bottom slice at the back in the middle, the top slice at the far
right). The pickup cues will be rewritten later to cover all three start positions. For now they
stay as they are. Until then, anything that does not match the episode's config goes under **Config
misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the operator does does not match the config on the board. The food is not in
  the start position for the config. Or the left gripper reaches across the board for an item at
  far right instead of getting it in a hand-over. Or the right gripper lifts or carries a food item
  instead of sliding it to the left gripper. Or an arm does the other arm's work because of where
  the food is.
* **SOP rule broken:** the start position and the hand-over rule (the left gripper puts every food
  item down in every config; the top slice at the far right is pinched and slid to the left gripper
  by the right gripper and handed over on the board; the steps and the arm roles are the same in all
  three configs).
* **Coaching note:** look where the food is before the first reach. The moves are the same in every
  config, only the start place changes.

**Violation: Wrong slice used as the bottom**

* **Visible cue:** the top slice is carried to the middle and spread, or the two slices are swapped
  part way through the build.
* **SOP rule broken:** Step 1 and Step 4, the slice at the right end of the board is the top slice
  and the other slice is the bottom slice, set before the episode.
* **Coaching note:** the slice at the right end is the top, every episode.

**Violation: Built in the wrong order**

* **Visible cue:** the layers go on in any order other than bottom slice, spread, ham, top slice.
  For example the ham before the spread, or the top slice put on before the ham.
* **SOP rule broken:** Steps 1 to 4, layer order: bottom slice to the middle, spread, ham, top
  slice.
* **Coaching note:** say the next layer to yourself before you reach for it.

**Violation: Wrong arm did the work**

* **Visible cue:** the left gripper takes the knife, the turner, or the cloth, or goes into the
  spread tub. Or the right gripper grips a half, lifts or carries any food, or touches the plate
  with anything but the turner. Or the left gripper goes to the plate before the turner is back on
  the tray. The right gripper anchoring a slice or the ham, or pinching and sliding a food item to
  the left gripper in a hand-over, is not this violation. The left gripper pushing the halves into place in
  Step 6.4 is not either.
* **SOP rule broken:** Steps 1 to 7, the left arm owns the food and the last fix on the plate, the
  right arm owns the tools and the tub and goes to the plate only with the turner, and neither arm
  does the other arm's work.
* **Coaching note:** left hand for food, right hand for tools. Anchoring is not gripping.

**Violation: Bread not held during the spread**

* **Visible cue:** the blade touches the bottom slice with no left gripper on its crust, the left
  gripper arrives after the first stroke has started, or it lifts off between strokes or while the
  knife is being loaded again, and the slice slides or folds up under the knife.
* **SOP rule broken:** Step 2.2 and Step 2.3 (the left gripper rests on the left side of the slice
  before the blade touches the bread and keeps holding through every stroke and every reload).
* **Coaching note:** hold the bread first, let go of it last.

**Violation: Spread stopped short**

* **Visible cue:** the knife goes back to the tray with a large part of the top of the slice still
  bare, a whole side or corner the blade never reached, or an empty blade dragged across the slice
  instead of taken back to the tub. The ham then goes down on a mostly bare slice. A few small bare
  spots or thin patches are not this violation.
* **SOP rule broken:** Step 2.3 (keep going across the slice in strokes, aiming to cover the whole
  top, corner to corner and out to the crust; if the knife runs out of spread, go back to the tub and
  load it again).
* **Coaching note:** look at the whole slice before you put the knife down. An empty blade means go
  back to the tub, not press harder.

**Violation: Blade held the wrong way**

* **Visible cue:** the spread is done with the blade edge down instead of flat, or the cut is made
  with the blade still flat instead of turned edge down. Or the blade is turned while it is already
  touching the bread instead of on the way over.
* **SOP rule broken:** Step 2.3 and Step 5.1, flat for loading and spreading, and the wrist turned
  edge down on the way over for the cut, turned while carrying and away from the board.
* **Coaching note:** flat to spread, edge down to cut, and turn it before you arrive.

**Violation: Tool left out of its place between uses**

* **Visible cue:** the knife or the turner is left on the board, on the tabletop, or in the wrong
  place on the tray between uses. Or the cloth is left on the board or put on the tray instead of
  back in its spot. Or a tool is kept in the right gripper while the left gripper moves food. Or the
  right gripper moves its grip along a handle without laying the tool down first.
* **SOP rule broken:** Steps 2.4, 5.3, 6.4, and 7.2, the knife and the turner go back flat to their
  own places on the tray and the cloth goes back to its spot between uses, no tool is held while food
  is being moved, and no tool is gripped again in the air.
* **Coaching note:** the tool goes home after every use. The cloth's home is its spot, not the
  tray.

**Violation: Sandwich not held during the cut**

* **Visible cue:** the blade comes down on a sandwich no gripper is holding, the left gripper arrives
  after the blade has touched the bread, or it lifts off before the knife is back on the tray, and
  the stack slides, spins, or comes apart under the press.
* **SOP rule broken:** Step 5.2 and Step 5.3 (the left gripper pinches the middle of the left side
  before the blade touches the bread and holds it still until the knife is back on the tray, just
  hard enough to stop the stack sliding).
* **Coaching note:** the left hand holds the sandwich before the blade comes down.

**Violation: Cut is not one diagonal**

* **Visible cue:** the cut runs straight across the sandwich instead of on the diagonal, it runs on
  the other diagonal, a second cut line is started, or the halves are pulled apart after a cut that
  did not go all the way through.
* **SOP rule broken:** Step 5.2 (put the tip at or near the back-left corner and cut on the diagonal
  toward the front-right corner, down to the board; one cut, as many cuts and presses as it takes in
  that same cut).
* **Coaching note:** tip near the back-left corner, cut on the diagonal toward the front-right, all
  the way to the board.

**Violation: Half moved without the turner**

* **Visible cue:** a gripper closes on a sandwich half and lifts, drags, or carries it, or a half is
  pushed onto the plate by a gripper or by the knife instead of being carried on the turner.
* **SOP rule broken:** Step 6, the turner is the only thing that lifts a half, and no gripper ever
  picks up a sandwich half.
* **Coaching note:** the turner carries every half. Fingers never close on one.

**Violation: Sandwich not held while the turner goes under**

* **Visible cue:** the turner blade goes under a half with no left gripper on the left half, the
  half slides ahead of the blade instead of riding up onto it, or the left gripper lifts off before
  the whole half is on the blade.
* **SOP rule broken:** Step 6.1 to 6.3 (the left gripper rests on the crust of the left half before
  the turner blade touches the board and keeps holding until each half is resting on the blade).
* **Coaching note:** hold the left half so the blade has something to push against.

**Violation: Wrong plating order**

* **Visible cue:** the left half is lifted onto the turner first, or both halves are put onto the
  turner together.
* **SOP rule broken:** Step 6, take the right half first, then the left half, one half per trip.
* **Coaching note:** right half first, one trip each.

**Violation: Half tipped or slid off the turner**

* **Visible cue:** the turner hits the left gripper or the board on the way to the plate, the half
  is dropped off the raised blade onto the plate instead of brought down and slid off, or the turner
  is pulled out from under the half while the blade is still up in the air.
* **SOP rule broken:** Step 6.2 and Step 6.3 (lift and carry the turner flat and over the left
  gripper, bring it down until the blade rests on the plate, then tip the front of the blade down
  and pull the turner straight back out).
* **Coaching note:** flat in the air, over the other hand, down on the plate, then slide out.

**Violation: Halves put on the plate wrong**

* **Visible cue:** the episode moves on from Step 6 with a half lying cut edge out, the right half on
  the left side of the plate or the left half on the right, the halves on top of each other, a half
  tipped up on its cut edge, or a half hanging over the rim, and the fix allowed in Step 6.4 was not
  done.
* **SOP rule broken:** Step 6 (both halves flat on the plate, right half on the right and left half
  on the left, cut edges facing each other so they roughly make the square again, nothing hanging
  over the rim; the left gripper pushes them into place in Step 6.4 if needed).
* **Coaching note:** cut edges face each other, both flat, the square put back together. Fix it
  before the cloth comes out.

**Violation: More than one item moved at once**

* **Visible cue:** the ham and a slice are lifted together, both halves are carried on the turner in
  one trip, or the left gripper moves food while a tool is still in the right gripper.
* **SOP rule broken:** Steps 1 to 6, move one item at a time, and no tool is held while food is
  being moved.
* **Coaching note:** one item per trip, every trip.

**Violation: Item dropped instead of put down**

* **Visible cue:** the left gripper opens above the board or the stack and the slice or the ham falls
  the rest of the way, instead of being brought down until it is resting.
* **SOP rule broken:** Steps 1, 3, and 4, bring each item down until it is resting on the layer
  below, then let go, and never drop an item from above.
* **Coaching note:** take it all the way down before you open the gripper.

**Violation: Gripper opened over the wrong place**

* **Visible cue:** a gripper opens over bare tabletop, over the spread tub, or over the back half of
  the tray. Or the knife or the turner is set down anywhere other than its own place on the tray.
  Or the cloth is set down anywhere other than its spot. Or food is set down anywhere other than the
  board or, from the turner, the plate.
* **SOP rule broken:** Steps 1 to 7, a gripper opens only over the board, over the tray in the tool's
  own place, over the cloth spot, or over the plate from the turner.
* **Coaching note:** know where it will land before you open the gripper.

**Violation: Scraps picked up or moved with the wrong tool**

* **Visible cue:** a gripper closes on a piece of ham, bread, or a crumb and carries it away, a bare
  gripper brushes the board, or the knife or the turner is used to push the scraps instead of the
  cloth.
* **SOP rule broken:** Step 7 (the cloth is the wiping tool; nothing is picked up in this step, no
  matter how big, and the knife is not used to sweep).
* **Coaching note:** the cloth clears the board. Fingers never touch a scrap.

**Violation: Board not wiped clean**

* **Visible cue:** the episode gets to the end with scraps still on the board, or the wiping stops
  while crumbs, fallen ham, or torn bread are still lying on the board.
* **SOP rule broken:** Step 7.1 (keep going in strips until the whole board is clean and everything is
  in the back half of the tray).
* **Coaching note:** keep wiping until the board is bare, not until it looks tidy.

**Violation: Scraps pushed off the wrong edge**

* **Visible cue:** a stroke pushes scraps over the back, left, or right edge of the board onto the
  tabletop or the floor, or pushes them as far as the knife and the turner in the front half of the
  tray, instead of over the front edge into the back half of the tray.
* **SOP rule broken:** Step 7.1 (pull the cloth from the back to the front, gather the scraps along
  the front edge, and push them over the front edge into the back half of the tray; do not push
  scraps over any other edge).
* **Coaching note:** every stroke ends in the tray, on the side against the board.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with the knife or the turner off its place on the tray, the cloth
  off its spot, a half still on the board, scraps still on the board, or an arm not at home.
* **SOP rule broken:** Step 7.3 (check both halves on the plate, the board empty, the knife and the
  turner on the tray, and the cloth in its spot; bring both arms home; then stop recording).
* **Coaching note:** check first. Going home is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was done. Write them down as system issues, throw the
episode away, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its picture** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, a crash caused by the controller, or a motor
  error.
* **Bad ingredient:** a slice found torn, dried hard, or stuck to the board during the episode, or
  ham that comes apart in pieces. Swap it out before the next episode.
* **Spread tub runs empty** before the top of the slice is covered, so there is nothing left to load
  the knife with. Top it up before the next episode.
* **Knife fault:** a blade that will not cut the halves apart no matter how many times it is pressed
  on the same line, or a handle too slippery or too thin for the gripper to lift off the tray.
  Sharpen or swap the knife before the next episode.
* **Turner or cloth fault:** a turner blade too thick to go under a half without tearing it, or a
  cloth too soft to push scraps. Swap it before the next episode.
* **Board, tray, tub, or plate moves out of its place** during the episode.

## Annotation subtasks (from SOP)

1. Anchor a bread slice, lift it with the left gripper, and lay it down
2. Hand a food item over to the left gripper on the board
3. Take the knife off the tray and load it with spread
4. Hold the bottom slice down while the knife works
5. Spread across the bottom slice
6. Put a tool back in its place
7. Move the ham onto the bottom slice
8. Hold the sandwich still for the cut
9. Cut the sandwich on the diagonal
10. Slide the turner under one half
11. Carry one half on the turner to the plate and slide it off
12. Push a half into place on the plate
13. Wipe the scraps off the board into the tray with the cloth
14. Bring both arms home and end the episode
