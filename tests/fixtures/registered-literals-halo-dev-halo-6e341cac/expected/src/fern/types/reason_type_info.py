

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReasonTypeInfo(UniversalBaseModel):
    """
    Reason type metadata used by notification preference UI.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    description of the reason type
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="display name of the reason type"),
    ] = None
    """
    display name of the reason type
    """

    name: str = pydantic.Field()
    """
    reason type <code>metadata.name</code>
    """

    ui_permissions: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="uiPermissions"),
        pydantic.Field(alias="uiPermissions", description="UI permissions required to manage this reason type"),
    ] = None
    """
    UI permissions required to manage this reason type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
