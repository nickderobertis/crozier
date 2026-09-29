

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class ToSchemaRelationshipDefLegacyFormat(UniversalBaseModel):
    hasura_fields: typing.List[str]
    remote_field: "RemoteFields"
    remote_schema: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .field_call import FieldCall
from .remote_fields import RemoteFields

update_forward_refs(ToSchemaRelationshipDefLegacyFormat, FieldCall=FieldCall, RemoteFields=RemoteFields)
