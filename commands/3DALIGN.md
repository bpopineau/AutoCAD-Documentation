# 3DALIGN

- **Type:** Command  

Aligns objects with other objects in 2D and 3D.

---

## Usage
Specify up to three points on the object to be aligned, then specify up to three corresponding destination points.  
Selected objects are moved and rotated so that their base point and axes align in 3D space with the destination.

3DALIGN supports **Dynamic UCS (DUCS)**, allowing objects to be dragged interactively and aligned to the face of a solid.

---

## Prompts

### Select objects
Select one or more objects to align.  

### Base point
Specifies a base point on the source object.  

### Second point
Defines a point on the source object’s X axis.  
This sets a new X axis direction within a plane parallel to the XY plane of the current UCS.  

### Third point
Specifies a point on the object’s positive XY plane.  
This sets the orientation of the X and Y axes of the source object.  

---

## Options

- **Continue**  
  Skips directly to destination point prompts. Use when the source X and Y axes should stay parallel with the UCS.

- **Copy**  
  Creates and aligns a copy of the source object instead of moving it.

---

## Destination Points

- **First destination point**  
  Defines the target location of the base point.  
  > Tip: With DUCS on, you can define a destination plane by clicking a single point on a solid face.

- **Second destination point**  
  Specifies the X axis direction at the destination, within a plane parallel to the XY plane of the UCS.

- **Third destination point**  
  Sets the X and Y orientation of the destination plane.

- **Exit**  
  Sets the X and Y axes of the destination to remain parallel with the UCS.

---

## Related
- [About Aligning Objects](../concepts/about-aligning-objects.md)  
- [Commands for Moving and Rotating Objects](../reference/commands-for-moving-and-rotating-objects.md)
