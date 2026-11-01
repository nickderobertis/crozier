

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class InferredReturnsNestedNullableResponseResultDataOuter(UniversalBaseModel):
    inner: typing.Optional[str] = None
    maybe_num: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maybeNum"), pydantic.Field(alias="maybeNum")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
