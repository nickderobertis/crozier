

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .operator_dbt import OperatorDbt
from .operator_normalization import OperatorNormalization
from .operator_type import OperatorType
from .operator_webhook import OperatorWebhook


class OperatorConfiguration(UniversalBaseModel):
    dbt: typing.Optional[OperatorDbt] = None
    normalization: typing.Optional[OperatorNormalization] = None
    operator_type: typing_extensions.Annotated[OperatorType, FieldMetadata(alias="operatorType")]
    webhook: typing.Optional[OperatorWebhook] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
