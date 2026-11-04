

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .crtdl import Crtdl


class Dataquery(UniversalBaseModel):
    label: typing.Optional[str] = None
    comment: typing.Optional[str] = None
    total_number_of_results: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalNumberOfResults"), pydantic.Field(alias="totalNumberOfResults")
    ] = None
    content: Crtdl

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
