

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CapabilityDocument(UniversalBaseModel):
    """
    The API groups, features, and limits that a deployment advertises.
    """

    api_groups: typing.List[str] = pydantic.Field()
    """
    The advertised API groups, as `group/version`. The deployment implements every required
    operation in each group.
    """

    features: typing.Optional[typing.Dict[str, bool]] = pydantic.Field(default=None)
    """
    Feature keys, and whether this deployment supports each one. An absent key means the feature
    isn't supported.
    """

    limits: typing.Optional[typing.Dict[str, int]] = pydantic.Field(default=None)
    """
    Advisory numeric limits that clients can use to check requests before sending them.
    """

    protocol_version: str = pydantic.Field()
    """
    The protocol version, `v0`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
