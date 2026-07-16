

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiException(UniversalBaseModel):
    """
    The object returned for a bad request
    """

    error_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="ErrorNumber"),
        pydantic.Field(alias="ErrorNumber", description="The error number"),
    ] = None
    """
    The error number
    """

    message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Message"),
        pydantic.Field(alias="Message", description="The message describing the error"),
    ] = None
    """
    The message describing the error
    """

    type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Type"), pydantic.Field(alias="Type", description="The type of error")
    ] = None
    """
    The type of error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
