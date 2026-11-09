

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReportRowContainer(UniversalBaseModel):
    key: typing.Optional[str] = None
    unit_id: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="unitId"), pydantic.Field(alias="unitId")
    ] = None
    sort_values: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="sortValues"),
        pydantic.Field(alias="sortValues"),
    ] = None
    columns_values: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="columnsValues"),
        pydantic.Field(alias="columnsValues"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
