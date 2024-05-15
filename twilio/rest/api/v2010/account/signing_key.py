r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SigningKeyInstance(InstanceResource):
    """
    :ivar sid:
    :ivar friendly_name:
    :ivar date_created:
    :ivar date_updated:
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )

        self._solution = {
            "account_sid": account_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[SigningKeyContext] = None

    @property
    def _proxy(self) -> "SigningKeyContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SigningKeyContext for this SigningKeyInstance
        """
        if self._context is None:
            self._context = SigningKeyContext(
                self._version,
                account_sid=self._solution["account_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the SigningKeyInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SigningKeyInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "SigningKeyInstance":
        """
        Fetch the SigningKeyInstance


        :returns: The fetched SigningKeyInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SigningKeyInstance":
        """
        Asynchronous coroutine to fetch the SigningKeyInstance


        :returns: The fetched SigningKeyInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, friendly_name: Union[str, object] = values.unset
    ) -> "SigningKeyInstance":
        """
        Update the SigningKeyInstance

        :param friendly_name:

        :returns: The updated SigningKeyInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
        )

    async def update_async(
        self, friendly_name: Union[str, object] = values.unset
    ) -> "SigningKeyInstance":
        """
        Asynchronous coroutine to update the SigningKeyInstance

        :param friendly_name:

        :returns: The updated SigningKeyInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.SigningKeyInstance {}>".format(context)


class SigningKeyContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the SigningKeyContext

        :param version: Version that contains the resource
        :param account_sid:
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/SigningKeys/{sid}.json".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the SigningKeyInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SigningKeyInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> SigningKeyInstance:
        """
        Fetch the SigningKeyInstance


        :returns: The fetched SigningKeyInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SigningKeyInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SigningKeyInstance:
        """
        Asynchronous coroutine to fetch the SigningKeyInstance


        :returns: The fetched SigningKeyInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SigningKeyInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self, friendly_name: Union[str, object] = values.unset
    ) -> SigningKeyInstance:
        """
        Update the SigningKeyInstance

        :param friendly_name:

        :returns: The updated SigningKeyInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SigningKeyInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, friendly_name: Union[str, object] = values.unset
    ) -> SigningKeyInstance:
        """
        Asynchronous coroutine to update the SigningKeyInstance

        :param friendly_name:

        :returns: The updated SigningKeyInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SigningKeyInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.SigningKeyContext {}>".format(context)


class SigningKeyPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> SigningKeyInstance:
        """
        Build an instance of SigningKeyInstance

        :param payload: Payload response from the API
        """
        return SigningKeyInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.SigningKeyPage>"


class SigningKeyList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the SigningKeyList

        :param version: Version that contains the resource
        :param account_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/SigningKeys.json".format(**self._solution)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SigningKeyInstance]:
        """
        Streams SigningKeyInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[SigningKeyInstance]:
        """
        Asynchronously streams SigningKeyInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SigningKeyInstance]:
        """
        Lists SigningKeyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SigningKeyInstance]:
        """
        Asynchronously lists SigningKeyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SigningKeyPage:
        """
        Retrieve a single page of SigningKeyInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SigningKeyInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SigningKeyPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SigningKeyPage:
        """
        Asynchronously retrieve a single page of SigningKeyInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SigningKeyInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SigningKeyPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> SigningKeyPage:
        """
        Retrieve a specific page of SigningKeyInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SigningKeyInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SigningKeyPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> SigningKeyPage:
        """
        Asynchronously retrieve a specific page of SigningKeyInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SigningKeyInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SigningKeyPage(self._version, response, self._solution)

    def get(self, sid: str) -> SigningKeyContext:
        """
        Constructs a SigningKeyContext

        :param sid:
        """
        return SigningKeyContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __call__(self, sid: str) -> SigningKeyContext:
        """
        Constructs a SigningKeyContext

        :param sid:
        """
        return SigningKeyContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.SigningKeyList>"
