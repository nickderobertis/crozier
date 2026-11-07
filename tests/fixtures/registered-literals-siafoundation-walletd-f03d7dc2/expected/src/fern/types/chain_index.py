

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChainIndex(UniversalBaseModel):
    height: typing.Optional[int] = pydantic.Field(default=None)
    """
    The height of the block in the blockchain
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for a block
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
