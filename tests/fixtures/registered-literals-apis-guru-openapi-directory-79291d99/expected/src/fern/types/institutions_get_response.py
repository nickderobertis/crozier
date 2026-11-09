

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .institution import Institution
from .request_id import RequestId


class InstitutionsGetResponse(UniversalBaseModel):
    """
    InstitutionsGetResponse defines the response schema for `/institutions/get`
    """

    institutions: typing.List[Institution] = pydantic.Field()
    """
    A list of Plaid institutions
    """

    request_id: RequestId
    total: int = pydantic.Field()
    """
    The total number of institutions available via this endpoint
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
