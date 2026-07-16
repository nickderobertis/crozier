

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .operator_configuration import OperatorConfiguration
from .workspace_id import WorkspaceId


class OperationCreate(UniversalBaseModel):
    name: str
    operator_configuration: typing_extensions.Annotated[
        OperatorConfiguration,
        FieldMetadata(alias="operatorConfiguration"),
        pydantic.Field(alias="operatorConfiguration"),
    ]
    workspace_id: typing_extensions.Annotated[
        WorkspaceId, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
