

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .channel_options_viber import ChannelOptionsViber
from .file_message_type import FileMessageType
from .send_message_request_four_three_file import SendMessageRequestFourThreeFile


class SendMessageRequestFourThree(ChannelOptionsViber, BaseMessageType):
    file: typing.Optional[SendMessageRequestFourThreeFile] = pydantic.Field(default=None)
    """
    An object containing details of the file to be sent. Note: allowed file types are `.doc,` `.docx`, `.rtf`, `.dot`, `.dotx`, `.odt`, `.odf`, `.fodt`, `.txt`, `.info`, `.pdf`, `.xps`, `.pdax`, `.eps`, `.xls`, `.xlsx`, `.ods`, `.fods`, `.csv`, `.xlsm`, `.xltx`. Maximum file size is 200MB
    """

    message_type: typing.Optional[FileMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `file` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
