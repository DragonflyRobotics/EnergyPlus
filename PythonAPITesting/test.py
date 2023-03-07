import sys
from pyenergyplus.api import EnergyPlusAPI

def dummy_callback_function():
pass

api = EnergyPlusAPI()
api.runtime.callback_begin_new_environment(dummy_callback_function)
api.runtime.run_energyplus(sys.argv[1:])
api.runtime.clear_all_states()
api.runtime.callback_begin_new_environment(dummy_callback_function)
api.runtime.run_energyplus(sys.argv[1:])