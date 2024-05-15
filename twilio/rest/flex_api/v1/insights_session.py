r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class InsightsSessionInstance(InstanceResource):
    """
    :ivar workspace_id: Unique ID to identify the user's workspace
    :ivar session_expiry: The session expiry date and time, given in ISO 8601 format.
    :ivar session_id: The unique ID for the session
    :ivar base_url: The base URL to fetch reports and dashboards
    :ivar url: The URL of this resource.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.workspace_id: Optional[str] = payload.get("workspace_id")
        self.session_expiry: Optional[str] = payload.get("session_expiry")
        self.session_id: Optional[str] = payload.get("session_id")
        self.base_url: Optional[str] = payload.get("base_url")
        self.url: Optional[str] = payload.get("url")

        self._context: Optional[InsightsSessionContext] = None

    @property
    def _proxy(self) -> "InsightsSessionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InsightsSessionContext for this InsightsSessionInstance
        """
        if self._context is None:
            self._context = InsightsSessionContext(
                self._version,
            )
        return self._context

    def create(
        self, authorization: Union[str, object] = values.unset
    ) -> "InsightsSessionInstance":
        """
        Create the InsightsSessionInstance

        :param authorization: The Authorization HTTP request header

        :returns: The created InsightsSessionInstance
        """
        return self._proxy.create(
            authorization=authorization,
        )

    async def create_async(
        self, authorization: Union[str, object] = values.unset
    ) -> "InsightsSessionInstance":
        """
        Asynchronous coroutine to create the InsightsSessionInstance

        :param authorization: The Authorization HTTP request header

        :returns: The created InsightsSessionInstance
        """
        return await self._proxy.create_async(
            authorization=authorization,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.FlexApi.V1.InsightsSessionInstance>"


class InsightsSessionContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the InsightsSessionContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/Insights/Session"

    def create(
        self, authorization: Union[str, object] = values.unset
    ) -> InsightsSessionInstance:
        """
        Create the InsightsSessionInstance

        :param authorization: The Authorization HTTP request header

        :returns: The created InsightsSessionInstance
        """
        data = values.of(
            {
                "Authorization": authorization,
            }
        )

        payload = self._version.create(method="POST", uri=self._uri, data=data)

        return InsightsSessionInstance(self._version, payload)

    async def create_async(
        self, authorization: Union[str, object] = values.unset
    ) -> InsightsSessionInstance:
        """
        Asynchronous coroutine to create the InsightsSessionInstance

        :param authorization: The Authorization HTTP request header

        :returns: The created InsightsSessionInstance
        """
        data = values.of(
            {
                "Authorization": authorization,
            }
        )

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data
        )

        return InsightsSessionInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.FlexApi.V1.InsightsSessionContext>"


class InsightsSessionList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InsightsSessionList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> InsightsSessionContext:
        """
        Constructs a InsightsSessionContext

        """
        return InsightsSessionContext(self._version)

    def __call__(self) -> InsightsSessionContext:
        """
        Constructs a InsightsSessionContext

        """
        return InsightsSessionContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsSessionList>"