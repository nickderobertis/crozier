

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .connector_id import ConnectorId
from .filter_id import FilterId
from .preview_config_info_card_selects_item import PreviewConfigInfoCardSelectsItem
from .preview_config_time_stratified_selects_item import PreviewConfigTimeStratifiedSelectsItem


class PreviewConfig(UniversalBaseModel):
    """
    Configuration to customize and integrate a Conquery instance.
    """

    observation_start: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="observationStart"),
        pydantic.Field(alias="observationStart", description="Default start date of entity-preview."),
    ] = None
    """
    Default start date of entity-preview.
    """

    info_card_selects: typing_extensions.Annotated[
        typing.Optional[typing.List[PreviewConfigInfoCardSelectsItem]],
        FieldMetadata(alias="infoCardSelects"),
        pydantic.Field(alias="infoCardSelects"),
    ] = None
    time_stratified_selects: typing_extensions.Annotated[
        typing.Optional[typing.List[PreviewConfigTimeStratifiedSelectsItem]],
        FieldMetadata(alias="timeStratifiedSelects"),
        pydantic.Field(alias="timeStratifiedSelects"),
    ] = None
    hidden: typing.Optional[typing.List[ColumnId]] = None
    grouping: typing.Optional[typing.List[ColumnId]] = None
    all_connectors: typing_extensions.Annotated[
        typing.Optional[typing.List[ConnectorId]],
        FieldMetadata(alias="allConnectors"),
        pydantic.Field(alias="allConnectors"),
    ] = None
    default_connectors: typing_extensions.Annotated[
        typing.Optional[typing.List[ConnectorId]],
        FieldMetadata(alias="defaultConnectors"),
        pydantic.Field(alias="defaultConnectors"),
    ] = None
    search_filters: typing_extensions.Annotated[
        typing.Optional[typing.List[FilterId]],
        FieldMetadata(alias="searchFilters"),
        pydantic.Field(alias="searchFilters"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
