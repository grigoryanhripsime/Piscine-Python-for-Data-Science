from datetime import datetime
import time

seconds = time.time()
formatted_seconds = f"{seconds:,.4f}"
scientific = f"{seconds:,.2e}"

print(f"Seconds since January 1, 1970: {formatted_seconds}  or {scientific} in scientific notation")

current_date = datetime.now()
print(current_date.strftime("%b %d %Y"))
