from tkinter import *
import cmath
import math
#import can
import time
#from gpiozero import LED
import random
import threading

# ratio for controling input values
sampling_ratio = 60


win = Tk()
win.attributes('-fullscreen', True)
win.geometry(f'{win.winfo_screenwidth()}x{win.winfo_screenheight()}')
win.bind('<Escape>', lambda event: win.destroy())
win.configure(bg = 'black')

  
"""""""""""""""""""""""Canvas"""""""""""""""""""""""

canvas_x_size = win.winfo_screenwidth() # canvas plotis
canvas_y_size = win.winfo_screenheight() #canvas aukštis
canvas_x_center = canvas_x_size/2 # canvas centras pagal x
canvas_y_center = canvas_y_size/2 # canvas centras pagal y
canvas = Canvas(width = canvas_x_size, height = canvas_y_size, bg = 'black', highlightthickness = 0) # canvas size
canvas.grid(row = 0, column = 0)
      

"""""""""""""""""""""""CURRENT"""""""""""""""""""""""

CONTROLLER_CURRENT_CHARGE_font_color = '#3d64f2' 
CONTROLLER_CURRENT_ZERO_font_color = 'white' 
CONTROLLER_CURRENT_ECO_font_color = '#ADFC3E' 
CONTROLLER_CURRENT_BOOST_font_color = 'red'

CONTROLLER_CURRENT_font = 'Tahoma' # CURRENT šriftas
CONTROLLER_CURRENT_font_size = canvas_y_center * 0.95/8 # CURRENT raidziu dydis
CONTROLLER_CURRENT_font_type = 'bold' # CURRENT šrifto tipas

CONTROLLER_CURRENT_x_offset = canvas_x_center * 0 # x vieta lange
CONTROLLER_CURRENT_y_offset = canvas_y_center * 0.075 # y vieta lange

#CONTROLLER_CURRENT_MAX_value = 320 # skalės MAX
CONTROLLER_CURRENT_MAX_value = 450 # skalės MAX

CONTROLLER_CURRENT_BOOST_value = 180 # BOOST vertė

CONTROLLER_CURRENT_ZERO_value = 0 # ZERO vertė


"""""""""""""""""""""""CONTROLLER_temp_gauge"""""""""""""""""""""""

CONTROLLER_temp_gauge_size = canvas_y_center * 0.4 # dydis

CONTROLLER_temp_gauge_small_tick_start = 0.89 # mažų brūkšnelių pradžia
CONTROLLER_temp_gauge_small_tick_end = 0.95 #  mažų brūkšnelių pabaiga
CONTROLLER_temp_gauge_small_tick_width = CONTROLLER_temp_gauge_size/100 #  mažų brūkšnelių plotis 

CONTROLLER_temp_gauge_middle_tick_start = 0.84 # vidutinių brūkšnelių pradžia
CONTROLLER_temp_gauge_middle_tick_end = 0.95 # vidutinių brūkšnelių pabaiga
CONTROLLER_temp_gauge_middle_tick_width = CONTROLLER_temp_gauge_size/100 # vidutinių brūkšnelių plotis

CONTROLLER_temp_gauge_large_tick_start = 0.78 # didelių brūkšnelių pradžia
CONTROLLER_temp_gauge_large_tick_end = 0.95 # didelių brūkšnelių pabaiga
CONTROLLER_temp_gauge_large_tick_width = CONTROLLER_temp_gauge_size/100 # didelių brūkšnelių plotis

CONTROLLER_temp_gauge_scale_number_start = 0.75 # skaičių pradžia
CONTROLLER_temp_gauge_scale_number_end = 0.75 # skaičių pabaiga

CONTROLLER_temp_digital_NORMAL_font_color = 'white' # LEFT_CONTROLLER temp digital raidžių spalva
CONTROLLER_temp_digital_HIGH_font_color = 'red' # LEFT_CONTROLLER temp digital raidžių spalva  

CONTROLLER_temp_digital_font_color = ''
CONTROLLER_temp_digital_font = 'Tahoma' # LEFT_CONTROLLER temp digital šriftas
CONTROLLER_temp_digital_font_size = CONTROLLER_temp_gauge_size/8 # LEFT_CONTROLLER temp digital raidžių dydis
CONTROLLER_temp_digital_font_type = 'bold' # LEFT_CONTROLLER temp digital šrifto tipas

CONTROLLER_temp_gauge_unit_font_color = 'white' # pavadinimo raidžių spalva
CONTROLLER_temp_gauge_unit_font = 'Tahoma' # pavadinimo šriftas
CONTROLLER_temp_gauge_unit_font_size = CONTROLLER_temp_gauge_size/15 # pavadinimo raidžių dydis
CONTROLLER_temp_gauge_unit_font_type = 'italic', 'bold' # unit šrifto tipas
CONTROLLER_temp_gauge_unit = 'CONTROLLER, °C' # vienetų pavadinimas

CONTROLLER_temp_gauge_unit_y_offset = CONTROLLER_temp_gauge_size/2.5 # pavadinimo aukštis nuo rodyklės

CONTROLLER_temp_gauge_NORMAL_scale_color = 'white' # skalės Low spalva
CONTROLLER_temp_gauge_HIGH_scale_color = 'red' # skalės High spalva

CONTROLLER_temp_gauge_scale_font = 'Tahoma' # skalės šriftas
CONTROLLER_temp_gauge_scale_font_size = CONTROLLER_temp_gauge_size/15 # skalės raidžių dydis
CONTROLLER_temp_gauge_scale_font_type = 'bold' # unit šrifto tipas

CONTROLLER_temp_gauge_scale_MAX_value = 140 # skalės MAX
CONTROLLER_temp_gauge_scale_MID_value = 90 # skalės MID
CONTROLLER_temp_gauge_scale_MIN_value = 20 # skalės MIN

CONTROLLER_temp_gauge_scale_rotation = 1.168 # skalės pasukimas, >1 į dešinę, <1 į kairę
CONTROLLER_temp_gauge_scale_extention = 0.665 # skalės plėtimas. >1 plečia, <1 spaudžia
               
CONTROLLER_temp_gauge_dial_center_size = CONTROLLER_temp_gauge_size/4.5 # rodyklės centro dydis
CONTROLLER_temp_gauge_dial_width = CONTROLLER_temp_gauge_size/24 # rodyklės storis
CONTROLLER_temp_gauge_dial_length = CONTROLLER_temp_gauge_size/1.15 # rodyklės ilgis
CONTROLLER_temp_gauge_dial_start_degree = 120 # rodyklės pradžios kampas
CONTROLLER_temp_gauge_dial_extent = 120 # rodyklės eigos laipsniai
CONTROLLER_temp_gauge_dial_center_color = 'black' # rodyklės centro spalva
CONTROLLER_temp_gauge_dial_center_outline_width = CONTROLLER_temp_gauge_size/130 # rodyklės centro apvado plotis
CONTROLLER_temp_gauge_dial_center_outline_color = 'white' # rodyklės centro apvado spalva

CONTROLLER_temp_gauge_outline_width = CONTROLLER_temp_gauge_size/40 # gauge lanko plotis
CONTROLLER_temp_gauge_outline_start = 28 # lanko pradžios kampas
CONTROLLER_temp_gauge_outline_extent = 124 # lanko ilgis laipsniais
CONTROLLER_temp_gauge_outline_type = 'arc' # lanko tipas
CONTROLLER_temp_gauge_outline_color = '#ADFC3E' # lanko spalva
   
CONTROLLER_temp_gauge_scale_division_number = 30
CONTROLLER_temp_gauge_NORMAL_scale = 18
CONTROLLER_temp_gauge_HIGH_scale = CONTROLLER_temp_gauge_scale_division_number + 1

LEFT_CONTROLLER_temp_gauge_x_offset = canvas_x_center * 0.75 # x vieta lange
LEFT_CONTROLLER_temp_gauge_y_offset = canvas_y_center * -0.86 # y vieta lange

RIGHT_CONTROLLER_temp_gauge_x_offset = canvas_x_center * -0.25 # x vieta lange
RIGHT_CONTROLLER_temp_gauge_y_offset = canvas_y_center * -0.86 # y vieta lange

LEFT_CONTROLLER_temp_digital_x_offset = LEFT_CONTROLLER_temp_gauge_x_offset  # CONTROLLER temp digital x vieta lange
LEFT_CONTROLLER_temp_digital_y_offset = LEFT_CONTROLLER_temp_gauge_y_offset  # CONTROLLER temp digital y vieta lange

RIGHT_CONTROLLER_temp_digital_x_offset = LEFT_CONTROLLER_temp_gauge_x_offset  # CONTROLLER temp digital x vieta lange
RIGHT_CONTROLLER_temp_digital_y_offset = LEFT_CONTROLLER_temp_gauge_y_offset  # CONTROLLER temp digital y vieta lange


"""""""""""""""""""""""MOTOR_temp_gauge"""""""""""""""""""""""

MOTOR_temp_gauge_size = canvas_y_center * 0.4 # dydis

MOTOR_temp_gauge_small_tick_start = 0.89 # mažų brūkšnelių pradžia
MOTOR_temp_gauge_small_tick_end = 0.95 #  mažų brūkšnelių pabaiga
MOTOR_temp_gauge_small_tick_width = MOTOR_temp_gauge_size/100 #  mažų brūkšnelių plotis 

MOTOR_temp_gauge_middle_tick_start = 0.84 # vidutinių brūkšnelių pradžia
MOTOR_temp_gauge_middle_tick_end = 0.95 # vidutinių brūkšnelių pabaiga
MOTOR_temp_gauge_middle_tick_width = MOTOR_temp_gauge_size/100 # vidutinių brūkšnelių plotis

MOTOR_temp_gauge_large_tick_start = 0.78 # didelių brūkšnelių pradžia
MOTOR_temp_gauge_large_tick_end = 0.95 # didelių brūkšnelių pabaiga
MOTOR_temp_gauge_large_tick_width = MOTOR_temp_gauge_size/100 # didelių brūkšnelių plotis

MOTOR_temp_gauge_scale_number_start = 0.75 # skaičių pradžia
MOTOR_temp_gauge_scale_number_end = 0.75 # skaičių pabaiga

MOTOR_temp_gauge_NORMAL_color = 'white' # MOTOR temp digital raidžių spalva
MOTOR_temp_gauge_HIGH_color = 'red' # MOTOR temp digital raidžių spalva

MOTOR_temp_digital_font_color = ''
MOTOR_temp_digital_font = 'Tahoma' # MOTOR temp digital šriftas
MOTOR_temp_digital_font_size = MOTOR_temp_gauge_size/8 # MOTOR temp digital raidžių dydis
MOTOR_temp_digital_font_type = 'bold' # MOTOR temp digital šrifto tipas
        
MOTOR_temp_gauge_unit_font_color = 'white' # pavadinimo raidžių spalva
MOTOR_temp_gauge_unit_font = 'Tahoma' # pavadinimo šriftas
MOTOR_temp_gauge_unit_font_size = MOTOR_temp_gauge_size/15 # pavadinimo raidžių dydis
MOTOR_temp_gauge_unit_font_type = 'italic', 'bold' # unit šrifto tipas
MOTOR_temp_gauge_unit = 'MOTOR, °C' # vienetų pavadinimas

MOTOR_temp_gauge_unit_y_offset = MOTOR_temp_gauge_size/2.5 # pavadinimo aukštis nuo rodyklės

MOTOR_temp_gauge_scale_font = 'Tahoma' # skalės šriftas
MOTOR_temp_gauge_scale_font_size = MOTOR_temp_gauge_size/15 # skalės raidžių dydis
MOTOR_temp_gauge_scale_font_type = 'bold' # unit šrifto tipas

MOTOR_temp_gauge_scale_MAX_value = 140 # skalės MAX
MOTOR_temp_gauge_scale_MID_value = 90 # skalės MID
MOTOR_temp_gauge_scale_MIN_value = 20 # skalės MIN

MOTOR_temp_gauge_scale_rotation = 1.168 # skalės pasukimas, >1 į dešinę, <1 į kairę
MOTOR_temp_gauge_scale_extention = 0.665 # skalės plėtimas. >1 plečia, <1 spaudžia
     
MOTOR_temp_gauge_dial_center_size = MOTOR_temp_gauge_size/4.5 # rodyklės centro dydis
MOTOR_temp_gauge_dial_width = MOTOR_temp_gauge_size/24 # rodyklės storis
MOTOR_temp_gauge_dial_length = MOTOR_temp_gauge_size/1.15 # rodyklės ilgis
MOTOR_temp_gauge_dial_start_degree = 120 # rodyklės pradžios kampas
MOTOR_temp_gauge_dial_extent = 120 # rodyklės eigos laipsniai
MOTOR_temp_gauge_dial_center_color = 'black' # rodyklės centro spalva
MOTOR_temp_gauge_dial_center_outline_width = MOTOR_temp_gauge_size/130 # rodyklės centro apvado plotis
MOTOR_temp_gauge_dial_center_outline_color = 'white' # rodyklės centro apvado spalva

MOTOR_temp_gauge_outline_width = MOTOR_temp_gauge_size/40 # gauge lanko plotis
MOTOR_temp_gauge_outline_start = 28 # lanko pradžios kampas
MOTOR_temp_gauge_outline_extent = 124 # lanko ilgis laipsniais
MOTOR_temp_gauge_outline_type = 'arc' # lanko tipas
MOTOR_temp_gauge_outline_color = '#ADFC3E' # lanko spalva

MOTOR_temp_gauge_scale_division_number = 30
MOTOR_temp_gauge_NORMAL_scale = 18
MOTOR_temp_gauge_HIGH_scale = MOTOR_temp_gauge_scale_division_number + 1

LEFT_MOTOR_temp_gauge_x_offset = canvas_x_center * 0.25 # x vieta lange
LEFT_MOTOR_temp_gauge_y_offset = canvas_y_center * -0.86 # y vieta lange

RIGHT_MOTOR_temp_gauge_x_offset = canvas_x_center * -0.75 # x vieta lange
RIGHT_MOTOR_temp_gauge_y_offset = canvas_y_center * -0.86 # y vieta lange

LEFT_MOTOR_temp_digital_x_offset = LEFT_MOTOR_temp_gauge_x_offset # MOTOR temp digital x vieta lange
LEFT_MOTOR_temp_digital_y_offset = LEFT_MOTOR_temp_gauge_y_offset # MOTOR temp digital y vieta lange

RIGHT_MOTOR_temp_digital_x_offset = RIGHT_MOTOR_temp_gauge_x_offset # MOTOR temp digital x vieta lange
RIGHT_MOTOR_temp_digital_y_offset = RIGHT_MOTOR_temp_gauge_y_offset # MOTOR temp digital y vieta lange
       

"""""""""""""""""""""""MOTOR_RPM gauge"""""""""""""""""""""""

MOTOR_RPM_gauge_size = canvas_y_center * 0.85 # dydis

MOTOR_RPM_gauge_small_tick_color = 'white' # mažų brūkšnelių spalva
MOTOR_RPM_gauge_small_tick_start = 0.89 # mažų brūkšnelių pradžia
MOTOR_RPM_gauge_small_tick_end = 0.95 #  mažų brūkšnelių pabaiga
MOTOR_RPM_gauge_small_tick_width = MOTOR_RPM_gauge_size/100 #  mažų brūkšnelių plotis

MOTOR_RPM_gauge_middle_tick_color = 'white' # vidutinių brūkšnelių spalva
MOTOR_RPM_gauge_middle_tick_start = 0.84 # vidutinių brūkšnelių pradžia
MOTOR_RPM_gauge_middle_tick_end = 0.95 # vidutinių brūkšnelių pabaiga
MOTOR_RPM_gauge_middle_tick_width = MOTOR_RPM_gauge_size/100 # vidutinių brūkšnelių

MOTOR_RPM_gauge_large_tick_color = 'white' # didelių brūkšnelių spalva
MOTOR_RPM_gauge_large_tick_start = 0.78 # didelių brūkšnelių pradžia
MOTOR_RPM_gauge_large_tick_end = 0.95 # didelių brūkšnelių pabaiga
MOTOR_RPM_gauge_large_tick_width = MOTOR_RPM_gauge_size/100 # didelių brūkšnelių plotis

MOTOR_RPM_gauge_scale_number_start = 0.75 # skaičių pradžia
MOTOR_RPM_gauge_scale_number_end = 0.75 # skaičių pabaiga

MOTOR_RPM_gauge_scale_font_color = 'white' # MOTOR temp digital raidžių spalva
MOTOR_RPM_gauge_scale_font = 'Tahoma' # skalės šriftas
MOTOR_RPM_gauge_scale_font_size = MOTOR_RPM_gauge_size/12 # skalės raidžių dydis
MOTOR_RPM_gauge_scale_font_type = 'bold' # unit šrifto tipas

MOTOR_RPM_gauge_unit_font_color = 'white' # pavadinimo raidžių spalva
MOTOR_RPM_gauge_unit_font = 'Tahoma' # pavadinimo šriftas
MOTOR_RPM_gauge_unit_font_size = MOTOR_RPM_gauge_size/18 # pavadinimo raidžių dydis
MOTOR_RPM_gauge_unit_font_type = 'bold', 'italic' # unit šrifto tipas

LEFT_MOTOR_RPM_gauge_unit = 'LEFT RPM, 1000/MIN' # vienetų pavadinimas
RIGHT_MOTOR_RPM_gauge_unit = 'RIGHT RPM, 1000/MIN' # vienetų pavadinimas

MOTOR_RPM_gauge_unit_y_offset = MOTOR_RPM_gauge_size/2.0 # pavadinimo aukštis nuo rodyklės

MOTOR_RPM_gauge_scale_MAX_value = 5000 # skalės MAX
MOTOR_RPM_gauge_scale_MIN_value = 0 # skalės MIN

MOTOR_RPM_gauge_scale_rotation = 0.8 # skalės pasukimas, >1 į dešinę, <1 į kairę
MOTOR_RPM_gauge_scale_extention = 1.4 # skalės plėtimas. >1 plečia, <1 spaudžia

MOTOR_RPM_gauge_outline_width = MOTOR_RPM_gauge_size/40 # gauge lanko plotis
MOTOR_RPM_gauge_outline_start = -37 # lanko pradžios kampas
MOTOR_RPM_gauge_outline_extent = 254 # lanko ilgis laipsniais
MOTOR_RPM_gauge_outline_type = 'arc' # lanko tipas
MOTOR_RPM_gauge_outline_color = '#ADFC3E' # lanko spalva

MOTOR_RPM_gauge_dial_center_size = MOTOR_RPM_gauge_size/2.8 # rodyklės centro dydis
MOTOR_RPM_gauge_dial_width = MOTOR_RPM_gauge_size/15 # rodyklės storis
MOTOR_RPM_gauge_dial_length = MOTOR_RPM_gauge_size/1.1 # rodyklės ilgis
MOTOR_RPM_gauge_dial_start_degree = 54 # rodyklės pradžios kampas
MOTOR_RPM_gauge_dial_extent = 252 # rodyklės eigos laipsniai
MOTOR_RPM_gauge_dial_color = '#ADFC3E' # rodyklės spalva
MOTOR_RPM_gauge_dial_center_color = 'black' # rodyklės centro spalva
MOTOR_RPM_gauge_dial_center_outline_width = MOTOR_RPM_gauge_size/100 # rodyklės centro apvado plotis
MOTOR_RPM_gauge_dial_center_outline_color = 'white' # rodyklės centro apvado spalva

MOTOR_RPM_gauge_scale_division_number = 50
MOTOR_RPM_gauge_scale_division_multiplier = 50000

LEFT_MOTOR_RPM_gauge_x_offset = canvas_x_center * 0.5 # x vieta lange
LEFT_MOTOR_RPM_gauge_y_offset = canvas_y_center * 0.1 # y vieta lange

RIGHT_MOTOR_RPM_gauge_x_offset = canvas_x_center * -0.5 # x vieta lange
RIGHT_MOTOR_RPM_gauge_y_offset = canvas_y_center * 0.1 # y vieta lange


"""""""""""""""""""""""SPEED"""""""""""""""""""""""

SPEED_font_color = 'white' # greičio skaičių spalva
SPEED_font = 'Tahoma' # greičio skaičių šriftas
SPEED_font_size = canvas_y_center * 0.95/4 # greičio skaičių dydis
SPEED_font_type = 'bold' # greičio skaičių tipas

SPEED_x_offset = canvas_x_center * 0 # greičio x vieta lange
SPEED_y_offset = canvas_y_center * 0.85 # greičio y vieta lange

SPEED_unit_font_color = 'white' # greičio skaičių spalva
SPEED_unit_font = 'Tahoma' # greičio skaičių šriftas
SPEED_unit_font_size = canvas_y_center * 0.95/15 # greičio skaičių dydis
SPEED_unit_font_type = 'bold' # greičio skaičių tipas
SPEED_unit = 'km/h'

SPEED_unit_x_offset = canvas_x_center * 0 # greičio unit x vieta lange
SPEED_unit_y_offset = canvas_y_center * 0.65 # greičio unit y vieta lange


"""""""""""""""""""""""BATTERY """""""""""""""""""""""

BATTERY_font_color = 'white'
BATTERY_font = 'Times New Roman' # BATTERY percents šriftas
BATTERY_font_size = canvas_y_center * 0.95/18 # BATTERY percents dydis
BATTERY_font_type = 'bold' # BATTERY digital šrifto tipas

LEFT_BATTERY_x_offset = canvas_x_center * 0.5 # BATTERY x vieta lange
LEFT_BATTERY_y_offset = canvas_y_center * -0.94 # BATTERY y vieta lange

RIGHT_BATTERY_x_offset = canvas_x_center * -0.5 # BATTERY x vieta lange
RIGHT_BATTERY_y_offset = canvas_y_center * -0.94 # BATTERY y vieta lange

BATTERY_unit = 'BATTERY'

BATTERY_digital_font = 'Times New Roman' # BATTERY percents šriftas
BATTERY_digital_font_size = canvas_y_center * 0.95/10 # BATTERY percents dydis
BATTERY_digital_font_type = 'bold' # BATTERY digital šrifto tipas

LEFT_BATTERY_digital_x_offset = canvas_x_center * 0.5 # BATTERY x vieta lange
LEFT_BATTERY_digital_y_offset = canvas_y_center * -0.83 # BATTERY y vieta lange

RIGHT_BATTERY_digital_x_offset = canvas_x_center * -0.5 # BATTERY x vieta lange
RIGHT_BATTERY_digital_y_offset = canvas_y_center * -0.83 # BATTERY y vieta lange

BATTERY_percents_font = 'Times New Roman' # BATTERY percents šriftas
BATTERY_percents_font_size = canvas_y_center * 0.95/20 # BATTERY percents dydis
BATTERY_percents_font_type = 'bold' # BATTERY digital šrifto tipas

LEFT_BATTERY_percents_x_offset = canvas_x_center * 0.42 # BATTERY x vieta lange
LEFT_BATTERY_percents_y_offset = canvas_y_center * -0.85 # BATTERY y vieta lange

RIGHT_BATTERY_percents_x_offset = canvas_x_center * -0.58 # BATTERY x vieta lange
RIGHT_BATTERY_percents_y_offset = canvas_y_center * -0.85 # BATTERY y vieta lange

BATTERY_percents = '%'


"""""""""""""""""""""""ERRORS"""""""""""""""""""""""

ERROR_font_color = 'red' # klaidos skaičių spalva
ERROR_font = 'Tahoma' # klaidos skaičių šriftas
ERROR_font_size = canvas_y_center * 0.95/15 # klaidos skaičių dydis
ERROR_font_type = 'bold' # klaidos skaičių tipas

LEFT_CONTROLLER_ERROR_count_x_offset = LEFT_MOTOR_RPM_gauge_x_offset # x vieta lange
LEFT_CONTROLLER_ERROR_count_y_offset = canvas_y_center * -0.28 # y vieta lange

RIGHT_CONTROLLER_ERROR_count_x_offset = RIGHT_MOTOR_RPM_gauge_x_offset # x vieta lange
RIGHT_CONTROLLER_ERROR_count_y_offset = canvas_y_center * -0.28 # y vieta lange

LEFT_CONTROLLER_ERROR_message_x_offset = LEFT_MOTOR_RPM_gauge_x_offset # x vieta lange
LEFT_CONTROLLER_ERROR_message_y_offset = canvas_y_center * -0.38 # y vieta lange

RIGHT_CONTROLLER_ERROR_message_x_offset = RIGHT_MOTOR_RPM_gauge_x_offset # x vieta lange
RIGHT_CONTROLLER_ERROR_message_y_offset = canvas_y_center * -0.38 # y vieta lange

ERR0_label = 'ERR0:', 'Ident.', 'error'
ERR1_label = 'ERR1:', 'Over', 'voltage'
ERR2_label = 'ERR2:', 'Low', 'voltage'
ERR4_label = 'ERR4:', 'Stall'
ERR5_label = 'ERR5:', 'Internal', 'volts'
ERR6_label = 'ERR6:', 'Contr.', 'overtemp.'
ERR7_label = 'ERR7:', 'Throttle', 'error'
ERR9_label = 'ERR9:', 'Internal', 'reset'
ERR10_label = 'ERR10:', 'Hall', 'throttle'
ERR11_label = 'ERR11:', 'Angle', 'sensor'
ERR14_label = 'ERR14:', 'Motor', 'overtemp.'
ERR15_label = 'ERR15:', 'Hall', 'sensor'

ERR_filter_0 = int('00000001', 2)
ERR_filter_1 = int('00000010', 2)
ERR_filter_2 = int('00000100', 2)
ERR_filter_3 = int('00001000', 2)
ERR_filter_4 = int('00010000', 2)
ERR_filter_5 = int('00100000', 2)
ERR_filter_6 = int('01000000', 2)
ERR_filter_7 = int('10000000', 2)


"""""""""""""""""""""""VOLTAGE"""""""""""""""""""""""

VOLTAGE_NORMAL_font_color = 'white' # VOLTAGE raidžių spalva
VOLTAGE_MID_font_color = 'dark orange' # VOLTAGE raidžių spalva
VOLTAGE_LOW_font_color = 'red' # VOLTAGE raidžių spalva

VOLTAGE_font = 'Tahoma' # VOLTAGE šriftas
VOLTAGE_font_size = canvas_y_center * 0.95/8 # VOLTAGE dydis
VOLTAGE_font_type = 'bold' # VOLTAGE tipas

VOLTAGE_MAX_value = 50.4 # VOLTAGE MAX
VOLTAGE_MID_value = 47.6 # VOLTAGE MID
VOLTAGE_MIN_value = 44.8 # VOLTAGE MIN
VOLTAGE_LOW_value = 42.0 # VOLTAGE LOW

CONTROLLER_VOLTAGE_x_offset = canvas_x_center * 0 # x vieta lange
CONTROLLER_VOLTAGE_y_offset = canvas_y_center * -0.1 # y vieta lange


"""""""""""""""""""""""WATER_PUMP"""""""""""""""""""""

WATER_PUMP_font_color = 'white' # WATER_PUMP raidžių spalva
ON_font_color = 'red' # WATER_PUMP raidžių spalva

WATER_PUMP_font = 'Times New Roman' # WATER_PUMP šriftas
WATER_PUMP_font_size = canvas_y_center * 0.95/14 # WATER_PUMP dydis
WATER_PUMP_font_type = 'bold' # WATER_PUMP tipas

ON_font = 'Times New Roman' # ON šriftas
ON_font_size = canvas_y_center * 0.95/10 # ON dydis
ON_font_type = 'bold' # ON tipas

WATER_PUMP_x_offset = canvas_x_center * 0 # x vieta lange
WATER_PUMP_y_offset = canvas_y_center * 0.9 # y vieta lange

ON_x_offset = canvas_x_center * 0 # x vieta lange
ON_y_offset = canvas_y_center * 0.8 # y vieta lange


"""""""""""""""""""""""Vykdymas"""""""""""""""""""""""

def draw_CONTROLLER_temp_gauge():
    inner_tick_radius1 = int(CONTROLLER_temp_gauge_size * CONTROLLER_temp_gauge_small_tick_start) 
    outer_tick_radius1 = int(CONTROLLER_temp_gauge_size * CONTROLLER_temp_gauge_small_tick_end) 
    inner_tick_radius2 = int(CONTROLLER_temp_gauge_size * CONTROLLER_temp_gauge_middle_tick_start) 
    outer_tick_radius2 = int(CONTROLLER_temp_gauge_size * CONTROLLER_temp_gauge_middle_tick_end) 
    inner_tick_radius3 = int(CONTROLLER_temp_gauge_size * CONTROLLER_temp_gauge_large_tick_start) 
    outer_tick_radius3 = int(CONTROLLER_temp_gauge_size * CONTROLLER_temp_gauge_large_tick_end) 
    inner_tick_radius4 = int(CONTROLLER_temp_gauge_size * CONTROLLER_temp_gauge_scale_number_start)
    outer_tick_radius4 = int(CONTROLLER_temp_gauge_size * CONTROLLER_temp_gauge_scale_number_end)
            
    for tick in range(CONTROLLER_temp_gauge_NORMAL_scale):
        angle_in_radians = CONTROLLER_temp_gauge_scale_rotation * cmath.pi + tick/CONTROLLER_temp_gauge_scale_division_number * CONTROLLER_temp_gauge_scale_extention * cmath.pi
        
        if (tick) >= 0:

            if (tick%10) == 0:
                inner_point2 = cmath.rect(inner_tick_radius2, angle_in_radians)
                outer_point2 = cmath.rect(outer_tick_radius2, angle_in_radians)                   
                inner_point4 = cmath.rect(inner_tick_radius4, angle_in_radians)
                outer_point4 = cmath.rect(outer_tick_radius4, angle_in_radians)
                x = outer_point4.real + canvas_x_center
                y = outer_point4.imag + canvas_y_center
                
                label = str(int(CONTROLLER_temp_gauge_scale_MIN_value + tick * (CONTROLLER_temp_gauge_scale_MAX_value - CONTROLLER_temp_gauge_scale_MIN_value)/CONTROLLER_temp_gauge_scale_division_number))
                                    
                canvas.create_line(*to_absolute_LEFT_CONTROLLER_temp(inner_point2.real, inner_point2.imag),
                                   *to_absolute_LEFT_CONTROLLER_temp(outer_point2.real, outer_point2.imag),
                                    width = CONTROLLER_temp_gauge_middle_tick_width,
                                    fill = CONTROLLER_temp_gauge_NORMAL_scale_color)
                
                canvas.create_text(x - LEFT_CONTROLLER_temp_gauge_x_offset,
                                   y - LEFT_CONTROLLER_temp_gauge_y_offset,
                                   font = (CONTROLLER_temp_gauge_scale_font, int(CONTROLLER_temp_gauge_scale_font_size), CONTROLLER_temp_gauge_scale_font_type),
                                   fill = CONTROLLER_temp_gauge_NORMAL_scale_color,
                                   text = label)
                
                canvas.create_line(*to_absolute_RIGHT_CONTROLLER_temp(inner_point2.real, inner_point2.imag),
                                   *to_absolute_RIGHT_CONTROLLER_temp(outer_point2.real, outer_point2.imag),
                                    width = CONTROLLER_temp_gauge_middle_tick_width,
                                    fill = CONTROLLER_temp_gauge_NORMAL_scale_color)
                
                canvas.create_text(x - RIGHT_CONTROLLER_temp_gauge_x_offset,
                                   y - RIGHT_CONTROLLER_temp_gauge_y_offset,
                                   font = (CONTROLLER_temp_gauge_scale_font, int(CONTROLLER_temp_gauge_scale_font_size), CONTROLLER_temp_gauge_scale_font_type),
                                   fill = CONTROLLER_temp_gauge_NORMAL_scale_color,
                                   text = label) 

            elif (tick%5) == 0:
                  inner_point3 = cmath.rect(inner_tick_radius3, angle_in_radians)
                  outer_point3 = cmath.rect(outer_tick_radius3, angle_in_radians)
                  
                  canvas.create_line(*to_absolute_LEFT_CONTROLLER_temp(inner_point3.real, inner_point3.imag),
                                     *to_absolute_LEFT_CONTROLLER_temp(outer_point3.real, outer_point3.imag),
                                      width = CONTROLLER_temp_gauge_large_tick_width,
                                      fill = CONTROLLER_temp_gauge_NORMAL_scale_color)
                  
                  canvas.create_line(*to_absolute_RIGHT_CONTROLLER_temp(inner_point3.real, inner_point3.imag),
                                     *to_absolute_RIGHT_CONTROLLER_temp(outer_point3.real, outer_point3.imag),
                                      width = CONTROLLER_temp_gauge_large_tick_width,
                                      fill = CONTROLLER_temp_gauge_NORMAL_scale_color) 

            else:
                 inner_point1 = cmath.rect(inner_tick_radius1, angle_in_radians)
                 outer_point1 = cmath.rect(outer_tick_radius1, angle_in_radians)
                 
                 canvas.create_line(*to_absolute_LEFT_CONTROLLER_temp(inner_point1.real, inner_point1.imag),
                                    *to_absolute_LEFT_CONTROLLER_temp(outer_point1.real, outer_point1.imag),
                                     width = CONTROLLER_temp_gauge_small_tick_width,
                                     fill = CONTROLLER_temp_gauge_NORMAL_scale_color)
                 
                 canvas.create_line(*to_absolute_RIGHT_CONTROLLER_temp(inner_point1.real, inner_point1.imag),
                                    *to_absolute_RIGHT_CONTROLLER_temp(outer_point1.real, outer_point1.imag),
                                     width = CONTROLLER_temp_gauge_small_tick_width,
                                     fill = CONTROLLER_temp_gauge_NORMAL_scale_color)

    for tick in range(CONTROLLER_temp_gauge_HIGH_scale):
        angle_in_radians = CONTROLLER_temp_gauge_scale_rotation * cmath.pi + tick/CONTROLLER_temp_gauge_scale_division_number * CONTROLLER_temp_gauge_scale_extention * cmath.pi

        if (tick) > CONTROLLER_temp_gauge_NORMAL_scale - 1:

            if (tick%10) == 0:
                inner_point2 = cmath.rect(inner_tick_radius2, angle_in_radians)
                outer_point2 = cmath.rect(outer_tick_radius2, angle_in_radians)
                inner_point4 = cmath.rect(inner_tick_radius4, angle_in_radians)
                outer_point4 = cmath.rect(outer_tick_radius4, angle_in_radians)
                x = outer_point4.real + canvas_x_center
                y = outer_point4.imag + canvas_y_center
                
                label = str(int(CONTROLLER_temp_gauge_scale_MIN_value + tick * (CONTROLLER_temp_gauge_scale_MAX_value - CONTROLLER_temp_gauge_scale_MIN_value)/CONTROLLER_temp_gauge_scale_division_number))
                
                canvas.create_line(*to_absolute_LEFT_CONTROLLER_temp(inner_point2.real, inner_point2.imag),
                                   *to_absolute_LEFT_CONTROLLER_temp(outer_point2.real, outer_point2.imag),
                                    width = CONTROLLER_temp_gauge_middle_tick_width,
                                    fill = CONTROLLER_temp_gauge_HIGH_scale_color)
                
                canvas.create_text(x - LEFT_CONTROLLER_temp_gauge_x_offset,
                                   y - LEFT_CONTROLLER_temp_gauge_y_offset,
                                   font = (CONTROLLER_temp_gauge_scale_font, int(CONTROLLER_temp_gauge_scale_font_size), CONTROLLER_temp_gauge_scale_font_type),
                                   fill = CONTROLLER_temp_gauge_HIGH_scale_color,
                                   text = label)
                
                canvas.create_line(*to_absolute_RIGHT_CONTROLLER_temp(inner_point2.real, inner_point2.imag),
                                   *to_absolute_RIGHT_CONTROLLER_temp(outer_point2.real, outer_point2.imag),
                                    width = CONTROLLER_temp_gauge_middle_tick_width,
                                    fill = CONTROLLER_temp_gauge_HIGH_scale_color)
                
                canvas.create_text(x - RIGHT_CONTROLLER_temp_gauge_x_offset,
                                   y - RIGHT_CONTROLLER_temp_gauge_y_offset,
                                   font = (CONTROLLER_temp_gauge_scale_font, int(CONTROLLER_temp_gauge_scale_font_size), CONTROLLER_temp_gauge_scale_font_type),
                                   fill = CONTROLLER_temp_gauge_HIGH_scale_color,
                                   text = label)  

            elif (tick%5) == 0:
                  inner_point3 = cmath.rect(inner_tick_radius3, angle_in_radians)
                  outer_point3 = cmath.rect(outer_tick_radius3, angle_in_radians)
                  
                  canvas.create_line(*to_absolute_LEFT_CONTROLLER_temp(inner_point3.real, inner_point3.imag),
                                     *to_absolute_LEFT_CONTROLLER_temp(outer_point3.real, outer_point3.imag),
                                      width = CONTROLLER_temp_gauge_large_tick_width,
                                      fill = CONTROLLER_temp_gauge_HIGH_scale_color)
                  
                  canvas.create_line(*to_absolute_RIGHT_CONTROLLER_temp(inner_point3.real, inner_point3.imag),
                                     *to_absolute_RIGHT_CONTROLLER_temp(outer_point3.real, outer_point3.imag),
                                      width = CONTROLLER_temp_gauge_large_tick_width,
                                      fill = CONTROLLER_temp_gauge_HIGH_scale_color) 

            else:
                 inner_point1 = cmath.rect(inner_tick_radius1, angle_in_radians)
                 outer_point1 = cmath.rect(outer_tick_radius1, angle_in_radians)
                 
                 canvas.create_line(*to_absolute_LEFT_CONTROLLER_temp(inner_point1.real, inner_point1.imag),
                                    *to_absolute_LEFT_CONTROLLER_temp(outer_point1.real, outer_point1.imag),
                                     width = CONTROLLER_temp_gauge_small_tick_width,
                                     fill = CONTROLLER_temp_gauge_HIGH_scale_color)
                 
                 canvas.create_line(*to_absolute_RIGHT_CONTROLLER_temp(inner_point1.real, inner_point1.imag),
                                    *to_absolute_RIGHT_CONTROLLER_temp(outer_point1.real, outer_point1.imag),
                                     width = CONTROLLER_temp_gauge_small_tick_width,
                                     fill = CONTROLLER_temp_gauge_HIGH_scale_color)
                 
                 
    
    canvas.create_text(canvas_x_center - LEFT_CONTROLLER_temp_gauge_x_offset,
                       canvas_y_center - LEFT_CONTROLLER_temp_gauge_y_offset - CONTROLLER_temp_gauge_unit_y_offset,
                       font = (CONTROLLER_temp_gauge_unit_font, int(CONTROLLER_temp_gauge_unit_font_size), CONTROLLER_temp_gauge_unit_font_type),
                       fill = CONTROLLER_temp_gauge_unit_font_color,
                       text = CONTROLLER_temp_gauge_unit) 
    
    canvas.create_arc(canvas_x_center - CONTROLLER_temp_gauge_size - LEFT_CONTROLLER_temp_gauge_x_offset,
                      canvas_y_center - CONTROLLER_temp_gauge_size - LEFT_CONTROLLER_temp_gauge_y_offset,
                      canvas_x_center + CONTROLLER_temp_gauge_size - LEFT_CONTROLLER_temp_gauge_x_offset,
                      canvas_y_center + CONTROLLER_temp_gauge_size - LEFT_CONTROLLER_temp_gauge_y_offset,
                      style = CONTROLLER_temp_gauge_outline_type,
                      width = CONTROLLER_temp_gauge_outline_width,
                      start = CONTROLLER_temp_gauge_outline_start,
                      extent = CONTROLLER_temp_gauge_outline_extent,
                      outline = CONTROLLER_temp_gauge_outline_color)
    
    canvas.create_text(canvas_x_center - RIGHT_CONTROLLER_temp_gauge_x_offset,
                       canvas_y_center - RIGHT_CONTROLLER_temp_gauge_y_offset - CONTROLLER_temp_gauge_unit_y_offset,
                       font = (CONTROLLER_temp_gauge_unit_font, int(CONTROLLER_temp_gauge_unit_font_size), CONTROLLER_temp_gauge_unit_font_type),
                       fill = CONTROLLER_temp_gauge_unit_font_color,
                       text = CONTROLLER_temp_gauge_unit) 
    
    canvas.create_arc(canvas_x_center - RIGHT_CONTROLLER_temp_gauge_x_offset  - CONTROLLER_temp_gauge_size,
                      canvas_y_center - RIGHT_CONTROLLER_temp_gauge_y_offset - CONTROLLER_temp_gauge_size,
                      canvas_x_center - RIGHT_CONTROLLER_temp_gauge_x_offset + CONTROLLER_temp_gauge_size,
                      canvas_y_center - RIGHT_CONTROLLER_temp_gauge_y_offset + CONTROLLER_temp_gauge_size,
                      style = CONTROLLER_temp_gauge_outline_type,
                      width = CONTROLLER_temp_gauge_outline_width,
                      start = CONTROLLER_temp_gauge_outline_start,
                      extent = CONTROLLER_temp_gauge_outline_extent,
                      outline = CONTROLLER_temp_gauge_outline_color)       

def set_LEFT_CONTROLLER_temp(LEFT_CONTROLLER_temp, LEFT_CONTROLLER_temp_digital):
              
    LEFT_CONTROLLER_temp = LEFT_CONTROLLER_temp if LEFT_CONTROLLER_temp <= CONTROLLER_temp_gauge_scale_MAX_value else CONTROLLER_temp_gauge_scale_MAX_value
    LEFT_CONTROLLER_temp = LEFT_CONTROLLER_temp if LEFT_CONTROLLER_temp > CONTROLLER_temp_gauge_scale_MIN_value else CONTROLLER_temp_gauge_scale_MIN_value
    degree = CONTROLLER_temp_gauge_dial_start_degree + (LEFT_CONTROLLER_temp - CONTROLLER_temp_gauge_scale_MIN_value)/(CONTROLLER_temp_gauge_scale_MAX_value -
             CONTROLLER_temp_gauge_scale_MIN_value) * CONTROLLER_temp_gauge_dial_extent            
       
    if LEFT_CONTROLLER_temp >= CONTROLLER_temp_gauge_scale_MIN_value:
       LEFT_CONTROLLER_temp_gauge_dial_color = CONTROLLER_temp_gauge_NORMAL_scale_color 
       LEFT_CONTROLLER_temp_digital_font_color = CONTROLLER_temp_digital_NORMAL_font_color
       LEFT_CONTROLLER_temp_gauge_dial_center_outline_color = CONTROLLER_temp_gauge_NORMAL_scale_color
                           
    if LEFT_CONTROLLER_temp > CONTROLLER_temp_gauge_scale_MID_value:
       LEFT_CONTROLLER_temp_gauge_dial_color = CONTROLLER_temp_gauge_HIGH_scale_color 
       LEFT_CONTROLLER_temp_digital_font_color = CONTROLLER_temp_digital_HIGH_font_color
       LEFT_CONTROLLER_temp_gauge_dial_center_outline_color = CONTROLLER_temp_gauge_HIGH_scale_color
                  
    xr = canvas_x_center - LEFT_CONTROLLER_temp_gauge_x_offset
    yr = canvas_y_center - LEFT_CONTROLLER_temp_gauge_y_offset
    angle = math.radians(-degree)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    dy = CONTROLLER_temp_gauge_dial_width * sin_val
    dx = CONTROLLER_temp_gauge_dial_width * cos_val
    dx2 = CONTROLLER_temp_gauge_dial_length * sin_val
    dy2 = CONTROLLER_temp_gauge_dial_length * cos_val
    mlx = xr + dx
    mly = yr - dy
    mrx = xr - dx
    mry = yr + dy
    px = xr + dx2
    py = yr + dy2
    xyz = mlx, mly, px, py, mrx, mry
   
    canvas.delete('LEFT_CONTROLLER_temp_dial')
    
    canvas.create_polygon(xyz, fill = LEFT_CONTROLLER_temp_gauge_dial_color, tags = 'LEFT_CONTROLLER_temp_dial')
    
    canvas.create_oval(xr - CONTROLLER_temp_gauge_dial_center_size,
                       yr - CONTROLLER_temp_gauge_dial_center_size,
                       xr + CONTROLLER_temp_gauge_dial_center_size,
                       yr + CONTROLLER_temp_gauge_dial_center_size,
                       fill = CONTROLLER_temp_gauge_dial_center_color,
                       outline = CONTROLLER_temp_gauge_dial_center_outline_color,
                       width = CONTROLLER_temp_gauge_dial_center_outline_width,
                       tags = 'LEFT_CONTROLLER_temp_dial')
    
    canvas.create_text(canvas_x_center - LEFT_CONTROLLER_temp_gauge_x_offset,
                       canvas_y_center - LEFT_CONTROLLER_temp_gauge_y_offset,
                       font = (CONTROLLER_temp_digital_font, int(CONTROLLER_temp_digital_font_size), CONTROLLER_temp_digital_font_type),
                       fill = LEFT_CONTROLLER_temp_digital_font_color,
                       text = LEFT_CONTROLLER_temp_digital,
                       tags = 'LEFT_CONTROLLER_temp_dial')

def set_RIGHT_CONTROLLER_temp(RIGHT_CONTROLLER_temp, RIGHT_CONTROLLER_temp_digital):
              
    RIGHT_CONTROLLER_temp = RIGHT_CONTROLLER_temp if RIGHT_CONTROLLER_temp <= CONTROLLER_temp_gauge_scale_MAX_value else CONTROLLER_temp_gauge_scale_MAX_value
    RIGHT_CONTROLLER_temp = RIGHT_CONTROLLER_temp if RIGHT_CONTROLLER_temp > CONTROLLER_temp_gauge_scale_MIN_value else CONTROLLER_temp_gauge_scale_MIN_value
    degree = CONTROLLER_temp_gauge_dial_start_degree + (RIGHT_CONTROLLER_temp - CONTROLLER_temp_gauge_scale_MIN_value)/(CONTROLLER_temp_gauge_scale_MAX_value -
             CONTROLLER_temp_gauge_scale_MIN_value) * CONTROLLER_temp_gauge_dial_extent            
       
    if RIGHT_CONTROLLER_temp >= CONTROLLER_temp_gauge_scale_MIN_value:
       RIGHT_CONTROLLER_temp_gauge_dial_color = CONTROLLER_temp_gauge_NORMAL_scale_color 
       RIGHT_CONTROLLER_temp_digital_font_color = CONTROLLER_temp_digital_NORMAL_font_color
       RIGHT_CONTROLLER_temp_gauge_dial_center_outline_color = CONTROLLER_temp_gauge_NORMAL_scale_color
                           
    if RIGHT_CONTROLLER_temp > CONTROLLER_temp_gauge_scale_MID_value:
       RIGHT_CONTROLLER_temp_gauge_dial_color = CONTROLLER_temp_gauge_HIGH_scale_color 
       RIGHT_CONTROLLER_temp_digital_font_color = CONTROLLER_temp_digital_HIGH_font_color
       RIGHT_CONTROLLER_temp_gauge_dial_center_outline_color = CONTROLLER_temp_gauge_HIGH_scale_color
                  
    xr = canvas_x_center - RIGHT_CONTROLLER_temp_gauge_x_offset
    yr = canvas_y_center - RIGHT_CONTROLLER_temp_gauge_y_offset
    angle = math.radians(-degree)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    dy = CONTROLLER_temp_gauge_dial_width * sin_val
    dx = CONTROLLER_temp_gauge_dial_width * cos_val
    dx2 = CONTROLLER_temp_gauge_dial_length * sin_val
    dy2 = CONTROLLER_temp_gauge_dial_length * cos_val
    mlx = xr + dx
    mly = yr - dy
    mrx = xr - dx
    mry = yr + dy
    px = xr + dx2
    py = yr + dy2
    xyz = mlx, mly, px, py, mrx, mry
   
    canvas.delete('RIGHT_CONTROLLER_temp_dial')
    
    canvas.create_polygon(xyz, fill = RIGHT_CONTROLLER_temp_gauge_dial_color, tags = 'RIGHT_CONTROLLER_temp_dial')
    
    canvas.create_oval(xr - CONTROLLER_temp_gauge_dial_center_size,
                       yr - CONTROLLER_temp_gauge_dial_center_size,
                       xr + CONTROLLER_temp_gauge_dial_center_size,
                       yr + CONTROLLER_temp_gauge_dial_center_size,
                       fill = CONTROLLER_temp_gauge_dial_center_color,
                       outline = CONTROLLER_temp_gauge_dial_center_outline_color,
                       width = CONTROLLER_temp_gauge_dial_center_outline_width,
                       tags = 'RIGHT_CONTROLLER_temp_dial')
    
    canvas.create_text(canvas_x_center - RIGHT_CONTROLLER_temp_gauge_x_offset,
                       canvas_y_center - RIGHT_CONTROLLER_temp_gauge_y_offset,
                       font = (CONTROLLER_temp_digital_font, int(CONTROLLER_temp_digital_font_size), CONTROLLER_temp_digital_font_type),
                       fill = RIGHT_CONTROLLER_temp_digital_font_color,
                       text = RIGHT_CONTROLLER_temp_digital,
                       tags = 'RIGHT_CONTROLLER_temp_dial')

def draw_MOTOR_temp_gauge():    
    inner_tick_radius1 = int(MOTOR_temp_gauge_size * MOTOR_temp_gauge_small_tick_start) 
    outer_tick_radius1 = int(MOTOR_temp_gauge_size * MOTOR_temp_gauge_small_tick_end)
    inner_tick_radius2 = int(MOTOR_temp_gauge_size * MOTOR_temp_gauge_middle_tick_start) 
    outer_tick_radius2 = int(MOTOR_temp_gauge_size * MOTOR_temp_gauge_middle_tick_end) 
    inner_tick_radius3 = int(MOTOR_temp_gauge_size * MOTOR_temp_gauge_large_tick_start) 
    outer_tick_radius3 = int(MOTOR_temp_gauge_size * MOTOR_temp_gauge_large_tick_end) 
    inner_tick_radius4 = int(MOTOR_temp_gauge_size * MOTOR_temp_gauge_scale_number_start)
    outer_tick_radius4 = int(MOTOR_temp_gauge_size * MOTOR_temp_gauge_scale_number_end)
    
    for tick in range(MOTOR_temp_gauge_NORMAL_scale):
        angle_in_radians = MOTOR_temp_gauge_scale_rotation * cmath.pi + tick/MOTOR_temp_gauge_scale_division_number * MOTOR_temp_gauge_scale_extention * cmath.pi
        
        if (tick) >= 0:

            if (tick%10) == 0:
                inner_point2 = cmath.rect(inner_tick_radius2, angle_in_radians)
                outer_point2 = cmath.rect(outer_tick_radius2, angle_in_radians)
                inner_point4 = cmath.rect(inner_tick_radius4, angle_in_radians)
                outer_point4 = cmath.rect(outer_tick_radius4, angle_in_radians)
                x = outer_point4.real + canvas_x_center
                y = outer_point4.imag + canvas_y_center
                
                label = str(int(MOTOR_temp_gauge_scale_MIN_value + tick * (MOTOR_temp_gauge_scale_MAX_value - MOTOR_temp_gauge_scale_MIN_value)/MOTOR_temp_gauge_scale_division_number))
                
                canvas.create_line(*to_absolute_LEFT_MOTOR_temp(inner_point2.real, inner_point2.imag),
                                   *to_absolute_LEFT_MOTOR_temp(outer_point2.real, outer_point2.imag),
                                    width = MOTOR_temp_gauge_middle_tick_width,
                                    fill = MOTOR_temp_gauge_NORMAL_color)
                
                canvas.create_text(x - LEFT_MOTOR_temp_gauge_x_offset,
                                   y - LEFT_MOTOR_temp_gauge_y_offset,
                                   font = (MOTOR_temp_gauge_scale_font, int(MOTOR_temp_gauge_scale_font_size), MOTOR_temp_gauge_scale_font_type),
                                   fill = MOTOR_temp_gauge_NORMAL_color,
                                   text = label)
                
                canvas.create_line(*to_absolute_RIGHT_MOTOR_temp(inner_point2.real, inner_point2.imag),
                                   *to_absolute_RIGHT_MOTOR_temp(outer_point2.real, outer_point2.imag),
                                    width = MOTOR_temp_gauge_middle_tick_width,
                                    fill = MOTOR_temp_gauge_NORMAL_color)
                
                canvas.create_text(x - RIGHT_MOTOR_temp_gauge_x_offset,
                                   y - RIGHT_MOTOR_temp_gauge_y_offset,
                                   font = (MOTOR_temp_gauge_scale_font, int(MOTOR_temp_gauge_scale_font_size), MOTOR_temp_gauge_scale_font_type),
                                   fill = MOTOR_temp_gauge_NORMAL_color,
                                   text = label) 


            elif (tick%5) == 0:
                  inner_point3 = cmath.rect(inner_tick_radius3, angle_in_radians)
                  outer_point3 = cmath.rect(outer_tick_radius3, angle_in_radians)
                  
                  canvas.create_line(*to_absolute_LEFT_MOTOR_temp(inner_point3.real, inner_point3.imag),
                                     *to_absolute_LEFT_MOTOR_temp(outer_point3.real, outer_point3.imag),
                                      width = MOTOR_temp_gauge_large_tick_width,
                                      fill = MOTOR_temp_gauge_NORMAL_color)
                  
                  canvas.create_line(*to_absolute_RIGHT_MOTOR_temp(inner_point3.real, inner_point3.imag),
                                     *to_absolute_RIGHT_MOTOR_temp(outer_point3.real, outer_point3.imag),
                                      width = MOTOR_temp_gauge_large_tick_width,
                                      fill = MOTOR_temp_gauge_NORMAL_color) 

            else:
                 inner_point1 = cmath.rect(inner_tick_radius1, angle_in_radians)
                 outer_point1 = cmath.rect(outer_tick_radius1, angle_in_radians)
                 
                 canvas.create_line(*to_absolute_LEFT_MOTOR_temp(inner_point1.real, inner_point1.imag),
                                    *to_absolute_LEFT_MOTOR_temp(outer_point1.real, outer_point1.imag),
                                     width = MOTOR_temp_gauge_small_tick_width,
                                     fill = MOTOR_temp_gauge_NORMAL_color)
                 
                 canvas.create_line(*to_absolute_RIGHT_MOTOR_temp(inner_point1.real, inner_point1.imag),
                                    *to_absolute_RIGHT_MOTOR_temp(outer_point1.real, outer_point1.imag),
                                     width = MOTOR_temp_gauge_small_tick_width,
                                     fill = MOTOR_temp_gauge_NORMAL_color)

    for tick in range(MOTOR_temp_gauge_HIGH_scale):
        angle_in_radians = MOTOR_temp_gauge_scale_rotation * cmath.pi + tick/MOTOR_temp_gauge_scale_division_number * MOTOR_temp_gauge_scale_extention * cmath.pi

        if (tick) > MOTOR_temp_gauge_NORMAL_scale - 1:

            if (tick%10) == 0:
                inner_point2 = cmath.rect(inner_tick_radius2, angle_in_radians)
                outer_point2 = cmath.rect(outer_tick_radius2, angle_in_radians)
                inner_point4 = cmath.rect(inner_tick_radius4, angle_in_radians)
                outer_point4 = cmath.rect(outer_tick_radius4, angle_in_radians)
                x = outer_point4.real + canvas_x_center
                y = outer_point4.imag + canvas_y_center
                
                label = str(int(MOTOR_temp_gauge_scale_MIN_value + tick * (MOTOR_temp_gauge_scale_MAX_value - MOTOR_temp_gauge_scale_MIN_value)/MOTOR_temp_gauge_scale_division_number))
                
                canvas.create_line(*to_absolute_LEFT_MOTOR_temp(inner_point2.real, inner_point2.imag),
                                   *to_absolute_LEFT_MOTOR_temp(outer_point2.real, outer_point2.imag),
                                    width = MOTOR_temp_gauge_middle_tick_width,
                                    fill = MOTOR_temp_gauge_HIGH_color)
                
                canvas.create_text(x - LEFT_MOTOR_temp_gauge_x_offset,
                                   y - LEFT_MOTOR_temp_gauge_y_offset,
                                   font = (MOTOR_temp_gauge_scale_font, int(MOTOR_temp_gauge_scale_font_size), MOTOR_temp_gauge_scale_font_type),
                                   fill = MOTOR_temp_gauge_HIGH_color,
                                   text = label)
                
                canvas.create_line(*to_absolute_RIGHT_MOTOR_temp(inner_point2.real, inner_point2.imag),
                                   *to_absolute_RIGHT_MOTOR_temp(outer_point2.real, outer_point2.imag),
                                    width = MOTOR_temp_gauge_middle_tick_width,
                                    fill = MOTOR_temp_gauge_HIGH_color)
                
                canvas.create_text(x - RIGHT_MOTOR_temp_gauge_x_offset,
                                   y - RIGHT_MOTOR_temp_gauge_y_offset,
                                   font = (MOTOR_temp_gauge_scale_font, int(MOTOR_temp_gauge_scale_font_size), MOTOR_temp_gauge_scale_font_type),
                                   fill = MOTOR_temp_gauge_HIGH_color,
                                   text = label) 

            elif (tick%5) == 0:
                  inner_point3 = cmath.rect(inner_tick_radius3, angle_in_radians)
                  outer_point3 = cmath.rect(outer_tick_radius3, angle_in_radians)
                  
                  canvas.create_line(*to_absolute_LEFT_MOTOR_temp(inner_point3.real, inner_point3.imag),
                                     *to_absolute_LEFT_MOTOR_temp(outer_point3.real, outer_point3.imag),
                                      width = MOTOR_temp_gauge_large_tick_width,
                                      fill = MOTOR_temp_gauge_HIGH_color)
                  
                  canvas.create_line(*to_absolute_RIGHT_MOTOR_temp(inner_point3.real, inner_point3.imag),
                                     *to_absolute_RIGHT_MOTOR_temp(outer_point3.real, outer_point3.imag),
                                      width = MOTOR_temp_gauge_large_tick_width,
                                      fill = MOTOR_temp_gauge_HIGH_color) 

            else:
                  inner_point1 = cmath.rect(inner_tick_radius1, angle_in_radians)
                  outer_point1 = cmath.rect(outer_tick_radius1, angle_in_radians)
                  
                  canvas.create_line(*to_absolute_LEFT_MOTOR_temp(inner_point1.real, inner_point1.imag),
                                     *to_absolute_LEFT_MOTOR_temp(outer_point1.real, outer_point1.imag),
                                      width = MOTOR_temp_gauge_small_tick_width,
                                      fill = MOTOR_temp_gauge_HIGH_color)
                  
                  canvas.create_line(*to_absolute_RIGHT_MOTOR_temp(inner_point1.real, inner_point1.imag),
                                    *to_absolute_RIGHT_MOTOR_temp(outer_point1.real, outer_point1.imag),
                                     width = MOTOR_temp_gauge_small_tick_width,
                                     fill = MOTOR_temp_gauge_HIGH_color)                  
                  
    canvas.create_text(canvas_x_center - LEFT_MOTOR_temp_gauge_x_offset,
                       canvas_y_center - LEFT_MOTOR_temp_gauge_y_offset - MOTOR_temp_gauge_unit_y_offset,
                       font = (MOTOR_temp_gauge_unit_font, int(MOTOR_temp_gauge_unit_font_size), MOTOR_temp_gauge_unit_font_type),
                       fill = MOTOR_temp_gauge_unit_font_color,
                       text = MOTOR_temp_gauge_unit)
    
    canvas.create_arc(canvas_x_center - LEFT_MOTOR_temp_gauge_x_offset  - MOTOR_temp_gauge_size,
                      canvas_y_center - LEFT_MOTOR_temp_gauge_y_offset - MOTOR_temp_gauge_size,
                      canvas_x_center + MOTOR_temp_gauge_size - LEFT_MOTOR_temp_gauge_x_offset,
                      canvas_y_center - LEFT_MOTOR_temp_gauge_y_offset + MOTOR_temp_gauge_size,
                      style = MOTOR_temp_gauge_outline_type,
                      width = MOTOR_temp_gauge_outline_width,
                      start = MOTOR_temp_gauge_outline_start,
                      extent = MOTOR_temp_gauge_outline_extent,
                      outline = MOTOR_temp_gauge_outline_color)
    
    canvas.create_text(canvas_x_center - RIGHT_MOTOR_temp_gauge_x_offset,
                       canvas_y_center - RIGHT_MOTOR_temp_gauge_y_offset - MOTOR_temp_gauge_unit_y_offset,
                       font = (MOTOR_temp_gauge_unit_font, int(MOTOR_temp_gauge_unit_font_size), MOTOR_temp_gauge_unit_font_type),
                       fill = MOTOR_temp_gauge_unit_font_color,
                       text = MOTOR_temp_gauge_unit)
    
    canvas.create_arc(canvas_x_center - RIGHT_MOTOR_temp_gauge_x_offset  - MOTOR_temp_gauge_size,
                      canvas_y_center - RIGHT_MOTOR_temp_gauge_y_offset - MOTOR_temp_gauge_size,
                      canvas_x_center - RIGHT_MOTOR_temp_gauge_x_offset + MOTOR_temp_gauge_size,
                      canvas_y_center - RIGHT_MOTOR_temp_gauge_y_offset + MOTOR_temp_gauge_size,
                      style = MOTOR_temp_gauge_outline_type,
                      width = MOTOR_temp_gauge_outline_width,
                      start = MOTOR_temp_gauge_outline_start,
                      extent = MOTOR_temp_gauge_outline_extent,
                      outline = MOTOR_temp_gauge_outline_color)
    
def set_LEFT_MOTOR_temp(LEFT_MOTOR_temp, LEFT_MOTOR_temp_digital):
               
    LEFT_MOTOR_temp = LEFT_MOTOR_temp if LEFT_MOTOR_temp <= MOTOR_temp_gauge_scale_MAX_value else MOTOR_temp_gauge_scale_MAX_value
    LEFT_MOTOR_temp = LEFT_MOTOR_temp if LEFT_MOTOR_temp > MOTOR_temp_gauge_scale_MIN_value else MOTOR_temp_gauge_scale_MIN_value
    degree = MOTOR_temp_gauge_dial_start_degree + (LEFT_MOTOR_temp - MOTOR_temp_gauge_scale_MIN_value)/(MOTOR_temp_gauge_scale_MAX_value -
             MOTOR_temp_gauge_scale_MIN_value) * MOTOR_temp_gauge_dial_extent
    
    if LEFT_MOTOR_temp >= MOTOR_temp_gauge_scale_MIN_value:
       LEFT_MOTOR_temp_gauge_dial_color = MOTOR_temp_gauge_NORMAL_color 
       LEFT_MOTOR_temp_digital_font_color = MOTOR_temp_gauge_NORMAL_color
       LEFT_MOTOR_temp_gauge_dial_center_outline_color = MOTOR_temp_gauge_NORMAL_color
           
    if LEFT_MOTOR_temp > MOTOR_temp_gauge_scale_MID_value:
       LEFT_MOTOR_temp_gauge_dial_color = MOTOR_temp_gauge_HIGH_color 
       LEFT_MOTOR_temp_digital_font_color = MOTOR_temp_gauge_HIGH_color
       LEFT_MOTOR_temp_gauge_dial_center_outline_color = MOTOR_temp_gauge_HIGH_color
      
    xr = canvas_x_center - LEFT_MOTOR_temp_gauge_x_offset
    yr = canvas_y_center - LEFT_MOTOR_temp_gauge_y_offset
    angle = math.radians(-degree)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    dy = MOTOR_temp_gauge_dial_width * sin_val
    dx = MOTOR_temp_gauge_dial_width * cos_val
    dx2 = MOTOR_temp_gauge_dial_length * sin_val
    dy2 = MOTOR_temp_gauge_dial_length * cos_val
    mlx = xr + dx
    mly = yr - dy
    mrx = xr - dx
    mry = yr + dy
    px = xr + dx2
    py = yr + dy2
    xyz = mlx, mly, px, py, mrx, mry
   
    canvas.delete('LEFT_MOTOR_temp_dial')

    canvas.create_polygon(xyz, fill = LEFT_MOTOR_temp_gauge_dial_color, tags = 'LEFT_MOTOR_temp_dial')
    
    canvas.create_oval(xr - MOTOR_temp_gauge_dial_center_size,
                       yr - MOTOR_temp_gauge_dial_center_size,
                       xr + MOTOR_temp_gauge_dial_center_size,
                       yr + MOTOR_temp_gauge_dial_center_size,
                       fill = MOTOR_temp_gauge_dial_center_color,
                       outline = MOTOR_temp_gauge_dial_center_outline_color,
                       width = MOTOR_temp_gauge_dial_center_outline_width,
                       tags = 'LEFT_MOTOR_temp_dial')

    canvas.create_text(canvas_x_center - LEFT_MOTOR_temp_gauge_x_offset,
                       canvas_y_center - LEFT_MOTOR_temp_gauge_y_offset,
                       font = (MOTOR_temp_digital_font, int(MOTOR_temp_digital_font_size), MOTOR_temp_digital_font_type),
                       fill = LEFT_MOTOR_temp_digital_font_color,
                       text = LEFT_MOTOR_temp_digital,
                       tags = 'LEFT_MOTOR_temp_dial')
    
def set_RIGHT_MOTOR_temp(RIGHT_MOTOR_temp, RIGHT_MOTOR_temp_digital):
               
    RIGHT_MOTOR_temp = RIGHT_MOTOR_temp if RIGHT_MOTOR_temp <= MOTOR_temp_gauge_scale_MAX_value else MOTOR_temp_gauge_scale_MAX_value
    RIGHT_MOTOR_temp = RIGHT_MOTOR_temp if RIGHT_MOTOR_temp > MOTOR_temp_gauge_scale_MIN_value else MOTOR_temp_gauge_scale_MIN_value
    degree = MOTOR_temp_gauge_dial_start_degree + (RIGHT_MOTOR_temp - MOTOR_temp_gauge_scale_MIN_value)/(MOTOR_temp_gauge_scale_MAX_value -
             MOTOR_temp_gauge_scale_MIN_value) * MOTOR_temp_gauge_dial_extent
    
    if RIGHT_MOTOR_temp >= MOTOR_temp_gauge_scale_MIN_value:
       RIGHT_MOTOR_temp_gauge_dial_color = MOTOR_temp_gauge_NORMAL_color 
       RIGHT_MOTOR_temp_digital_font_color = MOTOR_temp_gauge_NORMAL_color
       RIGHT_MOTOR_temp_gauge_dial_center_outline_color = MOTOR_temp_gauge_NORMAL_color
           
    if RIGHT_MOTOR_temp > MOTOR_temp_gauge_scale_MID_value:
       RIGHT_MOTOR_temp_gauge_dial_color = MOTOR_temp_gauge_HIGH_color 
       RIGHT_MOTOR_temp_digital_font_color = MOTOR_temp_gauge_HIGH_color 
       RIGHT_MOTOR_temp_gauge_dial_center_outline_color = MOTOR_temp_gauge_HIGH_color 
      
    xr = canvas_x_center - RIGHT_MOTOR_temp_gauge_x_offset
    yr = canvas_y_center - RIGHT_MOTOR_temp_gauge_y_offset
    angle = math.radians(-degree)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    dy = MOTOR_temp_gauge_dial_width * sin_val
    dx = MOTOR_temp_gauge_dial_width * cos_val
    dx2 = MOTOR_temp_gauge_dial_length * sin_val
    dy2 = MOTOR_temp_gauge_dial_length * cos_val
    mlx = xr + dx
    mly = yr - dy
    mrx = xr - dx
    mry = yr + dy
    px = xr + dx2
    py = yr + dy2
    xyz = mlx, mly, px, py, mrx, mry
   
    canvas.delete('RIGHT_MOTOR_temp_dial')

    canvas.create_polygon(xyz, fill = RIGHT_MOTOR_temp_gauge_dial_color, tags = 'RIGHT_MOTOR_temp_dial')
    
    canvas.create_oval(xr - MOTOR_temp_gauge_dial_center_size,
                       yr - MOTOR_temp_gauge_dial_center_size,
                       xr + MOTOR_temp_gauge_dial_center_size,
                       yr + MOTOR_temp_gauge_dial_center_size,
                       fill = MOTOR_temp_gauge_dial_center_color,
                       outline = MOTOR_temp_gauge_dial_center_outline_color,
                       width = MOTOR_temp_gauge_dial_center_outline_width,
                       tags = 'RIGHT_MOTOR_temp_dial')

    canvas.create_text(canvas_x_center - RIGHT_MOTOR_temp_gauge_x_offset,
                       canvas_y_center - RIGHT_MOTOR_temp_gauge_y_offset,
                       font = (MOTOR_temp_digital_font, int(MOTOR_temp_digital_font_size), MOTOR_temp_digital_font_type),
                       fill = RIGHT_MOTOR_temp_digital_font_color,
                       text = RIGHT_MOTOR_temp_digital,
                       tags = 'RIGHT_MOTOR_temp_dial')

def draw_MOTOR_RPM_gauge():
    inner_tick_radius1 = int(MOTOR_RPM_gauge_size * MOTOR_RPM_gauge_small_tick_start) 
    outer_tick_radius1 = int(MOTOR_RPM_gauge_size * MOTOR_RPM_gauge_small_tick_end) 
    inner_tick_radius2 = int(MOTOR_RPM_gauge_size * MOTOR_RPM_gauge_middle_tick_start) 
    outer_tick_radius2 = int(MOTOR_RPM_gauge_size * MOTOR_RPM_gauge_middle_tick_end) 
    inner_tick_radius3 = int(MOTOR_RPM_gauge_size * MOTOR_RPM_gauge_large_tick_start) 
    outer_tick_radius3 = int(MOTOR_RPM_gauge_size * MOTOR_RPM_gauge_large_tick_end) 
    inner_tick_radius4 = int(MOTOR_RPM_gauge_size * MOTOR_RPM_gauge_scale_number_start) 
    outer_tick_radius4 = int(MOTOR_RPM_gauge_size * MOTOR_RPM_gauge_scale_number_end)
    
    for tick in range(MOTOR_RPM_gauge_scale_division_number + 1):
        angle_in_radians = MOTOR_RPM_gauge_scale_rotation * cmath.pi + tick/MOTOR_RPM_gauge_scale_division_number * MOTOR_RPM_gauge_scale_extention * cmath.pi

        if (tick%10) == 0:
            inner_point2 = cmath.rect(inner_tick_radius2, angle_in_radians)
            outer_point2 = cmath.rect(outer_tick_radius2, angle_in_radians)
            
            canvas.create_line(*to_absolute_LEFT_MOTOR_RPM(inner_point2.real, inner_point2.imag),
                               *to_absolute_LEFT_MOTOR_RPM(outer_point2.real, outer_point2.imag),
                                width = MOTOR_RPM_gauge_middle_tick_width,
                                fill = MOTOR_RPM_gauge_middle_tick_color)
            
            canvas.create_line(*to_absolute_RIGHT_MOTOR_RPM(inner_point2.real, inner_point2.imag),
                               *to_absolute_RIGHT_MOTOR_RPM(outer_point2.real, outer_point2.imag),
                                width = MOTOR_RPM_gauge_middle_tick_width,
                                fill = MOTOR_RPM_gauge_middle_tick_color) 

        elif (tick%5) == 0:
              inner_point3 = cmath.rect(inner_tick_radius3, angle_in_radians)
              outer_point3 = cmath.rect(outer_tick_radius3, angle_in_radians)
              
              canvas.create_line(*to_absolute_LEFT_MOTOR_RPM(inner_point3.real, inner_point3.imag),
                                 *to_absolute_LEFT_MOTOR_RPM(outer_point3.real, outer_point3.imag),
                                  width = MOTOR_RPM_gauge_large_tick_width,
                                  fill = MOTOR_RPM_gauge_large_tick_color)
              
              canvas.create_line(*to_absolute_RIGHT_MOTOR_RPM(inner_point3.real, inner_point3.imag),
                                 *to_absolute_RIGHT_MOTOR_RPM(outer_point3.real, outer_point3.imag),
                                  width = MOTOR_RPM_gauge_large_tick_width,
                                  fill = MOTOR_RPM_gauge_large_tick_color) 

        else:
              inner_point1 = cmath.rect(inner_tick_radius1, angle_in_radians)
              outer_point1 = cmath.rect(outer_tick_radius1, angle_in_radians)
              
              canvas.create_line(*to_absolute_LEFT_MOTOR_RPM(inner_point1.real, inner_point1.imag),
                                 *to_absolute_LEFT_MOTOR_RPM(outer_point1.real, outer_point1.imag),
                                  width = MOTOR_RPM_gauge_small_tick_width,
                                  fill = MOTOR_RPM_gauge_small_tick_color)
              
              canvas.create_line(*to_absolute_RIGHT_MOTOR_RPM(inner_point1.real, inner_point1.imag),
                                 *to_absolute_RIGHT_MOTOR_RPM(outer_point1.real, outer_point1.imag),
                                  width = MOTOR_RPM_gauge_small_tick_width,
                                  fill = MOTOR_RPM_gauge_small_tick_color)
        
        if (tick%10) == 0:
            inner_point4 = cmath.rect(inner_tick_radius4, angle_in_radians)
            outer_point4 = cmath.rect(outer_tick_radius4, angle_in_radians)
            x = outer_point4.real + canvas_x_center
            y = outer_point4.imag + canvas_y_center
            
            label = str(int(tick * MOTOR_RPM_gauge_scale_MAX_value/MOTOR_RPM_gauge_scale_division_multiplier))
            
            canvas.create_text(x - LEFT_MOTOR_RPM_gauge_x_offset,
                               y - LEFT_MOTOR_RPM_gauge_y_offset,
                               font = (MOTOR_RPM_gauge_scale_font, int(MOTOR_RPM_gauge_scale_font_size), MOTOR_RPM_gauge_scale_font_type),
                               fill = MOTOR_RPM_gauge_scale_font_color,
                               text = label)
            
            canvas.create_text(x - RIGHT_MOTOR_RPM_gauge_x_offset,
                               y - RIGHT_MOTOR_RPM_gauge_y_offset,
                               font = (MOTOR_RPM_gauge_scale_font, int(MOTOR_RPM_gauge_scale_font_size), MOTOR_RPM_gauge_scale_font_type),
                               fill = MOTOR_RPM_gauge_scale_font_color,
                               text = label)
                          
    canvas.create_text(canvas_x_center - LEFT_MOTOR_RPM_gauge_x_offset,
                       canvas_y_center - LEFT_MOTOR_RPM_gauge_y_offset - MOTOR_RPM_gauge_unit_y_offset,
                       font = (MOTOR_RPM_gauge_unit_font, int(MOTOR_RPM_gauge_unit_font_size), MOTOR_RPM_gauge_unit_font_type),
                       fill = MOTOR_RPM_gauge_unit_font_color,
                       text = LEFT_MOTOR_RPM_gauge_unit)
    
    canvas.create_text(canvas_x_center - RIGHT_MOTOR_RPM_gauge_x_offset,
                       canvas_y_center - RIGHT_MOTOR_RPM_gauge_y_offset - MOTOR_RPM_gauge_unit_y_offset,
                       font = (MOTOR_RPM_gauge_unit_font, int(MOTOR_RPM_gauge_unit_font_size), MOTOR_RPM_gauge_unit_font_type),
                       fill = MOTOR_RPM_gauge_unit_font_color,
                       text = RIGHT_MOTOR_RPM_gauge_unit) 
     
    canvas.create_arc(canvas_x_center - LEFT_MOTOR_RPM_gauge_x_offset  - MOTOR_RPM_gauge_size,
                      canvas_y_center - LEFT_MOTOR_RPM_gauge_y_offset - MOTOR_RPM_gauge_size,
                      canvas_x_center + MOTOR_RPM_gauge_size - LEFT_MOTOR_RPM_gauge_x_offset,
                      canvas_y_center - LEFT_MOTOR_RPM_gauge_y_offset + MOTOR_RPM_gauge_size,
                      style = MOTOR_RPM_gauge_outline_type,
                      width = MOTOR_RPM_gauge_outline_width,
                      start = MOTOR_RPM_gauge_outline_start,
                      extent = MOTOR_RPM_gauge_outline_extent,
                      outline = MOTOR_RPM_gauge_outline_color)
    
    canvas.create_arc(canvas_x_center - RIGHT_MOTOR_RPM_gauge_x_offset  - MOTOR_RPM_gauge_size,
                      canvas_y_center - RIGHT_MOTOR_RPM_gauge_y_offset - MOTOR_RPM_gauge_size,
                      canvas_x_center + MOTOR_RPM_gauge_size - RIGHT_MOTOR_RPM_gauge_x_offset,
                      canvas_y_center - RIGHT_MOTOR_RPM_gauge_y_offset + MOTOR_RPM_gauge_size,
                      style = MOTOR_RPM_gauge_outline_type,
                      width = MOTOR_RPM_gauge_outline_width,
                      start = MOTOR_RPM_gauge_outline_start,
                      extent = MOTOR_RPM_gauge_outline_extent,
                      outline = MOTOR_RPM_gauge_outline_color) 
    
def set_LEFT_MOTOR_RPM(LEFT_MOTOR_RPM, LEFT_CONTROLLER_VOLTAGE, LEFT_CONTROLLER_CURRENT):

    LEFT_MOTOR_RPM = LEFT_MOTOR_RPM if LEFT_MOTOR_RPM <= MOTOR_RPM_gauge_scale_MAX_value else MOTOR_RPM_gauge_scale_MAX_value
    LEFT_MOTOR_RPM = LEFT_MOTOR_RPM if LEFT_MOTOR_RPM > MOTOR_RPM_gauge_scale_MIN_value else MOTOR_RPM_gauge_scale_MIN_value
    degree = MOTOR_RPM_gauge_dial_start_degree + (LEFT_MOTOR_RPM - MOTOR_RPM_gauge_scale_MIN_value)/(MOTOR_RPM_gauge_scale_MAX_value -
             MOTOR_RPM_gauge_scale_MIN_value) * MOTOR_RPM_gauge_dial_extent
    
    xr = canvas_x_center - LEFT_MOTOR_RPM_gauge_x_offset
    yr = canvas_y_center - LEFT_MOTOR_RPM_gauge_y_offset
    angle = math.radians(-degree)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    dy = MOTOR_RPM_gauge_dial_width * sin_val
    dx = MOTOR_RPM_gauge_dial_width * cos_val
    dx2 = MOTOR_RPM_gauge_dial_length * sin_val
    dy2 = MOTOR_RPM_gauge_dial_length * cos_val
    mlx = xr + dx
    mly = yr - dy
    mrx = xr - dx
    mry = yr + dy
    px = xr + dx2
    py = yr + dy2
    xyz = mlx, mly, px, py, mrx, mry

    if LEFT_CONTROLLER_CURRENT < CONTROLLER_CURRENT_ZERO_value:
       LEFT_CONTROLLER_CURRENT_color = CONTROLLER_CURRENT_CHARGE_font_color

    if LEFT_CONTROLLER_CURRENT == CONTROLLER_CURRENT_ZERO_value:
       LEFT_CONTROLLER_CURRENT_color = CONTROLLER_CURRENT_ZERO_font_color

    if LEFT_CONTROLLER_CURRENT > CONTROLLER_CURRENT_ZERO_value:
       LEFT_CONTROLLER_CURRENT_color = CONTROLLER_CURRENT_ECO_font_color

    if LEFT_CONTROLLER_CURRENT > CONTROLLER_CURRENT_BOOST_value:
       LEFT_CONTROLLER_CURRENT_color = CONTROLLER_CURRENT_BOOST_font_color
                  
    if LEFT_CONTROLLER_VOLTAGE > VOLTAGE_MAX_value:
       LEFT_CONTROLLER_VOLTAGE_font_color = VOLTAGE_LOW_font_color
                                      
    if LEFT_CONTROLLER_VOLTAGE <= VOLTAGE_MAX_value:
       LEFT_CONTROLLER_VOLTAGE_font_color = VOLTAGE_NORMAL_font_color
                                         
    if LEFT_CONTROLLER_VOLTAGE < VOLTAGE_MID_value:
       LEFT_CONTROLLER_VOLTAGE_font_color = VOLTAGE_MID_font_color
            
    if LEFT_CONTROLLER_VOLTAGE < VOLTAGE_MIN_value:
       LEFT_CONTROLLER_VOLTAGE_font_color = VOLTAGE_LOW_font_color
     
    if LEFT_CONTROLLER_VOLTAGE <= VOLTAGE_LOW_value:
       LEFT_CONTROLLER_VOLTAGE_font_color = VOLTAGE_LOW_font_color
       
    label1 = str(LEFT_CONTROLLER_CURRENT),'A'
    label2 = LEFT_CONTROLLER_VOLTAGE, 'V'
          
    canvas.delete('LEFT_MOTOR_RPM_dial')
    
    canvas.create_polygon(xyz, fill = MOTOR_RPM_gauge_dial_color, tags = 'LEFT_MOTOR_RPM_dial')
    
    canvas.create_oval(xr - MOTOR_RPM_gauge_dial_center_size,
                       yr - MOTOR_RPM_gauge_dial_center_size + 10,
                       xr + MOTOR_RPM_gauge_dial_center_size,
                       yr + MOTOR_RPM_gauge_dial_center_size + 10,
                       fill = MOTOR_RPM_gauge_dial_center_color,
                       outline = MOTOR_RPM_gauge_dial_center_outline_color,
                       width = MOTOR_RPM_gauge_dial_center_outline_width,
                       tags = 'LEFT_MOTOR_RPM_dial')

    canvas.create_text(xr - CONTROLLER_CURRENT_x_offset,
                       yr - CONTROLLER_CURRENT_y_offset,
                       font = (CONTROLLER_CURRENT_font, int(CONTROLLER_CURRENT_font_size), CONTROLLER_CURRENT_font_type),
                       fill = LEFT_CONTROLLER_CURRENT_color,
                       text = label1,
                       tags = 'LEFT_MOTOR_RPM_dial')

    canvas.create_text(xr - CONTROLLER_VOLTAGE_x_offset,
                       yr - CONTROLLER_VOLTAGE_y_offset,
                       font = (VOLTAGE_font, int(VOLTAGE_font_size), VOLTAGE_font_type),
                       fill = LEFT_CONTROLLER_VOLTAGE_font_color,
                       text = label2,
                       tags = 'LEFT_MOTOR_RPM_dial')
   
def set_RIGHT_MOTOR_RPM(RIGHT_MOTOR_RPM, RIGHT_CONTROLLER_VOLTAGE, RIGHT_CONTROLLER_CURRENT):

    RIGHT_MOTOR_RPM = RIGHT_MOTOR_RPM if RIGHT_MOTOR_RPM <= MOTOR_RPM_gauge_scale_MAX_value else MOTOR_RPM_gauge_scale_MAX_value
    RIGHT_MOTOR_RPM = RIGHT_MOTOR_RPM if RIGHT_MOTOR_RPM > MOTOR_RPM_gauge_scale_MIN_value else MOTOR_RPM_gauge_scale_MIN_value
    degree = MOTOR_RPM_gauge_dial_start_degree + (RIGHT_MOTOR_RPM - MOTOR_RPM_gauge_scale_MIN_value)/(MOTOR_RPM_gauge_scale_MAX_value -
             MOTOR_RPM_gauge_scale_MIN_value) * MOTOR_RPM_gauge_dial_extent
    
    xr = canvas_x_center - RIGHT_MOTOR_RPM_gauge_x_offset
    yr = canvas_y_center - RIGHT_MOTOR_RPM_gauge_y_offset
    angle = math.radians(-degree)
    cos_val = math.cos(angle)
    sin_val = math.sin(angle)
    dy = MOTOR_RPM_gauge_dial_width * sin_val
    dx = MOTOR_RPM_gauge_dial_width * cos_val
    dx2 = MOTOR_RPM_gauge_dial_length * sin_val
    dy2 = MOTOR_RPM_gauge_dial_length * cos_val
    mlx = xr + dx
    mly = yr - dy
    mrx = xr - dx
    mry = yr + dy
    px = xr + dx2
    py = yr + dy2
    xyz = mlx, mly, px, py, mrx, mry

    if RIGHT_CONTROLLER_CURRENT < CONTROLLER_CURRENT_ZERO_value:
       RIGHT_CONTROLLER_CURRENT_color = CONTROLLER_CURRENT_CHARGE_font_color

    if RIGHT_CONTROLLER_CURRENT == CONTROLLER_CURRENT_ZERO_value:
       RIGHT_CONTROLLER_CURRENT_color = CONTROLLER_CURRENT_ZERO_font_color

    if RIGHT_CONTROLLER_CURRENT > CONTROLLER_CURRENT_ZERO_value:
       RIGHT_CONTROLLER_CURRENT_color = CONTROLLER_CURRENT_ECO_font_color

    if RIGHT_CONTROLLER_CURRENT > CONTROLLER_CURRENT_BOOST_value:
       RIGHT_CONTROLLER_CURRENT_color = CONTROLLER_CURRENT_BOOST_font_color
                  
    if RIGHT_CONTROLLER_VOLTAGE > VOLTAGE_MAX_value:
       RIGHT_CONTROLLER_VOLTAGE_font_color = VOLTAGE_LOW_font_color
                                      
    if RIGHT_CONTROLLER_VOLTAGE <= VOLTAGE_MAX_value:
       RIGHT_CONTROLLER_VOLTAGE_font_color = VOLTAGE_NORMAL_font_color
                                         
    if RIGHT_CONTROLLER_VOLTAGE < VOLTAGE_MID_value:
       RIGHT_CONTROLLER_VOLTAGE_font_color = VOLTAGE_MID_font_color
            
    if RIGHT_CONTROLLER_VOLTAGE < VOLTAGE_MIN_value:
       RIGHT_CONTROLLER_VOLTAGE_font_color = VOLTAGE_LOW_font_color
     
    if RIGHT_CONTROLLER_VOLTAGE <= VOLTAGE_LOW_value:
       RIGHT_CONTROLLER_VOLTAGE_font_color = VOLTAGE_LOW_font_color
       
    label1 = RIGHT_CONTROLLER_CURRENT, 'A'
    label2 = RIGHT_CONTROLLER_VOLTAGE,'V'
          
    canvas.delete('RIGHT_MOTOR_RPM_dial')
    
    canvas.create_polygon(xyz, fill = MOTOR_RPM_gauge_dial_color, tags = 'RIGHT_MOTOR_RPM_dial')
    
    canvas.create_oval(xr - MOTOR_RPM_gauge_dial_center_size,
                       yr - MOTOR_RPM_gauge_dial_center_size + 10,
                       xr + MOTOR_RPM_gauge_dial_center_size,
                       yr + MOTOR_RPM_gauge_dial_center_size + 10,
                       fill = MOTOR_RPM_gauge_dial_center_color,
                       outline = MOTOR_RPM_gauge_dial_center_outline_color,
                       width = MOTOR_RPM_gauge_dial_center_outline_width,
                       tags = 'RIGHT_MOTOR_RPM_dial')

    canvas.create_text(xr - CONTROLLER_CURRENT_x_offset,
                       yr - CONTROLLER_CURRENT_y_offset,
                       font = (CONTROLLER_CURRENT_font, int(CONTROLLER_CURRENT_font_size), CONTROLLER_CURRENT_font_type),
                       fill = RIGHT_CONTROLLER_CURRENT_color,
                       text = label1,
                       tags = 'RIGHT_MOTOR_RPM_dial')

    canvas.create_text(xr - CONTROLLER_VOLTAGE_x_offset,
                       yr - CONTROLLER_VOLTAGE_y_offset,
                       font = (VOLTAGE_font, int(VOLTAGE_font_size), VOLTAGE_font_type),
                       fill = RIGHT_CONTROLLER_VOLTAGE_font_color,
                       text = label2,
                       tags = 'RIGHT_MOTOR_RPM_dial')
    
def draw_LEFT_BATTERY():
    canvas.create_text(canvas_x_center - LEFT_BATTERY_x_offset,
                       canvas_y_center - LEFT_BATTERY_y_offset,
                       font = (BATTERY_font, int(BATTERY_font_size), BATTERY_font_type),
                       fill = BATTERY_font_color,
                       text = BATTERY_unit)
    
def draw_RIGHT_BATTERY():
    canvas.create_text(canvas_x_center - RIGHT_BATTERY_x_offset,
                       canvas_y_center - RIGHT_BATTERY_y_offset,
                       font = (BATTERY_font, int(BATTERY_font_size), BATTERY_font_type),
                       fill = BATTERY_font_color,
                       text = BATTERY_unit)
    
def set_LEFT_BATTERY(LEFT_BATTERY, LEFT_CONTROLLER_VOLTAGE):
    
    if LEFT_CONTROLLER_VOLTAGE > VOLTAGE_MAX_value:
       BATTERY_digital_font_color = VOLTAGE_LOW_font_color
       label = 100
                                    
    if LEFT_CONTROLLER_VOLTAGE <= VOLTAGE_MAX_value:
       BATTERY_digital_font_color = VOLTAGE_NORMAL_font_color
       label = LEFT_BATTERY
                                         
    if LEFT_CONTROLLER_VOLTAGE < VOLTAGE_MID_value:
       BATTERY_digital_font_color = VOLTAGE_MID_font_color
       label = LEFT_BATTERY
            
    if LEFT_CONTROLLER_VOLTAGE < VOLTAGE_MIN_value:
       BATTERY_digital_font_color = VOLTAGE_LOW_font_color
       label = LEFT_BATTERY
       
    if LEFT_CONTROLLER_VOLTAGE < VOLTAGE_LOW_value:
       BATTERY_digital_font_color = VOLTAGE_LOW_font_color
       label = 0   
       
    canvas.delete('LEFT_BATTERY')
    
    canvas.create_text(canvas_x_center - LEFT_BATTERY_digital_x_offset,
                       canvas_y_center - LEFT_BATTERY_digital_y_offset,
                       font = (BATTERY_digital_font, int(BATTERY_digital_font_size), BATTERY_digital_font_type),
                       fill = BATTERY_digital_font_color,
                       text = label,
                       tags = 'LEFT_BATTERY')
    canvas.create_text(canvas_x_center - LEFT_BATTERY_percents_x_offset,
                       canvas_y_center - LEFT_BATTERY_percents_y_offset,
                       font = (BATTERY_percents_font, int(BATTERY_percents_font_size), BATTERY_percents_font_type),
                       fill = BATTERY_digital_font_color,
                       text = BATTERY_percents,
                       tags = 'LEFT_BATTERY')
    
def set_RIGHT_BATTERY(RIGHT_BATTERY, RIGHT_CONTROLLER_VOLTAGE):
    
    if RIGHT_CONTROLLER_VOLTAGE > VOLTAGE_MAX_value:
       BATTERY_digital_font_color = VOLTAGE_LOW_font_color
       label = 100
                                    
    if RIGHT_CONTROLLER_VOLTAGE <= VOLTAGE_MAX_value:
       BATTERY_digital_font_color = VOLTAGE_NORMAL_font_color
       label = RIGHT_BATTERY
                                         
    if RIGHT_CONTROLLER_VOLTAGE < VOLTAGE_MID_value:
       BATTERY_digital_font_color = VOLTAGE_MID_font_color
       label = RIGHT_BATTERY
            
    if RIGHT_CONTROLLER_VOLTAGE < VOLTAGE_MIN_value:
       BATTERY_digital_font_color = VOLTAGE_LOW_font_color
       label = RIGHT_BATTERY
       
    if RIGHT_CONTROLLER_VOLTAGE < VOLTAGE_LOW_value:
       BATTERY_digital_font_color = VOLTAGE_LOW_font_color
       label = 0   
       
    canvas.delete('RIGHT_BATTERY')
    
    canvas.create_text(canvas_x_center - RIGHT_BATTERY_digital_x_offset,
                       canvas_y_center - RIGHT_BATTERY_digital_y_offset,
                       font = (BATTERY_digital_font, int(BATTERY_digital_font_size), BATTERY_digital_font_type),
                       fill = BATTERY_digital_font_color,
                       text = label,
                       tags = 'RIGHT_BATTERY')
    canvas.create_text(canvas_x_center - RIGHT_BATTERY_percents_x_offset,
                       canvas_y_center - RIGHT_BATTERY_percents_y_offset,
                       font = (BATTERY_percents_font, int(BATTERY_percents_font_size), BATTERY_percents_font_type),
                       fill = BATTERY_digital_font_color,
                       text = BATTERY_percents,
                       tags = 'RIGHT_BATTERY')
  
def set_LEFT_CONTROLLER_ERROR_count(LEFT_CONTROLLER_ERROR_count):
    
    if LEFT_CONTROLLER_ERROR_count == 1:
       label = LEFT_CONTROLLER_ERROR_count, 'Error'
                  
    if LEFT_CONTROLLER_ERROR_count > 1:
       label = LEFT_CONTROLLER_ERROR_count, 'Errors'
    
    canvas.delete('LEFT_CONTROLLER_ERROR_count')
    
    canvas.create_text(canvas_x_center - LEFT_CONTROLLER_ERROR_count_x_offset,
                       canvas_y_center - LEFT_CONTROLLER_ERROR_count_y_offset,
                       font = (ERROR_font, int(ERROR_font_size), ERROR_font_type),
                       fill = ERROR_font_color,
                       text = label,
                       tags = 'LEFT_CONTROLLER_ERROR_count')
    
def LEFT_CONTROLLER_ERROR_0_7_filter(LEFT_CONTROLLER_ERROR_0_7):
    
    global LEFT_CONTROLLER_ERROR_array
    
    LEFT_CONTROLLER_ERROR_array = []
    
    LEFT_CONTROLLER_ERR0 = LEFT_CONTROLLER_ERROR_0_7 & ERR_filter_0
    if LEFT_CONTROLLER_ERR0 == 1:
       LEFT_CONTROLLER_ERROR_array.append(ERR0_label)
                          
    LEFT_CONTROLLER_ERR1 = LEFT_CONTROLLER_ERROR_0_7 & ERR_filter_1
    if LEFT_CONTROLLER_ERR1 == 2:
       LEFT_CONTROLLER_ERROR_array.append(ERR1_label) 
                
    LEFT_CONTROLLER_ERR2 = LEFT_CONTROLLER_ERROR_0_7 & ERR_filter_2
    if LEFT_CONTROLLER_ERR2 == 4:
       LEFT_CONTROLLER_ERROR_array.append(ERR2_label) 
                       
    LEFT_CONTROLLER_ERR4 = LEFT_CONTROLLER_ERROR_0_7 & ERR_filter_4
    if LEFT_CONTROLLER_ERR4 == 16:
       LEFT_CONTROLLER_ERROR_array.append(ERR4_label)  
               
    LEFT_CONTROLLER_ERR5 = LEFT_CONTROLLER_ERROR_0_7 & ERR_filter_5
    if LEFT_CONTROLLER_ERR5 == 32:
       LEFT_CONTROLLER_ERROR_array.append(ERR5_label)  
              
    LEFT_CONTROLLER_ERR6 = LEFT_CONTROLLER_ERROR_0_7 & ERR_filter_6
    if LEFT_CONTROLLER_ERR6 == 64:
       LEFT_CONTROLLER_ERROR_array.append(ERR6_label)  
           
    LEFT_CONTROLLER_ERR7 = LEFT_CONTROLLER_ERROR_0_7 & ERR_filter_7
    if LEFT_CONTROLLER_ERR7 == 128:
       LEFT_CONTROLLER_ERROR_array.append(ERR7_label)  
                
def LEFT_CONTROLLER_ERROR_8_15_filter(LEFT_CONTROLLER_ERROR_8_15):
    
    global LEFT_CONTROLLER_ERROR_array
    
    LEFT_CONTROLLER_ERROR_array = []
    
    LEFT_CONTROLLER_ERR9 = LEFT_CONTROLLER_ERROR_8_15 & ERR_filter_1
    if LEFT_CONTROLLER_ERR9 == 2:
       LEFT_CONTROLLER_ERROR_array.append(ERR9_label)  
                
    LEFT_CONTROLLER_ERR10 = LEFT_CONTROLLER_ERROR_8_15 & ERR_filter_2
    if LEFT_CONTROLLER_ERR10 == 4:
       LEFT_CONTROLLER_ERROR_array.append(ERR10_label)  
             
    LEFT_CONTROLLER_ERR11 = LEFT_CONTROLLER_ERROR_8_15 & ERR_filter_3
    if LEFT_CONTROLLER_ERR11 == 8:
       LEFT_CONTROLLER_ERROR_array.append(ERR11_label)  
           
    LEFT_CONTROLLER_ERR14 = LEFT_CONTROLLER_ERROR_8_15 & ERR_filter_6
    if LEFT_CONTROLLER_ERR14 == 64:
       LEFT_CONTROLLER_ERROR_array.append(ERR14_label)  
       
    LEFT_CONTROLLER_ERR15 = LEFT_CONTROLLER_ERROR_8_15 & ERR_filter_7
    if LEFT_CONTROLLER_ERR15 == 128:
       LEFT_CONTROLLER_ERROR_array.append(ERR15_label)  
             
def show_LEFT_CONTROLLER_ERROR(LEFT_CONTROLLER_ERROR_count):
   
    global LEFT_CONTROLLER_ERR_message_No
                   
    canvas.delete('LEFT_CONTROLLER_ERROR')
     
    canvas.create_text(canvas_x_center - LEFT_CONTROLLER_ERROR_message_x_offset,
                       canvas_y_center - LEFT_CONTROLLER_ERROR_message_y_offset,
                       font = (ERROR_font, int(ERROR_font_size), ERROR_font_type),
                       fill = ERROR_font_color,
                       text = LEFT_CONTROLLER_ERROR_array[LEFT_CONTROLLER_ERR_message_No],
                       tags = 'LEFT_CONTROLLER_ERROR')
    
    LEFT_CONTROLLER_ERR_message_No += 1
        
    if LEFT_CONTROLLER_ERR_message_No < LEFT_CONTROLLER_ERROR_count:
       return
    else: 
         LEFT_CONTROLLER_ERR_message_No = 0
         return

def set_RIGHT_CONTROLLER_ERROR_count(RIGHT_CONTROLLER_ERROR_count):
    
    if RIGHT_CONTROLLER_ERROR_count == 1:
       label = RIGHT_CONTROLLER_ERROR_count, 'Error'
                  
    if RIGHT_CONTROLLER_ERROR_count > 1:
       label = RIGHT_CONTROLLER_ERROR_count, 'Errors'
    
    canvas.delete('RIGHT_CONTROLLER_ERROR_count')
    
    canvas.create_text(canvas_x_center - RIGHT_CONTROLLER_ERROR_count_x_offset,
                       canvas_y_center - RIGHT_CONTROLLER_ERROR_count_y_offset,
                       font = (ERROR_font, int(ERROR_font_size), ERROR_font_type),
                       fill = ERROR_font_color,
                       text = label,
                       tags = 'RIGHT_CONTROLLER_ERROR_count')

def RIGHT_CONTROLLER_ERROR_0_7_filter(RIGHT_CONTROLLER_ERROR_0_7):
    
    global RIGHT_CONTROLLER_ERROR_array
    
    RIGHT_CONTROLLER_ERROR_array = []
    
    RIGHT_CONTROLLER_ERR0 = RIGHT_CONTROLLER_ERROR_0_7 & ERR_filter_0
    if RIGHT_CONTROLLER_ERR0 == 1:
       RIGHT_CONTROLLER_ERROR_array.append(ERR0_label)
                          
    RIGHT_CONTROLLER_ERR1 = RIGHT_CONTROLLER_ERROR_0_7 & ERR_filter_1
    if RIGHT_CONTROLLER_ERR1 == 2:
       RIGHT_CONTROLLER_ERROR_array.append(ERR1_label) 
                
    RIGHT_CONTROLLER_ERR2 = RIGHT_CONTROLLER_ERROR_0_7 & ERR_filter_2
    if RIGHT_CONTROLLER_ERR2 == 4:
       RIGHT_CONTROLLER_ERROR_array.append(ERR2_label) 
                       
    RIGHT_CONTROLLER_ERR4 = RIGHT_CONTROLLER_ERROR_0_7 & ERR_filter_4
    if RIGHT_CONTROLLER_ERR4 == 16:
       RIGHT_CONTROLLER_ERROR_array.append(ERR4_label)  
               
    RIGHT_CONTROLLER_ERR5 = RIGHT_CONTROLLER_ERROR_0_7 & ERR_filter_5
    if RIGHT_CONTROLLER_ERR5 == 32:
       RIGHT_CONTROLLER_ERROR_array.append(ERR5_label)  
              
    RIGHT_CONTROLLER_ERR6 = RIGHT_CONTROLLER_ERROR_0_7 & ERR_filter_6
    if RIGHT_CONTROLLER_ERR6 == 64:
       RIGHT_CONTROLLER_ERROR_array.append(ERR6_label)  
           
    RIGHT_CONTROLLER_ERR7 = RIGHT_CONTROLLER_ERROR_0_7 & ERR_filter_7
    if RIGHT_CONTROLLER_ERR7 == 128:
       RIGHT_CONTROLLER_ERROR_array.append(ERR7_label)  
                
def RIGHT_CONTROLLER_ERROR_8_15_filter(RIGHT_CONTROLLER_ERROR_8_15):
    
    global RIGHT_CONTROLLER_ERROR_array
    
    RIGHT_CONTROLLER_ERROR_array = []
    
    RIGHT_CONTROLLER_ERR9 = RIGHT_CONTROLLER_ERROR_8_15 & ERR_filter_1
    if RIGHT_CONTROLLER_ERR9 == 2:
       RIGHT_CONTROLLER_ERROR_array.append(ERR9_label)  
                
    RIGHT_CONTROLLER_ERR10 = RIGHT_CONTROLLER_ERROR_8_15 & ERR_filter_2
    if RIGHT_CONTROLLER_ERR10 == 4:
       RIGHT_CONTROLLER_ERROR_array.append(ERR10_label)  
             
    RIGHT_CONTROLLER_ERR11 = RIGHT_CONTROLLER_ERROR_8_15 & ERR_filter_3
    if RIGHT_CONTROLLER_ERR11 == 8:
       RIGHT_CONTROLLER_ERROR_array.append(ERR11_label)  
           
    RIGHT_CONTROLLER_ERR14 = RIGHT_CONTROLLER_ERROR_8_15 & ERR_filter_6
    if RIGHT_CONTROLLER_ERR14 == 64:
       RIGHT_CONTROLLER_ERROR_array.append(ERR14_label)  
       
    RIGHT_CONTROLLER_ERR15 = RIGHT_CONTROLLER_ERROR_8_15 & ERR_filter_7
    if RIGHT_CONTROLLER_ERR15 == 128:
       RIGHT_CONTROLLER_ERROR_array.append(ERR15_label)

def show_RIGHT_CONTROLLER_ERROR(RIGHT_CONTROLLER_ERROR_count):
    
    global RIGHT_CONTROLLER_ERR_message_No
                   
    canvas.delete('RIGHT_CONTROLLER_ERROR')
     
    canvas.create_text(canvas_x_center - RIGHT_CONTROLLER_ERROR_message_x_offset,
                            canvas_y_center - RIGHT_CONTROLLER_ERROR_message_y_offset,
                            font = (ERROR_font, int(ERROR_font_size), ERROR_font_type),
                            fill = ERROR_font_color,
                            text = RIGHT_CONTROLLER_ERROR_array[RIGHT_CONTROLLER_ERR_message_No],
                            tags = 'RIGHT_CONTROLLER_ERROR')
    
    RIGHT_CONTROLLER_ERR_message_No += 1
        
    if RIGHT_CONTROLLER_ERR_message_No < RIGHT_CONTROLLER_ERROR_count:
       return
    else: 
         RIGHT_CONTROLLER_ERR_message_No = 0
         return
        
def set_CAN_ERROR():
    
    set_LEFT_CONTROLLER_temp(0, 0)
    set_RIGHT_CONTROLLER_temp(0, 0)
    set_LEFT_MOTOR_temp(0,0)
    set_RIGHT_MOTOR_temp(0,0)
    set_LEFT_MOTOR_RPM(0,0,0)
    set_RIGHT_MOTOR_RPM(0,0,0)
    set_LEFT_BATTERY(0,0)
    set_RIGHT_BATTERY(0,0)
            
    canvas.delete('No_CAN_data')
    canvas.delete('RIGHT_CONTROLLER_ERROR', 'RIGHT_CONTROLLER_ERROR_count')
    canvas.delete('LEFT_CONTROLLER_ERROR', 'LEFT_CONTROLLER_ERROR_count')
       
    canvas.create_text(canvas_x_center - LEFT_CONTROLLER_ERROR_count_x_offset,
                       canvas_y_center - LEFT_CONTROLLER_ERROR_count_y_offset + 30,
                       font = (ERROR_font, int(ERROR_font_size), ERROR_font_type),
                       fill = ERROR_font_color,
                       text = 'No CAN data',
                       tags = 'No_CAN_data')
    canvas.create_text(canvas_x_center - RIGHT_CONTROLLER_ERROR_count_x_offset,
                       canvas_y_center - RIGHT_CONTROLLER_ERROR_count_y_offset + 30,
                       font = (ERROR_font, int(ERROR_font_size), ERROR_font_type),
                       fill = ERROR_font_color,
                       text = 'No CAN data',
                       tags = 'No_CAN_data')
    return
                        
def draw_WATER_PUMP():
    label = 'WATER PUMP'
    label1 = 'ON'
    
    canvas.delete('WATER_PUMP')
    
    canvas.create_text(canvas_x_center - WATER_PUMP_x_offset,
                       canvas_y_center - WATER_PUMP_y_offset,
                       font = (WATER_PUMP_font, int(WATER_PUMP_font_size), WATER_PUMP_font_type),
                       fill = WATER_PUMP_font_color,
                       text = label,
                       tags = 'WATER_PUMP')
    canvas.create_text(canvas_x_center - ON_x_offset,
                       canvas_y_center - ON_y_offset,
                       font = (ON_font, int(ON_font_size), ON_font_type),
                       fill = ON_font_color,
                       text = label1,
                       tags = 'WATER_PUMP') 


def to_absolute_LEFT_CONTROLLER_temp(x, y):
    return x + canvas_x_center - LEFT_CONTROLLER_temp_gauge_x_offset, y + canvas_y_center - LEFT_CONTROLLER_temp_gauge_y_offset

def to_absolute_RIGHT_CONTROLLER_temp(x, y):
    return x + canvas_x_center - RIGHT_CONTROLLER_temp_gauge_x_offset, y + canvas_y_center - RIGHT_CONTROLLER_temp_gauge_y_offset

def to_absolute_LEFT_MOTOR_temp(x, y):
    return x + canvas_x_center - LEFT_MOTOR_temp_gauge_x_offset, y + canvas_y_center - LEFT_MOTOR_temp_gauge_y_offset

def to_absolute_RIGHT_MOTOR_temp(x, y):
    return x + canvas_x_center - RIGHT_MOTOR_temp_gauge_x_offset, y + canvas_y_center - RIGHT_MOTOR_temp_gauge_y_offset

def to_absolute_LEFT_MOTOR_RPM(x, y):
    return x + canvas_x_center - LEFT_MOTOR_RPM_gauge_x_offset, y + canvas_y_center - LEFT_MOTOR_RPM_gauge_y_offset

def to_absolute_RIGHT_MOTOR_RPM(x, y):
    return x + canvas_x_center - RIGHT_MOTOR_RPM_gauge_x_offset, y + canvas_y_center - RIGHT_MOTOR_RPM_gauge_y_offset

time_count = 0
message = 0
#Water_Pump = LED(14)

LEFT_CONTROLLER_CURRENT_MSB = 0
LEFT_CONTROLLER_CURRENT_LSB = 0
LEFT_CONTROLLER_CURRENT_HEX = 0
LEFT_CONTROLLER_CURRENT_DEC = 0
LEFT_CONTROLLER_CURRENT = 0
LEFT_CONTROLLER_CURRENT_unstable = 0
LEFT_CONTROLLER_temp = 0
LEFT_CONTROLLER_temp_digital = LEFT_CONTROLLER_temp
LEFT_MOTOR_temp = 0
LEFT_MOTOR_temp_digital = LEFT_MOTOR_temp
LEFT_MOTOR_RPM = 0
LEFT_CONTROLLER_ERROR_0_7 = 0
LEFT_CONTROLLER_ERROR_8_15 = 0
LEFT_CONTROLLER_ERROR_0_7_count = 0
LEFT_CONTROLLER_ERROR_8_15_count = 0
LEFT_CONTROLLER_ERROR_count = 0
LEFT_CONTROLLER_ERR_message_No = 0
LEFT_CONTROLLER_VOLTAGE = 0

RIGHT_CONTROLLER_CURRENT_MSB = 0
RIGHT_CONTROLLER_CURRENT_LSB = 0
RIGHT_CONTROLLER_CURRENT_HEX = 0
RIGHT_CONTROLLER_CURRENT_DEC = 0
RIGHT_CONTROLLER_CURRENT = 0
RIGHT_CONTROLLER_CURRENT_unstable = 0
RIGHT_CONTROLLER_temp = 0
RIGHT_CONTROLLER_temp_digital = RIGHT_CONTROLLER_temp
RIGHT_MOTOR_temp = 0
RIGHT_MOTOR_temp_digital = RIGHT_MOTOR_temp
RIGHT_MOTOR_RPM = 0
RIGHT_CONTROLLER_ERROR_0_7 = 0
RIGHT_CONTROLLER_ERROR_8_15 = 0
RIGHT_CONTROLLER_ERROR_0_7_count = 0
RIGHT_CONTROLLER_ERROR_8_15_count = 0
RIGHT_CONTROLLER_ERROR_count = 0
RIGHT_CONTROLLER_ERR_message_No = 0
RIGHT_CONTROLLER_VOLTAGE = 0

#can_interface = 'can0'
#bus = can.interface.Bus(can_interface, bustype='socketcan') 

def main():

    
    global time_count
    global message
    
    global LEFT_CONTROLLER_CURRENT
    global LEFT_CONTROLLER_CURRENT_unstable
    global LEFT_CONTROLLER_temp
    global LEFT_CONTROLLER_temp_digital
    global LEFT_MOTOR_temp
    global LEFT_MOTOR_temp_digital
    global LEFT_MOTOR_RPM
    global LEFT_CONTROLLER_ERROR_0_7
    global LEFT_CONTROLLER_ERROR_8_15
    global LEFT_CONTROLLER_ERROR_0_7_count
    global LEFT_CONTROLLER_ERROR_8_15_count
    global LEFT_CONTROLLER_ERROR_count
    global LEFT_CONTROLLER_ERROR_array
    global LEFT_CONTROLLER_ERR_message_No
    global LEFT_CONTROLLER_VOLTAGE
    global LEFT_BATTERY_digital
    
    global RIGHT_CONTROLLER_CURRENT
    global RIGHT_CONTROLLER_CURRENT_unstable
    global RIGHT_CONTROLLER_temp
    global RIGHT_CONTROLLER_temp_digital
    global RIGHT_MOTOR_temp
    global RIGHT_MOTOR_temp_digital
    global RIGHT_MOTOR_RPM
    global RIGHT_CONTROLLER_ERROR_0_7
    global RIGHT_CONTROLLER_ERROR_8_15
    global RIGHT_CONTROLLER_ERROR_0_7_count
    global RIGHT_CONTROLLER_ERROR_8_15_count
    global RIGHT_CONTROLLER_ERROR_count
    global RIGHT_CONTROLLER_ERR_message_No
    global RIGHT_CONTROLLER_VOLTAGE
    global RIGHT_BATTERY_digital
        
    message = random.randint(0,100)


    LEFT_CONTROLLER_CURRENT = random.randint(0,25)



    RIGHT_CONTROLLER_CURRENT = random.randint(0,25)
    LEFT_MOTOR_RPM = random.randint(500,3000)
    RIGHT_MOTOR_RPM = random.randint(500,3000)
    LEFT_CONTROLLER_temp_digital = LEFT_CONTROLLER_temp
    RIGHT_CONTROLLER_temp_digital = RIGHT_CONTROLLER_temp
    LEFT_MOTOR_temp_digital = LEFT_MOTOR_temp
    RIGHT_MOTOR_temp_digital = RIGHT_MOTOR_temp
    LEFT_CONTROLLER_VOLTAGE = random.randint(10,20)
    RIGHT_CONTROLLER_VOLTAGE = random.randint(10,20)

    LEFT_BATTERY = int(100 - (50.4 - LEFT_CONTROLLER_VOLTAGE) * 11.9)
    set_LEFT_BATTERY(LEFT_BATTERY, LEFT_CONTROLLER_VOLTAGE)
    
    RIGHT_BATTERY = int(100 - (50.4 - RIGHT_CONTROLLER_VOLTAGE) * 11.9)
    set_RIGHT_BATTERY(RIGHT_BATTERY, RIGHT_CONTROLLER_VOLTAGE)
    
    if LEFT_MOTOR_temp > 75:
       #Water_Pump.on()
       draw_WATER_PUMP()
       
    if RIGHT_MOTOR_temp > 75:
       #Water_Pump.on()
       draw_WATER_PUMP()
       
    if LEFT_MOTOR_temp < 60:
       if RIGHT_MOTOR_temp < 60:
          #Water_Pump.off()
          canvas.delete('WATER_PUMP')


    time_count +=1
    if (time_count%sampling_ratio) == 0:
    	# Dynamics
    	# Threading 
    	t1 = threading.Thread(target=set_LEFT_CONTROLLER_temp, args=(LEFT_CONTROLLER_temp, LEFT_CONTROLLER_temp_digital,))
    	t2 = threading.Thread(target=set_RIGHT_CONTROLLER_temp, args=(RIGHT_CONTROLLER_temp, RIGHT_CONTROLLER_temp_digital,))
    	t3 = threading.Thread(target=set_LEFT_MOTOR_temp, args=(LEFT_MOTOR_temp, LEFT_MOTOR_temp_digital,))
    	t4 = threading.Thread(target=set_RIGHT_MOTOR_temp, args=(RIGHT_MOTOR_temp, RIGHT_MOTOR_temp_digital,))
    	t5 = threading.Thread(target=set_LEFT_MOTOR_RPM, args=(LEFT_MOTOR_RPM, LEFT_CONTROLLER_VOLTAGE, LEFT_CONTROLLER_CURRENT,))
    	t6 = threading.Thread(target=set_RIGHT_MOTOR_RPM, args=(RIGHT_MOTOR_RPM, RIGHT_CONTROLLER_VOLTAGE, RIGHT_CONTROLLER_CURRENT,))

    	#  Start Threading
    	t1.start()
    	t2.start()
    	t3.start()
    	t4.start()
    	t5.start()
    	t6.start()


    """
    time_count +=1
    
    if message is None:
       
       set_CAN_ERROR()
       
    else:
         canvas.delete('No_CAN_data')
         
               
         if message.arbitration_id == 0x065:
                        
            LEFT_CONTROLLER_CURRENT_MSB = hex(message.data[2])[2:].zfill(2)
            LEFT_CONTROLLER_CURRENT_LSB = hex(message.data[1])[2:].zfill(2)
                         
            LEFT_CONTROLLER_CURRENT_HEX = "%s%s" % (LEFT_CONTROLLER_CURRENT_MSB, LEFT_CONTROLLER_CURRENT_LSB)
            LEFT_CONTROLLER_CURRENT_DEC = int(str(LEFT_CONTROLLER_CURRENT_HEX), 16)
            #LEFT_CONTROLLER_CURRENT_unstable = int((LEFT_CONTROLLER_CURRENT_DEC - 2039) * -0.165) #320A
            LEFT_CONTROLLER_CURRENT_unstable = int((LEFT_CONTROLLER_CURRENT_DEC - 2041) * -0.22) #450A
            
            if LEFT_CONTROLLER_CURRENT_unstable > -1:
               if LEFT_CONTROLLER_CURRENT_unstable < 1:
                  LEFT_CONTROLLER_CURRENT = 0
               else:
                   LEFT_CONTROLLER_CURRENT = LEFT_CONTROLLER_CURRENT_unstable   
            else:
                 LEFT_CONTROLLER_CURRENT = LEFT_CONTROLLER_CURRENT_unstable      
                              
         if message.arbitration_id == 0x066:
             
            RIGHT_CONTROLLER_CURRENT_MSB = hex(message.data[2])[2:].zfill(2)
            RIGHT_CONTROLLER_CURRENT_LSB = hex(message.data[1])[2:].zfill(2)
                 
            RIGHT_CONTROLLER_CURRENT_HEX = "%s%s" % (RIGHT_CONTROLLER_CURRENT_MSB, RIGHT_CONTROLLER_CURRENT_LSB)
            RIGHT_CONTROLLER_CURRENT_DEC = int(str(RIGHT_CONTROLLER_CURRENT_HEX), 16)
            #RIGHT_CONTROLLER_CURRENT_unstable = int((RIGHT_CONTROLLER_CURRENT_DEC - 2134) * -0.165) #320A 2039
            RIGHT_CONTROLLER_CURRENT_unstable = int((RIGHT_CONTROLLER_CURRENT_DEC - 2059) * -0.22) #450A
            
            if RIGHT_CONTROLLER_CURRENT_unstable > -1:
               if RIGHT_CONTROLLER_CURRENT_unstable < 1:
                  RIGHT_CONTROLLER_CURRENT = 0
               else:
                   RIGHT_CONTROLLER_CURRENT = RIGHT_CONTROLLER_CURRENT_unstable   
            else:
                 RIGHT_CONTROLLER_CURRENT = RIGHT_CONTROLLER_CURRENT_unstable
                             
         if message.arbitration_id == 0x0cf11e05:
                     
            if (time_count%30) == 0:
                           
               LEFT_CONTROLLER_ERROR_0_7 = message.data[6]
               LEFT_CONTROLLER_ERROR_8_15 = message.data[7]
               LEFT_MOTOR_RPM = int(message.data[1] * 256 + message.data[0])
               LEFT_CONTROLLER_VOLTAGE = int((message.data[5] * 256 + message.data[4])/10)
               set_LEFT_MOTOR_RPM(LEFT_MOTOR_RPM, LEFT_CONTROLLER_VOLTAGE, LEFT_CONTROLLER_CURRENT) 
               
               if LEFT_CONTROLLER_ERROR_0_7 > 0:
                  LEFT_CONTROLLER_ERROR_0_7_in_binary = bin(LEFT_CONTROLLER_ERROR_0_7) 
                  setBits = [ones for ones in LEFT_CONTROLLER_ERROR_0_7_in_binary[2:] if ones=='1']  
                  LEFT_CONTROLLER_ERROR_0_7_count = (len(setBits))
                  LEFT_CONTROLLER_ERROR_0_7_filter(LEFT_CONTROLLER_ERROR_0_7)
                  
               else:
                    LEFT_CONTROLLER_ERROR_0_7_count = 0
                   
               if LEFT_CONTROLLER_ERROR_8_15 > 0:
                  LEFT_CONTROLLER_ERROR_8_15_in_binary = bin(LEFT_CONTROLLER_ERROR_8_15)
                  setBits = [ones for ones in LEFT_CONTROLLER_ERROR_8_15_in_binary[2:] if ones=='1'] 
                  LEFT_CONTROLLER_ERROR_8_15_count = (len(setBits))
                  LEFT_CONTROLLER_ERROR_8_15_filter(LEFT_CONTROLLER_ERROR_8_15)
                  
               else:
                    LEFT_CONTROLLER_ERROR_8_15_count = 0
                
               LEFT_CONTROLLER_ERROR_count = LEFT_CONTROLLER_ERROR_0_7_count + LEFT_CONTROLLER_ERROR_8_15_count
               
               if LEFT_CONTROLLER_ERROR_count > 0:
                  set_LEFT_CONTROLLER_ERROR_count(LEFT_CONTROLLER_ERROR_count)
                  show_LEFT_CONTROLLER_ERROR(LEFT_CONTROLLER_ERROR_count)
                                   
               else:
                    canvas.delete('LEFT_CONTROLLER_ERROR', 'LEFT_CONTROLLER_ERROR_count')                 
            else:
                 LEFT_MOTOR_RPM = int(message.data[1] * 256 + message.data[0])
                 set_LEFT_MOTOR_RPM(LEFT_MOTOR_RPM, LEFT_CONTROLLER_VOLTAGE, LEFT_CONTROLLER_CURRENT)  
                   
         if message.arbitration_id == 0x0cf11e06:
                     
            if (time_count%30) == 0:
                           
               RIGHT_CONTROLLER_ERROR_0_7 = message.data[6]
               RIGHT_CONTROLLER_ERROR_8_15 = message.data[7]
               RIGHT_MOTOR_RPM = int(message.data[1] * 256 + message.data[0])
               RIGHT_CONTROLLER_VOLTAGE = int((message.data[5] * 256 + message.data[4])/10)
               set_RIGHT_MOTOR_RPM(RIGHT_MOTOR_RPM, RIGHT_CONTROLLER_VOLTAGE, RIGHT_CONTROLLER_CURRENT)

               if RIGHT_CONTROLLER_ERROR_0_7 > 0:
                  RIGHT_CONTROLLER_ERROR_0_7_in_binary = bin(RIGHT_CONTROLLER_ERROR_0_7) 
                  setBits = [ones for ones in RIGHT_CONTROLLER_ERROR_0_7_in_binary[2:] if ones=='1']  
                  RIGHT_CONTROLLER_ERROR_0_7_count = (len(setBits))
                  RIGHT_CONTROLLER_ERROR_0_7_filter(RIGHT_CONTROLLER_ERROR_0_7)
       
               else:
                    RIGHT_CONTROLLER_ERROR_0_7_count = 0
                   
               if RIGHT_CONTROLLER_ERROR_8_15 > 0:
                  RIGHT_CONTROLLER_ERROR_8_15_in_binary = bin(RIGHT_CONTROLLER_ERROR_8_15)
                  setBits = [ones for ones in RIGHT_CONTROLLER_ERROR_8_15_in_binary[2:] if ones=='1'] 
                  RIGHT_CONTROLLER_ERROR_8_15_count = (len(setBits))
                  RIGHT_CONTROLLER_ERROR_8_15_filter(RIGHT_CONTROLLER_ERROR_8_15)
      
               else:
                    RIGHT_CONTROLLER_ERROR_8_15_count = 0
                
               RIGHT_CONTROLLER_ERROR_count = RIGHT_CONTROLLER_ERROR_0_7_count + RIGHT_CONTROLLER_ERROR_8_15_count
               
               if RIGHT_CONTROLLER_ERROR_count > 0:
                  set_RIGHT_CONTROLLER_ERROR_count(RIGHT_CONTROLLER_ERROR_count)
                  show_RIGHT_CONTROLLER_ERROR(RIGHT_CONTROLLER_ERROR_count)
                                     
               else:
                    canvas.delete('RIGHT_CONTROLLER_ERROR', 'RIGHT_CONTROLLER_ERROR_count')
                  
            else:
                 RIGHT_MOTOR_RPM = int(message.data[1] * 256 + message.data[0])
                 set_RIGHT_MOTOR_RPM(RIGHT_MOTOR_RPM, RIGHT_CONTROLLER_VOLTAGE, RIGHT_CONTROLLER_CURRENT) 
                                      
         if message.arbitration_id == 0x0cf11f05:
       
            if (time_count%30) == 0:
               LEFT_CONTROLLER_temp = message.data[1] - 40
               LEFT_MOTOR_temp = message.data[2] - 30
               LEFT_CONTROLLER_temp_digital = LEFT_CONTROLLER_temp 
               LEFT_MOTOR_temp_digital = LEFT_MOTOR_temp
                  
               set_LEFT_CONTROLLER_temp(LEFT_CONTROLLER_temp, LEFT_CONTROLLER_temp_digital)
               set_LEFT_MOTOR_temp(LEFT_MOTOR_temp, LEFT_MOTOR_temp_digital)
              
         if message.arbitration_id == 0x0cf11f06:
       
            if (time_count%30) == 0:
               RIGHT_CONTROLLER_temp = message.data[1] - 40
               RIGHT_MOTOR_temp = message.data[2] - 30
               RIGHT_CONTROLLER_temp_digital = RIGHT_CONTROLLER_temp 
               RIGHT_MOTOR_temp_digital = RIGHT_MOTOR_temp
                  
               set_RIGHT_CONTROLLER_temp(RIGHT_CONTROLLER_temp, RIGHT_CONTROLLER_temp_digital)
               set_RIGHT_MOTOR_temp(RIGHT_MOTOR_temp, RIGHT_MOTOR_temp_digital)
        """






    win.after(1, main)

# stationary

draw_CONTROLLER_temp_gauge()
draw_MOTOR_temp_gauge()
draw_MOTOR_RPM_gauge()
draw_LEFT_BATTERY()
draw_RIGHT_BATTERY()



main()

mainloop()
