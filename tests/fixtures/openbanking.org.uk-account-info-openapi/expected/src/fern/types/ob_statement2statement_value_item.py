

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_external_statement_value_type1code import ObExternalStatementValueType1Code
from .value import Value


class ObStatement2StatementValueItem(UniversalBaseModel):
    """
    Set of elements used to provide details of a generic number value related to the statement resource.
    """

    type: typing_extensions.Annotated[ObExternalStatementValueType1Code, FieldMetadata(alias="Type")]
    value: typing_extensions.Annotated[Value, FieldMetadata(alias="Value")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
