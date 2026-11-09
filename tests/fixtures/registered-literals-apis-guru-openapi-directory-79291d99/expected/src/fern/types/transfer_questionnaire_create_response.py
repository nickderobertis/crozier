

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class TransferQuestionnaireCreateResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/questionnaire/create`
    """

    onboarding_url: str = pydantic.Field()
    """
    Plaid-hosted onboarding URL that you will redirect the end customer to.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
