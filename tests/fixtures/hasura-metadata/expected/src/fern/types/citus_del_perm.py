

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .citus_bool_exp import CitusBoolExp
from .validate_input_input_webhook import ValidateInputInputWebhook


class CitusDelPerm(UniversalBaseModel):
    backend_only: typing.Optional[bool] = None
    filter: CitusBoolExp
    validate_input: typing.Optional[ValidateInputInputWebhook] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
