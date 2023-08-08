import asyncio
import time

#กำหนดฟังก์ชันอะซิงโครนัส hello() ที่จำลองการหน่วงเวลาโดยใช้ asyncio.sleep()
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

#ฟังก์ชัน main() สร้างรายการของวัตถุ coroutine และใช้ asyncio.gather()
async def main():
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end - start:.2f} sec')

#ANS
#Tue Aug  8 19:48:29 2023 hello 0 started
#Tue Aug  8 19:48:29 2023 hello 1 started
#Tue Aug  8 19:48:29 2023 hello 2 started
#Tue Aug  8 19:48:29 2023 hello 3 started
#Tue Aug  8 19:48:29 2023 hello 4 started
#Tue Aug  8 19:48:29 2023 hello 5 started
#Tue Aug  8 19:48:29 2023 hello 6 started
#Tue Aug  8 19:48:29 2023 hello 7 started
#Tue Aug  8 19:48:29 2023 hello 8 started
#Tue Aug  8 19:48:29 2023 hello 9 started
#Tue Aug  8 19:48:33 2023 hello 0 done
#Tue Aug  8 19:48:33 2023 hello 2 done
#Tue Aug  8 19:48:33 2023 hello 6 done
#Tue Aug  8 19:48:33 2023 hello 9 done
#Tue Aug  8 19:48:33 2023 hello 8 done
#Tue Aug  8 19:48:33 2023 hello 5 done
#Tue Aug  8 19:48:33 2023 hello 7 done
#Tue Aug  8 19:48:33 2023 hello 4 done
#Tue Aug  8 19:48:33 2023 hello 1 done
#Tue Aug  8 19:48:33 2023 hello 3 done
#Time: 4.03 sec
