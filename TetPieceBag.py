from TetRandom import TetRandom
class TetPieceBag:
    tetrominoList = ['Z', 'L', 'O', 'S', 'I', 'J', 'T']

    def __init__(self, bagSize, seed):
        self.bagSize = bagSize
        self.refillSlots = [False] * bagSize
        self.seed = seed
        self.RNG = TetRandom(seed)
        self.pieceBag = []
        self.pieceList = []
        self.generator = self.pieceGenerator()

    def pickPiece(self):
        if (len(self.pieceBag) == 0):
            self.refillBag()
        return self.pieceBag.pop(0)

    def refillBag(self):
        self.refillSlots = [False] * self.bagSize
        for i in range(0, self.bagSize):
            doLoop = True
            while (doLoop):
                refillIndex = self.RNG.getNextRandom() % self.bagSize
                doLoop = self.refillSlots[refillIndex]

            self.refillSlots[refillIndex] = True
            self.pieceBag.append(self.tetrominoList[refillIndex])

    #Get piece at index in a tetromino sequence
    def atIndex(self, index):
        n = index - len(self.pieceList) + 1

        #Cache all the pieces up to a given piece
        while index >= len(self.pieceList):
            self.pieceList.append(next(self.generator))

        return self.pieceList[index]

    #Implemented as a python generator
    def pieceGenerator(self):
        RNG = TetRandom(self.seed)
        self.refillSlots = [False] * self.bagSize

        while True:
            if all(self.refillSlots):
                self.refillSlots = [False] * self.bagSize

            doLoop = True
            while (doLoop):
                refillIndex = RNG.getNextRandom() % self.bagSize
                doLoop = self.refillSlots[refillIndex]

            self.refillSlots[refillIndex] = True
            yield self.tetrominoList[refillIndex]