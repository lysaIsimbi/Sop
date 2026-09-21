# Assemble a Gasketed Enclosure SOP (1x Episode: 1 Enclosure)

One episode closes one enclosure. The table begins with the **enclosure body** clamped in its **holding
fixture** on the assembly spot, just right of the center of the table. The body is open on top. A **groove**
runs all the way around its top rim, and a **screw post** stands at each of the four corners of the rim. The
groove starts empty. Four **screws**, one **lid**, and one **torque driver** are staged on the right. One
**gasket** lies in its **gasket tray** in the start zone for the episode's config. One **label sheet** lies flat
just left of center.

The order never changes: lay the gasket into the groove, press it home all the way round, lower the lid on,
start all four corner screws by hand, torque them in the cross pattern **1 → 3 → 2 → 4**, then put the label
on the front face. The lid does not go on until the gasket is seated all the way round. No screw is torqued
until all four screws are started. The label does not go on until all four screws have clicked.

The right gripper does the work: it lays and seats the gasket, carries the lid, starts each screw, holds the
torque driver, and puts the label on. The left gripper supports: it presses the gasket down on the left run of
the groove, holds the lid flat on the body while the screws are started, squares the driver, and pins the
label sheet for the peel. The left gripper works the left side of the body, the label sheet, and (Config L and
M) the gasket tray only, and never reaches across the body.

The table is set up in one of three ways. Only the gasket tray moves; the body in its fixture, the screw tray,
the lid stand, the driver cradle, and the label sheet are in the same place in all three.

* **Config L:** the gasket tray is at the back-left.
* **Config M:** the gasket tray is at the front-center, in front of the label sheet.
* **Config R:** the gasket tray is at the front-right, left of the screw tray.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line that
matches.

What stays constant across all sessions:

* **Start position:** the gasket tray stands at the back-left (**Config L**), the front-center (**Config M**)
  or the front-right (**Config R**). One config per episode, chosen before recording and never changed
  mid-episode.
* **Same-side rule:** the gripper on the gasket tray's side lifts the gasket — the left gripper in Config L
  and M, the right gripper in Config R. No arm reaches across the table.
* **Hand-over rule:** in Config L and M the left gripper never reaches across the body, so it **hands the
  gasket over** to the right gripper above the body: the left gripper holds the gasket still, the right
  gripper closes on the opposite side of the loop, and only then does the left gripper open. The right
  gripper lays the gasket in. Nothing is handed over in Config R.
* **Fixed roles:** the body stays clamped on the assembly spot, and the right gripper lays and seats the
  gasket, carries the lid, starts and torques the screws, and puts the label on in every config.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the whole table: the enclosure body in its fixture, all four screw posts, the
   body's front face, the gasket tray in the start zone for this episode's config, the right supply zone, and
   the label sheet.
3. The body is visible from above, so the whole groove, all four posts, and the top of the rim can be seen.
4. Both arms are at home with grippers open.
5. The table is bare apart from the fixture, the gasket tray, the right supply zone, the label sheet, and robot
   hardware.
6. The right arm reaches the screw tray, the lid stand, the driver cradle, all four posts, the body's front
   face, and (Config R) the gasket tray without stretching. The left arm reaches the left side of the body's
   rim, the left edge of the lid, the label sheet, and (Config L and M) the gasket tray without stretching.

### Materials checklist

1. One **enclosure body** is clamped in the **holding fixture** on the **assembly spot**, just right of the
   center of the table, square to the front edge. It does not move when a gripper presses on it.
2. The body's **groove** is empty, clean, and dry all the way round. The **rim land** beside it is clean.
3. Four **screw posts** stand at the four corners of the rim, each with a clean, empty tapped hole.
4. One **gasket** lies flat in the **gasket tray**, untwisted, with its painted **line** facing up. The tray
   stands in the start zone for this episode's config, and the other two zones are bare:
   * **Config L:** back-left, behind the label sheet
   * **Config M:** front-center, in front of the label sheet and clear of the body's front face
   * **Config R:** front-right, left of the screw tray
5. Four matching **screws** are staged head-up in the **screw tray** at the front-right. Each has a straight
   shank, clean threads, and an unmarked head.
6. One **lid** lies on the **lid stand** at the right, face up, with its **front mark** pointing toward the
   front edge. Its **grab rib** stands up across the middle of its top face. Its four corner holes are clear.
7. One **torque driver** stands in the **driver cradle** at the back-right, set to forward and to the
   validated torque setting.
8. One **label sheet** lies flat just left of the center of the table, carrying one label, **label face** up.
9. The gasket has no cracks, splits, flat spots, or frayed edges, and it is not stretched out of shape.
10. Keep the left side of the table clear apart from the label sheet and (Config L) the gasket tray. The left
    gripper comes in from there onto the body, the lid, and the label sheet.
11. Before collection, confirm by hand that the gasket drops into the groove all the way round without being
    stretched, that the lid's four holes drop over the four posts with the gasket seated, that each screw
    turns into its post by hand, and that the driver clicks on each corner at the set torque.

### Workspace layout

- **Assembly spot:** just right of the center of the table — the body stays clamped in its fixture here for
  the whole episode
- **Body rim:** the groove all the way round, with post **1** at the front-left, **2** at the front-right,
  **3** at the back-right, and **4** at the back-left
- **Start zone:** the gasket tray with one gasket (input) — back-left (**Config L**), front-center, in front
  of the label sheet (**Config M**), or front-right, left of the screw tray (**Config R**). One per episode
- **Front-right:** the screw tray with four screws
- **Right supply zone:** the lid stand with one lid
- **Back-right:** the driver cradle with the torque driver
- **Just left of center:** the label sheet with one label, lying flat
- **Left side:** kept clear apart from (Config L) the gasket tray, so the left gripper can come in onto the
  body, the lid, and the label sheet

### Arm assignments

- **Left gripper:** in Config L and M, lifts the gasket out of its tray and hands it over to the right gripper
  above the body; presses the gasket down on the left run of the groove while the right gripper seats the
  rest, then presses the lid flat on the body until all four screws hold on their own, squares the torque
  driver in the right gripper, and pins the label sheet flat for the peel.
- **Right gripper:** carries the gasket from the tray (Config R) or takes it from the left gripper above the
  body (Config L and M), lays it into the groove, presses the gasket home,
  carries the lid by its grab rib and lowers it on, starts each of the four screws by hand, holds the torque
  driver and torques the four screws, then peels the label and presses it onto the front face.

## Vocabulary

- **Enclosure body:** the open-top box the lid closes. It stays clamped in the holding fixture for the whole
  episode and is never lifted or turned.
- **Holding fixture:** the clamp on the assembly spot that holds the body still. It is never opened during an
  episode.
- **Rim:** the flat top edge of the body, running all the way round the open top.
- **Groove:** the channel cut into the rim that the gasket sits in.
- **Rim land:** the flat strip of rim on either side of the groove. The lid lands on it once the gasket is
  seated.
- **Gasket:** the rubber loop that sits in the groove and seals the lid.
- **Start zone:** where the gasket tray stands at the start of the episode — back-left (**Config L**),
  front-center (**Config M**), or front-right (**Config R**). One per episode, chosen before recording and
  never changed mid-episode.
- **Hand over:** the left gripper holds the gasket still above the body by the outside face of its left run,
  the right gripper closes on the outside face of the right run, and only then does the left gripper open and
  lift clear. Config L and M only, because the left gripper never reaches across the body.
- **Line:** the painted line running all the way round the top face of the gasket. If the line disappears
  anywhere, that part of the gasket is twisted.
- **Run:** one straight side of the gasket or the groove. There are four: the **back run**, the **left run**,
  the **right run**, and the **front run**.
- **Seated:** the gasket sits down inside the groove all the way round, with no part of it above the rim and
  no part of it up on the rim land.
- **Proud:** a part of the gasket stands above the rim instead of sitting down in the groove.
- **Bunched:** the gasket has too much length in one place, so it bulges away from the groove wall or lifts
  into a loop at a corner.
- **Lid:** the flat plate that closes the body. It has four corner holes, a grab rib, and a front mark.
- **Grab rib:** the raised rib across the middle of the lid's top face. It is the only place the right gripper
  pinches the lid.
- **Front mark:** the painted mark on one edge of the lid's top face. It points toward the front edge when the
  lid is the right way round.
- **Screw post:** one of the four short posts at the corners of the rim, each with a tapped hole for one
  screw.
- **Post numbers:** post **1** is the front-left, **2** the front-right, **3** the back-right, and **4** the
  back-left. Screws are started in the order 1, 2, 3, 4.
- **Cross pattern:** torquing diagonally opposite corners in turn, in the order **1 → 3 → 2 → 4**.
- **Started screw:** the screw stands upright in its post, holds on its own when the gripper opens, and still
  shows a gap between its head and the lid.
- **Holds on its own:** the screw stays standing in the post, and does not fall or lean, once the gripper
  lets go.
- **Torque driver:** the hand driver in the cradle. Turned clockwise on a screw, it clicks once when the screw
  reaches the set torque.
- **Driver vertical:** the bit points straight down and the driver body looks upright, not tilted, when seen
  against the lid.
- **Click:** the single sound and give of the driver when the screw reaches the set torque. It is the signal
  to stop turning that screw.
- **Front face:** the outside wall of the body facing the front edge. The label goes here, not on the lid and
  not on a side wall.
- **Label sheet:** the sheet lying flat just left of center that carries the label. It is held flat by the
  left gripper for the peel and is never lifted.
- **Label face:** the written side of the label.
- **Lifted corner:** a corner of the pressed label standing off the front face instead of lying flat on it.

## Steps

Run Steps 1–7 in order on the one enclosure, then end the episode with Step 8. Only Step 1.1 depends on where
the gasket tray is: in Config L and M the **left gripper** lifts the gasket and **hands it over** to the right
gripper above the body; in Config R the **right gripper** lifts it itself. Every other line is the same in all
three configs.

### Step 1: Lay the gasket into the groove

**Goal:** the gasket lies in the groove all the way round, flat and untwisted, without being stretched.

- Carry the gasket in one go, straight from the gasket tray to the body. Do not set it down on the rim or the
  table on the way.
- Hold the gasket by its outside face only. Do not hook the gripper tip inside the loop.
- Lay the runs in this order: **back run, left run, right run, front run**.
- Lay the gasket in. Do not stretch it, roll it, or pull it to make it fit.

#### 1.1 Lift the gasket

Look where the gasket tray is before reaching for the gasket.

- **IF the gasket tray is at the back-left (Config L):** with the **left gripper**, pinch the gasket by the
  outside face of its **left run**, lift it out of the tray, and carry it level, forward and to the right, to
  above the body. **Hand it over:** hold it still; the **right gripper** closes on the outside face of the
  **right run**; then the left gripper opens and lifts clear to the left.
- **IF the gasket tray is at the front-center (Config M):** with the **left gripper**, pinch the gasket by the
  outside face of its **left run**, lift it out of the tray, and carry it level, back and to the right, to
  above the body. Hand it over to the **right gripper** the same way.
- **IF the gasket tray is at the front-right (Config R):** with the **right gripper**, pinch the gasket by its
  outside face, lift it out of the tray, and carry it level to above the body.

Then, in all three:

- Hold the gasket flat above the body in the **right gripper**, by its outside face, with its painted **line**
  facing up.

#### 1.2 Lay the runs in

- With the **right gripper**, lower the **back run** into the back of the groove and let it rest there.
- With the **right gripper**, lay the **left run** into the groove, then the **right run**, then the
  **front run**.
- Let go once the whole gasket rests in the groove.

**Expected state:** the gasket rests in the groove all the way round, the gasket tray is empty, and no screw
has been touched.

**Check:** the gasket is in the groove on all four runs, the painted **line** shows all the way round on the
top face, and no part of the gasket is trapped under the rim land or hanging outside the body. If the line
disappears anywhere, the gasket is twisted: with the right gripper, lift that run out, untwist it flat, and
lay it back in.

### Step 2: Seat the gasket all the way round

**Goal:** the gasket sits down inside the groove all the way round, with nothing proud and nothing bunched.

- With the **left gripper**, press down on the gasket along the **left run** and hold it in the groove.
- With the **right gripper**, close the gripper and run its tip along the top of the gasket, pressing it down
  into the groove: the back run first, then the right run, then the front run.
- Press the gasket down only. Do not drag it sideways along the groove and do not pry under it with the tip.
- Keep the **left gripper** on the left run until the other three runs are pressed home, then press the left
  run with the **right gripper** as the left gripper lifts clear.

**Expected state:** the gasket is seated in the groove on all four runs, the rim land is clear, and the lid is
still on its stand.

**Check:** the gasket sits below the rim all the way round, with no part **proud** of the rim, no part up on
the rim land, and no **bunched** loop or bulge at any corner. If a part stands proud, press it down again with
the right gripper. If a corner is bunched, lift that run out with the right gripper, lay it back in, and press
it home again.

### Step 3: Place the lid on the body

**Goal:** the lid sits flat on the seated gasket, the right way round, with all four holes over their posts.

- With the **right gripper**, pinch the lid by its **grab rib**, lift it off the lid stand, and hold it level
  above the body with its **front mark** pointing toward the **front edge**.
- Carry the lid in one go. Do not set it down on the rim or the table on the way.
- With the **right gripper**, lower the lid straight down onto the body so all four holes drop over their
  posts and the lid lands flat on the rim land.
- Lower the lid level. Do not land it on one corner, and do not slide, drag, or twist it on the gasket to line
  the holes up.
- If a hole misses its post, lift the lid straight up with the **right gripper**, hold it level again, and
  lower it once more.
- Open the **right gripper** only once the lid rests flat on the body.

**Expected state:** the lid rests flat on the body, the front mark points toward the front edge, all four
posts stand through their holes, and the lid stand is empty.

**Check:** the lid sits flat on the rim land all the way round, its front mark points toward the front edge,
and each of the four posts stands in its own hole. If the lid rocks or sits high on one side, lift it straight
up with the right gripper, check the gasket as in Step 2, then lower the lid on again.

### Step 4: Hold the lid and start the four corner screws

**Goal:** all four screws stand started in their posts, each holding on its own with a gap under its head.

- With the **left gripper**, press the lid down flat by its **left edge**, and hold it there for the whole of
  this step.
- Start the screws by hand with the **right gripper**. Do not pick up the torque driver in this step.
- Start the screws in post order **1, 2, 3, 4**.

#### 4.1 Set one screw in its post

- With the **right gripper**, grasp one screw from the screw tray by the sides of its head, threaded end
  pointing down.
- Stand the screw upright in the hole of the current post, with the screw straight and the head level.

#### 4.2 Turn it in by hand

- With the **right gripper**, turn the screw **clockwise** a quarter turn, open the gripper, take the head
  again at the start of a fresh quarter turn, and turn again.
- Keep going until the screw has gone in **two full turns** and holds on its own when the gripper opens.
- Stop there. Leave a gap showing between the screw head and the lid.
- If the screw goes in crooked, binds, or will not turn, stop turning it, lift it back out with the **right
  gripper**, and set it in again. If it binds a second time, end the episode at Step 8 and log the post for a
  station check.

#### 4.3 Start the remaining screws

- Repeat 4.1 and 4.2 on the remaining posts, in the order 1, 2, 3, 4.
- Finish the current screw before taking the next screw from the tray.
- With the **left gripper**, let go of the lid and move clear only once all four screws hold on their own.

**Expected state:** four screws stand in the four posts, each holding on its own with a gap under its head,
the screw tray is empty, the lid sits flat on the body, and the left gripper is clear.

**Check:** all four posts carry a started screw, every screw stands straight, every screw still shows a gap
under its head, and the lid still sits flat on the rim land all the way round. If a screw is already tight
against the lid, leave it as it is and go on to Step 5. If a screw is missing or will not hold, set it again
as in 4.1 and 4.2.

### Step 5: Pick up the torque driver

**Goal:** the torque driver is held vertical in the right gripper, bit clear of the screws.

- With the **right gripper**, lift the torque driver out of its cradle by its handle.
- With the **left gripper**, steady and square the driver in the right gripper so the bit points straight down
  and the driver is **vertical**; open the **left gripper** once the driver is squared, and move it clear of
  the lid.
- Hold the driver in the **right gripper** for the whole of Step 6. Do not re-cradle it between screws.

**Check:** the driver is vertical in the right gripper, its bit is clear of all four screws, and the left
gripper is clear of the lid. If the driver sits tilted or loose, square it again with the left gripper before
touching a screw.

### Step 6: Torque the four screws in the cross pattern

**Goal:** each of the four screws is torqued to one click, in the order **1 → 3 → 2 → 4**.

- Torque the screws in the **cross pattern**: post **1**, then post **3**, then post **2**, then post **4**.
- Give each screw one click. Do not go back to a screw that has already clicked.
- Keep the **left gripper** clear of the lid and the driver for the whole of this step.

#### 6.1 Torque one screw

- With the **right gripper**, set the driver bit down into the head of the current screw, keeping the driver
  **vertical**.
- Turn the driver **clockwise** in a steady move until it **clicks** once.
- Stop turning the moment it clicks.
- Lift the driver straight up off the screw head.

#### 6.2 Work round the cross pattern

- Repeat 6.1 on the next post in the cross pattern, until all four screws have clicked once.
- If the bit slips out of a head, or the driver tilts off vertical, stop turning, set the bit back down
  square, and turn again.
- If a screw will not click, or a screw turns without ever coming up against the lid, stop, end the episode at
  Step 8, and log that post for a station check.
- With the **right gripper**, return the driver to its cradle once the fourth screw has clicked.

**Expected state:** all four screws are down against the lid, each having clicked once, the lid sits flat on
the body all the way round, and the driver is back in its cradle.

**Check:** all four screws clicked, the lid sits flat on the rim land all the way round, no screw head stands
off the lid, and no part of the gasket has been squeezed out onto the rim land or outside the body. If gasket
shows outside the groove, leave the screws as they are and log the episode for a station check.

### Step 7: Label the front face

**Goal:** the label lies flat on the body's front face, writing upright and centered.

- With the **left gripper**, press the **label sheet** flat on the table and hold it there for the whole peel.
- With the **right gripper**, close on the corner of the label and peel it off the sheet in one motion, with
  the **label face** out.
- With the **left gripper**, let go of the sheet and move clear of the front face. The sheet stays flat on the
  table.
- With the **right gripper**, bring the label to the body's **front face**, label face out and the writing
  upright.
- Press the label onto the front face, centered on the face, then press along it from one edge to the other.

**Expected state:** the label lies flat on the front face, the label sheet is empty and still flat on the
table, and both grippers are clear of the enclosure.

**Check:** the label is on the body's front face, its writing is upright, it sits centered on the face, and it
lies flat with no **lifted corner**. If a corner stands off, press it down again with the right gripper. If
the label went on the lid, a side wall, or badly crooked, leave it as it is and log the episode for a station
check.

### Step 8: End the episode

**Goal:** recording ends with the enclosure closed, torqued, and labeled, and both arms home.

1. Confirm the gasket is seated all the way round, the lid sits flat on the body, all four screws are down
   against the lid, the label lies flat on the front face, the gasket tray, screw tray, and lid stand are
   empty, and the torque driver is back in its cradle.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

1. With recording off, set the torque driver to reverse, or use a hand driver, and back the four screws out in
   the order 4, 2, 3, 1. Return the driver to forward and to the validated torque setting.
2. Lift the lid straight up off the body and set it on the lid stand, face up, with its front mark toward the
   front edge.
3. Lift the gasket out of the groove and lay it flat in the gasket tray, line facing up and no twist in it.
   Stand the tray in the start zone for the next episode's config — back-left (Config L), front-center
   (Config M), or front-right (Config R) — leaving the other two zones bare.
4. Peel the label off the front face and wipe any adhesive off the body.
5. Wipe grit, dust, and rubber crumbs out of the groove and off the rim land. Wipe the underside of the lid.
6. Stage four screws head-up in the screw tray and leave all four post holes empty.
7. Lay one label sheet flat just left of center, label face up.
8. Inspect the parts. Replace the gasket if it is cracked, split, flat-spotted, frayed, or stretched so far
   that it no longer drops into the groove. Replace a screw with damaged threads or a marked head. Replace the
   lid if a hole is torn or the grab rib is loose. Replace the body if a post thread no longer holds a screw
   or the groove is damaged. Tighten the holding fixture if the body moves under a gripper.
9. Run both Setup checklists before the next episode.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

- the **start timestamp** in the video;
- the **violation name** from the list below; and
- the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an annotation
label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain multiple violations; tag each
separately. Retain the episode in training data with its violation tags. Do not delete a recorded episode
solely because it contains a violation.

### Violations

**Note on the start position:** the violations below were written for Config R (gasket tray at the
front-right, left of the screw tray). The pickup and arm-role cues will be rewritten later to cover all three
start positions; they are left as they are for now. Until then, anything that does not match the episode's
config goes under **Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the gasket tray is not in
  the start zone for the config; a gripper reaches across the table for the gasket; in Config L or M the left
  gripper lays the gasket into the groove itself, or the right gripper reaches to the left for it, instead of
  a hand-over above the body; or the wrong IF line is followed.
- **SOP rule broken:** the start position, the same-side rule, and the hand-over rule (the left gripper lifts
  the gasket in Config L and M and hands it over to the right gripper above the body; the right gripper lifts
  it in Config R; no arm reaches across the table; the IF line followed is the one for the config on the
  table).
- **Coaching note:** look where the gasket tray is before the first reach, then follow that config's IF line
  through Step 1.1.

**Violation: Gasket mishandled on the way in**
- **Visible cue:** the gasket is set down on the rim or the table on the way from the tray, is picked up by
  its inside face, or the gripper tip is hooked inside the loop to carry it.
- **SOP rule broken:** Step 1 (carry the gasket in one go, straight from the tray to the body, held by its
  outside face).
- **Coaching note:** one lift, outside face, straight into the groove.

**Violation: Gasket runs laid in the wrong order**
- **Visible cue:** the front run or a side run goes into the groove before the back run is resting in it.
- **SOP rule broken:** Step 1 (lay the runs in the order back, left, right, front).
- **Coaching note:** far side first. The back run anchors the loop, and the rest falls in.

**Violation: Gasket stretched or forced into the groove**
- **Visible cue:** the gasket is pulled hard along a run, rolled into the groove, or worked on with the
  gripper tip under it, instead of being laid in and pressed down.
- **SOP rule broken:** Steps 1–2 (lay the gasket in without stretching, rolling, or pulling it to fit, and
  press it down only).
- **Coaching note:** it should drop in. If it needs a pull, it is the wrong gasket or it is bunched.

**Violation: Gasket left twisted**
- **Visible cue:** the painted line on the gasket disappears somewhere round the loop, or a run shows a
  visible half-turn, and the episode goes on anyway.
- **SOP rule broken:** Step 1 (the line shows all the way round on the top face before Step 2).
- **Coaching note:** follow the line all the way round with your eye before you press anything down.

**Violation: Gasket not seated all the way round**
- **Visible cue:** part of the gasket stands proud of the rim, sits up on the rim land, or bulges away from
  the groove wall or loops up at a corner, and the step moves on.
- **SOP rule broken:** Step 2 (the gasket sits below the rim all the way round, with nothing proud, nothing on
  the rim land, and no bunched loop at a corner).
- **Coaching note:** press all four runs and look all the way round before you touch the lid.

**Violation: Gasket left run not held**
- **Visible cue:** the left gripper is off the left run while the right gripper presses the other runs, and
  the gasket lifts, shifts along the groove, or pops out on the left.
- **SOP rule broken:** Step 2 (the left gripper presses the gasket down on the left run and holds it until the
  other three runs are pressed home).
- **Coaching note:** left gripper pins the left run first, then press round with the right.

**Violation: Lid placed before the gasket is seated**
- **Visible cue:** the lid comes down while part of the gasket is still proud, on the rim land, twisted, or
  bunched.
- **SOP rule broken:** Steps 2 and 3 (the gasket is seated all the way round before the lid is lowered).
- **Coaching note:** seat first, lid second. A lid on a proud gasket only pinches it worse.

**Violation: Lid dragged or slid on the gasket**
- **Visible cue:** the lid lands and is then slid, dragged, or twisted on the rim to line the holes up with
  the posts, or it is set down on the rim on the way from the stand.
- **SOP rule broken:** Step 3 (lower the lid straight down; if a hole misses its post, lift the lid straight
  up and lower it again).
- **Coaching note:** lift and re-land it. Never shove a lid across a seated gasket.

**Violation: Lid set down wrong**
- **Visible cue:** the front mark does not point toward the front edge, a post is not in its own hole, the lid
  rests on top of a post, or the lid lands on one corner and stays rocking or high on one side.
- **SOP rule broken:** Step 3 (lower the lid level, front mark toward the front edge, with all four holes over
  their posts and the lid flat on the rim land).
- **Coaching note:** mark to the front, level all the way down, four posts through four holes.

**Violation: Lid not held down through the start pass**
- **Visible cue:** the left gripper is off the lid's left edge while screws are being started, or it lets go
  before all four screws hold on their own, and the lid lifts, rocks, or shifts.
- **SOP rule broken:** Step 4 (the left gripper presses the lid down by its left edge for the whole of Step 4
  and lets go only once all four screws hold on their own).
- **Coaching note:** the left gripper stays on the lid until four screws can hold it themselves.

**Violation: Screws started out of order**
- **Visible cue:** a screw is started in a higher-numbered post while a lower-numbered post is still empty.
- **SOP rule broken:** Step 4 (start the screws in post order 1, 2, 3, 4).
- **Coaching note:** 1, 2, 3, 4 round the corners. Finish one screw before taking the next.

**Violation: Screw run down tight in the start pass**
- **Visible cue:** a screw is turned in until its head pulls down against the lid with no gap left, or the
  torque driver is picked up and used before all four screws are started by hand.
- **SOP rule broken:** Step 4 (turn each screw in two full turns by hand until it holds on its own, leaving a
  gap under the head; no driver in this step).
- **Coaching note:** start means started. Two turns, gap under the head, hands only.

**Violation: Crooked screw forced**
- **Visible cue:** a screw stands leaning or binds, and the gripper keeps turning it instead of backing it out
  and setting it again.
- **SOP rule broken:** Step 4.2 (stop turning a screw that goes in crooked, binds, or will not turn; lift it
  out and set it in again).
- **Coaching note:** stop at the first bind. A forced screw wrecks the post.

**Violation: Torque pass started with fewer than four screws holding**
- **Visible cue:** the driver goes down on a screw while a post is still empty or a started screw has fallen
  or is leaning.
- **SOP rule broken:** Steps 4 and 6 (all four screws stand started and holding on their own before any screw
  is torqued).
- **Coaching note:** four screws in first. Pulling one corner down alone lifts the lid off the others.

**Violation: Torque driver not held vertical**
- **Visible cue:** the driver sits tilted or loose in the right gripper and the left gripper never squares it,
  or the driver tilts off upright while a screw is being turned, or the bit slips out of the head and turning
  continues.
- **SOP rule broken:** Steps 5 and 6.1 (square the driver vertical with the left gripper before touching a
  screw, and keep it vertical while turning; if the bit slips, stop, set it back down square, and turn again).
- **Coaching note:** square it, then turn. A tilted driver slips and marks the head.

**Violation: Torque order not the cross pattern**
- **Visible cue:** the screws are torqued in an order other than 1 → 3 → 2 → 4, for example straight round the
  corners, or a screw that has already clicked is turned again.
- **SOP rule broken:** Step 6 (torque in the cross pattern 1 → 3 → 2 → 4, one click each, and do not go back
  to a screw that has clicked).
- **Coaching note:** always cross to the opposite corner. Say the next post number before you move.

**Violation: Screw turned past the click**
- **Visible cue:** the driver keeps turning after it has clicked, or it is worked until it clicks a second
  time on the same screw.
- **SOP rule broken:** Step 6.1 (stop turning the moment the driver clicks, then lift it straight up).
- **Coaching note:** one click, hands off. The click is the finish line, not a checkpoint.

**Violation: Screw left without a click**
- **Visible cue:** the driver is lifted off a screw before it clicks, or the episode goes on to the label with
  a screw head still standing off the lid.
- **SOP rule broken:** Step 6 (every one of the four screws is turned until the driver clicks once).
- **Coaching note:** four screws, four clicks. Count them out loud.

**Violation: Label sheet not pinned for the peel**
- **Visible cue:** the left gripper is off the label sheet while the right gripper peels, or the sheet lifts,
  slides, or folds during the peel.
- **SOP rule broken:** Step 7 (the left gripper holds the sheet flat on the table for the whole peel; the
  sheet is never lifted).
- **Coaching note:** pin the sheet first, then peel. The sheet never leaves the table.

**Violation: Label crooked, off center, or lifting**
- **Visible cue:** the writing on the label face is not upright, the label sits off center on the front face,
  or a corner of it stands off the face.
- **SOP rule broken:** Step 7 (press the label on centered on the front face, writing upright, then press
  along it from one edge to the other).
- **Coaching note:** line it up before it touches, then press right across it.

**Violation: Label put on the wrong surface**
- **Visible cue:** the label goes on the lid, a side wall, the back wall, or the fixture instead of the body's
  front face.
- **SOP rule broken:** Step 7 (the label goes on the body's front face, the outside wall facing the front
  edge).
- **Coaching note:** front face means the body wall you are looking at, never the lid.

**Violation: Work done out of order**
- **Visible cue:** the steps run out of sequence, for example the lid goes on before the gasket is pressed
  home, a screw is torqued before all four are started, or the label goes on before the fourth screw clicks.
- **SOP rule broken:** Steps 1–7 (lay, seat, lid, start, pick up the driver, torque, label, in that order).
- **Coaching note:** the order is the task. Say the next step's name before you move.

**Violation: Wrong arm used**
- **Visible cue:** an action assigned to one gripper is done by the other, including the left gripper laying
  or pressing the gasket runs other than the left run, carrying the lid, starting or torquing a screw, or
  pressing the label on; or the right gripper holding the lid down during the start pass or pinning the label
  sheet.
- **SOP rule broken:** Steps 1–7 (the right gripper lays and seats the gasket, carries the lid, starts and
  torques the screws, and applies the label; the left gripper presses the left run, holds the lid, squares the
  driver, and pins the sheet).
- **Coaching note:** right gripper does the work, left gripper holds and steadies.

**Violation: Part or supply knocked off its spot**
- **Visible cue:** a screw, the gasket, or the lid is dropped on the lid, the table, or the floor; a tray or
  the lid stand is tipped, pushed off its spot, or spilled; or the body is knocked out of square in its
  fixture.
- **SOP rule broken:** Steps 1–7 (keep the parts, the trays, the lid stand, and the body on their spots
  through the assembly).
- **Coaching note:** work slower and lower over the table, and keep every carry short.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before the end state is confirmed, the driver is left out of its cradle, an
  arm is not home, a gripper is closed, or an arm does something else after homing.
- **SOP rule broken:** Step 8 (confirm the end state with the driver cradled, return both arms home with
  grippers open as their final action, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by how the task was run are system issues. Log and discard the episode rather than tagging
them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- The torque driver does not click at the set torque, clicks early, or slips its setting.
- A gasket is split, flat-spotted, or moulded out of shape, so a correctly laid gasket will not sit in the
  groove.
- A post thread is stripped, so a correctly started screw spins without ever coming up against the lid.
- A screw thread is damaged or its head is soft, so it binds or the bit cannot hold it.
- A lid hole is torn or a lid is warped, so a correctly lowered lid cannot sit flat on the rim land.
- The holding fixture is loose, so the body moves however carefully a gripper presses on it.
- The label has no tack left, or it tears during a correct peel.

## Annotation subtasks (from SOP)

1. Carry the gasket from the tray and lay it into the groove
2. Hand the gasket from the left gripper to the right gripper above the body (Config L and M)
3. Press the gasket home all the way round
4. Carry the lid from its stand and lower it onto the body
5. Hold the lid down with the left gripper
6. Start one screw by hand in its post
7. Pick up the torque driver and square it
8. Torque one screw to a click
9. Return the torque driver to its cradle
10. Peel the label off the sheet
11. Press the label onto the front face
12. Confirm the end state, return both arms home, and end the episode
