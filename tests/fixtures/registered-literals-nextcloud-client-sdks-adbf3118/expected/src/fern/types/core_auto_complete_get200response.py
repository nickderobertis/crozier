

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_auto_complete_get200response_ocs import CoreAutoCompleteGet200ResponseOcs


class CoreAutoCompleteGet200Response(UniversalBaseModel):
    ocs: CoreAutoCompleteGet200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
