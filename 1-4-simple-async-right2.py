#นำเข้าอะซิงโคลและนำเข้าเวลา
import asyncio
import time
#กำหนดฟังก์ชันแบบอะซิงโครนัส sleep() หน่วงเวลาแบบอะซิงโครนัส 1 วินาที
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
#ฟังก์ชันจะรอฟังก์ชัน sleep() ซึ่งจะหน่วงเวลา 1 วินาที การหน่วงเวลานี้เป็นการจำลองการทำงานแบบอะซิงโครนัส
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

    async def main():
        await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end - start:.2f} sec ')
