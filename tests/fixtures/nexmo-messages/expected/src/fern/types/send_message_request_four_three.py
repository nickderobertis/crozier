

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_message_type import BaseMessageType
from .channel_options_viber_channel import ChannelOptionsViberChannel
from .channel_options_viber_viber_service import ChannelOptionsViberViberService
from .file_message_type import FileMessageType
from .from_id import FromId
from .send_message_request_four_three_file import SendMessageRequestFourThreeFile
from .to_number import ToNumber


class SendMessageRequestFourThree(BaseMessageType):
    to: ToNumber
    from_: typing_extensions.Annotated[FromId, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    channel: ChannelOptionsViberChannel = pydantic.Field()
    """
    The channel to send to. You must provide `viber_service` in this field
    """

    file: SendMessageRequestFourThreeFile = pydantic.Field()
    """
    An object containing details of the file to be sent. Note: allowed file types are `.doc,` `.docx`, `.rtf`, `.dot`, `.dotx`, `.odt`, `.odf`, `.fodt`, `.txt`, `.info`, `.pdf`, `.xps`, `.pdax`, `.eps`, `.xls`, `.xlsx`, `.ods`, `.fods`, `.csv`, `.xlsm`, `.xltx`. Maximum file size is 200MB
    """

    viber_service: typing.Optional[ChannelOptionsViberViberService] = None
    message_type: FileMessageType = pydantic.Field()
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
