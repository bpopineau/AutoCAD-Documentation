# 3DMESH (Command)

Creates a free-form polygon mesh.

---

## Notes
- Mesh density is controlled by a matrix of **M** and **N** vertices (rows × columns).  
- Designed primarily for program control rather than manual entry.  
- For smoothing, creasing, and refinement, use the modern [MESH](./mesh.md) command.  
- 3DMESH polygon meshes are always open in both **M** and **N** directions.  
  - Use **PEDIT** to close a mesh.  

---

## Prompts

### Size of mesh in M direction
Specifies the number of vertices in the **M** direction.  
- Value range: **2 to 256**  

### Size of mesh in N direction
Specifies the number of vertices in the **N** direction.  
- Value range: **2 to 256**  

- The product `M × N` equals the total number of vertices that must be specified.  

### Location for vertex (0, 0)
Defines the coordinate location of a vertex.  
- Enter a 2D or 3D coordinate.  
- Vertices are specified row by row:  
  - Begin with vertex **(0,0)**.  
  - Complete row `m` before starting row `m + 1`.  
- Vertices can be any distance apart.  
- The **M** and **N** orientation depends on vertex placement.  

---

## Related
### Concepts
- [About Creating a Custom Mesh (Legacy)](../concepts/about-creating-a-custom-mesh-legacy.md)  

### Reference
- [Commands for Creating a Custom Mesh (Legacy)](../reference/commands-for-creating-a-custom-mesh-legacy.md)
