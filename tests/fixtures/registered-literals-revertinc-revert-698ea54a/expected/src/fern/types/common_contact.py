

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .common_common_unified_fields import CommonCommonUnifiedFields
from .common_contact_read import CommonContactRead


class CommonContact(CommonCommonUnifiedFields, CommonContactRead):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
