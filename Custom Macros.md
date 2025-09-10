# Custom Macros

Personal collection of custom AutoCAD command macro strings. See `Macros Guide.md` and related concept files for background on syntax, special characters, and best practices.

---
## Multiple Polyline Fillet (Radius 12, Repeating)

### Goal
Repeatedly apply a fillet with radius 12 to selected 2D polylines without re‑entering options each time.

### Macro String
```
*^C^C._FILLET _R 12 _P 
```

### Breakdown
- `*` Repeat the entire macro until you press Esc (keeps invoking FILLET).
- `^C^C` Cancel any active command(s) to start clean.
- `._FILLET` Call the standard (.) global (_) FILLET command.
- `_R 12` Set the fillet Radius option to 12 (ensures consistent radius every cycle).
- `_P` Invoke the Polyline option so the next selection applies fillets to all corners of one 2D polyline.
- `\` Pause for user input (select the polyline). After completion the command ends and the leading `*` restarts it.

### Usage
1. Run the macro (assign it to a custom button / CUI element / ribbon).  
2. Select a 2D polyline when prompted.  
3. Fillets are applied to all eligible corners with radius 12.  
4. Automatically restarts; continue selecting more polylines.  
5. Press Esc to stop.

### Notes
- Order matters: Radius is set before selecting Polyline so the correct value is applied.
- If you only need to set the radius once per session, you could omit `_R 12` for faster repetition after the first run.
- To use a different radius, edit the numeric value; for a variable radius you could create variants (e.g., 6, 24) as separate macros.
- Ensure objects are true 2D polylines; segments that cannot be filleted (e.g., too short relative to radius) may be skipped.

### Variations
| Purpose | Macro |
|---------|-------|
| Different radius (e.g., 6) | `*^C^C._FILLET _R 6 _P \` |
| Use current radius (don’t reset) | `*^C^C._FILLET _P \` |
| Force trim mode ON first | `*^C^C._FILLET _T _R 12 _P \` |

### Troubleshooting
- If nothing happens, confirm the entity is a single 2D polyline (use PEDIT to convert/join if needed).  
- If the radius is larger than some corner geometry, AutoCAD may be unable to create the arc there. Reduce radius and retry.  
- If the macro appears to “stall,” you might still be in object selection; press Enter to finish or Esc to cancel.

---
## Planned Macros
(Add new custom macros below this line using the same structure.)

- (Placeholder) Batch layer isolate & restore
- (Placeholder) Set dimension style & annotate

---
Parent topics for reference:
- See `Macros Guide.md`
- See `concepts/about-special-control-characters-in-command-macros.md`
- See `concepts/about-pausing-macros-for-user-input.md`
