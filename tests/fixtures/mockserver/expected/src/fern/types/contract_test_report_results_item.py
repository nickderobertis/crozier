

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContractTestReportResultsItem(UniversalBaseModel):
    operation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="operationId"), pydantic.Field(alias="operationId")
    ] = None
    method: typing.Optional[str] = None
    path: typing.Optional[str] = None
    status_code_received: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="statusCodeReceived"), pydantic.Field(alias="statusCodeReceived")
    ] = None
    passed: typing.Optional[bool] = None
    validation_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="validationErrors"),
        pydantic.Field(alias="validationErrors"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
