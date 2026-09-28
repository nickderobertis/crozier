

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HttpLlmResponseContentFilter(UniversalBaseModel):
    hate: typing.Optional[str] = None
    sexual: typing.Optional[str] = None
    violence: typing.Optional[str] = None
    self_harm: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="selfHarm"), pydantic.Field(alias="selfHarm")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
