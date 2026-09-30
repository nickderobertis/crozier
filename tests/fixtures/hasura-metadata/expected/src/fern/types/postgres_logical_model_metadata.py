

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .postgres_select_perm_def import PostgresSelectPermDef


class PostgresLogicalModelMetadata(UniversalBaseModel):
    """
    A return type.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description text which appears in the GraphQL Schema.
    """

    fields: typing.List[typing.Dict[str, typing.Any]] = pydantic.Field()
    """
    Return types for the logical model
    """

    name: str = pydantic.Field()
    """
    A name for a logical model
    """

    select_permissions: typing.Optional[typing.List[PostgresSelectPermDef]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
