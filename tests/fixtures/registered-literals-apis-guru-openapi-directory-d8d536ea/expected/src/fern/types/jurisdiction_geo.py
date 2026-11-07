

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JurisdictionGeo(UniversalBaseModel):
    city: typing.Optional[str] = None
    country: str
    county: typing.Optional[str] = None
    courts_for_jurisdiction_geo_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="courtsForJurisdictionGeoAPI"), pydantic.Field(alias="courtsForJurisdictionGeoAPI")
    ]
    created_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdDate"),
        pydantic.Field(
            alias="createdDate",
            description="The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.",
        ),
    ]
    """
    The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.
    """

    fips_code: typing_extensions.Annotated[str, FieldMetadata(alias="fipsCode"), pydantic.Field(alias="fipsCode")]
    jurisdiction_geo_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="jurisdictionGeoId"), pydantic.Field(alias="jurisdictionGeoId")
    ]
    object: str
    state: str
    zip_code_array: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="zipCodeArray"), pydantic.Field(alias="zipCodeArray")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
