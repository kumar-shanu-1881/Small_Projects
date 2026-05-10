from cx_Freeze import setup,Executable

setup(
    name="Kumar Calculator",
    version="1.0",
    description="A simple calculator application",
    executables=[Executable("Calculator.py")]
)   
