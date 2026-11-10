

import typing

from .score_one import ScoreOne
from .score_two import ScoreTwo
from .score_zero import ScoreZero

Score = typing.Union[ScoreZero, ScoreOne, ScoreTwo]
