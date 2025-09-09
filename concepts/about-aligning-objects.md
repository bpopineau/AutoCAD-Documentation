# About Aligning Objects

You can move, rotate, or tilt an object so that it aligns with another object.

---

## Aligning in 2D
In 2D, use the **ALIGN** command with two pairs of points.  
For example, endpoint object snaps can precisely align piping in a drawing.  

---

## Aligning in 3D
In 3D, use the **3DALIGN** command to specify up to three points to define the source plane, followed by up to three points to define the destination plane.

- The **first source point** (base point) always moves to the first destination point.  
- A **second point** (source or destination) rotates the selected objects.  
- A **third point** (source or destination) applies further rotation.  

> Tip: With 3D solids, turn on **Dynamic UCS (DUCS)** to quickly select the destination plane.  

⚠️ **Note:** 3D alignment is not available in AutoCAD LT.  

---

## Related
- [About Moving Objects](../concepts/about-moving-objects.md)  
- [Have You Tried: Rotate and Scale Objects by Reference](../concepts/have-you-tried-rotate-and-scale-objects-by-reference.md)  

### Tasks
- [To Align Two Objects in 2D](../tasks/to-align-two-objects-in-2d.md)  
- [To Align Two Objects in 3D](../tasks/to-align-two-objects-in-3d.md)  

### Reference
- [Commands for Moving and Rotating Objects](../reference/commands-for-moving-and-rotating-objects.md)
