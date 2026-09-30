

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_config_exposed_as import FunctionConfigExposedAs
from .function_custom_root_fields import FunctionCustomRootFields
from .graph_ql_name import GraphQlName


class FunctionConfig(UniversalBaseModel):
    custom_name: typing.Optional[GraphQlName] = None
    custom_root_fields: typing.Optional[FunctionCustomRootFields] = None
    exposed_as: typing.Optional[FunctionConfigExposedAs] = None
    response: typing.Optional[typing.Dict[str, typing.Any]] = None
    session_argument: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
