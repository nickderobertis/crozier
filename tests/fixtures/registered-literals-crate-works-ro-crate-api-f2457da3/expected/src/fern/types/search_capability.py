

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .facet_capability import FacetCapability
from .filter_capability import FilterCapability


class SearchCapability(UniversalBaseModel):
    """
    Declares what the implementation's search endpoint supports — the filters that may be used in search requests and the facets returned in search responses.

    Every field declared in `facets` MUST also be declared in `filters`, so that clients can always turn a facet value the user clicks into a filter on the next request. Filter-only fields (for example date fields, which are filterable but not meaningful as facets) are permitted.
    """

    filters: typing.Dict[str, FilterCapability] = pydantic.Field()
    """
    The fields that may be used in the search request's `filters` object, as a map of field name to a declaration of the field's type and display label. Requests using a field not declared here MUST be rejected with a 400 `ValidationError`.
    """

    facets: typing.Dict[str, FacetCapability] = pydantic.Field()
    """
    The facet fields the implementation supports in search responses, as a map of facet field name to its declaration. Every field listed here MUST also appear in `filters`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
