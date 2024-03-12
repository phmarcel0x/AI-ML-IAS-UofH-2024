# IAS Practical 6 - March 12 2024
# Daisyworld Model: Pseudocode

# FOR all solar intesities:     
    # WHILE change_in_world_temp < convergence_threshold:
        # world_albedo 
        #  - % wd_surface * wd_albedo
        #  - % bd_surface * bd_albedo
        #  - % barren_surface = (1 - white - black) * barren_albedo

        # world_temp
        #  - sun_intensity
        #  - world_albedo
        #  - some fancy math

        # wd_growth
        #  - (ideal_world_temp - world_temp)
        #  - % wd_surface
        #  - % barren_surface = (1 - white - black)
        #  - wd_albedo
        #  - wd_death_rate
        #  - Example function: wd_growth = 1 - 0.003265 * (temp_daisy_ideal - temp_white)**2
        #  - Homeostasis happens at [temp_daisy_ideal - temp_white]

        # bd_growth
        #  - (ideal_world_temp - world_temp)
        #  - % bd_surface
        #  - % barren_surface = (1 - white - black)
        #  - bd_albedo
        #  - bd_death_rate
        #  - Example function: bd_growth = 1 - 0.003265 * (temp_daisy_ideal - temp_black)**2
        #  - Homeostasis happens at [temp_daisy_ideal - temp_black]