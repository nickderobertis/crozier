

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .catalog_id_mapping import CatalogIdMapping
from .error import Error


class UpsertCatalogObjectResponse(UniversalBaseModel):
    """ """

    catalog_object: typing.Optional["CatalogObject"] = None
    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    id_mappings: typing.Optional[typing.List[CatalogIdMapping]] = pydantic.Field(default=None)
    """
    The mapping between client and server IDs for this upsert.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_object import CatalogObject

update_forward_refs(UpsertCatalogObjectResponse)
