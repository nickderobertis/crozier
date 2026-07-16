

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .header import Header


class EventMessage(UniversalBaseModel):
    """ """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Body content for this message
    """

    headers: typing.Optional[typing.List[Header]] = pydantic.Field(default=None)
    """
    Headers for this message
    """

    id: str = pydantic.Field()
    """
    Unique identifier of this message
    """

    media_type: typing_extensions.Annotated[str, FieldMetadata(alias="mediaType")] = pydantic.Field()
    """
    Content type of message
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique distinct name of this message
    """

    operation_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="operationId")] = (
        pydantic.Field(default=None)
    )
    """
    Identifier of Operation this message is associated to
    """

    test_case_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="testCaseId")] = pydantic.Field(
        default=None
    )
    """
    Unique identifier of TestCase this message is attached (in case of a test)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
