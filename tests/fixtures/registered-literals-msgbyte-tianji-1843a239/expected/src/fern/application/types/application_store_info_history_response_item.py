

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ApplicationStoreInfoHistoryResponseItem(UniversalBaseModel):
    downloads: typing.Optional[int] = None
    score: typing.Optional[float] = None
    rating_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ratingCount"), pydantic.Field(alias="ratingCount")
    ] = None
    reviews: typing.Optional[int] = None
    size: typing.Optional[float] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
