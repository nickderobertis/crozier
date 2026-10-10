

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_me_subject import GetMeSubject
from .me_session_type import MeSessionType


class Me(UniversalBaseModel):
    roles: typing.List[str] = pydantic.Field()
    """
    Roles for the authenticated caller.
    """

    subject: GetMeSubject
    tenant_id: str = pydantic.Field()
    """
    Tenant scope for the authenticated caller.
    """

    type: MeSessionType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
