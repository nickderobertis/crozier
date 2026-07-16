

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyMaterialRequirement(UniversalBaseModel):
    """
    Many actions relating to items require you to expend materials: - Activating a talent node - Inserting a plug into a socket The items will refer to material requirements by a materialRequirementsHash in these cases, and this is the definition for those requirements in terms of the item required, how much of it is required and other interesting info. This is one of the rare/strange times where a single contract class is used both in definitions *and* in live data response contracts. I'm not sure yet whether I regret that.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount of the material required.
    """

    count_is_constant: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="countIsConstant"),
        pydantic.Field(
            alias="countIsConstant",
            description="If true, the material requirement count value is constant. Since The Witch Queen expansion, some material requirement counts can be dynamic and will need to be returned with an API call.",
        ),
    ] = None
    """
    If true, the material requirement count value is constant. Since The Witch Queen expansion, some material requirement counts can be dynamic and will need to be returned with an API call.
    """

    delete_on_action: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="deleteOnAction"),
        pydantic.Field(
            alias="deleteOnAction",
            description="If True, the material will be removed from the character's inventory when the action is performed.",
        ),
    ] = None
    """
    If True, the material will be removed from the character's inventory when the action is performed.
    """

    item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemHash"),
        pydantic.Field(
            alias="itemHash",
            description="The hash identifier of the material required. Use it to look up the material's DestinyInventoryItemDefinition.",
        ),
    ] = None
    """
    The hash identifier of the material required. Use it to look up the material's DestinyInventoryItemDefinition.
    """

    omit_from_requirements: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="omitFromRequirements"),
        pydantic.Field(
            alias="omitFromRequirements",
            description="If True, this requirement is \"silent\": don't bother showing it in a material requirements display. I mean, I'm not your mom: I'm not going to tell you you *can't* show it. But we won't show it in our UI.",
        ),
    ] = None
    """
    If True, this requirement is "silent": don't bother showing it in a material requirements display. I mean, I'm not your mom: I'm not going to tell you you *can't* show it. But we won't show it in our UI.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
