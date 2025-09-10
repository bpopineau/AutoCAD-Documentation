# About Command Macro Strings

Command macro strings are used to instruct AutoCAD which commands and system variables to execute along with any expected input allowed at the Command prompt. Special characters, DIESEL expressions, and AutoLISP programming code can also be included in a command macro string.

---

## Overview
You can create custom command macro strings that help to:
- Reduce repetitive tasks  
- Enforce CAD standards  
- Simplify workflows  

You define and edit command macro strings with the:
- Customize User Interface Editor (AutoCAD and AutoCAD LT for Windows)  
- Command Macro Editor (AutoCAD for Windows only; not supported in AutoCAD-based toolsets or AutoCAD LT)  
- Customize dialog box (AutoCAD for Mac OS only)  

---

## Command Macro String Basics
A command macro string is a series of commands and expected options and values with a specialized syntax, similar to the input you enter at the AutoCAD Command prompt.  

Examples:  
- Simple: CIRCLE  
- With special characters: ^C^C_.circle \1  

### Common Special Characters
- ^C — Press Esc key  
- . — Use the standard definition of a command  
- _ — Global/English name (for multi-language macros)  
- ; — Press Enter  
- \ — Pause for user input  
- (space) — Press Spacebar  

Note: AutoLISP is not available in AutoCAD LT for Mac OS, and ObjectARX is not available in AutoCAD LT for Windows or Mac OS.

---

## Example: Drawing a Circle
Command prompt sequence:  
Command: CIRCLE  
Specify center point...  
Specify radius: 5  

Macro string equivalent:  
CIRCLE;  
\  
5;  

### Macro Breakdown
1. ^C^C — Cancel current commands before starting  
2. ._CIRCLE; — Start the CIRCLE command  
3. \ — Prompt for center point  
4. 5; — Enter radius and complete command  

Alternate syntax (without semicolons):  
^C^C_.circle \5  

---

## Example: Using MOCORO
Command prompt sequence:  
Command: MOCORO  
Select objects...  
Base point...  
Copy...  
Rotate...  

Macro string equivalent:  
^C^C._MOCORO;  
\\;  
\;  
_C;  
\;  
_R;  
\;  
;  

---

## Key Practices
### Cancel the Active Command
Use ^C^C at the start to ensure no command is active.  
- ^C cancels most commands.  
- ^C^C handles dimension commands.  
- ^C^C^C may be required for some options (e.g., -LAYER).  

### Use Standard Commands
Prefix with . to force the standard definition, even if a command was redefined with UNDEFINE.  
Example: ._CIRCLE  

### Verify Macro Characters
- Spaces are significant: interpreted as pressing Spacebar or Enter.  
- Place semicolons (;) where Enter is required.  

### International Support
Use _ to ensure compatibility across languages.  
Example: ._COPY  

### Single Object Selection
Example macro:  
^C^C._erase single  

### Repeat Commands
Use a leading * to repeat until Esc is pressed.  
Examples:  
*^C^C._move single  
*^C^C._copy single  

### Terminate Macros
- ; = Enter  
- Ending with \ or ; prevents AutoCAD from adding a space automatically.  

### Suppress Echoes and Prompts
- ^P temporarily disables echoes/prompts  
- ^Q suppresses all prompts from Command Line history  

---

## Topics in This Section
- [About Special Control Characters in Command Macros](../concepts/about-special-control-characters-in-command-macros.md)  
- [About Pausing Macros for User Input](../concepts/about-pausing-macros-for-user-input.md)  
- [About Swapping User Interface Elements Using Macros](../concepts/about-swapping-user-interface-elements-using-macros.md)  
- [About Using Conditional Expressions in Macros](../concepts/about-using-conditional-expressions-in-macros.md)  
- [About Using AutoLISP in Macros](../concepts/about-using-autolisp-in-macros.md)  

Parent topic: [About Command Customization](../concepts/about-command-customization.md)  

---

## Related
### Concepts
- [About Command Customization](../concepts/about-command-customization.md)  
- [About User Interface Customization](../concepts/about-user-interface-customization.md)  

### Tasks
- [To Assign or Modify a Command Macro](../tasks/to-assign-or-modify-a-command-macro.md)
