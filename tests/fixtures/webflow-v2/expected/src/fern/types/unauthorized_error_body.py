

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .unauthorized_error_body_code import UnauthorizedErrorBodyCode


class UnauthorizedErrorBody(UniversalBaseModel):
    code: typing.Optional[UnauthorizedErrorBodyCode] = pydantic.Field(default=None)
    """
    Error code
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message
    """

    external_reference: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="externalReference"),
        pydantic.Field(alias="externalReference", description="Link to more information"),
    ] = None
    """
    Link to more information
    """

    details: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Array of errors
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
