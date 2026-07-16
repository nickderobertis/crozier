

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .date_time import DateTime
from .ob_external_statement_date_time_type1code import ObExternalStatementDateTimeType1Code


class ObStatement2StatementDateTimeItem(UniversalBaseModel):
    """
    Set of elements used to provide details of a generic date time for the statement resource.
    """

    date_time: typing_extensions.Annotated[DateTime, FieldMetadata(alias="DateTime")]
    type: typing_extensions.Annotated[ObExternalStatementDateTimeType1Code, FieldMetadata(alias="Type")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
