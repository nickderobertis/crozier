

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .inventory_change import InventoryChange
from .inventory_count import InventoryCount


class BatchChangeInventoryResponse(UniversalBaseModel):
    """ """

    changes: typing.Optional[typing.List[InventoryChange]] = pydantic.Field(default=None)
    """
    Changes created for the request.
    """

    counts: typing.Optional[typing.List[InventoryCount]] = pydantic.Field(default=None)
    """
    The current counts for all objects referenced in the request.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
