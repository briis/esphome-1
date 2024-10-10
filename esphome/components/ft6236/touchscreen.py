import esphome.codegen as cg
from esphome.components import i2c
import esphome.config_validation as cv
from esphome.const import CONF_ID

DEPENDENCIES = ["i2c"]

ft6236_ns = cg.esphome_ns.namespace("ft6236")
FT6236Component = ft6236_ns.class_(
    "FT6236Component", cg.PollingComponent, i2c.I2CDevice
)

CONF_FT6236_ID = "ft6236_id"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(FT6236Component),
        }
    )
    .extend(cv.polling_component_schema("60ms"))
    .extend(i2c.i2c_device_schema(0x38))
)  # I2C Address is typically 0x38


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield i2c.register_i2c_device(var, config)
