# 3DMOVE (Command)

In a 3D view, displays the 3D Move gizmo to aid in moving 3D objects a specified distance in a specified direction.

---

## Notes
- The **3D Move gizmo** allows free movement or constrained movement along an axis or plane.  
- If `DEFAULTGIZMO` is set to **3D Move**, the gizmo is displayed automatically when selecting objects in a 3D visual style.  
- If the visual style is **2D Wireframe**, it temporarily switches to **3D Wireframe** for the duration of the command.  
- By default, the gizmo is placed at the center of the selected object(s).  
- The **3D Move Gizmo shortcut menu** provides options for aligning, moving, or switching to another gizmo.  
  - Example: **Align Gizmo With Object** aligns the gizmo to a face or object plane, constraining movement to that plane.  

---

## Prompts

### Select objects
Selects the 3D objects to move.  
- Press **Enter** after selecting.  
- The gizmo is displayed, and you can:  
  - **Move along an axis** — click an axis line.  
  - **Move along a plane** — click the area between axes.  

### Stretch point
Specifies the new location of the objects using the gizmo.  
- Drag and click to move dynamically.  

### Copy
Creates a copy of the selected objects instead of moving them.  
- Multiple copies can be created by continuing to specify new locations.  

### Base point
Specifies the base point of the 3D objects to move.  

### Second point
Specifies the destination point for the move.  
- Alternatively, move the cursor to indicate a direction and then enter a distance.  

### Displacement
Specifies a relative distance and direction using coordinate values at the command prompt.  

---

## Related
### Concepts
- [About Moving 3D Objects](../concepts/about-moving-3d-objects.md)  
- [About Moving, Rotating, and Scaling 3D Subobjects](../concepts/about-moving-rotating-and-scaling-3d-subobjects.md)  
- [About Moving, Rotating, and Scaling Faces on 3D Solids and Surfaces](../concepts/about-moving-rotating-and-scaling-faces-on-3d-solids-and-surfaces.md)  
- [About Using 3D Gizmos](../concepts/about-using-3d-gizmos.md)  

### Reference
- [3D Move Gizmo Shortcut Menu](../reference/3d-move-gizmo-shortcut-menu.md)  
- [Commands for Moving, Rotating, and Scaling 3D Objects](../reference/commands-for-moving-rotating-and-scaling-3d-objects.md)
