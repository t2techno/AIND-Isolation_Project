"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # Returns the difference of moves between opponent and I
    return float(len(game.get_legal_moves(player=game._player_1)) - len(game.get_legal_moves(player=game._player_2)))


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # Returns the same as above, but opponent moves weighted 2 
    return float(len(game.get_legal_moves(player=game._player_1)) - 2*len(game.get_legal_moves(player=game._player_2)))



def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # This time the number of my moves is weighted 2
    return float(2*len(game.get_legal_moves(player=game._player_1)) - len(game.get_legal_moves(player=game._player_2)))



class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        # TODO: finish this function!
        # Finished! #
        
        
        # Recursively calls min_value, returns the max value of children
        def max_value(game,current_depth):
            # Timer check
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
               
            legal_moves = game.get_legal_moves()
            if len(legal_moves) == 0:
                return game.utility(self)
            
            # depth check
            if current_depth < depth:
                # Game board is 7x7, impossible for v to be larger than abs(-50)
                v = float('-inf')
                
                # Walk through list of legal moves given board state
                for a in legal_moves:
                    # Take the max value between current hold value, and the min_value of the next ply
                    # Increase depth by 1
                    v = max(v,min_value(game.forecast_move(a),current_depth+1))
                    
                return v
            
            # Return heuristic of current branch if we have reach max depth
            return self.score(game,game.active_player)
        
        # Recursively calls max_value, returns the min value of children
        def min_value(game,current_depth):
            # Timer check
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
                
            legal_moves = game.get_legal_moves()
            if len(legal_moves) == 0:
                return game.utility(self)
            
            # depth check
            if current_depth < depth and len(game.get_legal_moves()) != 0:
                # Game board is 7x7, impossible for v to be larger than abs(-50)
                v = float('inf')
                
                # Walk through list of legal moves given board state
                for a in legal_moves:
                    # Take the min value between current hold value, and the max_value of the next ply
                    # increase depth by 1
                    v = min(v,max_value(game.forecast_move(a),current_depth+1))
                    
                return v
            
            # Return heuristic of current branch if we have reach max depth
            return self.score(game,game.inactive_player)
        
        # Recursively uses helper functions above,
        # Base function minimax
        # Timer check
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # default to no valid moves
        a = (-1,-1)
        moves = {move: min_value(game.forecast_move(move),1) for move in game.get_legal_moves()}
        a = max(moves, key=moves.get)

        return a


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)
        value = -1
        iteritive_depth = self.search_depth-1
        
        while self.time_left()>self.TIMER_THRESHOLD:
            iteritive_depth+=1
            try:
                # The try/except block will automatically catch the exception
                # raised when the timer is about to expire.
                best_move = self.alphabeta(game, iteritive_depth)

            except SearchTimeout:
                # Handle any actions required after timeout as needed
                return best_move
            
            self.time_left = time_left

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        
        def max_value(game,current_depth,alpha,beta):
            # Timer Check
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
            
            # get list of legal moves, return utilty if there are none
            legal_moves = game.get_legal_moves()
            if len(legal_moves) == 0:
                return game.utility(self)
            
            # If we've reached the maximal depth, return heuristic score
            if current_depth >= depth:
                return self.score(game,game.active_player)
            
            
            v = float('-inf')
            for a in legal_moves:
                # Gets the max value of the children of current node, passing on alpha and beta
                # Incrementing depth
                v = max(v,min_value(game.forecast_move(a),current_depth+1,alpha,beta))
                
                # If v is a new lower bound, apply as such
                alpha = max(alpha,v)
                
                # If v >= upper bound, no need to check more children
                if v >= beta:
                    return v
            return v
            
            
            
        def min_value(game,current_depth,alpha,beta):
            # Timer Check
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()
                
            
            legal_moves = game.get_legal_moves()
            if len(legal_moves) == 0:
                return game.utility(self)
            
            # If we've reached the maximal depth, return heuristic score
            if current_depth >= depth:
                return self.score(game,game.inactive_player)
            
            v = float('inf')
            for a in legal_moves:
                # Gets the min value of the children of current node, passing on alpha and beta
                # Incrementing depth
                v = min(v,max_value(game.forecast_move(a),current_depth+1,alpha,beta))
                
                # If v is a new upper bound, apply as such
                beta = min(beta,v)
                
                # If v <= lower bound, no need to check more children
                if v <= alpha:
                    return v
            return v
            
        # TODO: finish this function!
        
        # Base function
        
        # Timer Check
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
                
        legal_moves = game.get_legal_moves()
        if len(legal_moves) == 0:
            return game.utility(self)

        # default to no valid moves
        a = (-1,-1)
        v = max_value(game,1,alpha,beta)
        for move in legal_moves:
            if self.score(game.forecast_move(move),game.active_player) == v:
                return move

        return a