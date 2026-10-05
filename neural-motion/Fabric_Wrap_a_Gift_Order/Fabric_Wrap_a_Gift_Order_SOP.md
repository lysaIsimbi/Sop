# Fabric Wrap a Gift Order SOP (1x Episode: 1 Order)

One episode wraps **one** gift box in one fabric cloth. Everything starts inside the tray. The cloth is
spread as a diamond at the center, the box is set on it, the front and far corners are wrapped over
the box, the left and right corners are twisted into tails and tied in a square knot on top, one gift
card is tucked into the right side of the wrap, the bundle is set upright on the band so the band runs
under its right part, the band is wrapped around the right part of the box and stuck closed by its
sticky tip, and the finished bundle is pushed into the **staging lane**.

The order never changes: cloth, box, front wrap, pull the box closer, far half fold, far wrap, twist
both corners, first tie, mirrored second tie, card, band out, bundle onto the band, band wrap, push to
the staging lane. Each step reaches its expected state before the next one starts.

The left gripper leads the box. The right gripper leads the card and the band. The left gripper pulls
the box closer, makes the front wrap, twists the left corner, carries the bundle by its knot onto the
band, and folds up the band's front end. The right gripper twists the right corner, tucks the card,
brings the band in, and wraps the band's sticky far end over. The **cloth gripper** brings the cloth
in and the **push gripper** pushes the finished bundle; which gripper each one is depends on the
config. Spreading the cloth, lifting the box, the half fold, the far wrap, and the two ties are shared,
and each bullet says what each gripper does.

The tray is set up in one of twenty-four ways. Two things move: the **cloth start**, where the cloth
lies at the start, and the **staging lane**, where the finished bundle ends. Each config is named
cloth start first, then staging lane. The box always starts at the back-left of the tray and the band
always lies along the far edge.

* **Config LC-LC:** the cloth starts at the left-center. The bundle ends at the left-center.
* **Config LC-BL:** the cloth starts at the left-center. The bundle ends at the back-left corner.
* **Config LC-BC:** the cloth starts at the left-center. The bundle ends at the back-center.
* **Config LC-BR:** the cloth starts at the left-center. The bundle ends at the back-right corner.
* **Config FL-LC:** the cloth starts at the front-left corner. The bundle ends at the left-center.
* **Config FL-BL:** the cloth starts at the front-left corner. The bundle ends at the back-left
  corner.
* **Config FL-BC:** the cloth starts at the front-left corner. The bundle ends at the back-center.
* **Config FL-BR:** the cloth starts at the front-left corner. The bundle ends at the back-right
  corner.
* **Config FC-LC:** the cloth starts at the front-center. The bundle ends at the left-center.
* **Config FC-BL:** the cloth starts at the front-center. The bundle ends at the back-left corner.
* **Config FC-BC:** the cloth starts at the front-center. The bundle ends at the back-center.
* **Config FC-BR:** the cloth starts at the front-center. The bundle ends at the back-right corner.
* **Config FR-LC:** the cloth starts at the front-right corner. The bundle ends at the left-center.
* **Config FR-BL:** the cloth starts at the front-right corner. The bundle ends at the back-left
  corner.
* **Config FR-BC:** the cloth starts at the front-right corner. The bundle ends at the back-center.
* **Config FR-BR:** the cloth starts at the front-right corner. The bundle ends at the back-right
  corner.
* **Config RC-LC:** the cloth starts at the right-center. The bundle ends at the left-center.
* **Config RC-BL:** the cloth starts at the right-center. The bundle ends at the back-left corner.
* **Config RC-BC:** the cloth starts at the right-center. The bundle ends at the back-center.
* **Config RC-BR:** the cloth starts at the right-center. The bundle ends at the back-right corner.
* **Config BR-LC:** the cloth starts at the back-right corner. The bundle ends at the left-center.
* **Config BR-BL:** the cloth starts at the back-right corner. The bundle ends at the back-left
  corner.
* **Config BR-BC:** the cloth starts at the back-right corner. The bundle ends at the back-center.
* **Config BR-BR:** the cloth starts at the back-right corner. The bundle ends at the back-right
  corner.

In Config LC-LC and Config BR-BR the bundle ends in the same spot the cloth started in. The cloth
leaves that spot in Step 1, so it is bare again by Step 15. The same holds for anything else that
starts in the chosen lane: the box leaves the back-left in Step 3, the card leaves its spot in Step
11, and the band leaves the far edge in Step 12.

Where a step depends on the setup it says so on an **IF** line: look at the tray and follow the line
that matches.

What stays constant across all sessions:

* **One config per episode:** chosen and noted before recording and never changed mid-episode.
* **Rotation:** keep a list of the configs already recorded, and before each episode pick one that
  has been recorded the fewest times, so every config gets recorded.
* **Cloth gripper:** the left gripper when the cloth starts at the left-center, front-left, or
  front-center (the front-center is always given to the left arm), and the right gripper when it
  starts at the front-right, right-center, or back-right.
* **Card spot:** the card starts at the right-center. Only when the cloth starts at the right-center
  does the card start at the left-center instead, because the cloth takes its usual spot. The right
  gripper picks up the card either way.
* **Push gripper:** the right gripper for the left-center and back-right lanes, and the left gripper
  for the back-left and back-center lanes.
* **Fixed roles:** Steps 2 to 10 and Steps 12 to 14 are the same in all twenty-four configs.

## Setup

Choose and note the config first. Then complete both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole tray: the cloth at its cloth start, the box at the
   back-left, the card at its card spot, the band along the far edge, the center of the tray, and the
   staging lane.
3. The center of the tray is visible from above, so all four cloth corners, the knot on the top face,
   the card, and the band can all be seen.
4. Both arms are at home with grippers open.
5. The tray is clean and dry, and holds nothing but the cloth, the box, the card, and the band.
6. Each arm reaches its work without extending to a joint limit:
   * The cloth gripper reaches the cloth start.
   * The left arm reaches the box at the back-left and the center of the tray.
   * The right arm reaches the card at its card spot, the band, the center of the tray, and the right
     side of the box once it is at the center. When the cloth starts at the right-center, check that
     the right arm reaches the card at the left-center.
   * The push gripper reaches the bundle in the work area and the staging lane.

### Materials checklist

1. One **fabric cloth** (square) lies flat at the cloth start, unfolded, pattern side down. It is
   clean, dry, and not frayed at the corners.
2. One **gift box** sits at the back-left of the tray, top face up. It is closed, sound, and light
   enough for the two grippers to lift together: no crushed corner, no open flap.
3. One **gift card** lies flat at the right-center of the tray, uncreased. Only when the cloth starts
   at the right-center, the card lies at the left-center instead.
4. One **band** lies flat lengthwise along the far edge of the tray. It is sticky only at the tip of
   one end, and that tip still sticks.
5. The center of the tray is clear.
6. The staging lane needs no clearing at the start. Anything that starts there (the cloth, the box,
   the card, or the band) has left it before Step 15.

### Workspace layout

* **Cloth spot:** the cloth start for the config. The cloth lies here until Step 1.
* **Box spot:** back-left of the tray. The box sits here until Step 3.
* **Card spot:** right-center of the tray, or left-center when the cloth starts at the right-center.
  The card lies here until Step 11.
* **Band spot:** along the far edge of the tray. The band lies here until Step 12.
* **Work area:** the center of the tray. The cloth is spread and the whole wrap happens here.
* **Band area:** the part of the work area just right of the bundle, where the band is laid in Step
  12.
* **Staging lane:** left-center, back-left, back-center, or back-right of the tray, as the config
  says. The finished bundle ends here.

## Vocabulary

### Arm assignment

* **Left gripper:** pulls the box closer (when needed and after the front wrap), makes the front
  wrap, twists the left corner, carries the bundle by its knot onto the band, and folds the band's
  front end up.
* **Right gripper:** twists the right corner, tucks the card, brings the band to the work area, and
  wraps the band's sticky far end over.
* **Cloth gripper:** the gripper that brings the cloth to the work area in Step 1, set by the cloth
  start.
* **Push gripper:** the gripper that pushes the finished bundle into the staging lane in Step 15,
  set by the staging lane.
* **Shared moments:** spreading the cloth (Step 2), lifting the box onto the cloth (Step 3),
  adjustments after the front wrap (Step 4), the half fold (Step 6), the far wrap (Step 7), both ties
  (Steps 9 and 10), and holding the band in its fold (Step 14).

### Positions

* **Front** is the near edge of the tray. **Back** is the far edge.
* **Left** and **right** are the sides of the left arm and the right arm.
* **Center** is the middle of that edge or side: the **left-center** is the middle of the left side,
  the **back-center** is the middle of the far edge.
* **Front-left**, **front-right**, **back-left**, and **back-right** are the corners of the tray.

### Cloth and box

* **Box:** the closed gift box. Its **top face** points up for the whole episode. Its **right side**
  is the face toward the right arm while it sits in the work area, and its **right part** is the end
  of the box nearest that face.
* **Diamond:** the cloth spread with one corner pointing to each edge of the tray: the **front
  corner** toward the near edge, the **far corner** toward the far edge, the **left corner** and the
  **right corner** toward the sides. The box on it stays square to the tray.
* **Flat:** the cloth shows no ridge, fold line, or bunched patch when looked at across the tray.
* **Front wrap:** the front corner laid up and over the box onto the top face.
* **Half fold:** the far corner's tip folded back on top of the far corner itself, so the fold sits
  about halfway along the corner and the corner ends in a straight folded edge instead of a point.
* **Far wrap:** the half-folded far corner laid up and over the box, on top of the front wrap.
* **Twist cycle:** one grasp of a side corner, one twist made by circling the held corner toward the
  back and toward the front, and one release.
* **Tail:** a side corner after twisting, gathered into a rope-like length that is easy to grasp.
* **Tie:** one full cross-and-pull-through of the two tails, pulled tight (Step 9).
* **Mirrored tie:** a tie made with the crossing the other way round from the tie before it: if the
  first tie crosses right over left, the mirrored tie crosses left over right (Step 10).
* **Square knot:** a tie followed by its mirrored tie. It lies flat on the top face and holds. Two
  ties crossed the same way round make a granny knot, which is not a square knot.
* **Bundle:** the box once the cloth is knotted around it.

### Card and band

* **Gift card:** one flat card, tucked into the right side of the wrap.
* **Exposed opening:** a gap on the right side of the bundle where a fold of the cloth stands open
  from the box or from the layer under it.
* **Band:** one flat strip that belts the right part of the bundle. Only the tip of one end is sticky.
* **Sticky tip:** the sticky tip at one end of the band.
* **Front end / far end of the band:** the band's two ends once it lies front to back in the band
  area. The far end is always the end with the sticky tip.

### Handling standard

* One cloth, one box, one card, and one band per episode.
* The box and the bundle are lifted, not dragged, except the slides the SOP calls for: the box pulled
  closer in Step 3 (only if needed) and Step 5, and the push to the staging lane in Step 15.
* Adjustments may be made by either gripper wherever a step says "adjust". Adjustments never undo a
  finished step.

## Steps

Run Steps 1 to 15 in order. Only Steps 1, 11, and 15 depend on the config: Step 1 by the cloth start,
Step 11 by the card spot, and Step 15 by the staging lane. The only other conditional is in Step 3.
Every other line is the same in all twenty-four configs.

### Step 1: Bring the cloth to the center

**Goal:** the cloth lies in the work area at the center of the tray.

Look where the cloth is before reaching for it.

* **IF the cloth starts at the left-center, front-left, or front-center:** the **left gripper** is the
  cloth gripper. The right gripper does not touch the cloth in this step.
* **IF the cloth starts at the front-right, right-center, or back-right:** the **right gripper** is
  the cloth gripper. The left gripper does not touch the cloth in this step.

Then:

* The **cloth gripper** pinches the cloth at its corner nearest the center of the tray.
* The **cloth gripper** slides the cloth toward the center until the cloth's middle is at the center
  of the tray, and releases.

**Check:** the middle of the cloth sits roughly at the center of the tray. If it is clearly off, the
**cloth gripper** pinches the same corner and moves it again.

**Expected state:** the cloth lies at the center of the tray, not yet spread. The cloth spot is empty.

### Step 2: Spread the cloth as a diamond

**Goal:** the cloth lies flat as a **diamond** at the center of the tray, with room for the box in the
middle.

* The **left gripper** pinches the left corner and the **right gripper** pinches the right corner.
* Both grippers pull their corners apart and outward until the cloth is flat between them, then turn
  the cloth together until one corner points to each edge of the tray, and release.
* Either gripper pinches the front corner or the far corner and pulls it straight out to take out any
  fold that remains.

**Check:** the cloth is **flat**, its four corners point to the front, far, left, and right edges of
the tray, and the bare middle of the cloth is larger than the box's bottom face on every side. If a
corner is folded under or the cloth is turned, the grippers pinch the out-of-place corner and pull it
out again.

**Expected state:** a flat cloth diamond lies at the center of the tray.

### Step 3: Set the box on the center of the cloth

**Goal:** the box sits top face up in the middle of the cloth, square to the tray.

Look at where the box is before reaching for it.

* **IF the right gripper cannot reach the box's right side at the box spot:** the **left gripper**
  closes on the box's far face, at its middle, and pulls the box toward the center of the tray until
  the right gripper can reach its right side. Then it releases.
* **IF the right gripper can already reach the box's right side:** skip the pull.

Then:

* The **left gripper** closes on the middle of the box's left side and the **right gripper** closes on
  the middle of its right side.
* Both grippers lift the box straight up until it clears the tray, carry it level over the middle of
  the cloth, and lower it until it rests there, top face up, its edges square to the tray edges.
* Both grippers release and lift clear.

**Check:** the box is roughly centered on the cloth, and the four cloth corners stick out past the box
by about the same length. If not, both grippers lift the box and set it down again.

**Expected state:** the box sits in the middle of the cloth diamond. The box spot is empty.

### Step 4: Front wrap

**Goal:** the front corner lies over the box, flat on the top face.

* The **left gripper** pinches the front corner at its tip.
* The **left gripper** lifts it up and over the front face of the box, lays it on the top face, and
  releases.
* Either or both grippers adjust the **front wrap** until it lies flat against the front face and the
  top face.

**Check:** the front face of the box is covered and the front wrap lies on the top face without
springing back. If it springs back, the **left gripper** pinches the tip and lays it again.

**Expected state:** the front wrap lies on the top face. The far, left, and right corners still lie on
the tray.

### Step 5: Pull the box closer

**Goal:** the wrapped box sits closer to the front edge, comfortably within reach of both arms.

* The **left gripper** closes on the box, over the front wrap, at the middle of the box's left side.
* The **left gripper** slides the box and the cloth together toward the front edge until the box is
  comfortably within reach of both arms, and releases.

The front wrap stays on the top face the whole time.

**Check:** both grippers can reach the far corner, the front wrap is still in place, and the cloth has
moved with the box, not out from under it. If the wrap has come off, go back to Step 4.

### Step 6: Half fold the far corner

**Goal:** the far corner is folded in half on itself, ending in a straight folded edge.

* The **right gripper** pinches the far corner at its tip.
* The **right gripper** lifts the tip and lays it back onto the far corner, toward the box, so the tip
  meets the far corner near the box's far bottom edge. The tip lies on top of the far corner, not
  tucked under it.
* The **left gripper** presses the fold flat along its folded edge.
* Either or both grippers adjust until the **half fold** lies flat with a straight folded edge.

**Check:** the fold sits about halfway along the far corner and the corner ends in one straight folded
edge. If it is bunched or folded crooked, the **right gripper** opens it out and folds it again.

**Expected state:** the half-folded far corner lies flat on the tray behind the box.

### Step 7: Far wrap

**Goal:** the half-folded far corner lies over the box, on top of the front wrap.

* The **left gripper** pinches the left end of the folded edge and the **right gripper** pinches its
  right end.
* Both grippers lift the far side up and over the far face of the box together, lay it on the top
  face on top of the front wrap, and release.
* Either or both grippers adjust the **far wrap** until it lies flat.

**Check:** no box face shows at the front or the far side, and the far wrap lies on top of the front
wrap. If a face shows or the far wrap is under the front wrap, both grippers lift the far wrap and lay
it again.

**Expected state:** the front and far faces are covered. Only the left and right corners lie out on
the tray.

### Step 8: Twist the side corners into tails

**Goal:** each side corner is twisted into a **tail** that is easy to grasp and tie.

* The **left gripper** closes on the left corner near its tip, twists it by circling the held corner
  toward the back and toward the front, and releases.
* The **left gripper** repeats the **twist cycle** (grasp, circle back and front, release), each time
  closing a little closer to the box, until the left corner has gathered into a tail.
* Then the **right gripper** does the same on the right corner, until it has gathered into a tail.

The front and far wraps stay on the top face the whole time.

**Check:** each tail is a single rope-like length with no flat sheet of cloth left at the side of the
box, and each is long enough to lift over the box and tie. If a tail untwists or stays flat, the
gripper on that side runs more twist cycles.

**Expected state:** two tails lie out from the left and right sides of the box.

### Step 9: First tie

**Goal:** the two tails are crossed right over left, passed through each other, and pulled tight on
the top face.

#### 9.1 Bring the tails up

* The **left gripper** closes on the left tail and the **right gripper** closes on the right tail.
* Both grippers lift their tails up and around, over the top of the box.

#### 9.2 Cross the tails

* The **right gripper** releases the right tail and closes on the left tail, next to the left gripper.
* The **left gripper** releases the left tail and closes on the right tail.
* The tails now cross over the middle of the top face right over left: the right tail lies on top.

#### 9.3 Pull one tail through

* The **right gripper** takes both tails where they cross and holds them together.
* The **left gripper** goes under the crossing, closes on the end of the lower tail, and pulls it up
  through the loop.

#### 9.4 Pull tight

* Once both ends are exposed and have passed over and through each other, the **left gripper** closes
  on the end on the left and the **right gripper** closes on the end on the right.
* Both grippers pull their ends apart, left and right, until the **tie** seats on the top face.

Pull the tie tight by pulling the two ends apart, never by dragging the bundle across the tray.

**Check:** one tie sits roughly in the middle of the top face, and the cloth is snug on the left and
right faces. If the tie slips open, the grippers undo it and run Step 9 again.

### Step 10: Second tie (mirrored) to make a square knot

**Goal:** a **mirrored tie** sits on the first tie, so the two together form a **square knot** that
lies flat and holds.

* Run Steps 9.1 to 9.4 again with the two ends coming out of the first tie, with one change in 9.2:
  cross the ends left over right, so the left end lies on top. This is the mirror of the first tie.
* Every other move is the same as in Step 9: the **right gripper** holds both ends at the crossing,
  the **left gripper** goes under and pulls the lower end through, and both grippers pull their ends
  apart.

**Check:** the knot is a square knot: it lies flat on the top face, the two ends come out of it side
by side, and it does not slip when both grippers let go. If it stands on end, twists, or slips (a sign
both ties were crossed the same way round), the grippers undo the second tie and tie it again
mirrored.

**Expected state:** the bundle sits in the work area, fully covered, with a square knot on the top
face.

### Step 11: Tuck the gift card

**Goal:** the gift card is held in an **exposed opening** on the right side of the bundle.

* **IF the cloth started at the right-center:** the card is at the left-center. The **right gripper**
  (not the left) reaches to the left-center and picks the **gift card** off it by one short edge.
* **IF the cloth started anywhere else:** the card is at the right-center. The **right gripper** picks
  the **gift card** off it by one short edge.

Then:

* The **right gripper** carries it to the right side of the bundle and slides the free end well into
  an exposed opening of the cloth there, so the cloth holds it, then releases.

The **left gripper** may hold the bundle still at its left side while the card goes in. One card only.

**Check:** the card stays in the opening when the **right gripper** opens and the knot is still tight.
If the card falls out, the **right gripper** picks it up and tucks it again.

**Expected state:** the card sticks out of the right side of the bundle. The card spot is empty.

### Step 12: Bring the band to the work area

**Goal:** the band lies flat and front to back in the band area, with its sticky tip at the far end.

* The **right gripper** pinches the **band** at its middle at the band spot.
* The **right gripper** carries the band to the band area, just right of the bundle, and lays it down
  flat, running front to back, with the **sticky tip** at the far end.
* The **right gripper** may smooth the band flat. This is optional.

**Check:** the band lies flat and front to back in the band area, with the sticky tip at the far end,
and clear of the bundle. If the sticky tip is at the front end, the **right gripper** turns the band
end for end.

### Step 13: Set the bundle on the band

**Goal:** the bundle stands upright on the band, with the band running under its right part.

* The **left gripper** closes around the knot.
* The **left gripper** lifts the bundle clear of the tray, keeping it upright (knot up), carries it
  over the band, and lowers it until it rests with the band running front to back under the bundle's
  right part. Then it releases.

The bundle is not tipped or turned onto a side. The right gripper does not carry the bundle.

**Check:** the bundle stands upright, knot up, the band runs under its right part, and both band ends
stick out past the front and far faces. The card is still in the wrap. If the band is under the middle
or the left part, or the bundle has tipped, the **left gripper** lifts it by the knot and sets it down
again.

**Expected state:** the bundle stands upright on the band, which runs under its right part.

### Step 14: Wrap the band around the right part of the box

**Goal:** the band belts the right part of the bundle and holds itself closed by its sticky tip.

* The **left gripper** pinches the front end of the band, lifts it, and folds it up and around the
  front face of the bundle's right part onto the top face.
* The **right gripper** presses the front end against the top face to hold it in the fold.
* The **right gripper** then pinches the far end of the band, lifts it up and around the far face of
  the bundle's right part, and lays it over the front end on the top face.
* The **right gripper** presses the sticky tip down onto the band until it sticks. Either or both
  grippers may adjust the band first so it lies snug.

**Check:** the band runs around the right part of the bundle with no gap, the far end overlaps the
front end on the top face, the sticky tip holds when both grippers let go, and the card is still in
the wrap. If the tip lifts, the **right gripper** presses it down again.

**Expected state:** the banded bundle stands upright in the work area.

### Step 15: Push the bundle into the staging lane and end the episode

**Goal:** the finished bundle sits upright in the staging lane and both arms are home.

The bundle is pushed from where it was banded. Look which lane the config names before the push.

* **IF the lane is the left-center:** the **right gripper** is the push gripper. It closes and pushes
  the bundle at its right side, to the left, until it reaches the left-center of the tray.
* **IF the lane is the back-left:** the **left gripper** is the push gripper. It closes and pushes the
  bundle at its front face, back and to the left, until it reaches the back-left corner of the tray.
* **IF the lane is the back-center:** the **left gripper** is the push gripper. It closes and pushes
  the bundle at its front face, straight back, until it reaches the middle of the far edge.
* **IF the lane is the back-right:** the **right gripper** is the push gripper. It closes and pushes
  the bundle at its front face, back and to the right, until it reaches the back-right corner of the
  tray.

Then:

* The **push gripper** stays low on the body and clear of the knot, the card, the band, and the sticky
  tip. It pushes until the whole bundle is in the staging lane, then lifts clear. The other gripper
  does not touch the bundle.
* Look over the bundle: covered, square knot tied, card in, band closed.
* Return both arms home with grippers open, then stop recording.

**Check:** the bundle sits upright in the staging lane with the band closed. If it has tipped or the
band has opened, fix it before homing.

## After the episode: reset the workspace

This reset is not recorded.

1. Take the band off the bundle. Keep it for reuse only if its sticky tip still holds. Otherwise, use
   a new band.
2. Take the card out, undo the square knot, and unwrap the cloth from the box.
3. Choose and note the next episode's config, picking one that has been recorded the fewest times.
4. Lay the cloth flat and unfolded at the cloth start for that config, pattern side down.
5. Set the box at the back-left of the tray, top face up. The box goes here in every config.
6. Lay the card flat at the right-center of the tray. If the cloth now lies at the right-center, lay
   the card at the left-center instead.
7. Lay the band flat and lengthwise along the far edge of the tray. The band goes here in every
   config. The staging lane needs no clearing.
8. Replace a cloth that is stained, torn, or frayed, a box that is crushed or will not stay closed, a
   card that is bent or torn, and a band whose tip no longer sticks.
9. Run both Setup checklists again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The
visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation
label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not
delete it just because a rule was broken.

### Violations

**Violation: Work done out of order**

* **Visible cue:** a step starts before the one before it has reached its expected state, for example
  the box goes on before the cloth is a diamond, the far corner is wrapped before the front corner,
  the tails are tied before both are twisted, the card goes in before the square knot, or the bundle
  goes onto the band before the card is in.
* **SOP rule broken:** Steps 1 to 15 run in order, each ending in its expected state before the next.
* **Coaching note:** cloth, box, front, pull, half fold, far, twist, tie, mirrored tie, card, band,
  push.

**Violation: Config changed mid-episode**

* **Visible cue:** the episode does not follow the config noted before recording: the cloth, the card,
  or the planned staging lane is moved to a different spot during the episode, or the episode's IF
  lines switch from one config to another partway through.
* **SOP rule broken:** one config per episode, chosen and noted before recording and kept for the
  whole episode.
* **Coaching note:** note the config before you press record. Stick to it to the end.

**Violation: Wrong gripper for the cloth or the lane**

* **Visible cue:** the cloth is brought to the center by the gripper not named for its cloth start,
  the other gripper helps with it in Step 1, the bundle is pushed by the gripper not named for the
  staging lane, or the other gripper helps with the push.
* **SOP rule broken:** Steps 1 and 15, the left gripper brings the cloth from the left-center,
  front-left, or front-center and the right gripper from the front-right, right-center, or back-right;
  the right gripper pushes to the left-center or back-right and the left gripper to the back-left or
  back-center.
* **Coaching note:** check the noted cloth start before the first reach and the noted lane before the
  push.

**Violation: Step skipped**

* **Visible cue:** a step is left out: no pull after the front wrap, no half fold, only one corner
  twisted, only one tie, no card, no band, or no push to the staging lane.
* **SOP rule broken:** Steps 1 to 15, every step is run.
* **Coaching note:** check the expected state before moving on. If a step was missed, go back and do
  it.

**Violation: Cloth brought in wrong**

* **Visible cue:** the cloth is left clearly off the center of the tray before spreading starts.
* **SOP rule broken:** Step 1, the cloth's middle is brought to the center of the tray.
* **Coaching note:** center it before spreading.

**Violation: Cloth not spread as a diamond**

* **Visible cue:** the box goes on while the cloth is square to the tray, visibly turned so its
  corners do not point to the tray edges, folded or bunched, or with too little bare cloth in the
  middle for the box.
* **SOP rule broken:** Step 2, both grippers spread the cloth flat as a diamond with room for the box.
* **Coaching note:** corners to the four edges, flat, before the box moves.

**Violation: Box brought in wrong**

* **Visible cue:** the box is carried by one gripper; it is dragged onto the cloth instead of lifted;
  the right gripper does the pull closer; the box is pulled when the right gripper could already
  reach it; or it is set down clearly off center, turned, or top face down.
* **SOP rule broken:** Step 3, the left gripper pulls the box closer only if needed, then both
  grippers lift it by its left and right sides and set it top face up and square in the middle of the
  cloth.
* **Coaching note:** pull only if the right hand can't reach. Lift with both, center it, square it.

**Violation: Front wrap wrong**

* **Visible cue:** the right gripper makes the front wrap, the front wrap is made by any corner other
  than the front corner, or it is left springing back off the top face.
* **SOP rule broken:** Step 4, the left gripper takes the front corner by its tip and lays it over the
  box onto the top face.
* **Coaching note:** left hand, front tip, over the top.

**Violation: Box not pulled closer**

* **Visible cue:** the far corner is worked without the box being pulled toward the front edge first,
  the right gripper does the pull, or the pull drags the box out of the cloth or knocks off the front
  wrap.
* **SOP rule broken:** Step 5, after the front wrap the left gripper slides the box and cloth together
  toward the front edge until the box is comfortably within reach of both arms.
* **Coaching note:** pull the whole wrap together, cloth with the box.

**Violation: Half fold missing or wrong**

* **Visible cue:** the far corner is wrapped over as a point with no half fold, the tip is folded
  under instead of on top, or the fold is left bunched or crooked when the far wrap starts.
* **SOP rule broken:** Step 6, the far corner's tip is folded back on top of the far corner into a
  straight folded edge before the far wrap.
* **Coaching note:** fold the tip back first. A straight edge wraps clean.

**Violation: Far wrap wrong**

* **Visible cue:** the far side is lifted by one gripper, it goes under the front wrap, or a box face
  still shows at the front or the far side when twisting starts.
* **SOP rule broken:** Step 7, both grippers lift the far side by the ends of its folded edge and lay
  it over the box on top of the front wrap.
* **Coaching note:** both hands on the folded edge, over the top, on the front wrap.

**Violation: Corner not twisted into a tail**

* **Visible cue:** a side corner is tied as a flat sheet; it is twisted in one grasp with no
  release-and-regrasp cycles; the twist is not made by circling the corner toward the back and front;
  the left corner is twisted by the right gripper or the right corner by the left gripper; or both
  corners are twisted at the same time.
* **SOP rule broken:** Step 8, the left gripper twists the left corner, then the right gripper twists
  the right corner, each by repeated cycles of grasp, circle back and front, release, until it forms a
  tail.
* **Coaching note:** grasp, circle back and front, release, repeat, until it's a rope.

**Violation: Tie sequence wrong**

* **Visible cue:** the tails are not brought up over the box before crossing; the grippers do not swap
  tails; a gripper releases a tail before the other gripper has closed on it; the left gripper holds
  both tails while the right pulls through; or the ends are pulled in the same direction.
* **SOP rule broken:** Steps 9 and 10, bring the tails up, swap them so they cross, the right gripper
  holds both while the left gripper pulls one through, then both pull apart in opposite directions.
* **Coaching note:** up, swap, right holds, left pulls through, pull apart.

**Violation: Knot not square or loose**

* **Visible cue:** only one tie is made; the second tie is crossed the same way round as the first
  (right over left twice, or left over right twice), giving a granny knot that stands on end or
  twists; the knot sits clearly off the middle of the top face; the knot slips when the grippers let
  go; or a tie is tightened by dragging the bundle.
* **SOP rule broken:** Steps 9 and 10, the first tie crosses right over left and the second tie is its
  mirror, crossing left over right, so the two form a square knot; each tie is pulled tight by pulling
  the ends apart, on the middle of the top face.
* **Coaching note:** right over left, then left over right. Same way twice slips.

**Violation: Card tucked wrong**

* **Visible cue:** the left gripper tucks the card; the card goes anywhere but the right side of the
  bundle; it is laid loose on the bundle instead of tucked into an opening; it falls out when the
  gripper opens; or more than one card is used.
* **SOP rule broken:** Step 11, the right gripper tucks one card into an exposed opening on the right
  side of the bundle.
* **Coaching note:** right hand, right side, into the opening, check it holds before letting go.

**Violation: Band laid out wrong**

* **Visible cue:** the left gripper brings the band in; the band is laid across the tray instead of
  front to back, not next to the bundle, or with the sticky tip at the front end; or the bundle is set
  on the band before the band is laid out.
* **SOP rule broken:** Step 12, the right gripper lays the band flat, front to back, just right of the
  bundle, with the sticky tip at the far end.
* **Coaching note:** flat, front to back, sticky tip to the far end, right next to the bundle.

**Violation: Bundle set on the band wrong**

* **Visible cue:** the bundle is lifted by anything other than the knot; the right gripper carries it;
  it is dragged or rolled onto the band; it is tipped or turned onto a side; or the band ends up under
  the middle or the left part of the bundle instead of its right part.
* **SOP rule broken:** Step 13, the left gripper lifts the bundle by the knot and sets it down upright
  with the band running under its right part.
* **Coaching note:** grip the knot, keep it upright, band under the right part.

**Violation: Band wrapped wrong**

* **Visible cue:** the far end is wrapped before the front end; the right gripper folds the front end
  up; the band is wrapped around the middle or the left part of the bundle; the far end does not
  overlap the front end; the sticky tip is not pressed down; the band pulls the card out of the wrap;
  or the episode moves on with the band open.
* **SOP rule broken:** Step 14, the left gripper folds the front end up around the right part with the
  right gripper holding it, then the right gripper laps the sticky far end over it and presses the
  sticky tip until it sticks.
* **Coaching note:** front end first, hold it, far end over, press the tip.

**Violation: Bundle not in the chosen lane**

* **Visible cue:** the bundle is lifted and carried instead of pushed; it is pushed at the wrong face
  (not the right side for the left-center lane, not the front face for a back lane); the push catches
  the knot, the card, the band, or the sticky tip; the bundle tips over; or it is left anywhere but
  fully in the staging lane the config names.
* **SOP rule broken:** Step 15, the push gripper pushes the upright bundle from where it was banded
  into the staging lane.
* **Coaching note:** push low on the body, all the way into the lane you noted.

**Violation: Dropped, collided, or knocked something over**

* **Visible cue:** the box, the card, the band, or the bundle falls short of its spot or off the tray,
  the box is knocked off the cloth, or the two arms strike each other, with no hardware fault visible.
* **SOP rule broken:** Steps 1 to 15, keep each thing on a clear path and release only after it rests.
* **Coaching note:** check the path and the landing spot before you move.

**Violation: Manipulation outside the camera frame**

* **Visible cue:** the wrap, a tie, the card tuck, or the band wrap happens partly or wholly outside
  the environment camera frame.
* **SOP rule broken:** Steps 1 to 15, every manipulation happens inside the camera frame, in the tray.
* **Coaching note:** keep the work at the center of the tray.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with a box face showing, a loose knot or one that is not square,
  no card, the band open, the bundle tipped or outside the staging lane, an arm away from home, or a
  gripper not fully open.
* **SOP rule broken:** Step 15, look over the finished bundle in the staging lane, then return both
  arms home with grippers open and stop recording.
* **Coaching note:** look first. Homing is the last thing the arms do.

### Non-violation failures

These failures are not caused by how the task was run. Log them as system issues, discard the
episode, and never use them for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Defective object:** a torn or frayed cloth, a crushed box, a bent card, or a band whose tip will
  not stick. Replace it before the next episode.
* **Wrong setup at episode start:** an item is missing, extra, or not at its start spot for the
  config. Reset error, not a violation.

## Annotation subtasks (from SOP)

1. Bring the cloth to the center with the cloth gripper
2. Spread the cloth flat as a diamond
3. Pull the box closer with the left gripper (only if needed)
4. Lift the box with both grippers and set it on the center of the cloth
5. Wrap the front corner over the box with the left gripper
6. Pull the box closer with the left gripper
7. Half fold the far corner
8. Wrap the far side over the box with both grippers
9. Twist the left corner into a tail
10. Twist the right corner into a tail
11. Bring both tails up over the box
12. Swap the tails so they cross right over left
13. Pull one tail through and pull the first tie tight
14. Tie the mirrored second tie, left over right, into a square knot
15. Pick the gift card from its card spot and tuck it into the right side of the bundle
16. Bring the band to the work area, sticky tip to the far end
17. Lift the bundle by the knot and set it upright with the band under its right part
18. Fold the band's front end up around the right part of the bundle
19. Wrap the band's far end over and press the sticky tip down
20. Push the bundle into the staging lane with the push gripper
21. Return both arms home and end the episode
