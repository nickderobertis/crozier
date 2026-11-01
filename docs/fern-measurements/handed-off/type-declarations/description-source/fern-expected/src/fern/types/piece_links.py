

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PieceLinks(UniversalBaseModel):
    """ """

    photo: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    catalogue: typing.Optional[str] = pydantic.Field(default=None)
    """
    Where the piece is listed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
