# Application
A desktop framework based on python 

Example: Chess game

## Projects directory

Put Application repository in the same directory of "your Chess project"

```
C:\Users\my_user\path\path\path\all_my_git_projects
```

<p align="center"><img alt="All projects directory" src="https://i.pinimg.com/originals/b3/c8/a4/b3c8a41f5b74aa86ef05b99f33ab2c68.png" /></p>

Obs.: If needed, you can find mor information about GLobals here: https://github.com/SamuelJansen/Globals

## Put PathMannanger.py in your "main" api

On Chess/api/src/ChessApplication.py (the main class that will consume Application library), 
you put the PathMannanger.py file following this path tree:

```
C:\Users\my_user\path\path\path\all_my_git_projects\Chess\api\src\domain\control\PathMannanger.py
```

Once again, "chess main class" needs to be in src directory.

<p align="center"><img alt="PathMannanger file in Chess/api/src/domain/control directory" src="https://i.pinimg.com/originals/e6/62/cb/e662cb3f41fecba77572de839a5e7a9f.png" /></p>

## Put this code in "your ChessApplication.py" file (the main class of your api)

Put the following code right on top of ChessApplication class.

```
if __name__ == '__main__' :
    from domain.control import PathMannanger
    pathMannanger = PathMannanger.PathMannanger(printStatus = True)

    import Chess
    Chess.Chess(pathMannanger).run()
```

<p align="center"><img alt="Chess api main file" src="https://i.pinimg.com/originals/6b/32/ff/6b32ffba3ecc48c232a9d9543f38223b.png" /></p>
