

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemPerkEntryDefinition(UniversalBaseModel):
    """
    An intrinsic perk on an item, and the requirements for it to be activated.
    """

    perk_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="perkHash"),
        pydantic.Field(
            alias="perkHash",
            description="A hash identifier for the DestinySandboxPerkDefinition being provided on the item.",
        ),
    ] = None
    """
    A hash identifier for the DestinySandboxPerkDefinition being provided on the item.
    """

    perk_visibility: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="perkVisibility"),
        pydantic.Field(
            alias="perkVisibility",
            description="Indicates whether this perk should be shown, or if it should be shown disabled.",
        ),
    ] = None
    """
    Indicates whether this perk should be shown, or if it should be shown disabled.
    """

    requirement_display_string: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requirementDisplayString"),
        pydantic.Field(
            alias="requirementDisplayString",
            description="If this perk is not active, this is the string to show for why it's not providing its benefits.",
        ),
    ] = None
    """
    If this perk is not active, this is the string to show for why it's not providing its benefits.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
