### 2884. 알람 시계 (2024.1.3) / B3
H, M = map(int, input().split());

# CASE 1.
M -= 45;

if (M < 0):
  # CASE 2.
  if (H == 0):
    H += 24;
  H -= 1;
  M += 60;

print(H, M);