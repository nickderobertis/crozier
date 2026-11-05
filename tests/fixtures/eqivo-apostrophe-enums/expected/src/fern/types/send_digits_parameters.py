

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .send_digits_parameters_leg import SendDigitsParametersLeg


class SendDigitsParameters(UniversalBaseModel):
    call_uuid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallUUID"),
        pydantic.Field(alias="CallUUID", description="Unique identifier of the call to send DTMF to"),
    ]
    """
    Unique identifier of the call to send DTMF to
    """

    digits: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Digits"),
        pydantic.Field(
            alias="Digits",
            description="DTMF tones to be sent; each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string",
        ),
    ]
    """
    DTMF tones to be sent; each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string
    """

    leg: typing_extensions.Annotated[
        typing.Optional[SendDigitsParametersLeg],
        FieldMetadata(alias="Leg"),
        pydantic.Field(
            alias="Leg",
            description="Call leg(s) to which DTMFs will be sent; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.",
        ),
    ] = None
    """
    Call leg(s) to which DTMFs will be sent; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
