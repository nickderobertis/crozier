

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project_get_checkout_key_by_fingerprint_response_type import ProjectGetCheckoutKeyByFingerprintResponseType


class ProjectGetCheckoutKeyByFingerprintResponse(UniversalBaseModel):
    """
    A checkout key
    """

    public_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="public-key"), pydantic.Field(alias="public-key", description="A public SSH key.")
    ]
    """
    A public SSH key.
    """

    type: ProjectGetCheckoutKeyByFingerprintResponseType = pydantic.Field()
    """
    The type of checkout key. This may be either `deploy-key` or `github-user-key`.
    """

    fingerprint: str = pydantic.Field()
    """
    An SSH key fingerprint.
    """

    preferred: bool = pydantic.Field()
    """
    A boolean value that indicates if this key is preferred.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="created-at"),
        pydantic.Field(alias="created-at", description="The date and time the checkout key was created."),
    ]
    """
    The date and time the checkout key was created.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
