# Application
A desktop framework based on python.

Example: Chess game

## Projects directory

Put Application repository in the same directory of "your Chess project"

```
C:\Users\my_user\path\path\path\all_my_git_projects
```

<p align="center"><img alt="All projects directory" src="https://i.pinimg.com/originals/b3/c8/a4/b3c8a41f5b74aa86ef05b99f33ab2c68.png" /></p>

Obs.: If needed, you can find mor information about Globals here: https://github.com/SamuelJansen/Globals

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

Notice the .run() method bein called in your main class. It's important.

<p align="center"><img alt="Chess api main file" src="https://i.pinimg.com/originals/6b/32/ff/6b32ffba3ecc48c232a9d9543f38223b.png" /></p>

By doing so, whenever you run you api in command prompt, you should be able to see the pathMannanger import path tree like this:

<p align="center"><img alt="Chess api main file" src="https://i.pinimg.com/originals/37/c7/6a/37c76addfcc511a00daa7e4eecef7d9e.png" /></p>

From now on, classes paths wont be a problem anymore

## Now, extend Application on "your Chess.py" class

Applicaiton should be extendend into one of your classes. In this example, it's Chess.py

```
import Application

class Chess(Application.Application):

    def __init__(self,pathMannanger):

        Application.Application.__init__(self,pathMannanger,floor=True)
```

Be a cool kid. Only one class in your project can inherit from Application.

And the .run() method of this same class must be called in your main (see above)

<p align="center"><img alt="Chess domain class" src="https://i.pinimg.com/originals/0f/ff/c4/0fffc4816db499719e0eee6005e576e5.png" /></p>

By setting floor to true, you automatically gain a "background image". All you have to do is put this "background image" in the correct directory with the correc name (see bellow)

This "background image" must be a png and be named like this: "YourApiName.floor.png"

In this example, it's "Chess.floor.png"

the directory follows:

```
the_whole_path_up_to_chess_project\Chess\api\src\resource\image\application floor\Chess.floor.png
```

<p align="center"><img alt="Chess.floor.png" src="https://i.pinimg.com/originals/3b/cc/d1/3bccd1addb8d8ab64aa729d19dec9f63.png" /></p>

Of course there are flexible ways to set your background image. This is just a quick start

Once you do that, you should be able to run "ChessApplication.py" form your command prompt

On Windows

```
the_whole_path_up_to_chess_project\Chess\api\src>ChessApplication.py
```

On Mac

```
the_whole_path_up_to_chess_project\Chess\api\src>pyton3 ChessApplication.py
```

<p align="center"><img alt="ChessApplication.py" src="https://i.pinimg.com/originals/e9/06/56/e90656587a8c955241397fd38f376a9a.png" /></p>

To quit, click on command prompt and hit `ctrl + c`

## How does Application library woks ❓

Of course there won't be any chess game at all if run this so far. The game needs to be implemented.

Let's start whit an exit button

-----

# UserInterface 

"UserInterface" is a root from a bunch of Application classes

"Button" is one of its manny implementetions

## Make a Button

import Button and instantiate it. Done

In this exemple, it's instantiated in the Chess.py class

```
import Application, Button

class Chess(Application.Application):

    def __init__(self,pathMannanger):

        Application.Application.__init__(self,pathMannanger,floor=True)

        button_name = 'exitChessButton'
        button_position = [0,0]
        button_size = [40,40]

        button_father = self

        Button.Button(
            button_name,
            button_position,
            button_size,
            button_father,
            onLeftClick = exitChessButtonFunction
        )

def exitChessButtonFunction(event):

    application = event.application

    application.close(event)
```

<p align="center"><img alt="exitChessButton instance" src="https://i.pinimg.com/originals/95/40/90/9540901887de16874af3b300d706b51d.png" /></p>

As Button is a UserInterface implementation, its image stays on "user interface" directory. 

The image file name must be the same of the object name

```
the_whole_path_up_to_chess_project\Chess\api\src\resource\image\user interface\exitChessButton.png
```

Again. There are flexible ways to do so. This is just an "easy path"

<p align="center"><img alt="exitChessButton.png" src="https://i.pinimg.com/originals/5c/19/3b/5c193b858fb7dd3c25c55eb92eece431.png" /></p>

☎️ ❗️ ☎️ Some important things ☎️ ❗️ ☎️

- Every object must have a unique name. There are ways to make it under the hood but... it's often nice to know their names

- objects and styles are in the same file. It's part of their code

- every object have its father. If we ommit the father of one object, its father becomes the "floor" and it's not cool.

- there is no ".run()" method, except the one in your main class

- there is no state. Globals api (implemented in PathMannager class) takes care of it

## Events 🌈

You might be wondering about the exit function itself

And yes. It's actualy that simple:

- Any function recieves an event as input.

- any event have the application on it

- the sky is not the limit 🚀

<p align="center"><img alt="exitChessButton.png" src="https://i.pinimg.com/originals/46/1a/54/461a54b109c4910fe3f0f2df6d630258.png" /></p>

If you run ChessApplication.py, you should be able to see a big exit button on the left upper corner of your screen.

# The chalange.

Now, lets do something that's usualy a pain in the ass

`After clicking on the exit button, a modal must appears with a message and two buttons: an "ok" and a "cancel"`

It's usually time to cry, but just guive a look at the simplicity of it:

<p align="center"><img alt="exitChessButton.png" src="https://i.pinimg.com/originals/ca/af/12/caaf128380d1dee1b29499e56af1b37f.png" /></p>

Done 😎 

And yes. The modal is actually implemented as a new page. 

No routes, no global states, nothing.

It's just that simple ✨

```
import Message, ItemDto
import textFunction

messageName = 'exitChessMessageModal'

def exitChessButtonFunction(event):

    buttonPosition = ['fill','center']
    buttonSize = [85,45]
    messageFontSize = 18
    textPosition = ['center','padded']

    cancelButtonDto = ItemDto.ItemDto('cancel',
        position = buttonPosition,
        size = buttonSize,
        text = 'Cancel',
        textPosition = textPosition,
        onLeftClick = cancel
    )
    okButtonDto = ItemDto.ItemDto('ok',
        position = buttonPosition,
        size = buttonSize,
        text = 'Ok',
        textPosition = textPosition,
        onLeftClick = ok
    )

    messageButtonsDto = [cancelButtonDto,okButtonDto]
    message = 'Do you want to exit the game?'

    Message.Message(event.object,message,
        name = messageName,
        messageButtonsDto = messageButtonsDto,
        fontSize = messageFontSize
    )

def cancel(event) :
    message = event.application.findObjectByName(messageName)
    message.close()

def ok(event) :
    message = event.application.findObjectByName(messageName)
    message.close()

    application = event.application
    application.close(event)
```

And in your Chess.py class you import it and pass it as the "onLeftClick" Button method

```
import Application, Button, exitChessButtonFunction

class Chess(Application.Application):

    def __init__(self,pathMannanger):

        Application.Application.__init__(self,pathMannanger,floor=True)

        button_name = 'exitChessButton'
        button_position = [0,0]
        button_size = [40,40]

        button_father = self

        Button.Button(
            button_name,
            button_position,
            button_size,
            button_father,
            onLeftClick = exitChessButtonFunction.exitChessButtonFunction
        )
```

# The future 🌍

I'll be implmenting more of this Chess example code on this other repository: https://github.com/SamuelJansen/Chess/tree/develop

Feel free to navigate throught the Application library source code here

Cheers

