

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link_type import LinkType


class AppPkgInfoLinks(UniversalBaseModel):
    """
    Links to resources related to this resource.
    """

    app_d: typing_extensions.Annotated[LinkType, FieldMetadata(alias="appD"), pydantic.Field(alias="appD")]
    app_pkg_content: typing_extensions.Annotated[
        LinkType, FieldMetadata(alias="appPkgContent"), pydantic.Field(alias="appPkgContent")
    ]
    self_: typing_extensions.Annotated[LinkType, FieldMetadata(alias="self"), pydantic.Field(alias="self")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
