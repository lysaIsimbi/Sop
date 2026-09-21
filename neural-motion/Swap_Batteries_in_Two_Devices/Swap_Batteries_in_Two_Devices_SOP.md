# Swap Batteries in Two Devices SOP (1x Episode: 2 Devices)

Replace the AA cells in **two battery-powered devices** in one recorded episode using the two-arm
tabletop robot. The table begins with both devices in the start zone for this episode's config, a clear
work position in the center, a tray of four fresh AA cells at the front-right, and a spent-cell tote at the
back-right.

Work **one device at a time** through the full sequence: bring it into the work position, open the
battery door, take out both spent cells, fit two fresh cells with the flat end against the spring,
close the door, and press the power button to confirm the device shows power. Only then start the
second device.

The table is set up in one of three ways. Only the two devices move; the work position, the spent-cell
tote, and the finished row are in the same place in all three. The fresh-cell tray moves only in Config R,
where the devices take its corner.

* **Config L:** the devices are at the front-left, device 2 behind device 1.
* **Config M:** the devices are at the front-center, in front of the work position, device 2 to the right
  of device 1.
* **Config R:** the devices are at the front-right, device 2 behind device 1; the fresh-cell tray is at the
  front-left.

Where a step depends on the setup it says so on an **IF** line — look at the table and follow the line
that matches.

What stays constant across all sessions:

* **Start position:** the devices start at the front-left (**Config L**), the front-center (**Config M**)
  or the front-right (**Config R**). One config per episode, chosen before recording and never changed
  mid-episode.
* **Same-side rule:** the gripper on the devices' side brings each device into the work position — the
  left gripper in Config L and M, the right gripper in Config R. No arm reaches across the table.
* **Supply side:** the fresh-cell tray is at the front-right in Config L and M and at the front-left in
  Config R. The gripper on the tray's side takes each fresh cell and fits it, and the other gripper holds
  the device down meanwhile.
* **Fixed roles:** in every config the left gripper holds the device down while the door is opened and
  closed and while the spent cells come out, the right gripper opens and closes the door, carries every
  spent cell to the back-right tote, turns the device face up and presses the power button, and the left
  gripper parks each verified device in the back-left finished row.

## Setup

Complete both checklists before recording starts.

### Cell configuration

* **Environment camera:** 900 mm.
* **cell_type:** bimanual

### Hardware checklist

1. Cameras are on and recording.
2. The environment camera shows the full tabletop: both devices in the start zone for this episode's
   config, the center work position, the fresh-cell tray, the spent-cell tote, and the back-left finished
   row.
3. Both arms are at home with grippers open.
4. The table is clear except for the two devices, the fresh-cell tray, the spent-cell tote, and robot
   hardware.

### Materials checklist

1. Stage two devices of the same model in the start zone for this episode's config, both **face down**,
   so the battery door faces up, and leave the other two start zones clear:
   * **Config L:** front-left, **device 1** nearest the front edge and **device 2** behind it
   * **Config M:** front-center, in front of the work position, **device 1** on the left and **device 2**
     to its right
   * **Config R:** front-right, **device 1** nearest the front edge and **device 2** behind it, clear of
     the tote
2. Each device starts with two spent AA cells in place and its battery door closed.
3. Put four fresh AA cells in the shallow tray at the front-right (Config L and M) or at the front-left
   (Config R). Lay them side by side in one row, all in the same direction, with every button end pointing
   toward the right edge of the table.
4. Put the empty spent-cell tote at the back-right.
5. Keep the center work position clear and keep the back-left finished row clear.
6. Before collection, confirm that each battery door opens and stays open on its own, that a fresh
   cell drops into each bay without being forced, and that each device switches on with one press of
   its power button.

### Workspace layout

- **Start zone:** the two devices, face down, before they are worked — front-left (**Config L**),
  front-center (**Config M**), or front-right (**Config R**)
- **Center work position:** the one device being worked on
- **Supply zone:** tray of four fresh AA cells — front-right in Config L and M, front-left in Config R
- **Back-right waste zone:** spent-cell tote
- **Back-left finished row:** devices that have been swapped and verified, face up

### Arm assignments

- **Left gripper:** moves each device between the start zone, the work position, and the finished
  row, and steadies the device and holds its battery door clear while the right gripper works. In Config R
  it also takes each fresh cell from the front-left tray and fits it.
- **Right gripper:** opens and closes the battery door, takes out the spent cells, fits the fresh
  cells, turns the device face up, and presses the power button. In Config R it also brings each device
  from the front-right into the work position and holds the device down while the left gripper fits the
  fresh cells.

## Vocabulary

- **Battery door:** the cover on the back of the device that closes over the two cell bays. It swings
  open from one edge and stays open on its own once it is released.
- **Cell bay:** one of the two hollows under the battery door that a single AA cell lies in.
- **Front bay:** the cell bay nearer the front edge of the table with the device in the work position.
  It is filled first.
- **Back bay:** the other cell bay, farther from the front edge. It is filled second.
- **Spring end:** the end of a cell bay with the coiled metal spring in it.
- **Plate end:** the other end of a cell bay, with a flat metal contact.
- **Correct polarity:** the cell's **flat end** touches the spring and its **button end** touches the
  flat plate. This holds for each bay on its own, so the two cells may end up pointing opposite ways.
- **Spent cell:** a cell taken out of a device. Spent cells only ever go into the spent-cell tote.
- **Fresh cell:** a cell taken from the fresh-cell tray. Fresh cells only ever come from that tray.
- **Seated cell:** the cell lies flat along the bottom of its bay, sits below the rim of the bay, and
  does not rock when the gripper lets go.
- **Door closed:** the door lies flat against the device body all the way around, its latch holds, and
  no cell is visible.
- **Power button:** the main button on the face of the device that switches it on.
- **Shows power:** the device's light comes on or its screen lights up after the button press.
- **Work position:** the single spot in the center of the table where every device is worked, face
  down, with the battery door facing up.
- **Start zone:** where the two devices lie at the start of the episode — front-left (**Config L**),
  front-center (**Config M**), or front-right (**Config R**). One per episode, chosen before recording and
  never changed mid-episode.
- **Supply side:** the side of the table holding the fresh-cell tray — the right in Config L and M, the
  left in Config R. The gripper on that side takes and fits every fresh cell.

## Steps

Run Steps 1–6 for device 1, then run Step 7 to repeat them for device 2, then end the episode with
Step 8. Finish one device completely before touching the other one.

Steps 1 and 4 depend on the config: in Config L and M the **left gripper** brings each device in and the
**right gripper** takes the fresh cells from the front-right tray; in Config R the **right gripper** brings
each device in from the front-right and the **left gripper** takes the fresh cells from the front-left tray
and fits them while the right gripper holds the device down. Every other line is the same in all three.

### Step 1: Bring the next device into the work position

**Goal:** one device lies alone in the work position, face down, with its battery door facing up and
its door still closed.

Look where the devices are before reaching for the first one.

- **IF the devices are at the front-left (Config L):** with the **left gripper**, grasp the next device by
  its side — **device 1** first, **device 2** second — lift it, and carry it low over the table back and to
  the right into the center work position.
- **IF the devices are at the front-center (Config M):** with the **left gripper**, grasp the next device
  by its side — **device 1** first, **device 2** second — lift it, and carry it low over the table straight
  back into the center work position.
- **IF the devices are at the front-right (Config R):** with the **right gripper**, grasp the next device
  by its side — **device 1** first, **device 2** second — lift it, and carry it low over the table back and
  to the left into the center work position.

Then, in all three:

- Set it down face down, with the battery door facing up.
- Keep the other device in the start zone and do not open its door.
- Set the **left gripper** on the device, or resting against its side, and keep it there to hold the
  device still for the rest of the swap.

**Check:** one device sits flat in the work position with its battery door facing up and the other
device is untouched in the start zone. If the device sits crooked or rocks, set it flat again with
the left gripper before opening the door.

### Step 2: Open the battery door

**Goal:** the battery door is open and clear of both cell bays, and both spent cells are visible.

- With the **left gripper**, hold the device down against the table.
- With the **right gripper**, take hold of the free edge of the battery door and swing it open.
- Open the door far enough that both cell bays are fully clear, then release the door.
- If the door swings back over a bay, hold it clear with the **left gripper** while the right gripper
  works, and keep the left gripper's hold on the device.

**Expected state:** the door is open, both cell bays are in view, and both spent cells are still in
place.

**Check:** both bays are clear of the door and nothing is bent or cracked. If the door will not open
at a light pull, stop and end the episode rather than forcing it.

### Step 3: Take out both spent cells

**Goal:** both bays are empty and both spent cells are in the spent-cell tote.

1. With the **right gripper**, grasp the spent cell in the **front bay** across its barrel and lift it
   straight out.
2. Carry it to the back-right spent-cell tote and release it inside the tote.
3. With the **right gripper**, take the spent cell out of the **back bay** the same way and release it
   in the tote.
4. Carry one cell at a time. Do not lay a spent cell on the table or on the device.

**Check:** both bays are empty and both spent cells are inside the tote. If a spent cell lands outside
the tote, pick it up with the right gripper and put it in the tote before fitting any fresh cell.

### Step 4: Fit two fresh cells

**Goal:** one fresh cell is seated in each bay with correct polarity, front bay first.

#### 4.1 Fit the front bay

- **IF Config L or M:** with the **right gripper**, take one fresh cell from the front-right tray,
  grasping it across its barrel. **IF Config R:** the tray is at the front-left, so the **left gripper**
  takes the cell the same way and fits it while the **right gripper** holds the device down.
- Turn the cell so its **flat end** faces the spring end of the **front bay**.
- Lower the cell into the bay flat end first, press it lightly against the spring, and drop the button
  end onto the plate.
- Release the cell only when it lies flat in the bay.

#### 4.2 Fit the back bay

- **IF Config L or M:** with the **right gripper**, take a second fresh cell from the tray. **IF Config
  R:** the **left gripper** takes it from the front-left tray and fits it, as in 4.1.
- Turn the cell so its **flat end** faces the spring end of the **back bay**. This may point the cell
  the opposite way from the first one.
- Seat it the same way and release it.

**Check:** each bay holds one fresh cell, each cell's flat end touches the spring, each cell sits below
the rim of its bay, and no cell rocks. If a cell is reversed or riding high, lift it out with the
same gripper and fit it again before closing the door.

### Step 5: Close the battery door

**Goal:** the battery door is closed over both cells with nothing trapped.

- With the **left gripper**, keep holding the device down against the table.
- With the **right gripper**, swing the battery door back over both bays.
- Press the door down until it lies flat all the way around and its latch holds.

**Check:** the door is closed, no cell is visible, and no cell or door edge is trapped. If the door
lifts at a corner or will not latch, open it, check that both cells are seated, and close it again.

### Step 6: Verify with a button press and park the device

**Goal:** the device shows power after one press and then rests face up in the finished row.

1. With the **right gripper**, lift the near edge of the device and turn it over so it lies face up in
   the work position.
2. With the **right gripper**, press the power button and hold it for 2 seconds, then release.
3. Watch the device until it shows power.
4. If it does not show power: open the door, fit both cells again, close the door, and press once
   more. If it still does not show power after this one retry, end the episode and log a defective
   cell or device.
5. With the **left gripper**, move the verified device to the back-left finished row and set it down
   face up. Leave a device already in the row where it is.

**Check:** the device shows power, its door stays closed, and it rests face up in the finished row
without touching the other device.

### Step 7: Swap the second device

**Goal:** both devices have fresh cells and have shown power.

- Repeat Steps 1–6 for **device 2**.
- Take its two fresh cells from the same tray and put its two spent cells in the same tote.
- Do not move or press device 1 again.

**Check:** the finished row holds both devices face up, the tote holds four spent cells, and the
fresh-cell tray is empty.

### Step 8: End the episode

**Goal:** recording ends after both devices have been swapped and verified.

1. Confirm both devices rest face up in the finished row with their doors closed, the tray is empty,
   the four spent cells are in the tote, and the work position is clear.
2. Return both arms home with grippers open. Homing is the last thing the arms do.
3. Stop recording.

## After the episode: reset the workspace

All reset work happens with recording off.

1. Switch both devices off.
2. Take the two fresh cells out of each device and set them aside for charging or disposal.
3. Empty the spent-cell tote and put it back empty at the back-right.
4. Restock the tray with four fresh AA cells, laid side by side in one row with every button end
   pointing toward the right edge of the table, and put it at the front-right for the next episode's
   config (Config L or M) or at the front-left (Config R).
5. Put two spent AA cells back in each device, close both doors, and confirm each door latches.
6. Inspect both devices, their doors, latches, springs, contacts, the tray, and the tote. Replace
   anything bent, cracked, corroded, or leaking.
7. Stage both devices face down with the battery door facing up in the start zone for the next
   episode's config — front-left, device 2 behind device 1 (Config L), front-center in front of the work
   position, device 2 to the right of device 1 (Config M), or front-right, device 2 behind device 1
   (Config R) — leaving the other two start zones clear.
8. Confirm the work position and the finished row are clear, then run both Setup checklists.

## SOP violations

Things that break this SOP and that reviewers look for in the side-by-side review tool.

### How to record a violation in review

For every violation seen in a recorded episode, record:

- the **start timestamp** in the video;
- the **violation name** from the list below; and
- the **SOP rule broken**, including the step number.

The visible cue is what the reviewer sees. The coaching note is for retraining and is not an
annotation label.

### Episode handling

Tag every violation with its timestamp and name. An episode may contain multiple violations; tag each
separately. Retain the episode in training data with its violation tags. Do not delete a recorded
episode solely because it contains a violation.

### Violations

**Note on the start position:** the violations below were written for Config L (devices start at the
front-left and the fresh-cell tray is at the front-right). The pickup and arm-role cues will be rewritten
later to cover all three start positions; they are left as they are for now. Until then, anything that
does not match the episode's config goes under **Config misaligned**.

**Violation: Config misaligned**
- **Visible cue:** what the operator does does not match the config on the table — the devices or the
  fresh-cell tray are not in the zones for the config; a gripper reaches across the table for a device or
  a fresh cell; in Config R the right gripper takes a fresh cell, or the left gripper fits one with no
  gripper holding the device down; or the wrong IF line is followed.
- **SOP rule broken:** the start position, the same-side rule, and the supply side (the gripper on the
  devices' side brings each device in; the gripper on the tray's side takes and fits each fresh cell while
  the other gripper holds the device; no arm reaches across the table; the IF line followed is the one for
  the config on the table).
- **Coaching note:** look where the devices and the tray are before the first reach, then follow that
  config's IF lines through Steps 1 and 4.

**Violation: Both devices worked at once**
- **Visible cue:** the second device's door is opened, or its cells are handled, before the first
  device has shown power and reached the finished row.
- **SOP rule broken:** Steps 1 and 7 (finish one device completely, then start the other).
- **Coaching note:** one device at a time, all the way through the button press.

**Violation: Device not steadied**
- **Visible cue:** the left gripper is away from the device while the right gripper works the door or
  the cells, and the device slides, spins, or is chased across the table.
- **SOP rule broken:** Steps 2–5 (the left gripper holds the device down while the right gripper
  works).
- **Coaching note:** set the left gripper on the device first, then work with the right gripper.

**Violation: Battery door mishandled**
- **Visible cue:** the right gripper pries the door at a fixed edge, forces a door that does not
  open, bends or snaps the door, or leaves the door swinging over a bay while cells are handled.
- **SOP rule broken:** Step 2 (open the door at its free edge, clear both bays, and hold the door
  clear with the left gripper if it swings back).
- **Coaching note:** open at the free edge, park the door clear, and stop rather than forcing it.

**Violation: Spent cell left in the device**
- **Visible cue:** a fresh cell is fitted into a bay that still holds a spent cell, or the door is
  closed with only one cell replaced.
- **SOP rule broken:** Step 3 (empty both bays before fitting any fresh cell).
- **Coaching note:** empty both bays first, then fit two fresh cells.

**Violation: Spent cell mishandled**
- **Visible cue:** a spent cell is laid on the table or on the device, lands outside the tote and is
  left there, is dropped into the fresh-cell tray, or goes back into a device.
- **SOP rule broken:** Step 3 (carry one spent cell at a time straight into the spent-cell tote).
- **Coaching note:** every spent cell goes into the tote, and nothing comes back out of it.

**Violation: Wrong cells used**
- **Visible cue:** more or fewer than two fresh cells go into one device, a cell is taken from the
  tote instead of the tray, or a fresh cell is carried and set down somewhere before its bay.
- **SOP rule broken:** Step 4 (fit exactly two cells taken from the front-right tray, one per bay).
- **Coaching note:** two cells per device, straight from the tray into the bay.

**Violation: Wrong polarity**
- **Visible cue:** a cell's button end is pressed against the spring, or its flat end sits against the
  flat plate, and the door is closed that way.
- **SOP rule broken:** Step 4 (the flat end touches the spring in each bay).
- **Coaching note:** check the flat end against the spring in each bay before releasing the cell.

**Violation: Cell not seated or bays filled out of order**
- **Visible cue:** a cell rides above the rim of its bay, sits at an angle, rocks when the right
  gripper lets go, or the back bay is filled before the front bay.
- **SOP rule broken:** Step 4 (seat the front bay first, then the back bay, with each cell flat and
  below the rim).
- **Coaching note:** front bay first, and press each cell flat before letting go.

**Violation: Door not closed**
- **Visible cue:** the door is left open, lifts at a corner, does not latch, traps a cell or its own
  edge, or the power button is pressed with the door still open.
- **SOP rule broken:** Step 5 (close the door flat and latched over both cells before the button
  press).
- **Coaching note:** press the door flat and confirm the latch holds before pressing the button.

**Violation: Verify press skipped or not confirmed**
- **Visible cue:** no power button press, a press on some other control, or the device is moved to the
  finished row without showing power.
- **SOP rule broken:** Step 6 (press the power button, hold 2 seconds, and watch the device show power
  before parking it).
- **Coaching note:** one press, then wait and look for the light or screen before moving on.

**Violation: Finished device parked wrong**
- **Visible cue:** a verified device is left in the work position or the staging zone, set on the tray
  or tote, set face down, or pushes the other finished device out of place.
- **SOP rule broken:** Step 6 (set the verified device face up in the back-left finished row and leave
  a device already there alone).
- **Coaching note:** park each finished device face up in the row with clear space around it.

**Violation: Device or supply knocked over**
- **Visible cue:** a device, the tray, or the tote is dropped, tipped, or pushed off its spot, or
  cells scatter on the table.
- **SOP rule broken:** Steps 1–7 (keep the devices, tray, and tote in their zones through the swap).
- **Coaching note:** work slower over the table and keep carries short and low.

**Violation: Wrong arm used**
- **Visible cue:** an action assigned to one gripper is done by the other, including the left gripper
  fitting a cell or pressing the power button, or the right gripper carrying a device between zones.
- **SOP rule broken:** Steps 1–7 (the left gripper moves and steadies the device; the right gripper
  works the door, the cells, and the button).
- **Coaching note:** left gripper holds and carries, right gripper does the swap and the press.

**Violation: Wrong episode ending**
- **Visible cue:** recording stops before both devices are swapped, verified, and parked, an arm is
  not home, a gripper is closed, or an arm does something else after homing.
- **SOP rule broken:** Step 8 (confirm the finished state, return both arms home with grippers open as
  their final action, then stop recording).
- **Coaching note:** confirm first. Homing is the last thing the arms do.

### Non-violation failures

Failures not caused by task execution are system issues. Log and discard the episode rather than
tagging them as SOP violations.

- Recording stops or pauses during the episode.
- A camera drops frames or loses its feed.
- An arm or gripper fails, drifts, or reports a motor error.
- A fresh cell is dead, so the device does not show power with correctly fitted cells.
- A device is faulty, or its door, latch, spring, or contact is broken.

## Annotation subtasks (from SOP)

1. Move one device from the staging zone into the work position, face down
2. Open the battery door and clear both cell bays
3. Take both spent cells out and drop them in the spent-cell tote
4. Fit one fresh cell in the front bay, then one in the back bay, flat end against the spring
5. Close the battery door until it latches
6. Turn the device face up and press the power button to confirm it shows power
7. Move the verified device to the finished row
8. Repeat the swap for the second device
9. Confirm the end state, return both arms home, and end the episode
