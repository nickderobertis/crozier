



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateProviderBodyAttributeMapping,
        CreateProviderBodyAttributeMappingKeysValue,
        CreateProviderBodyAttributeMappingKeysValueDefault,
        CreateProviderBodyAttributeMappingKeysValueDefaultZero,
        CreateProviderBodyNameIdFormat,
        CreateProviderBodyType,
        CreateSigningKeyBodyAlgorithm,
        CreateSigningKeyBodyPrivateJwk,
        CreateSigningKeyBodyPrivateJwkEc,
        CreateSigningKeyBodyPrivateJwkEcAlg,
        CreateSigningKeyBodyPrivateJwkEcCrv,
        CreateSigningKeyBodyPrivateJwkEcKeyOpsItem,
        CreateSigningKeyBodyPrivateJwkEcUse,
        CreateSigningKeyBodyPrivateJwkOct,
        CreateSigningKeyBodyPrivateJwkOctAlg,
        CreateSigningKeyBodyPrivateJwkOctKeyOpsItem,
        CreateSigningKeyBodyPrivateJwkOctUse,
        CreateSigningKeyBodyPrivateJwkOkp,
        CreateSigningKeyBodyPrivateJwkOkpAlg,
        CreateSigningKeyBodyPrivateJwkOkpCrv,
        CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem,
        CreateSigningKeyBodyPrivateJwkOkpUse,
        CreateSigningKeyBodyPrivateJwkRsa,
        CreateSigningKeyBodyPrivateJwkRsaAlg,
        CreateSigningKeyBodyPrivateJwkRsaE,
        CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem,
        CreateSigningKeyBodyPrivateJwkRsaUse,
        CreateSigningKeyBodyPrivateJwk_Ec,
        CreateSigningKeyBodyPrivateJwk_Oct,
        CreateSigningKeyBodyPrivateJwk_Okp,
        CreateSigningKeyBodyPrivateJwk_Rsa,
        CreateSigningKeyBodyStatus,
        UpdateAuthConfigBodyDbMaxPoolSizeUnit,
        UpdateAuthConfigBodyPasswordRequiredCharacters,
        UpdateAuthConfigBodySecurityCaptchaProvider,
        UpdateAuthConfigBodySmsProvider,
        UpdateProviderBodyAttributeMapping,
        UpdateProviderBodyAttributeMappingKeysValue,
        UpdateProviderBodyAttributeMappingKeysValueDefault,
        UpdateProviderBodyAttributeMappingKeysValueDefaultZero,
        UpdateProviderBodyNameIdFormat,
        UpdateSigningKeyBodyStatus,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateProviderBodyAttributeMapping": ".types",
    "CreateProviderBodyAttributeMappingKeysValue": ".types",
    "CreateProviderBodyAttributeMappingKeysValueDefault": ".types",
    "CreateProviderBodyAttributeMappingKeysValueDefaultZero": ".types",
    "CreateProviderBodyNameIdFormat": ".types",
    "CreateProviderBodyType": ".types",
    "CreateSigningKeyBodyAlgorithm": ".types",
    "CreateSigningKeyBodyPrivateJwk": ".types",
    "CreateSigningKeyBodyPrivateJwkEc": ".types",
    "CreateSigningKeyBodyPrivateJwkEcAlg": ".types",
    "CreateSigningKeyBodyPrivateJwkEcCrv": ".types",
    "CreateSigningKeyBodyPrivateJwkEcKeyOpsItem": ".types",
    "CreateSigningKeyBodyPrivateJwkEcUse": ".types",
    "CreateSigningKeyBodyPrivateJwkOct": ".types",
    "CreateSigningKeyBodyPrivateJwkOctAlg": ".types",
    "CreateSigningKeyBodyPrivateJwkOctKeyOpsItem": ".types",
    "CreateSigningKeyBodyPrivateJwkOctUse": ".types",
    "CreateSigningKeyBodyPrivateJwkOkp": ".types",
    "CreateSigningKeyBodyPrivateJwkOkpAlg": ".types",
    "CreateSigningKeyBodyPrivateJwkOkpCrv": ".types",
    "CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem": ".types",
    "CreateSigningKeyBodyPrivateJwkOkpUse": ".types",
    "CreateSigningKeyBodyPrivateJwkRsa": ".types",
    "CreateSigningKeyBodyPrivateJwkRsaAlg": ".types",
    "CreateSigningKeyBodyPrivateJwkRsaE": ".types",
    "CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem": ".types",
    "CreateSigningKeyBodyPrivateJwkRsaUse": ".types",
    "CreateSigningKeyBodyPrivateJwk_Ec": ".types",
    "CreateSigningKeyBodyPrivateJwk_Oct": ".types",
    "CreateSigningKeyBodyPrivateJwk_Okp": ".types",
    "CreateSigningKeyBodyPrivateJwk_Rsa": ".types",
    "CreateSigningKeyBodyStatus": ".types",
    "UpdateAuthConfigBodyDbMaxPoolSizeUnit": ".types",
    "UpdateAuthConfigBodyPasswordRequiredCharacters": ".types",
    "UpdateAuthConfigBodySecurityCaptchaProvider": ".types",
    "UpdateAuthConfigBodySmsProvider": ".types",
    "UpdateProviderBodyAttributeMapping": ".types",
    "UpdateProviderBodyAttributeMappingKeysValue": ".types",
    "UpdateProviderBodyAttributeMappingKeysValueDefault": ".types",
    "UpdateProviderBodyAttributeMappingKeysValueDefaultZero": ".types",
    "UpdateProviderBodyNameIdFormat": ".types",
    "UpdateSigningKeyBodyStatus": ".types",
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
    "CreateProviderBodyAttributeMapping",
    "CreateProviderBodyAttributeMappingKeysValue",
    "CreateProviderBodyAttributeMappingKeysValueDefault",
    "CreateProviderBodyAttributeMappingKeysValueDefaultZero",
    "CreateProviderBodyNameIdFormat",
    "CreateProviderBodyType",
    "CreateSigningKeyBodyAlgorithm",
    "CreateSigningKeyBodyPrivateJwk",
    "CreateSigningKeyBodyPrivateJwkEc",
    "CreateSigningKeyBodyPrivateJwkEcAlg",
    "CreateSigningKeyBodyPrivateJwkEcCrv",
    "CreateSigningKeyBodyPrivateJwkEcKeyOpsItem",
    "CreateSigningKeyBodyPrivateJwkEcUse",
    "CreateSigningKeyBodyPrivateJwkOct",
    "CreateSigningKeyBodyPrivateJwkOctAlg",
    "CreateSigningKeyBodyPrivateJwkOctKeyOpsItem",
    "CreateSigningKeyBodyPrivateJwkOctUse",
    "CreateSigningKeyBodyPrivateJwkOkp",
    "CreateSigningKeyBodyPrivateJwkOkpAlg",
    "CreateSigningKeyBodyPrivateJwkOkpCrv",
    "CreateSigningKeyBodyPrivateJwkOkpKeyOpsItem",
    "CreateSigningKeyBodyPrivateJwkOkpUse",
    "CreateSigningKeyBodyPrivateJwkRsa",
    "CreateSigningKeyBodyPrivateJwkRsaAlg",
    "CreateSigningKeyBodyPrivateJwkRsaE",
    "CreateSigningKeyBodyPrivateJwkRsaKeyOpsItem",
    "CreateSigningKeyBodyPrivateJwkRsaUse",
    "CreateSigningKeyBodyPrivateJwk_Ec",
    "CreateSigningKeyBodyPrivateJwk_Oct",
    "CreateSigningKeyBodyPrivateJwk_Okp",
    "CreateSigningKeyBodyPrivateJwk_Rsa",
    "CreateSigningKeyBodyStatus",
    "UpdateAuthConfigBodyDbMaxPoolSizeUnit",
    "UpdateAuthConfigBodyPasswordRequiredCharacters",
    "UpdateAuthConfigBodySecurityCaptchaProvider",
    "UpdateAuthConfigBodySmsProvider",
    "UpdateProviderBodyAttributeMapping",
    "UpdateProviderBodyAttributeMappingKeysValue",
    "UpdateProviderBodyAttributeMappingKeysValueDefault",
    "UpdateProviderBodyAttributeMappingKeysValueDefaultZero",
    "UpdateProviderBodyNameIdFormat",
    "UpdateSigningKeyBodyStatus",
]
