# def get_medical_service(preparat):
#     def do_treat():
#         print(f"[{preparat}] подействовал")
#
#     return do_treat
#
#
# treater1 = get_medical_service("анальгин")
# treater2 = get_medical_service("укол")
#
# treater1()
# treater1()
# treater1()
#
# treater2()
# treater2()

def func_counter(start_from=0):
    def count():
        nonlocal start_from
        start_from += 1
        print(f"Номер: {start_from}")

    return count


counter1 = func_counter(0)
counter2 = func_counter(10)

counter1()
counter2()
counter1()
counter1()
counter2()
