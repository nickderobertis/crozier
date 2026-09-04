

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_consent_details_response_errors_item import GetConsentDetailsResponseErrorsItem
from .get_consent_details_response_response import GetConsentDetailsResponseResponse


class GetConsentDetailsResponse(UniversalBaseModel):
    response_time: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="responseTime"), pydantic.Field(alias="responseTime")
    ]
    response: typing.Optional[GetConsentDetailsResponseResponse] = None
    errors: typing.Optional[typing.List[GetConsentDetailsResponseErrorsItem]] = pydantic.Field(default=None)
    """
    List of Errors in case of request validation / processing failure in eSignet server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
