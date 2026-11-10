

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .risk_check_linked_service import RiskCheckLinkedService


class RiskCheckPhone(UniversalBaseModel):
    """
    Result summary object specifying values for `phone` attributes of risk check.
    """

    linked_services: typing.List[RiskCheckLinkedService]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
