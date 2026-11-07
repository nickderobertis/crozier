

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .audit_fields import AuditFields
from .category_ref import CategoryRef
from .non_empty_id import NonEmptyId
from .slug import Slug
from .timestamps import Timestamps


class Category(Timestamps, AuditFields):
    id: NonEmptyId
    name: str
    parent: typing.Optional[CategoryRef] = None
    slug: Slug

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
