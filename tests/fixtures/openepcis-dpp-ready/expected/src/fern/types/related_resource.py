

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .data_element_base import DataElementBase


class RelatedResource(DataElementBase):
    """
    A related resource such as a document or image (EN 18223 clause 4.1.2.7).
    """

    resource_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceTitle"), pydantic.Field(alias="resourceTitle")
    ] = None
    content_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contentType"),
        pydantic.Field(alias="contentType", description="IANA media type of the resource."),
    ] = None
    """
    IANA media type of the resource.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource location (RFC 3986).
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 639 language code, optionally with ISO 3166-1 region.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
