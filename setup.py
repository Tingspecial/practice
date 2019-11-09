import cx_Freeze

executables = [cx_Freeze.Executable("08.py")]

cx_Freeze.setup(
    name = "A small game",
    options = {"build_exe": {"packages": ["pygame"],
                             "include_files": ["img/car.jpg"]}},
    executables = executables
)

