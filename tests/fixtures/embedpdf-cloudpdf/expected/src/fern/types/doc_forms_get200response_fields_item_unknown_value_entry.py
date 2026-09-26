

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DocFormsGet200ResponseFieldsItemUnknownValueEntry_None(UniversalBaseModel):
    kind: typing.Literal["none"] = "none"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemUnknownValueEntry_Scalar(UniversalBaseModel):
    kind: typing.Literal["scalar"] = "scalar"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemUnknownValueEntry_Array(UniversalBaseModel):
    kind: typing.Literal["array"] = "array"
    values: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocFormsGet200ResponseFieldsItemUnknownValueEntry_Unsupported(UniversalBaseModel):
    kind: typing.Literal["unsupported"] = "unsupported"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocFormsGet200ResponseFieldsItemUnknownValueEntry = typing_extensions.Annotated[
    typing.Union[
        DocFormsGet200ResponseFieldsItemUnknownValueEntry_None,
        DocFormsGet200ResponseFieldsItemUnknownValueEntry_Scalar,
        DocFormsGet200ResponseFieldsItemUnknownValueEntry_Array,
        DocFormsGet200ResponseFieldsItemUnknownValueEntry_Unsupported,
    ],
    pydantic.Field(discriminator="kind"),
]
