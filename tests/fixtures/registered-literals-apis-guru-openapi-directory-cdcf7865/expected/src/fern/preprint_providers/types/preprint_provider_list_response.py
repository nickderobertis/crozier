

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .preprint_provider_list_response_attributes import PreprintProviderListResponseAttributes
from .preprint_provider_list_response_links import PreprintProviderListResponseLinks
from .preprint_provider_list_response_relationships import PreprintProviderListResponseRelationships


class PreprintProviderListResponse(UniversalBaseModel):
    attributes: typing.Optional[PreprintProviderListResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the preprint provider entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the preprint provider entity.
    """

    links: typing.Optional[PreprintProviderListResponseLinks] = pydantic.Field(default=None)
    """
    Links to alternative representations of the preprint entity.
    """

    relationships: typing.Optional[PreprintProviderListResponseRelationships] = pydantic.Field(default=None)
    """
    Links to other entities or entity collections that have a relationship to the preprint provider.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the preprint provider entity (`preprint_providers`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
