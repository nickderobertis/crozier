

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .date import Date
from .entity_preview_config_all_item import EntityPreviewConfigAllItem
from .entity_preview_config_default_item import EntityPreviewConfigDefaultItem


class EntityPreviewConfig(UniversalBaseModel):
    """
    Frontend configuration for the entity-preview.
    """

    observation_period_min: typing_extensions.Annotated[
        typing.Optional[Date], FieldMetadata(alias="observationPeriodMin"), pydantic.Field(alias="observationPeriodMin")
    ] = None
    all_: typing_extensions.Annotated[
        typing.Optional[typing.List[EntityPreviewConfigAllItem]],
        FieldMetadata(alias="all"),
        pydantic.Field(
            alias="all",
            description="For frontend, list of sources to show the user. Usually a list of sources that have been tidied up.",
        ),
    ] = None
    """
    For frontend, list of sources to show the user. Usually a list of sources that have been tidied up.
    """

    default: typing.Optional[typing.List[EntityPreviewConfigDefaultItem]] = pydantic.Field(default=None)
    """
    For frontend, list of sources to select by default.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
