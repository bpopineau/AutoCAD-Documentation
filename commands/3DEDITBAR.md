# 3DEDITBAR (Command)

Reshapes splines and NURBS surfaces, including their tangency properties.

---

## Notes
- Provides grips for moving points and adjusting tangent magnitude and direction.  
- Works in the **U, V, and W** directions on NURBS surfaces.  

### Grips
- **Triangle grip:** Specifies the method for reshaping the selected object.  
- **Square grip:** Reshapes by moving the base point or changing tangent direction at the base point.  
  - Use axes to restrict movement to one axis.  
  - Use squares to restrict movement to one plane.  
- **Tangent arrow grip:** Adjusts the tangent magnitude at the base point.  
  - Lengthening flattens curvature.  
  - Arrow points in the direction of the surface’s U, V, or W axis.  

---

## Prompts

### Select a NURBS Surface or Curve to Edit
Specifies the object to be modified.  
- Valid: lines, arcs, circles, ellipses, elliptical arcs, polylines, helixes, splines, NURBS surfaces.  
- Non-surfaces may be converted to splines.  

### Select Point on Curve / NURBS Surface
Specifies a base point on the curve or surface. Changes are relative to this point.  

### Base Point
Specifies a new base point on the curve or NURBS surface.  

### Displacement
Specifies a new base point by projecting entered coordinates onto the curve or surface.  

### Undo
Cancels the previous change without exiting the command.  

### Exit
Cancels the current operation and returns to the previous prompt, or exits the command.  

---

## Related
### Concepts
- [About Modifying Splines](../concepts/about-modifying-splines.md)  
- [About Editing NURBS Surfaces](../concepts/about-editing-nurbs-surfaces.md)  

### Reference
- [3D Edit Bar Shortcut Menu](../reference/3d-edit-bar-shortcut-menu.md)  
- [Commands for Surface Editing](../reference/commands-for-surface-editing.md)
