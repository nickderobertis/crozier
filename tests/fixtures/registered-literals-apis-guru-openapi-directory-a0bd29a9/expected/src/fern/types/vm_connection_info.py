

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .vm_connection_type import VmConnectionType


class VmConnectionInfo(UniversalBaseModel):
    connection_type: typing_extensions.Annotated[
        typing.Optional[VmConnectionType], FieldMetadata(alias="connectionType"), pydantic.Field(alias="connectionType")
    ] = None
    live_share_workspace_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="liveShareWorkspaceId"), pydantic.Field(alias="liveShareWorkspaceId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
