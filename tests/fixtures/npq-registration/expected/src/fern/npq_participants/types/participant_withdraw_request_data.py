

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_withdraw_request_data_attributes import ParticipantWithdrawRequestDataAttributes


class ParticipantWithdrawRequestData(UniversalBaseModel):
    """
    A participant withdraw request data
    """

    type: str = pydantic.Field()
    """
    The data typed
    """

    attributes: ParticipantWithdrawRequestDataAttributes = pydantic.Field()
    """
    A participant withdraw request attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
