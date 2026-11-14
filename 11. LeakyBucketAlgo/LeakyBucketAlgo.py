
# Leaky Bucket Algorithm

bucket_size = int(input("Enter the bucket size: "))
process_rate = int(input("Enter the processing rate: "))
n = int(input("Enter the number of seconds: "))

packets = []

for i in range(n):
    packet = int(input(f"Enter the size of the packet entering at {i+1} sec: "))
    packets.append(packet)

count = 0

print("\nSecond | Received | Sent | Packet Left | Dropped")
print("------------------------------------------------")

for i in range(n):
    received = packets[i]
    count += received

    dropped = 0

    if count > bucket_size:
        dropped = count - bucket_size
        count = bucket_size

    sent = min(count, process_rate)
    count -= sent

    print(f"{i+1:6} | {received:8} | {sent:4} | {count:11} | {dropped:7}")

# Process remaining packets
i = n

while count > 0:
    sent = min(count, process_rate)
    count -= sent

    print(f"{i+1:6} | {0:8} | {sent:4} | {count:11} | {0:7}")
    i += 1
