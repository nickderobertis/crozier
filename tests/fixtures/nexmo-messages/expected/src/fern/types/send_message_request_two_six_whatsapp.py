

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .send_message_request_two_six_whatsapp_policy import SendMessageRequestTwoSixWhatsappPolicy


class SendMessageRequestTwoSixWhatsapp(UniversalBaseModel):
    locale: str = pydantic.Field()
    """
    The [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag) language of the template. See [the WhatsApp documentation](https://developers.facebook.com/docs/whatsapp/api/messages/message-templates#supported-languages-) for supported languages.
    """

    policy: typing.Optional[SendMessageRequestTwoSixWhatsappPolicy] = pydantic.Field(default=None)
    """
    Policy for resolving what language template to use. As of right now the only valid choice is `deterministic`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
