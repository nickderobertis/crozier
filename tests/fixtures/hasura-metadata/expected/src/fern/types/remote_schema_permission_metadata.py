

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_schema_permission_definition import RemoteSchemaPermissionDefinition


class RemoteSchemaPermissionMetadata(UniversalBaseModel):
    comment: typing.Optional[str] = None
    definition: RemoteSchemaPermissionDefinition
    role: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
