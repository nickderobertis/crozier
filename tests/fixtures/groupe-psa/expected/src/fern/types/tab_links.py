

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class TabLinks(UniversalBaseModel):
    """
    [HAL](https://en.wikipedia.org/wiki/Hypertext_Application_Language#Convention) (Hypertext Application Language) link collection
    """

    self_: typing_extensions.Annotated[Link, FieldMetadata(alias="self"), pydantic.Field(alias="self")]
    first: Link
    next: typing.Optional[Link] = None
    prev: typing.Optional[Link] = None
    last: typing.Optional[Link] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
