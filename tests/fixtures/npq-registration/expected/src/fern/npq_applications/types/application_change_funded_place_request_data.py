

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_change_funded_place_request_data_attributes import ApplicationChangeFundedPlaceRequestDataAttributes


class ApplicationChangeFundedPlaceRequestData(UniversalBaseModel):
    """
    A NPQ application change funded place request data
    """

    type: str = pydantic.Field()
    """
    The data typed
    """

    attributes: ApplicationChangeFundedPlaceRequestDataAttributes = pydantic.Field()
    """
    A NPQ application change funded place request attributes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
