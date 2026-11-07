

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .node_usage_data import NodeUsageData


class ComponentUsagesInScenario(UniversalBaseModel):
    name: str
    nodes_usages_data: typing_extensions.Annotated[
        typing.Optional[typing.List[NodeUsageData]],
        FieldMetadata(alias="nodesUsagesData"),
        pydantic.Field(alias="nodesUsagesData"),
    ] = None
    is_fragment: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isFragment"), pydantic.Field(alias="isFragment")
    ]
    process_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="processCategory"), pydantic.Field(alias="processCategory")
    ]
    modification_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="modificationDate"), pydantic.Field(alias="modificationDate")
    ]
    modified_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="modifiedAt"), pydantic.Field(alias="modifiedAt")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
