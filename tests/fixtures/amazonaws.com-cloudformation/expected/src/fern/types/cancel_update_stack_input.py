

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CancelUpdateStackInput(UniversalBaseModel):
    """
    The input for the <a>CancelUpdateStack</a> action.
    """

    stack_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StackName"),
        pydantic.Field(
            alias="StackName", description="The name or the unique stack ID that's associated with the stack."
        ),
    ]
    """
    The name or the unique stack ID that's associated with the stack.
    """

    client_request_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientRequestToken"),
        pydantic.Field(
            alias="ClientRequestToken",
            description="A unique identifier for this <code>CancelUpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to cancel an update on a stack with the same name. You might retry <code>CancelUpdateStack</code> requests to ensure that CloudFormation successfully received them.",
        ),
    ] = None
    """
    A unique identifier for this <code>CancelUpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to cancel an update on a stack with the same name. You might retry <code>CancelUpdateStack</code> requests to ensure that CloudFormation successfully received them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
