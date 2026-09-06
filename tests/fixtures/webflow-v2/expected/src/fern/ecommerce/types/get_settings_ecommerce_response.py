

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetSettingsEcommerceResponse(UniversalBaseModel):
    """
    Ecommerce settings for a Webflow Site
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="The identifier of the Site"),
    ] = None
    """
    The identifier of the Site
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Date that the Site was created on"),
    ] = None
    """
    Date that the Site was created on
    """

    default_currency: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="defaultCurrency"),
        pydantic.Field(alias="defaultCurrency", description="The three-letter ISO currency code for the Site"),
    ] = None
    """
    The three-letter ISO currency code for the Site
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
