

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tool_entry_floor import ToolEntryFloor


class ToolEntry(UniversalBaseModel):
    """
    Locale-resolved tool registry projection returned by the api
    service's hitlGetTools (cached 5 minutes). The `floor` here is the
    wire-effective HITL floor — `auto` or `manual`. Distinct from
    `ToolRegistryEntry` which is the orchestrator's internal-only
    projection that may carry `forbidden`.
    """

    name: str
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    display_name_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayNameKey"), pydantic.Field(alias="displayNameKey")
    ] = None
    platform: str
    floor: ToolEntryFloor
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
