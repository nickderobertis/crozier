

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .api_reference import ApiReference
from .feature_prerequisites_item import FeaturePrerequisitesItem
from .resource_description import ResourceDescription


class Feature(ApiReference, ResourceDescription):
    """
    `Feature`
    """

    class_: typing_extensions.Annotated[
        typing.Optional[ApiReference], FieldMetadata(alias="class"), pydantic.Field(alias="class")
    ] = None
    feature_specific: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Information specific to this feature.
    """

    level: typing.Optional[float] = pydantic.Field(default=None)
    """
    The level this feature is gained.
    """

    parent: typing.Optional[ApiReference] = None
    prerequisites: typing.Optional[typing.List[FeaturePrerequisitesItem]] = pydantic.Field(default=None)
    """
    The prerequisites for this feature.
    """

    subclass: typing.Optional[ApiReference] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
