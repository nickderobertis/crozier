

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Error(UniversalBaseModel):
    error_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="errorId"),
        pydantic.Field(alias="errorId", description="Machine-readable error identifier"),
    ]
    """
    Machine-readable error identifier
    """

    error_message: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="errorMessage"),
        pydantic.Field(alias="errorMessage", description="Human-readable error message"),
    ]
    """
    Human-readable error message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
