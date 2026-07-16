

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .site import Site


class ListSitesResponse(UniversalBaseModel):
    """
    Represents a `ListSites` response. The response can include either `sites` or `errors`.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    sites: typing.Optional[typing.List[Site]] = pydantic.Field(default=None)
    """
    The sites that belong to the seller.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
