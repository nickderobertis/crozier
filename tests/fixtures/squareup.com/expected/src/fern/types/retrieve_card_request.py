

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RetrieveCardRequest(UniversalBaseModel):
    """
    Retrieves details for a specific Card. Accessible via
    HTTP requests at GET https://connect.squareup.com/v2/cards/{card_id}
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
