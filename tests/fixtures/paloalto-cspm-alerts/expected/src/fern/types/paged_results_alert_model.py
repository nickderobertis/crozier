

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alert_model import AlertModel


class PagedResultsAlertModel(UniversalBaseModel):
    dynamic_columns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="dynamicColumns"), pydantic.Field(alias="dynamicColumns")
    ] = None
    info_msg: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="infoMsg"), pydantic.Field(alias="infoMsg")
    ] = None
    items: typing.Optional[typing.List[AlertModel]] = None
    next_page_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextPageToken"), pydantic.Field(alias="nextPageToken")
    ] = None
    sort_allowed_columns: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="sortAllowedColumns"),
        pydantic.Field(alias="sortAllowedColumns"),
    ] = None
    total_rows: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalRows"), pydantic.Field(alias="totalRows")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
