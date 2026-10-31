

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateCollectionOptionsTimeseries(UniversalBaseModel):
    meta_field: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="metaField"), pydantic.Field(alias="metaField")
    ] = None
    time_field: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="timeField"), pydantic.Field(alias="timeField")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
