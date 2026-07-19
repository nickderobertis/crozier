

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ecgi import Ecgi
from .global_ran_node_id import GlobalRanNodeId
from .ncgi import Ncgi
from .presence_state import PresenceState
from .tai import Tai


class PresenceInfo(UniversalBaseModel):
    pra_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="praId"), pydantic.Field(alias="praId")
    ] = None
    presence_state: typing_extensions.Annotated[
        typing.Optional[PresenceState], FieldMetadata(alias="presenceState"), pydantic.Field(alias="presenceState")
    ] = None
    tracking_area_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Tai]],
        FieldMetadata(alias="trackingAreaList"),
        pydantic.Field(alias="trackingAreaList"),
    ] = None
    ecgi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Ecgi]], FieldMetadata(alias="ecgiList"), pydantic.Field(alias="ecgiList")
    ] = None
    ncgi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Ncgi]], FieldMetadata(alias="ncgiList"), pydantic.Field(alias="ncgiList")
    ] = None
    global_ran_node_id_list: typing_extensions.Annotated[
        typing.Optional[typing.List[GlobalRanNodeId]],
        FieldMetadata(alias="globalRanNodeIdList"),
        pydantic.Field(alias="globalRanNodeIdList"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
