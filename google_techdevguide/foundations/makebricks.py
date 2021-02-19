
def make_bricks(small: int, big: int, goal: int) -> bool:
    """We want to make a row of bricks that is goal inches long. We have a number of small
    bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to
    make the goal by choosing from the given bricks. This is a little harder than it looks
    and can be done without any loops. 
    """
    size_big = 5
    max_big_bricks = goal // size_big
    if max_big_bricks > big:
        goal = goal - big * size_big
    else:
        goal = goal - max_big_bricks * size_big    

    return goal <= small
    
    # return (goal - big * 5 if goal // 5 > big else goal - goal // 5 * 5)  <= small
    # return (goal % 5 if big * 5 > goal else goal - big * 5) <=small


assert make_bricks(3, 1, 8) == True
assert make_bricks(3, 1, 9) == False
assert make_bricks(6, 1, 9) == True
assert make_bricks(3, 3, 10) == True
assert make_bricks(3, 3, 17) == True
assert make_bricks(3, 3, 21) == False

