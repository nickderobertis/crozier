

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mssql_bool_exp import MssqlBoolExp
from .mssql_upd_perm_columns import MssqlUpdPermColumns
from .validate_input_input_webhook import ValidateInputInputWebhook


class MssqlUpdPerm(UniversalBaseModel):
    backend_only: typing.Optional[bool] = None
    check: typing.Optional[MssqlBoolExp] = None
    columns: MssqlUpdPermColumns = pydantic.Field()
    """
    Allowed columns
    """

    filter: MssqlBoolExp
    set_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="set"),
        pydantic.Field(alias="set", description="Preset columns"),
    ] = None
    """
    Preset columns
    """

    validate_input: typing.Optional[ValidateInputInputWebhook] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
