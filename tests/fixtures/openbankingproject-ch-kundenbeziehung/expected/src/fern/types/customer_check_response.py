

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .customer_check_response_level_of_assurance import CustomerCheckResponseLevelOfAssurance


class CustomerCheckResponse(UniversalBaseModel):
    match: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Ob ein Kunde gefunden wurde
    """

    identification_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="identificationDate"),
        pydantic.Field(alias="identificationDate", description="Datum der letzten Identifikation"),
    ] = None
    """
    Datum der letzten Identifikation
    """

    level_of_assurance: typing_extensions.Annotated[
        typing.Optional[CustomerCheckResponseLevelOfAssurance],
        FieldMetadata(alias="levelOfAssurance"),
        pydantic.Field(alias="levelOfAssurance", description="Sicherheitsniveau der Identifikation"),
    ] = None
    """
    Sicherheitsniveau der Identifikation
    """

    valid_until: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="validUntil"),
        pydantic.Field(alias="validUntil", description="Gültigkeit der Identifikation"),
    ] = None
    """
    Gültigkeit der Identifikation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
