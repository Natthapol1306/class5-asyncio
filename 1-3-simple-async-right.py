import asyncio
import time
#กำหนดฟังก์ชันอะซิงโครนัส sleep()
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
#กำหนดฟังก์ชันอะซิงโครนัส sum(ชื่อ,ตัวเลข)
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

#ANSWER
#Task A: Computing 0+1
#Time: 0.01
#Task A: Computing 1+2
#Time: 1.02
#Task A: Sum = 3

#Task B: Computing 0+1
#Time: 2.03
#Task B: Computing 1+2
#Time: 3.05
#Task B: Computing 3+3
#Time: 4.06
#Task B: Sum = 6

#Time: 5.07 sec
