

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .visibility import Visibility


class Document(UniversalBaseModel):
    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    File Name
    """

    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType", description="Mime Type")
    ] = None
    """
    Mime Type
    """

    owner_organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerOrganizationId"),
        pydantic.Field(alias="ownerOrganizationId", description="The organization's namespace which owns the document"),
    ] = None
    """
    The organization's namespace which owns the document
    """

    visibility: typing.Optional[Visibility] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
