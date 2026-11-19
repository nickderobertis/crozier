

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alarm import Alarm
from .entry_mood import EntryMood
from .entry_spare import EntrySpare
from .entry_tally import EntryTally
from .entry_tone import EntryTone
from .memo import Memo


class Entry(UniversalBaseModel):
    memo: str = pydantic.Field()
    """
    The wording.
    """

    aside: typing.Optional[str] = pydantic.Field(default=None)
    """
    An aside kept beside the entry.
    """

    label: str = pydantic.Field()
    """
    The label's wording.
    """

    caption: Memo = pydantic.Field()
    """
    The caption kept beside the entry.
    """

    tally: EntryTally = pydantic.Field()
    """
    The tally's wording.
    """

    spare: typing.Optional[EntrySpare] = pydantic.Field(default=None)
    """
    The spare kept beside the entry.
    """

    mood: EntryMood = pydantic.Field()
    """
    The mood's wording.
    """

    tone: typing.Optional[EntryTone] = pydantic.Field(default=None)
    """
    The tone kept beside the entry.
    """

    alarm: typing.Optional[Alarm] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
