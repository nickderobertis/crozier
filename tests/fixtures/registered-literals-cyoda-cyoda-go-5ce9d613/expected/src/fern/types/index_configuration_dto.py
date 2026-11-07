

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .index_configuration_dto_decision import IndexConfigurationDtoDecision
from .leaf_col_info import LeafColInfo


class IndexConfigurationDto(UniversalBaseModel):
    index_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="indexId"), pydantic.Field(alias="indexId")
    ] = None
    index_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="indexName"), pydantic.Field(alias="indexName")
    ] = None
    range_field: typing_extensions.Annotated[
        typing.Optional[LeafColInfo], FieldMetadata(alias="rangeField"), pydantic.Field(alias="rangeField")
    ] = None
    none_range_fields: typing_extensions.Annotated[
        typing.Optional[typing.List[LeafColInfo]],
        FieldMetadata(alias="noneRangeFields"),
        pydantic.Field(alias="noneRangeFields"),
    ] = None
    create_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createDate"), pydantic.Field(alias="createDate")
    ] = None
    ready_for_querying: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="readyForQuerying"), pydantic.Field(alias="readyForQuerying")
    ] = None
    returns_list: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="returnsList"), pydantic.Field(alias="returnsList")
    ] = None
    persisted: typing.Optional[bool] = None
    id: typing.Optional[typing.Dict[str, typing.Any]] = None
    decision: IndexConfigurationDtoDecision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
