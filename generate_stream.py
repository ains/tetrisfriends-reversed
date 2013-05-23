from TetPieceBag import TetPieceBag
import itertools

#Check if the head of a given tetromino bag sequence matches the given sequence
def headMatches(given, bag):
    generatedPieces = list(itertools.islice(bag.pieceGenerator(), 0, len(given)))
    return (generatedPieces == given)

#Sample given, set to first 9 pieces of a game
given = list("LITOZSJJI")

bagSize = 7
searchSpace = (TetPieceBag(bagSize, seed) 
	for seed in range(0, 2 ** 16) 
	if headMatches(given, TetPieceBag(bagSize, seed)))
#Stop at first match.
firstMatch = next(searchSpace)

print "The seed which was used to generate the given sequence is: {}".format(firstMatch.seed)
print "The first 50 pieces in the tetromino sequence are"
print list(itertools.islice(firstMatch.pieceGenerator(), 0, 50))