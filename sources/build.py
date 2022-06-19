from cx_Freeze import Executable, setup

executables = [Executable("main.py")]

setup(
    name="Discord Mass DM Self Bot",
    version="1.0.0",
    description="Most Easiest Lightweight Easy-To-Use Mass Dm Self Bot",
    executables=executables,
)