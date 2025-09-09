# About Moving Objects

You can move objects at a specified distance and direction from the originals.

Use coordinates, grid snap, object snaps, and other tools to move objects with precision.

---

## Specify Distance with Two Points
Move an object using the distance and direction specified by a base point followed by a second point.  

In this example, you move the block representing a window:  
1. Select the object to be moved.  
2. Specify the base point for the move.  
3. Specify a second point.  

The object is moved the distance and direction of point 2 to point 3.  

---

## Use a Stretch-Move
You can also use **STRETCH** to move objects if all their endpoints lie entirely within the selection window.  

- Turn on **Ortho mode** or **polar tracking** to move the objects at a specific angle.  
- A common example is moving a door in a wall. The door is entirely within a crossing selection, while the wall lines are only partly within the crossing selection area.  

The result is that only the endpoints inside the crossing selection move.  

---

## Drag, Grip-Edit, or Nudge Objects
Move selected objects quickly by dragging, grip-editing, or nudging.

- **Drag** objects within a drawing, or between open drawings and other applications.  
  - Dragging with the right mouse button lets you specify whether to move, copy, or create a block from the dragged objects.  
  - Dragging disregards all snap settings.  

- **Nudge** objects in orthogonal increments with **Ctrl + arrow keys**.  
  - With **Snap mode off**: moves two pixels at a time, relative and orthogonal to the screen.  
  - With **Snap mode on**: moves by the snap spacing, orthogonal to the X and Y axes of the UCS and relative to the view direction.  

---

## Related
- [About Aligning Objects](../concepts/about-aligning-objects.md)  

### Tasks
- [To Move an Object Using a Displacement](../tasks/to-move-an-object-using-a-displacement.md)  
- [To Move Objects Using Two Points](../tasks/to-move-objects-using-two-points.md)  
- [To Move Objects With the Stretch Command](../tasks/to-move-objects-with-the-stretch-command.md)  
- [To Cut Objects](../tasks/to-cut-objects.md)  

### Reference
- [Commands for Moving and Rotating Objects](../reference/commands-for-moving-and-rotating-objects.md)
