import time
import multiprocessing

square_result = []
def calc_square(numbers):
    global square_result
    for n in numbers:
        time.sleep(5)
        print('square ',n*n)
        square_result.append(n*n)
    print("With in the Process Result", square_result)


# def calc_cube(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print('cube ' , n*n*n)

if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    # p2 = multiprocessing.Process(target=calc_cube,args=(arr,))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()        

    print("Result", square_result)