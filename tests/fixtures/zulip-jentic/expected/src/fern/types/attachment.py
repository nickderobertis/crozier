

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Attachment(UniversalBaseModel):
    """
    Dictionary containing details of a file uploaded by a user.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique ID for the attachment.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the uploaded file.
    """

    path_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A representation of the path of the file within the
    repository of user-uploaded files. If the `path_id` of a
    file is `{realm_id}/ab/cdef/temp_file.py`, its URL will be:
    `{server_url}/user_uploads/{realm_id}/ab/cdef/temp_file.py`.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of the file in bytes.
    """

    create_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time when the attachment was uploaded as a UNIX timestamp.
    
    **Changes**: Before Zulip 12.0 (feature level 443), this value
    was milliseconds since the epoch, not seconds.
    
    Changed in Zulip 3.0 (feature level 22). This field was
    previously a floating point number.
    """

    message_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array containing the IDs of messages that reference this
    [uploaded file](/api/upload-file). This includes messages
    sent by any user in the Zulip organization who sent a
    message containing a link to the uploaded file.
    
    **Changes**: In Zulip 12.0 (feature level 472), this
    replaced the previous `messages` field, which was an array
    of objects containing both `id` and `date_sent` properties.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
