

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_validity_response_data import GetValidityResponseData
from .get_validity_response_meta import GetValidityResponseMeta


class GetValidityResponse(UniversalBaseModel):
    meta: GetValidityResponseMeta
    data: GetValidityResponseData = pydantic.Field()
    """
    Validation of API Key
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
