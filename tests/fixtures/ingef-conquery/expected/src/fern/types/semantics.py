

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .concept_id import ConceptId
from .secondary_id_id import SecondaryIdId
from .select_id import SelectId


class Semantics_Categorical(UniversalBaseModel):
    """
    Used to add additional information to a queries resulting column, such as sources or restrictions of the values.
    """

    type: typing.Literal["CATEGORICAL"] = "CATEGORICAL"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Semantics_Column(UniversalBaseModel):
    """
    Used to add additional information to a queries resulting column, such as sources or restrictions of the values.
    """

    type: typing.Literal["COLUMN"] = "COLUMN"
    column: typing.Optional[ColumnId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Semantics_ConceptColumn(UniversalBaseModel):
    """
    Used to add additional information to a queries resulting column, such as sources or restrictions of the values.
    """

    type: typing.Literal["CONCEPT_COLUMN"] = "CONCEPT_COLUMN"
    concept: typing.Optional[ConceptId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Semantics_EventDate(UniversalBaseModel):
    """
    Used to add additional information to a queries resulting column, such as sources or restrictions of the values.
    """

    type: typing.Literal["EVENT_DATE"] = "EVENT_DATE"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Semantics_Group(UniversalBaseModel):
    """
    Used to add additional information to a queries resulting column, such as sources or restrictions of the values.
    """

    type: typing.Literal["GROUP"] = "GROUP"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Semantics_Hidden(UniversalBaseModel):
    """
    Used to add additional information to a queries resulting column, such as sources or restrictions of the values.
    """

    type: typing.Literal["HIDDEN"] = "HIDDEN"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Semantics_Id(UniversalBaseModel):
    """
    Used to add additional information to a queries resulting column, such as sources or restrictions of the values.
    """

    type: typing.Literal["ID"] = "ID"
    kind: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Semantics_SecondaryId(UniversalBaseModel):
    """
    Used to add additional information to a queries resulting column, such as sources or restrictions of the values.
    """

    type: typing.Literal["SECONDARY_ID"] = "SECONDARY_ID"
    secondary_id: typing_extensions.Annotated[
        typing.Optional[SecondaryIdId], FieldMetadata(alias="secondaryId"), pydantic.Field(alias="secondaryId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Semantics_Select(UniversalBaseModel):
    """
    Used to add additional information to a queries resulting column, such as sources or restrictions of the values.
    """

    type: typing.Literal["SELECT"] = "SELECT"
    select: typing.Optional[SelectId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Semantics_Sources(UniversalBaseModel):
    """
    Used to add additional information to a queries resulting column, such as sources or restrictions of the values.
    """

    type: typing.Literal["SOURCES"] = "SOURCES"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Semantics = typing_extensions.Annotated[
    typing.Union[
        Semantics_Categorical,
        Semantics_Column,
        Semantics_ConceptColumn,
        Semantics_EventDate,
        Semantics_Group,
        Semantics_Hidden,
        Semantics_Id,
        Semantics_SecondaryId,
        Semantics_Select,
        Semantics_Sources,
    ],
    pydantic.Field(discriminator="type"),
]
