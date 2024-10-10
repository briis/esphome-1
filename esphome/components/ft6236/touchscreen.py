import esphome.codegen as cg
import esphome.config_validation as cv

from esphome import pins
from esphome.components import i2c, touchscreen
from esphome.const import CONF_ID, CONF_INTERRUPT_PIN, CONF_RESET_PIN, CONF_THRESHOLD

# Namespace for the FT6236 component
ft6236_ns = cg.esphome_ns.namespace("ft6236")
FT6236Touchscreen = ft6236_ns.class_(
    "FT6236Touchscreen",
    touchscreen.Touchscreen,
    i2c.I2CDevice,
)

# Configuration parameters
CONF_FT6236_ID = "ft6236_id"

# Defining the configuration schema
CONFIG_SCHEMA = touchscreen.TOUCHSCREEN_SCHEMA.extend(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(FT6236Touchscreen),
            cv.Optional(CONF_INTERRUPT_PIN): cv.All(
                pins.internal_gpio_input_pin_schema
            ),
            cv.Optional(CONF_RESET_PIN): pins.gpio_output_pin_schema,
            cv.Optional(CONF_THRESHOLD): cv.uint8_t,
        }
    ).extend(i2c.i2c_device_schema(0x38))  # Default I2C address for FT6236
)

# Asynchronous code generation for the FT6236 component
async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await touchscreen.register_touchscreen(var, config)
    await i2c.register_i2c_device(var, config)

    if interrupt_pin_config := config.get(CONF_INTERRUPT_PIN):
        interrupt_pin = await cg.gpio_pin_expression(interrupt_pin_config)
        cg.add(var.set_interrupt_pin(interrupt_pin))
    if reset_pin_config := config.get(CONF_RESET_PIN):
        reset_pin = await cg.gpio_pin_expression(reset_pin_config)
        cg.add(var.set_reset_pin(reset_pin))

    if CONF_THRESHOLD in config:
        cg.add(var.set_threshold(config[CONF_THRESHOLD]))
