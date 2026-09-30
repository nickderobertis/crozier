

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .enum_value_definition import EnumValueDefinition
from .graph_ql_name import GraphQlName


class EnumTypeDefinition(UniversalBaseModel):
    description: typing.Optional[str] = None
    name: GraphQlName
    values: typing.List[EnumValueDefinition]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
