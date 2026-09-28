

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TableDisplayOptions(UniversalBaseModel):
    """
    Table display options that can be reused.
    """

    shown_columns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="shownColumns"),
        pydantic.Field(
            alias="shownColumns",
            description="Optional. This field is unused and has been replaced by TimeSeriesTable.column_settings",
        ),
    ] = None
    """
    Optional. This field is unused and has been replaced by TimeSeriesTable.column_settings
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
