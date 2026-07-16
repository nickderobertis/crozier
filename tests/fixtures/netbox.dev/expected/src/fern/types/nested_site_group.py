

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NestedSiteGroup(UniversalBaseModel):
    depth: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="_depth")] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: str
    site_count: typing.Optional[int] = None
    slug: str
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
