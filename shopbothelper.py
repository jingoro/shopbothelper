import sys
import time

spindle_current = 490
vacuum_table_current = 1234
air_quality_sensor = 2345
waste_sensor = 3453
dust_collector_power = True
air_quality_bad = False
waste_bin_full = True
spindle_warmed_up = True

diagnostics_template = """
  +-------< spindle_current = {}mv
  | +-----< vacuum_table_current = {}mv
  | | +---< air_quality_sensor = {}mv
  | | | +-< waste_sensor = {}mv
  | | | |
+-+-+-+-+-+
|  RasPi  |
+-+-+-+-+-+
  | | | |
  | | | +-> dust_collector_power = {}
  | | +---> air_quality_bad = {}
  | +-----> waste_bin_full = {}
  +-------> spindle_warmed_up = {}
"""

def multiply(a, b):
    return a*b

def clear_screen():
    sys.stdout.write("\x1b[2J\x1b[H")

def update_inputs():
    global spindle_current
    spindle_current += 1
    
def event_loop():
    while True:
        update_inputs()
        update_dustcollector_power()

        clear_screen()
        display_diagnostics()
        time.sleep(1.0) # pause for one second

def update_dustcollector_power():
    global dust_collector_power 
    if spindle_current > 500:
        dust_collector_power = True
    else: 
        dust_collector_power = False
        

def display_diagnostics(): 
    print diagnostics_template.format(
        spindle_current,
        vacuum_table_current,
        air_quality_sensor,
        waste_sensor,
        dust_collector_power,
        air_quality_bad,
        waste_bin_full,
        spindle_warmed_up,
    )

if __name__ == '__main__':
    event_loop()