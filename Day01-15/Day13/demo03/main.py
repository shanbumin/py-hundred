# 接下来我们将重点放在如何实现两个进程间的通信。
# 我们启动两个进程，一个输出Ping，一个输出Pong，两个进程输出的Ping和Pong加起来一共10个。
# 听起来很简单吧，但是如果这样写可是错的哦。

from multiprocessing import  Process
from time import sleep


counter=0

def sub_task(string):
    global counter
    while counter <10:
        print(string,end='',flush=True)
        counter +=1
        sleep(0.01)



def main():
    Process(target=sub_task,args=('Ping',)).start()
    Process(target=sub_task,args=('Pong',)).start()


if __name__ == '__main__':
    main()


# 看起来没毛病，但是最后的结果是Ping和Pong各输出了10个，Why？
# 当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进程有自己独立的内存空间，这也就意味着两个子进程中各有一个counter变量，所以结果也就可想而知了。
# 要解决这个问题比较简单的办法是使用multiprocessing模块中的Queue类，它是可以被多个进程共享的队列，底层是通过管道和信号量（semaphore）机制来实现的，有兴趣的读者可以自己尝试一下。