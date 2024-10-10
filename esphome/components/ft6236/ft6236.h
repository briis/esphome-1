/*
This is a library for the FT6236 touchscreen controller by FocalTech.

The FT6236 and FT6236u work the same way.

A lot of this library is originally written by Limor Fried/Ladyada.

Because Adafruit invests time and resources providing this open source code,
please support Adafruit and open-source hardware by purchasing
products from Adafruit!

@section author Author
Written by Limor Fried/Ladyada for Adafruit Industries.

@section license License
MIT license, all text above must be included in any redistribution
*/
#pragma once

#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
namespace ft6236 {

#define FT6236_ADDR 0x38            // I2C address
#define FT6236_REG_NUMTOUCHES 0x02  // Number of touch points

#define FT6236_REG_VENDID 0xA8  // Vendor ID register
#define FT6236_VENDID 0x11      // Expected Vendor ID

#define FT6236_REG_CHIPID 0xA3  // Chip ID register
#define FT6236_CHIPID 0x36      // FT6236 Chip ID
#define FT6236U_CHIPID 0x64     // FT6236U Chip ID
#define FT6206_CHIPID 0x06      // FT6206 Chip ID

class TS_Point {
 public:
  TS_Point(void);
  TS_Point(int16_t x, int16_t y, int16_t z);

  bool operator==(TS_Point);
  bool operator!=(TS_Point);

  int16_t x;
  int16_t y;
  int16_t z;
};

class FT6236Touchscreen : public Component, public i2c::I2CDevice {
 public:
  FT6236Touchscreen(void);

  void setup() override;
  void loop() override;
  void dump_config() override;

  uint8_t touched(void);
  TS_Point getPoint(uint8_t n = 0);

 protected:
  void writeRegister8(uint8_t reg, uint8_t val);
  uint8_t readRegister8(uint8_t reg);
  void readData(void);

  uint8_t touches;
  uint16_t touchX[2], touchY[2], touchID[2];
};

}  // namespace ft6236
}  // namespace esphome
