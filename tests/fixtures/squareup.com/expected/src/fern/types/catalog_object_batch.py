

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class CatalogObjectBatch(UniversalBaseModel):
    """
    A batch of catalog objects.
    """

    objects: typing.List["CatalogObject"] = pydantic.Field()
    """
    A list of CatalogObjects belonging to this batch.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_object import CatalogObject

update_forward_refs(CatalogObjectBatch)
