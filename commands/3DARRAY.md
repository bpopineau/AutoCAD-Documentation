# 3DARRAY (Command)

Creates nonassociative, 3D rectangular or polar arrays.

---

## Notes
- **Replaced by:** The enhanced [ARRAY](array.md) command, which allows creation of associative or nonassociative 2D/3D arrays.  
- **Legacy behavior:** 3DARRAY maintains the older, nonassociative functionality.  
- For **3D rectangular arrays**, you specify rows, columns, and levels (Z).  
- For **3D polar arrays**, you define the axis of rotation with any two points in space.  
- The entire selection set is treated as a single element in the array.  

---

## Prompts

### Select objects
Select the objects to array.  

### Rectangular
Copies objects in a matrix of rows (**X axis**), columns (**Y axis**), and levels (**Z axis**).  
- Must have at least two rows, two columns, or two levels.  
- Positive values generate arrays along positive X, Y, Z axes.  
- Negative values generate arrays along negative X, Y, Z axes.  

**Options:**  
- **Number of rows (---):** Number of repeats along the X axis.  
- **Number of columns (|||):** Number of repeats along the Y axis.  
- **Number of levels (...):** Number of repeats along the Z axis.  
- **Distance between rows (---):** Distance between base points along X axis.  
- **Distance between columns (|||):** Distance between base points along Y axis.  
- **Distance between levels (...):** Distance between base points along Z axis.  

### Polar
Copies objects around an axis of rotation.  
- The specified angle determines array spread around the axis.  
- Negative values produce clockwise rotation.  

**Options:**  
- **Number of items in the array:** Total objects.  
- **Angle to fill:** Angle between first and last object.  
- **Rotate arrayed objects?:**  
  - **Yes:** Rotates objects along axis.  
  - **No:** Keeps orientation constant.  
- **Center point of array:** Defines array center.  
- **Second point on axis of rotation:** Defines rotation axis direction.  

---

## Related
### Concepts
- [About Arrays](../concepts/about-arrays.md)  

### Reference
- [Commands for Working with Arrays](../reference/commands-for-working-with-arrays.md)
