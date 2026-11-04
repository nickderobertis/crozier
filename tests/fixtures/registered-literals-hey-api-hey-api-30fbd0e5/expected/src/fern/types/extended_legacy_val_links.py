

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExtendedLegacyValLinks(UniversalBaseModel):
    self_: typing_extensions.Annotated[
        str, FieldMetadata(alias="self"), pydantic.Field(alias="self", description="The URL of this val on this API")
    ]
    """
    The URL of this val on this API
    """

    versions: str = pydantic.Field()
    """
    The endpoint to retrieve this val's versions
    """

    module: str = pydantic.Field()
    """
    The URL of this Val's source code as a module
    """

    endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    This val's web endpoint, where it serves a website or API
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
