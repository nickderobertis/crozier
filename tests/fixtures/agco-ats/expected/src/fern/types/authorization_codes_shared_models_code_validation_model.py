

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthorizationCodesSharedModelsCodeValidationModel(UniversalBaseModel):
    expiration_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="ExpirationDate"), pydantic.Field(alias="ExpirationDate")
    ] = None
    is_valid: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IsValid"), pydantic.Field(alias="IsValid")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
