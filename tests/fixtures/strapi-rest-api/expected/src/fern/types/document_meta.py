

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocumentMeta(UniversalBaseModel):
    """
    Strapi 5 system fields present on every document (flattened, not nested under data.attributes).
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Numeric id, retained for backwards compatibility; not used to address documents.
    """

    document_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="documentId"),
        pydantic.Field(alias="documentId", description="Stable document identifier used in URLs."),
    ] = None
    """
    Stable document identifier used in URLs.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    published_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="publishedAt"),
        pydantic.Field(alias="publishedAt", description="Publication timestamp; null when the version is a draft."),
    ] = None
    """
    Publication timestamp; null when the version is a draft.
    """

    locale: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
