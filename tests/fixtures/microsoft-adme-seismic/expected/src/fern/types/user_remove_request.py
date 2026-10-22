

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserRemoveRequest(UniversalBaseModel):
    email: str = pydantic.Field()
    """
    Email address of the user. Note that this field is used as a principal identifer for entitlements-svc and be configured using the env variable USER_ID_CLAIM_FOR_ENTITLEMENTS_SVC in the Seismic DMS runtime.
    """

    path: str = pydantic.Field()
    """
    Seismic store path in the format sd://tenant/subproject.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
