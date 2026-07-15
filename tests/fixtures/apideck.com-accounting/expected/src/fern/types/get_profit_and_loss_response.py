

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .profit_and_loss import ProfitAndLoss


class GetProfitAndLossResponse(UniversalBaseModel):
    data: ProfitAndLoss
    operation: str = pydantic.Field()
    """
    Operation performed
    """

    resource: str = pydantic.Field()
    """
    Unified API resource name
    """

    service: str = pydantic.Field()
    """
    Apideck ID of service provider
    """

    status: str = pydantic.Field()
    """
    HTTP Response Status
    """

    status_code: int = pydantic.Field()
    """
    HTTP Response Status Code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(GetProfitAndLossResponse)
