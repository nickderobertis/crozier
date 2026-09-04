

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TeaServerInfo(UniversalBaseModel):
    """
    TEA server information including URL, versions, and optional priority
    """

    root_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="rootUrl"),
        pydantic.Field(alias="rootUrl", description="Root URL of the TEA server for this TEI without trailing slash"),
    ]
    """
    Root URL of the TEA server for this TEI without trailing slash
    """

    versions: typing.List[str] = pydantic.Field()
    """
    Supported TEA API versions at this server without v prefix
    """

    priority: typing.Optional[float] = pydantic.Field(default=None)
    """
    Optional priority for this server (0.0 to 1.0, where 1.0 is highest priority)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
