

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_tollfree_verification_response_meta import ListTollfreeVerificationResponseMeta
from .messaging_v1tollfree_verification import MessagingV1TollfreeVerification


class ListTollfreeVerificationResponse(UniversalBaseModel):
    meta: typing.Optional[ListTollfreeVerificationResponseMeta] = None
    verifications: typing.Optional[typing.List[MessagingV1TollfreeVerification]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
