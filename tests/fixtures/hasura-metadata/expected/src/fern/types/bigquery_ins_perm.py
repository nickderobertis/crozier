

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bigquery_bool_exp import BigqueryBoolExp
from .bigquery_ins_perm_columns import BigqueryInsPermColumns
from .validate_input_input_webhook import ValidateInputInputWebhook


class BigqueryInsPerm(UniversalBaseModel):
    backend_only: typing.Optional[bool] = None
    check: BigqueryBoolExp
    columns: typing.Optional[BigqueryInsPermColumns] = None
    set_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="set"), pydantic.Field(alias="set")
    ] = None
    validate_input: typing.Optional[ValidateInputInputWebhook] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
