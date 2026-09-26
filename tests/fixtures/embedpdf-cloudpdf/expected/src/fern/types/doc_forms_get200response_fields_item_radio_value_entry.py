

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DocFormsGet200ResponseFieldsItemRadioValueEntry_None(UniversalBaseModel):
    kind: typing.Literal["none"] = "none"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemRadioValueEntry_Scalar(UniversalBaseModel):
    kind: typing.Literal["scalar"] = "scalar"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemRadioValueEntry_Array(UniversalBaseModel):
    kind: typing.Literal["array"] = "array"
    values: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemRadioValueEntry_Unsupported(UniversalBaseModel):
    kind: typing.Literal["unsupported"] = "unsupported"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemRadioValueEntry = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemRadioValueEntry_None,
        DocFormsGet200ResponseFieldsItemRadioValueEntry_Scalar,
        DocFormsGet200ResponseFieldsItemRadioValueEntry_Array,
        DocFormsGet200ResponseFieldsItemRadioValueEntry_Unsupported,
    ],
    pydantic.Field(discriminator="kind"),
]
