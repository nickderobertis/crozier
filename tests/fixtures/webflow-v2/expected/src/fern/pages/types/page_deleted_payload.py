

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .page_deleted_payload_payload import PageDeletedPayloadPayload


class PageDeletedPayload(UniversalBaseModel):
    """
    The Webhook payload for when a Page is deleted
    """

    trigger_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="triggerType"),
        pydantic.Field(alias="triggerType", description="The type of event that triggered the request"),
    ] = None
    """
    The type of event that triggered the request
    """

    payload: typing.Optional[PageDeletedPayloadPayload] = pydantic.Field(default=None)
    """
    The payload of data sent from Webflow
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
