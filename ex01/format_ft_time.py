import time
from datetime import datetime

# Time
sec_since_epoch = time.time() # Get the current time in seconds since the epoch
sec_1000s_sep = f"{sec_since_epoch:,.4f}"
sec_sci = f"{sec_since_epoch:.2e}"

# Date
date = datetime.now()
"""
%b: Outputs the abbreviated month name (e.g., Jan, Feb, Mar, etc.).
%m: Outputs the numeric month (e.g., 01 for January, 02 for February, 12 for December).
"""
formatted_date = f"{date:%b %d %Y}"

print(f"Seconds since January 1, 1970: {sec_1000s_sep} or {sec_sci} in scientific notation")
print(formatted_date)
