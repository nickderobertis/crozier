

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .institution import Institution
from .request_id import RequestId


class InstitutionsGetByIdResponse(UniversalBaseModel):
    """
    InstitutionsGetByIdResponse defines the response schema for `/institutions/get_by_id`
    """

    institution: Institution
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
