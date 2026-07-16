

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .header import Header


class Response(UniversalBaseModel):
    """
    A mock invocation or test response
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Body content of this Response
    """

    headers: typing.Optional[typing.List[Header]] = pydantic.Field(default=None)
    """
    Headers for this Response
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of Response
    """

    name: str = pydantic.Field()
    """
    Unique distinct name of this Response
    """

    operation_id: typing_extensions.Annotated[str, FieldMetadata(alias="operationId")] = pydantic.Field()
    """
    Identifier of Operation this Response is associated to
    """

    test_case_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="testCaseId")] = pydantic.Field(
        default=None
    )
    """
    Unique identifier of TestCase this Response is attached (in case of a test)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
