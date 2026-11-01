

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .maker import Maker
from .piece_id import PieceId
from .piece_links import PieceLinks


class Piece(UniversalBaseModel):
    """ """

    piece_id: typing_extensions.Annotated[
        typing.Optional[PieceId], FieldMetadata(alias="pieceId"), pydantic.Field(alias="pieceId")
    ] = None
    maker: typing.Optional[Maker] = None
    links: typing.Optional[PieceLinks] = pydantic.Field(default=None)
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
