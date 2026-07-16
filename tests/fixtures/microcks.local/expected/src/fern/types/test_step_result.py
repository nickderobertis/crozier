

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TestStepResult(UniversalBaseModel):
    """
    TestStepResult is an entity embedded within TestCaseResult. They are created for each request associated with an operation / action of a microservice.
    """

    elapsed_time: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="elapsedTime")] = (
        pydantic.Field(default=None)
    )
    """
    Elapsed time in milliseconds since the test step beginning
    """

    event_message_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="eventMessageName")] = (
        pydantic.Field(default=None)
    )
    """
    Name of event this test step is bound to
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message that may be associated to this test step
    """

    request_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="requestName")] = (
        pydantic.Field(default=None)
    )
    """
    Name of request this test step is bound to
    """

    success: bool = pydantic.Field()
    """
    Flag telling if test case is a success
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
