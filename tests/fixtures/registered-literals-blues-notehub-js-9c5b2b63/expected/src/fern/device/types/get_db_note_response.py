

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetDbNoteResponse(UniversalBaseModel):
    body: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The note body
    """

    payload: typing.Optional[str] = pydantic.Field(default=None)
    """
    The note payload
    """

    time: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time the Note was added to the Notecard or Notehub
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
