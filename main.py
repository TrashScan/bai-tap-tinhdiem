def tinh_diem_gpa(diem_so):
  return round((diem_so / 10) * 4, 2)

print("Điểm GPA hệ 4 là:", tinh_diem_gpa(8.5))