global calls
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(new_str):
    count_calls()
    return len(new_str), new_str.upper(), new_str.lower()


def is_contains(new_str, str_list: tuple):
    count_calls()
    for str_ in str_list:
        if new_str.lower() in str_.lower(): return True
    return False


print(string_info("UltraUrbanAnia"))
print(string_info("ArbanAnia"))
print(string_info("Rayban"))
print(is_contains("UrBaN", ["UltraUrbanAnia", "ArbanAnia", "Rayban"]))
print(is_contains("BaN", ["rbaN ", "BaNaN", "Jban"]))
print(is_contains("UrB", ["rbaN ", "BaNaN", "Jban"]))

print(calls)
