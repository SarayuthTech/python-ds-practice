def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    most_common={}
    for num in nums:
        if most_common[num]:
            most_common[num]=most_common.get(num)+1#most_common[num]=most_common.get(num,0)#only this line
        else:
            most_common[num]=0
    max_value=max(most_common.values)
    for (num,value) in most_common:
        if max_value==value:
            return num
        
    # most_common=[temp_mode[] if nums[num] else num=0 for num in nums]