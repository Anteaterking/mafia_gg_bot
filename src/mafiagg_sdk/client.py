from dataclasses import dataclass
from typing import Dict, Optional, Type, TypeVar

import requests
from mafiagg_sdk.models.base import Base
from mafiagg_sdk.models.rooms_response import RoomsResponse
from mafiagg_sdk.models.user_session_response import UserSessionResponse

B = TypeVar("B", Type[Base], Base)


def _deserialize_response(response: Dict, cls: B) -> B:
    return cls.from_json(response)


@dataclass
class Client:
    host: str = "mafia.gg"
    __cookie: Optional[str] = None
    _username: Optional[str] = None

    @property
    def base_url(self) -> str:
        return f"https://{self.host}/api"

    @property
    def username(self) -> str:
        return self._username

    def _headers(self) -> Dict:
        if self.__cookie:
            return {
                "Cookie": self.__cookie,
            }
        else:
            return {}

    def _get(self, url: str, **kwargs) -> requests.Response:
        return requests.get(
            url=f"{self.base_url}{url}",
            headers=self._headers(),
            **kwargs,
        )

    def _post(self, url: str, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        if json is None:
            json = {}
        return requests.post(
            url=f"{self.base_url}{url}",
            headers=self._headers(),
            json=json,
            **kwargs,
        )

    def _put(self, url: str, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        if json is None:
            json = {}
        return requests.put(
            url=f"{self.base_url}{url}",
            headers=self._headers(),
            json=json,
            **kwargs,
        )

    def _delete(self, url: str, **kwargs) -> requests.Response:
        return requests.delete(
            url=f"{self.base_url}{url}",
            headers=self._headers(),
            **kwargs,
        )

    def login(self, login: str, password: str) -> UserSessionResponse:
        url = "/user-session"
        data = {
            login: login,
            password: password,
        }
        raw_response = self._post(
            url=url,
            json=data,
        )
        resp: UserSessionResponse = _deserialize_response(raw_response.json(), UserSessionResponse)
        self.__cookie = raw_response.headers.get("Set-Cookie").split(";")[0]
        self._username = resp.username
        return resp

    def logout(self) -> None:
        self.__cookie = None
        self._username = None

    def list_rooms(self) -> RoomsResponse:
        url = "/rooms"
        raw_response = self._get(
            url=url,
        )
        return _deserialize_response(raw_response.json(), RoomsResponse)
