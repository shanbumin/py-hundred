
# 因为多个线程可以共享进程的内存空间，因此要实现多个线程间的通信相对简单，大家能想到的最直接的办法就是设置一个全局变量，多个线程共享这个全局变量即可。
# 但是当多个线程共享同一个变量（我们通常称之为“资源”）的时候，很有可能产生不可控的结果从而导致程序失效甚至崩溃。
# 如果一个资源被多个线程竞争使用，那么我们通常称之为“临界资源”，对“临界资源”的访问需要加上保护，否则资源会处于“混乱”的状态。
# 下面的例子演示了100个线程向同一个银行账户转账（转入1元钱）的场景，在这个例子中，银行账户就是一个临界资源，在没有保护的情况下我们很有可能会得到错误的结果。


from time import sleep
from threading import Thread


class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        new_balance = self._balance + money  #计算存款后的余额
        sleep(0.01)   #模拟受理存款业务需要0.01秒的时间
        self._balance = new_balance  #修改账户余额

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    #重载了父类的run方法
    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []

    for _ in range(100):
        t = AddMoneyThread(account, 1)   # 创建100个存款的线程对象向同一个账户中存钱
        threads.append(t)
        t.start() #本质是执行了Thread的run方法



    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()



    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()


# 运行上面的程序，结果让人大跌眼镜，100个线程分别向账户中转入1元钱，结果居然远远小于100元。输出1都有可能。
# 之所以出现这种情况是因为我们没有对银行账户这个“临界资源”加以保护，多个线程同时向账户中存钱时，
# 会一起执行到new_balance = self._balance + money这行代码，多个线程得到的账户余额都是初始状态下的0，所以都是0上面做了+1的操作，
# 因此得到了错误的结果。
# 在这种情况下，“锁”就可以派上用场了。
# 我们可以通过“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”，而其他没有得到“锁”的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”，其他线程才有机会获得“锁”，进而访问被保护的“临界资源”。
# todo 下面的代码演示了如何使用“锁”来保护对银行账户的操作，从而获得正确的结果。