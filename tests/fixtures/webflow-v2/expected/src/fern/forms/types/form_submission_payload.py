

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .form_submission_payload_payload import FormSubmissionPayloadPayload


class FormSubmissionPayload(UniversalBaseModel):
    """
    The Webhook payload for when a form is submitted
    """

    trigger_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="triggerType"),
        pydantic.Field(alias="triggerType", description="The type of event that triggered the request"),
    ] = None
    """
    The type of event that triggered the request
    """

    payload: typing.Optional[FormSubmissionPayloadPayload] = pydantic.Field(default=None)
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
