

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentNewsArticleRssItem(UniversalBaseModel):
    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = None
    html_content: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="HtmlContent")] = None
    image_path: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ImagePath")] = None
    link: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Link")] = None
    optional_mobile_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="OptionalMobileImagePath")
    ] = None
    pub_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="PubDate")] = None
    title: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Title")] = None
    unique_identifier: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="UniqueIdentifier")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
