

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_ql_name import GraphQlName
from .stored_procedure_config_exposed_as import StoredProcedureConfigExposedAs


class StoredProcedureConfig(UniversalBaseModel):
    custom_name: typing.Optional[GraphQlName] = None
    exposed_as: StoredProcedureConfigExposedAs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
