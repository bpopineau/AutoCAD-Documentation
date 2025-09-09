# Have You Tried: Rotate and Scale Objects by Reference

Specifying a base point and then an angle of rotation or a scale factor are the most common ways to rotate or scale an object. In most cases, this works fine, but you can also rotate or scale objects relative to two other points by using the **Reference** option.

---

## Using the Reference Option
The **Reference** option in the **ROTATE** and **SCALE** commands allows you to specify:  
- A **final angle of rotation** rather than an additional angle.  
- A **final length between two points** rather than a scale factor.  

---

## Rotate Objects by Reference
You can rotate objects to a new absolute angle without needing to know their current angle.  

**Example steps:**  
1. Draw a series of lines at any angle.  
2. On the ribbon, click **Home > Modify > Rotate**.  
3. Select the lines.  
4. Specify the start point of one line as the base point.  
5. At the prompt, enter **R** (Reference).  
6. For the first reference point, enter `@` or reuse the base point.  
7. Specify the second point to define the reference angle.  
8. Enter a new angle value (e.g., `0` for alignment with the X-axis).  

The objects are rotated to match the absolute angle specified.  

---

## Scale Objects by Reference
You can scale objects to match a new length instead of calculating a scale factor.  

**Example steps:**  
1. Draw a rectangle and dimension one side.  
2. On the ribbon, click **Home > Modify > Scale**.  
3. Select the rectangle.  
4. Specify the base point at a rectangle corner.  
5. At the prompt, enter **R** (Reference).  
6. For the reference length, enter `@` or reuse the base point.  
7. Specify the corner point on the same side.  
8. Enter a new length (e.g., `1.5`).  

The object scales based on the difference between the reference and new lengths.  

---

## Align Objects
The **ALIGN** command lets you move, rotate, and scale objects in one operation, based on geometry in a drawing.  

**Example steps:**  
1. On the ribbon, click **Home > Modify > Align**.  
2. Select the objects to align.  
3. Specify the first source point and first destination point.  
4. Specify the second source point and second destination point.  
   - These points move and rotate the objects.  
5. Optionally, specify a third point pair to rotate in 3D.  
6. At the prompt, choose whether to scale objects based on alignment points.  

---

## Related
- [About Rotating Objects](../concepts/about-rotating-objects.md)  
- [About Resizing or Reshaping Objects](../concepts/about-resizing-or-reshaping-objects.md)  
- [About Aligning Objects](../concepts/about-aligning-objects.md)  
- [Welcome to Have You Tried](../concepts/welcome-to-have-you-tried.md)  

### Tasks
- [To Rotate an Object to an Absolute Angle](../tasks/to-rotate-an-object-to-an-absolute-angle.md)  
- [To Scale an Object by Reference](../tasks/to-scale-an-object-by-reference.md)  
- [To Align Two Objects in 2D](../tasks/to-align-two-objects-in-2d.md)  

### Reference
- [Commands for Moving and Rotating Objects](../reference/commands-for-moving-and-rotating-objects.md)  
- [Commands for Resizing Objects](../reference/commands-for-resizing-objects.md)
