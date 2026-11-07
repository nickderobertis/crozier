

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NoteInput(UniversalBaseModel):
    body: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Arbitrary user-defined JSON for the note.
    """

    payload: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional base64-encoded payload.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
