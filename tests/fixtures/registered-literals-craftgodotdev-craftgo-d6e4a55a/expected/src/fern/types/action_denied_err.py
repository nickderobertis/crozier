

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .suspension_reason import SuspensionReason


class ActionDeniedErr(UniversalBaseModel):
    """
    Forbidden error response (HTTP 403).
    """

    code: typing.Optional[str] = None
    reason: SuspensionReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
