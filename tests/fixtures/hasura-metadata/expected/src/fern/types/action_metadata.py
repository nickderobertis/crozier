

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_metadata_definition import ActionMetadataDefinition
from .action_permission_metadata import ActionPermissionMetadata
from .graph_ql_name import GraphQlName


class ActionMetadata(UniversalBaseModel):
    comment: typing.Optional[str] = None
    definition: ActionMetadataDefinition
    name: GraphQlName
    permissions: typing.Optional[typing.List[ActionPermissionMetadata]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
