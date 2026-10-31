

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PlaceFulfillmentOrderRequestMarketingData(UniversalBaseModel):
    utm_campaign: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmCampaign"),
        pydantic.Field(alias="utmCampaign", description="UTM campaign"),
    ] = None
    """
    UTM campaign
    """

    utm_medium: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmMedium"),
        pydantic.Field(alias="utmMedium", description="UTM medium."),
    ] = None
    """
    UTM medium.
    """

    utm_source: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmSource"),
        pydantic.Field(alias="utmSource", description="UTM source."),
    ] = None
    """
    UTM source.
    """

    utmi_campaign: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmiCampaign"),
        pydantic.Field(alias="utmiCampaign", description="utmi_campaign (internal utm)"),
    ] = None
    """
    utmi_campaign (internal utm)
    """

    utmi_page: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmiPage"),
        pydantic.Field(alias="utmiPage", description="utmi_page (internal utm)"),
    ] = None
    """
    utmi_page (internal utm)
    """

    utmi_part: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="utmiPart"),
        pydantic.Field(alias="utmiPart", description="utmi_part (internal utm)"),
    ] = None
    """
    utmi_part (internal utm)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
