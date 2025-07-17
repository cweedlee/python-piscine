from time import gmtime, strftime, time

start = strftime("%B %-d, %Y", gmtime(0));
tm_f = strftime("%b %d %Y", gmtime(time()));

tm_f1 = f"{time():,}"


print(f"Seconds since {start}: {time():,.4f} or {time():.2e} in scientific notation");
print(tm_f)
