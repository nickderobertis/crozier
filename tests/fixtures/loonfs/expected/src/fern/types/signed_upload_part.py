

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .object_transfer_access import ObjectTransferAccess


class SignedUploadPart(UniversalBaseModel):
    """
    One authorized part upload.
    """

    access: ObjectTransferAccess = pydantic.Field()
    """
    A short-lived write capability for this part.
    """

    part_number: int = pydantic.Field()
    """
    The part number that this capability writes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
