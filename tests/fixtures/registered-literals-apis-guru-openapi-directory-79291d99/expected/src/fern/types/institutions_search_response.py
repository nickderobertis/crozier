

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .institution import Institution
from .request_id import RequestId


class InstitutionsSearchResponse(UniversalBaseModel):
    """
    InstitutionsSearchResponse defines the response schema for `/institutions/search`
    """

    institutions: typing.List[Institution] = pydantic.Field()
    """
    An array of institutions matching the search criteria
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
