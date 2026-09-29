

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .graph_ql_name import GraphQlName
from .remote_field_customization import RemoteFieldCustomization
from .remote_type_customization import RemoteTypeCustomization


class RemoteSchemaCustomization(UniversalBaseModel):
    field_names: typing.Optional[typing.List[RemoteFieldCustomization]] = None
    root_fields_namespace: typing.Optional[GraphQlName] = None
    type_names: typing.Optional[RemoteTypeCustomization] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
