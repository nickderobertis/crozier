

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MarimoMatrixData(UniversalBaseModel):
    initial_value: typing_extensions.Annotated[
        typing.List[typing.List[float]], FieldMetadata(alias="initialValue"), pydantic.Field(alias="initialValue")
    ]
    label: typing.Optional[str] = None
    min_value: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[float]]],
        FieldMetadata(alias="minValue"),
        pydantic.Field(alias="minValue"),
    ] = None
    max_value: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[float]]],
        FieldMetadata(alias="maxValue"),
        pydantic.Field(alias="maxValue"),
    ] = None
    step: typing.List[typing.List[float]]
    precision: float
    row_labels: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="rowLabels"), pydantic.Field(alias="rowLabels")
    ] = None
    column_labels: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="columnLabels"), pydantic.Field(alias="columnLabels")
    ] = None
    symmetric: bool
    debounce: typing.Optional[bool] = None
    scientific: bool
    disabled: typing.List[typing.List[bool]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
