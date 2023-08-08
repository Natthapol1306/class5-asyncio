#นำเข้าอะซิงโคลและนำเข้าเวลา
import asyncio
import time
#กำหนดฟังก์ชันแบบอะซิงโครนัส sleep() หน่วงเวลาแบบอะซิงโครนัส 1 วินาที
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
#กำหนดผลรวมของฟังก์ชันอะซิงโครนัส (ชื่อ,ตัวเลข) ที่จากคำนวณผลรวมของรายการตัวเลขขณะพิมพ์แต่ละขั้นตอน ใช้ wait sleep() เพื่อแหน่วงเวลาระหว่างขั้นตอน
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
#asyncio ถูกสร้างขึ้นโดยใช้ asyncio.get_event_loop()
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')

#ANS
#Task A: Computing 0+1
#Time: 0.04
#Task A: Computing 1+2
#Time: 1.04
#Task A: Sum = 3

#Task B: Computing 0+1
#Time: 2.06
#Task B: Computing 1+2
#Time: 3.07
#Task B: Computing 3+3
#Time: 4.08
#Task B: Sum = 6

#Time: 5.10 sec
