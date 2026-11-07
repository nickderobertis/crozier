

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Note(UniversalBaseModel):
    body: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Arbitrary user-defined JSON for the note.
    """

    edge: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if originated from an edge source.
    """

    id: str = pydantic.Field()
    """
    Note name/identifier (e.g., "1:435", "my_note").
    """

    payload: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional base64-encoded payload.
    """

    pending: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the note is pending delivery or processing.
    """

    time: int = pydantic.Field()
    """
    Unix epoch seconds.
    """

    where: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional location/metadata string.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
