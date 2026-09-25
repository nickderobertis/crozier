

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.attachment import Attachment


class UpdateMessageResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    detached_uploads: typing.Optional[typing.List[Attachment]] = pydantic.Field(default=None)
    """
    Details on all files uploaded by the acting user whose only references
    were removed when editing this message. Clients should ask the acting user
    if they wish to delete the uploaded files returned in this response,
    which might otherwise remain visible only in message edit history.
    
    Note that [access to message edit history][edit-history-access]
    is configurable; this detail may be important in presenting the
    question clearly to users.
    
    New in Zulip 10.0 (feature level 285).
    
    [edit-history-access]: /help/restrict-message-edit-history-access
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
