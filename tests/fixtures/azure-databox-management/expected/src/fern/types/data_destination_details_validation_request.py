

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .destination_account_details import DestinationAccountDetails
from .validation_input_request import ValidationInputRequest


class DataDestinationDetailsValidationRequest(ValidationInputRequest):
    """
    Request to validate data destination details.
    """

    destination_account_details: typing_extensions.Annotated[
        typing.List[DestinationAccountDetails],
        FieldMetadata(alias="destinationAccountDetails"),
        pydantic.Field(alias="destinationAccountDetails", description="Destination account details list."),
    ]
    """
    Destination account details list.
    """

    location: str = pydantic.Field()
    """
    Location of stamp or geo.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
