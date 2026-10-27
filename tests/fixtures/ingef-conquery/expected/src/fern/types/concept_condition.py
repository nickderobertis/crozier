

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .column_id import ColumnId


class ConceptCondition_And(UniversalBaseModel):
    type: typing.Literal["AND"] = "AND"
    conditions: typing.Optional[typing.List["ConceptCondition"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConceptCondition_ColumnEqual(UniversalBaseModel):
    type: typing.Literal["COLUMN_EQUAL"] = "COLUMN_EQUAL"
    column: typing.Optional[ColumnId] = None
    values: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConceptCondition_Equal(UniversalBaseModel):
    type: typing.Literal["EQUAL"] = "EQUAL"
    values: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConceptCondition_Groovy(UniversalBaseModel):
    type: typing.Literal["GROOVY"] = "GROOVY"
    script: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConceptCondition_Not(UniversalBaseModel):
    type: typing.Literal["NOT"] = "NOT"
    condition: typing.Optional["ConceptCondition"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConceptCondition_Or(UniversalBaseModel):
    type: typing.Literal["OR"] = "OR"
    conditions: typing.Optional[typing.List["ConceptCondition"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConceptCondition_Prefix(UniversalBaseModel):
    type: typing.Literal["PREFIX"] = "PREFIX"
    prefixes: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConceptCondition_PrefixRange(UniversalBaseModel):
    type: typing.Literal["PREFIX_RANGE"] = "PREFIX_RANGE"
    min: typing.Optional[str] = None
    max: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConceptCondition_Present(UniversalBaseModel):
    type: typing.Literal["PRESENT"] = "PRESENT"
    column: typing.Optional[ColumnId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ConceptCondition = typing_extensions.Annotated[
    typing.Union[
        ConceptCondition_And,
        ConceptCondition_ColumnEqual,
        ConceptCondition_Equal,
        ConceptCondition_Groovy,
        ConceptCondition_Not,
        ConceptCondition_Or,
        ConceptCondition_Prefix,
        ConceptCondition_PrefixRange,
        ConceptCondition_Present,
    ],
    pydantic.Field(discriminator="type"),
]
from .not_condition import NotCondition
from .or_condition import OrCondition
from .and_condition import AndCondition

update_forward_refs(
    ConceptCondition_And, ConceptCondition=ConceptCondition, NotCondition=NotCondition, OrCondition=OrCondition
)
update_forward_refs(
    ConceptCondition_Not, AndCondition=AndCondition, ConceptCondition=ConceptCondition, OrCondition=OrCondition
)
update_forward_refs(
    ConceptCondition_Or, AndCondition=AndCondition, ConceptCondition=ConceptCondition, NotCondition=NotCondition
)
