

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EnhancedCashFlowTransactions(UniversalBaseModel):
    """ """

    data_sources: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="dataSources"),
        pydantic.Field(alias="dataSources"),
    ] = None
    report_info: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="reportInfo"), pydantic.Field(alias="reportInfo")
    ] = None
    report_items: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="reportItems"),
        pydantic.Field(alias="reportItems"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
