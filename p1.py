# main.py
import sys

def main():
    n = int(sys.stdin.read().strip())
    # 0 始まりにした上で 10bit の2進数にし、0→'4', 1→'7' に対応付け
    k = n - 1
    bits = f"{k:010b}"
    ans = ''.join('7' if b == '1' else '4' for b in bits)
    print(ans)

if __name__ == "__main__":
    main()
