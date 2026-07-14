

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .generic_notification_payload import GenericNotificationPayload
from .vuln_diff_result import VulnDiffResult


class VulnUpdateNotificationPayload(GenericNotificationPayload):
    annotations: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    List of Corresponding Image Annotations
    """

    diff_vulnerability_result: typing.Optional[VulnDiffResult] = None
    image_digest: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="imageDigest")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
