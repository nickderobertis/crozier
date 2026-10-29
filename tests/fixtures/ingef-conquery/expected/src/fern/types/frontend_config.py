

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency_config import CurrencyConfig
from .mail import Mail
from .upload_config import UploadConfig
from .version_container import VersionContainer


class FrontendConfig(UniversalBaseModel):
    versions: typing.Optional[typing.List[VersionContainer]] = pydantic.Field(default=None)
    """
    Revisions of backend components such as the backend and form-backends
    """

    manual_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="manualUrl"),
        pydantic.Field(alias="manualUrl", description="URL to this instances manual if available."),
    ] = None
    """
    URL to this instances manual if available.
    """

    contact_email: typing_extensions.Annotated[
        typing.Optional[Mail], FieldMetadata(alias="contactEmail"), pydantic.Field(alias="contactEmail")
    ] = None
    currency: typing.Optional[CurrencyConfig] = None
    upload: typing.Optional[UploadConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
