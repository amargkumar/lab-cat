'''
This program prints stdin to the screen using O(1) memory.
'''
import sys

def cat(file):
    while True:
        chunk = file.read(4096)  # Read in 4KB chunks
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
