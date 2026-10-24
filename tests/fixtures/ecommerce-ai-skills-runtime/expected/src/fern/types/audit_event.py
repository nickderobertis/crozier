

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AuditEvent(UniversalBaseModel):
    id: str
    tenant_id: str
    actor_user_id: typing.Optional[str] = None
    request_id: str
    action: str
    resource_type: str
    resource_id: typing.Optional[str] = None
    outcome: str
    metadata: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Tenant audit metadata; runtime bounds its serialized object to 20
    """

    created_at: dt.datetime
    previous_hash: str
    event_hash: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
