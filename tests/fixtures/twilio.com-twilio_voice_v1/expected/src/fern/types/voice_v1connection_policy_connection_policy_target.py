

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VoiceV1ConnectionPolicyConnectionPolicyTarget(UniversalBaseModel):
    account_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Target resource.
    """

    connection_policy_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the Connection Policy that owns the Target.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the target is enabled. The default is `true`.
    """

    friendly_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The string that you assigned to describe the resource.
    """

    priority: typing.Optional[int] = pydantic.Field(default=None)
    """
    The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target.
    """

    sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that we created to identify the Target resource.
    """

    target: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SIP address you want Twilio to route your calls to. This must be a `sip:` schema. `sips` is NOT supported.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of the resource.
    """

    weight: typing.Optional[int] = pydantic.Field(default=None)
    """
    The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
