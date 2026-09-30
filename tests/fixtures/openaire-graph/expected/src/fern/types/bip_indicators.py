

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BipIndicators(UniversalBaseModel):
    citation_count: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="citationCount"), pydantic.Field(alias="citationCount")
    ] = None
    influence: typing.Optional[float] = None
    popularity: typing.Optional[float] = None
    impulse: typing.Optional[float] = None
    citation_class: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="citationClass"), pydantic.Field(alias="citationClass")
    ] = None
    influence_class: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="influenceClass"), pydantic.Field(alias="influenceClass")
    ] = None
    impulse_class: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="impulseClass"), pydantic.Field(alias="impulseClass")
    ] = None
    popularity_class: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="popularityClass"), pydantic.Field(alias="popularityClass")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
