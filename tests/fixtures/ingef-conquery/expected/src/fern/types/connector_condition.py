

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .column_id import ColumnId


class ConnectorCondition_And(UniversalBaseModel):
    """
    Allows filtering of events for the tree. Useful to separate out events from a larger table for a very niche concept.
    """

    type: typing.Literal["AND"] = "AND"
    conditions: typing.Optional[typing.List["ConceptCondition"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConnectorCondition_ColumnEqual(UniversalBaseModel):
    """
    Allows filtering of events for the tree. Useful to separate out events from a larger table for a very niche concept.
    """

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


class ConnectorCondition_Equal(UniversalBaseModel):
    """
    Allows filtering of events for the tree. Useful to separate out events from a larger table for a very niche concept.
    """

    type: typing.Literal["EQUAL"] = "EQUAL"
    values: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConnectorCondition_Groovy(UniversalBaseModel):
    """
    Allows filtering of events for the tree. Useful to separate out events from a larger table for a very niche concept.
    """

    type: typing.Literal["GROOVY"] = "GROOVY"
    script: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConnectorCondition_Not(UniversalBaseModel):
    """
    Allows filtering of events for the tree. Useful to separate out events from a larger table for a very niche concept.
    """

    type: typing.Literal["NOT"] = "NOT"
    condition: typing.Optional["ConceptCondition"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConnectorCondition_Or(UniversalBaseModel):
    """
    Allows filtering of events for the tree. Useful to separate out events from a larger table for a very niche concept.
    """

    type: typing.Literal["OR"] = "OR"
    conditions: typing.Optional[typing.List["ConceptCondition"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConnectorCondition_Prefix(UniversalBaseModel):
    """
    Allows filtering of events for the tree. Useful to separate out events from a larger table for a very niche concept.
    """

    type: typing.Literal["PREFIX"] = "PREFIX"
    prefixes: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConnectorCondition_PrefixRange(UniversalBaseModel):
    """
    Allows filtering of events for the tree. Useful to separate out events from a larger table for a very niche concept.
    """

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


class ConnectorCondition_Present(UniversalBaseModel):
    """
    Allows filtering of events for the tree. Useful to separate out events from a larger table for a very niche concept.
    """

    type: typing.Literal["PRESENT"] = "PRESENT"
    column: typing.Optional[ColumnId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ConnectorCondition = typing_extensions.Annotated[
    typing.Union[
        ConnectorCondition_And,
        ConnectorCondition_ColumnEqual,
        ConnectorCondition_Equal,
        ConnectorCondition_Groovy,
        ConnectorCondition_Not,
        ConnectorCondition_Or,
        ConnectorCondition_Prefix,
        ConnectorCondition_PrefixRange,
        ConnectorCondition_Present,
    ],
    pydantic.Field(discriminator="type"),
]
from .concept_condition import ConceptCondition
from .not_condition import NotCondition
from .or_condition import OrCondition
from .and_condition import AndCondition

update_forward_refs(
    ConnectorCondition_And, ConceptCondition=ConceptCondition, NotCondition=NotCondition, OrCondition=OrCondition
)
update_forward_refs(
    ConnectorCondition_Not, AndCondition=AndCondition, ConceptCondition=ConceptCondition, OrCondition=OrCondition
)
update_forward_refs(
    ConnectorCondition_Or, AndCondition=AndCondition, ConceptCondition=ConceptCondition, NotCondition=NotCondition
)
