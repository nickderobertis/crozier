

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogMessageCatalogStreamsItem(UniversalBaseModel):
    """
    A named collection of records — analogous to a table or API resource.
    """

    name: str = pydantic.Field()
    """
    Collection name (e.g. "customers", "invoices", "pg_public.users").
    """

    primary_key: typing.List[typing.List[str]] = pydantic.Field()
    """
    Paths to fields that uniquely identify a record within this stream. Supports composite keys and nested paths. e.g. [["id"]] or [["account_id"], ["created"]]
    """

    json_schema: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    JSON Schema describing the record shape. Discovered at runtime or provided by config.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Source-specific metadata that applies to every record in this stream. The destination can use these for schema naming, partitioning, etc. Examples: Stripe: { api_version, account_id, live_mode }.
    """

    newer_than_field: str = pydantic.Field()
    """
    Field whose value increases monotonically. Destination uses it to skip stale writes (e.g. "updated").
    """

    soft_delete_field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Field in record data that signals a soft delete (e.g. "deleted"). Destination uses this to classify upserts as deletes when the field is truthy.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
