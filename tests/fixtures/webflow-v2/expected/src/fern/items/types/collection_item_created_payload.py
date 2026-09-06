

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .collection_item_created_payload_payload import CollectionItemCreatedPayloadPayload
from .collection_item_created_payload_trigger_type import CollectionItemCreatedPayloadTriggerType


class CollectionItemCreatedPayload(UniversalBaseModel):
    """
    The Webhook payload for when a Collection Item is created
    """

    trigger_type: typing_extensions.Annotated[
        CollectionItemCreatedPayloadTriggerType,
        FieldMetadata(alias="triggerType"),
        pydantic.Field(alias="triggerType", description="The type of event that triggered the request"),
    ]
    """
    The type of event that triggered the request
    """

    payload: CollectionItemCreatedPayloadPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
