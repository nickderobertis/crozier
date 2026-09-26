

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dealer_information_request_type import DealerInformationRequestType


class DealerInformationRequest(UniversalBaseModel):
    """
    Typed AAP request for the `dealer.information` skill. The request carries no parameters; it asks for the dealer's static profile. Carried inside an A2A `Message.parts[].data` DataPart via the A2A `SendMessage` operation.
    """

    type: DealerInformationRequestType = pydantic.Field()
    """
    AAP message type. Skill ID plus role.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
