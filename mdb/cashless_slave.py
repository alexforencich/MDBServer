import asyncio
import logging
from usb_handler import USBHandler, to_ascii


class CashlessSlave:
    _initialized: bool
    _logger: logging.Logger
    _usb_handler: USBHandler

    def __init__(self):
        self._initalized = False
        self._logger = logging.getLogger('.'.join((__name__,
                                                  self._class__.__name__)))

    async def initialize(self, usb_handler: USBHandler):
        self._usb_handler = usb_handler
        self._initalized = True

    async def run(self):
        assert self._initialized
