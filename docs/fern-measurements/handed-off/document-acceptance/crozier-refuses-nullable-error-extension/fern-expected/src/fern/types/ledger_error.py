

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LedgerError(UniversalBaseModel):
    error_code: typing_extensions.Annotated[str, FieldMetadata(alias="errorCode"), pydantic.Field(alias="errorCode")]
    error_message: typing_extensions.Annotated[
        str, FieldMetadata(alias="errorMessage"), pydantic.Field(alias="errorMessage")
    ]
    retryable: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
