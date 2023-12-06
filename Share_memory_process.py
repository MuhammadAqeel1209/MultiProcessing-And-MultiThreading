import multiprocessing

def calc_square(numbers, result,v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == "__main__":
    numbers = [2,3,5]

    # result = multiprocessing.Array('data type',size of array)
    result = multiprocessing.Array('i',3)
    value = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result,value))

    p.start()
    p.join()

    print(result[:])
    print(value.value)