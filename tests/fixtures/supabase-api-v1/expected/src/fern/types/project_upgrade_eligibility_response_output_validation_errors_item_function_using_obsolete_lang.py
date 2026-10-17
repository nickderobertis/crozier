

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItemFunctionUsingObsoleteLang(UniversalBaseModel):
    schema_name: str
    function_name: str
    lang_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
