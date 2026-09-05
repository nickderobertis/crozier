

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .error_detail import ErrorDetail


class Error(UniversalBaseModel):
    category: str = pydantic.Field()
    """
    The error category
    """

    context: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic.Field(default=None)
    """
    Context about the error condition
    """

    correlation_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="correlationId"),
        pydantic.Field(
            alias="correlationId",
            description="A unique identifier for the request. Include this value with any error reports or support tickets",
        ),
    ]
    """
    A unique identifier for the request. Include this value with any error reports or support tickets
    """

    errors: typing.Optional[typing.List[ErrorDetail]] = pydantic.Field(default=None)
    """
    further information about the error
    """

    links: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    A map of link names to associated URIs containing documentation about the error or recommended remediation steps
    """

    message: str = pydantic.Field()
    """
    A human readable message describing the error along with remediation steps where appropriate
    """

    sub_category: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="subCategory"),
        pydantic.Field(
            alias="subCategory", description="A specific category that contains more specific detail about the error"
        ),
    ] = None
    """
    A specific category that contains more specific detail about the error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
