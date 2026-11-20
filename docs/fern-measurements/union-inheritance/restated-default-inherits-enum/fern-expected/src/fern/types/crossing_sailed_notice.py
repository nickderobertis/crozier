

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .crossing_sailed_notice_phase import CrossingSailedNoticePhase


class CrossingSailedNotice(UniversalBaseModel):
    """
    The crossing has sailed.
    """

    phase: typing.Optional[CrossingSailedNoticePhase] = pydantic.Field(default=None)
    """
    Where the crossing stands.
    """

    crossing_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="crossingId"), pydantic.Field(alias="crossingId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
