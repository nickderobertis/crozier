

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employer import Employer
from .request_id import RequestId


class EmployersSearchResponse(UniversalBaseModel):
    """
    EmployersSearchResponse defines the response schema for `/employers/search`.
    """

    employers: typing.List[Employer] = pydantic.Field()
    """
    A list of employers matching the search criteria.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
