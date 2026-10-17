



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .update_storage_config_body_external import UpdateStorageConfigBodyExternal
    from .update_storage_config_body_external_upstream_target import UpdateStorageConfigBodyExternalUpstreamTarget
    from .update_storage_config_body_features import UpdateStorageConfigBodyFeatures
    from .update_storage_config_body_features_iceberg_catalog import UpdateStorageConfigBodyFeaturesIcebergCatalog
    from .update_storage_config_body_features_image_transformation import (
        UpdateStorageConfigBodyFeaturesImageTransformation,
    )
    from .update_storage_config_body_features_purge_cache import UpdateStorageConfigBodyFeaturesPurgeCache
    from .update_storage_config_body_features_s3protocol import UpdateStorageConfigBodyFeaturesS3Protocol
    from .update_storage_config_body_features_vector_buckets import UpdateStorageConfigBodyFeaturesVectorBuckets
_dynamic_imports: typing.Dict[str, str] = {
    "UpdateStorageConfigBodyExternal": ".update_storage_config_body_external",
    "UpdateStorageConfigBodyExternalUpstreamTarget": ".update_storage_config_body_external_upstream_target",
    "UpdateStorageConfigBodyFeatures": ".update_storage_config_body_features",
    "UpdateStorageConfigBodyFeaturesIcebergCatalog": ".update_storage_config_body_features_iceberg_catalog",
    "UpdateStorageConfigBodyFeaturesImageTransformation": ".update_storage_config_body_features_image_transformation",
    "UpdateStorageConfigBodyFeaturesPurgeCache": ".update_storage_config_body_features_purge_cache",
    "UpdateStorageConfigBodyFeaturesS3Protocol": ".update_storage_config_body_features_s3protocol",
    "UpdateStorageConfigBodyFeaturesVectorBuckets": ".update_storage_config_body_features_vector_buckets",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "UpdateStorageConfigBodyExternal",
    "UpdateStorageConfigBodyExternalUpstreamTarget",
    "UpdateStorageConfigBodyFeatures",
    "UpdateStorageConfigBodyFeaturesIcebergCatalog",
    "UpdateStorageConfigBodyFeaturesImageTransformation",
    "UpdateStorageConfigBodyFeaturesPurgeCache",
    "UpdateStorageConfigBodyFeaturesS3Protocol",
    "UpdateStorageConfigBodyFeaturesVectorBuckets",
]
