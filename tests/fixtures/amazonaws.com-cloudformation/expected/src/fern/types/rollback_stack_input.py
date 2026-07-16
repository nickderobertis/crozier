

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RollbackStackInput(UniversalBaseModel):
    stack_name: typing_extensions.Annotated[str, FieldMetadata(alias="StackName")] = pydantic.Field()
    """
    The name that's associated with the stack.
    """

    role_arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="RoleARN")] = pydantic.Field(
        default=None
    )
    """
    The Amazon Resource Name (ARN) of an Identity and Access Management role that CloudFormation assumes to rollback the stack.
    """

    client_request_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ClientRequestToken")
    ] = pydantic.Field(default=None)
    """
    A unique identifier for this <code>RollbackStack</code> request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
