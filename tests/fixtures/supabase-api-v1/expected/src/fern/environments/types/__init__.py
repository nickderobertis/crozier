



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_branch_body_desired_instance_size import CreateBranchBodyDesiredInstanceSize
    from .create_branch_body_postgres_engine import CreateBranchBodyPostgresEngine
    from .create_branch_body_release_channel import CreateBranchBodyReleaseChannel
    from .update_branch_body_status import UpdateBranchBodyStatus
    from .update_run_status_body_clone import UpdateRunStatusBodyClone
    from .update_run_status_body_configure import UpdateRunStatusBodyConfigure
    from .update_run_status_body_deploy import UpdateRunStatusBodyDeploy
    from .update_run_status_body_health import UpdateRunStatusBodyHealth
    from .update_run_status_body_migrate import UpdateRunStatusBodyMigrate
    from .update_run_status_body_pull import UpdateRunStatusBodyPull
    from .update_run_status_body_seed import UpdateRunStatusBodySeed
_dynamic_imports: typing.Dict[str, str] = {
    "CreateBranchBodyDesiredInstanceSize": ".create_branch_body_desired_instance_size",
    "CreateBranchBodyPostgresEngine": ".create_branch_body_postgres_engine",
    "CreateBranchBodyReleaseChannel": ".create_branch_body_release_channel",
    "UpdateBranchBodyStatus": ".update_branch_body_status",
    "UpdateRunStatusBodyClone": ".update_run_status_body_clone",
    "UpdateRunStatusBodyConfigure": ".update_run_status_body_configure",
    "UpdateRunStatusBodyDeploy": ".update_run_status_body_deploy",
    "UpdateRunStatusBodyHealth": ".update_run_status_body_health",
    "UpdateRunStatusBodyMigrate": ".update_run_status_body_migrate",
    "UpdateRunStatusBodyPull": ".update_run_status_body_pull",
    "UpdateRunStatusBodySeed": ".update_run_status_body_seed",
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
    "CreateBranchBodyDesiredInstanceSize",
    "CreateBranchBodyPostgresEngine",
    "CreateBranchBodyReleaseChannel",
    "UpdateBranchBodyStatus",
    "UpdateRunStatusBodyClone",
    "UpdateRunStatusBodyConfigure",
    "UpdateRunStatusBodyDeploy",
    "UpdateRunStatusBodyHealth",
    "UpdateRunStatusBodyMigrate",
    "UpdateRunStatusBodyPull",
    "UpdateRunStatusBodySeed",
]
