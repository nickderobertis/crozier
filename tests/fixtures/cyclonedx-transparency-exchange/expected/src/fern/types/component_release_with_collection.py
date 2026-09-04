

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .collection import Collection
from .release import Release


class ComponentReleaseWithCollection(UniversalBaseModel):
    """
    A TEA Component Release combined with its latest collection
    """

    release: Release = pydantic.Field()
    """
    The TEA Component Release information
    """

    latest_collection: typing_extensions.Annotated[
        Collection,
        FieldMetadata(alias="latestCollection"),
        pydantic.Field(alias="latestCollection", description="The latest TEA Collection for this component release"),
    ]
    """
    The latest TEA Collection for this component release
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
