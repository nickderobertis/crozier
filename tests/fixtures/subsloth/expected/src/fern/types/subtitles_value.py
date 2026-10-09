

import typing

from .subtitle_track import SubtitleTrack
from .subtitles_value_one_value import SubtitlesValueOneValue

SubtitlesValue = typing.Union[typing.List[SubtitleTrack], typing.Dict[str, SubtitlesValueOneValue]]
