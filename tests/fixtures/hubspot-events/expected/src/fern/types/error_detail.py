

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ErrorDetail(UniversalBaseModel):
    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status code associated with the error detail
    """

    context: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic.Field(default=None)
    """
    Context about the error condition
    """

    in_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="in"),
        pydantic.Field(alias="in", description="The name of the field or parameter in which the error was found."),
    ] = None
    """
    The name of the field or parameter in which the error was found.
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
