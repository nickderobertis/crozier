

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .highlight_info import HighlightInfo


class GetSuggestedLicense(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The primary key of the suggested license.
    """

    spdx_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="spdxName"),
        pydantic.Field(alias="spdxName", description="The SPDX identifier of the suggested license."),
    ] = None
    """
    The SPDX identifier of the suggested license.
    """

    shortname: typing.Optional[str] = pydantic.Field(default=None)
    """
    The short name of the suggested license.
    """

    fullname: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full name of the suggested license.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text content of the suggested license.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL associated with the suggested license.
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional notes or comments about the suggested license.
    """

    risk: typing.Optional[int] = pydantic.Field(default=None)
    """
    The risk level associated with the suggested license.
    """

    highlights: typing.Optional[typing.List[HighlightInfo]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
