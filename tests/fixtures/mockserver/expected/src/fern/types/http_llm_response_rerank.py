

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HttpLlmResponseRerank(UniversalBaseModel):
    top_n: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="topN"), pydantic.Field(alias="topN")
    ] = None
    deterministic_from_input: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="deterministicFromInput"),
        pydantic.Field(alias="deterministicFromInput"),
    ] = None
    seed: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
