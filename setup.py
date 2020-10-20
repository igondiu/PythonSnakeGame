from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name="Snake game",
    version="1",
    description="Une fenêtre s'ouvre, vous pouvez jouer au bon vieux snake",
    executables=[Executable("play snake.py")],
)
