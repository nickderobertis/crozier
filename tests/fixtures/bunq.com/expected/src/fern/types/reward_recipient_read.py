

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .label_user import LabelUser


class RewardRecipientRead(UniversalBaseModel):
    amount_reward: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount that will be/was awarded as reward for the reward.
    """

    counterparty_alias: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The alias of the other user eligible for the reward award.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time the reward was created.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the reward.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the reward.
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subStatus of the reward.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the reward.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time the reward was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
