import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window()

meter = ttk.Meter(
    metersize=100,
    padding=5,
    amountused=0,
    metertype="semi",
    subtext="Percent of Exercises Completed",
    interactive=True,
)
meter.pack()


app.mainloop()
