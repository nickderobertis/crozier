

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class RemoteCallbackLinks(UniversalBaseModel):
    """
    *Note*: ```remotes``` is a templated link.
    """

    self_: typing_extensions.Annotated[Link, FieldMetadata(alias="self"), pydantic.Field(alias="self")]
    fleet: typing.Optional[Link] = None
    remotes: typing.Optional[Link] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
