

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GraphNodeInputPosition(UniversalBaseModel):
    """
    The position of the node
    """

    x: float = pydantic.Field()
    """
    The x position of the node
    """

    y: float = pydantic.Field()
    """
    The y position of the node
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
