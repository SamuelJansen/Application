import surfaceFunction

class Attribute:

    NAME = 'Text'
    STANDARD_LINE_SPACE = 2
    CENTER = 'center'
    PADDED = 'padded'
    WORD_WIDTH = 'wordWidth'


def calculateTextPositionPaddedOnMenu(surfaceOriginalSize,padding,fontSize) :
    positionError = calculatePositionError()
    deslocation = [
        (surfaceOriginalSize[1] - 2 * padding[1] - fontSize) / 2,
        (surfaceOriginalSize[1] - 2 * padding[1] - fontSize) / 2
    ]
    return [
        deslocation[0] + positionError[0],
        deslocation[0] + positionError[1]
    ]

def calculatePositionError() :
    return [0,-1]

def calculateFontSize(surfaceOriginalSize,padding,
    lineSpace = Attribute.STANDARD_LINE_SPACE
) :
    return surfaceFunction.getSizePadded(surfaceOriginalSize,padding)[1] - lineSpace

def parsePosition(textPosition,object,padding = [0,0]) :
    if textPosition :
        if textPosition[0] == Attribute.CENTER :
            textPosition = textPosition.copy()
            textPosition[0] = (object.size[0] - len(object.text) * 8) / 2
        if textPosition[1] == Attribute.PADDED :
            textPosition[1] = calculateTextPositionPaddedOnMenu(object.size,padding,object.fontSize)[1]
    return textPosition
