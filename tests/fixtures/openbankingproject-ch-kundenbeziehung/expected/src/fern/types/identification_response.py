

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identification_response_level_of_assurance import IdentificationResponseLevelOfAssurance
from .identification_response_status import IdentificationResponseStatus


class IdentificationResponse(UniversalBaseModel):
    verification_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="verificationId"), pydantic.Field(alias="verificationId")
    ] = None
    status: typing.Optional[IdentificationResponseStatus] = None
    level_of_assurance: typing_extensions.Annotated[
        typing.Optional[IdentificationResponseLevelOfAssurance],
        FieldMetadata(alias="levelOfAssurance"),
        pydantic.Field(alias="levelOfAssurance"),
    ] = None
    verification_method: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="verificationMethod"), pydantic.Field(alias="verificationMethod")
    ] = None
    timestamp: typing.Optional[dt.datetime] = None
    errors: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
