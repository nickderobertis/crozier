

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .leaf_col_info_decision import LeafColInfoDecision
from .leaf_col_info_type import LeafColInfoType


class LeafColInfo(UniversalBaseModel):
    column_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="columnName"), pydantic.Field(alias="columnName")
    ] = None
    column_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="columnPath"), pydantic.Field(alias="columnPath")
    ] = None
    type: typing.Optional[LeafColInfoType] = None
    id: typing.Optional[typing.Dict[str, typing.Any]] = None
    decision: LeafColInfoDecision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
