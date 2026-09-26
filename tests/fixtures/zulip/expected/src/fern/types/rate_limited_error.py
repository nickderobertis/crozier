

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RateLimitedError(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    code: typing.Optional[typing.Any] = None
    retry_after: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="retry-after"),
        pydantic.Field(
            alias="retry-after", description="How many seconds the client must wait before making\nadditional requests."
        ),
    ] = None
    """
    How many seconds the client must wait before making
    additional requests.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
