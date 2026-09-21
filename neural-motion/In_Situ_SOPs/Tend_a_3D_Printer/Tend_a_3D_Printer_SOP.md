# Tend a 3D Printer SOP (1x Tend Cycle, in situ)

One episode tends one finished print at the printer where it lives.

The base is **passive**. It has no drive of its own. It is pushed by hand to the bench in front of the
printer and locked there. Nothing is carried away to a table. Everything the episode touches is already
there when recording starts: the printer on its bench under the shelf, the debris tray on its ledge under
the door sill, the plate rest on the bench in front of it, and the scraper and the brush on the bench beside
it, on whichever side this episode's config puts them.

The episode runs these nine actions in this order and no other: **check the printer at the panel, open the
front door, lift the build plate off the bed, bow the part off over the tray, scrape the plate clean, clear
the bed, reseat the plate, shut the front door, start the next job.**

The printer is worked **as found**. The job on the bed is finished. The front door is shut. The bed is cool.
The toolhead is parked at the back left. The printed part is still stuck to the build plate. The episode ends
with the part and the scrapings in the tray, the plate clean and back on the bed, the door shut, and the next
job running.

**This printer is a closed box.** It has glass on the front and glass on top. The only way in is the **front
door**. The **top cover** stays on, the **filament unit** stands on top of it, and a **feed tube** runs from
that unit into the back of the printer. Nothing on top is ever touched.

**This is an in-situ task. Four rules follow from that.**

First, there is a **shelf directly above the printer**, and the top of the printer is closed. So **every
approach is from the front, straight in, level**. No gripper comes down onto the bed from above.

Second, the **printer is never leaned on and never pushed**. No gripper, wrist, or forearm rests on the glass,
the frame, the bed, or the panel. No press is ever hard enough to shift the machine.

Third, the **printer stays where it stands**. It is not turned, slid along the bench, or tipped to make a
reach easier.

Fourth, the **purge chute and its bin are behind the printer**, out of both arms' reach. They are not part of
this episode and are never touched.

**The build plate is only ever held by its two front corners**, one gripper on each. No gripper ever touches
the **print side** of the plate. The plate is **never turned over**. It comes off the bed print side up, it
is worked print side up, and it goes back print side up.

**The bench is set up in one of three ways.** The printer, the tray, the plate rest, and the panel never move.
Only the scraper and the brush do.

* **Config L:** the scraper and the brush both lie on the bench to the **left** of the plate rest.
* **Config M:** the scraper lies to the **left** of the plate rest and the brush to the **right**.
* **Config R:** the scraper and the brush both lie on the bench to the **right** of the plate rest.

One config per episode, chosen before recording and never changed mid-episode. Where a step depends on the
setup it says so on an **IF** line. Look at the bench and follow the line that matches.

**The two arms never cross.** Everything sits on the centre line or on its own side. The **debris tray and
the plate rest are centred** in front of the printer, and each gripper works its own side of the plate. The
**panel is on the right** and belongs to the right gripper alone. The **left gripper always stays left of the
right gripper.**

**Tool-side rule:** the gripper on a tool's side is the one that takes it and works it. While the plate is
scraped, the other gripper holds the plate down by its front corner. While the bed is swept, the other arm
stays at home. No arm reaches across the plate rest for a tool.

The **front door is the one thing both arms work**, because it hinges on the left and its handle is on the
right. The **right gripper** pulls the catch open and takes it through the first half of its swing. The **left
gripper** takes it through the second half, out to its stop. Shutting it runs the same swing backwards. The
door is never carried and never handed over: each gripper takes it in its own half of the swing and lets go
before the other one moves.

Every other arm role is fixed and never swaps. The **right gripper** takes the door catch, the control panel,
the press-downs, and the right front corner of the plate. The **left gripper** takes the outer half of the
door swing and the left front corner of the plate in both carries. Only the scraper, the brush, and the hold
on the plate while it is scraped follow the tool-side rule.

## Setup

Complete the base positioning and both checklists before starting an episode.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Base positioning

The base is **passive**. It has no drive of its own. It is pushed into place by hand. It is never steered,
nudged, or repositioned once recording starts. It is parked once, before recording, and does not move again
until the episode is over.

1. Push the base by hand up to the bench. Stop it **square to the front of the printer**, so the front of the
   machine runs straight across the camera frame and neither side of it sits nearer than the other.
2. Stop it **centred on the door opening**, so the left upright and the right upright of the opening are the
   same distance out from the middle of the base. The debris tray and the plate rest then line up with the
   middle of the base too.
3. Stop it **close enough** that both grippers reach the back edge of the bed straight in through the door
   opening without either arm extending. Stop it **far enough** that no arm, wrist, or part of the base
   touches the printer, the open door, or the shelf above while both arms work.
4. Check the **height band**. With the base parked, both grippers enter the door opening level, carry the
   plate in and out of it, and the **right gripper** reaches every touch target on the panel. None of this
   makes a wrist or forearm touch the gantry, the top cover, the filament unit, or the shelf above.
5. Check the **door swing**. The **right gripper** reaches the door handle with the door shut and carries it
   through the first half of its swing without extending. The **left gripper** reaches the handle at that
   halfway point and carries the door out to its **door stop** without extending. Neither arm reaches past
   the other to do it.
6. Check the **open door**. At its stop the door stands clear of both arms' path to the door opening, clear
   of the panel, and clear of the plate rest, the tray, the scraper, and the brush. Its whole swing passes
   above the bench top and touches nothing on it.
7. Check the **bench**. The **right gripper** reaches the panel, and each gripper reaches the scraper and the
   brush where they lie on its own side, without extending. **Both** grippers reach the plate's front corners where the plate lies on the plate rest, the
   left gripper on the left corner and the right gripper on the right corner, without extending and without
   either arm reaching past the other.
8. Check the **carry line**. Both grippers carry the plate from the bed to the plate rest and back without
   either arm crossing in front of the other, without the plate passing over the panel, and without the plate
   touching the open door.
9. Check the **tray line**. The debris tray sits on its ledge directly below the **door sill**, centred, with
   its open top clear, so the plate is held over it and the bed is swept into it without either arm reaching
   to one side.
10. Lock or brake the base. Push it firmly once by hand. It must not roll, creep, or turn.
11. If any of lines 1 to 9 fails, push the base to a new park by hand and start again at line 1. Do not work
    a printer the arms cannot reach comfortably.

**The base stays locked and still for the whole episode.** Nothing moves it. No arm leans on the bench hard
enough to shift it. Nothing touches it by hand. It is never repositioned mid-task. A base that moves after
recording starts ends the episode.

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera is centred on the front of the printer. Its frame includes the whole bed, the build
   plate on it, the door shut and the door open at its stop, the panel, the debris tray on its ledge, the
   plate rest, and the scraper and the brush on the bench.
3. The camera reads the bed through the open door from the front. You can see whether the plate sits flat and
   square and whether debris is left on the bed.
4. The camera reads the plate on the plate rest from the front. You can see whether the part has come off and
   whether the print side is clean.
5. The camera reads the panel. You can see what the display shows, what the bed temperature reads, and where
   the **right gripper** presses.
6. The camera reads the debris tray. You can see whether the part and the scrapings landed in it.
7. The camera reads the door front once it is shut, so a door standing ajar is readable.
8. Both arms are at home with grippers open.
9. The **right gripper** has its **stylus tip** fitted to a finger, seated firm and not loose. It is fitted
   before recording starts and is never taken off or put on during the episode.
10. The **right arm** reaches the door handle with the door shut, the plate's right front corner on the bed
    and on the plate rest, the scraper and the brush when they lie on the right, the whole bed surface, and
    every touch target on the panel, without extending to a joint limit.
11. The **left arm** reaches the door handle at the halfway point of the swing and at the door stop, the
    plate's left front corner on the bed and on the plate rest, the scraper and the brush when they lie on
    the left, and the whole bed surface, without extending. It reaches no touch target on the panel.
12. Both grippers enter and leave the door opening **from the front and level**. Neither comes down onto the
    bed from above. Neither wrist nor forearm touches the gantry, the top cover, the filament unit, the feed
    tube, or the shelf above on the way in or out.
13. The two arms do not touch each other while they carry the plate together, the left gripper stays left of
    the right gripper throughout, and neither arm passes over the panel.
14. If a place cannot be reached, re-park the base by the Base positioning steps until lines 10 to 13 hold.

### Materials checklist

1. The **printer** stands where it lives, on its bench, set back from the front edge. It is not moved, not
   leaned on, and not pushed at any point.
2. The printer is a **closed box**. It has a glass **front door**, a glass **top cover** that stays on, and a
   solid back. There is a **shelf directly above the printer**. So the only way to the bed is the front door,
   never the top.
3. The **filament unit** stands on the top cover with its **feed tube** running into the back of the printer.
   Both are out of the arms' path and are never touched.
4. The **purge chute** and its waste bin sit behind the printer, out of both arms' reach. They are not
   emptied, checked, or touched in this episode.
5. The **front door** is hinged on the left and its **handle** is on the right. It is held shut by a catch. It
   swings open to the left, past the front of the machine, and **stands at its door stop on its own**, without
   being held and without drifting shut.
6. A correctly shut door meets the frame all round, stands flush with the front of the printer, and does not
   spring back open.
7. The **door opening** is tall enough and wide enough that both grippers carry the plate in and out level
   with the door standing at its stop.
8. The **door sill** is the bottom edge of the door opening. The bed sits level with it, so a brush pull runs
   from the back of the bed straight over the sill and out of the printer.
9. The **toolhead is parked at the back left of the bed and raised clear of it**. It stays there until the
   next job starts.
10. The **bed** is a flat heated magnetic bed. It sits level with the door sill when the job ends and does not
    move at any point in the episode. It carries **two locating pins** at its back edge that set where the
    plate sits.
11. The **build plate** is a flexible steel sheet lying on the bed, held by the bed's magnets. It sits flat
    and square, with its back edge against both locating pins.
12. The plate's **front edge stands out past the front edge of the bed**, so both grippers close on the left
    and right ends of it. Those two **front corners** are the only part of the plate a gripper ever holds.
13. The plate springs back flat on its own after it is bowed. It does not crease.
14. The **print side** of the plate faces up. It carries one finished **part**, plus the skirt and the **prime
    line** the printer laid down at the front left of the plate when the job started.
15. The part is stuck to the plate but not welded to it. It comes free when the plate is bowed, or it lifts
    under a flat blade.
16. The part is small enough and light enough that one bow drops it into the debris tray. It does not roll out
    of the tray once it is in.
17. The bed is **cool to handle**. The panel reads the finished job and the bed temperature before the episode
    starts.
18. The **panel** is a touch screen at the front right of the printer, to the right of the door, readable from
    the front. It shows the finished job and the bed temperature at the start. It carries a **Print** target,
    a job list, and a **Start** target. All three are **touch targets** drawn on the screen. The printer has no
    physical button that this episode uses, and the only input the arms give it is a touch on the screen with
    the stylus tip. The exact menu path, **Print**, then the top job, then **Start**, is **unvalidated**: confirm
    it on the station's printer before the first recording, and rewrite Step 9.1 if that printer's menu differs.
19. The **tray ledge** is a fixed shelf on the front of the printer bench, **directly below the door sill and
    centred on the door opening**. It holds the debris tray at a height where the tray's open top sits just
    under the sill.
20. The **debris tray** stands on the tray ledge. It has low walls all round, deep enough that a part lying in
    it does not roll out, and low enough that scrapings pushed off the plate and debris swept off the bed drop
    straight into it. It is empty at the start. **It is never lifted, carried, or moved at any point in the
    episode.**
21. The **plate rest** is a clear flat area of the bench **directly in front of the debris tray**, centred on
    the base, wide enough for the whole plate to lie flat on it with its front corners standing clear toward
    the front.
22. The plate rest is far enough forward of the tray that debris pushed off the plate's far edge falls into
    the tray and not onto the bench.
23. The **scraper** lies flat on the bench beside the plate rest, on the side this episode's config puts it,
    the **left in Config L and M** and the **right in Config R**, handle toward the front, blade away from the
    front. Its blade is stiff plastic, flat, and square-edged. It does not gouge the plate.
24. The **brush** lies flat on the bench beside the plate rest, on the side this episode's config puts it, the
    **left in Config L** and the **right in Config M and R**, bristles down, handle toward the front. When both
    tools are on one side they lie side by side. Its bristles are soft enough not to mark the bed.
25. The bench between the plate rest, the scraper, and the brush is clear, so an arm carrying the plate, the
    scraper, or the brush passes over nothing.
26. Nothing else stands on the bench within either arm's reach. A tool lying to the left of the plate rest lies
    flat and low, and the door at its stop stands clear above it without touching it. Nothing else is on the
    bench to the left of the plate rest, so the open door has clear air over it.
27. There is a next job ready at the top of the job list on the panel.

### Workspace layout

Nothing anywhere is marked or taped out. You judge every place below by eye against the printer and the bench
themselves: the door opening, the bed, and the bench top.

* **Printer:** the closed box the base is parked at. It is never moved, never leaned on, and never pushed.
* **Top cover:** the glass panel on top of the printer. It stays on. Nothing ever touches it.
* **Filament unit and feed tube:** the unit standing on the top cover and the tube running from it into the
  back of the printer. Nothing ever touches either.
* **Shelf above:** the shelf directly over the printer. Together with the closed top it is what makes every
  approach a front approach. Nothing ever touches it.
* **Purge chute:** behind the printer, out of reach. Not part of this episode.
* **Front door:** the glass door on the front, hinged left, handle right. Opened and shut by both grippers,
  the **right gripper** in the half of the swing nearest the frame and the **left gripper** in the half
  nearest the stop.
* **Door opening:** the open front of the printer with the door at its stop. Both grippers go in and come out
  through it, level and from the front.
* **Door sill:** the bottom edge of the door opening. Debris swept forward goes over it into the tray below.
* **Bed:** the heated magnetic bed inside the printer, level with the door sill, with its two locating pins at
  the back edge. The plate sits on it.
* **Panel:** the touch screen at the front right of the printer. **Right gripper only.**
* **Build plate:** starts on the bed, is worked on the plate rest, and ends on the bed. Carried by both
  grippers, one on each front corner.
* **Tray ledge:** the fixed shelf directly below the door sill, centred on the door opening. It holds the
  debris tray and nothing else.
* **Debris tray:** stands on the tray ledge, centred, for the whole episode. The part and the scrapings and
  the bed debris all go in it. **Neither gripper ever touches it.**
* **Plate rest:** the clear area of bench directly in front of the debris tray, centred on the base, where the
  plate is laid print side up with its front corners toward the front. Both grippers use it, the left gripper
  on the left corner and the right gripper on the right corner.
* **Scraper:** lies flat on the bench beside the plate rest, left in Config L and M, right in Config R. Worked
  by the gripper on its side only.
* **Brush:** lies flat on the bench beside the plate rest, left in Config L, right in Config M and R. Worked by
  the gripper on its side only.

### Arm lanes

The two arms never cross. This holds for the whole episode.

* The **left gripper always stays left of the right gripper**. On the plate, the left gripper is always on the
  left front corner and the left side, and the right gripper is always on the right front corner and the right
  side.
* On the door, the **right gripper** works the half of the swing nearest the frame and the **left gripper**
  works the half nearest the stop. Only one gripper is on the door at a time, and the other arm is clear.
* Neither arm reaches over, under, around, or past the other. Neither arm reaches across the front of the other
  arm's body.
* The **right gripper alone** works the door catch and the panel, and whichever of the scraper and the brush
  lies on the right. The **left gripper alone** works whichever lies on the left. The **left gripper never goes
  right of the plate rest**, except to take the door handle at the halfway point of the swing, where the handle
  sits on the centre line, and the **right gripper never goes left of it**.
* Nothing is handed from gripper to gripper. Only one thing is moved at a time, except the plate, which both
  grippers carry together with a front corner each.

### Arm assignments

* **Right gripper.** Pulls the door catch open and takes the door through the inner half of its swing both ways. Takes the
  plate's right front corner in both carries. Presses the plate flat on the bed. Presses the door shut. Works
  the panel. Works whichever of the scraper and the brush lies on the right, and holds the plate down while the
  scraper is worked from the left. It never touches the debris tray.
* **Left gripper.** Takes the door through the outer half of its swing both ways. Takes the plate's left front
  corner in both carries. Works whichever of the scraper and the brush lies on the left, and holds the plate
  down while the scraper is worked from the right. It never touches the panel or the debris tray.

## Vocabulary

* **Front approach:** the gripper enters and leaves the door opening level and from the front. It never comes
  down onto the bed from above. Every action at the printer is a front approach.
* **Stylus tip:** the tip fitted to a finger of the **right gripper** so it can press the touch screen. It is
  part of the station hardware, fitted before recording and never touched during the episode. **Unvalidated.**
* **Door stop:** the point where the open door comes to rest by itself, swung fully out to the left and clear of
  the door opening. A door at its stop stands there without being held.
* **Halfway point:** the point in the door's swing where the handle sits out on the centre line, in front of the
  middle of the printer. It is where the **right gripper** lets go and the **left gripper** takes over, and
  where they change over again on the way back. The gripper that brings the door there stops it and holds it
  still for half a second before it lets go, so the door is not moving when the other gripper takes it.
  **Unvalidated.**
* **Latched:** the door meets the frame all round, sits flush with the front of the printer, and does not spring
  back when the **right gripper** comes off it.
* **Front corners:** the left and right ends of the plate's front edge, which stands out past the front of the
  bed. They are the only part of the plate a gripper ever holds.
* **Corner grip:** the **left gripper** closes on the left front corner and the **right gripper** on the right
  front corner, both flat on the plate and both closing at the same time. It is the only way the plate is ever
  taken hold of.
* **Print side:** the face of the plate the part was printed on. It faces up the whole episode. No gripper ever
  touches it.
* **Prime line:** the short line of plastic the printer laid down at the front left of the plate when the job
  started. It comes off with the scraper like the skirt.
* **Bow the plate:** both grippers hold the front corners still and both wrists roll forward together, so the far
  edge of the plate bends down and the plate curls with its print side on the outside of the curve.
* **Comes free:** the part is no longer stuck to the plate. It lifts, slides, or drops when the plate is bowed or
  when the blade goes under it.
* **Tool side:** the side of the plate rest a tool lies on in this episode's config. The gripper on that side is
  the only one that takes that tool. Scraper: left in Config L and M, right in Config R. Brush: left in Config
  L, right in Config M and R.
* **Scraping gripper:** in Step 5, the gripper on the scraper's side: the **right gripper** in Config R, the
  **left gripper** in Config L or M. It takes the scraper, makes the three passes, and puts the scraper back.
* **Holding gripper:** in Step 5, the gripper on the side opposite the scraper. It keeps its front corner of the
  plate pressed to the bench while the scraping gripper scrapes.
* **Sweeping gripper:** in Step 6, the gripper on the brush's side: the **right gripper** in Config M or R, the
  **left gripper** in Config L. It takes the brush, makes the three pulls, and puts the brush back. The other
  arm stays at home.
* **Blade flat:** the scraper is held so its whole blade edge lies down on the print side, not tipped up on a
  corner and not dug into the surface.
* **Clean plate:** the print side has no part, no skirt, no prime line, and nothing raised on it. Look across it
  from the front: nothing stands proud of the surface.
* **Seated flat:** the plate lies down on the bed all over, square to it, back edge against both locating pins,
  no corner lifted, and both front corners standing out clear past the front of the bed.
* **Cool to handle:** the panel shows the bed at or under its handling temperature, and the finished job is done.
* **Clear of the front:** the arm is drawn back so that no part of it is over the bench, the panel, the open door,
  or the door opening.
* **Touch target:** a spot drawn on the panel's touch screen that reacts to a press. **Print**, the **top job**,
  and **Start** are touch targets. There is no physical button anywhere in this task. **Unvalidated.**
* **Top job:** the first job in the list on the panel. It is the one that is started, every time.
* **Job running:** the panel shows the job name and the printer has begun to heat.
* **Levelling:** the check the printer runs on its own after **Start**, when it heats and then feels its way over
  the plate. Nothing touches the printer while it runs.

## Steps

Every bullet that moves an arm names the gripper that does it, even when the sub-step before it used the same
gripper. Where the gripper depends on the config, the bullet says which gripper it is in each config.

Steps 5 and 6 depend on the config: the gripper on the scraper's side scrapes while the other holds the plate,
and the gripper on the brush's side sweeps the bed. Every other step is the same in all three.

### Step 1: Check the printer at the panel

**Goal:** the printer is finished, cool, and safe to tend. Both arms have touched nothing yet.

#### 1.1 Read the panel

* Hold both arms **clear of the front**. Touch nothing.
* Read the panel from the front. The job on the bed is finished, and the bed is **cool to handle**.
* Look at the bed through the glass door. The toolhead is parked at the back left and raised. Nothing is
  moving.

**Check:** the panel reads the finished job, the bed reads cool to handle, and the toolhead is parked and still.
If the job is still running, if the bed is not cool, or if the toolhead is moving, do not touch the printer. End
the episode and report it.

**Expected state:** the door is shut. The finished part is still on the plate. The plate is still on the bed. The
tray, the scraper, and the brush stand where they started.

### Step 2: Open the front door

**Goal:** the door stands at its **door stop** on its own, and both arms are off it.

The door hinges on the left and its handle is on the right. So the swing is worked in two halves, one arm each,
and only one gripper is on the door at a time.

#### 2.1 Pull the catch open and start the swing

* With the **right gripper**, close on the door handle at the right edge of the door.
* With the **right gripper** still closed on the handle, pull it straight toward the front until the catch lets
  go, then keep pulling forward and to the left until the handle reaches the **halfway point**.
* Pull only as fast as the door swings. Do not snatch it. Do not lever it against the frame.
* Stop the door at the halfway point and hold it still with the **right gripper** for half a second, so the door
  has stopped moving before it is let go.
* Only then open the **right gripper**, draw the right arm back, and hold it **clear of the front**.

**Check:** the door stands part open at the halfway point and the handle is out on the centre line. The door was
still, not swinging, when the right gripper opened. The right arm is off the door. If the catch did not let go,
close on the handle again with the **right gripper** and pull straight toward the front once more.

#### 2.2 Swing it out to the stop

* With the **left gripper**, close on the door handle where it stands still at the halfway point.
* With the **left gripper**, carry the handle on round to the left until the door rests at its **door stop**.
* Open the **left gripper** and draw the left arm back.
* Do not push the door past its stop with the left gripper and do not let it swing back.

**Check:** the door stands at its stop on its own. It does not drift shut. It is clear of the door opening, the
panel, and both arms' path in. If it drifts, take the handle with the **left gripper** and set it at the stop
again.

**Expected state:** the door opening is clear. The plate and the part are still on the bed. Both arms are clear of
the front.

### Step 3: Lift the build plate off the bed

**Goal:** the plate is off the bed and out through the door opening, held by both front corners, print side up.

#### 3.1 Take both front corners

* Bring both grippers straight in over the door sill to the front edge of the plate, level. The **left gripper**
  goes onto the left front corner. The **right gripper** goes onto the right front corner.
* Close both grippers on the corners at the same time, flat on the plate.
* Do not close on the print side. Do not close on the part. Do not take the plate by one corner alone.

**Check:** both grippers hold a front corner, straight across from each other, with the left gripper on the left.
The part on the plate has not been touched.

#### 3.2 Peel the front edge up

* Lift both grippers straight up together, slowly, so the front edge of the plate comes up off the bed and the
  magnets let go from the front toward the back.
* Lift only as fast as the magnets release. Do not snap the plate up and do not jerk it.
* Keep both grippers lifting until the whole plate is off the bed and clear of both locating pins.

**Check:** the whole plate is off the bed. The part is still on it. The plate has not dragged across the bed.

#### 3.3 Draw it out

* With **both grippers**, the **left gripper** on the left front corner and the **right gripper** on the right
  front corner, draw the plate straight out through the door opening, level and slowly. Keep it print side up
  the whole way.
* Do not tilt it, do not swing it, and do not let it turn between the grippers.
* Do not let the plate or either wrist touch the gantry, the door sill, the open door, or the shelf above.

**Check:** the plate is clear of the printer, still level, and the part is still on it. Both grippers still hold
their front corners.

**Expected state:** the bed is bare. The plate hangs level between the two grippers, print side up. The door stands
at its stop. The tray is empty on its ledge.

### Step 4: Bow the part off over the tray

**Goal:** the part is in the debris tray and the plate is flat again.

The tray sits on its ledge directly in front of the printer, centred, under the door sill. So the plate is already
over it as it comes out. **Neither gripper touches the tray.**

#### 4.1 Hold the plate over the tray

* With **both grippers**, the **left gripper** on the left front corner and the **right gripper** on the right
  front corner, hold the plate level, low over the **debris tray**, with the plate's far edge above the tray's
  open top.
* Keep it print side up. Neither gripper lets go of its corner or moves along the edge.

**Check:** the plate hangs level over the tray. The part is over the tray and not over the bench.

#### 4.2 Bow it

* **Bow the plate.** With **both grippers** holding the front corners still, roll both wrists forward together,
  so the far edge bends down and the print side curves outward.
* Bow it until the part **comes free**, then hold the bow for 2 seconds.
* Roll both wrists back and let the plate spring flat.
* Do this **twice**.
* Bow it only far enough to release the part. Do not fold it. Do not bow it against the tray or the bench.

**Check:** the part has cracked free of the print side. If it is still stuck after two bows, leave it on the plate.
It comes off with the scraper in Step 5.

#### 4.3 Tip the part into the tray

* With **both grippers** still on the front corners, roll both wrists forward once more and hold, so the loose
  part slides off the far edge and drops into the tray.
* Keep the plate over the tray until the part has landed.
* Roll both wrists back and hold the plate level again.

**Check:** the part is lying in the tray. Nothing has landed on the bench or the floor. If the part landed on the
bench, leave it. It goes in the tray in the reset.

**Expected state:** the part is in the tray. The plate is flat and print side up between the grippers. The plate may
still carry the skirt and the prime line.

### Step 5: Scrape the plate clean

**Goal:** the print side is clean and the scraper is back on the bench.

Look which side the scraper is on before the plate comes down.

#### 5.1 Lay the plate down and hold it

* Lower the plate onto the **plate rest**, print side up, front corners toward the front, and set it flat.
* **IF the scraper is on the right (Config R):** open the **right gripper** and draw it off the right front
  corner. Keep the **left gripper** closed on the left front corner and press it down on the bench, so the plate
  cannot slide or turn.
* **IF the scraper is on the left (Config L or M):** open the **left gripper** and draw it off the left front
  corner. Keep the **right gripper** closed on the right front corner and press it down on the bench, so the
  plate cannot slide or turn.
* The **holding gripper** stays there until Step 5.4.

**Check:** the plate lies flat on the plate rest, print side up. It does not move when the **holding gripper**
presses on it.

#### 5.2 Take the scraper

* With the **scraping gripper**, close on the scraper handle, not on its blade. **IF Config R:** that is the
  **right gripper**. **IF Config L or M:** that is the **left gripper**.
* With the **scraping gripper**, lift the scraper straight up off the bench and carry it level to the near edge of
  the plate.

**Check:** the **scraping gripper** holds the scraper by its handle. The blade hangs clear of the bench. The
**holding gripper** is still pressing its front corner down.

#### 5.3 Scrape in three passes

* With the **scraping gripper**, set the blade down **blade flat** on the print side at the near edge of the
  plate.
* With the **scraping gripper**, push it straight away from the front, all the way to the far edge, so what it lifts goes over the far edge and
  drops into the tray behind the plate rest.
* Keep the blade flat the whole way. Do not tip it up on a corner. Do not dig it in. Do not pull it back toward the
  front with the blade still down.
* Do this **three times**: once down each third of the plate. Start on the scraper's side and finish beside the
  **holding gripper**. **IF Config R:** right third, middle, left third. **IF Config L or M:** left third,
  middle, right third.
* The **prime line** sits at the front left, just inside the left front corner. **IF Config R:** the left
  gripper holds that corner, so start the left pass beside the **left gripper**, not under it. **IF Config L or
  M:** that corner is free, so the first pass takes the prime line with it, and the last pass starts beside the
  **right gripper**, not under it. Keep the blade clear of the holding gripper and do not scrape over the corner
  it holds.

**Check:** the plate is a **clean plate**. There is no part, no skirt, no prime line, and nothing raised.
Everything that came off is in the tray. If plastic is still stuck, put the blade down just short of it with the **scraping
gripper** and push through it again.

#### 5.4 Put the scraper back

* With the **scraping gripper**, carry the scraper back to the bench and lay it flat where it started, on its own
  side, handle toward the front, blade away from the front.
* Open the **scraping gripper** and draw it clear of the scraper.
* Open the **holding gripper** and draw it back off its front corner.

**Check:** the scraper lies flat on the bench where it started. The clean plate lies flat on the plate rest.

**Expected state:** the plate is clean and lies on the plate rest. The part and the scrapings are in the tray. The
bed is still bare and the door still stands at its stop.

### Step 6: Clear the bed

**Goal:** the bed is clear of debris and the brush is back where it started.

The tray already sits on its ledge under the door sill. Nothing has to hold it. The **sweeping gripper** does this
whole step and the **other arm stays at home**. **IF the brush is on the right (Config M or R):** the sweeping
gripper is the **right gripper**. **IF the brush is on the left (Config L):** it is the **left gripper**, which
passes the open door on its way in and out and keeps the brush and the arm clear of it.

#### 6.1 Take the brush

* With the **sweeping gripper**, close on the brush handle, not on its bristles, and lift it straight up off the
  bench. **IF Config M or R:** that is the **right gripper**. **IF Config L:** that is the **left gripper**.

**Check:** the **sweeping gripper** holds the brush by its handle. The bristles hang clear of the bench. The other
arm is at home.

#### 6.2 Sweep the bed

* With the **sweeping gripper**, bring the brush straight in through the door opening, level, and set the
  bristles down on the bed at its back edge.
* With the **sweeping gripper**, pull the brush straight toward the front, in one pull, all the way over the **door sill**, so the debris goes over
  the sill into the tray below.
* Do this **three times**: once down the left third of the bed, once down the middle, once down the right third.
* Pull from back to front only. Do not sweep side to side. Do not sweep debris toward the locating pins. Do not
  knock the toolhead. Do not touch the open door with the brush.

**Check:** the bed is clear. There are no plastic bits, no strings, and nothing loose on it. What came off is in the
tray. If a bit is left on the bed, set the brush down beside it with the **sweeping gripper** and pull it forward
again.

#### 6.3 Put the brush back

* With the **sweeping gripper**, draw the brush straight out through the door opening, level. Carry it to the
  bench and lay it flat where it started, on its own side, bristles down, handle toward the front.
* Open the **sweeping gripper** and draw it clear of the brush.

**Check:** the brush lies flat on the bench where it started. The tray stands on its ledge where it started, and
nothing has spilled out of it.

**Expected state:** the bed is bare and clear. The clean plate lies on the plate rest. The part and the scrapings are
in the tray.

### Step 7: Reseat the plate

**Goal:** the plate is seated flat on the bed, square and against both locating pins, with both front corners clear
past the front of the bed.

#### 7.1 Take the plate again

* Bring both grippers to the plate's front corners on the plate rest. The **left gripper** goes onto the left front
  corner. The **right gripper** goes onto the right front corner.
* Close both grippers on the corners at the same time, flat on the plate.
* Lift the plate straight up off the plate rest, only high enough to clear it, and hold it level, print side up.

**Check:** both grippers hold a front corner, with the left gripper on the left. The plate is level and the print
side is still clean.

#### 7.2 Carry it in and set the back edge

* With **both grippers**, the **left gripper** on the left front corner and the **right gripper** on the right
  front corner, carry the plate level to the door opening, over the tray, and take it straight in from the front.
  Keep it level the whole way.
* Do not tilt it, do not swing it, and do not let it turn between the grippers. Do not let it touch the open door or
  the door sill.
* With **both grippers**, bring the plate's far edge up against the **two locating pins** at the back of the bed
  and set it down there first.

**Check:** the plate's far edge is against both locating pins. The plate is still level and square to the bed.

#### 7.3 Lower the front and press it flat

* With **both grippers**, lower the front edge of the plate straight down until the magnets take it.
* Let the magnets take it down. Do not drop it flat onto the bed and do not slap it down.
* Open both grippers and draw them off the front corners.
* With the **right gripper** closed, press the plate straight down flat at the front right, then the front middle,
  then the front left. That is **three presses**.
* Press straight down only. Do not press hard enough to move the printer.
* Draw both grippers straight out of the door opening, level.

**Check:** the plate is **seated flat**. It is down on the bed all over, square to it, back edge against both pins,
no corner lifted, both front corners standing clear past the front of the bed. If a corner is lifted or the plate
sits crooked, take the near corner with the **right gripper**, lift the front edge, and set it down again against the
pins.

**Expected state:** the clean plate is seated flat on the bare bed. Both arms are out of the printer. The door still
stands at its stop. The panel still reads the finished job.

### Step 8: Shut the front door

**Goal:** the door is **latched** shut and both arms are off it.

The swing runs backwards now: the **left gripper** brings the door in to the halfway point, then the **right gripper**
takes it home.

#### 8.1 Bring the door in to the halfway point

* Confirm both arms and the plate are out of the door opening and nothing is left inside the printer.
* With the **left gripper**, close on the door handle where it stands at the **door stop**.
* With the **left gripper**, carry the handle round to the right until it reaches the **halfway point** on the
  centre line.
* Stop the door at the halfway point and hold it still with the **left gripper** for half a second, so the door
  has stopped moving before it is let go.
* Only then open the **left gripper**, draw the left arm back, and hold it **clear of the front**.

**Check:** the door stands part shut at the halfway point and the left arm is off it. The door was still, not
swinging, when the left gripper opened. Nothing is trapped between the door and the frame.

#### 8.2 Close it until the catch takes

* With the **right gripper**, close on the door handle where it stands still at the halfway point.
* With the **right gripper**, carry it on round to the right until the door meets the frame, then press it straight
  back until the catch takes.
* Open the **right gripper** and draw it back off the door.
* Do not slam it. Do not press hard enough to move the printer.

**Check:** the door is **latched**. It meets the frame all round, sits flush with the front, and does not spring back
when the **right gripper** comes off it. If it stands ajar, close on the handle again with the **right gripper** and
press it straight back once more.

**Expected state:** the door is shut on a clean seated plate and a clear bed. Both arms are clear of the front.

### Step 9: Start the next job at the panel

**Goal:** the **top job** is running and both arms are clear of the front.

The panel is a touch screen. **Print**, the **top job**, and **Start** are **touch targets** drawn on that screen.
There is no physical button on the printer that this step uses. Every input in this step is one touch on the screen
with the **stylus tip** on the **right gripper**.

#### 9.1 Press the panel

* Confirm the door is latched. Do not start a job with the door open or ajar.
* With the **right gripper** closed, come straight in to the panel and press **Print**, straight in and level with the
  **stylus tip**.
* Draw the **right gripper** back off the panel. Then, with the **right gripper**, press the **top job** in the
  list the same way.
* Draw the **right gripper** back off the panel. Then, with the **right gripper**, press **Start** the same way.
* Press one target at a time, straight in, and draw the **right gripper** back off the panel between presses.
* Do not rest the gripper, wrist, or forearm on the panel. Do not press two targets at once.
* The **left arm stays at home** for the whole of this step.

**Check:** the panel shows the job name of the **top job**. If it shows another job, back out with the **right
gripper** and press **Print** and the top job again.

#### 9.2 Stand clear

* Draw both arms back **clear of the front** as soon as **Start** is pressed.
* Touch nothing after that: not the panel, not the door, not the bench. The printer heats and then runs its
  **levelling** on its own.

**Check:** the panel shows the **job running**. The printer has begun to heat. Both arms are clear of the front and
the bench.

**Expected state:** the next job is running behind a shut door on a clean seated plate. The part and the scrapings are
in the tray.

### Step 10: End the episode

* Confirm the plate. It is clean and seated flat on the bed, square, against both pins, with both front corners clear
  past the front of the bed.
* Confirm the bed. No debris is left on it and nothing is left inside the printer.
* Confirm the door. It is latched shut and sits flush with the front.
* Confirm the panel. The top job is running.
* Confirm the bench. The tray stands on its ledge holding the part and the scrapings. The scraper and the brush lie
  flat where they started.
* Confirm nothing has been dropped on the bench or the floor, and the top cover, the filament unit, and the feed tube
  have not been touched.
* Confirm the base has not moved and the printer has not shifted.
* Correct any failed check before ending.
* Return both arms home with grippers open. Then stop recording.

## After the episode: reset the workspace

This reset is not recorded.

1. Stop the job at the panel and let the bed cool back to its handling temperature.
2. Tip the part and the scrapings out of the debris tray, wipe the tray out, and stand it back on the tray ledge,
   empty and centred under the door sill.
3. Pick up anything that landed on the bench or the floor.
4. Open the door by hand. Take the plate off the bed. Check the print side is clean and flat, and check the front edge
   is straight and both front corners are firm and not bent.
5. Set the next job's finished part back on the plate for the next episode. Put the plate back on the bed against the
   locating pins, seated flat.
6. Wipe the bed clear. Check both locating pins are firm and upright, and check the bed still sits level with the door
   sill.
7. Shut the door by hand and check the catch holds it flush. Check it still swings to its stop and stands there on its
   own.
8. Lay the scraper flat on the bench beside the plate rest, on the side the next episode's config puts it, left for
   Config L and M, right for Config R, handle toward the front, blade away from the front.
9. Lay the brush flat on the bench beside the plate rest, on the side the next episode's config puts it, left for
   Config L, right for Config M and R, bristles down, handle toward the front.
10. Check the bench holds nothing but the tools for this config. Swing the door by hand to its stop and check it
    clears any tool lying to the left of the plate rest.
11. Check the top cover is seated, the filament unit stands square on it, and the feed tube runs clear of the arms'
    path.
12. Empty the purge chute bin behind the printer if it is full. This is bench work only and never happens on camera.
13. Replace a scraper whose blade has chipped, curled, or worn to an edge that digs into the plate.
14. Replace a brush whose bristles have splayed, hardened, or picked up plastic they will not release.
15. Replace a plate that has creased, that no longer springs flat, whose front edge has bent, or whose print side has
    been gouged.
16. Replace a tray whose walls have cracked or that no longer stands flat on its ledge.
17. Check the **right gripper's** stylus tip is still seated firm. Refit or replace it if it has shifted.
18. Check the panel shows a next job at the top of the list, and queue one if it does not.
19. Check the base is still locked and parked square. Then run the Base positioning steps and both Setup checklists
    again.

## SOP violations

These are actions that break the SOP and are reviewed side by side in the review tool.

### How to record a violation in review

For each violation, record the **start timestamp**, **violation name**, and **SOP rule broken**. The visible cue is
what the reviewer sees. The coaching note is for retraining and is not an annotation label.

### Episode handling

Tag every violation with its timestamp and name. Keep the episode with the violation tag. Do not delete it just
because a rule was broken.

### Violations

**Note on the tool side:** the violations below were written for Config R (scraper and brush on the right, worked
by the right gripper). The arm-role cues in them will be rewritten later to cover all three configs; they are left
as they are for now. Until then, anything that does not match the episode's config goes under **Config
misaligned**.

**Violation: Config misaligned**

* **Visible cue:** what the operator does does not match the config on the bench. A gripper reaches across the
  plate rest for the scraper or the brush; a tool is worked by the gripper on the other side; the plate is held
  down by the gripper on the scraper's side; the scraper or the brush is not where that config puts it; or the
  wrong IF line is followed in Step 5 or 6.
* **SOP rule broken:** the tool-side rule. The gripper on a tool's side takes it and works it, the other gripper
  holds the plate while it is scraped or stays home while the bed is swept, and the IF line followed is the one
  for the config on the bench.
* **Coaching note:** look where the scraper and the brush are before the plate comes down on the plate rest, then
  follow that config's IF lines through Steps 5 and 6.

**Violation: Base moved during the episode**

* **Visible cue:** the printer shifts in frame, the door opening changes angle or size in frame, or the base rolls,
  creeps, or turns at any point after recording starts.
* **SOP rule broken:** Steps 1 to 10. The base is parked and locked before recording and stays still for the whole
  episode.
* **Coaching note:** park it, lock it, push-test it, then start recording. A base that drifts is a lost episode.

**Violation: Wrong arm used or arms crossed**

* **Visible cue:** the **left gripper** takes the scraper, the brush, or the panel, pulls the door catch open, or touches the
  tray. The **right gripper** holds the plate down while it is scraped or carries the door past the halfway point.
  The left gripper goes to the right of the right gripper or takes the right front corner. The right gripper takes the
  left front corner. One arm reaches over, under, around, or past the other, or across the front of the other arm's
  body. Both grippers are on the door at once.
* **SOP rule broken:** Steps 2 to 9. Each action uses the gripper its step names: the **right gripper** works the door
  catch, the scraper, the brush, the press-downs, and the panel, the **left gripper** works the outer half of the door
  swing and holds the plate, and both take a front corner each for the two carries.
* **Coaching note:** right arm works, left arm holds, both arms carry the plate, one gripper on the door at a time. If
  you have to reach past the other arm, the wrong arm is doing the job.

**Violation: Approached from above or touched the top of the printer**

* **Visible cue:** a gripper comes down onto the bed from above instead of entering level from the front. Or a wrist,
  forearm, or the plate knocks, scrapes, or rests on the gantry, the top cover, the filament unit, the feed tube, or
  the shelf above on the way in or out.
* **SOP rule broken:** Steps 3, 6, 7, and 9. Every action at the printer is a front approach, level, in and out through
  the door opening, and nothing on top of the printer is ever touched.
* **Coaching note:** straight in from the front, straight out the same way. The box is closed on top; there is no way
  in from there.

**Violation: Leaned on or pushed the printer**

* **Visible cue:** a gripper, wrist, or forearm rests on the glass, the frame, the bed, the open door, or the panel.
  The printer rocks, slides, or turns on the bench. Or a press-down on the plate, a press on the door, or a press on
  the panel moves the machine.
* **SOP rule broken:** Steps 2 to 9. The printer carries no weight and is never pushed out of place.
* **Coaching note:** the arm holds itself up. Press only as hard as the magnets, the catch, or the screen need.

**Violation: Tended a printer that was not finished or not cool**

* **Visible cue:** an arm goes to the door or into the printer while the panel still shows a job running, while the bed
  still reads above its handling temperature, or while the toolhead is still moving.
* **SOP rule broken:** Step 1.1. Read the panel first. Only tend a printer whose job is finished, whose bed is cool to
  handle, and whose toolhead is parked and still.
* **Coaching note:** read the panel before the arms move. A moving toolhead will take a gripper with it.

**Violation: Door worked wrong**

* **Visible cue:** the door is opened or shut by one gripper alone through the whole swing. It is levered, snatched, or
  slammed. It is held by a gripper while the plate goes in or out. It is left short of its stop, so an arm or the plate
  fouls it. It drifts shut and is not reset. It is pushed past its stop. The changeover happens away from the halfway
  point, so an arm reaches across the front of the other one. A gripper lets go at the halfway point while the door
  is still moving, without the half-second hold, so the other gripper takes a swinging door. Or the door is left
  ajar against the frame and **Start** is pressed on it.
* **SOP rule broken:** Steps 2.1, 2.2, 8.1, 8.2, and 9.1. The **right gripper** pulls the catch open and works the half of
  the swing nearest the frame, the **left gripper** works the half nearest the stop, each gripper holds the door still
  at the halfway point for half a second before it lets go, only one gripper is on the door at a time, the door stands
  at its stop on its own while the printer is worked, and it is latched flush before the panel is pressed.
* **Coaching note:** right arm to the halfway point, hold it still, let go, then left arm to the stop. Let go before the
  other arm moves, and never let go of a door that is still swinging. A door short of its stop is a door the plate will
  hit, and a job that starts on an open door has to be thrown away.

**Violation: Plate taken by the wrong grip**

* **Visible cue:** one gripper alone lifts the plate. A gripper closes on the print side or on the part instead of a
  front corner. The two grippers close at different times. Or the plate is handed from one gripper to the other.
* **SOP rule broken:** Steps 3.1 and 7.1. Both grippers close on the front corners at the same time, the **left
  gripper** on the left corner and the **right gripper** on the right corner.
* **Coaching note:** both corners, closing together, every time. A plate held by one corner folds under its own weight.

**Violation: Print side touched**

* **Visible cue:** a gripper, wrist, or forearm touches the print side of the plate at any point. Or the plate is laid
  down print side down.
* **SOP rule broken:** Steps 3 to 7. No gripper ever touches the print side, and the plate is never turned over.
* **Coaching note:** front corners only, print side up, all the way through. Marks on the print side end up in the next
  job.

**Violation: Plate snapped or dragged off the bed**

* **Visible cue:** the plate is yanked or snapped up off the bed instead of coming up as the magnets release. It is
  dragged or slid across the bed. It is lifted at an angle from one side. Or it scrapes the bed or the locating pins on
  the way up.
* **SOP rule broken:** Step 3.2. Lift both front corners straight up together and only as fast as the magnets release,
  until the whole plate is off the bed.
* **Coaching note:** straight up, both corners, at the speed the magnets give you. Let the plate peel, do not rip it.

**Violation: Plate carried wrong**

* **Visible cue:** the plate tips out of level during a carry. It swings between the grippers. It turns between them. It
  strikes the door sill, the frame, or the open door. Or the part slides or falls off it while it is carried in or out.
* **SOP rule broken:** Steps 3.3, 4.1, 7.1, and 7.2. Carry the plate level and straight, lifting only high enough to
  clear the surface and drawing it straight in and out of the door opening.
* **Coaching note:** level, low, and slow, both ways.

**Violation: Bowed wrong or not over the tray**

* **Visible cue:** the plate is bowed fewer or more than two times. It is bowed the wrong way so the print side curves
  inward. It is bowed over the bench or over the printer instead of over the tray. It is bowed against the tray or the
  bench. Or it is bent far enough to crease.
* **SOP rule broken:** Steps 4.1 and 4.2. Hold the plate out over the tray and roll both wrists forward together twice,
  bowing only far enough to release the part.
* **Coaching note:** over the tray, print side out, twice, and no further than it takes. A creased plate is a scrapped
  plate.

**Violation: Part not landed in the tray**

* **Visible cue:** the part drops onto the bench, into the printer, or on the floor. It is left on the plate rest. Or the
  plate is drawn back off the tray before the part has landed.
* **SOP rule broken:** Step 4.3. Keep the plate over the tray until the loose part has slid off the far edge and landed
  in it.
* **Coaching note:** stay over the tray until you see it land.

**Violation: Plate not held while it is scraped**

* **Visible cue:** the **left gripper** is not pressing the left front corner down while the scraper works. It comes off
  the plate early. Or the plate slides, turns, or lifts on the plate rest during a pass.
* **SOP rule broken:** Steps 5.1 and 5.4. The **left gripper** presses the left front corner down on the bench from
  before the first pass until after the scraper is put back.
* **Coaching note:** hold it first, then scrape it. A plate that slides under the blade takes the blade off the bench.

**Violation: Scraped wrong**

* **Visible cue:** the **right gripper** closes on the scraper blade instead of its handle. The blade is tipped up on a
  corner or dug into the print side. A pass is pulled back toward the front with the blade still down. Fewer or more
  than three passes are made. The passes do not run the right third, the middle, and the left third. Or the blade runs
  over the left front corner or the **left gripper**.
* **SOP rule broken:** Step 5.3. Hold the blade flat and push it straight away from the front, once down the right
  third, once down the middle, and once down the left third, clear of the left gripper.
* **Coaching note:** flat blade, push away, three passes, right to left. A tipped blade gouges the plate.

**Violation: Plate left not clean**

* **Visible cue:** part, skirt, prime line, or anything raised is still on the print side when the plate goes back on the
  bed. Or scrapings are left on the plate rest instead of in the tray.
* **SOP rule broken:** Steps 5.3 and 5.4. The plate leaves the plate rest as a clean plate, with everything that came off
  it in the tray.
* **Coaching note:** look across the print side from the front before you pick it up. Anything raised will show up in the
  next job.

**Violation: Debris tray touched, moved, or knocked**

* **Visible cue:** a gripper closes on the tray, lifts it, slides it along its ledge, or knocks it out of place. The tray
  tips. Or the part or the scrapings fall out of it.
* **SOP rule broken:** Steps 4 to 6. The tray stands on its ledge under the door sill for the whole episode and neither
  gripper ever touches it.
* **Coaching note:** the tray is furniture, not a tool. Work over it and never on it.

**Violation: Bed swept wrong or left with debris**

* **Visible cue:** the **right gripper** closes on the brush bristles instead of its handle. The bed is swept side to side
  or front to back instead of back to front. Fewer or more than three pulls are made. A pull stops short of the door sill.
  Debris is swept toward the locating pins. Or plastic bits or strings are still on the bed when the plate goes back.
* **SOP rule broken:** Step 6.2. Pull the brush from the back edge over the door sill three times, once down the left
  third, once down the middle, and once down the right third, until the bed is clear.
* **Coaching note:** back to front, over the sill, three pulls. Anything left on the bed sits under the plate.

**Violation: Scraper or brush parked wrong**

* **Visible cue:** the scraper or the brush is left on the plate, on the bed, or inside the printer. It is dropped on the
  bench or the floor. It is laid down somewhere other than where it started. Or it is laid down blade toward the front,
  bristles up, or handle away from the front.
* **SOP rule broken:** Steps 5.4 and 6.3. Lay the scraper and the brush back flat on the bench where they started,
  handles toward the front, blade away from the front and bristles down.
* **Coaching note:** same spot, same way round, every time. A tool shut inside the printer meets the toolhead.

**Violation: Plate reseated wrong**

* **Visible cue:** the plate is set down without its far edge against both locating pins. It is dropped or slapped flat
  onto the bed. It is slid across the bed into place. It is left crooked or with a corner lifted. It is left with an edge
  hanging over the bed. Or fewer or more than three presses are made at the front.
* **SOP rule broken:** Steps 7.2 and 7.3. Set the far edge against both locating pins first, then lower the front until
  the magnets take it, then press it down flat at the front right, middle, and left.
* **Coaching note:** pins first, front down second, three presses third. The pins are what makes it square, and the
  printer feels the plate before it prints.

**Violation: Panel worked wrong or the wrong job started**

* **Visible cue:** the **right gripper** presses targets other than **Print**, the **top job**, and **Start**. It presses
  two targets at once. It rests on the panel between presses. It starts a job that is not the top job. Or the **left
  gripper** touches the panel.
* **SOP rule broken:** Step 9.1. The **right gripper** presses **Print**, then the **top job**, then **Start**, one target
  at a time, straight in and back off the panel between presses.
* **Coaching note:** three presses, right gripper only, always the job at the top of the list.

**Violation: Arms not clear when the job started**

* **Visible cue:** an arm stays over the bench, the panel, the door, or the door opening after **Start** is pressed. Or a
  gripper touches the printer, the plate, or the bench once the job is running and the printer is levelling.
* **SOP rule broken:** Step 9.2. Draw both arms back clear of the front as soon as **Start** is pressed and touch nothing
  after that.
* **Coaching note:** press Start and get out. The printer heats and feels its way over the plate next.

**Violation: Wrong order of work**

* **Visible cue:** an arm goes to the door before the panel is read. The plate is lifted before the door stands at its
  stop. The part is bowed off over the bench before the plate is over the tray. The plate is scraped before the part is
  off. The bed is swept before the plate is off it. The plate goes back before the bed is clear. The door is shut before
  the plate is seated. Or the job is started before the door is latched.
* **SOP rule broken:** Steps 1 to 9. Check the panel, open the door, lift the plate, bow the part off, scrape the plate,
  clear the bed, reseat the plate, shut the door, start the job.
* **Coaching note:** the order is the task. Every step leaves the station ready for the next one.

**Violation: Required check not followed**

* **Visible cue:** a check named in a step is skipped. Or a check is made and the fault it finds is left uncorrected: a
  catch that did not release, a door short of its stop, a part still on the plate, plastic still stuck after three
  passes, a bit left on the bed, a lifted corner, a crooked plate, a door left ajar, or the wrong job on the panel.
* **SOP rule broken:** Steps 1.1 to 9.2. Run each check and correct what it finds by the retry written in that step.
* **Coaching note:** a check is not done until what it found has been put right.

**Violation: Dropped or knocked over**

* **Visible cue:** the plate, the part, the scraper, or the brush is dropped on the bench, inside the printer, or on the
  floor. Or an arm knocks the toolhead, a locating pin, the tray, the open door, or the panel.
* **SOP rule broken:** Steps 3 to 9. Nothing is dropped or knocked out of its place, and every gripper leaves the door
  opening straight out to the front.
* **Coaching note:** check the path and the landing place before the arm moves, and come out the way you went in.

**Violation: Wrong episode ending**

* **Visible cue:** the episode ends with the plate off the bed, the plate not seated flat, debris on the bed, something
  left inside the printer, the door open or ajar, the part or the scrapings out of the tray, the scraper or the brush out
  of place, the job not running, an arm short of home, or a gripper not fully open.
* **SOP rule broken:** Step 10. Confirm the plate, the bed, the door, the panel, the bench, the drops, and the base. Then
  return both arms home with grippers open and stop recording.
* **Coaching note:** confirm first. Homing is the last thing the arms do.

### Failures that are not violations

These failures are not caused by how the task was run. Log them as system issues, discard the episode, and never use them
for coaching.

* **Recording stopped or paused during the episode** (recording system).
* **Camera dropped frames or lost its feed** (capture system).
* **Camera cannot read the bed, the print side of the plate, the door, or the panel**, so whether debris was left,
  whether the plate came clean, whether the door latched, or which target was pressed cannot be judged.
* **Hardware fault on an arm:** gripper failure, drift, controller caused collision, or motor error.
* **Stylus tip fault:** a tip that comes loose, slips on the gripper finger, or will not register a correct press on the
  panel.
* **Base fault:** a brake or lock that will not hold, or a base that rolls, creeps, or turns with the lock set.
* **Faulty printer:** one that will not start a job from a correct press sequence, that shows no job list, that reports an
  error the panel will not clear, that refuses to start with a correctly latched door, or whose toolhead moves while the
  panel shows the job finished.
* **Faulty door:** a door whose catch will not release under a correct pull, whose catch will not hold it shut, that will
  not stand at its stop, that drifts shut on its own, or whose hinge binds part way through the swing.
* **Faulty panel:** a screen that does not respond to a correct press, that responds where it was not pressed, or that is
  unreadable from the front.
* **Faulty bed:** magnets too weak to hold the plate flat, magnets so strong the plate cannot be peeled off in a correct
  lift, a bent locating pin, a bed that is not level, or a bed that has moved off the door sill height.
* **Tray ledge fault:** a ledge that will not hold the tray steady, or that sits the tray too high or too low for debris
  to fall over the door sill into it.
* **Defective plate:** one that arrives creased, that will not spring back flat after a correct bow, whose front edge has
  bent so a gripper cannot take a corner, or whose print side is already gouged.
* **Part will not release:** a part welded to the plate that neither two correct bows nor three correct scraper passes
  will free.
* **Door opening too tight:** an opening so low or so narrow that both grippers cannot carry the plate in and out level
  with the door at its stop, or cannot reach the back edge of the bed.
* **A place turns out to sit outside its arm's comfortable reach** with the base correctly parked, so the door handle at
  either end of its swing, a front corner of the plate, the scraper, the brush, the back edge of the bed, or a target on
  the panel cannot be reached without extending or folding the arm.

## Annotation subtasks (from SOP)

1. Read the panel and check the printer is finished and cool
2. Pull the front door open and swing it to the halfway point
3. Swing the front door out to its stop
4. Take both front corners of the build plate
5. Peel the plate up off the bed
6. Carry the plate out through the door opening
7. Hold the plate out over the debris tray
8. Bow the plate to free the part
9. Tip the part off into the tray
10. Lay the plate down on the plate rest and hold it
11. Take the scraper off the bench
12. Scrape one pass down the plate
13. Lay the scraper back on the bench
14. Take the brush off the bench
15. Pull one brush stroke across the bed
16. Lay the brush back on the bench
17. Carry the plate back in and set it against the locating pins
18. Press the plate flat on the bed
19. Bring the front door in to the halfway point
20. Close the front door until the catch takes
21. Press one target on the panel
22. Return both arms home and end the episode
