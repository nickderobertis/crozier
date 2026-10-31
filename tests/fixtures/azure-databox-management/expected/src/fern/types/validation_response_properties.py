

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .validation_input_response import ValidationInputResponse
from .validation_response_properties_status import ValidationResponsePropertiesStatus


class ValidationResponseProperties(UniversalBaseModel):
    """
    Properties of pre job creation validation response.
    """

    individual_response_details: typing_extensions.Annotated[
        typing.Optional[typing.List[ValidationInputResponse]],
        FieldMetadata(alias="individualResponseDetails"),
        pydantic.Field(
            alias="individualResponseDetails",
            description="List of response details contain validationType and its response as key and value respectively.",
        ),
    ] = None
    """
    List of response details contain validationType and its response as key and value respectively.
    """

    status: typing.Optional[ValidationResponsePropertiesStatus] = pydantic.Field(default=None)
    """
    Overall validation status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
