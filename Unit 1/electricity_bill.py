print ("========== ELECTRICITY BILL GENERATOR")
consumer_name = input("enter consumer name:")
consumer_id = input("enter consumer id:")
previous_reading = float(input("enter previous meter reading (kWh):"))
current_reading = float(input("enter current meter reading (kWh) :"))
cost_per_unit = float(input("enter cost per unit : "))
units = current_reading - previous_reading
energy_charge = units * cost_per_unit
electricity_duty = energy_charge * 0.05
fixed_charge = 100
net_bill = energy_charge + electricity_duty + fixed_charge


print("\n============ ELECTRICITY BILL ===========")
print(f"Consumer Name :{consumer_name}")
print(f"Consumer ID : {consumer_id}")
print(f"Units Consumed : {units:.2f}kWh")
print(f"Energy charge : {energy_charge}")
print(f"Electricity Duty(%5) : {electricity_duty:.2f}")
print(f"Fixed Meter Charge : {fixed_charge:.2f}")
print("-----------------------")
print(f"Net Bill Amount : {net_bill:.2f}")
print("=======================")

