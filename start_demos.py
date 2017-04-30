from demos.demo1 import demo1
from demos.demo2 import demo2
from demos.demo3 import demo3
from demos.demo4 import demo4


__author__ = 'cenk'

if __name__ == "__main__":
    print "-*-" * 20, "Demo 1 Starts", "-*-" * 20
    demo1()
    print "-*-" * 20, "Demo 1 Ends", "-*-" * 20
    print "-*-" * 20, "Demo 2 Starts", "-*-" * 20
    demo2()
    print "-*-" * 20, "Demo 2 Ends", "-*-" * 20
    print "-*-" * 20, "Demo 3 Starts", "-*-" * 20
    demo3()
    print "-*-" * 20, "Demo 3 Ends", "-*-" * 20
    print "-*-" * 20, "Demo 4 Starts", "-*-" * 20
    demo4(3000)
    demo4(30000)
    demo4(300000)
    demo4(3000000)
    demo4(12000000)
    print "-*-" * 20, "Demo 4 Ends", "-*-" * 20
