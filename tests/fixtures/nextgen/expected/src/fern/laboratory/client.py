

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok41 import Ok41
from ..types.ok53 import Ok53
from ..types.ok54 import Ok54
from ..types.ok56 import Ok56
from ..types.ok57 import Ok57
from ..types.ok58 import Ok58
from ..types.ok59 import Ok59
from ..types.ok60 import Ok60
from ..types.ok61 import Ok61
from ..types.ok63 import Ok63
from ..types.ok64 import Ok64
from ..types.ok65 import Ok65
from ..types.ok66 import Ok66
from .raw_client import AsyncRawLaboratoryClient, RawLaboratoryClient


OMIT = typing.cast(typing.Any, ...)


class LaboratoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLaboratoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLaboratoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLaboratoryClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_encounters_encounter_id_lab_orders(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok53:
        """
        Adds a new lab order for the given person id and encounter id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient to add the new lab order for.

        encounter_id : str
            (Required) (Required) The id of the encounter to add the new lab order to.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok53
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_encounters_encounter_id_lab_orders(
            person_id="personId",
            encounter_id="encounterId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_lab_orders(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders(
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
    ) -> Ok54:
        """
        Gets a list of lab order summaries for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose lab orders are being retrieved

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
        Ok54
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_orders(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders(
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

    def base_url_persons_person_id_chart_lab_orders_order_id1(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok53:
        """
        Gets the lab order details for the given person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose lab orders are being retrieved

        order_id : str
            (Required) (Required) The id of the lab order being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok53
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id1(
            person_id="personId",
            order_id="orderId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id1(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_lab_orders_order_id(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update the specified lab order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is to be updated.

        order_id : str
            (Required) (Required) The id of the order that is to be updated.

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
        client.laboratory.put_base_url_persons_person_id_chart_lab_orders_order_id(
            person_id="personId",
            order_id="orderId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_lab_orders_order_id(
            person_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is to be deleted.

        order_id : str
            (Required) (Required) The id of the order that is to be deleted.

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
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id(
            person_id="personId",
            order_id="orderId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_insurances(
        self,
        person_id: str,
        order_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok56:
        """
        Get a list of insurances that are associated with the specified person Id and order Id after apply additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom the order insurances are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order for which the insurances are being retrieved.

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
        Ok56
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_insurances(
            person_id="personId",
            order_id="orderId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_insurances(
            person_id,
            order_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_schedule(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok57:
        """
        Get the schedule details for the specified person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order schedule is being retrieved.

        order_id : str
            (Required) (Required) The id of the order whose schedule is being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok57
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_schedule(
            person_id="personId",
            order_id="orderId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_schedule(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    def post_base_url_persons_person_id_chart_lab_orders_order_id_schedule(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Set the schedule for the specified person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is being scheduled.

        order_id : str
            (Required) (Required) The id of the order that is being scheduled.

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
        client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_schedule(
            person_id="personId",
            order_id="orderId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_lab_orders_order_id_schedule(
            person_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_send(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a record to the interface queue with the provided order Id and lab interface agent information that is determined based on the order's lab Id. This route does not control when the order will be processed and sent out to the lab which is controlled by the interface.

        Parameters
        ----------
        person_id : str
            (Required) (Required) Id of the person whose order is being sent to interface

        order_id : str
            (Required) (Required) Id of the lab order which is being sent to interface

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
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_send(
            person_id="personId",
            order_id="orderId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_send(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_tests(
        self,
        person_id: str,
        order_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok58:
        """
        Gets a list of ordered test summaries for the specified person id and order id after apply additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose ordered tests are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order for which the ordered tests are being retrieved.

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
        Ok58
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests(
            person_id="personId",
            order_id="orderId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests(
            person_id,
            order_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def post_base_url_persons_person_id_chart_lab_orders_order_id_tests(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Add a lab test to the specified order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person where the new lab test will be added to the order.

        order_id : str
            (Required) (Required) The id of the order where the new lab test will be added.

        request : typing.Sequence[typing.Any]

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
        client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tests(
            person_id="personId",
            order_id="orderId",
            request=[],
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_lab_orders_order_id_tests(
            person_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id1(
        self, person_id: str, order_id: str, test_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok59:
        """
        Gets the ordered test for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient to retrieve the ordered test for.

        order_id : str
            (Required) (Required) The id of the lab order which contains the test that were ordered.

        test_id : str
            (Required) (Required) The id of the ordered test being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok59
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id1(
            person_id="personId",
            order_id="orderId",
            test_id="testId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id1(
            person_id, order_id, test_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates the specified order test for the specified person and order.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered test is to be updated.

        order_id : str
            (Required) (Required) The id of the order whose ordered test is to be updated.

        test_id : str
            (Required) (Required) The id of the ordered test that is to be updated.

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
        client.laboratory.put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
            person_id="personId",
            order_id="orderId",
            test_id="testId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
            person_id, order_id, test_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
        self, person_id: str, order_id: str, test_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes the specified ordered test for the person and order.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered test will be deleted.

        order_id : str
            (Required) (Required) The id of the order whose ordered test will be deleted.

        test_id : str
            (Required) (Required) The id of the order test to be deleted.

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
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
            person_id="personId",
            order_id="orderId",
            test_id="testId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
            person_id, order_id, test_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok60:
        """
        Gets a list of order entry answers for the specified person id, order id and test id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answers are being retrieved.

        order_id : str
            (Required) (Required) The id of the order whose order entry answers are being retrieved.

        test_id : str
            (Required) (Required) The id of the ordered test whose order entry answers are being retrieved.

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
        Ok60
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
            person_id="personId",
            order_id="orderId",
            test_id="testId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = (
            self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
                person_id,
                order_id,
                test_id,
                top=top,
                filter=filter,
                orderby=orderby,
                skip=skip,
                inlinecount=inlinecount,
                count=count,
                request_options=request_options,
            )
        )
        return _response.data

    def post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds an answer to an order entry question for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) This id of the person whose order entry answer is to be added.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is to be added.

        test_id : str
            (Required) (Required) The id of the ordered test whose order entry answer is to be added.

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
        client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
            person_id="personId",
            order_id="orderId",
            test_id="testId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
            person_id, order_id, test_id, request=request, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        answer_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates the specifed order entry answer for the specified person id, order id, test id and answer id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answer is being updated.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is being updated.

        test_id : str
            (Required) (Required) The id of the ordered test id whose order entry answer is being udpated.

        answer_id : str
            (Required) (Required) The id of the order entry answer to update.

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
        client.laboratory.put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
            person_id="personId",
            order_id="orderId",
            test_id="testId",
            answer_id="answerId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
            person_id, order_id, test_id, answer_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        answer_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified order entry answer for the specified person id, order id and ordered test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answer is being deleted.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is being deleted.

        test_id : str
            (Required) (Required) The id of the ordered test id whose order entry answer is being deleted.

        answer_id : str
            (Required) (Required)

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
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
            person_id="personId",
            order_id="orderId",
            test_id="testId",
            answer_id="answerId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
            person_id, order_id, test_id, answer_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok61:
        """
        Get a list of suspected diagnosis for the specified ordered test id after applying addition OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose suspected diagnoses are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order which contains the test whose suspected diagnosis are beign retrieved.

        test_id : str
            (Required) (Required) The id of the ordered test whose suspected diagnosis are being retrieved.

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
        Ok61
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
            person_id="personId",
            order_id="orderId",
            test_id="testId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = (
            self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
                person_id,
                order_id,
                test_id,
                top=top,
                filter=filter,
                orderby=orderby,
                skip=skip,
                inlinecount=inlinecount,
                count=count,
                request_options=request_options,
            )
        )
        return _response.data

    def post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a suspected diagnosis for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the suspected diagnosis will be added.

        order_id : str
            (Required) (Required) The id of the order for which the suspected diagnosis will be added.

        test_id : str
            (Required) (Required) The id of the ordered test for which the suspected diagnosis will be added.

        request : typing.Sequence[typing.Any]

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
        client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
            person_id="personId",
            order_id="orderId",
            test_id="testId",
            request=[],
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
            person_id, order_id, test_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_diagnosis_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        diagnosis_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified suspected diagnosis for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose suspected diagnosis is to be deleted.

        order_id : str
            (Required) (Required) The id of the order whose suspected diagnosis is to be deleted.

        test_id : str
            (Required) (Required) The id of the ordered test whose suspected diagnosis is to be deleted.

        diagnosis_id : str
            (Required) (Required) The id of the suspected diagnosis to be deleted.

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
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_diagnosis_id(
            person_id="personId",
            order_id="orderId",
            test_id="testId",
            diagnosis_id="diagnosisId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_diagnosis_id(
            person_id, order_id, test_id, diagnosis_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
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
        client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
            person_id="personId",
            order_id="orderId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    def post_base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a tracking comment for the given person id and lab order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to.

        order_id : str
            (Required) (Required) The id of the lab order which the tracking comment will be added for.

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
        client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
            person_id="personId",
            order_id="orderId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
            person_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_panels(
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
    ) -> Ok63:
        """
        Gets a list of observation panels for the specified person id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom the observation panels are being retrieved.

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
        Ok63
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_panels(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_panels(
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

    def post_base_url_persons_person_id_chart_lab_panels(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds an observation panel the specified person.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person to add the observation panel for.

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
        client.laboratory.post_base_url_persons_person_id_chart_lab_panels(
            person_id="personId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_lab_panels(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_panels_panel_id1(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok64:
        """
        Gets an observation panel for the specified person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is being retrieved.

        panel_id : str
            (Required) (Required) The id of the observation panel being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok64
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id1(
            person_id="personId",
            panel_id="panelId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_panels_panel_id1(
            person_id, panel_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_lab_panels_panel_id(
        self,
        person_id: str,
        panel_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update the specified observation panel for the specified personId.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is to be updated.

        panel_id : str
            (Required) (Required) The id of the panel to be updated.

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
        client.laboratory.put_base_url_persons_person_id_chart_lab_panels_panel_id(
            person_id="personId",
            panel_id="panelId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_lab_panels_panel_id(
            person_id, panel_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_panels_panel_id(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified observation panel for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is to be deleted.

        panel_id : str
            (Required) (Required) The id of the observation panel to be deleted.

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
        client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id(
            person_id="personId",
            panel_id="panelId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_panels_panel_id(
            person_id, panel_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_panels_panel_id_results(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok65:
        """
        Gets a list of observation results for the specified person id and observation panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation results are being retrieved.

        panel_id : str
            (Required) (Required) The id of the observation panel for whose observation results are being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok65
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id_results(
            person_id="personId",
            panel_id="panelId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_panels_panel_id_results(
            person_id, panel_id, request_options=request_options
        )
        return _response.data

    def post_base_url_persons_person_id_chart_lab_panels_panel_id_results(
        self,
        person_id: str,
        panel_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds observation results for the specified person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person to add observation results for.

        panel_id : str
            (Required) (Required) The id of the observation panel to add results to.

        request : typing.Sequence[typing.Any]

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
        client.laboratory.post_base_url_persons_person_id_chart_lab_panels_panel_id_results(
            person_id="personId",
            panel_id="panelId",
            request=[],
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_lab_panels_panel_id_results(
            person_id, panel_id, request=request, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
        self,
        person_id: str,
        panel_id: str,
        sequence_number: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update the specified observation result for the specifed person id, panel id and sequenceNumber.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of person whose observation result is to be updated.

        panel_id : str
            (Required) (Required) The id of the panel whose observation result is to be updated.

        sequence_number : str
            (Required) (Required) The observation result sequence number that is to be updated.

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
        client.laboratory.put_base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
            person_id="personId",
            panel_id="panelId",
            sequence_number="sequenceNumber",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
            person_id, panel_id, sequence_number, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
        self,
        person_id: str,
        panel_id: str,
        sequence_number: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified observation result for the specifed person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of person whose observation result is to be deleted.

        panel_id : str
            (Required) (Required) The id of the panel whose observation result is to be deleted.

        sequence_number : str
            (Required) (Required) The observation result sequence number that is to be deleted.

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
        client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
            person_id="personId",
            panel_id="panelId",
            sequence_number="sequenceNumber",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
            person_id, panel_id, sequence_number, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_lab_results(
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
    ) -> Ok66:
        """
        Gets a list of observation results for the specified person id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation results are being retrieved.

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
        Ok66
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.laboratory.base_url_persons_person_id_chart_lab_results(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_lab_results(
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


class AsyncLaboratoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLaboratoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLaboratoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLaboratoryClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_encounters_encounter_id_lab_orders(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok53:
        """
        Adds a new lab order for the given person id and encounter id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient to add the new lab order for.

        encounter_id : str
            (Required) (Required) The id of the encounter to add the new lab order to.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok53
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_encounters_encounter_id_lab_orders(
                person_id="personId",
                encounter_id="encounterId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_lab_orders(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders(
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
    ) -> Ok54:
        """
        Gets a list of lab order summaries for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose lab orders are being retrieved

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
        Ok54
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_orders(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders(
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

    async def base_url_persons_person_id_chart_lab_orders_order_id1(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok53:
        """
        Gets the lab order details for the given person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose lab orders are being retrieved

        order_id : str
            (Required) (Required) The id of the lab order being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok53
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id1(
                person_id="personId",
                order_id="orderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id1(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_lab_orders_order_id(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update the specified lab order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is to be updated.

        order_id : str
            (Required) (Required) The id of the order that is to be updated.

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
            await client.laboratory.put_base_url_persons_person_id_chart_lab_orders_order_id(
                person_id="personId",
                order_id="orderId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_lab_orders_order_id(
            person_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is to be deleted.

        order_id : str
            (Required) (Required) The id of the order that is to be deleted.

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
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id(
                person_id="personId",
                order_id="orderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_insurances(
        self,
        person_id: str,
        order_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok56:
        """
        Get a list of insurances that are associated with the specified person Id and order Id after apply additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom the order insurances are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order for which the insurances are being retrieved.

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
        Ok56
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_insurances(
                person_id="personId",
                order_id="orderId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_insurances(
            person_id,
            order_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_schedule(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok57:
        """
        Get the schedule details for the specified person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order schedule is being retrieved.

        order_id : str
            (Required) (Required) The id of the order whose schedule is being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok57
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_schedule(
                person_id="personId",
                order_id="orderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_schedule(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_lab_orders_order_id_schedule(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Set the schedule for the specified person id and order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order is being scheduled.

        order_id : str
            (Required) (Required) The id of the order that is being scheduled.

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
            await client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_schedule(
                person_id="personId",
                order_id="orderId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_lab_orders_order_id_schedule(
            person_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_send(
        self, person_id: str, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a record to the interface queue with the provided order Id and lab interface agent information that is determined based on the order's lab Id. This route does not control when the order will be processed and sent out to the lab which is controlled by the interface.

        Parameters
        ----------
        person_id : str
            (Required) (Required) Id of the person whose order is being sent to interface

        order_id : str
            (Required) (Required) Id of the lab order which is being sent to interface

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
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_send(
                person_id="personId",
                order_id="orderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_send(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests(
        self,
        person_id: str,
        order_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok58:
        """
        Gets a list of ordered test summaries for the specified person id and order id after apply additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose ordered tests are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order for which the ordered tests are being retrieved.

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
        Ok58
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests(
                person_id="personId",
                order_id="orderId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests(
            person_id,
            order_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_lab_orders_order_id_tests(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Add a lab test to the specified order id for the person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person where the new lab test will be added to the order.

        order_id : str
            (Required) (Required) The id of the order where the new lab test will be added.

        request : typing.Sequence[typing.Any]

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
            await client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tests(
                person_id="personId",
                order_id="orderId",
                request=[],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_lab_orders_order_id_tests(
            person_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id1(
        self, person_id: str, order_id: str, test_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok59:
        """
        Gets the ordered test for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient to retrieve the ordered test for.

        order_id : str
            (Required) (Required) The id of the lab order which contains the test that were ordered.

        test_id : str
            (Required) (Required) The id of the ordered test being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok59
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id1(
                person_id="personId",
                order_id="orderId",
                test_id="testId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id1(
            person_id, order_id, test_id, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates the specified order test for the specified person and order.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered test is to be updated.

        order_id : str
            (Required) (Required) The id of the order whose ordered test is to be updated.

        test_id : str
            (Required) (Required) The id of the ordered test that is to be updated.

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
            await client.laboratory.put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
                person_id="personId",
                order_id="orderId",
                test_id="testId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
            person_id, order_id, test_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
        self, person_id: str, order_id: str, test_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes the specified ordered test for the person and order.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ordered test will be deleted.

        order_id : str
            (Required) (Required) The id of the order whose ordered test will be deleted.

        test_id : str
            (Required) (Required) The id of the order test to be deleted.

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
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
                person_id="personId",
                order_id="orderId",
                test_id="testId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id(
            person_id, order_id, test_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok60:
        """
        Gets a list of order entry answers for the specified person id, order id and test id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answers are being retrieved.

        order_id : str
            (Required) (Required) The id of the order whose order entry answers are being retrieved.

        test_id : str
            (Required) (Required) The id of the ordered test whose order entry answers are being retrieved.

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
        Ok60
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
                person_id="personId",
                order_id="orderId",
                test_id="testId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
            person_id,
            order_id,
            test_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds an answer to an order entry question for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) This id of the person whose order entry answer is to be added.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is to be added.

        test_id : str
            (Required) (Required) The id of the ordered test whose order entry answer is to be added.

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
            await client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
                person_id="personId",
                order_id="orderId",
                test_id="testId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers(
            person_id, order_id, test_id, request=request, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        answer_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates the specifed order entry answer for the specified person id, order id, test id and answer id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answer is being updated.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is being updated.

        test_id : str
            (Required) (Required) The id of the ordered test id whose order entry answer is being udpated.

        answer_id : str
            (Required) (Required) The id of the order entry answer to update.

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
            await client.laboratory.put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
                person_id="personId",
                order_id="orderId",
                test_id="testId",
                answer_id="answerId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
            person_id, order_id, test_id, answer_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        answer_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified order entry answer for the specified person id, order id and ordered test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose order entry answer is being deleted.

        order_id : str
            (Required) (Required) The id of the order whose order entry answer is being deleted.

        test_id : str
            (Required) (Required) The id of the ordered test id whose order entry answer is being deleted.

        answer_id : str
            (Required) (Required)

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
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
                person_id="personId",
                order_id="orderId",
                test_id="testId",
                answer_id="answerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id(
            person_id, order_id, test_id, answer_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok61:
        """
        Get a list of suspected diagnosis for the specified ordered test id after applying addition OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose suspected diagnoses are being retrieved.

        order_id : str
            (Required) (Required) The id of the lab order which contains the test whose suspected diagnosis are beign retrieved.

        test_id : str
            (Required) (Required) The id of the ordered test whose suspected diagnosis are being retrieved.

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
        Ok61
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
                person_id="personId",
                order_id="orderId",
                test_id="testId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
            person_id,
            order_id,
            test_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a suspected diagnosis for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the suspected diagnosis will be added.

        order_id : str
            (Required) (Required) The id of the order for which the suspected diagnosis will be added.

        test_id : str
            (Required) (Required) The id of the ordered test for which the suspected diagnosis will be added.

        request : typing.Sequence[typing.Any]

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
            await client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
                person_id="personId",
                order_id="orderId",
                test_id="testId",
                request=[],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses(
            person_id, order_id, test_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_diagnosis_id(
        self,
        person_id: str,
        order_id: str,
        test_id: str,
        diagnosis_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified suspected diagnosis for the specified person id, order id and test id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose suspected diagnosis is to be deleted.

        order_id : str
            (Required) (Required) The id of the order whose suspected diagnosis is to be deleted.

        test_id : str
            (Required) (Required) The id of the ordered test whose suspected diagnosis is to be deleted.

        diagnosis_id : str
            (Required) (Required) The id of the suspected diagnosis to be deleted.

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
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_diagnosis_id(
                person_id="personId",
                order_id="orderId",
                test_id="testId",
                diagnosis_id="diagnosisId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_diagnosis_id(
            person_id, order_id, test_id, diagnosis_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
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
            await client.laboratory.base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
                person_id="personId",
                order_id="orderId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
            person_id, order_id, request_options=request_options
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
        self,
        person_id: str,
        order_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a tracking comment for the given person id and lab order id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person who the order belongs to.

        order_id : str
            (Required) (Required) The id of the lab order which the tracking comment will be added for.

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
            await client.laboratory.post_base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
                person_id="personId",
                order_id="orderId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments(
            person_id, order_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_panels(
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
    ) -> Ok63:
        """
        Gets a list of observation panels for the specified person id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom the observation panels are being retrieved.

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
        Ok63
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_panels(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_panels(
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

    async def post_base_url_persons_person_id_chart_lab_panels(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds an observation panel the specified person.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person to add the observation panel for.

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
            await client.laboratory.post_base_url_persons_person_id_chart_lab_panels(
                person_id="personId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_lab_panels(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_panels_panel_id1(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok64:
        """
        Gets an observation panel for the specified person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is being retrieved.

        panel_id : str
            (Required) (Required) The id of the observation panel being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok64
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id1(
                person_id="personId",
                panel_id="panelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_panels_panel_id1(
            person_id, panel_id, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_lab_panels_panel_id(
        self,
        person_id: str,
        panel_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update the specified observation panel for the specified personId.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is to be updated.

        panel_id : str
            (Required) (Required) The id of the panel to be updated.

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
            await client.laboratory.put_base_url_persons_person_id_chart_lab_panels_panel_id(
                person_id="personId",
                panel_id="panelId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_lab_panels_panel_id(
            person_id, panel_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_panels_panel_id(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified observation panel for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation panel is to be deleted.

        panel_id : str
            (Required) (Required) The id of the observation panel to be deleted.

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
            await client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id(
                person_id="personId",
                panel_id="panelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_panels_panel_id(
            person_id, panel_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_panels_panel_id_results(
        self, person_id: str, panel_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok65:
        """
        Gets a list of observation results for the specified person id and observation panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation results are being retrieved.

        panel_id : str
            (Required) (Required) The id of the observation panel for whose observation results are being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok65
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id_results(
                person_id="personId",
                panel_id="panelId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_panels_panel_id_results(
            person_id, panel_id, request_options=request_options
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_lab_panels_panel_id_results(
        self,
        person_id: str,
        panel_id: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds observation results for the specified person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person to add observation results for.

        panel_id : str
            (Required) (Required) The id of the observation panel to add results to.

        request : typing.Sequence[typing.Any]

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
            await client.laboratory.post_base_url_persons_person_id_chart_lab_panels_panel_id_results(
                person_id="personId",
                panel_id="panelId",
                request=[],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_lab_panels_panel_id_results(
            person_id, panel_id, request=request, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
        self,
        person_id: str,
        panel_id: str,
        sequence_number: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update the specified observation result for the specifed person id, panel id and sequenceNumber.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of person whose observation result is to be updated.

        panel_id : str
            (Required) (Required) The id of the panel whose observation result is to be updated.

        sequence_number : str
            (Required) (Required) The observation result sequence number that is to be updated.

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
            await client.laboratory.put_base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
                person_id="personId",
                panel_id="panelId",
                sequence_number="sequenceNumber",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.put_base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
                person_id, panel_id, sequence_number, request=request, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
        self,
        person_id: str,
        panel_id: str,
        sequence_number: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified observation result for the specifed person id and panel id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of person whose observation result is to be deleted.

        panel_id : str
            (Required) (Required) The id of the panel whose observation result is to be deleted.

        sequence_number : str
            (Required) (Required) The observation result sequence number that is to be deleted.

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
            await client.laboratory.base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
                person_id="personId",
                panel_id="panelId",
                sequence_number="sequenceNumber",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number(
            person_id, panel_id, sequence_number, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_lab_results(
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
    ) -> Ok66:
        """
        Gets a list of observation results for the specified person id after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose observation results are being retrieved.

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
        Ok66
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.laboratory.base_url_persons_person_id_chart_lab_results(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_lab_results(
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
