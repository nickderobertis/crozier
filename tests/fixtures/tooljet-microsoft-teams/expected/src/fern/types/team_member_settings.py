

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TeamMemberSettings(UniversalBaseModel):
    allow_create_update_channels: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowCreateUpdateChannels"),
        pydantic.Field(alias="allowCreateUpdateChannels"),
    ] = None
    allow_create_private_channels: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowCreatePrivateChannels"),
        pydantic.Field(alias="allowCreatePrivateChannels"),
    ] = None
    allow_delete_channels: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDeleteChannels"), pydantic.Field(alias="allowDeleteChannels")
    ] = None
    allow_add_remove_apps: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowAddRemoveApps"), pydantic.Field(alias="allowAddRemoveApps")
    ] = None
    allow_create_update_remove_tabs: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowCreateUpdateRemoveTabs"),
        pydantic.Field(alias="allowCreateUpdateRemoveTabs"),
    ] = None
    allow_create_update_remove_connectors: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowCreateUpdateRemoveConnectors"),
        pydantic.Field(alias="allowCreateUpdateRemoveConnectors"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
