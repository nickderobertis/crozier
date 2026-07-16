

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyVendorInventoryFlyoutBucketDefinition(UniversalBaseModel):
    """
    Information about a single inventory bucket in a vendor flyout UI and how it is shown.
    """

    collapsible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, the inventory bucket should be able to be collapsed visually.
    """

    inventory_bucket_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="inventoryBucketHash"),
        pydantic.Field(alias="inventoryBucketHash", description="The inventory bucket whose contents should be shown."),
    ] = None
    """
    The inventory bucket whose contents should be shown.
    """

    sort_items_by: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sortItemsBy"),
        pydantic.Field(alias="sortItemsBy", description="The methodology to use for sorting items from the flyout."),
    ] = None
    """
    The methodology to use for sorting items from the flyout.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
