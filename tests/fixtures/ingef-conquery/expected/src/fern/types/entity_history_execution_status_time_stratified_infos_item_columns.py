

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_type import ColumnType
from .semantics import Semantics


class EntityHistoryExecutionStatusTimeStratifiedInfosItemColumns(UniversalBaseModel):
    """
    Description of the columns of totals, years and quarters.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    label of the column in csv.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    If available any description of the data of the query. For example SecondaryId or an exported Column.
    """

    default_label: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="defaultLabel"), pydantic.Field(alias="defaultLabel")
    ] = None
    type: typing.Optional[ColumnType] = None
    semantics: typing_extensions.Annotated[
        typing.Optional[typing.List[Semantics]],
        FieldMetadata(alias="Semantics"),
        pydantic.Field(alias="Semantics", description="Additional information and tags of the query."),
    ] = None
    """
    Additional information and tags of the query.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
