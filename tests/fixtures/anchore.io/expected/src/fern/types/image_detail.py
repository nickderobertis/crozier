

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ImageDetail(UniversalBaseModel):
    """
    A metadata detail record for a specific image. Multiple detail records may map a single catalog image.
    """

    created_at: typing.Optional[dt.datetime] = None
    dockerfile: typing.Optional[str] = None
    fulldigest: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full docker-pullable digest string including the registry url and repository necessary get the image
    """

    fulltag: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full docker-pullable tag string referencing the image
    """

    image_digest: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="imageDigest")] = (
        pydantic.Field(default=None)
    )
    """
    The parent Anchore Image record to which this detail maps
    """

    image_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="imageId")] = None
    last_updated: typing.Optional[dt.datetime] = None
    registry: typing.Optional[str] = None
    repo: typing.Optional[str] = None
    user_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="userId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
