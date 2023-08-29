import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window()

meter = ttk.Meter(
    metersize=180,
    padding=5,
    amountused=0,
    metertype="semi",
    subtext="Percent Completed",
    interactive=True,
)
meter.pack()

app.mainloop()
