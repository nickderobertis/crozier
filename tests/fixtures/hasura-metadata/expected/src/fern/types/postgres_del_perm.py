

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .postgres_bool_exp import PostgresBoolExp
from .validate_input_input_webhook import ValidateInputInputWebhook


class PostgresDelPerm(UniversalBaseModel):
    backend_only: typing.Optional[bool] = None
    filter: PostgresBoolExp
    validate_input: typing.Optional[ValidateInputInputWebhook] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
