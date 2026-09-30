

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_ql_name import GraphQlName


class EnumValueDefinition(UniversalBaseModel):
    description: typing.Optional[str] = None
    is_deprecated: typing.Optional[bool] = None
    value: GraphQlName

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
