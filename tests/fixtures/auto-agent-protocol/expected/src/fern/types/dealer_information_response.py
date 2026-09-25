

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dealer_information import DealerInformation
from .dealer_information_response_type import DealerInformationResponseType


class DealerInformationResponse(UniversalBaseModel):
    """
    Typed AAP response for the `dealer.information` skill. Wraps a DealerInformation object inside the standard AAP response envelope (`{ type, data, message? }`). Carried inside an A2A `Message.parts[].data` DataPart returned from the `SendMessage` operation.
    """

    type: DealerInformationResponseType
    data: DealerInformation
    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional contextual note from the dealer or LLM. MAY be omitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
