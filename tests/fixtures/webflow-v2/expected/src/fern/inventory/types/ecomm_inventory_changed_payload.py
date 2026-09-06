

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .ecomm_inventory_changed_payload_payload import EcommInventoryChangedPayloadPayload
from .ecomm_inventory_changed_payload_trigger_type import EcommInventoryChangedPayloadTriggerType


class EcommInventoryChangedPayload(UniversalBaseModel):
    trigger_type: typing_extensions.Annotated[
        typing.Optional[EcommInventoryChangedPayloadTriggerType],
        FieldMetadata(alias="triggerType"),
        pydantic.Field(alias="triggerType"),
    ] = None
    payload: typing.Optional[EcommInventoryChangedPayloadPayload] = pydantic.Field(default=None)
    """
    The availabile inventory for an item
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
