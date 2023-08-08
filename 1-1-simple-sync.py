# 1-1 simply-sync.py
import time

#กำหนดฟังค์ชั่นSleep
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

#กำหนดฟังก์ชัน sum(ชื่อ,ตัวเลข)คำนวณผลรวมของรายการตัวเลข
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    #หลังจากการวนซ้ำ ผลรวมทั้งหมดจะถูกพิมพ์พร้อมกับชื่องาน
    print(f'Task {name}: Sum = {total}\n')

    start = time.time()
    #กำหนดเวลาเริ่มต้นโดยใช้ "time.time()"" เพื่อบันทึกเวลาเริ่มต้นของการดำเนินการสคริปต์
    tasks = [
        sum("A", [1, 2]),
        sum("B", [1, 2, 3]),
    ]
    end = time.time()
    print(f'Time: {end-start:.2f} sec')
