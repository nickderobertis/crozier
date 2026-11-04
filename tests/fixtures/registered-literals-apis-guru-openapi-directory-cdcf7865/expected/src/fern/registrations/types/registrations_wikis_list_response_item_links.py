

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class RegistrationsWikisListResponseItemLinks(UniversalBaseModel):
    """
    URLs to alternative representations of the wiki.
    """

    download: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to download the content of the wiki.
    """

    info: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the detail page for the wiki.
    """

    self_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="A link to the detail page for the wiki."),
    ] = None
    """
    A link to the detail page for the wiki.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
