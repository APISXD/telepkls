r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.insights.v1.call.annotation import AnnotationList
from twilio.rest.insights.v1.call.call_summary import CallSummaryList
from twilio.rest.insights.v1.call.event import EventList
from twilio.rest.insights.v1.call.metric import MetricList


class CallInstance(InstanceResource):
    """
    :ivar sid:
    :ivar url:
    :ivar links:
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[CallContext] = None

    @property
    def _proxy(self) -> "CallContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CallContext for this CallInstance
        """
        if self._context is None:
            self._context = CallContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "CallInstance":
        """
        Fetch the CallInstance


        :returns: The fetched CallInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CallInstance":
        """
        Asynchronous coroutine to fetch the CallInstance


        :returns: The fetched CallInstance
        """
        return await self._proxy.fetch_async()

    @property
    def annotation(self) -> AnnotationList:
        """
        Access the annotation
        """
        return self._proxy.annotation

    @property
    def summary(self) -> CallSummaryList:
        """
        Access the summary
        """
        return self._proxy.summary

    @property
    def events(self) -> EventList:
        """
        Access the events
        """
        return self._proxy.events

    @property
    def metrics(self) -> MetricList:
        """
        Access the metrics
        """
        return self._proxy.metrics

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.CallInstance {}>".format(context)


class CallContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the CallContext

        :param version: Version that contains the resource
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Voice/{sid}".format(**self._solution)

        self._annotation: Optional[AnnotationList] = None
        self._summary: Optional[CallSummaryList] = None
        self._events: Optional[EventList] = None
        self._metrics: Optional[MetricList] = None

    def fetch(self) -> CallInstance:
        """
        Fetch the CallInstance


        :returns: The fetched CallInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CallInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CallInstance:
        """
        Asynchronous coroutine to fetch the CallInstance


        :returns: The fetched CallInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CallInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    @property
    def annotation(self) -> AnnotationList:
        """
        Access the annotation
        """
        if self._annotation is None:
            self._annotation = AnnotationList(
                self._version,
                self._solution["sid"],
            )
        return self._annotation

    @property
    def summary(self) -> CallSummaryList:
        """
        Access the summary
        """
        if self._summary is None:
            self._summary = CallSummaryList(
                self._version,
                self._solution["sid"],
            )
        return self._summary

    @property
    def events(self) -> EventList:
        """
        Access the events
        """
        if self._events is None:
            self._events = EventList(
                self._version,
                self._solution["sid"],
            )
        return self._events

    @property
    def metrics(self) -> MetricList:
        """
        Access the metrics
        """
        if self._metrics is None:
            self._metrics = MetricList(
                self._version,
                self._solution["sid"],
            )
        return self._metrics

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.CallContext {}>".format(context)


class CallList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CallList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, sid: str) -> CallContext:
        """
        Constructs a CallContext

        :param sid:
        """
        return CallContext(self._version, sid=sid)

    def __call__(self, sid: str) -> CallContext:
        """
        Constructs a CallContext

        :param sid:
        """
        return CallContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.CallList>"