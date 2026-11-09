

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .spend_policy_type import SpendPolicyType


class SpendPolicy(UniversalBaseModel):
    """
    Polymorphic spend policy serialized by `go.sia.tech/core/types.SpendPolicy`.
    """

    type: SpendPolicyType = pydantic.Field()
    """
    Policy discriminator.
    """

    policy: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Policy-specific payload; structure depends on the `type`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
