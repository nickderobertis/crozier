

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetReadReceiptsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    user_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    An array of IDs of users who have marked the target message as
    read and whose read status is available to the current user.
    
    The IDs of users who have disabled sending read receipts
    (`"send_read_receipts": false`) will never appear in the response,
    nor will the message's sender. Additionally, the IDs of any users
    who have been muted by the current user or who have muted the
    current user will not be included in the response.
    
    The current user's ID will appear if they have marked the target
    message as read.
    
    **Changes**: Prior to Zulip 6.0 (feature level 143), the IDs of
    users who have been muted by or have muted the current user were
    included in the response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
