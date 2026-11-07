

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ValidationBlockYaml(UniversalBaseModel):
    label: str
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    complete_criterion: typing.Optional[str] = None
    terminate_criterion: typing.Optional[str] = None
    error_code_mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    parameter_keys: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
