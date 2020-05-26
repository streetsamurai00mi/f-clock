# Fuzzy Clock
Shows you the approximate time by using words showing Fuzzy Time like 'Quarter Past Five'. It's a cool clock written in python.
## Just another polybar script
```
[module/f-clock]
type = custom/script
exec = python ~/.config/polybar/scripts/f-clock.py
tail = true
format-prefix = " "
format-foreground = ${color.fg}
format-background = ${color.module-bg}
format-padding = ${layout.module-padding}
```
