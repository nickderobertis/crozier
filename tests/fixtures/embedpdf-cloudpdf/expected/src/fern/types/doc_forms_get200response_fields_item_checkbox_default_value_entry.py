

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry_None(UniversalBaseModel):
    kind: typing.Literal["none"] = "none"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry_Scalar(UniversalBaseModel):
    kind: typing.Literal["scalar"] = "scalar"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry_Array(UniversalBaseModel):
    kind: typing.Literal["array"] = "array"
    values: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry_Unsupported(UniversalBaseModel):
    kind: typing.Literal["unsupported"] = "unsupported"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry_None,
        DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry_Scalar,
        DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry_Array,
        DocFormsGet200ResponseFieldsItemCheckboxDefaultValueEntry_Unsupported,
    ],
    pydantic.Field(discriminator="kind"),
]
