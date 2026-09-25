

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok32 import Ok32
from ..types.ok34 import Ok34
from ..types.ok35 import Ok35
from ..types.ok36 import Ok36
from ..types.ok37 import Ok37
from ..types.ok38 import Ok38
from ..types.ok39 import Ok39
from ..types.ok40 import Ok40
from ..types.ok41 import Ok41
from ..types.ok42 import Ok42
from ..types.ok43 import Ok43
from ..types.ok44 import Ok44
from ..types.ok45 import Ok45
from ..types.ok46 import Ok46
from ..types.ok47 import Ok47
from ..types.ok49 import Ok49
from .raw_client import AsyncRawImmunizationsClient, RawImmunizationsClient


OMIT = typing.cast(typing.Any, ...)


class ImmunizationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImmunizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImmunizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImmunizationsClient
        """
        return self._raw_client

    def base_url_persons_charts_immunizations(
        self,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok32:
        """
        GETs immunizations updated within a given interval. If an oData filter of createTimestamp or modifyTimestamp is not specified, immunizations which are created or updated for the last 7 days are retrieved.

        Parameters
        ----------
        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok32
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_charts_immunizations(
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_charts_immunizations(
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a patient's immunization order record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization order record is being added

        encounter_id : str
            (Required) (Required) The id of the encounter for which the immunization order is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders(
            person_id="personId",
            encounter_id="encounterId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's immunization order record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization order record is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter that contains the immunization order is being updated

        order_id : str
            (Required) (Required) The id of the immunization order being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id(
            person_id="personId",
            encounter_id="encounterId",
            order_id="orderId",
            request={"key": "value"},
        )
        """
        _response = (
            self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id(
                person_id, encounter_id, order_id, request=request, request_options=request_options
            )
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a patient's ordered vaccine record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine record is being added

        encounter_id : str
            (Required) (Required) The id of the encounter that contains the immunization order to which vaccine record id being added

        order_id : str
            (Required) (Required) The id of the immunization order to which vaccine record is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines(
            person_id="personId",
            encounter_id="encounterId",
            order_id="orderId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines(
            person_id, encounter_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        vaccine_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's vaccine record.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine record is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter for the immunization order which contains the vaccine being updated

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine being updated

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id(
            person_id="personId",
            encounter_id="encounterId",
            order_id="orderId",
            vaccine_id="vaccineId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id(
            person_id, encounter_id, order_id, vaccine_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        vaccine_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds vaccine vis history for the provided ordered vaccine

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person associated with the vaccine vis history that is being added

        encounter_id : str
            (Required) (Required) The id of the encounter associated with the vaccine for which vis history is being added

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine for which vis history is being added

        vaccine_id : str
            (Required) (Required) The id of the vaccine for which vis history is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
            person_id="personId",
            encounter_id="encounterId",
            order_id="orderId",
            vaccine_id="vaccineId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
            person_id, encounter_id, order_id, vaccine_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_vis_id(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        vaccine_id: str,
        vis_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's vaccine vis history record.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person associated with the vaccine vis history that is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter associated with the vaccine for which vis history is being updated

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine for which vis history is being updated

        vaccine_id : str
            (Required) (Required) The id of the vaccine for which vis history is being updated

        vis_id : str
            (Required) (Required) The id of the vis history record that is being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_vis_id(
            person_id="personId",
            encounter_id="encounterId",
            order_id="orderId",
            vaccine_id="vaccineId",
            vis_id="visId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_vis_id(
            person_id, encounter_id, order_id, vaccine_id, vis_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        vaccine_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a wasted vaccine record associated with a patient's ordered vaccine.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered vaccine is associated with the wasted vaccine record that is being added

        encounter_id : str
            (Required) (Required) The id of the encounter that contains the ordered vaccine that is associated with the wasted vaccine record

        order_id : str
            (Required) (Required) The id of the immunization order which contains the ordered vaccine associated with the wasted vaccine record

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine that is associated with the wasted vaccine that is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
            person_id="personId",
            encounter_id="encounterId",
            order_id="orderId",
            vaccine_id="vaccineId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
            person_id, encounter_id, order_id, vaccine_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok32:
        """
        Gets a list of ordered vaccines for the specified person id after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered vaccines are being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok32
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_dose_validation(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok34:
        """
        Gets a list of vaccine dose validation for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine dose validation information is being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok34
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_dose_validation(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_dose_validation(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_exclusions(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok35:
        """
        Gets a list of excluded vaccines for the specified person id after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose excluded vaccines are being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok35
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_exclusions(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_exclusions(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def post_base_url_persons_person_id_chart_immunizations_exclusions(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a patient's vaccine exclusion record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine exclusion record is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.post_base_url_persons_person_id_chart_immunizations_exclusions(
            person_id="personId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_immunizations_exclusions(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_exclusions_exclusion_id(
        self,
        person_id: str,
        exclusion_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's excluded vaccine record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose excluded vaccine record is being updated

        exclusion_id : str
            (Required) (Required) The id of the excluded vaccine being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_exclusions_exclusion_id(
            person_id="personId",
            exclusion_id="exclusionId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_exclusions_exclusion_id(
            person_id, exclusion_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_group_status(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok36:
        """
        Gets a list of vaccine group status for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine group statuses are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok36
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_group_status(
            person_id="personId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_group_status(
            person_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_interactions(
        self, person_id: str, *, cvx_code: str, cpt_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok37:
        """
        Gets patient interactions for a vaccine with the given CVX and CPT codes.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose interactions are being retrieved

        cvx_code : str
            (Required) The cvx code of the vaccine for which interaction are being retrieved

        cpt_code : str
            (Required) The cpt code of the vaccine for which interaction are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok37
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_interactions(
            person_id="personId",
            cvx_code="cvxCode",
            cpt_code="cptCode",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_interactions(
            person_id, cvx_code=cvx_code, cpt_code=cpt_code, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok38:
        """
        Gets immunization orders for the specified person after performing additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization order is being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok38
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok39:
        """
        Gets immunization order details for the specified person and order.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization order is being retrieved

        order_id : str
            (Required) (Required) The id of the immunization order being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok39
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id(
            person_id="personId",
            order_id="orderId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id_insurances(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok40:
        """
        Get a list of insurances that are associated with the specified person Id and order Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom the order insurances are being retrieved

        order_id : str
            (Required) (Required) The id of the immunization order for which insurances are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok40
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_insurances(
            person_id="personId",
            order_id="orderId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_insurances(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok41:
        """
        Gets a list of tracking comments for the given person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to

        order_id : str
            (Required) (Required) The id of the order whose tracking comments are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok41
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
            person_id="personId",
            order_id="orderId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    def post_base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a tracking comment for the given person id and order id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to

        order_id : str
            (Required) (Required) The id of the order whose tracking comments are being retrieved

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.post_base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
            person_id="personId",
            order_id="orderId",
            request={"key": "value"},
        )
        """
        _response = (
            self._raw_client.post_base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
                person_id, order_id, request=request, request_options=request_options
            )
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok42:
        """
        Gets vaccines for the given person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to

        order_id : str
            (Required) (Required) The id of the order whose vaccines are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok42
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines(
            person_id="personId",
            order_id="orderId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id1(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok43:
        """
        Gets vaccine details for the given person id, order id, and vaccine id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to

        order_id : str
            (Required) (Required) The id of the order whose vaccines are being retrieved

        vaccine_id : str
            (Required) (Required) The id of the vaccine for which we are retrieving the details

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok43
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id1(
            person_id="personId",
            order_id="orderId",
            vaccine_id="vaccineId",
        )
        """
        _response = (
            self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id1(
                person_id, order_id, vaccine_id, request_options=request_options
            )
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a patient's ordered vaccine record.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine record is being deleted

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine being deleted

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine being deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id(
            person_id="personId",
            order_id="orderId",
            vaccine_id="vaccineId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id(
            person_id, order_id, vaccine_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_component_lot_numbers(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok44:
        """
        Get a list of component lot numbers for the specified ordered vaccine ID.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered vaccine component lot numbers are being retrieved

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine whose component lot numbers are being retrieved

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine whose component lot numbers are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok44
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_component_lot_numbers(
            person_id="personId",
            order_id="orderId",
            vaccine_id="vaccineId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_component_lot_numbers(
            person_id, order_id, vaccine_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_suspected_diagnoses(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok45:
        """
        Get a list of diagnosis for the specified ordered vaccine ID.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose diagnosis are being retrieved

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine whose associated diagnosis are being retrieved

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine whose associated diagnosis are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok45
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_suspected_diagnoses(
            person_id="personId",
            order_id="orderId",
            vaccine_id="vaccineId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_suspected_diagnoses(
            person_id, order_id, vaccine_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok46:
        """
        Get a list of VIS histories that are documented as given to the patient for the specified ordered vaccine ID.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for who the vaccine VIS history information belongs to

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine for which the vaccine VIS history information was documented

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine for which the vaccine VIS history information was recorded

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok46
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
            person_id="personId",
            order_id="orderId",
            vaccine_id="vaccineId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
            person_id, order_id, vaccine_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok47:
        """
        Gets a list of wasted vaccines for the specified person Id, order Id and vaccine Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) Id of the person whose wasted vaccines are being retrieved

        order_id : str
            (Required) (Required) Id of the order associated with the wasted vaccines that are being retrieved

        vaccine_id : str
            (Required) (Required) Id of the ordered vaccine whose wasted vaccines are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok47
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
            person_id="personId",
            order_id="orderId",
            vaccine_id="vaccineId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
            person_id, order_id, vaccine_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines_wasted_vaccine_id(
        self,
        person_id: str,
        order_id: str,
        vaccine_id: str,
        wasted_vaccine_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok47:
        """
        Gets the wasted vaccine details for the specified person Id, order Id, vaccine Id and wasted vaccine Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) Id of the person whose wasted vaccine details are being retrieved

        order_id : str
            (Required) (Required) Id of the order associated with the wasted vaccine detials that are being retrieved

        vaccine_id : str
            (Required) (Required) Id of the ordered vaccine whose wasted vaccine detials are being retrieved

        wasted_vaccine_id : str
            (Required) (Required) Id of the wasted vaccine whose detials are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok47
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines_wasted_vaccine_id(
            person_id="personId",
            order_id="orderId",
            vaccine_id="vaccineId",
            wasted_vaccine_id="wastedVaccineId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines_wasted_vaccine_id(
            person_id, order_id, vaccine_id, wasted_vaccine_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_series_completions(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok49:
        """
        Gets a patient's immunization series completion records.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization series completion records are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok49
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_series_completions(
            person_id="personId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_series_completions(
            person_id, request_options=request_options
        )
        return _response.data

    def post_base_url_persons_person_id_chart_immunizations_series_completions(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a patient's immunization series completion record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization series completion record is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.post_base_url_persons_person_id_chart_immunizations_series_completions(
            person_id="personId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_immunizations_series_completions(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_immunizations_series_completions_series_id(
        self, person_id: str, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok49:
        """
        Gets a patient's immunization series completion information for the provided person Id and series completion Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization series completion information is being retrieved

        series_id : str
            (Required) (Required) The id of the series completion record whose details are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok49
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.base_url_persons_person_id_chart_immunizations_series_completions_series_id(
            person_id="personId",
            series_id="seriesId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_immunizations_series_completions_series_id(
            person_id, series_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_immunizations_series_completions_series_id(
        self,
        person_id: str,
        series_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's immunization series completion record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization series completion record is being updated

        series_id : str
            (Required) (Required) The id of the series being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.immunizations.put_base_url_persons_person_id_chart_immunizations_series_completions_series_id(
            person_id="personId",
            series_id="seriesId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_immunizations_series_completions_series_id(
            person_id, series_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncImmunizationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImmunizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImmunizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImmunizationsClient
        """
        return self._raw_client

    async def base_url_persons_charts_immunizations(
        self,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok32:
        """
        GETs immunizations updated within a given interval. If an oData filter of createTimestamp or modifyTimestamp is not specified, immunizations which are created or updated for the last 7 days are retrieved.

        Parameters
        ----------
        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok32
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_charts_immunizations(
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_charts_immunizations(
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a patient's immunization order record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization order record is being added

        encounter_id : str
            (Required) (Required) The id of the encounter for which the immunization order is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders(
                person_id="personId",
                encounter_id="encounterId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders(
                person_id, encounter_id, request=request, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's immunization order record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization order record is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter that contains the immunization order is being updated

        order_id : str
            (Required) (Required) The id of the immunization order being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id(
                person_id="personId",
                encounter_id="encounterId",
                order_id="orderId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id(
            person_id, encounter_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a patient's ordered vaccine record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine record is being added

        encounter_id : str
            (Required) (Required) The id of the encounter that contains the immunization order to which vaccine record id being added

        order_id : str
            (Required) (Required) The id of the immunization order to which vaccine record is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines(
                person_id="personId",
                encounter_id="encounterId",
                order_id="orderId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines(
            person_id, encounter_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        vaccine_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's vaccine record.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine record is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter for the immunization order which contains the vaccine being updated

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine being updated

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id(
                person_id="personId",
                encounter_id="encounterId",
                order_id="orderId",
                vaccine_id="vaccineId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id(
            person_id, encounter_id, order_id, vaccine_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        vaccine_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds vaccine vis history for the provided ordered vaccine

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person associated with the vaccine vis history that is being added

        encounter_id : str
            (Required) (Required) The id of the encounter associated with the vaccine for which vis history is being added

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine for which vis history is being added

        vaccine_id : str
            (Required) (Required) The id of the vaccine for which vis history is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
                person_id="personId",
                encounter_id="encounterId",
                order_id="orderId",
                vaccine_id="vaccineId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
            person_id, encounter_id, order_id, vaccine_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_vis_id(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        vaccine_id: str,
        vis_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's vaccine vis history record.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person associated with the vaccine vis history that is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter associated with the vaccine for which vis history is being updated

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine for which vis history is being updated

        vaccine_id : str
            (Required) (Required) The id of the vaccine for which vis history is being updated

        vis_id : str
            (Required) (Required) The id of the vis history record that is being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_vis_id(
                person_id="personId",
                encounter_id="encounterId",
                order_id="orderId",
                vaccine_id="vaccineId",
                vis_id="visId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_vis_id(
            person_id, encounter_id, order_id, vaccine_id, vis_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
        self,
        person_id: str,
        encounter_id: str,
        order_id: str,
        vaccine_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a wasted vaccine record associated with a patient's ordered vaccine.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered vaccine is associated with the wasted vaccine record that is being added

        encounter_id : str
            (Required) (Required) The id of the encounter that contains the ordered vaccine that is associated with the wasted vaccine record

        order_id : str
            (Required) (Required) The id of the immunization order which contains the ordered vaccine associated with the wasted vaccine record

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine that is associated with the wasted vaccine that is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
                person_id="personId",
                encounter_id="encounterId",
                order_id="orderId",
                vaccine_id="vaccineId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
            person_id, encounter_id, order_id, vaccine_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok32:
        """
        Gets a list of ordered vaccines for the specified person id after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered vaccines are being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok32
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations(
                person_id="personId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_dose_validation(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok34:
        """
        Gets a list of vaccine dose validation for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine dose validation information is being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok34
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_dose_validation(
                person_id="personId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_dose_validation(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_exclusions(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok35:
        """
        Gets a list of excluded vaccines for the specified person id after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose excluded vaccines are being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok35
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_exclusions(
                person_id="personId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_exclusions(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_immunizations_exclusions(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a patient's vaccine exclusion record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine exclusion record is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.post_base_url_persons_person_id_chart_immunizations_exclusions(
                person_id="personId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_immunizations_exclusions(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_exclusions_exclusion_id(
        self,
        person_id: str,
        exclusion_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's excluded vaccine record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose excluded vaccine record is being updated

        exclusion_id : str
            (Required) (Required) The id of the excluded vaccine being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_exclusions_exclusion_id(
                person_id="personId",
                exclusion_id="exclusionId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_exclusions_exclusion_id(
            person_id, exclusion_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_group_status(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok36:
        """
        Gets a list of vaccine group status for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine group statuses are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok36
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_group_status(
                person_id="personId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_group_status(
            person_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_interactions(
        self, person_id: str, *, cvx_code: str, cpt_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok37:
        """
        Gets patient interactions for a vaccine with the given CVX and CPT codes.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose interactions are being retrieved

        cvx_code : str
            (Required) The cvx code of the vaccine for which interaction are being retrieved

        cpt_code : str
            (Required) The cpt code of the vaccine for which interaction are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok37
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_interactions(
                person_id="personId",
                cvx_code="cvxCode",
                cpt_code="cptCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_interactions(
            person_id, cvx_code=cvx_code, cpt_code=cpt_code, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok38:
        """
        Gets immunization orders for the specified person after performing additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization order is being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok38
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders(
                person_id="personId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_orders(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok39:
        """
        Gets immunization order details for the specified person and order.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization order is being retrieved

        order_id : str
            (Required) (Required) The id of the immunization order being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok39
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id(
                person_id="personId",
                order_id="orderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id_insurances(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok40:
        """
        Get a list of insurances that are associated with the specified person Id and order Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom the order insurances are being retrieved

        order_id : str
            (Required) (Required) The id of the immunization order for which insurances are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok40
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_insurances(
                person_id="personId",
                order_id="orderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_insurances(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok41:
        """
        Gets a list of tracking comments for the given person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to

        order_id : str
            (Required) (Required) The id of the order whose tracking comments are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok41
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
                person_id="personId",
                order_id="orderId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
                person_id, order_id, request_options=request_options
            )
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a tracking comment for the given person id and order id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to

        order_id : str
            (Required) (Required) The id of the order whose tracking comments are being retrieved

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.post_base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
                person_id="personId",
                order_id="orderId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments(
            person_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok42:
        """
        Gets vaccines for the given person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to

        order_id : str
            (Required) (Required) The id of the order whose vaccines are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok42
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines(
                person_id="personId",
                order_id="orderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id1(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok43:
        """
        Gets vaccine details for the given person id, order id, and vaccine id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to

        order_id : str
            (Required) (Required) The id of the order whose vaccines are being retrieved

        vaccine_id : str
            (Required) (Required) The id of the vaccine for which we are retrieving the details

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok43
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id1(
                person_id="personId",
                order_id="orderId",
                vaccine_id="vaccineId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id1(
                person_id, order_id, vaccine_id, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a patient's ordered vaccine record.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose vaccine record is being deleted

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine being deleted

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine being deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id(
                person_id="personId",
                order_id="orderId",
                vaccine_id="vaccineId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id(
                person_id, order_id, vaccine_id, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_component_lot_numbers(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok44:
        """
        Get a list of component lot numbers for the specified ordered vaccine ID.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered vaccine component lot numbers are being retrieved

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine whose component lot numbers are being retrieved

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine whose component lot numbers are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok44
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_component_lot_numbers(
                person_id="personId",
                order_id="orderId",
                vaccine_id="vaccineId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_component_lot_numbers(
            person_id, order_id, vaccine_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_suspected_diagnoses(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok45:
        """
        Get a list of diagnosis for the specified ordered vaccine ID.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose diagnosis are being retrieved

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine whose associated diagnosis are being retrieved

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine whose associated diagnosis are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok45
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_suspected_diagnoses(
                person_id="personId",
                order_id="orderId",
                vaccine_id="vaccineId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_suspected_diagnoses(
            person_id, order_id, vaccine_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok46:
        """
        Get a list of VIS histories that are documented as given to the patient for the specified ordered vaccine ID.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for who the vaccine VIS history information belongs to

        order_id : str
            (Required) (Required) The id of the immunization order which contains the vaccine for which the vaccine VIS history information was documented

        vaccine_id : str
            (Required) (Required) The id of the ordered vaccine for which the vaccine VIS history information was recorded

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok46
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
                person_id="personId",
                order_id="orderId",
                vaccine_id="vaccineId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories(
            person_id, order_id, vaccine_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
        self, person_id: str, order_id: str, vaccine_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok47:
        """
        Gets a list of wasted vaccines for the specified person Id, order Id and vaccine Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) Id of the person whose wasted vaccines are being retrieved

        order_id : str
            (Required) (Required) Id of the order associated with the wasted vaccines that are being retrieved

        vaccine_id : str
            (Required) (Required) Id of the ordered vaccine whose wasted vaccines are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok47
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
                person_id="personId",
                order_id="orderId",
                vaccine_id="vaccineId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines(
            person_id, order_id, vaccine_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines_wasted_vaccine_id(
        self,
        person_id: str,
        order_id: str,
        vaccine_id: str,
        wasted_vaccine_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok47:
        """
        Gets the wasted vaccine details for the specified person Id, order Id, vaccine Id and wasted vaccine Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) Id of the person whose wasted vaccine details are being retrieved

        order_id : str
            (Required) (Required) Id of the order associated with the wasted vaccine detials that are being retrieved

        vaccine_id : str
            (Required) (Required) Id of the ordered vaccine whose wasted vaccine detials are being retrieved

        wasted_vaccine_id : str
            (Required) (Required) Id of the wasted vaccine whose detials are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok47
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines_wasted_vaccine_id(
                person_id="personId",
                order_id="orderId",
                vaccine_id="vaccineId",
                wasted_vaccine_id="wastedVaccineId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines_wasted_vaccine_id(
            person_id, order_id, vaccine_id, wasted_vaccine_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_series_completions(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok49:
        """
        Gets a patient's immunization series completion records.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization series completion records are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok49
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_series_completions(
                person_id="personId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_series_completions(
            person_id, request_options=request_options
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_immunizations_series_completions(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a patient's immunization series completion record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization series completion record is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.post_base_url_persons_person_id_chart_immunizations_series_completions(
                person_id="personId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_immunizations_series_completions(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_immunizations_series_completions_series_id(
        self, person_id: str, series_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok49:
        """
        Gets a patient's immunization series completion information for the provided person Id and series completion Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization series completion information is being retrieved

        series_id : str
            (Required) (Required) The id of the series completion record whose details are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok49
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.base_url_persons_person_id_chart_immunizations_series_completions_series_id(
                person_id="personId",
                series_id="seriesId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_immunizations_series_completions_series_id(
            person_id, series_id, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_immunizations_series_completions_series_id(
        self,
        person_id: str,
        series_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's immunization series completion record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose immunization series completion record is being updated

        series_id : str
            (Required) (Required) The id of the series being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.immunizations.put_base_url_persons_person_id_chart_immunizations_series_completions_series_id(
                person_id="personId",
                series_id="seriesId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.put_base_url_persons_person_id_chart_immunizations_series_completions_series_id(
                person_id, series_id, request=request, request_options=request_options
            )
        )
        return _response.data
