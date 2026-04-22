def py_shadow_merge(list1: list[int], list2: list[int]) -> list[int]:

        if list1 is None:
            return sorted(list2)
        if list2 is None:
            return sorted(list1)
        list1.extend(list2)
        return sorted(list1)
