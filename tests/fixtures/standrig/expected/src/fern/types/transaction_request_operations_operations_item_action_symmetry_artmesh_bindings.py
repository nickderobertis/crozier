

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item import (
    TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItem,
)


class TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindings(UniversalBaseModel):
    links: typing.List[TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItem]
    overwrite: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
