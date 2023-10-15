import sys

if len(sys.argv) != 2:
    print("Використання: python runner.py <назва_лабораторної>")
    sys.exit(1)

lab_name = sys.argv[1]

if lab_name == "lab_1":
    from lab_1 import main as lab_1_main
    lab_1_main()
elif lab_name == "lab_2":
    from lab_2 import main as lab_2_main
    lab_2_main()
elif lab_name == "lab_3":
    from lab_3 import main as lab_3_main
    lab_3_main()
elif lab_name == "lab_4":
    from lab_4 import main as lab_4_main
    lab_4_main()
else:
    print("Невідома лабораторна робота")


