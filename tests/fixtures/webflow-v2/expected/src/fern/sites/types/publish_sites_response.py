

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .publish_sites_response_custom_domains_item import PublishSitesResponseCustomDomainsItem
from .publish_sites_response_publish_scope import PublishSitesResponsePublishScope


class PublishSitesResponse(UniversalBaseModel):
    custom_domains: typing_extensions.Annotated[
        typing.Optional[typing.List[PublishSitesResponseCustomDomainsItem]],
        FieldMetadata(alias="customDomains"),
        pydantic.Field(alias="customDomains", description="Array of domains objects"),
    ] = None
    """
    Array of domains objects
    """

    publish_to_webflow_subdomain: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="publishToWebflowSubdomain"),
        pydantic.Field(alias="publishToWebflowSubdomain", description="Flag for publishing to webflow.io subdomain"),
    ] = None
    """
    Flag for publishing to webflow.io subdomain
    """

    publish_scope: typing_extensions.Annotated[
        typing.Optional[PublishSitesResponsePublishScope],
        FieldMetadata(alias="publishScope"),
        pydantic.Field(alias="publishScope", description="Whether the site or an individual page was published"),
    ] = None
    """
    Whether the site or an individual page was published
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
