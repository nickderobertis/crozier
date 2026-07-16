

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metadata import Metadata
from .secret_ref import SecretRef
from .service_ref import ServiceRef


class ImportJob(UniversalBaseModel):
    """
    An ImportJob allow defining a repository artifact to poll for discovering Services and APIs mocks and tests
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this ImportJob is active (ie. scheduled for execution)
    """

    created_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdDate"),
        pydantic.Field(alias="createdDate", description="Creation date for this ImportJob"),
    ] = None
    """
    Creation date for this ImportJob
    """

    etag: typing.Optional[str] = pydantic.Field(default=None)
    """
    Etag of repository URL during previous import. Is used for not re-importing if no recent changes
    """

    frequency: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved for future usage
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of ImportJob
    """

    last_import_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastImportDate"),
        pydantic.Field(alias="lastImportDate", description="Date last import was done"),
    ] = None
    """
    Date last import was done
    """

    last_import_error: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastImportError"),
        pydantic.Field(alias="lastImportError", description="Error message of last import (if any)"),
    ] = None
    """
    Error message of last import (if any)
    """

    main_artifact: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="mainArtifact"),
        pydantic.Field(
            alias="mainArtifact",
            description="Flag telling if considered as primary or secondary artifact. Default to `true`",
        ),
    ] = None
    """
    Flag telling if considered as primary or secondary artifact. Default to `true`
    """

    metadata: typing.Optional[Metadata] = pydantic.Field(default=None)
    """
    Metadata of ImportJob
    """

    name: str = pydantic.Field()
    """
    Unique distinct name of this ImportJob
    """

    repository_disable_ssl_validation: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="repositoryDisableSSLValidation"),
        pydantic.Field(
            alias="repositoryDisableSSLValidation",
            description="Whether to disable SSL certificate verification when checking repository",
        ),
    ] = None
    """
    Whether to disable SSL certificate verification when checking repository
    """

    repository_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="repositoryUrl"),
        pydantic.Field(alias="repositoryUrl", description="URL of mocks and tests repository artifact"),
    ]
    """
    URL of mocks and tests repository artifact
    """

    secret_ref: typing_extensions.Annotated[
        typing.Optional[SecretRef],
        FieldMetadata(alias="secretRef"),
        pydantic.Field(alias="secretRef", description="Reference of a Secret to used when checking repository"),
    ] = None
    """
    Reference of a Secret to used when checking repository
    """

    service_refs: typing_extensions.Annotated[
        typing.Optional[typing.List[ServiceRef]],
        FieldMetadata(alias="serviceRefs"),
        pydantic.Field(alias="serviceRefs", description="References of Services discovered when checking repository"),
    ] = None
    """
    References of Services discovered when checking repository
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
