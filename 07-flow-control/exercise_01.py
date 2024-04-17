# To what values do the following expressions evaluate?

False or (True and False)   # False
True or (1 + 2)             # True
(1 + 2) or True             # 3, (1 + 2) will be shortcircuited because "or" operator 
                            # only needs 1 truthy value.
                            # Since 3 is truthy, output will be shortcicuited to 3
True and (1 + 2)            # 3, Again due to shortcircuit.
                            # This time, the left side True is evaluated first to be truthy
                            # So the expression is now depends on the evaluated of (1+2)
                            # Which is 3, it will be shortcircuited
False and (1 + 2)           # False
(1 + 2) and True            # True
(32 * 4) >= 129             # False
False != (not True)         # False
True == 4                   # False, trick question after the and/or section
False == (847 == '847')     # True, False == False is truthy