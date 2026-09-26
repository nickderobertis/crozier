

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChannelToPhone(UniversalBaseModel):
    """
    Connect to a Phone (PSTN) number
    """

    dtmf_answer: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dtmfAnswer"),
        pydantic.Field(
            alias="dtmfAnswer",
            description="Provide [DTMF digits](https://developer.nexmo.com/voice/voice-api/guides/dtmf) to send when the call is answered",
        ),
    ] = None
    """
    Provide [DTMF digits](https://developer.nexmo.com/voice/voice-api/guides/dtmf) to send when the call is answered
    """

    number: str = pydantic.Field()
    """
    The phone number to connect to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
