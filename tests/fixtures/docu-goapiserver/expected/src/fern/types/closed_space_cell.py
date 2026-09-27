

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClosedSpaceCell(UniversalBaseModel):
    """
    Closed Space Cell.
    """

    room_id: str = pydantic.Field()
    """
    Lead id.
    """

    period: str
    closed_spaces: typing.Optional[int] = pydantic.Field(default=None)
    """
    Cannot exceed the room capacity. Zero removes the existing override; omitted or null is decoded as zero by the current handler.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
