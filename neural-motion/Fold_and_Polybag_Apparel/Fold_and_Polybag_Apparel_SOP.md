# Fold and Polybag Apparel SOP

This SOP covers packing a single garment: opening it out and squaring it flat and face down with its
collar to the left, laying the packing board on its collar half, folding the near side, the far
side, the tail and then the hem half over the board so the board stays inside the folded packet,
flipping the packet face up so its collar comes to the right, feeding it collar first into a poly
bag, sealing the flap, stacking the pack and applying one size label on top,
using a two-arm robot system. Both arms are used throughout: the grippers cooperate to open out,
square, fold, flip, bag, seal, stack and label, with the left and right grippers taking the roles
called out in each step. The task runs from one rumpled garment lying in the garment start zone, the
packing board on the board park at the back-center and one poly bag lying at the back to the right
of the board, to a sealed and labelled pack lying on top of the output stack in the back-right
corner.

The table is set up in one of three ways. Only the garment and the size label move; the packing
board, the poly bag, the working area and the output stack are in the same place in all three.

* **Config L:** the garment is at the left-center, in front of the left gripper. The label is at
  the right-center.
* **Config M:** the garment is at the front-center, in front of the working area. The label is at
  the right-center.
* **Config R:** the garment is at the right-center, in front of the right gripper. The label is at
  the left-center.

Where a step depends on the setup it says so on an **IF** line: look at the table and follow the
line that matches.

What stays constant across all sessions:

* **Start position:** the garment starts at the left-center (**Config L**), the front-center
  (**Config M**) or the right-center (**Config R**). One config per episode, chosen before recording
  and never changed mid-episode.
* **Same-side rule:** the gripper on the garment's side picks it: the **left gripper** in Config L
  and M, the **right gripper** in Config R. The same goes for the label: the **right gripper** takes
  it from the right-center in Config L and M, the **left gripper** takes it from the left-center in
  Config R. No arm reaches across the table for the garment or the label. Nothing is handed over.
* **Layout:** the packing board on the board park at the back-center, the poly bag at the back
  immediately to the right of the board, and the output stack in the back-right corner are in the
  same place in all three configs. The working area is the center of the table. The label spot is
  the right-center in Config L and M and the left-center in Config R.
* **Arm roles:** the **left gripper** picks the garment in Config L and M, carries the board,
  takes the flat hold on the board for the half fold, flips the packet, lifts the packet and feeds
  it into the bag, turns the bunch over, holds the bag through the push and the seal, takes the
  back-left corner of the pack for the stack, and takes the label in Config R. The **right
  gripper** picks the garment in Config R, folds the tail and the hem half, drags the poly bag to
  the working area, holds the bag while the collar goes in, pushes the rest of the packet through,
  drags the pack to the output stack, takes the front-right corner of the pack for the stack, takes
  the label in Config L and M, and drags the stack into the corner. Both grippers together lay the
  garment open, adjust the board, fold the near side and the far side, fold the sleeves back, take
  turns on the flap while sealing, lay the pack down and turn it, lift the pack onto the stack, and
  adjust the label.
* **Working position:** the garment is always moved to the center of the table, into the working
  area, before anything is opened out, squared or folded.
* **Garment orientation:** from the end of Step 2 the garment lies face down with its collar to the
  left and its hem to the right, so its length runs left to right across the working area. The
  collar stays to the left through the four folds. The flip in Step 8 brings the collar to the
  right, and the packet goes into the bag collar first. When the sealed pack is laid down it is
  turned so its collar end is toward the back edge, and it is stacked that way.
* **Board rule:** the board goes onto the garment, never the garment onto the board. Only the left
  gripper carries the board. The board may land folded over on itself: it is lifted again and
  unfolded, and either gripper may adjust it until it lies square. The board is squared before the
  first fold. The board stays inside the packet: it is never drawn out, and it goes into the bag with
  the garment.
* **Fold target:** four folds over the board, near side, far side, tail, then the hem half onto the
  upper part, to a packet matching the board footprint with the board inside, checked on all four
  sides before the flip.
* **Pack order:** square, board on, near side, far side, tail, half fold, flip, bag, seal, stack,
  label. The pack is stacked before the label goes on. The order never changes and no step is
  skipped.
* **Bagging:** the right gripper holds the bag, the left gripper feeds the packet in collar first,
  the bunch is turned over, the rest of the packet is pushed through, and the flap is sealed with
  the pack still held. This may be done in the air or with the bag resting on the table, whichever
  gets the packet in cleanly. The pack is laid down only once the bag is sealed.
* **Seal rule:** the seal strip is exposed from staging, so there is no liner to peel during the
  episode. The flap is bent down over the mouth onto the bag wall while the pack is held, the
  grippers taking turns holding and folding, until the bag is fully sealed.
* **One at a time:** exactly one garment, one board, one poly bag and one size label are handled per
  episode, and exactly one pack goes onto the output stack.

## Setup

Go through both checklists before starting the episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

* Cameras are on and recording
* Env camera frame includes the whole table from the front edge to the back edge and both side
  edges, so the garment in its start zone, the board and the bag at the back, the label on its spot
  and the output stack in the back-right corner are all in frame, and is centered on the table's
  midpoint
* The working area is visible from above, and the space above it is in frame, so every fold, the
  flip, the bagging, the seal and the stacking can be seen
* The left arm reaches the left-center, the front-center, the board park, the whole working area,
  the left-center label spot and the back-left corner of a pack lying on the output stack; the right
  arm reaches the right-center, the bag start zone at the back, the whole working area, the
  right-center label spot and the output stack in the back-right corner, without either arm
  stretching or colliding with the other
* Both arms are at the home position with grippers open
* Table surface is clear of any objects other than the garment, the packing board, the poly bag, the
  size label and the output stack

### Materials checklist

* One garment, the only one handled in the episode, lies in the garment start zone as it comes:
  rumpled, any way up and any way round. It is not flattened or squared before the episode; opening
  it out and squaring it is Step 2
  * **Config L:** left-center, level with the working area and to its left, in front of the left
    gripper
  * **Config M:** front-center, in front of the working area, between it and the front edge
  * **Config R:** right-center, level with the working area and to its right, in front of the right
    gripper
* The garment is wide enough that both sleeves and both side edges stand outside the packing board
  when the board is centered on it, and long enough that its hem end stands out past the right edge
  of the board when the board is squared on its collar half, so all four folds have something to
  fold
* The packing board is a plain, flat rectangle with no tab, thin enough to go into the bag inside
  the packet. It is thin enough to fold over on itself when it hangs from one gripper; that is
  expected and is handled in Step 3. It lies flat on the board park at the back-center, at the very
  back, long edges running left to right, clear so the left gripper can take it from above
* The working area at the center is clear and dry
* One poly bag lies flat at the back, in the bag start zone immediately to the right of the board,
  with its mouth facing left toward the board, its flap lying out flat beyond the mouth, and its
  seal strip exposed, clean and facing up. No liner is on the strip; nothing is peeled during the
  episode
* The bag mouth is wider than the packing board and the bag is deeper than the board is long, so a
  packet folded to the board footprint goes fully in without being squeezed
* One size label lies flat and face up on the label spot, already peeled from its backing, so a
  gripper can take it straight off the table
  * **Config L and M:** right-center, in front of the right gripper
  * **Config R:** left-center, in front of the left gripper
* The output stack in the back-right corner holds at least one packed garment, lying flat with its
  collar end toward the back edge, and the packs in it lie square on each other with the top one
  flat and clear so the new pack can be lowered onto it

### Workspace layout

* **Garment start zone:** where the rumpled garment (input) lies: left-center, level with the
  working area and to its left (**Config L**), front-center, in front of the working area
  (**Config M**), or right-center, level with the working area and to its right (**Config R**)
* **Back-center:** board park, at the very back: where the packing board rests at the start of the
  episode. It is empty from Step 3 on, because the board goes into the bag inside the packet
* **Back, right of the board:** bag start zone: where the one poly bag lies at the start
* **Center:** working area: where the garment is opened out and squared, the board is laid on it,
  the four folds are made and the packet is flipped. The packet is bagged here, in the air or on
  the table, and the sealed pack is laid back down here before it is stacked
* **Label spot:** where the size label lies: right-center, in front of the right gripper
  (**Config L** and **M**), or left-center, in front of the left gripper (**Config R**)
* **Back-right corner:** output stack: the packed garments, where the finished pack is stacked and
  labelled

## Vocabulary

These are the terms used in this SOP. Collectors and annotators must use this language consistently.
One term per concept, used throughout.

### Garment anatomy

* **Garment:** one apparel item. One garment per episode.
* **Collar:** the collar or waistband edge of the garment. It lies to the left from the end of Step
  2 until the flip in Step 8, then to the right.
* **Collar points:** the two ends of the collar, where it meets the side edges.
* **Hem:** the edge opposite the collar. It lies to the right until the tail fold.
* **Collar end:** the end of the garment carrying the collar. **Hem end:** the end carrying the hem.
* **Side edge:** one of the two edges running between the collar and the hem. The **near side**
  **edge** is the one toward the front edge, the **far side edge** the one toward the back edge.
* **Sleeve:** one of the two arms standing out from the side edges at the collar end. The **near**
  **sleeve** stands toward the front edge, the **far sleeve** toward the back edge.
* **Upper part:** the collar half of the body, the half the board lies on.
* **Tail:** the hem half of the body, the part standing out past the right edge of the board once
  the board is squared.
* **Hem corner:** one of the two corners where the hem meets a side edge. The **near hem corner** is
  the one toward the front edge, the **far hem corner** the one toward the back edge.
* **Face down:** the front of the garment is against the table. **Face up:** the front of the
  garment shows.
* **Rumpled:** how the garment lies at the start: bunched, with edges and sleeves folded into the
  body, any way up and any way round.

### Packaging anatomy

* **Packing board:** the flat rectangle that sets the finished packet size and stays inside the
  packet. It lies long edges running left to right, so its long edges are its near edge and far edge
  and its short edges are its left edge and right edge. It is thin, and it can fold over on itself
  while it hangs from one gripper. It is called the board in the steps.
* **Board footprint:** the rectangle the packing board covers. It is the target size of the folded
  packet.
* **Packet:** the garment after all four folds, lying flat with the board inside, nothing standing
  outside the board footprint and no layer standing up or hanging loose. Its **near edge** and
  **far edge** are the two side-fold creases. Its two ends are the **collar end** and the
  **half-fold crease**: the collar end is on the left until the flip and on the right after it.
* **Poly bag:** one flat bag holding one packet. Its **bag mouth** is the open end, its **bag wall**
  is the face of the bag the flap is bent down onto, its **top face** is whichever face of the bag
  is up once the pack lies on the stack, and its **bag flap** is the lip beyond the mouth.
* **Seal strip:** the adhesive strip on the flap. It is exposed from staging; there is no liner.
* **Sealed bag:** the flap bent down over the bag mouth onto the bag wall and pressed, so the seal
  strip has taken hold across the full width, no corner is lifting, and the flap stays down.
* **Sealed end:** the end of the bag carrying the mouth and the sealed flap. It is the end the
  packet went in by, so the hem end of the packet is at this end. Once the pack is laid down and
  turned, it is toward the front edge.
* **Bunch:** the packet and the bag together, from the moment the collar has entered the mouth until
  the packet is fully inside.
* **Size label:** the adhesive label carrying the garment size, lying peeled and face up on the
  label spot.
* **Pack:** one sealed bag holding one packet with its board. It carries one size label once
  Step 13 is done.
* **Output stack:** the packed garments lying flat on each other in the back-right corner. The
  finished pack goes on top of it.

### Workspace zones

* **Garment start zone:** where the rumpled garment lies at the beginning of the episode:
  left-center (**Config L**), front-center (**Config M**), or right-center (**Config R**). One per
  episode, chosen before recording and never changed mid-episode.
* **Board park:** the back-center of the table, at the very back, where the packing board rests
  before Step 3.
* **Bag start zone:** the back of the table immediately to the right of the board, where the poly
  bag lies before Step 9.
* **Working area:** the center of the table where the garment is opened out and squared, the board
  is laid on it, the folds are made and the packet is flipped, and where the packet is bagged.
* **Label spot:** where the size label lies: the right-center in Config L and M, the left-center in
  Config R.
* **Output stack:** the back-right corner of the table, where the packed garments lie and the
  finished pack is stacked in Step 12 and labelled in Step 13.
* **Home position:** the default resting pose for each arm: gripper open and clear of the table.

### Actions

* **Pick:** lift the garment clear of the table and carry it to the working area, with the gripper
  on the garment's side: the left gripper in Config L and M, the right gripper in Config R.
* **Lay open:** how a rumpled garment is opened out. There is no set grip or order: both grippers
  work together, taking turns and replacing each other as needed, lifting, spreading and laying the
  garment out until it lies flat, collar to the left and hem to the right, sleeves out to their
  sides. Any edge folded under is folded inward and then outward by the gripper that can reach it.
* **Squared:** the garment lying flat and face down in the working area, collar to the left and hem
  to the right, both sleeves lying out flat to their sides, no ridge across the body, and no corner
  or edge folded under itself.
* **Drape flip:** how a face-up garment is turned over. Both grippers lift the far side until the
  near side edge peels off the table, carry the hanging side toward the front edge and down in one
  smooth motion, and release so the garment lands flat. It is never flung.
* **Lay the board:** the left gripper lowers the packing board onto the collar half of the squared
  garment so its left edge lies just inside the collar and its long edges run along the garment's
  length.
* **Unfold the board:** when the board has landed folded over on itself, the left gripper lifts it
  again and tilts or shakes it so the other half of the board falls open, while the right gripper
  anchors the garment, then lays it again.
* **Adjust the board:** the left gripper, the right gripper or both lift the board just clear and
  lay it again, or nudge it, until it lies square on the garment: left edge just inside the collar,
  long edges along the garment's length, and the same width of garment standing outside the board
  on the near side and on the far side.
* **Flat hold:** a gripper closed and resting on the board, the garment or a packet to keep it from
  sliding while the other gripper works. During a fold it lifts clear as the incoming layer reaches
  it, so the fold lands flat.
* **Side fold:** both grippers take one side of the garment, the left gripper at the sleeve and the
  right gripper at the hem end, carry it over the board together and lay it down so the crease runs
  along the board edge. The body of the garment stays on the table.
* **Tail fold:** lift the hem, carry it to the left over the body and lay it down so the hem lies
  along the right edge of the board, doubling the tail on itself beyond the board.
* **Half fold:** lift the doubled tail by its crease, carry it to the left up and over the right
  edge of the board, and lay it down on the board so the crease runs along the right edge of the
  board.
* **Flip:** the left gripper closes on the collar end of the packet through all layers and the
  board, lifts that end and turns the packet up onto its other end and over toward the right in one
  smooth motion, so it lands flat and face up with its collar now to the right.
* **Hold the bag:** hold the poly bag by its wall near the mouth, in the air or resting on the
  table, so the mouth stands open and faces the packet. The holding gripper may let go and take the
  bag again at another place to get a better hold.
* **Feed in:** bring the collar end of the packet to the open mouth and push it in, collar first,
  until the collar has entered the bag.
* **Turn the bunch:** holding the packet and the bag together where they join, turn the whole bunch
  over smoothly, so the face of the garment looks down, the bag is on the left and the
  packet on the right.
* **Push through:** with the bag held by its upper part, push the rest of the packet through the
  mouth until the whole packet is inside.
* **Seal:** with the pack held, bend the flap down over the mouth onto the bag wall and press it
  so the seal strip takes hold across the full width, the grippers taking turns holding the pack and
  folding the flap.
* **Turn the pack:** with the pack lying flat, both grippers turn it on the table so its collar end
  is toward the back edge.
* **Drag:** slide the bag, a pack or the stack along the table, keeping it flat, without lifting
  it.
* **Stack:** lift the pack by two corners, the right gripper at its front-right corner and the left
  gripper at its back-left corner, and lower it onto the top pack of the output stack so its edges
  line up with the pack below.
* **Apply:** press the size label flat onto the top face of the pack lying on top of the output
  stack.
* **Lift:** come straight down onto the grasp point, close, and raise straight up until there is
  daylight under the thing, before anything moves sideways.
* **Lower on:** carry level over the spot, lower straight down until the thing is resting, and
  release once it is resting. Nothing is dropped from height.

## Steps

Step 1 and Step 13 depend on the config: in Config L and M the **left gripper** picks the garment
and the **right gripper** takes the label from the right-center; in Config R the **right gripper**
picks the garment and the **left gripper** takes the label from the left-center. Every other line is
the same in all three configs.

### Step 1: Move the garment into the working area

**Goal:** the garment lies in the middle of the working area, ready to be opened out.

Look where the garment is before reaching for it.

* **IF the garment is at the left-center (Config L):** with the **left gripper**, close on the
  garment, lift it clear of the table and carry it to the center. The **right gripper** stays clear.
* **IF the garment is at the front-center (Config M):** with the **left gripper**, close on the
  garment, lift it clear of the table and carry it to the center. The **right gripper** stays clear.
* **IF the garment is at the right-center (Config R):** with the **right gripper**, close on the
  garment, lift it clear of the table and carry it to the center. The **left gripper** stays clear.

Then, in all three:

* Lower the garment into the middle of the working area and release.
* Confirm the garment lies in the working area with clear table around it, the garment start zone
  is empty, and the board park still holds the board.

### Step 2: Open the garment out and square it

**Goal:** the garment **squared** in the working area, collar to the left, ready for the board.

#### 2.1 Lay it open

* Both grippers **lay open** the garment. There is no set grip or order: the **left gripper** and
  the **right gripper** work together, taking turns and replacing each other as needed, to lift,
  spread and lay the garment out until it lies flat with its collar to the left, its hem to the
  right, and both sleeves lying out to their sides.
* For any edge or corner folded under itself, the gripper that can reach it, the **left gripper**
  or the **right gripper**, folds that edge inward toward the middle and then outward again until it
  lies flat.
* If a sleeve or the hem is still bunched into the body, or the collar is not at the left end, the
  **left gripper** and the **right gripper** lift and lay that part out again.

#### 2.2 Check the face orientation

* Look at the garment. If it is face down, go on to Step 3.
* If it is face up, the **left gripper** closes on the **far sleeve** and the **right gripper** on
  the far side edge at the hem end, both lift the far side, and make a **drape flip** toward the
  front edge, then release. The collar stays to the left.
* If it lands bunched, the **left gripper** and the **right gripper** spread it flat and the flip
  is made again.

Never fling the garment over. A flung garment lands folded under itself and has to be spread again.

**Check:** the garment is **squared**: flat, face down, collar to the left and hem to the right,
both sleeves lying out flat, no ridge across the body, and no corner or edge folded under itself.
The board does not go on until this check passes.

### Step 3: Lay the board on the garment

**Goal:** the packing board lies flat and open on the collar half of the squared garment, centered
between the near and far side edges, its long edges running along the garment's length, its left
edge just inside the collar, and its right edge across the middle of the body.

* With the **left gripper**, close on the board on the board park at the back-center, lift it clear
  of the table and carry it forward over the garment. Only the **left gripper** carries the board;
  the **right gripper** stays clear.
* The **left gripper lays the board** on the collar half of the garment, left edge just inside the
  collar, and releases.
* The board may land folded over on itself, because it hangs from the one gripper. If it does, the
  **left gripper unfolds the board**: lifts it again and tilts or shakes it so the other half of the
  board falls open, while the **right gripper** anchors the garment with a **flat hold**, then lays
  the board again and releases.
* The **left gripper**, the **right gripper** or both **adjust the board** until it lies square:
  lift it just clear and lay it again, or nudge it, until its left edge lies just inside the collar,
  its long edges run along the garment's length, and the same width of garment stands outside the
  board on the near side and on the far side along the whole length.
* Confirm both side edges and both sleeves stand outside the board, the same width on the near side
  as on the far side, and the hem end stands out past the right edge of the board.

**Warning:** The board goes onto a squared garment. Nothing is folded until the board lies open and
square on it.

### Step 4: Fold the near side over the board

**Goal:** the near side folded in over the board, with the crease running along the near edge of
the board and continuing straight to the hem, and nothing standing outside the board footprint on
that side.

* The **left gripper** closes on the **near sleeve** and the **right gripper** closes on the **near
  hem corner**, at the same time.
* Both grippers make the **side fold**: carry the near side toward the far edge together, keeping
  the side straight between them, and lay it over the board so the crease runs along the near edge
  of the board from the collar end and continues straight past the right edge of the board to the
  hem, then release together.

The body of the garment stays on the table. Only the side being folded is carried over the board.

**Expected state:** a narrower shape with a straight crease along the near edge of the board running
the whole length of the garment, and the near sleeve lying over the board.

### Step 5: Fold the far side over the board

**Goal:** the far side folded in over the board, with the crease running along the far edge of the
board and continuing straight to the hem, parallel to the crease from Step 4.

* The **left gripper** closes on the **far sleeve** and the **right gripper** closes on the far side
  edge at the hem end, at the same time.
* Both grippers make the **side fold**: carry the far side toward the front edge together, keeping
  the edge straight between them, and lay it over the board so the crease runs along the far edge
  of the board from the collar end and continues straight past the right edge of the board to the
  hem, then release together.
* The **left gripper** and the **right gripper** fold the sleeves back on themselves so no part of
  either sleeve stands outside the board footprint, then release.

**Check:** the two creases run along the near and far edges of the board, continue straight to the
hem, and are parallel to each other, and neither sleeve stands outside the board footprint. If a
crease wanders off the board edge, open that fold, lay the layer flat, and fold it again.

### Step 6: Fold the tail

**Goal:** the tail doubled back on itself beyond the right edge of the board, with the hem lying
along the right edge of the board.

* The **left gripper** may take a **flat hold** on the middle of the board. This is optional.
* The **right gripper** pinches the middle of the **hem**, lifts it, carries it to the left over the
  body, and makes the **tail fold**: lays the hem down so it lies along the right edge of the board,
  then releases.
* The **right gripper** re-tucks either **hem corner** standing outside the board footprint width.

**Expected state:** the tail lies doubled beyond the right edge of the board, hem along the board's
right edge, the tail crease at the right end, and the tail no wider than the board.

### Step 7: Fold the hem half onto the upper part

**Goal:** a **packet** matching the board footprint with the board inside.

* The **left gripper** takes a **flat hold** on the middle of the board.
* The **right gripper** pinches the **tail crease** at the right end, lifts it, and makes the **half
  fold**: carries it to the left, up and over the right edge of the board, and lays it down on the
  board so the crease runs along the right edge of the board, then releases.
* The **left gripper** lifts clear as the incoming layer reaches it.
* Look along all four sides. The gripper on that side, the **left gripper** or the **right
  gripper**, re-tucks any sleeve, hem or corner standing outside the board footprint.

**Check:** the packet is a clean rectangle matching the board footprint, with the board inside, no
layer standing up, hanging loose or standing outside the board edge. If an edge stands proud, open
the last fold, lay the layer flat, and fold it again. A packet wider or longer than the board will
not go into the bag.

### Step 8: Flip the packet face up

**Goal:** the packet lying flat and face up in the working area, garment front and collar showing,
collar to the right, board still inside.

* The **right gripper** stays clear.
* The **left gripper** closes on the **collar end** of the packet, the left end, pinching through
  all the layers and the left edge of the board.
* The **left gripper** makes the **flip**: lifts the collar end and turns the packet up onto its
  other end, standing at 90 degrees, then on over toward the right, and lays it down flat and face
  up in one smooth motion, then releases. The goal of the turn is to bring the collar to the right
  side: after the flip the collar is on the right and the half-fold crease on the left.
* If a fold opens during the flip, the **left gripper** turns the packet back face down the same
  way, the open fold is made again, and the flip is made again.

**Warning:** The packet is turned over with the board inside. The board is never drawn out, and the
packet is never flung.

**Check:** the packet lies flat and face up, collar to the right, front of the garment showing, still
a clean rectangle matching the board footprint, and the board park is empty because the board is
inside the packet.

### Step 9: Bring the poly bag to the working area

**Goal:** the poly bag lying flat to the right of the packet, mouth facing left toward the packet's
collar end, ready to be picked up for bagging.

* With the **right gripper**, close on the **poly bag** on the bag start zone at the back, to the
  right of the board park, and **drag** it forward along the table to the working area. The **left
  gripper** stays clear.
* The **right gripper** lays the bag flat to the right of the packet, with the **bag mouth** facing
  left toward the collar end of the packet, the **bag flap** lying out flat and the seal strip up,
  then releases.

Nothing is set down on the flap. The bag is taken up again in Step 10.

**Check:** the bag lies flat to the right of the packet, mouth facing the collar end, flap out and
seal strip up, and the bag start zone at the back is empty.

### Step 10: Bag the packet

**Goal:** the whole packet inside the bag, collar end at the bottom of the bag, with the bag held
by the left gripper and the mouth clear of fabric.

#### 10.1 Take the packet up

* The **right gripper** may anchor the packet with a **flat hold** so it does not slide while it is
  taken. This is allowed, not required.
* The **left gripper** closes on the packet, pinching through all the layers and the board, with the
  collar still facing to the right, and lifts it clear of the table. The **right gripper** releases
  its hold on the packet.

#### 10.2 Feed the collar in

* The **right gripper** closes on the poly bag by its wall near the mouth and **holds the bag**, in
  the air or on the table, with the mouth open and facing the collar end of the packet.
* The **left gripper feeds in** the packet: brings the collar end to the mouth and pushes it in,
  collar first. The **right gripper** may let go and take the bag again at another place, and may
  push the bag onto the packet, to make the entrance easy.
* Stop once the collar has entered the bag and the packet and the bag are joined in part. They are
  now the **bunch**.

#### 10.3 Turn the bunch over

* The **left gripper** holds the packet together with the bag where they join. The **right
  gripper** releases the bag.
* The **left gripper turns the bunch**: turns the whole bunch over smoothly, in one motion, so the
  face of the garment now looks down, the bag is on the left and the packet is on the right.

#### 10.4 Push the packet through

* The **left gripper** pinches the upper part of the bag and holds it.
* The **right gripper pushes through** the rest of the packet: pushes it through the mouth into the
  bag until the whole packet is inside, then releases.
* Once the packet is securely inside, the **left gripper** lifts the bag by that hold and checks
  the packet is fully in. It may shake the bag so the packet settles at the bottom.
* The **left gripper** keeps that hold. Nothing is set down.

**Warning:** The packet is never dropped into the bag from above.

**Check:** the whole packet is inside the bag with no part of it standing proud of the mouth and no
fabric caught in the mouth, the collar end is at the bottom of the bag, and the **left gripper**
holds the bag.

### Step 11: Seal the bag and lay the pack down

**Goal:** a **sealed bag** lying flat in the working area with its collar end toward the back edge.

#### 11.1 Bend the flap down

* With the **left gripper** still holding the bag, the **right gripper** takes hold of the right
  side of the whole bunch.
* The **left gripper** then takes the **bag flap** on the left side and bends it down over the
  **bag mouth** toward the **bag wall**, so the **seal strip** meets the bag, and presses it.
* The **left gripper** and the **right gripper** may take turns: while one folds the flap down and
  presses it, the other holds the pack, until the bag is fully sealed along the whole flap.
* Confirm the flap lies flat on the bag wall over the mouth, with no bag film and no fabric trapped
  under it, and the strip has taken hold across the full width.

#### 11.2 Lay the pack down and turn it

* The **left gripper** and the **right gripper** lay the pack flat in the working area.
* Both grippers **turn the pack** on the table so its collar end is toward the back edge, away from
  the front edge, then release.

**Warning:** The bag is not sealed until the strip has taken hold across the full width. A flap bent
over but not pressed counts as unsealed.

**Check:** the flap lies flat on the bag wall over the mouth with nothing trapped under it, the seal
strip has taken hold across the full width, no corner is lifting, and the pack lies flat in the
working area with its collar end toward the back edge.

### Step 12: Stack the pack on the output stack

**Goal:** the **pack** lying flat on top of the **output stack** in the back-right corner, edges in
line with the pack below, collar end toward the back edge.

* The **right gripper** closes on the pack and **drags** it along the table, keeping it flat, to the
  output stack in the back-right corner, stopping beside the stack, then releases. The **left
  gripper** stays clear.
* The **right gripper** closes on the **front-right corner** of the pack and the **left gripper** on
  the **back-left corner**, both pinching bag, packet and board together.
* Both grippers **stack** the pack: lift it up together and lower it onto the top pack of the stack,
  so its edges line up with the pack below and its collar end is toward the back edge, then release
  together.
* If it lands overhanging or turned, the **left gripper** and the **right gripper** lift it clear
  and lay it again.

**Check:** the pack lies flat on top of the output stack, edges in line with the pack below, collar
end toward the back edge, and the working area is empty. No label is on it yet.

### Step 13: Apply the size label

**Goal:** one **size label** stuck flat on the top face of the pack on top of the output stack,
square to the pack and near its right edge, and the stack sitting square in the back-right corner.

Look where the label is before reaching for it.

* **IF the label is at the right-center (Config L and M):** with the **right gripper**, close on the
  **size label**, lift it straight up, and carry it level to the output stack. The **left gripper**
  stays clear.
* **IF the label is at the left-center (Config R):** with the **left gripper**, close on the **size
  label**, lift it straight up, and carry it level to the output stack. The **right gripper** stays
  clear.

Then, in all three:

* Land the label on the top face of the pack on top of the stack, square to the pack and near its
  right edge, not centered, and **apply** it: press it down over its whole area, then release.
* The **left gripper** and the **right gripper** may both be used to adjust the label and press it
  on.
* If a corner lifts, press it down again. Do not peel the label off to place it again, and do not
  add a second label.
* Once the label is on, the **right gripper drags** the stack into the back-right corner so it sits
  square in the corner, clear of the working area, then releases.

**Check:** one label lies flat on the top face of the pack, square to it, near its right edge, with
no corner lifting, the stack sits square in the back-right corner, and the label spot is empty.

### Step 14: Home the arms and end the episode

**Goal:** the finished pack on the output stack and both arms back at home.

* Confirm the pack lies sealed and labelled on top of the output stack in the back-right corner, the
  working area, the garment start zone, the board park, the bag start zone and the label spot are
  empty, and nothing lies loose on the table.
* Move both arms back to the home position with grippers open.
* End data collection.

## SOP violations

These are the things that break (violate) the SOP. This list feeds the violation set and is what
reviewers look for using the side-by-side review tool.

### How to record a violation in review

For each violation you spot in a recorded episode, record:

* The start timestamp of the violation in the video.
* The violation name from the list below.
* The SOP rule broken (the step number from the list below).

The visible cue is what you actually see in the video. The coaching note is for retraining after the
review; it is not what the annotator labels.

### Episode handling

Any SOP violation is flagged (or tagged) with the timestamp and violation name. Rather than being
discarded, the episode is retained in the training data and tagged with the violation. No flagged
episode is deleted. This matches the goal of capturing realistic variance in training.

### Violations

**Note on the start position:** the violations below were written for Config L (the garment starts
at the left-center, in front of the left gripper, and the label lies at the right-center). The
pickup and label cues will be rewritten later to cover all three configs; they are left as they are
for now. Until then, anything that does not match the episode's config goes under **Config
misaligned**.

**Violation: Config misaligned.**

* **Visible cue:** what the operator does does not match the config on the table: the garment or
  the label is not on the spot for the config; a gripper reaches across the table for the garment or
  the label; or the wrong IF line is followed.
* **SOP rule broken:** the start position and the same-side rule (the left gripper picks the
  garment in Config L and M, the right gripper in Config R; the right gripper takes the label from
  the right-center in Config L and M, the left gripper from the left-center in Config R; the IF line
  followed is the one for the config on the table).
* **Coaching note:** look where the garment and the label are before the first reach, then follow
  that config's IF lines in Steps 1 and 13.

**Violation: Wrong order.**

* **Visible cue:** the board goes on before the garment is squared, a fold is made before the board
  is on, the packet is flipped with a fold still unmade, the packet is fed into the bag before it is
  flipped, the flap is sealed before the packet is fully inside, the label goes on before the pack
  is on the stack, or the pack is laid down before the bag is sealed.
* **SOP rule broken:** Steps 2 to 13, the pack order (square, board on, near side, far side, tail,
  half fold, flip, bag, seal, stack, label).
* **Coaching note:** square, board on, near, far, tail, half, flip, bag, seal, stack, label. Finish
  the step you are in before you start the next one.

**Violation: Garment laid outside the working area.**

* **Visible cue:** the garment is laid down outside the working area, on the board park, on the bag
  start zone or on the label spot, and the episode goes on anyway.
* **SOP rule broken:** Step 1 (the left gripper lifts the garment, carries it, and lays it in the
  middle of the working area).
* **Coaching note:** lift the garment and carry it to the center before anything else.

**Violation: Garment not squared before the board goes on.**

* **Visible cue:** the board is lowered onto the garment while it is still rumpled, while it is face
  up, while its collar is not to the left, while a ridge runs across the body, while a sleeve lies
  under the body, or with a corner or edge still folded under itself.
* **SOP rule broken:** Step 2 (the garment is laid open and squared, flat, face down, collar to the
  left, sleeves out flat, no ridge, no tucked edge, before the board goes on).
* **Coaching note:** lay it open with both grippers, fold any tucked edge inward and then outward,
  and check the face before the board goes on. Every fold after this lands wrong otherwise.

**Violation: Face-up garment flung instead of draped.**

* **Visible cue:** a face-up garment is thrown or flicked over instead of being lifted at the far
  sleeve and the far side edge by both grippers and carried down toward the front edge in one smooth
  motion, or a rumpled garment is shaken or flung out instead of being lifted and laid open.
* **SOP rule broken:** Steps 2.1 and 2.2 (lay a rumpled garment open by lifting and laying it out;
  turn a face-up garment with a drape flip and never fling it).
* **Coaching note:** lift it, let it hang, lay it down. Nothing is flung.

**Violation: Board not squared.**

* **Visible cue:** the folding is started with the board still folded over on itself, sitting to
  one side so a side edge or sleeve does not stand outside it, with its left edge far inside or past
  the collar, or with the board turned across the garment.
* **SOP rule broken:** Step 3 (the left gripper lays the board on the collar half, unfolds it if it
  landed folded, and either gripper adjusts it until it lies open and square along the garment's
  length before the first fold).
* **Coaching note:** open the board out and aim it before the first fold: even fabric on both sides
  along the whole length, left edge at the collar.

**Violation: Folds made in the wrong order or the wrong direction.**

* **Visible cue:** the far side is folded before the near side, a side is carried the opposite way,
  the tail fold or the half fold is made before both side folds, the hem is carried to the right
  instead of to the left, the half fold is made before the tail fold, or the packet is flipped with
  a fold still unmade.
* **SOP rule broken:** Steps 4, 5, 6 and 7 (fold the near side toward the far edge first, then the
  far side toward the front edge, then the tail to the left so the hem lies along the right edge of
  the board, then the doubled tail to the left onto the board).
* **Coaching note:** near in, far in, tail back, half over. Four folds, always in that order, always
  over the board.

**Violation: Side fold made with one gripper.**

* **Visible cue:** the near side or the far side is carried over the board by one gripper only, with
  the other gripper clear or holding elsewhere, so the side lands slanted or the crease wanders off
  the board edge.
* **SOP rule broken:** Steps 4 and 5 (the left gripper at the sleeve and the right gripper at the
  hem end carry the side over the board together, keeping it straight, and release together).
* **Coaching note:** the side folds are two-gripper folds. Both ends move together so the crease
  lands straight along the board.

**Violation: Flat hold left under the fold.**

* **Visible cue:** the left gripper is still on the board when the half fold lands on top of it, so
  the layer lands over the gripper and has to be lifted again; or during the tail fold or the half
  fold no gripper holds the board and the board or the bottom layer drags along with the incoming
  hem.
* **SOP rule broken:** Steps 6 and 7 (the left gripper holds the board through the drag, in Step 6
  if it chooses and in Step 7 always, and lifts clear as the incoming layer reaches it).
* **Coaching note:** hold it down through the drag, then get out of the way just before it lands.

**Violation: Packet does not match the board footprint.**

* **Visible cue:** at the end of Step 7 a sleeve, a hem corner or a side stands outside the board
  edge, the hem has landed short of or past the right edge of the board in the tail fold, the half
  fold crease lands short of or past the right edge of the board, a layer stands up or hangs loose,
  or the packet is not a clean rectangle, and the packet is flipped anyway.
* **SOP rule broken:** Steps 4, 5, 6 and 7 (fold the sleeves back inside the footprint, lay the hem
  along the right edge of the board, land the half fold crease along the right edge of the board,
  and re-tuck anything standing outside the board edge before going on).
* **Coaching note:** walk all four sides before the flip. A packet wider or longer than the board
  will not go into the bag.

**Violation: Board drawn out of the packet.**

* **Visible cue:** the board is pulled, slid or lifted out from under or inside the folded layers at
  any point after the first fold, the packet is flipped, bagged or stacked without the board inside,
  or the board is laid back on the board park or anywhere else on the table during the episode.
* **SOP rule broken:** Steps 3 to 12 (the board stays inside the packet from the first fold to the
  output stack; it is never drawn out, and it goes into the bag with the garment).
* **Coaching note:** the board is part of the pack. It goes in the bag, not back on the park.

**Violation: Packet flipped wrong, or flung.**

* **Visible cue:** the packet is flipped with the right gripper, or with both grippers, it is
  thrown or flicked over instead of being lifted at its collar end and turned up and over in one
  smooth motion, it lands face down, on edge, bunched or with the collar not to the right, and the
  episode goes on; or a fold that opened during the flip is not made again.
* **SOP rule broken:** Step 8 (the left gripper closes on the collar end of the packet through all
  layers and the board, turns it up onto its other end and over toward the right so it lands flat
  and face up with its collar to the right; a fold that opens is made again and the flip is
  repeated).
* **Coaching note:** pinch the collar end through the board, stand it up, lay it over to the right.
  If a fold opened, turn it back and make the fold again.

**Violation: Bag brought wrong.**

* **Visible cue:** the bag is taken from the bag start zone with the left gripper, it is laid on the
  far side of the packet, on top of the packet, or with the mouth facing away from the collar end,
  or the bag is held by the left gripper while the collar goes in.
* **SOP rule broken:** Steps 9 and 10.2 (the right gripper drags the bag over and lays it to the
  right of the packet, mouth facing the collar end, then holds the bag while the left gripper feeds
  the collar in).
* **Coaching note:** the bag comes with the right gripper, mouth facing the collar, and the right
  gripper holds it while the collar goes in.

**Violation: Packet bagged wrong.**

* **Visible cue:** the packet is fed in half-fold crease first instead of collar first, the bunch is
  not turned over before the rest of the packet is pushed through, the packet is dropped or stuffed
  into the bag instead of fed and pushed, the right gripper releases with part of the packet still
  standing out of the mouth, fabric is caught in the mouth and the flap is sealed over it anyway, or
  the pack is set down before the bag is sealed.
* **SOP rule broken:** Steps 10.1 to 10.4 (the left gripper lifts the packet collar to the right,
  feeds the collar into the bag held by the right gripper, turns the bunch over face down, then holds
  the bag by its upper part while the right gripper pushes the rest through, and keeps that hold
  until the bag is sealed).
* **Coaching note:** collar in, turn the bunch, push the rest through, lift and check. It stays in
  hand until it is sealed.

**Violation: Flap not sealed.**

* **Visible cue:** the flap is left standing out, it is bent over but never pressed, it is sealed
  along part of its width only, bag film or fabric is trapped under it, or a corner is lifting and
  the pack is stacked anyway.
* **SOP rule broken:** Step 11.1 (the flap is bent down over the mouth onto the bag wall and pressed
  while the pack is held, the grippers taking turns holding and folding, until the strip has taken
  hold across the full width with nothing trapped under it).
* **Coaching note:** bend it down flat and press the whole width. Swap hands as often as you need,
  but do not put the pack down until it holds.

**Violation: Pack laid down the wrong way, or not stacked in line.**

* **Visible cue:** the pack is laid down with its collar end not toward the back edge and stacked
  that way, it is left in the working area, put down beside the output stack instead of on top of it,
  lifted onto the stack by one gripper only or not by its front-right and back-left corners, lowered
  onto the stack overhanging the pack below or turned across it, and the episode goes on; or a pack
  that landed out of line is left as it is.
* **SOP rule broken:** Steps 11.2 and 12 (both grippers lay the pack down and turn it collar end to
  the back; the right gripper drags it to the output stack; the right gripper at the front-right
  corner and the left gripper at the back-left corner lift it together onto the top pack with its
  edges in line; a pack that lands out of line is lifted and laid again).
* **Coaching note:** turn it collar to the back, drag it over, then two corners up and straight
  down onto the pack below. If it lands off, lift it and lay it again.

**Violation: Label missing, applied too early, or doubled.**

* **Visible cue:** the episode ends with no label on the pack, the label is applied while the pack
  is still in the working area or off the stack, it lands on the underside, off the pack, or
  centered instead of near the right edge, a corner is lifting, a placed label is peeled off and
  stuck down again, a second label is added, or the stack is left short of the back-right corner
  after the label is on.
* **SOP rule broken:** Step 13 (the label is taken by the gripper on its side once the pack is on
  the stack, landed on the top face near the right edge, pressed on, with both grippers free to
  adjust it; a lifting corner is pressed down again rather than peeled; then the right gripper
  drags the stack into the corner).
* **Coaching note:** stack first, then label: top face, near the right edge. A lifting corner gets
  pressed, not removed. Finish by pushing the stack into the corner.

**Violation: Wrong arm used for an action.**

* **Visible cue:** any step that specifies the left gripper or the right gripper is performed with
  the opposite gripper: the right gripper picks the garment from the left-center, carries the board,
  flips the packet, lifts the packet to feed it in, turns the bunch over or holds the bag while the
  rest is pushed through; or the left gripper folds the tail or the hem half, drags the bag, pushes
  the packet through, drags the pack or the stack, or takes the label from the right-center;
  or a step that calls for both grippers together (the side folds, the sleeve tuck, laying the pack
  down and turning it, lifting the pack onto the stack) is done with one.
* **SOP rule broken:** any step that specifies a gripper, including Steps 1, 3, 4, 5, 6, 7, 8, 9,
  10, 11, 12 and 13.
* **Coaching note:** confusion about left vs right roles. Walk through the SOP step by step at the
  station: the left gripper picks the garment, carries the board, flips, lifts and feeds the packet
  and holds the bag; the right gripper folds the tail and the half, drags the bag over, pushes the
  rest through, drags and labels; both grippers lay open, fold the sides, seal, lay down, turn and
  stack.

**Violation: Dropped.**

* **Visible cue:** the garment, the board, the packet, the bunch, the bag, the label or the pack
  falls to the table or the floor short of its spot, or a pack slides off the output stack.
* **SOP rule broken:** Steps 1 to 13 (keep hold of the bunch until the bag is sealed, and release
  only once the thing is resting where it belongs).
* **Coaching note:** keep one gripper on the bunch until the bag is sealed, and let go only once
  the thing is resting.

**Violation: Wrong episode ending.**

* **Visible cue:** the episode ends with the packet still unbagged, a bag unsealed or unlabelled,
  the pack still in the working area or beside the stack, the board on the board park or loose on
  the table instead of inside the pack, the stack out of the corner, an arm away from home, or an
  arm still over the working area or the output stack.
* **SOP rule broken:** Step 14 (confirm the sealed and labelled pack on top of the output stack in
  the back-right corner, the working area and all start zones empty; return both arms home with
  grippers open; then stop recording).
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

These are episode failures that are not caused by how the task was run and do not go in the
violation set. They are recorded as system issues, the episode is discarded/deleted, and the episode
does not become a coaching point.

* **Recording stopped or paused mid-episode:** Cause: software or hardware issue with the recording
  system.
* **Camera dropped frames or lost feed during the episode:** Cause: camera or capture system issue.
* **Hardware fault on the robot arm:** Cause: gripper malfunction, arm position drift, or motor
  error during the episode.
* **Defective garment:** Cause: a garment that arrives torn, stained, or so misshapen it cannot be
  squared. Replace before the next episode.
* **Defective poly bag:** Cause: a split seam, a mouth that will not stand open, a flap torn at the
  fold, or a seal strip that has lost its tack, been touched, or will not take hold under a correct
  press. Lay a fresh bag on the bag start zone before the next episode.
* **Defective label:** Cause: a label that has lost its tack and will not stay on the bag under a
  correct press, or one that has curled on the table so it cannot be taken flat. Replace before the
  next episode.
* **Packing board fault:** Cause: the board is cracked or creased so it will not open flat, it is
  too wide or too long to go into the bag with the packet, or a corner has crushed so the packet
  will not lie flat. Replace the board before the next episode.
* **Garment slides under a correct flat hold:** Cause: a dusty or slick table. Wipe the table
  before the next episode.
* **Output stack slides:** Cause: the packs under the new one are not square on each other, or the
  top pack is not flat, so the new pack cannot lie in line. Square the stack before the next
  episode.

### After each episode: repeat or reset

* **Batch sessions (e.g., 5x):** if fewer than the target number are packed, reset the workspace and
  return to Step 1 with the same garment, once the reset has laid it back in the start zone. Once
  the target number is packed, reset the workspace before the next session.
* Clear the working area and re-run the Setup checklist before the next session.

## After the episode: reset the workspace

This part is not recorded. It is just how you reset the table for the next episode.

* With recording off, take the newest pack off the top of the output stack, leaving the packs that
  were under it where they lie in the back-right corner.
* Peel the flap back, slide the packet out, and take the label off the bag. Open the packet's folds
  and take the board out.
* Check the garment for tears and stains; replace it if it is torn or stained. Check the board opens
  flat and is uncreased and uncrushed at the corners; replace it if it is not.
* Lay the board flat on the board park at the back-center, at the very back, long edges running left
  to right and clear so the left gripper can take it from above.
* Lay the garment in the garment start zone for the next episode's config, left-center (Config L),
  front-center (Config M), or right-center (Config R), as it comes. It does not need to be flat, face
  down or any particular way round; a rumpled garment is the start state.
* Discard the used bag and the used label.
* Lay a fresh poly bag flat on the bag start zone at the back, immediately to the right of the
  board, mouth facing left toward the board, flap lying out flat with its seal strip exposed, clean
  and facing up. Swap it out if the flap is torn at the fold or the strip has been touched or has
  lost its tack.
* Lay a fresh size label flat and face up on the label spot for the next episode's config,
  right-center (Config L and M) or left-center (Config R), peeled from its backing.
* Confirm the packs left on the output stack lie flat and square on each other in the back-right
  corner, collar ends toward the back edge, with the top one clear so the next pack can be lowered
  onto it.
* Wipe the working area.
* Confirm the table surface is clear of any objects other than the garment, the packing board, the
  poly bag, the size label and the output stack in their designated zones.
* Go through the Setup checklist again before starting the next episode.

**Warning:** The table must be clear except for the garment in its start zone, the packing board on
the board park at the back-center, the poly bag at the back to the right of the board, the size
label on its spot and the output stack in the back-right corner.

## Annotation subtasks

1. Move the garment from the start zone into the working area
2. Lay the garment open and check it is face down, collar to the left
3. Lay the packing board on the garment
4. Fold the near side over the board
5. Fold the far side over the board
6. Fold the tail
7. Fold the hem half onto the upper part
8. Flip the packet face up, collar to the right
9. Bring the poly bag to the working area
10. Bag the packet
11. Seal the bag and lay the pack down
12. Stack the pack on the output stack
13. Apply the size label
14. Home the arms and end the episode
