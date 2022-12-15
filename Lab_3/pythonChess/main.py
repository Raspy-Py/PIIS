import random
import chess

class NegaAgent:
    board = None

    def __init__(self, board: chess.Board()):
        self.board = board

    def board_balance(self):
        W = self.board.occupied_co[chess.WHITE]
        B = self.board.occupied_co[chess.BLACK]
        pawn_weight = 1
        knight_weight = 3
        bishop_weight = 3
        rook_weight = 5
        queen_weight = 9

        balance = (
                pawn_weight     * (chess.popcount(W & board.pawns)    - chess.popcount(B & board.pawns)) +
                knight_weight   * (chess.popcount(W & board.knights)  - chess.popcount(B & board.knights)) +
                bishop_weight   * (chess.popcount(W & board.bishops)  - chess.popcount(B & board.bishops)) +
                rook_weight     * (chess.popcount(W & board.rooks)    - chess.popcount(B & board.rooks)) +
                queen_weight    * (chess.popcount(W & board.queens)   - chess.popcount(B & board.queens))
        )
        return balance

    def numberOFPieces(self, whoToMove):
        if whoToMove == 1:
            chosen = self.board.occupied_co[chess.WHITE]
        else:
            chosen = self.board.occupied_co[chess.BLACK]
        return (
                chess.popcount(chosen & self.board.pawns) +
                (chess.popcount(chosen & self.board.knights)) +
                (chess.popcount(chosen & self.board.bishops)) +
                (chess.popcount(chosen & self.board.rooks)) +
                (chess.popcount(chosen & self.board.queens))
        )

    def evalF(self, whoToMove):
        numberOfWhites = self.numberOFPieces(1)
        numberOfBlacks = self.numberOFPieces(-1)
        materialBalance = self.board_balance()
        return materialBalance * (numberOfWhites - numberOfBlacks) * whoToMove

    def negaMax(self, depth: int, whoToMove: int) -> tuple:
        if depth == 0:
            return self.evalF(whoToMove), None
        maxScore = -10000
        bestMove = None
        for legalMove in self.board.legal_moves:
            score = -(self.negaMax(depth - 1, -whoToMove)[0])
            if score == 0:
                score = random.random()
            if score > maxScore:
                maxScore = score
                bestMove = legalMove
        return maxScore, bestMove

    def negaScout(self, depth: int, whoToMove: int, alpha: int, beta: int) -> tuple:
        if depth == 0:
            return self.evalF(whoToMove), None
        bestMove = None
        for legalMove in self.board.legal_moves:
            score = -(self.negaScout(depth - 1, -whoToMove, -beta, -alpha)[0])
            if score > alpha and score < beta and depth > 1:
                score2 = -(self.negaScout(depth - 1, -whoToMove, -beta, -score))[0]
                score = max(score, score2)
            if score == 0:
                score = random.random()
            if score > alpha:
                alpha = score
                bestMove = legalMove
            if alpha >= beta:
                return alpha, bestMove
            beta = alpha + 1
        return alpha, bestMove

    def PVC(self, depth: int, whoToMove: int, alpha: int, beta: int) -> tuple:
        if depth == 0:
            return self.evalF(whoToMove), None

        bestMove = None
        for legalMove in self.board.legal_moves:
            score = -(self.PVC(depth - 1, -whoToMove, -beta, -alpha)[0])
            if (score > alpha) and (score < beta):
                score = -(self.PVC(depth - 1, -whoToMove, -beta, -score))[0]
            if score == 0:
                score = random.random()
            if score > alpha:
                alpha = score
                bestMove = legalMove
            if alpha >= beta:
                return alpha, bestMove
            beta = alpha + 1
        return alpha, bestMove

board = chess.Board()
negaAgent = NegaAgent(board)
depth, whoToMove = 5, -1

algoType = int(input("1 - negaMax, 2 - negaScout, 3 - PVC: "))
while not board.is_checkmate():
    print("Game state:\n")
    print(board)
    move = input("Input your move: ")
    board.push_san(move)
    if algoType == 2:
        print("hi")
        negaMove = negaAgent.negaScout(depth, whoToMove, -10000, 10000)[1]
    elif algoType == 3:
        negaMove = negaAgent.PVC(depth, whoToMove, -10000, 10000)[1]
    else:
        negaMove = negaAgent.negaMax(depth, whoToMove)[1]
    board.push(negaMove)
