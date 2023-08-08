import asyncio
import time

#กำหนดฟังก์ชันอะซิงโครนัส hello() ที่จำลองการหน่วงเวลาโดยใช้ asyncio.sleep()
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

#ฟังก์ชัน main() สร้างสองงานด้วย asyncio.create_task() เพื่อเรียกใช้ฟังก์ชัน hello() พร้อมกัน
async def main():
    task1 = asyncio.create_task(hello(1))
    task2 = asyncio.create_task(hello(2))
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end - start:.2f} sec')

#ANS
#Tue Aug  8 19:40:56 2023 hello 1 started
#Tue Aug  8 19:40:56 2023 hello 2 started
#Tue Aug  8 19:41:00 2023 hello 1 done
#Tue Aug  8 19:41:00 2023 hello 2 done
#Time: 4.03 sec
