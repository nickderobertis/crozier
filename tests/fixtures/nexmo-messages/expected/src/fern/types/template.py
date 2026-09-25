

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .template_message_type import TemplateMessageType
from .template_template import TemplateTemplate


class Template(BaseMessageType):
    message_type: typing.Optional[TemplateMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `template` in this field
    """

    template: TemplateTemplate

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
