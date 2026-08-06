import time

start = time.perf_counter()

time.sleep(2)

print(start)

end = time.perf_counter()

print(end)

print(f"{end - start:.2f}")

start = time.perf_counter()
print(start)