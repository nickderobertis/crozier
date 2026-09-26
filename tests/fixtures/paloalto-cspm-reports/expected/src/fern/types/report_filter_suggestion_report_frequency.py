

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .name_value_integer_string import NameValueIntegerString


class ReportFilterSuggestionReportFrequency(UniversalBaseModel):
    """
    Model for FilterSuggestion
    """

    name_value: typing_extensions.Annotated[
        typing.Optional[typing.List[NameValueIntegerString]],
        FieldMetadata(alias="nameValue"),
        pydantic.Field(alias="nameValue", description="Filter options"),
    ] = None
    """
    Filter options
    """

    options: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Filter options, which lists all the default options for static filters or all the recent options, if any, for non-static filters
    """

    static_filter: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="staticFilter"),
        pydantic.Field(alias="staticFilter", description="Filter is a static filter"),
    ] = None
    """
    Filter is a static filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
