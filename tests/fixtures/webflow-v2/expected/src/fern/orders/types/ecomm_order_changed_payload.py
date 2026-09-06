

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .ecomm_order_changed_payload_payload import EcommOrderChangedPayloadPayload


class EcommOrderChangedPayload(UniversalBaseModel):
    """
    The Webhook payload for when an order is updated
    """

    trigger_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="triggerType"),
        pydantic.Field(alias="triggerType", description="The type of event that triggered the request"),
    ] = None
    """
    The type of event that triggered the request
    """

    payload: typing.Optional[EcommOrderChangedPayloadPayload] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
