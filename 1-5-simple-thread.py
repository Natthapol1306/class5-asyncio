import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
#ฟังก์ชัน sum() จะสร้าง"ThreadPoolExecutor"ชื่อ _executorสูงสุด 2 เธรด ภายในลูป จะใช้ loop.run_in_executor()เพื่อเรียกใช้ฟังก์ชัน sleep() ภายในThreadPool
async def sum(name, numbers):
    _executo = ThreadPoolExecutor(2)
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await loop.run_in_executor(_executo, sleep)
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')

#Answer
#Task A: Computing 1+2Time: 1.01

#Time: 1.01
#Task A: Sum = 3

#Task B: Computing 3+3
#Time: 2.03
#Task B: Sum = 6

#Time: 3.03 sec
