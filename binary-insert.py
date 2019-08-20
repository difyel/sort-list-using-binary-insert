def binaryInsert(_list, insertElement, overTwoLen):
    if len(_list) == 0:
        # if the list is empty insert the element at the begining of the list
        _list.append(insertElement)
        return _list

    if insertElement == _list[overTwoLen]:
        # if the element that we want to insert is equal to the element at the length over two
        _list.insert(overTwoLen+1, insertElement)
        # the search element is found and insert it after the element to which it is equal
        return _list

    if insertElement < _list[overTwoLen]:
        # searchElement  in the lower half
        # the element to insert is smaller than the element at _list[overTwoLen]
        if overTwoLen == 0 or (overTwoLen == len(_list) - 1 and len(_list) != 2):  #
            # if the length over  is zero ,
            # or is equal to the last element  of the list , and the number of  elements in the list is != 2
            # insert the element
            _list.insert(overTwoLen, insertElement)
            # either at the begining of the list , the smallest
            # before the end of the list it is smaller than the last element
            return _list
        newOverTwo = (overTwoLen - 0) // 2
        # calculate the new length over two
        # try to insert at the new length over two
        return binaryInsert(_list, insertElement, newOverTwo)

    if insertElement > _list[overTwoLen]:
        # uper half
        # if the element to insert is larger the _list[overTwoLen]
        if overTwoLen == len(_list) - 1 or overTwoLen == 0:
            # if overTwoLen is equal to the  index of the last element
            # of if it s equal to zero
            _list.insert(overTwoLen + 1, insertElement)
            # the element is larger than the smallest element insert it after
            # the element i larger than the largest element insert it after
            return _list
        newOverTwo = (len(_list) + overTwoLen) // 2
        # calculate the new length over two
        # try to insert at the new length over two
        return binaryInsert(_list, insertElement, newOverTwo)

def sortArrayRecursively(_list):
    if len(_list) == 0:
        return _list
    if len(_list) == 1:
        return _list
    sortedList = []
    for elemenet in _list:
        # 2 // 2 = 1
        # print(
        #     f'sortedList : {sortedList}  , len(sortedList)//2 {len(sortedList)//2}')
        binaryInsert(sortedList, elemenet, len(sortedList)//2)
    return sortedList


def testSortArrayRecursively():
    # sort the empty list
    print(sortArrayRecursively([]))

    # sort a list containing one element
    print(sortArrayRecursively([1]))

    # sort a list containing two elements
    print(sortArrayRecursively([1, 2]))
    print(sortArrayRecursively([2, 1]))

    # sort a list containing three elements
    print(sortArrayRecursively([1, 2, 3]))
    print(sortArrayRecursively([1, 3, 2]))
    print(sortArrayRecursively([2, 3, 1]))
    print(sortArrayRecursively([2, 1, 3]))
    print(sortArrayRecursively([3, 1, 2]))
    print(sortArrayRecursively([3, 2, 1]))

    # sort a list containing 4 elements
    print(sortArrayRecursively([1, 2, 3, 4]))
    print(sortArrayRecursively([1, 2, 4, 3]))
    print(sortArrayRecursively([1, 3, 2, 4]))
    print(sortArrayRecursively([1, 3, 4, 2]))
    print(sortArrayRecursively([1, 4, 2, 3]))
    print(sortArrayRecursively([1, 4, 3, 2]))
    print(sortArrayRecursively([2, 1, 3, 4]))
    print(sortArrayRecursively([2, 1, 4, 3]))
    print(sortArrayRecursively([2, 3, 1, 4]))
    print(sortArrayRecursively([2, 3, 4, 1]))
    print(sortArrayRecursively([2, 4, 1, 3]))
    print(sortArrayRecursively([2, 4, 3, 1]))
    print(sortArrayRecursively([3, 1, 2, 4]))
    print(sortArrayRecursively([3, 1, 4, 2]))
    print(sortArrayRecursively([3, 2, 1, 4]))
    print(sortArrayRecursively([3, 2, 4, 1]))
    print(sortArrayRecursively([3, 4, 1, 2]))
    print(sortArrayRecursively([3, 4, 2, 1]))
    print(sortArrayRecursively([4, 1, 2, 3]))
    print(sortArrayRecursively([4, 1, 3, 2]))
    print(sortArrayRecursively([4, 2, 1, 3]))
    print(sortArrayRecursively([4, 2, 3, 1]))
    print(sortArrayRecursively([4, 3, 1, 2]))
    print(sortArrayRecursively([4, 3, 2, 1]))


if __name__ == '__main__':
    testSortArrayRecursively()


/*output
[]
[1]
[1, 2]
[1, 2]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
*/

