

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .taxonomies_list_response_item_attributes import TaxonomiesListResponseItemAttributes
from .taxonomies_list_response_item_links import TaxonomiesListResponseItemLinks


class TaxonomiesListResponseItem(UniversalBaseModel):
    attributes: typing.Optional[TaxonomiesListResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the taxonomy entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the taxonomy entity.
    """

    links: typing.Optional[TaxonomiesListResponseItemLinks] = pydantic.Field(default=None)
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
