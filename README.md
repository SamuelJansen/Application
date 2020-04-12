# Application
A desktop framework based on python 

Example: Chess game

## Projects directory

Put Application repository in the same directory of "your Chess project"

```
C:\Users\my_user\path\path\path\all_my_git_projects
```

<p align="center"><img alt="All projects directory" src="https://i.pinimg.com/originals/67/ec/2c/67ec2c13bc7ee72a06eb737eac3dc8bb.png" /></p>

Obs.: If needed, you can find mor information about GLobals here: https://github.com/SamuelJansen/Globals

## Put PathMannanger.py in your "main" api

On Chess/api/src/ChessApplication.py (the main class that will consume Application library), 
you put the PathMannanger.py file following this path tree:

```
C:\Users\my_user\path\path\path\all_my_git_projects\Chess\api\src\domain\control\PathMannanger.py
```

Once again, "chess main class" needs to be in src directory.

<p align="center"><img alt="PathMannanger.py file" src="https://i.pinimg.com/originals/d1/a3/3e/d1a33efcc8880eefadec49f503352429.png" /></p>

## Put this code in "your ChessApplication.py" file (the main class of your api)

Put the following code right on top of ChessApplication class.

```
if __name__ == '__main__' :
    from domain.control import PathMannanger
    pathMannanger = PathMannanger.PathMannanger(printStatus = True)

    import Chess
    Chess.Chess(pathMannanger).run()
```

<p align="center"><img alt="Chess api main file" src="https://i.pinimg.com/originals/fb/4a/ff/fb4aff6b961958d69707e0ab3c71e054.png" /></p>
