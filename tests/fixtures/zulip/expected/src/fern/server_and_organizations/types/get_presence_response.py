

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.legacy_presence_format import LegacyPresenceFormat


class GetPresenceResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    server_timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    The time when the server fetched the `presences` data included
    in the response.
    """

    presences: typing.Optional[typing.Dict[str, typing.Dict[str, LegacyPresenceFormat]]] = pydantic.Field(default=None)
    """
    A dictionary where each entry describes the presence details
    of a user in the Zulip organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
