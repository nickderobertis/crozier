

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ApplicationInfoResponseApplicationStoreInfosItem(UniversalBaseModel):
    application_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="applicationId"), pydantic.Field(alias="applicationId")
    ]
    store_type: typing_extensions.Annotated[str, FieldMetadata(alias="storeType"), pydantic.Field(alias="storeType")]
    store_id: typing_extensions.Annotated[str, FieldMetadata(alias="storeId"), pydantic.Field(alias="storeId")]
    app_id: typing_extensions.Annotated[str, FieldMetadata(alias="appId"), pydantic.Field(alias="appId")]
    title: str
    description: str
    release_notes: typing_extensions.Annotated[
        str, FieldMetadata(alias="releaseNotes"), pydantic.Field(alias="releaseNotes")
    ]
    url: str
    downloads: typing.Optional[int] = None
    score: typing.Optional[float] = None
    rating_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ratingCount"), pydantic.Field(alias="ratingCount")
    ] = None
    reviews: typing.Optional[int] = None
    version: typing.Optional[str] = None
    size: typing.Optional[float] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
