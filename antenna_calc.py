def calculate_quarter_wavelength(frequency, unit):
    c = 3 * 10**8
    
    if unit.lower() == "hz":
        frequency *= 1
    elif unit.lower() == "khz":
        frequency *= 10**3
    elif unit.lower() == "mhz":
        frequency *= 10**6
    elif unit.lower() == "ghz":
        frequency *= 10**9
    else:
        raise ValueError("Invalid unit. Please enter Hz, kHz, MHz, or GHz.")
    
    wavelength = c / frequency
    
    quarter_wavelength_meters = wavelength / 4
    
    quarter_wavelength_cm = quarter_wavelength_meters * 100
    quarter_wavelength_mm = quarter_wavelength_meters * 1000
    
    return quarter_wavelength_meters, quarter_wavelength_cm, quarter_wavelength_mm


def main():
    try:
        frequency = float(input("Enter the frequency: "))
        unit = input("Enter the unit (Hz, kHz, MHz, GHz):")
        

        quarter_wavelength_meters, quarter_wavelength_cm, quarter_wavelength_mm = calculate_quarter_wavelength(frequency, unit)
        

        print(f"\n\nFull wavelength: {quarter_wavelength_meters*4:.6f} meters")
        print(f"Full wavelength: {quarter_wavelength_cm*4:.6f} centimeters")
        print(f"Full wavelength: {quarter_wavelength_mm*4:.6f} millimeters \n\n")
        print(f"Half wavelength: {quarter_wavelength_meters*2:.6f} meters")
        print(f"Half wavelength: {quarter_wavelength_cm*2:.6f} centimeters")
        print(f"Half wavelength: {quarter_wavelength_mm*2:.6f} millimeters \n\n")
        print(f"Quarter wavelength: {quarter_wavelength_meters:.6f} meters")
        print(f"Quarter wavelength: {quarter_wavelength_cm:.6f} centimeters")
        print(f"Quarter wavelength: {quarter_wavelength_mm:.6f} millimeters")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
