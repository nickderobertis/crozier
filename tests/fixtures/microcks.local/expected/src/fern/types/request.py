

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .header import Header


class Request(UniversalBaseModel):
    """
    A mock invocation or test request
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Body content for this request
    """

    headers: typing.Optional[typing.List[Header]] = pydantic.Field(default=None)
    """
    Headers for this Request
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of Request
    """

    name: str = pydantic.Field()
    """
    Unique distinct name of this Request
    """

    operation_id: typing_extensions.Annotated[str, FieldMetadata(alias="operationId")] = pydantic.Field()
    """
    Identifier of Operation this Request is associated to
    """

    test_case_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="testCaseId")] = pydantic.Field(
        default=None
    )
    """
    Unique identifier of TestCase this Request is attached (in case of a test)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
