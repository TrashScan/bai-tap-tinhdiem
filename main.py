def tinh_diem_gpa(diem_so):
  """Chuyển điểm thang 10 sang GPA thang 4.

  Accepts a number or numeric string. Raises ValueError for invalid input.
  """
  try:
    diem = float(diem_so)
  except (TypeError, ValueError):
    raise ValueError("Giá trị điểm phải là số.")
  if diem < 0 or diem > 10:
    raise ValueError("Điểm phải trong khoảng 0 đến 10.")
  return round((diem / 10) * 4, 2)


def main():
  import sys

  if len(sys.argv) > 1:
    inp = sys.argv[1]
  else:
    inp = input("Nhập điểm (0-10): ").strip()

  try:
    gpa = tinh_diem_gpa(inp)
  except ValueError as e:
    print("Lỗi:", e)
    return

  print("Điểm GPA hệ 4 là:", gpa)


if __name__ == "__main__":
  main()