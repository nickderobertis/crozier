

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_inventory_response_inventory_type import ListInventoryResponseInventoryType


class ListInventoryResponse(UniversalBaseModel):
    """
    The availabile inventory for an item
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for a SKU item
    """

    quantity: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total quantity of items remaining in inventory (if inventoryType is finite)
    """

    inventory_type: typing_extensions.Annotated[
        typing.Optional[ListInventoryResponseInventoryType],
        FieldMetadata(alias="inventoryType"),
        pydantic.Field(alias="inventoryType", description="infinite or finite"),
    ] = None
    """
    infinite or finite
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
