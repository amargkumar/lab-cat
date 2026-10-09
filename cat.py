'''
This program prints stdin to the screen.
'''
import sys

def cat(file):
    # Read and write in chunks to maintain O(1) memory
    chunk_size = 8192  # 8KB chunks
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        sys.stdout.buffer.write(data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
