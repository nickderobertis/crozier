

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .preprint_provider_taxonomies_list_response_attributes import PreprintProviderTaxonomiesListResponseAttributes
from .preprint_provider_taxonomies_list_response_links import PreprintProviderTaxonomiesListResponseLinks


class PreprintProviderTaxonomiesListResponse(UniversalBaseModel):
    attributes: typing.Optional[PreprintProviderTaxonomiesListResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the taxonomy entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the taxonomy entity.
    """

    links: typing.Optional[PreprintProviderTaxonomiesListResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the taxonomy entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the taxonomy entity (`taxonomies`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
