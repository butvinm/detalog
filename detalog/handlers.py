from logging import Handler, LogRecord
from typing import Optional

from requests import Session
import requests


LEVEL_TO_ICON = {
    "CRITICAL": ":fire:",
    "ERROR": ":x:",
    "WARNING": ":warning:",
    "INFO": ":information_source:",
    "DEBUG": ":bug:",
    "NOTSET": ":question:"
}


class PingBackHandler(Handler):
    def __init__(
        self,
        app_url: str,
        api_key: str,
        project: str = "default",
        channel: str = "default",
    ):
        super().__init__()
        self.app_url = app_url
        if self.app_url.endswith("/"):
            self.app_url = self.app_url[:-1]

        self.project = project
        self.channel = channel
        self.api_key = api_key

        self._session = Session()
        self._session.headers.update({"X-API-KEY": self.api_key, "Content-Type": "application/json"})

    def get_destination(self, record: LogRecord) -> tuple[str, str]:
        project: Optional[str] = record.__dict__.get("project", self.project)
        channel: Optional[str] = record.__dict__.get("channel", self.channel)
        return project or self.project, channel or self.channel

    def emit(self, record: LogRecord) -> None:
        project, channel = self.get_destination(record)

        data = {
            "project": project,
            "channel": channel,
            "name": record.levelname.lower(),
            "title": f"{record.levelname} in {record.name}",
            "description": record.msg,
            "icon": LEVEL_TO_ICON[record.levelname],
        }
        events_url = f"{self.app_url}/api/v1/events"

        self._session.post(events_url, json=data)
