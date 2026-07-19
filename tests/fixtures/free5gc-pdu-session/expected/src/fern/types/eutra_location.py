

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ecgi import Ecgi
from .global_ran_node_id import GlobalRanNodeId
from .tai import Tai


class EutraLocation(UniversalBaseModel):
    tai: Tai
    ecgi: Ecgi
    age_of_location_information: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ageOfLocationInformation"),
        pydantic.Field(alias="ageOfLocationInformation"),
    ] = None
    ue_location_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="ueLocationTimestamp"),
        pydantic.Field(alias="ueLocationTimestamp"),
    ] = None
    geographical_information: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="geographicalInformation"),
        pydantic.Field(alias="geographicalInformation"),
    ] = None
    geodetic_information: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="geodeticInformation"), pydantic.Field(alias="geodeticInformation")
    ] = None
    global_ngenb_id: typing_extensions.Annotated[
        typing.Optional[GlobalRanNodeId], FieldMetadata(alias="globalNgenbId"), pydantic.Field(alias="globalNgenbId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
