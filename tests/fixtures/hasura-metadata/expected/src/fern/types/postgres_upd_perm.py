

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .postgres_bool_exp import PostgresBoolExp
from .postgres_upd_perm_columns import PostgresUpdPermColumns
from .validate_input_input_webhook import ValidateInputInputWebhook


class PostgresUpdPerm(UniversalBaseModel):
    backend_only: typing.Optional[bool] = None
    check: typing.Optional[PostgresBoolExp] = None
    columns: PostgresUpdPermColumns = pydantic.Field()
    """
    Allowed columns
    """

    filter: PostgresBoolExp
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
