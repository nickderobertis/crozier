

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ListSitesResponseSitesItemLocalesPrimary(UniversalBaseModel):
    """
    The primary locale for the site or application.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the locale.
    """

    cms_locale_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cmsLocaleId"),
        pydantic.Field(alias="cmsLocaleId", description="A CMS-specific identifier for the locale."),
    ] = None
    """
    A CMS-specific identifier for the locale.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the locale is enabled.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="The display name of the locale, typically in English."),
    ] = None
    """
    The display name of the locale, typically in English.
    """

    display_image_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayImageId"),
        pydantic.Field(
            alias="displayImageId", description="An optional ID for an image associated with the locale, nullable."
        ),
    ] = None
    """
    An optional ID for an image associated with the locale, nullable.
    """

    redirect: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines if requests should redirect to the locale's subdirectory.
    """

    subdirectory: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subdirectory path for the locale, used in URLs.
    """

    tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    A tag or code representing the locale, often following a standard format like 'en-US'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
