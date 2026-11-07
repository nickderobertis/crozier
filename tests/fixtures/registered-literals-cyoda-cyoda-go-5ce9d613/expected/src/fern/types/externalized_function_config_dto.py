

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExternalizedFunctionConfigDto(UniversalBaseModel):
    attach_entity: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="attachEntity"),
        pydantic.Field(alias="attachEntity", description="Whether to attach entity data to the function call"),
    ] = None
    """
    Whether to attach entity data to the function call
    """

    calculation_nodes_tags: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="calculationNodesTags"),
        pydantic.Field(alias="calculationNodesTags", description="Comma-separated list of calculation node tags"),
    ] = None
    """
    Comma-separated list of calculation node tags
    """

    response_timeout_ms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="responseTimeoutMs"),
        pydantic.Field(alias="responseTimeoutMs", description="Response timeout in milliseconds"),
    ] = None
    """
    Response timeout in milliseconds
    """

    retry_policy: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="retryPolicy"),
        pydantic.Field(alias="retryPolicy", description="Retry policy for the function"),
    ] = None
    """
    Retry policy for the function
    """

    context: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional context for the function
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
