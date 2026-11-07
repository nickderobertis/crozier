

from .player_round_result import PlayerRoundResult

PlayerFinishEvent = PlayerRoundResult
"""
Fired after a player's solution has gone through all submission tests and the final result for the player has been determined.
This event contains all values that were sent in the PlayerSubmitEvent before as well as the score of the player.
"""
