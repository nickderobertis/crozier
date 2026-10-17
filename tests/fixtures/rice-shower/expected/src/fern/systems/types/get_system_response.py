

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_system_response_heaters_item import GetSystemResponseHeatersItem
from .get_system_response_thermos_item import GetSystemResponseThermosItem


class GetSystemResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique system slug, e.g. lab-2005
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Human-readable system name"),
    ]
    """
    Human-readable system name
    """

    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    Physical location description
    """

    thermo_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="thermoUrl"),
        pydantic.Field(alias="thermoUrl", description="Base URL to thermo/ls-api instance"),
    ]
    """
    Base URL to thermo/ls-api instance
    """

    heater_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="heaterUrl"),
        pydantic.Field(alias="heaterUrl", description="Base URL to heater-api instance"),
    ]
    """
    Base URL to heater-api instance
    """

    enabled: bool = pydantic.Field()
    """
    Whether scraping is enabled
    """

    thermos: typing.List[GetSystemResponseThermosItem]
    heaters: typing.List[GetSystemResponseHeatersItem]
    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Creation timestamp"),
    ]
    """
    Creation timestamp
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Last update timestamp"),
    ]
    """
    Last update timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
