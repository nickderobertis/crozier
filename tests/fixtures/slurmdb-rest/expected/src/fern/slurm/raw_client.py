

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.dbv0037account_info import Dbv0037AccountInfo
from ..types.dbv0037account_response import Dbv0037AccountResponse
from ..types.dbv0037associations_info import Dbv0037AssociationsInfo
from ..types.dbv0037cluster_info import Dbv0037ClusterInfo
from ..types.dbv0037config_info import Dbv0037ConfigInfo
from ..types.dbv0037config_response import Dbv0037ConfigResponse
from ..types.dbv0037diag import Dbv0037Diag
from ..types.dbv0037job_info import Dbv0037JobInfo
from ..types.dbv0037qos_info import Dbv0037QosInfo
from ..types.dbv0037response_account_delete import Dbv0037ResponseAccountDelete
from ..types.dbv0037response_association_delete import Dbv0037ResponseAssociationDelete
from ..types.dbv0037response_cluster_add import Dbv0037ResponseClusterAdd
from ..types.dbv0037response_cluster_delete import Dbv0037ResponseClusterDelete
from ..types.dbv0037response_qos_delete import Dbv0037ResponseQosDelete
from ..types.dbv0037response_tres import Dbv0037ResponseTres
from ..types.dbv0037response_user_delete import Dbv0037ResponseUserDelete
from ..types.dbv0037response_user_update import Dbv0037ResponseUserUpdate
from ..types.dbv0037response_wckey_add import Dbv0037ResponseWckeyAdd
from ..types.dbv0037response_wckey_delete import Dbv0037ResponseWckeyDelete
from ..types.dbv0037tres_info import Dbv0037TresInfo
from ..types.dbv0037user_info import Dbv0037UserInfo
from ..types.dbv0037wckey_info import Dbv0037WckeyInfo
from pydantic import ValidationError


class RawSlurmClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def slurmdbd_get_job(
        self, job_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037JobInfo]:
        """
        This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

        Parameters
        ----------
        job_id : int
            Slurm Job ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037JobInfo]
            Job description
        """
        _response = self._client_wrapper.httpx_client.request(
            f"job/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037JobInfo,
                    parse_obj_as(
                        type_=Dbv0037JobInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_db_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ConfigInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ConfigInfo]
            slurmdbd configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            "config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ConfigInfo,
                    parse_obj_as(
                        type_=Dbv0037ConfigInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_set_db_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ConfigResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ConfigResponse]
            Load config
        """
        _response = self._client_wrapper.httpx_client.request(
            "config",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ConfigResponse,
                    parse_obj_as(
                        type_=Dbv0037ConfigResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_tres(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037TresInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037TresInfo]
            List of TRES
        """
        _response = self._client_wrapper.httpx_client.request(
            "tres/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037TresInfo,
                    parse_obj_as(
                        type_=Dbv0037TresInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_update_tres(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ResponseTres]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ResponseTres]
            List of TRES
        """
        _response = self._client_wrapper.httpx_client.request(
            "tres/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseTres,
                    parse_obj_as(
                        type_=Dbv0037ResponseTres,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_single_qos(
        self, qos_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037QosInfo]:
        """
        Parameters
        ----------
        qos_name : str
            Slurm QOS Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037QosInfo]
            QOS information
        """
        _response = self._client_wrapper.httpx_client.request(
            f"qos/{encode_path_param(qos_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037QosInfo,
                    parse_obj_as(
                        type_=Dbv0037QosInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_delete_qos(
        self, qos_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ResponseQosDelete]:
        """
        Parameters
        ----------
        qos_name : str
            Slurm QOS Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ResponseQosDelete]
            Delete qos
        """
        _response = self._client_wrapper.httpx_client.request(
            f"qos/{encode_path_param(qos_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseQosDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseQosDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_qos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037QosInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037QosInfo]
            List of QOS'
        """
        _response = self._client_wrapper.httpx_client.request(
            "qos/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037QosInfo,
                    parse_obj_as(
                        type_=Dbv0037QosInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_associations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037AssociationsInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037AssociationsInfo]
            List of associations
        """
        _response = self._client_wrapper.httpx_client.request(
            "associations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037AssociationsInfo,
                    parse_obj_as(
                        type_=Dbv0037AssociationsInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_association(
        self,
        *,
        cluster: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dbv0037AssociationsInfo]:
        """
        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster name

        account : typing.Optional[str]
            Account name

        user : typing.Optional[str]
            User name

        partition : typing.Optional[str]
            Partition Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037AssociationsInfo]
            List of associations
        """
        _response = self._client_wrapper.httpx_client.request(
            "association/",
            method="GET",
            params={
                "cluster": cluster,
                "account": account,
                "user": user,
                "partition": partition,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037AssociationsInfo,
                    parse_obj_as(
                        type_=Dbv0037AssociationsInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_delete_association(
        self,
        *,
        account: str,
        user: str,
        cluster: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dbv0037ResponseAssociationDelete]:
        """
        Parameters
        ----------
        account : str
            Account name

        user : str
            User name

        cluster : typing.Optional[str]
            Cluster name

        partition : typing.Optional[str]
            Partition Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ResponseAssociationDelete]
            Delete associations
        """
        _response = self._client_wrapper.httpx_client.request(
            "association/",
            method="DELETE",
            params={
                "cluster": cluster,
                "account": account,
                "user": user,
                "partition": partition,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseAssociationDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseAssociationDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_user(
        self, user_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037UserInfo]:
        """
        Parameters
        ----------
        user_name : str
            Slurm User Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037UserInfo]
            List of users
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037UserInfo,
                    parse_obj_as(
                        type_=Dbv0037UserInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_delete_user(
        self, user_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ResponseUserDelete]:
        """
        Parameters
        ----------
        user_name : str
            Slurm User Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ResponseUserDelete]
            Delete user
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseUserDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseUserDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037UserInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037UserInfo]
            List of users
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037UserInfo,
                    parse_obj_as(
                        type_=Dbv0037UserInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_update_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ResponseUserUpdate]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ResponseUserUpdate]
            Update users
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseUserUpdate,
                    parse_obj_as(
                        type_=Dbv0037ResponseUserUpdate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_cluster(
        self, cluster_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ClusterInfo]:
        """
        Parameters
        ----------
        cluster_name : str
            Slurm cluster name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ClusterInfo]
            Cluster information
        """
        _response = self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ClusterInfo,
                    parse_obj_as(
                        type_=Dbv0037ClusterInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_delete_cluster(
        self, cluster_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ResponseClusterDelete]:
        """
        Parameters
        ----------
        cluster_name : str
            Slurm cluster name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ResponseClusterDelete]
            Delete cluster
        """
        _response = self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseClusterDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseClusterDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_clusters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ClusterInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ClusterInfo]
            List of clusters
        """
        _response = self._client_wrapper.httpx_client.request(
            "clusters/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ClusterInfo,
                    parse_obj_as(
                        type_=Dbv0037ClusterInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_add_clusters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ResponseClusterAdd]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ResponseClusterAdd]
            List of clusters
        """
        _response = self._client_wrapper.httpx_client.request(
            "clusters/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseClusterAdd,
                    parse_obj_as(
                        type_=Dbv0037ResponseClusterAdd,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_wckey(
        self, wckey: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037WckeyInfo]:
        """
        Parameters
        ----------
        wckey : str
            Slurm wckey name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037WckeyInfo]
            List of wckey
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wckey/{encode_path_param(wckey)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037WckeyInfo,
                    parse_obj_as(
                        type_=Dbv0037WckeyInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_delete_wckey(
        self, wckey: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ResponseWckeyDelete]:
        """
        Parameters
        ----------
        wckey : str
            Slurm wckey name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ResponseWckeyDelete]
            Delete wckey
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wckey/{encode_path_param(wckey)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseWckeyDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseWckeyDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_wckeys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037WckeyInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037WckeyInfo]
            List of wckeys
        """
        _response = self._client_wrapper.httpx_client.request(
            "wckeys/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037WckeyInfo,
                    parse_obj_as(
                        type_=Dbv0037WckeyInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_add_wckeys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ResponseWckeyAdd]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ResponseWckeyAdd]
            List of wckeys
        """
        _response = self._client_wrapper.httpx_client.request(
            "wckeys/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseWckeyAdd,
                    parse_obj_as(
                        type_=Dbv0037ResponseWckeyAdd,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_account(
        self, account_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037AccountInfo]:
        """
        Parameters
        ----------
        account_name : str
            Slurm Account Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037AccountInfo]
            List of accounts
        """
        _response = self._client_wrapper.httpx_client.request(
            f"account/{encode_path_param(account_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037AccountInfo,
                    parse_obj_as(
                        type_=Dbv0037AccountInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_delete_account(
        self, account_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037ResponseAccountDelete]:
        """
        Parameters
        ----------
        account_name : str
            Slurm Account Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037ResponseAccountDelete]
            Delete account
        """
        _response = self._client_wrapper.httpx_client.request(
            f"account/{encode_path_param(account_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseAccountDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseAccountDelete,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037AccountInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037AccountInfo]
            List of accounts
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounts/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037AccountInfo,
                    parse_obj_as(
                        type_=Dbv0037AccountInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_update_account(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dbv0037AccountResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037AccountResponse]
            Add/update list of accounts
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounts/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037AccountResponse,
                    parse_obj_as(
                        type_=Dbv0037AccountResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_get_jobs(
        self,
        *,
        submit_time: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        association: typing.Optional[str] = None,
        cluster: typing.Optional[str] = None,
        constraints: typing.Optional[str] = None,
        cpus_max: typing.Optional[str] = None,
        cpus_min: typing.Optional[str] = None,
        skip_steps: typing.Optional[bool] = None,
        disable_wait_for_result: typing.Optional[bool] = None,
        exit_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        job_name: typing.Optional[str] = None,
        nodes_max: typing.Optional[str] = None,
        nodes_min: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        qos: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        reservation: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        step: typing.Optional[str] = None,
        node: typing.Optional[str] = None,
        wckey: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dbv0037JobInfo]:
        """
        Parameters
        ----------
        submit_time : typing.Optional[str]
            Filter by submission time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        start_time : typing.Optional[str]
            Filter by start time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        end_time : typing.Optional[str]
            Filter by end time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        account : typing.Optional[str]
            Comma delimited list of accounts to match

        association : typing.Optional[str]
            Comma delimited list of associations to match

        cluster : typing.Optional[str]
            Comma delimited list of cluster to match

        constraints : typing.Optional[str]
            Comma delimited list of constraints to match

        cpus_max : typing.Optional[str]
            Number of CPUs high range

        cpus_min : typing.Optional[str]
            Number of CPUs low range

        skip_steps : typing.Optional[bool]
            Report job step information

        disable_wait_for_result : typing.Optional[bool]
            Disable waiting for result from slurmdbd

        exit_code : typing.Optional[str]
            Exit code of job

        format : typing.Optional[str]
            Comma delimited list of formats to match

        group : typing.Optional[str]
            Comma delimited list of groups to match

        job_name : typing.Optional[str]
            Comma delimited list of job names to match

        nodes_max : typing.Optional[str]
            Number of nodes high range

        nodes_min : typing.Optional[str]
            Number of nodes low range

        partition : typing.Optional[str]
            Comma delimited list of partitions to match

        qos : typing.Optional[str]
            Comma delimited list of QOS to match

        reason : typing.Optional[str]
            Comma delimited list of job reasons to match

        reservation : typing.Optional[str]
            Comma delimited list of reservations to match

        state : typing.Optional[str]
            Comma delimited list of states to match

        step : typing.Optional[str]
            Comma delimited list of job steps to match

        node : typing.Optional[str]
            Comma delimited list of used nodes to match

        wckey : typing.Optional[str]
            Comma delimited list of wckeys to match

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037JobInfo]
            List of jobs
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs/",
            method="GET",
            params={
                "submit_time": submit_time,
                "start_time": start_time,
                "end_time": end_time,
                "account": account,
                "association": association,
                "cluster": cluster,
                "constraints": constraints,
                "cpus_max": cpus_max,
                "cpus_min": cpus_min,
                "skip_steps": skip_steps,
                "disable_wait_for_result": disable_wait_for_result,
                "exit_code": exit_code,
                "format": format,
                "group": group,
                "job_name": job_name,
                "nodes_max": nodes_max,
                "nodes_min": nodes_min,
                "partition": partition,
                "qos": qos,
                "reason": reason,
                "reservation": reservation,
                "state": state,
                "step": step,
                "node": node,
                "wckey": wckey,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037JobInfo,
                    parse_obj_as(
                        type_=Dbv0037JobInfo,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def slurmdbd_diag(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Dbv0037Diag]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dbv0037Diag]
            Dictionary of statistics
        """
        _response = self._client_wrapper.httpx_client.request(
            "diag/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037Diag,
                    parse_obj_as(
                        type_=Dbv0037Diag,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSlurmClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def slurmdbd_get_job(
        self, job_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037JobInfo]:
        """
        This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

        Parameters
        ----------
        job_id : int
            Slurm Job ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037JobInfo]
            Job description
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"job/{encode_path_param(job_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037JobInfo,
                    parse_obj_as(
                        type_=Dbv0037JobInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_db_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ConfigInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ConfigInfo]
            slurmdbd configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            "config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ConfigInfo,
                    parse_obj_as(
                        type_=Dbv0037ConfigInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_set_db_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ConfigResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ConfigResponse]
            Load config
        """
        _response = await self._client_wrapper.httpx_client.request(
            "config",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ConfigResponse,
                    parse_obj_as(
                        type_=Dbv0037ConfigResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_tres(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037TresInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037TresInfo]
            List of TRES
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tres/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037TresInfo,
                    parse_obj_as(
                        type_=Dbv0037TresInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_update_tres(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ResponseTres]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ResponseTres]
            List of TRES
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tres/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseTres,
                    parse_obj_as(
                        type_=Dbv0037ResponseTres,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_single_qos(
        self, qos_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037QosInfo]:
        """
        Parameters
        ----------
        qos_name : str
            Slurm QOS Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037QosInfo]
            QOS information
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"qos/{encode_path_param(qos_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037QosInfo,
                    parse_obj_as(
                        type_=Dbv0037QosInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_delete_qos(
        self, qos_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ResponseQosDelete]:
        """
        Parameters
        ----------
        qos_name : str
            Slurm QOS Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ResponseQosDelete]
            Delete qos
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"qos/{encode_path_param(qos_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseQosDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseQosDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_qos(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037QosInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037QosInfo]
            List of QOS'
        """
        _response = await self._client_wrapper.httpx_client.request(
            "qos/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037QosInfo,
                    parse_obj_as(
                        type_=Dbv0037QosInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_associations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037AssociationsInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037AssociationsInfo]
            List of associations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "associations/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037AssociationsInfo,
                    parse_obj_as(
                        type_=Dbv0037AssociationsInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_association(
        self,
        *,
        cluster: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dbv0037AssociationsInfo]:
        """
        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster name

        account : typing.Optional[str]
            Account name

        user : typing.Optional[str]
            User name

        partition : typing.Optional[str]
            Partition Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037AssociationsInfo]
            List of associations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "association/",
            method="GET",
            params={
                "cluster": cluster,
                "account": account,
                "user": user,
                "partition": partition,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037AssociationsInfo,
                    parse_obj_as(
                        type_=Dbv0037AssociationsInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_delete_association(
        self,
        *,
        account: str,
        user: str,
        cluster: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dbv0037ResponseAssociationDelete]:
        """
        Parameters
        ----------
        account : str
            Account name

        user : str
            User name

        cluster : typing.Optional[str]
            Cluster name

        partition : typing.Optional[str]
            Partition Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ResponseAssociationDelete]
            Delete associations
        """
        _response = await self._client_wrapper.httpx_client.request(
            "association/",
            method="DELETE",
            params={
                "cluster": cluster,
                "account": account,
                "user": user,
                "partition": partition,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseAssociationDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseAssociationDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_user(
        self, user_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037UserInfo]:
        """
        Parameters
        ----------
        user_name : str
            Slurm User Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037UserInfo]
            List of users
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037UserInfo,
                    parse_obj_as(
                        type_=Dbv0037UserInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_delete_user(
        self, user_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ResponseUserDelete]:
        """
        Parameters
        ----------
        user_name : str
            Slurm User Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ResponseUserDelete]
            Delete user
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseUserDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseUserDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037UserInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037UserInfo]
            List of users
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037UserInfo,
                    parse_obj_as(
                        type_=Dbv0037UserInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_update_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ResponseUserUpdate]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ResponseUserUpdate]
            Update users
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseUserUpdate,
                    parse_obj_as(
                        type_=Dbv0037ResponseUserUpdate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_cluster(
        self, cluster_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ClusterInfo]:
        """
        Parameters
        ----------
        cluster_name : str
            Slurm cluster name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ClusterInfo]
            Cluster information
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ClusterInfo,
                    parse_obj_as(
                        type_=Dbv0037ClusterInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_delete_cluster(
        self, cluster_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ResponseClusterDelete]:
        """
        Parameters
        ----------
        cluster_name : str
            Slurm cluster name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ResponseClusterDelete]
            Delete cluster
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseClusterDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseClusterDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_clusters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ClusterInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ClusterInfo]
            List of clusters
        """
        _response = await self._client_wrapper.httpx_client.request(
            "clusters/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ClusterInfo,
                    parse_obj_as(
                        type_=Dbv0037ClusterInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_add_clusters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ResponseClusterAdd]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ResponseClusterAdd]
            List of clusters
        """
        _response = await self._client_wrapper.httpx_client.request(
            "clusters/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseClusterAdd,
                    parse_obj_as(
                        type_=Dbv0037ResponseClusterAdd,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_wckey(
        self, wckey: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037WckeyInfo]:
        """
        Parameters
        ----------
        wckey : str
            Slurm wckey name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037WckeyInfo]
            List of wckey
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wckey/{encode_path_param(wckey)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037WckeyInfo,
                    parse_obj_as(
                        type_=Dbv0037WckeyInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_delete_wckey(
        self, wckey: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ResponseWckeyDelete]:
        """
        Parameters
        ----------
        wckey : str
            Slurm wckey name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ResponseWckeyDelete]
            Delete wckey
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wckey/{encode_path_param(wckey)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseWckeyDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseWckeyDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_wckeys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037WckeyInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037WckeyInfo]
            List of wckeys
        """
        _response = await self._client_wrapper.httpx_client.request(
            "wckeys/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037WckeyInfo,
                    parse_obj_as(
                        type_=Dbv0037WckeyInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_add_wckeys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ResponseWckeyAdd]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ResponseWckeyAdd]
            List of wckeys
        """
        _response = await self._client_wrapper.httpx_client.request(
            "wckeys/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseWckeyAdd,
                    parse_obj_as(
                        type_=Dbv0037ResponseWckeyAdd,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_account(
        self, account_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037AccountInfo]:
        """
        Parameters
        ----------
        account_name : str
            Slurm Account Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037AccountInfo]
            List of accounts
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"account/{encode_path_param(account_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037AccountInfo,
                    parse_obj_as(
                        type_=Dbv0037AccountInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_delete_account(
        self, account_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037ResponseAccountDelete]:
        """
        Parameters
        ----------
        account_name : str
            Slurm Account Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037ResponseAccountDelete]
            Delete account
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"account/{encode_path_param(account_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037ResponseAccountDelete,
                    parse_obj_as(
                        type_=Dbv0037ResponseAccountDelete,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037AccountInfo]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037AccountInfo]
            List of accounts
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounts/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037AccountInfo,
                    parse_obj_as(
                        type_=Dbv0037AccountInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_update_account(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037AccountResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037AccountResponse]
            Add/update list of accounts
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounts/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037AccountResponse,
                    parse_obj_as(
                        type_=Dbv0037AccountResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_get_jobs(
        self,
        *,
        submit_time: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        association: typing.Optional[str] = None,
        cluster: typing.Optional[str] = None,
        constraints: typing.Optional[str] = None,
        cpus_max: typing.Optional[str] = None,
        cpus_min: typing.Optional[str] = None,
        skip_steps: typing.Optional[bool] = None,
        disable_wait_for_result: typing.Optional[bool] = None,
        exit_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        job_name: typing.Optional[str] = None,
        nodes_max: typing.Optional[str] = None,
        nodes_min: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        qos: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        reservation: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        step: typing.Optional[str] = None,
        node: typing.Optional[str] = None,
        wckey: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dbv0037JobInfo]:
        """
        Parameters
        ----------
        submit_time : typing.Optional[str]
            Filter by submission time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        start_time : typing.Optional[str]
            Filter by start time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        end_time : typing.Optional[str]
            Filter by end time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        account : typing.Optional[str]
            Comma delimited list of accounts to match

        association : typing.Optional[str]
            Comma delimited list of associations to match

        cluster : typing.Optional[str]
            Comma delimited list of cluster to match

        constraints : typing.Optional[str]
            Comma delimited list of constraints to match

        cpus_max : typing.Optional[str]
            Number of CPUs high range

        cpus_min : typing.Optional[str]
            Number of CPUs low range

        skip_steps : typing.Optional[bool]
            Report job step information

        disable_wait_for_result : typing.Optional[bool]
            Disable waiting for result from slurmdbd

        exit_code : typing.Optional[str]
            Exit code of job

        format : typing.Optional[str]
            Comma delimited list of formats to match

        group : typing.Optional[str]
            Comma delimited list of groups to match

        job_name : typing.Optional[str]
            Comma delimited list of job names to match

        nodes_max : typing.Optional[str]
            Number of nodes high range

        nodes_min : typing.Optional[str]
            Number of nodes low range

        partition : typing.Optional[str]
            Comma delimited list of partitions to match

        qos : typing.Optional[str]
            Comma delimited list of QOS to match

        reason : typing.Optional[str]
            Comma delimited list of job reasons to match

        reservation : typing.Optional[str]
            Comma delimited list of reservations to match

        state : typing.Optional[str]
            Comma delimited list of states to match

        step : typing.Optional[str]
            Comma delimited list of job steps to match

        node : typing.Optional[str]
            Comma delimited list of used nodes to match

        wckey : typing.Optional[str]
            Comma delimited list of wckeys to match

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037JobInfo]
            List of jobs
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs/",
            method="GET",
            params={
                "submit_time": submit_time,
                "start_time": start_time,
                "end_time": end_time,
                "account": account,
                "association": association,
                "cluster": cluster,
                "constraints": constraints,
                "cpus_max": cpus_max,
                "cpus_min": cpus_min,
                "skip_steps": skip_steps,
                "disable_wait_for_result": disable_wait_for_result,
                "exit_code": exit_code,
                "format": format,
                "group": group,
                "job_name": job_name,
                "nodes_max": nodes_max,
                "nodes_min": nodes_min,
                "partition": partition,
                "qos": qos,
                "reason": reason,
                "reservation": reservation,
                "state": state,
                "step": step,
                "node": node,
                "wckey": wckey,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037JobInfo,
                    parse_obj_as(
                        type_=Dbv0037JobInfo,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def slurmdbd_diag(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dbv0037Diag]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dbv0037Diag]
            Dictionary of statistics
        """
        _response = await self._client_wrapper.httpx_client.request(
            "diag/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dbv0037Diag,
                    parse_obj_as(
                        type_=Dbv0037Diag,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
