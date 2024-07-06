import csv

with open('household_power_consumption.txt', 'r') as in_file:
    lines = [line.strip().split(';') for line in in_file if line.strip()]
    with open('log.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['Date', 'Time', 'Global_active_power', 'Global_reactive_power', 'Voltage', 'Global_intensity', 'Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'])
        writer.writerows(lines)
