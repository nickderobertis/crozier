

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_error1 import ObError1


class ObErrorResponse1(UniversalBaseModel):
    """
    An array of detail error codes, and messages, and URLs to documentation to help remediation.
    """

    code: typing_extensions.Annotated[str, FieldMetadata(alias="Code")] = pydantic.Field()
    """
    High level textual error code, to help categorize the errors.
    """

    errors: typing_extensions.Annotated[typing.List[ObError1], FieldMetadata(alias="Errors")]
    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Id")] = pydantic.Field(default=None)
    """
    A unique reference for the error instance, for audit purposes, in case of unknown/unclassified errors.
    """

    message: typing_extensions.Annotated[str, FieldMetadata(alias="Message")] = pydantic.Field()
    """
    Brief Error message, e.g., 'There is something wrong with the request parameters provided'
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
