from homeassistant.components.button import Button
from .coordinator import GenericBTCoordinator
from .entity import GenericBTEntity


class PairButton(GenericBTEntity, Button):
    _attr_name = None

    def __init__(self, coordinator: GenericBTCoordinator) -> None:
        """Initialize the Device."""
        super().__init__(coordinator)

    async def async_press(self) -> None:
        """Handle the button press."""
        await self._device.pair()