

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delete_image_response_status import DeleteImageResponseStatus


class DeleteImageResponse(UniversalBaseModel):
    """
    Image deletion response containing status and details
    """

    detail: typing.Optional[str] = None
    digest: str
    status: DeleteImageResponseStatus = pydantic.Field()
    """
    Current status of the image deletion
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
