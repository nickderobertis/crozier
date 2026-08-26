

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .secret_keys_result_notification_op import SecretKeysResultNotificationOp
from .secret_keys_with_provider import SecretKeysWithProvider


class SecretKeysResultNotification(UniversalBaseModel):
    """
    Available secret keys from secret providers.

        Attributes:
            request_id: Request ID this responds to.
            secrets: Secret keys with provider info.
    """

    op: SecretKeysResultNotificationOp
    request_id: RequestId
    secrets: typing.List[SecretKeysWithProvider]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
