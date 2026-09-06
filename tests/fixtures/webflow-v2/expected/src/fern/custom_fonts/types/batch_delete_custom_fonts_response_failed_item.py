

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BatchDeleteCustomFontsResponseFailedItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of a custom font that could not be deleted
    """

    name: str = pydantic.Field()
    """
    Error name
    """

    msg: str = pydantic.Field()
    """
    Human-readable error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
