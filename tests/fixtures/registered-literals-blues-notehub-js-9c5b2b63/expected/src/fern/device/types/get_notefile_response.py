

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetNotefileResponse(UniversalBaseModel):
    changes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of pending changes in the Notefile.
    """

    notes: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    An object with a key for each note and a value object with the body of each Note and the time the Note was added.
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of notes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
