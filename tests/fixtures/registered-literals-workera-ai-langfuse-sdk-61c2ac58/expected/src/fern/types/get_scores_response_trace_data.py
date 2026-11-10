

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetScoresResponseTraceData(UniversalBaseModel):
    user_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="userId"),
        pydantic.Field(alias="userId", description="The user ID associated with the trace referenced by score"),
    ] = None
    """
    The user ID associated with the trace referenced by score
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of tags associated with the trace referenced by score
    """

    environment: typing.Optional[str] = pydantic.Field(default=None)
    """
    The environment of the trace referenced by score
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
