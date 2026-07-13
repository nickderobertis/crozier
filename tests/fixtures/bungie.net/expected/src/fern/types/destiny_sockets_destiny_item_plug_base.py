

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinySocketsDestinyItemPlugBase(UniversalBaseModel):
    can_insert: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="canInsert")] = pydantic.Field(
        default=None
    )
    """
    If true, this plug has met all of its insertion requirements. Big if true.
    """

    enable_fail_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="enableFailIndexes")
    ] = pydantic.Field(default=None)
    """
    If a plug is not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled.
    This list will be empty if the plug is enabled.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, this plug will provide its benefits while inserted.
    """

    insert_fail_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="insertFailIndexes")
    ] = pydantic.Field(default=None)
    """
    If the plug cannot be inserted for some reason, this will have the indexes into the plug item definition's plug.insertionRules property, so you can show the reasons why it can't be inserted.
    This list will be empty if the plug can be inserted.
    """

    plug_item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="plugItemHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash identifier of the DestinyInventoryItemDefinition that represents this plug.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
