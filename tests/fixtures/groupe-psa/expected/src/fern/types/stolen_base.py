

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stolen_base_end_position import StolenBaseEndPosition
from .stolen_base_links import StolenBaseLinks
from .stolen_base_start_position import StolenBaseStartPosition


class StolenBase(UniversalBaseModel):
    links: typing_extensions.Annotated[StolenBaseLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    id: str
    state: bool = pydantic.Field()
    """
    Stolen state of the vehicle (True means the vhicle is reported stolen).
    """

    started_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startedAt"),
        pydantic.Field(alias="startedAt", description="Stolen vehicle start time."),
    ]
    """
    Stolen vehicle start time.
    """

    end_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="endAt"),
        pydantic.Field(alias="endAt", description="Stolen vehicle stop time."),
    ] = None
    """
    Stolen vehicle stop time.
    """

    start_position: typing_extensions.Annotated[
        typing.Optional[StolenBaseStartPosition],
        FieldMetadata(alias="startPosition"),
        pydantic.Field(alias="startPosition"),
    ] = None
    end_position: typing_extensions.Annotated[
        typing.Optional[StolenBaseEndPosition], FieldMetadata(alias="endPosition"), pydantic.Field(alias="endPosition")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
