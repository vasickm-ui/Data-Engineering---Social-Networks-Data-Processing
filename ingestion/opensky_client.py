import requests
import time
import logging
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


class OpenSkyClient:
    """
    This class represents client that calls OpenSky API.
    """
    
    BASE_URL = "https://opensky-network.org"
    
    def init(self, username : Optional[str] = None, password : Optional[str] = None):
        self.session = requests.Session()