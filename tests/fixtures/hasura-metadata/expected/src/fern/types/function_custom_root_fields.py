

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_ql_name import GraphQlName


class FunctionCustomRootFields(UniversalBaseModel):
    function: typing.Optional[GraphQlName] = None
    function_aggregate: typing.Optional[GraphQlName] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
