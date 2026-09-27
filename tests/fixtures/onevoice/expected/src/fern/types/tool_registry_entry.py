

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tool_floor import ToolFloor


class ToolRegistryEntry(UniversalBaseModel):
    """
    Orchestrator's internal tool registry projection. The `floor` may
    carry `forbidden` (in addition to `auto` / `manual`); the api side
    uses `ToolEntry` (auto/manual only).
    """

    name: str
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    display_name_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayNameKey"), pydantic.Field(alias="displayNameKey")
    ] = None
    platform: str
    floor: ToolFloor
    editable_fields: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="editableFields"), pydantic.Field(alias="editableFields")
    ]
    description: str
    user_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="userDescription"), pydantic.Field(alias="userDescription")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
