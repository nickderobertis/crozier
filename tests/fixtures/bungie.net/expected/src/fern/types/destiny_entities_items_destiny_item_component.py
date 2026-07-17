

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress


class DestinyEntitiesItemsDestinyItemComponent(UniversalBaseModel):
    """
    The base item component, filled with properties that are generally useful to know in any item request or that don't feel worthwhile to put in their own component.
    """

    bind_status: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="bindStatus"),
        pydantic.Field(
            alias="bindStatus", description="If the item is bound to a location, it will be specified in this enum."
        ),
    ] = None
    """
    If the item is bound to a location, it will be specified in this enum.
    """

    bucket_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="bucketHash"),
        pydantic.Field(
            alias="bucketHash",
            description="The hash identifier for the specific inventory bucket in which the item is located.",
        ),
    ] = None
    """
    The hash identifier for the specific inventory bucket in which the item is located.
    """

    expiration_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expirationDate"),
        pydantic.Field(
            alias="expirationDate", description="If the item can expire, this is the date at which it will/did expire."
        ),
    ] = None
    """
    If the item can expire, this is the date at which it will/did expire.
    """

    is_wrapper: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isWrapper"),
        pydantic.Field(
            alias="isWrapper",
            description='If this is true, the object is actually a "wrapper" of the object it\'s representing. This means that it\'s not the actual item itself, but rather an item that must be "opened" in game before you have and can use the item.\r\n Wrappers are an evolution of "bundles", which give an easy way to let you preview the contents of what you purchased while still letting you get a refund before you "open" it.',
        ),
    ] = None
    """
    If this is true, the object is actually a "wrapper" of the object it's representing. This means that it's not the actual item itself, but rather an item that must be "opened" in game before you have and can use the item.
     Wrappers are an evolution of "bundles", which give an easy way to let you preview the contents of what you purchased while still letting you get a refund before you "open" it.
    """

    item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemHash"),
        pydantic.Field(
            alias="itemHash",
            description="The identifier for the item's definition, which is where most of the useful static information for the item can be found.",
        ),
    ] = None
    """
    The identifier for the item's definition, which is where most of the useful static information for the item can be found.
    """

    item_instance_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemInstanceId"),
        pydantic.Field(
            alias="itemInstanceId",
            description="If the item is instanced, it will have an instance ID. Lack of an instance ID implies that the item has no distinct local qualities aside from stack size.",
        ),
    ] = None
    """
    If the item is instanced, it will have an instance ID. Lack of an instance ID implies that the item has no distinct local qualities aside from stack size.
    """

    item_value_visibility: typing_extensions.Annotated[
        typing.Optional[typing.List[bool]],
        FieldMetadata(alias="itemValueVisibility"),
        pydantic.Field(
            alias="itemValueVisibility",
            description="If available, a list that describes which item values (rewards) should be shown (true) or hidden (false).",
        ),
    ] = None
    """
    If available, a list that describes which item values (rewards) should be shown (true) or hidden (false).
    """

    location: typing.Optional[int] = pydantic.Field(default=None)
    """
    An easy reference for where the item is located. Redundant if you got the item from an Inventory, but useful when making detail calls on specific items.
    """

    lockable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the item can be locked, this will indicate that state.
    """

    metric_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="metricHash"),
        pydantic.Field(
            alias="metricHash",
            description="The identifier for the currently-selected metric definition, to be displayed on the emblem nameplate.",
        ),
    ] = None
    """
    The identifier for the currently-selected metric definition, to be displayed on the emblem nameplate.
    """

    metric_objective: typing_extensions.Annotated[
        typing.Optional[DestinyQuestsDestinyObjectiveProgress],
        FieldMetadata(alias="metricObjective"),
        pydantic.Field(
            alias="metricObjective",
            description="The objective progress for the currently-selected metric definition, to be displayed on the emblem nameplate.",
        ),
    ] = None
    """
    The objective progress for the currently-selected metric definition, to be displayed on the emblem nameplate.
    """

    override_style_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="overrideStyleItemHash"),
        pydantic.Field(
            alias="overrideStyleItemHash",
            description="If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold.\r\nIf you don't do this, certain items whose styles are being overridden by socketed items - such as the \"Recycle Shader\" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.",
        ),
    ] = None
    """
    If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold.
    If you don't do this, certain items whose styles are being overridden by socketed items - such as the "Recycle Shader" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    The quantity of the item in this stack. Note that Instanced items cannot stack. If an instanced item, this value will always be 1 (as the stack has exactly one item in it)
    """

    state: typing.Optional[int] = pydantic.Field(default=None)
    """
    A flags enumeration indicating the transient/custom states of the item that affect how it is rendered: whether it's tracked or locked for example, or whether it has a masterwork plug inserted.
    """

    tooltip_notification_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="tooltipNotificationIndexes"),
        pydantic.Field(
            alias="tooltipNotificationIndexes",
            description="If this is populated, it is a list of indexes into DestinyInventoryItemDefinition.tooltipNotifications for any special tooltip messages that need to be shown for this item.",
        ),
    ] = None
    """
    If this is populated, it is a list of indexes into DestinyInventoryItemDefinition.tooltipNotifications for any special tooltip messages that need to be shown for this item.
    """

    transfer_status: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="transferStatus"),
        pydantic.Field(
            alias="transferStatus",
            description="If there is a known error state that would cause this item to not be transferable, this Flags enum will indicate all of those error states. Otherwise, it will be 0 (CanTransfer).",
        ),
    ] = None
    """
    If there is a known error state that would cause this item to not be transferable, this Flags enum will indicate all of those error states. Otherwise, it will be 0 (CanTransfer).
    """

    version_number: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="versionNumber"),
        pydantic.Field(
            alias="versionNumber",
            description="The version of this item, used to index into the versions list in the item definition quality block.",
        ),
    ] = None
    """
    The version of this item, used to index into the versions list in the item definition quality block.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
