

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeviceServer(UniversalBaseModel):
    description: str = pydantic.Field()
    """
    The description of the DeviceServer. This is only for your own reference when reading the DeviceServer again.
    """

    permitted_ips: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of IPs (v4 or v6) this DeviceServer will be able to do calls from. These will be linked to the API key.
    """

    secret: str = pydantic.Field()
    """
    The API key. You can request an API key in the bunq app.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
