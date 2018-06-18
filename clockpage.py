NUMBER_OF_FRAMES = 3
paging_seq = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]


frames = [0 for _ in range(NUMBER_OF_FRAMES)]
ref = [0 for _ in range(NUMBER_OF_FRAMES)]
clock_hand = 0
faults = 0

for i in range(0, len(paging_seq), 1):
    fault_happened = False
    if paging_seq[i] not in frames:
        fault_happened = True
        faults += 1
        while ref[clock_hand] != 0:
            ref[clock_hand] = 0
            clock_hand = (clock_hand + 1) % NUMBER_OF_FRAMES
        frames[clock_hand] = paging_seq[i]
        ref[clock_hand] = 1
        clock_hand = (clock_hand+1) % NUMBER_OF_FRAMES
    elif paging_seq[i] in frames:
        found_at = frames.index(paging_seq[i])
        ref[found_at] = 1

    print("\nFRAMES: %s\tClockHand: %d\nREFBIT: %s\t%s" %
          (frames, clock_hand, ref, ("fault" if fault_happened else "no fault")))

print("\nFaults: %d" % faults)
