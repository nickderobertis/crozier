

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conf_response_unified_columns_report_conf_section_id import ConfResponseUnifiedColumnsReportConfSectionId


class ConfResponseUnifiedColumns(UniversalBaseModel):
    """
    unified columns value
    """

    report_conf_section_id: typing_extensions.Annotated[
        typing.Optional[ConfResponseUnifiedColumnsReportConfSectionId],
        FieldMetadata(alias="report conf section id"),
        pydantic.Field(alias="report conf section id"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
