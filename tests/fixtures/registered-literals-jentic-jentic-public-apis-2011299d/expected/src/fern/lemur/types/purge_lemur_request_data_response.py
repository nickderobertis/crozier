

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PurgeLemurRequestDataResponse(UniversalBaseModel):
    request_id: str = pydantic.Field()
    """
    The ID of the deletion request of the LeMUR request
    """

    request_id_to_purge: str = pydantic.Field()
    """
    The ID of the LeMUR request to purge the data for
    """

    deleted: bool = pydantic.Field()
    """
    Whether the request data was deleted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
