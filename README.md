# The Robot Apology

A two-line robot confession for the make.fun contest "The Robot Apology".

A household robot owns one small, exact mistake — it watered the plastic
plant for six weeks while the real fern beside it died of thirst — and
draws the lesson that mistake actually teaches: a full watering tray is
not a living plant, so now it checks for roots before it pours.

`main.py` holds the entry as a constant, checks it against the gate
(UTF-8, 1–400 characters, exactly two lines), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), and reads
the file back to verify.
