

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_external_statement_rate_type1code import ObExternalStatementRateType1Code
from .rate import Rate


class ObStatement2BasicStatementRateItem(UniversalBaseModel):
    """
    Set of elements used to provide details of a generic rate related to the statement resource.
    """

    rate: typing_extensions.Annotated[Rate, FieldMetadata(alias="Rate"), pydantic.Field(alias="Rate")]
    type: typing_extensions.Annotated[
        ObExternalStatementRateType1Code, FieldMetadata(alias="Type"), pydantic.Field(alias="Type")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
