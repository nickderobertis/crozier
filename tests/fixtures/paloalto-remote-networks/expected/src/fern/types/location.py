

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .public_ip import PublicIp
from .region_cordinates import RegionCordinates


class Location(UniversalBaseModel):
    """
    Site Public IP or approximate gps coordinates
    """

    public_ip: typing_extensions.Annotated[
        typing.Optional[PublicIp], FieldMetadata(alias="public-ip"), pydantic.Field(alias="public-ip")
    ] = None
    region_cordinates: typing_extensions.Annotated[
        typing.Optional[RegionCordinates],
        FieldMetadata(alias="region-cordinates"),
        pydantic.Field(alias="region-cordinates"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
