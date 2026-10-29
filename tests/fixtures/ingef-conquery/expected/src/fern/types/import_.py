

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .import_inputs_item import ImportInputsItem
from .table_id import TableId


class Import(UniversalBaseModel):
    """
    Describes how one or multiple CSV files are to be transformed into a .cqpp file compatible with the designated table.
    """

    table: typing.Optional[TableId] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the import. When preprocessed with tags, will be overwritten to the respective tag.
    """

    label: typing.Optional[str] = None
    inputs: typing.Optional[typing.List[ImportInputsItem]] = pydantic.Field(default=None)
    """
    One or more descriptions to preprocess a `.csv` or `.csv.gz` into a single cqpp.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
