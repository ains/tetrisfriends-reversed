#Tetris Friends TetRandom random number generator
#Derived directly from the decompiled source code
class TetRandom:
    randIndex1 = 0
    randIndex2 = 10
    bufferSize = 17
    randomBuffer = [0] * 17

    def __init__(self, seed):
        self.seed = seed & 0xFFFF

        self.populateBuffer()
        for i in range(0, 100):
            self.getNextRandom()

    def populateBuffer(self):
        currentValue = self.seed
        for i in range(0, self.bufferSize):
            self.randomBuffer[i] = currentValue;
            currentValue = (((((currentValue << 5) & 0xFFFF) | ((currentValue >> 11) & 0xFFFF)) & 0xFFFF) + 97)
            currentValue = currentValue & 0xFFFF

    def getNextRandom(self):
        fstRandom = self.randomBuffer[self.randIndex1]
        sndRandom = self.randomBuffer[self.randIndex2]

        replaceRandom = ((((fstRandom << 3) & 0xFFFF) | ((fstRandom >> 13) & 0xFFFF)) & 0xFFFF)
        replaceRandom = (replaceRandom + ((((sndRandom << 5) & 0xFFFF) | ((sndRandom >> 11) & 0xFFFF)) & 0xFFFF))
        replaceRandom = replaceRandom & 0xFFFF;

        self.randomBuffer[self.randIndex1] = replaceRandom
        self.randIndex1 = (self.bufferSize - 1) if (self.randIndex1 <= 0) else self.randIndex1 - 1
        self.randIndex2 = (self.bufferSize - 1) if (self.randIndex2 <= 0) else self.randIndex2 - 1
        return replaceRandom & 2047;