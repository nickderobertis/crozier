

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sailboat_hull import SailboatHull


class Sailboat(UniversalBaseModel):
    """
    A vessel under sail.
    """

    hull: typing.Optional[SailboatHull] = None
    mast_count: typing_extensions.Annotated[int, FieldMetadata(alias="mastCount"), pydantic.Field(alias="mastCount")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
