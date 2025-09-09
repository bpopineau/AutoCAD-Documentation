# 3DFACE (Command)

Creates a three-sided or four-sided surface in 3D space.

---

## Notes
- After specifying the last two points of a 3D face, the command repeats automatically using those points as the first two points of the next 3D face.  
- Faces created with all four points on the same plane are planar and behave similarly to region objects.  
- When shaded or rendered, planar faces are filled.  
- Multiple 3D faces can be combined to model complex 3D surfaces.  

---

## Prompts

### First point
Defines the start point for the 3D surface.  
- Enter the remaining points in clockwise or counterclockwise order.  

### Second point
Defines the second point for the 3D surface.  

### Third point
Defines the third point for the 3D surface.  

### Fourth point
Defines the fourth point for the 3D surface.  

- The **Third point** and **Fourth point** prompts repeat until you press **Enter**.  
- Specify additional points at these repeating prompts to continue creating faces.  

### Invisible
Controls edge visibility.  
- Enter `I` (Invisible) before selecting the first point of an edge to make it invisible.  
- Invisible edges:  
  - Do not appear in wireframe presentations.  
  - Can hide material in line drawings.  
  - Remain visible in shaded renderings.  
- All edges of a 3D face can be made invisible, creating a phantom face.  

---

## Related
### Concepts
- [About Creating a Custom Mesh (Legacy)](../concepts/about-creating-a-custom-mesh-legacy.md)  
- [About Creating Meshes by Conversion](../concepts/about-creating-meshes-by-conversion.md)  
- [About Face Normals and Removing Hidden Surfaces](../concepts/about-face-normals-and-removing-hidden-surfaces.md)  
- [About Minimizing Intersecting and Coplanar Faces](../concepts/about-minimizing-intersecting-and-coplanar-faces.md)  

### Reference
- [Commands for Creating a Custom Mesh (Legacy)](../reference/commands-for-creating-a-custom-mesh-legacy.md)
