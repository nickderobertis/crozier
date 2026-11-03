

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .glassblower import Glassblower
from .glaze_kind import GlazeKind
from .maker import Maker
from .piece_id import PieceId
from .piece_links import PieceLinks


class Piece(UniversalBaseModel):
    """ """

    piece_id: typing_extensions.Annotated[
        typing.Optional[PieceId], FieldMetadata(alias="pieceId"), pydantic.Field(alias="pieceId")
    ] = None
    maker: typing.Optional[Maker] = None
    glaze: typing.Optional[GlazeKind] = None
    fired_by: typing_extensions.Annotated[
        typing.Optional[Glassblower], FieldMetadata(alias="firedBy"), pydantic.Field(alias="firedBy")
    ] = None
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
