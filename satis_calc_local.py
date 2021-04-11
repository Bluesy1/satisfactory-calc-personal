# print('Initializing')
import pandas as pd
import numpy as np
import time
import sys
save_location = ""
# an example location would be something like this for wsl ubuntu( you want it to save to the folder that you've probably got this script saved to, so you know it has the appropriate write permissions): /mnt/c/Users/(username)/Documents/GitHub/satisfactory-calc-personal/Calculator_Output.csv
# the /Calculator_Output.csv will be the file name (Calculator_Output.csv) you an change the name if you want it named differently, but not the extension part (.csv) 
# for windows, the save_location would be like as follows: C:\Users\<username>\Documents\GitHub\satisfactory-calc-personal\Calculator_Output.csv
recipes_url = 'https://raw.githubusercontent.com/JazzManToo/satisfactory-calc-personal/main/Data/Satisfactory%20every%20recipe.csv'
print('will attempt to save CSV (output) to:',save_location)
val = str(input('Is that okay? (y/n)'))

table = pd.read_csv(recipes_url, index_col= 'Recipe')
table2 = pd.DataFrame()
def craft(item, recipe, Target, In1, In2, In3, In4, By1):
    if isinstance(Target,float):
        x = Target / float(table.loc[recipe, item])
    else:
        x = float(Target[0]) / float(table.loc[recipe, item])
    In1_Target = 0 
    In2_Target = 0
    In3_Target = 0
    In4_Target = 0 
    By1_Target = 0
    # print(Target, '\n spacer\n Type:', type(Target), '\n spacer')
    # print(float(table.loc[recipe, item]), '\n spacer Type:', type(float(table.loc[recipe, item])), '\n spacer')
    if In1 != None:
      In1_Target = x * abs(table.loc[recipe, In1])
      if In1 in Target_Resources:
        Target_Resources.remove(In1)
      Target_Resources.append(In1)
    if In2 != None:
      In2_Target = x * abs(table.loc[recipe, In2])
      if In2 in Target_Resources:
        Target_Resources.remove(In2)
      Target_Resources.append(In2)
    if In3 != None:
      In3_Target = x * abs(table.loc[recipe, In3])
      if In3 in Target_Resources:
        Target_Resources.remove(In3)
      Target_Resources.append(In3)
    if In4 != None:
      In4_Target = x * abs(table.loc[recipe, In4])
      if In4 in Target_Resources:
        Target_Resources.remove(In4)
      Target_Resources.append(In4) 
    if By1 != None:
      By1_Target = x * abs(table.loc[recipe, By1])
      if By1 in Byproducts:
        Byproducts.remove(By1)
      Byproducts.append(By1)
    # if CSV_Output:
    resultsDict = {'Recipe': recipe, 'Building': table.loc[recipe, 'Building'], 'Amount of Buliding(s)': x, 'Input 1': In1, 'Amount of Input 1': In1_Target, 'Input 2': In2, 'Amount of Input 2': In2_Target, 'Input 3': In3, 'Amount of Input 3': In3_Target, 'Input 4': In4, 'Amount of Input 4': In4_Target, 'Byproduct': By1, 'Amount of Byproduct': By1_Target}
    resultstable = pd.DataFrame(resultsDict, index= ['Recipe', 'Building', 'AmountofBuliding(s)', 'Input1', 'AmountofInput1', 'Input2', 'AmountofInput2', 'Input3', 'AmountofInput3', 'Input4', 'AmountofInput4', 'Byproduct', 'AmountofByproduct'])
    resultstable = resultstable.iloc[[0]]
    print(item, ': ', round(x, 2), resultstable.loc['Recipe', 'Building'], '(s)\nRecipe:', recipe)
    # print(resultstable)
    return resultstable
if val == "y":
    print('Great, Starting now')
elif val == 'n':
    print('Quitting program, please update string on line 6 (save_location) with the proper string')
    time.sleep(1)
    quit()
valid_inputs = ["Adaptive_Control_Unit", "AI_Limiter", "Alclad_Aluminum_Sheet",  "Alumina_Solution", "Aluminum_Casing", "Aluminum_Ingot", "Aluminum_Scrap", "Assembly_Director_System", "Automated_Wiring", "Battery", "Beacon", "Biomass", "Black_Powder", "Cable", "Caterium_Ingot", "Caterium_Ore", "Circuit_Board", "Coal", "Color_Cartridge", "Compacted_Coal", "Computer", "Concrete", "Cooling_System", "Copper_Ingot", "Copper_Powder", "Copper_Sheet",  "Crystal_Oscillator", "Electromagnetic_Control_Rod", "Empty_Canister", "Empty_Fluid_Tank", "Encased_Industrial_Beam", "Encased_Plutonium_Cell", "Encased_Uranium_Cell", "Fabric", "Flower_Petals", "Fuel", "Fused_Modular_Frame", "Gas_Filter", "Heat_Sink", "Heavy_Modular_Frame", "Heavy_Oil_Residue", "High_Speed_Connector", "Iodine_Infused_Filter", "Iron_Ingot", "Iron_Plate", "Iron_Rod", "Liquid_Biofuel", "Magnetic_Field_Generator", "Modular_Engine", "Modular_Frame", "Motor", "Mycelia", "Nitric_Acid", "Nitrogen_Gas", "Nobelisk", "Non_Fissile_Uranium", "Nuclear_Fuel_Rod", "Nuclear_Pasta", "Nuclear_Waste", "Packaged_Alumina_Solution", "Packaged_Fuel", "Packaged_Heavy_Oil_Residue", "Packaged_Liquid_Biofuel", "Packaged_Nitric_Acid", "Packaged_Nitrogen_Gas", "Packaged_Oil", "Packaged_Sulfuric_Acid", "Packaged_Turbofuel", "Packaged_Water", "Petroleum_Coke", "Plastic", "Plutonium_Fuel_Rod", "Plutonium_Pellets", "Plutonium_Waste", "Polymer_Resin", "Pressure_Conversion_Cube", "Quartz_Crystal", "Quickwire", "Radio_Control_Unit", "Reinforced_Iron_Plate", "Rifle_Cartridge", "Rotor", "Rubber", "Screw", "Silica", "Smart_Plating", "Solid_Biofuel", "Spiked_Rebar", "Stator", "Steel_Beam", "Steel_Ingot", "Steel_Pipe", "Sulfuric_Acid", "Supercomputer", "Thermal_Propulsion_Rocket", "Turbo_Motor", "Turbofuel", "Versatile_Framework", "Wire"]
n = 0
while n < len(valid_inputs):
    print('Is your target', valid_inputs[n], '?')
    target_set = str(input('y/n:'))
    if target_set == 'y':
       Target_Resource = valid_inputs[n]
       break
    n += 1
try:
    Target_Resource_Amount = float(input('Target amount?'))
except ValueError:
    sys.exit('Error: Target amount must be a positive number, with no letters')
ACU_Target = 0
AIL_Target = 0
AAS_Target = 0 
Alien_Carapace_Target = 0 
AS_Target = 0 
AC_Target = 0 
AI_Target = 0 
Alien_Organs_Target = 0 
ASc_Target = 0 
ADS_Target = 0 
AW_Target = 0 
Battery_Target = 0 
Bauxite_Target = 0 
Beacon_Target = 0 
Biomass_Target = 0 
BP_Target = 0 
Cable_Target = 0 
CopI_Target = 0 
Caterium_Ore_Target = 0 
CB_Target = 0 
Coal_Target = 0 
Color_Cartridge_Target = 0 
Compacted_Coal_Target = 0 
Computer_Target = 0 
Concrete_Target = 0 
CSys_Target = 0 
CatI_Target = 0 
Copper_Ore_Target = 0 
CPow_Target = 0 #totally didn't almost accidentally name this var CP_Target lol
CSheet_Target = 0 
Crude_Oil_Target = 0 
COsc_Target = 0 
ECR_Target = 0 
EC_Target = 0 
EFT_Target = 0 
EIB_Target = 0 
EPC_Target = 0 
EUC_Target = 0 
Fabric_Target = 0 
Flower_Petals_Target = 0 
Fuel_Target = 0 
FMF_Target = 0 
GF_Target = 0 
HS_Target = 0 
HMF_Target = 0 
HOR_Target = 0 
HSC_Target = 0 
IIF_Target = 0 
II_Target = 0 
Iron_Ore_Target = 0 
IP_Target = 0 
IR_Target = 0 
Leaves_Target = 0 
Limestone_Target = 0 
LB_Target = 0 
MFG_Target = 0 
ME_Target = 0 
MF_Target = 0 
Motor_Target = 0 
Mycelia_Target = 0 
NA_Target = 0 
Nitrogen_Gas_Target = 0 
Nobelisk_Target = 0 
NFU_Target = 0 
NFR_Target = 0 
NP_Target = 0 
NW_Target = 0 
PAS_Target = 0 
PF_Target = 0 
PHOR_Target = 0 
PLB_Target = 0 
PNA_Target = 0 
PNG_Target = 0 
PO_Target = 0 
PSA_Target = 0 
PT_Target = 0 
PW_Target = 0 
PC_Target = 0 
Plastic_Target = 0 
PFR_Target = 0 
PP_Target = 0 
PW_Target = 0 
PR_Target = 0 
PCC_Target = 0 
QCrystal_Target = 0 
Quickwire_Target = 0 
RCU_Target = 0 
Raw_Quartz_Target = 0 
RIP_Target = 0 
RC_Target = 0 
Rotor_Target = 0 
Rubber_Target = 0 
Screw_Target = 0 
Silica_Target = 0 
SP_Target = 0 
SB_Target = 0 
SR_Target = 0 
Stator_Target = 0 
SB_Target = 0 
SI_Target = 0 
SP_Target = 0 
Sulfur_Target = 0 
SA_Target = 0 
Supercomputer_Target = 0 
SO_Target = 0 
TPR_Target = 0 
TM_Target = 0 
Turbofuel_Target = 0 
Uranium_Target = 0 
VF_Target = 0
Water_Target = 0 
Wire_Target = 0 
Wood_Target = 0
Inputs = []
Byproducts = []
Target_Resources = []
Target_Resources.append(Target_Resource)
print('Target:', Target_Resource, 'at', Target_Resource_Amount, 'per minute')
for y in Target_Resources:
    print("\n")
    if y == "Adaptive_Control_Unit":
        if y == Target_Resource:
          ACU_Target = Target_Resource_Amount
        results = craft(y, 'Adaptive_Control_Unit', ACU_Target, 'Automated_Wiring', 'Circuit_Board', 'Heavy_Modular_Frame', 'Computer', None)
        AW_Target += results['Amount of Input 1']
        CB_Target += results['Amount of Input 2']
        HMF_Target += results['Amount of Input 3']
        Computer_Target += results['Amount of Input 4']
        ACU_Target = 0
    elif y == "AI_Limiter": 
        if y == Target_Resource:
          AIL_Target = Target_Resource_Amount
        results = craft(y, 'AI_Limiter', AIL_Target, 'Copper_Sheet', 'Quickwire', None, None, None)
        CSheet_Target += results['Amount of Input 1']
        QW_Target += results['Amount of Input 2']
        z = 0
        AIL_Target = 0
    elif y == "Alclad_Aluminum_Sheet": 
        if y == Target_Resource:
          AAS_Target = Target_Resource_Amount
        results = craft(y, 'Alclad_Aluminum_Sheet', AAS_Target, 'Aluminum_Ingot', 'Copper_Ingot', None, None, None)
        AI_Target += results['Amount of Input 1']
        CopI_Target += results['Amount of Input 2']
        AAS_Target = 0
    elif y == "Alien_Carapace":
        Inputs.append("Alien_Carapce"  )
    elif y == "Alumina_Solution":
        print("1: Alumina_Solution, 2: Sloppy_Alumina")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Alumina_Solution = "Alumina_Solution"
        elif alternate == 2:
            Alumina_Solution = "Sloppy_Alumina"
        else:
            print('Invalid, quitting out')
            quit()
        if Alumina_Solution == "Alumina_Solution":
            if y == Target_Resource:
                AS_Target = Target_Resource_Amount
            results = craft(y, Alumina_Solution, AS_Target, 'Bauxite', 'Water', None, None, 'Silica')
            Bauxite_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            Silica_Target += results['Amount of Byproduct']
            AS_Target = 0
        elif Alumina_Solution == "Sloppy_Alumina":
            if y == Target_Resource:
                AS_Target = Target_Resource_Amount
            results = craft(y, Alumina_Solution, AS_Target, 'Bauxite', 'Water', None, None, None)
            Bauxite_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            AS_Target = 0
    elif y == "Aluminum_Casing": 
        print("1:Aluminum_Casing , 2: Aluminum_Casing")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Aluminum_Casing = "Aluminum_Casing"
        elif alternate == 2:
            Aluminum_Casing = "Aluminum_Casing"
        else:
            print('Invalid, quitting out')
            quit()
        if Aluminum_Casing == "Aluminum_Casing":
            if y == Target_Resource:
                AC_Target = Target_Resource_Amount
            results = craft(y, Aluminum_Casing, AC_Target, 'Aluminum_Ingot', None, None, None, None)
            AI_Target += results['Amount of Input 1']
            AC_Target = 0
        elif Aluminum_Casing == "Alclad_Casing":
            if y == Target_Resource:
                AC_Target = Target_Resource_Amount
            results = craft(y, Aluminum_Casing, AC_Target, 'Aluminum_Ingot', 'Copper_Ingot', None, None, None)
            AI_Target += results['Amount of Input 1']
            CopI_Target += results['Amount of Input 2']
            AC_Target = 0
    elif y == "Aluminum_Ingot": 
        print("1: Aluminum_Ingot, 2: Pure_Aluminum_Ingot")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Aluminum_Ingot = "Aluminum_Ingot"
        elif alternate == 2:
            Aluminum_Ingot = "Pure_Aluminum_Ingot"
        else:
            print('Invalid, quitting out')
            quit()
        if Aluminum_Ingot == "Aluminum_Ingot":
            if y == Target_Resource:
                AI_Target = Target_Resource_Amount
            results = craft(y, Aluminum_Ingot, AI_Target, 'Aluminum_Scrap', 'Silica', None, None, None)
            ASc_Target += results['Amount of Input 1']
            Silica_Target += results['Amount of Input 2']
            AI_Target = 0
        elif Aluminum_Ingot == "Pure_Aluminum_Ingot":
            if y == Target_Resource:
                AI_Target = Target_Resource_Amount
            results = craft(y, Aluminum_Ingot, AI_Target, 'Aluminum_Scrap', None, None, None, None)
            ASc_Target += results['Amount of Input 1']
            AI_Target = 0
    elif y == "Alien_Organs": 
        Inputs.append("Alien_Organs")
    elif y == "Aluminum_Scrap": 
        print("1: Aluminum_Scrap, 2: Electrode_Aluminum_Scrap, 3:Instant_Scrap")
        alternate = int(input('1,2, or 3?'))
        if alternate == 1:
            Aluminum_Scrap = "Aluminum_Scrap"
        elif alternate == 2:
            Aluminum_Scrap = "Electrode_Aluminum_Scrap"
        elif alternate == 3:
            Aluminum_Scrap = "Instant_Scrap"
        else:
            print('Invalid, quitting out')
            quit()
        if Aluminum_Scrap == "Aluminum_Scrap":
            if y == Target_Resource:
                ASc_Target = Target_Resource_Amount
            results = craft(y, Aluminum_Scrap, ASc_Target, 'Alumina_Solution', 'Coal', None, None, 'Water')
            AS_Target += results['Amount of Input 1']
            Coal_Target += results['Amount of Input 2']
            Water_Target -= results['Amount of Byproduct']
            ASc_Target = 0
        elif Aluminum_Scrap == "Electrode_Aluminum_Scrap":
            if y == Target_Resource:
                ASc_Target = Target_Resource_Amount
            results = craft(y, Aluminum_Scrap, ASc_Target, 'Alumina_Solution', 'Petroleum_Coke', None, None, 'Water')
            AS_Target += results['Amount of Input 1']
            PC_Target += results['Amount of Input 2']
            Water_Target -= results['Amount of Byproduct']
            ASc_Target = 0
        elif Aluminum_Scrap == "Instant_Scrap":
            if y == Target_Resource:
                ASc_Target = Target_Resource_Amount
            results = craft(y, Aluminum_Scrap, ACU_Target, 'Bauxite', 'Coal', 'Sulfuric_Acid', 'Water', None)
            Bauxite_Target += results['Amount of Input 1']
            Coal_Target += results['Amount of Input 2']
            SA_Target += results['Amount of Input 3']
            Water_Target += results['Amount of Input 4']
            print('Output water from this recipie:', 40 * ASc_Target / 300)
            ASc_Target = 0
    elif y == "Assembly_Director_System": 
        if y == Target_Resource:
            ADS_Target = Target_Resource_Amount
        results = craft(y, 'Assembly_Director_System', ADS_Target, 'Adaptive_Control_Unit', 'Supercomputer', None, None, None)
        ACU_Target += results['Amount of Input 1']
        Supercomputer_Target += results['Amount of Input 2']
        ADS_Target = 0
    elif y == "Automated_Wiring": 
        print("1: Automated_Wiring, 2: High_Speed_Wiring")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Automated_Wiring = "Automated_Wiring"
        elif alternate == 2:
            Automated_Wiring = "High_Speed_Wiring"
        else:
            print('Invalid, quitting out')
            quit()
        if Automated_Wiring == 'Automated_Wiring':
            if y == Target_Resource:
                AW_Target = Target_Resource_Amount
            results = craft(y, Automated_Wiring, AW_Target, 'Stator', 'Cable', None, None, None)
            Stator_Target += results['Amount of Input 1']
            Cable_Target += results['Amount of Input 2']
            AW_Target = 0
        elif Automated_Wiring == 'High_Speed_Wiring':
            if y == Target_Resource:
                AW_Target = Target_Resource_Amount
            results = craft(y, Automated_Wiring, ACU_Target, 'Stator', 'Wire', 'High_Speed_Connector', None, None)
            Stator_Target += results['Amount of Input 1']
            Wire_Target += results['Amount of Input 2']
            HSC_Target += results['Amount of Input 3']
            AW_Target = 0
    elif y == "Battery": 
        print("1: Battery, 2: ")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Battery = "Battery"
        elif alternate == 2:
            Battery = "Classic_Battery"
        else:
            print('Invalid, quitting out')
            quit()
        if Battery == 'Battery':
            if y == Target_Resource:
                Battery_Target = Target_Resource_Amount
            results = craft(y, Battery, Battery_Target, 'Aluminum_Casing', 'Alumina_Solution', 'Sulfuric_Acid', None, 'Water')
            AC_Target += results['Amount of Input 1']
            AS_Target += results['Amount of Input 2']
            SA_Target += results['Amount of Input 3']
            Water_Target -= results['Amount of Byproduct']
            Battery_Target = 0
        elif Battery == 'Classic_Battery':
            if y == Target_Resource:
                Battery_Target = Target_Resource_Amount
            results = craft(y, Battery, Battery_Target, 'Sulfur', 'Alclad_Aluminum_Sheet', 'Plastic', 'Wire', None)
            Sulfur_Target += results['Amount of Input 1']
            AAS_Target += results['Amount of Input 2']
            Plastic_Target += results['Amount of Input 3']
            Wire_Target += results['Amount of Input 4']
            Battery_Target = 0
    elif y == "Bauxite": 
        Inputs.append("Bauxite")
    elif y == "Beacon":
        print("1: Beacon, 2: Signal_Beacon")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Beacon = "Beacon"
        elif alternate == 2:
            Beacon = "Signal_Beacon"
        else:
            print('Invalid, quitting out')
            quit()
        if Beacon == 'Beacon':
            if y == Target_Resource:
                Beacon_Target = Target_Resource_Amount
            results = craft(y, Beacon, Beacon_Target, 'Iron_Plate', 'Iron_Rod', 'Cable', 'Wire', None)
            IP_Target += results['Amount of Input 1']
            IR_Target += results['Amount of Input 2']
            Cable_Target += results['Amount of Input 3']
            Wire_Target += results['Amount of Input 4']
            Beacon_Target = 0
        elif Beacon == 'Signal_Beacon':
            if y == Target_Resource:
                Beacon_Target = Target_Resource_Amount
            results = craft(y, Beacon, Beacon_Target, 'Steel_Beam', 'Steel_Pipe', 'Crystal_Oscillator', None, None)
            SB_Target += results['Amount of Input 1']
            SP_Target += results['Amount of Input 2']
            COsc_Target += results['Amount of Input 3']
            Beacon_Target = 0
    elif y == "Biomass": 
        print("Biomass: 1: Alien_Carapace, 2: Alien_Organs, 3: Leaves, 4: Mycelia, 5: Wood")
        alternate = int(input('1, 2, 3, 4, or 5?'))
        if alternate == 1:
            Biomass = "Alien_Carapace"
        elif alternate == 2:
            Biomass = "Alien_Organs"
        elif alternate == 3:
            Biomass = "Leaves"
        elif alternate == 4:
            Biomass = "Mycelia"
        elif alternate == 5:
            Biomass = "Wood"
        else:
            print('Invalid, quitting out')
            quit()
        if Biomass == "Alien_Carapace":
            if y == Target_Resource:
                Biomass_Target = Target_Resource_Amount
            results = craft(y, 'Biomass_Alien_Carapace', Biomass_Target, 'Alien_Carapace', None, None, None, None)
            Alien_Carapace_Target += results['Amount of Input 1']
            Biomass_Target = 0
        elif Biomass == "Alien_Organs":
            if y == Target_Resource:
                Biomass_Target = Target_Resource_Amount
            results = craft(y, 'Biomass_Alien_Organs', Biomass_Target, 'Alien_Organs', None, None, None, None)
            Alien_Organs_Target += results['Amount of Input 1']
            Biomass_Target = 0
        elif Biomass == "Leaves":
            if y == Target_Resource:
                Biomass_Target = Target_Resource_Amount
            results = craft(y, 'Biomass_Leaves', Biomass_Target, 'Leaves', None, None, None, None)
            Leaves_Target += results['Amount of Input 1']
            Biomass_Target = 0
        elif Biomass == "Mycelia":
            if y == Target_Resource:
                Biomass_Target = Target_Resource_Amount
            results = craft(y, 'Biomass_Mycelia', Biomass_Target, 'Mycelia', None, None, None, None)
            Mycelia_Target += results['Amount of Input 1']
            z = 0
            Biomass_Target = 0
        elif Biomass == "Wood":
            if y == Target_Resource:
                Biomass_Target = Target_Resource_Amount
            results = craft(y, 'Biomass_Wood', Biomass_Target, 'Wood', None, None, None, None)
            Wood_Target += results['Amount of Input 1']
            Biomass_Target = 0
    elif y == "Black_Powder": 
        print("1: Black_Powder, 2: Fine_Black_Powder")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Black_Powder = "Black_Powder"
        elif alternate == 2:
            Black_Powder = "Fine_Black_Powder"
        else:
            print('Invalid, quitting out')
            quit()
        if Black_Powder == 'Black_Powder':
            if y == Target_Resource:
                BP_Target = Target_Resource_Amount
            results = craft(y, Black_Powder, BP_Target, 'Coal', 'Sulfur', None, None, None)
            Coal_Target += results['Amount of Input 1']
            Sulfur_Target += results['Amount of Input 2']
            BP_Target = 0
        elif Black_Powder == 'Fine_Black_Powder':
            if y == Target_Resource:
                BP_Target = Target_Resource_Amount
            results = craft(y, Black_Powder, BP_Target, 'Compacted_Coal', 'Sulfur', None, None, None)
            Compacted_Coal_Target += results['Amount of Input 1']
            Sulfur_Target += results['Amount of Input 2']
            BP_Target = 0
    elif y == "Cable": 
        print("1: Cable, 2: , 3: , 4: ")
        alternate = int(input('1, 2, 3, or 4?'))
        if alternate == 1:
            Cable = "Cable"
        elif alternate == 2:
            Cable = "Coated_Cable"
        elif alternate == 3:
            Cable = "Insulated_Cable"
        elif alternate == 4:
            Cable = "Quickwire_Cable"
        else:
            print('Invalid, quitting out')
            quit()
        if Cable == "Cable":
            if y == Target_Resource:
                Cable_Target = Target_Resource_Amount
            results = craft(y, Cable, Cable_Target, 'Wire', None, None, None, None)
            Wire_Target += results['Amount of Input 1']
            Cable_Target = 0
        elif Cable == "Coated_Cable":
            if y == Target_Resource:
                Cable_Target = Target_Resource_Amount
            results = craft(y, Cable, Cable_Target, 'Wire', 'Heavy_Oil_Residue', None, None, None)
            Wire_Target += results['Amount of Input 1']
            HOR_Target += results['Amount of Input 2']
            Cable_Target = 0
        elif Cable == "Insulated_Cable":
            if y == Target_Resource:
                Cable_Target = Target_Resource_Amount
            results = craft(y, Cable, Cable_Target, 'Wire', 'Rubber', None, None, None)
            Wire_Target += results['Amount of Input 1']
            Rubber_Target += results['Amount of Input 2']
            Cable_Target = 0
        elif Cable == "Quickwire_Cable":
            if y == Target_Resource:
                Cable_Target = Target_Resource_Amount
            results = craft(y, Cable, ACU_Target, 'Quickwire', 'Rubber', None, None, None)
            Quickwire_Target += results['Amount of Input 1']
            Rubber_Target += results['Amount of Input 2']
            Cable_Target = 0
    elif y == "Caterium_Ingot": 
        print("1: Caterium_Ingot, 2: Pure_Caterium_Ingot")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Caterium_Ingot = "Caterium_Ingot"
        elif alternate == 2:
            Caterium_Ingot = "Pure_Caterium_Ingot"
        else:
            print('Invalid, quitting out')
            quit()
        if Caterium_Ingot == 'Caterium_Ingot':
            if y == Target_Resource:
                CatI_Target = Target_Resource_Amount
            results = craft(y, Caterium_Ingot, CatI_Target, 'Caterium_Ore', None, None, None, None)
            Caterium_Ore_Target += results['Amount of Input 1']
            CatI_Target = 0
        elif Caterium_Ingot == 'Pure_Caterium_Ingot':
            if y == Target_Resource:
                CatI_Target = Target_Resource_Amount
            results = craft(y, Caterium_Ingot, CatI_Target, 'Caterium_Ore', 'Water', None, None, None)
            Caterium_Ore_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            CatI_Target = 0
    elif y == "Caterium_Ore": 
        Inputs.append("Caterium_Ore")
    elif y == "Circuit_Board": 
        print("1: Circuit_Board, 2: , 3: , 4: ")
        alternate = int(input('1, 2, 3, or 4?'))
        if alternate == 1:
            Circuit_Board = "Circuit_Board"
        elif alternate == 2:
            Circuit_Board = "Electrode_Circuit_Board"
        elif alternate == 3:
            Circuit_Board = "Silicone_Circuit_Board"
        elif alternate == 4:
            Circuit_Board = "Caterium_Circuit_Board"
        else:
            print('Invalid, quitting out')
            quit()
        if Circuit_Board == "Circuit_Board":
            if y == Target_Resource:
                CB_Target = Target_Resource_Amount
            results = craft(y, Circuit_Board, CB_Target, 'Copper_Sheet', 'Plastic', None, None, None)
            CSheet_Target += results['Amount of Input 1']
            Plastic_Target += results['Amount of Input 2']
            CB_Target = 0
        elif Circuit_Board == "Electrode_Circuit_Board":
            if y == Target_Resource:
                CB_Target = Target_Resource_Amount
            results = craft(y, Circuit_Board, CB_Target, 'Rubber', 'Petroleum_Coke', None, None, None)
            Rubber_Target += results['Amount of Input 1']
            PC_Target += results['Amount of Input 2']
            CB_Target = 0
        elif Circuit_Board == "Silicone_Circuit_Board":
            if y == Target_Resource:
                CB_Target = Target_Resource_Amount
            results = craft(y, Circuit_Board, CB_Target, 'Copper_Sheet', 'Silica', None, None, None)
            CSheet_Target += results['Amount of Input 1']
            Silica_Target += results['Amount of Input 2']
            CB_Target = 0
        elif Circuit_Board == "Caterium_Circuit_Board":
            if y == Target_Resource:
                CB_Target = Target_Resource_Amount
            results = craft(y, Circuit_Board, CB_Target, 'Plastic', 'Quickwire', None, None, None)
            Plastic_Target += results['Amount of Input 1']
            Quickwire_Target += results['Amount of Input 2']
            CB_Target = 0
    elif y == "Coal": 
        print("Coal: 1: Miner, 2: Biocoal3, : Charcoal")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Coal = "Coal"
        elif alternate == 2:
            Coal = "Biocoal"
        elif alternate == 3:
            Coal = "Charcoal"
        else:
            print('Invalid, quitting out')
            quit()
        if Coal == "Mine":
            Inputs.append('Coal')
        elif Coal == "Biocoal":
            if y == Target_Resource:
                Coal_Target = Target_Resource_Amount
            results = craft(y, Coal, Coal_Target, 'Biomass', None, None, None, None)
            Biomass_Target += results['Amount of Input 1']
            Coal_Target = 0
        elif Coal == "Charcoal":
            if y == Target_Resource:
                Coal_Target = Target_Resource_Amount
            results = craft(y, Coal, Coal_Target, 'Wood', None, None, None, None)
            Wood_Target += results['Amount of Input 1']
            Coal_Target = 0
    elif y == "Color_Cartridge": 
        if y == Target_Resource:
            Color_Cartridge_Target = Target_Resource_Amount
        results = craft(y, 'Color_Cartridge', Color_Cartridge_Target, 'Flower_Petals', None, None, None, None)
        Flower_Petals_Target += results['Amount of Input 1']
        Color_Cartridge_Target = 0
    elif y == "Compacted_Coal": 
        if y == Target_Resource:
            Compacted_Coal_Target = Target_Resource_Amount
        results = craft(y, 'Compacted_Coal', ACU_Target, 'Coal', 'Sulfur', None, None, None)
        Coal_Target += results['Amount of Input 1']
        Sulfur_Target += results['Amount of Input 2']
        Compacted_Coal_Target = 0
    elif y == "Computer": 
        print("1: Computer, 2: Crystal_Computer, 3: Caterium_Computer")
        alternate = int(input('1, 2, or 3'))
        if alternate == 1:
            Computer = "Computer"
        elif alternate == 2:
            Computer = "Crystal_Computer"
        elif alternate == 3:
            Computer = "Caterium_Computer"
        else:
            print('Invalid, quitting out')
            quit()
        if Computer == "Computer":
            if y == Target_Resource:
                Computer_Target = Target_Resource_Amount
            results = craft(y, Computer, Computer_Target, 'Circuit_Board', 'Cable', 'Plastic', 'Screw', None)
            CB_Target += results['Amount of Input 1']
            Cable_Target += results['Amount of Input 2']
            Plastic_Target += results['Amount of Input 3']
            Screw_Target += results['Amount of Input 4']
            Computer_Target = 0
        elif Computer == "Crystal_Computer":
            if y == Target_Resource:
                Computer_Target = Target_Resource_Amount
            results = craft(y, Computer, Computer_Target, 'Circuit_Board', 'Crystal_Oscillator', None, None, None)
            CB_Target += results['Amount of Input 1']
            COsc_Target += results['Amount of Input 2']
            Computer_Target = 0
        elif Computer == "Caterium_Computer":
            if y == Target_Resource:
                Computer_Target = Target_Resource_Amount
            results = craft(y, Computer, Computer_Target, 'Circuit_Board', 'Quickwire', 'Rubber', None, None)
            CB_Target += results['Amount of Input 1']
            Quickwire_Target += results['Amount of Input 2']
            Rubber_Target += results['Amount of Input 3']
            Computer_Target = 0
    elif y == "Concrete": 
        print("1: Concrete, 2: , 3: , 4: ")
        alternate = int(input('1, 2, 3, or 4?'))
        if alternate == 1:
            Concrete = "Concrete"
        elif alternate == 2:
            Concrete = "Rubber_Concrete"
        elif alternate == 3:
            Concrete = "Wet_Concrete"
        elif alternate == 4:
            Concrete = "Fine_Concrete"
        else:
            print('Invalid, quitting out')
            quit()
        if Concrete == "Concrete":
            if y == Target_Resource:
                Concrete_Target = Target_Resource_Amount
            results = craft(y, Concrete, Concrete_Target, 'Limestone', None, None, None, None)
            Limestone_Target += results['Amount of Input 1']
            Concrete_Target = 0
        elif Concrete == "Rubber_Concrete":
            if y == Target_Resource:
                Concrete_Target = Target_Resource_Amount
            results = craft(y, Concrete, Concrete_Target, 'Limestone', 'Rubber', None, None, None)
            Limestone_Target += results['Amount of Input 1']
            Rubber_Target += results['Amount of Input 2']
            Concrete_Target = 0
        elif Concrete == "Wet_Concrete":
            if y == Target_Resource:
                Concrete_Target = Target_Resource_Amount
            results = craft(y, Concrete, Concrete_Target, 'Limestone', 'Water', None, None, None)
            Limestone_Target += results['Amount of Input 1']
            Rubber_Target += results['Amount of Input 2']
            Concrete_Target = 0
        elif Concrete == "Fine_Concrete":
            if y == Target_Resource:
                Concrete_Target = Target_Resource_Amount
            results = craft(y, Concrete, Concrete_Target, 'Silica', 'Limestone', None, None, None)
            Silica_Target += results['Amount of Input 1']
            Limestone_Target += results['Amount of Input 2']
            Concrete_Target = 0
    elif y == "Cooling_System": 
        print("1: Cooling_System, 2: Cooling_Device")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Cooling_System = "Cooling_System"
        elif alternate == 2:
            Cooling_System = "Cooling_Device"
        else:
            print('Invalid, quitting out')
            quit()
        if Cooling_System == "Cooling_System":
            if y == Target_Resource:
                CSys_Target = Target_Resource_Amount
            results = craft(y, Cooling_System, CSys_Target, 'Heat_Sink', 'Rubber', 'Water', 'Nitrogen_Gas', None)
            HS_Target += results['Amount of Input 1']
            Rubber_Target += results['Amount of Input 2']
            Water_Target += results['Amount of Input 3']
            Nitrogen_Gas_Target += results['Amount of Input 4']
            CSys_Target = 0
        elif Cooling_System == "Cooling_Device":
            if y == Target_Resource:
                CSys_Target = Target_Resource_Amount
            results = craft(y, Cooling_System, ACU_Target, 'Heat_Sink', 'Motor', 'Nitrogen_Gas', None, None)
            HS_Target += results['Amount of Input 1']
            Motor += results['Amount of Input 2']
            Nitrogen_Gas_Target += results['Amount of Input 3']
            CSys_Target = 0
    elif y == "Copper_Ingot": 
        print("1: Copper_Ingot, 2: , 3: ")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Copper_Ingot = "Copper_Ingot"
        elif alternate == 2:
            Copper_Ingot = "Copper_Alloy_Ingot"
        elif alternate == 3:
            Copper_Ingot = "Pure_Copper_Ingot"
        else:
            print('Invalid, quitting out')
            quit()
        if Copper_Ingot == "Copper_Ingot":
            if y == Target_Resource:
                CopI_Target = Target_Resource_Amount
            results = craft(y, Copper_Ingot, CopI_Target, 'Copper_Ore', None, None, None, None)
            Copper_Ore_Target += results['Amount of Input 1']
            CopI_Target = 0
        elif Copper_Ingot == "Copper_Alloy_Ingot":
            if y == Target_Resource:
                CopI_Target = Target_Resource_Amount
            results = craft(y, Copper_Ingot, CopI_Target, 'Copper_Ore', 'Iron_Ore', None, None, None)
            Copper_Ore_Target += results['Amount of Input 1']
            Iron_Ore_Target += results['Amount of Input 2']
            CopI_Target = 0
        elif Copper_Ingot == "Pure_Copper_Ingot":
            if y == Target_Resource:
                CopI_Target = Target_Resource_Amount
            results = craft(y, Copper_Ingot, CopI_Target, 'Copper_Ore', 'Water', None, None, None)
            Copper_Ore_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            CopI_Target = 0
    elif y == "Copper_Ore": 
        Inputs.append('Copper_Ore')
    elif y == "Copper_Powder": 
        if y == Target_Resource:
            CPow_Target = Target_Resource_Amount
        results = craft(y, 'Copper_Powder', CPow_Target, 'Copper_Ingot', None, None, None, None)
        CopI_Target += results['Amount of Input 1']
        CPow_Target = 0
    elif y == "Copper_Sheet": 
        print("1: Copper_Sheet, 2:Steamed_Copper_Sheet ")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Copper_Sheet = "Copper_Sheet"
        elif alternate == 2:
            Copper_Sheet = "Steamed_Copper_Sheet"
        else:
            print('Invalid, quitting out')
            quit()
        if Copper_Sheet == 'Copper_Sheet':
            if y == Target_Resource:
                CSheet_Target= Target_Resource_Amount
            results = craft(y, Copper_Sheet, CSheet_Target, 'Copper_Ingot', None, None, None, None)
            CopI_Target += results['Amount of Input 1']
            CSheet_Target = 0
        elif Copper_Sheet == 'Steamed_Copper_Sheet':
            if y == Target_Resource:
                CSheet_Target= Target_Resource_Amount
            results = craft(y, Copper_Sheet, CSheet_Target, 'Copper_Ingot', 'Water', None, None, None)
            CopI_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            CSheet_Target = 0
    elif y == "Crude_Oil": 
        Inputs.append('Crude_Oil')
    elif y == "Crystal_Oscillator": 
        print("1: Crystal_Oscillator, 2: Insulated_Crystal_Oscillator")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Crystal_Oscillator = "Crystal_Oscillator"
        elif alternate == 2:
            Crystal_Oscillator = "Insulated_Crystal_Oscillator"
        else:
            print('Invalid, quitting out')
            quit()
        if Crystal_Oscillator == 'Crystal_Oscillator':
            if y == Target_Resource:
                COsc_Target= Target_Resource_Amount
            results = craft(y, Crystal_Oscillator, COsc_Target, 'Quartz_Crystal', 'Cable', 'Reinforced_Iron_Plate', None, None)
            QCrystal_Target += results['Amount of Input 1']
            Cable_Target += results['Amount of Input 2']
            RIP_Target += results['Amount of Input 3']
            COsc_Target = 0
        elif Crystal_Oscillator == 'Insulated_Crystal_Oscillator':
            if y == Target_Resource:
                COsc_Target= Target_Resource_Amount
            results = craft(y, Crystal_Oscillator, ACU_Target, 'Quartz_Crystal', 'Rubber', 'AI_Limiter', None, None)
            QCrystal_Target += results['Amount of Input 1']
            Rubber_Target += results['Amount of Input 2']
            AIL_Target += results['Amount of Input 3']
            COsc_Target = 0
    elif y == "Electromagnetic_Control_Rod": 
        print("1: Electromagnetic_Control_Rod, 2: Electromagnetic_Connection_Rod")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Electromagnetic_Control_Rod = "Electromagnetic_Control_Rod"
        elif alternate == 2:
            Electromagnetic_Control_Rod = "Electromagnetic_Connection_Rod"
        else:
            print('Invalid, quitting out')
            quit()
        if Electromagnetic_Control_Rod == 'Electromagnetic_Control_Rod':
            if y == Target_Resource:
                ECR_Target= Target_Resource_Amount
            results = craft(y, Electromagnetic_Control_Rod, ECR_Target, 'Stator', 'AI_Limiter', None, None, None)
            Stator_Target += results['Amount of Input 1']
            AIL_Target += results['Amount of Input 2']
            ECR_Target = 0
        elif Electromagnetic_Control_Rod == 'Electromagnetic_Connection_Rod':
            if y == Target_Resource:
                ECR_Target= Target_Resource_Amount
            results = craft(y, Electromagnetic_Control_Rod, ECR_Target, 'Stator', 'High_Speed_Connector', None, None, None)
            Stator_Target += results['Amount of Input 1']
            HSC_Target += results['Amount of Input 2']
            ECR_Target = 0
    elif y == "Empty_Canister": 
        print("1: Empty_Canister, 2: Steel_Canister, 3: Coated_Iron_Canister")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Empty_Canister = "Empty_Canister"
        elif alternate == 2:
            Empty_Canister = "Steel_Canister"
        elif alternate == 3:
            Empty_Canister = "Coated_Iron_Canister"
        else:
            print('Invalid, quitting out')
            quit()
        if Empty_Canister == "Empty_Canister":
            if y == Target_Resource:
                EC_Target= Target_Resource_Amount
            results = craft(y, Empty_Canister, EC_Target, 'Plastic', None, None, None, None)
            Plastic_Target += results['Amount of Input 1']
            EC_Target = 0
        elif Empty_Canister == "Steel_Canister":
            if y == Target_Resource:
                EC_Target= Target_Resource_Amount
            results = craft(y, Empty_Canister, EC_Target, 'Steel_Ingot', None, None, None, None)
            SI_Target += results['Amount of Input 1']
            EC_Target = 0
        elif Empty_Canister == "Coated_Iron_Canister":
            if y == Target_Resource:
                EC_Target= Target_Resource_Amount
            results = craft(y, Empty_Canister, EC_Target, 'Iron_Plate', 'Copper_Sheet', None, None, None)
            IP_Target += results['Amount of Input 1']
            CSheet_Target += results['Amount of Input 2']
            EC_Target = 0
    elif y == "Empty_Fluid_Tank": 
        if y == Target_Resource:
            EFT_Target= Target_Resource_Amount
        results = craft(y, 'Empty_Fluid_Tank', EFT_Target, 'Aluminum_Ingot', None, None, None, None)
        AI_Target += results['Amount of Input 1']
        EFT_Target = 0
    elif y == "Encased_Industrial_Beam": 
        print("1: Encased_Industrial_Beam, 2: Encased_Industrial_Pipe")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Encased_Industrial_Beam = "Encased_Industrial_Beam"
        elif alternate == 2:
            Encased_Industrial_Beam = "Encased_Industrial_Pipe"
        else:
            print('Invalid, quitting out')
            quit()
        if Encased_Industrial_Beam == 'Encased_Industrial_Beam':
            if y == Target_Resource:
                EIB_Target= Target_Resource_Amount
            results = craft(y, Encased_Industrial_Beam, EIB_Target, 'Steel_Beam', 'Concrete', None, None, None)
            SB_Target += results['Amount of Input 1']
            Concrete_Target += results['Amount of Input 2']
            EIB_Target = 0
        elif Encased_Industrial_Beam == 'Encased_Industrial_Pipe':
            if y == Target_Resource:
                EIB_Target= Target_Resource_Amount
            results = craft(y, Encased_Industrial_Beam, EIB_Target, 'Steel_Pipe', 'Concrete', None, None, None)
            SP_Target += results['Amount of Input 1']
            Concrete_Target += results['Amount of Input 2']
            EIB_Target = 0
    elif y == "Encased_Plutonium_Cell": 
        print("1: Encased_Plutonium_Cell, 2: Instant_Plutonium_Cell")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Encased_Plutonium_Cell = "Encased_Plutonium_Cell"
        elif alternate == 2:
            Encased_Plutonium_Cell = "Instant_Plutonium_Cell"
        else:
            print('Invalid, quitting out')
            quit()
        if Encased_Plutonium_Cell == 'Encased_Plutonium_Cell':
            if y == Target_Resource:
                EPC_Target= Target_Resource_Amount
            results = craft(y, Encased_Plutonium_Cell, EPC_Target, 'Plutonium_Pellets', 'Concrete', None, None, None)
            PP_Target += results['Amount of Input 1']
            Concrete_Target += results['Amount of Input 2']
            EPC_Target = 0
        elif Encased_Plutonium_Cell == 'Instant_Plutonium_Cell':
            if y == Target_Resource:
                EPC_Target= Target_Resource_Amount
            results = craft(y, Encased_Plutonium_Cell, EPC_Target, 'Non_Fissile_Uranium', 'Aluminum_Casing', 'Nitrogen_Gas', None, None)
            NFU_Target += results['Amount of Input 1']
            AC_Target += results['Amount of Input 2']
            Nitrogen_Gas_Target += results['Amount of Input 3']
            EPC_Target = 0
    elif y == "Encased_Uranium_Cell": 
        print("1: Encased_Uranium_Cell, 2: Infused_Uranium_Cell")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Encased_Uranium_Cell = "Encased_Uranium_Cell"
        elif alternate == 2:
            Encased_Uranium_Cell = "Infused_Uranium_Cell"
        else:
            print('Invalid, quitting out')
            quit()
        if Encased_Uranium_Cell == 'Encased_Uranium_Cell':
            if y == Target_Resource:
                EUC_Target= Target_Resource_Amount
            results = craft(y, Encased_Uranium_Cell, EUC_Target, 'Uranium', 'Concrete', 'Sulfuric_Acid', None, None)
            Uranium_Target += results['Amount of Input 1']
            Concrete_Target += results['Amount of Input 2']
            SA_Target += results['Amount of Input 3']
            print('Output sulfuric acid from this recipie:', 10 * EUC_Target / 25)
            EUC_Target = 0
        elif Encased_Uranium_Cell == 'Infused_Uranium_Cell':
            if y == Target_Resource:
                EUC_Target= Target_Resource_Amount
            results = craft(y, Encased_Uranium_Cell, EUC_Target, 'Uranium', 'Silica', 'Sulfur', 'Quickwire', None)
            Silica_Target += results['Amount of Input 1']
            Sulfur_Target += results['Amount of Input 2']
            Quickwire_Target += results['Amount of Input 3']
            EUC_Target = 0
    elif y == "Fabric": 
        print("1: Fabric, 2: Polyester_Fabric")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Fabric = "Fabric"
        elif alternate == 2:
            Fabric = "Polyester_Fabric"
        else:
            print('Invalid, quitting out')
            quit()
        if Fabric == 'Fabric':
            if y == Target_Resource:
                Fabric_Target= Target_Resource_Amount
            results = craft(y, Fabric, Fabric_Target, 'Mycelia', 'Biomass', None, None, None)
            Mycelia_Target += results['Amount of Input 1']
            Biomass_Target += results['Amount of Input 2']
            Fabric_Target = 0
        elif Fabric == 'Polyester_Fabric':
            if y == Target_Resource:
                Fabric_Target= Target_Resource_Amount
            results = craft(y, Fabric, Fabric_Target, 'Polymer_Resin', 'Water', None, None, None)
            PR_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            Fabric_Target = 0
    elif y == "Flower_Petals": 
        Inputs.append('Flower_Petals')
    elif y == "Fuel": 
        print("1: Fuel, 2: Residual_Fuel, 3: Unpackage_Fuel(diluted), 4: Diluted_Fuel")
        alternate = int(input('1, 2, 3, or 4?'))
        if alternate == 1:
            Fuel = "Fuel"
        elif alternate == 2:
            Fuel = "Residual_Fuel"
        elif alternate == 3:
            Fuel = "Unpackage_Fuel(diluted)"
        elif alternate == 4:
            Fuel = "Diluted_Fuel"
        else:
            print('Invalid, quitting out')
            quit()
        if Fuel == "Fuel":
            if y == Target_Resource:
                Fuel_Target= Target_Resource_Amount
            results = craft(y, Fuel, Fuel_Target, 'Crude_Oil', None, None, None, 'Polymer_Resin')
            Crude_Oil_Target += results['Amount of Input 1']
            PR_Target -= results['Amount of Byproduct']
            Fuel_Target = 0
        elif Fuel == "Residual_Fuel":
            if y == Target_Resource:
                Fuel_Target= Target_Resource_Amount
            results = craft(y, Fuel, Fuel_Target, 'Heavy_Oil_Residue', None, None, None, None)
            HOR_Target += results['Amount of Input 1']
            Fuel_Target = 0
        elif Fuel == "Unpackage_Fuel(diluted)":
            if y == Target_Resource:
                Fuel_Target= Target_Resource_Amount
            results = craft(y, 'Unpackage_Fuel', Fuel_Target, 'Packaged_Fuel', None, None, None, 'Empty_Canister')
            PF_Target += results['Amount of Input 1']
            EC_Target -= results['Amount of Byproduct']
            Target_Resources.remove('Packaged_Fuel')
            Fuel_Target = 0
            results = craft(y, 'Diluted_Packaged_Fuel', PF_Target, 'Heavy_Oil_Residue', 'Packaged_Water', None, None, None)
            HOR_Target += results['Amount of Input 1']
            PW_Target += results['Amount of Input 2']
            PF_Target = 0
        elif Fuel == "Diluted_Fuel":
            if y == Target_Resource:
                Fuel_Target= Target_Resource_Amount
            results = craft(y, Fuel, Fuel_Target, 'Heavy_Oil_Residue', 'Water', None, None, None)
            HOR_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            Fuel_Target = 0
    elif y == "Fused_Modular_Frame": 
        print("1: Fused_Modular_Frame, 2: Heat_Fused_Frame")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Fused_Modular_Frame = "Fused_Modular_Frame"
        elif alternate == 2:
            Fused_Modular_Frame = "Heat_Fused_Frame"
        else:
            print('Invalid, quitting out')
            quit()
        if Fused_Modular_Frame == 'Fused_Modular_Frame':
            if y == Target_Resource:
                FMF_Target= Target_Resource_Amount
            results = craft(y, Fused_Modular_Frame, FMF_Target, 'Heavy_Modular_Frame', 'Aluminum_Casing', 'Nitrogen_Gas', None, None)
            HMF_Target += results['Amount of Input 1']
            AC_Target += results['Amount of Input 2']
            Nitrogen_Gas_Target += results['Amount of Input 3']
            FMF_Target = 0
        elif Fused_Modular_Frame == "Heat_Fused_Frame":
            if y == Target_Resource:
                FMF_Target= Target_Resource_Amount
            results = craft(y, Fused_Modular_Frame, FMF_Target, 'Heavy_Modular_Frame', 'Aluminum_Ingot', 'Nitric_Acid', 'Fuel', None)
            HMF_Target += results['Amount of Input 1']
            AI_Target += results['Amount of Input 2']
            NA_Target += results['Amount of Input 3']
            Fuel_Target += results['Amount of Input 4']
            FMF_Target = 0
    elif y == "Gas_Filter": 
        if y == Target_Resource:
            GF_Target= Target_Resource_Amount
        results = craft(y, 'Gas_Filter', GF_Target, 'Coal', 'Rubber', 'Fabric', None, None)
        Coal_Target += results['Amount of Input 1']
        Rubber_Target += results['Amount of Input 2']
        Fabric_Target += results['Amount of Input 3']
        GF_Target = 0
    elif y == "Heat_Sink": 
        print("1: Heat_Sink, 2: Heat_Exchanger")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Heat_Sink = "Heat_Sink"
        elif alternate == 2:
            Heat_Sink = "Heat_Exchanger"
        else:
            print('Invalid, quitting out')
            quit()
        if Heat_Sink == 'Heat_Sink':
            if y == Target_Resource:
                HS_Target = Target_Resource_Amount
            results = craft(y, Heat_Sink, HS_Target, 'Alclad_Aluminum_Sheet', 'Copper_Sheet', None, None, None)
            AAS_Target += results['Amount of Input 1']
            CSheet_Target += results['Amount of Input 2']
            HS_Target = 0
        elif Heat_Sink == 'Heat_Exchanger':
            if y == Target_Resource:
                HS_Target = Target_Resource_Amount
            results = craft(y, Heat_Sink, HS_Target, 'Aluminum_Casing', 'Rubber', None, None, None)
            AC_Target += results['Amount of Input 1']
            Rubber_Target += results['Amount of Input 2']
            HS_Target = 0
    elif y == "Heavy_Modular_Frame": 
        print("1: Heavy_Modular_Frame, 2: Heavy_Flexible_Frame, 3: Heavy_Encased_Frame")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Heavy_Modular_Frame = "Heavy_Modular_Frame"
        elif alternate == 2:
            Heavy_Modular_Frame = "Heavy_Flexible_Frame"
        elif alternate == 3:
            Heavy_Modular_Frame = "Heavy_Encased_Frame"
        else:
            print('Invalid, quitting out')
            quit()
        if Heavy_Modular_Frame == 'Heavy_Modular_Frame':
            if y == Target_Resource:
                HMF_Target= Target_Resource_Amount
            results = craft(y, Heavy_Modular_Frame, HMF_Target, 'Modular_Frame', 'Steel_Pipe', 'Encased_Industrial_Beam', 'Screw', None)
            MF_Target += results['Amount of Input 1']
            SP_Target += results['Amount of Input 2']
            EIB_Target += results['Amount of Input 3']
            Screw_Target += results['Amount of Input 4']
            HMF_Target = 0
        elif Heavy_Modular_Frame == 'Heavy_Flexible_Frame':
            if y == Target_Resource:
                HMF_Target= Target_Resource_Amount
            results = craft(y, Heavy_Modular_Frame, HMF_Target, 'Modular_Frame', 'Encased_Industrial_Beam', 'Rubber', 'Screw', None)
            MF_Target += results['Amount of Input 1']
            EIB_Target += results['Amount of Input 2']
            Rubber_Target += results['Amount of Input 3']
            Screw_Target += results['Amount of Input 4']
            HMF_Target = 0
        elif Heavy_Modular_Frame == 'Heavy_Encased_Frame':
            if y == Target_Resource:
                HMF_Target= Target_Resource_Amount
            results = craft(y, Heavy_Modular_Frame, HMF_Target, 'Modular_Frame', 'Encased_Industrial_Beam', 'Steel_Pipe', 'Concrete', None)
            MF_Target += results['Amount of Input 1']
            EIB_Target += results['Amount of Input 2']
            SP_Target += results['Amount of Input 3']
            Concrete_Target += results['Amount of Input 4']
            HMF_Target = 0
    elif y == "Heavy_Oil_Residue": 
        print("Heavy_Oil_Residue: 1: Plastic, 2: Rubber, 3: Polymer_Resin, 4: Heavy_Oil_Residue")
        alternate = int(input('1, 2, 3, or 4?'))
        if alternate == 1:
            Heavy_Oil_Residue = "Plastic"
        elif alternate == 2:
            Heavy_Oil_Residue = "Rubber"
        elif alternate == 3:
            Heavy_Oil_Residue = "Polymer_Resin"
        elif alternate == 4:
            Heavy_Oil_Residue = "Heavy_Oil_Residue"
        else:
            print('Invalid, quitting out')
            quit()
        if Heavy_Oil_Residue == "Plastic":
            if y == Target_Resource:
                HOR_Target= Target_Resource_Amount
            results = craft(y, Heavy_Oil_Residue, HOR_Target, 'Crude_Oil', None, None, None, 'Plastic')
            Crude_Oil_Target += results['Amount of Input 1']
            Plastic_Target -= results['Amount of Byproduct']
            HOR_Target = 0
        elif Heavy_Oil_Residue == "Rubber":
            if y == Target_Resource:
                HOR_Target= Target_Resource_Amount
            results = craft(y, Heavy_Oil_Residue, HOR_Target, 'Crude_Oil', None, None, None, 'Rubber')
            Crude_Oil_Target += results['Amount of Input 1']
            Rubber_Target -= results['Amount of Byproduct']
            HOR_Target = 0
        elif Heavy_Oil_Residue == "Polymer_Resin":
            if y == Target_Resource:
                HOR_Target= Target_Resource_Amount
            results = craft(y, Heavy_Oil_Residue, HOR_Target, 'Crude_Oil', None, None, None, 'Polymer_Resin')
            Crude_Oil_Target += results['Amount of Input 1']
            PR_Target -= results['Amount of Byproduct']
            HOR_Target = 0
        elif Heavy_Oil_Residue == "Heavy_Oil_Residue":
            if y == Target_Resource:
                HOR_Target= Target_Resource_Amount
            results = craft(y, Heavy_Oil_Residue, HOR_Target, 'Crude_Oil', None, None, None, 'Polymer_Resin')
            Crude_Oil_Target += results['Amount of Input 1']
            PR_Target -= results['Amount of Byproduct']
            HOR_Target = 0
    elif y == "High_Speed_Connector": 
        print("1: High_Speed_Connector, 2: Silicone_High_Speed_Connector")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            High_Speed_Connector = "High_Speed_Connector"
        elif alternate == 2:
            High_Speed_Connector = "Silicone_High_Speed_Connector"
        else:
            print('Invalid, quitting out')
            quit()
        if High_Speed_Connector == 'High_Speed_Connector':
            if y == Target_Resource:
                HSC_Target= Target_Resource_Amount
            results = craft(y, High_Speed_Connector, HSC_Target, 'Quickwire', 'Cable', 'Circuit_Board', None, None)
            Quickwire_Target += results['Amount of Input 1']
            Cable_Target += results['Amount of Input 2']
            CB_Target += results['Amount of Input 3']
            HSC_Target = 0
        elif High_Speed_Connector == 'Silicone_High_Speed_Connector':
            if y == Target_Resource:
                HSC_Target= Target_Resource_Amount
            results = craft(y, High_Speed_Connector, HSC_Target, 'Quickwire', 'Silica', 'Circuit_Board', None, None)
            Quickwire_Target += results['Amount of Input 1']
            Silica_Target += results['Amount of Input 2']
            CB_Target += results['Amount of Input 3']
            HSC_Target = 0
    elif y == "Iodine_Infused_Filter": 
        if y == Target_Resource:
            IIF_Target= 'Target_Resource_Amount'
        results = craft(y, 'Iodine_Infused_Filter', IIF_Target, 'Gas_Filter', 'Quickwire', 'Aluminum_Casing', None, None)
        GF_Target += results['Amount of Input 1']
        Quickwire_Target += results['Amount of Input 2']
        AC_Target += results['Amount of Input 3']
        IIF_Target = 0
    elif y == "Iron_Ingot": 
        print("1: Iron_Ingot, 2: Pure_Iron_Ingot, 3: Iron_Alloy_Ingot")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Iron_Ingot = "Iron_Ingot"
        elif alternate == 2:
            Iron_Ingot = "Pure_Iron_Ingot"
        elif alternate == 3:
            Iron_Ingot = "Iron_Alloy_Ingot"
        else:
            print('Invalid, quitting out')
            quit()
        if Iron_Ingot == "Iron_Ingot":
            if y == Target_Resource:
                II_Target = Target_Resource_Amount
            results = craft(y, Iron_Ingot, II_Target, 'Iron_Ore', None, None, None, None)
            Iron_Ore_Target += results['Amount of Input 1']
            II_Target = 0
        elif Iron_Ingot == "Pure_Iron_Ingot":
            if y == Target_Resource:
                II_Target = Target_Resource_Amount
            results = craft(y, Iron_Ingot, II_Target, 'Iron_Ore', 'Water', None, None, None)
            Iron_Ore_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            II_Target = 0
        elif Iron_Ingot == "Iron_Alloy_Ingot":
            if y == Target_Resource:
                II_Target = Target_Resource_Amount
            results = craft(y, Iron_Ingot, II_Target, 'Iron_Ore', 'Copper_Ore', None, None, None)
            Iron_Ore_Target += results['Amount of Input 1']
            Copper_Ore_Target += results['Amount of Input 2']
            II_Target = 0
    elif y == "Iron_Ore": 
        Inputs.append('Iron_Ore')
    elif y == "Iron_Plate": 
        print("1: Iron_Plate, 2: Coated_Iron_Plate, 3: Steel_Coated_Plate")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Iron_Plate = "Iron_Plate"
        elif alternate == 2:
            Iron_Plate = "Coated_Iron_Plate"
        elif alternate == 3:
            Iron_Plate = "Steel_Coated_Plate"
        else:
            print('Invalid, quitting out')
            quit()
        if Iron_Plate == 'Iron_Plate':
            if y == Target_Resource:
                IP_Target= Target_Resource_Amount
            results = craft(y, Iron_Plate, IP_Target, 'Iron_Ingot', None, None, None, None)
            II_Target += results['Amount of Input 1']
            IP_Target = 0
        elif Iron_Plate == 'Coated_Iron_Plate':
            if y == Target_Resource:
                IP_Target= Target_Resource_Amount
            results = craft(y, Iron_Plate, IP_Target, 'Iron_Ingot', 'Plastic', None, None, None)
            II_Target += results['Amount of Input 1']
            Plastic_Target += results['Amount of Input 2']
            IP_Target = 0
        elif Iron_Plate == 'Steel_Coated_Plate':
            if y == Target_Resource:
                IP_Target= Target_Resource_Amount
            results = craft(y, Iron_Plate, IP_Target, 'Steel_Ingot', 'Plastic', None, None, None)
            SI_Target += results['Amount of Input 1']
            Plastic_Target += results['Amount of Input 2']
            IP_Target = 0
    elif y == "Iron_Rod": 
        print("1: Iron_Rod, 2: Steel_Rod")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Iron_Rod = "Iron_Rod"
        elif alternate == 2:
            Iron_Rod = "Steel_Rod"
        else:
            print('Invalid, quitting out')
            quit()
        if Iron_Rod == 'Iron_Rod':
            if y == Target_Resource:
                IR_Target= Target_Resource_Amount
            results = craft(y, Iron_Rod, IR_Target, 'Iron_Ingot', None, None, None, None)
            II_Target += results['Amount of Input 1']
            IR_Target = 0
        elif Iron_Rod == 'Steel_Rod':
            if y == Target_Resource:
                IR_Target= Target_Resource_Amount
            results = craft(y, Iron_Rod, IR_Target, 'Steel_Ingot', None, None, None, None)
            SI_Target += results['Amount of Input 1']
            IR_Target = 0
    elif y == "Leaves": 
        Inputs.append('Leaves')
    elif y == "Limestone": 
        Inputs.append('Limestone')
    elif y == "Liquid_Biofuel": 
        if y == Target_Resource:
            LB_Target= Target_Resource_Amount
        results = craft(y, 'Liquid_Biofuel', LB_Target, 'Solid_Biofuel', 'Water', None, None, None)
        SB_Target += results['Amount of Input 1']
        Water_Target += results['Amount of Input 2']
        LB_Target = 0
    elif y == "Magnetic_Field_Generator": 
        if y == Target_Resource:
            MFG_Target= Target_Resource_Amount
        results = craft(y, 'Magnetic_Field_Generator', MFG_Target, 'Versatile_Framework', 'Electromagnetic_Connection_Rod', 'Battery', None, None)
        VF_Target += results['Amount of Input 1']
        ECR_Target += results['Amount of Input 2']
        Battery_Target += results['Amount of Input 3']
        MFG_Target = 0
    elif y == "Modular_Engine": 
        if y == Target_Resource:
            ME_Target= Target_Resource_Amount
        results = craft(y, 'Modular_Engine', ME_Target, 'Motor', 'Rubber', 'Smart_Plating', None, None)
        Motor_Target += results['Amount of Input 1']
        Rubber_Target += results['Amount of Input 2']
        SP_Target += results['Amount of Input 3']
        ME_Target = 0
    elif y == "Modular_Frame": 
        print("1: Modular_Frame, 2: Bolted_Frame, 3: Steeled_Frame")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Modular_Frame = "Modular_Frame"
        elif alternate == 2:
            Modular_Frame = "Bolted_Frame"
        elif alternate == 3:
            Modular_Frame = "Steeled_Frame"
        else:
            print('Invalid, quitting out')
            quit()
        if Modular_Frame == 'Modular_Frame':
            if y == Target_Resource:
                MF_Target= Target_Resource_Amount
            results = craft(y, Modular_Frame, MF_Target, 'Reinforced_Iron_Plate', 'Iron_Rod', None, None, None)
            RIP_Target += results['Amount of Input 1']
            IR_Target += results['Amount of Input 2']
            MF_Target = 0
        elif Modular_Frame == 'Bolted_Frame':
            if y == Target_Resource:
                MF_Target= Target_Resource_Amount
            results = craft(y, Modular_Frame, MF_Target, 'Reinforced_Iron_Plate', 'Screw', None, None, None)
            RIP_Target += results['Amount of Input 1']
            Screw_Target += results['Amount of Input 2']
            MF_Target = 0
        elif Modular_Frame == 'Steeled_Frame':
            if y == Target_Resource:
                MF_Target= Target_Resource_Amount
            results = craft(y, Modular_Frame, MF_Target, 'Reinforced_Iron_Plate', 'Steel_Pipe', None, None, None)
            RIP_Target += results['Amount of Input 1']
            SP_Target += results['Amount of Input 2']
            MF_Target = 0
    elif y == "Motor": 
        print("1: Motor, 2: Rigour_Motor, 3: Electric_Motor")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Motor = "Motor"
        elif alternate == 2:
            Motor = "Rigour_Motor"
        elif alternate == 3:
            Motor = "Electric_Motor"
        else:
            print('Invalid, quitting out')
            quit()
        if Motor == 'Motor':
            if y == Target_Resource:
                Motor_Target= Target_Resource_Amount
            results = craft(y, Motor, Motor_Target, 'Rotor', 'Stator', None, None, None)
            Rotor_Target += results['Amount of Input 1']
            Stator_Target += results['Amount of Input 2']
            Motor_Target = 0
        elif Motor == 'Rigour_Motor':
            if y == Target_Resource:
                Motor_Target= Target_Resource_Amount
            results = craft(y, Motor, Motor_Target, 'Rotor', 'Stator', 'Crystal_Oscillator', None, None)
            Rotor_Target += results['Amount of Input 1']
            Stator_Target += results['Amount of Input 2']
            COsc_Target += results['Amount of Input 3']
            Motor_Target = 0
        elif Motor == 'Electric_Motor':
            if y == Target_Resource:
                Motor_Target= Target_Resource_Amount
            results = craft(y, Motor, Motor_Target, 'Electromagnetic_Control_Rod', 'Rotor', None, None, None)
            ECR_Target += results['Amount of Input 1']
            Rotor_Target += results['Amount of Input 2']
            Motor_Target = 0
    elif y == "Mycelia": 
        Inputs.append('Mycelia')
    elif y == "Nitric_Acid": 
        if y == Target_Resource:
            NA_Target= Target_Resource_Amount
        results = craft(y, 'Nitric_Acid', NA_Target, 'Nitrogen_Gas', 'Water', 'Iron_Plate', None, None)
        Nitrogen_Gas_Target += results['Amount of Input 1']
        Water_Target += results['Amount of Input 2']
        IP_Target += results['Amount of Input 3']
        NA_Target = 0
    elif y == "Nitrogen_Gas": 
        Inputs.append('Nitrogen_Gas')
    elif y == "Nobelisk": 
        print("1: Nobelisk, 2: Seismic_Nobelisk")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Nobelisk = "Nobelisk"
        elif alternate == 2:
            Nobelisk = "Seismic_Nobelisk"
        else:
            print('Invalid, quitting out')
            quit()
        if Nobelisk == 'Nobelisk':
            if y == Target_Resource:
                Nobelisk_Target= Target_Resource_Amount
            results = craft(y, Nobelisk, Nobelisk_Target, 'Black_Powder', 'Steel_Pipe', None, None, None)
            BP_Target += results['Amount of Input 1']
            SP_Target += results['Amount of Input 2']
            Nobelisk_Target = 0
        elif Nobelisk == 'Seismic_Nobelisk':
            if y == Target_Resource:
                Nobelisk_Target= Target_Resource_Amount
            results = craft(y, Nobelisk, Nobelisk_Target, 'Black_Powder', 'Steel_Pipe', 'Crystal_Oscillator', None, None)
            BP_Target += results['Amount of Input 1']
            SP_Target += results['Amount of Input 2']
            COsc_Target += results['Amount of Input 3']
            Nobelisk_Target = 0
    elif y == "Non_Fissile_Uranium": 
        print("1: Non_Fissile_Uranium, 2: Fertile_Uranium")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Non_Fissile_Uranium = "Non_Fissile_Uranium"
        elif alternate == 2:
            Non_Fissile_Uranium = "Fertile_Uranium"
        else:
            print('Invalid, quitting out')
            quit()
        if Non_Fissile_Uranium == 'Non_Fissile_Uranium':
            if y == Target_Resource:
                NFU_Target= Target_Resource_Amount
            results = craft(y, Non_Fissile_Uranium, NFU_Target, 'Nuclear_Waste', 'Nitric_Acid', 'Sulfuric_Acid', 'Silica', 'Water')
            NW_Target += results['Amount of Input 1']
            NA_Target += results['Amount of Input 2']
            SA_Target += results['Amount of Input 3']
            Silica_Target += results['Amount of Input 4']
            Water_Target -= results['Amount of Byproduct']
            NFU_Target = 0
        elif Non_Fissile_Uranium == 'Fertile_Uranium':
            if y == Target_Resource:
                NFU_Target= Target_Resource_Amount
            results = craft(y, Non_Fissile_Uranium, NFU_Target, 'Uranium', 'Nuclear_Waste', 'Nitric_Acid', 'Sulfuric_Acid', None)
            Uranium_Target += results['Amount of Input 1']
            NW_Target += results['Amount of Input 2']
            NA_Target += results['Amount of Input 3']
            SA_Target += results['Amount of Input 4']
            NFU_Target = 0
    elif y == "Nuclear_Fuel_Rod": 
        print("Nuclear_Fuel_Rod: 1: Uranium_Fuel_Rod, 2: Nuclear_Fuel_Unit")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Uranium_Fuel_Rod = "Uranium_Fuel_Rod"
        elif alternate == 2:
            Uranium_Fuel_Rod = "Nuclear_Fuel_Unit"
        else:
            print('Invalid, quitting out')
            quit()
        if Uranium_Fuel_Rod == 'Uranium_Fuel_Rod':
            if y == Target_Resource:
                NFR_Target= Target_Resource_Amount
            results = craft(y, Uranium_Fuel_Rod, NFR_Target, 'Encased_Uranium_Cell', 'Encased_Industrial_Beam', 'Electromagnetic_Control_Rod', None, None)
            EUC_Target += results['Amount of Input 1']
            EIB_Target += results['Amount of Input 2']
            ECR_Target += results['Amount of Input 3']
            NFR_Target = 0
        elif Uranium_Fuel_Rod == 'Nuclear_Fuel_Unit':
            if y == Target_Resource:
                NFR_Target= Target_Resource_Amount
            results = craft(y, Uranium_Fuel_Rod, NFR_Target, 'Encased_Uranium_Cell', 'Electromagnetic_Control_Rod', 'Crystal_Oscillator', 'Beacon', None)
            EUC_Target += results['Amount of Input 1']
            ECR_Target += results['Amount of Input 2']
            COsc_Target += results['Amount of Input 3']
            Beacon_Target += results['Amount of Input 4']
            NFR_Target = 0
    elif y == "Nuclear_Pasta": 
        if y == Target_Resource:
            NP_Target= Target_Resource_Amount
        results = craft(y, 'Nuclear_Pasta', NP_Target, 'Copper_Powder', 'Pressure_Conversion_Cube', None, None, None)
        CPow_Target += results['Amount of Input 1']
        PCC_Target += results['Amount of Input 2']
        NP_Target = 0
    elif y == "Nuclear_Waste": 
        if y == Target_Resource:
            NW_Target= Target_Resource_Amount
        results = craft(y, 'Nuclear_Waste', NW_Target, 'Nuclear_Fuel_Rod', 'Water', None, None, None)
        NFR_Target += results['Amount of Input 1']
        Water_Target += results['Amount of Input 2']
        NW_Target = 0
    elif y == "Packaged_Alumina_Solution": 
        if y == Target_Resource:
            PAS_Target= Target_Resource_Amount
        results = craft(y, 'Packaged_Alumina_Solution', PAS_Target, 'Alumina_Solution', 'Empty_Canister', None, None, None)
        AS_Target += results['Amount of Input 1']
        EC_Target += results['Amount of Input 2']
        PAS_Target = 0
    elif y == "Packaged_Fuel": 
        print("1: Packaged_Fuel, 2:Diluted_Packaged_Fuel ")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Packaged_Fuel = "Packaged_Fuel"
        elif alternate == 2:
            Packaged_Fuel = "Diluted_Packaged_Fuel"
        else:
            print('Invalid, quitting out')
            quit()
        if Packaged_Fuel == 'Packaged_Fuel':
            if y == Target_Resource:
                PF_Target = Target_Resource_Amount
            results = craft(y, Packaged_Fuel, PF_Target, 'Fuel', 'Empty_Canister', None, None, None)
            Fuel_Target += results['Amount of Input 1']
            EC_Target += results['Amount of Input 2']
            PF_Target = 0
        elif Packaged_Fuel == 'Diluted_Packaged_Fuel':
            if y == Target_Resource:
                PF_Target= Target_Resource_Amount
            results = craft(y, Packaged_Fuel, PF_Target, 'Heavy_Oil_Residue', 'Packaged_Water', None, None, None)
            HOR_Target += results['Amount of Input 1']
            PW_Target += results['Amount of Input 2']
            PF_Target = 0
    elif y == "Packaged_Heavy_Oil_Residue": 
        if y == Target_Resource:
            PHOR_Target = Target_Resource_Amount
        results = craft(y, 'Packaged_Heavy_Oil_Residue', PHOR_Target, 'Heavy_Oil_Residue', 'Empty_Canister', None, None, None)
        HOR_Target += results['Amount of Input 1']
        EC_Target += results['Amount of Input 2']
        PHOR_Target = 0
    elif y == "Packaged_Liquid_Biofuel":
        if y == Target_Resource:
            PLB_Target = Target_Resource_Amount
        results = craft(y, 'Packaged_Liquid_Biofuel', PLB_Target, 'Liquid_Biofuel', 'Empty_Canister', None, None, None)
        LB_Target += results['Amount of Input 1']
        EC_Target += results['Amount of Input 2']
        PLB_Target = 0
    elif y == "Packaged Nitric Acid":
        if y == Target_Resource:
            PNA_Target = Target_Resource_Amount
        results = craft(y, 'Packaged_Nitric_Acid', PNA_Target, 'Nitric_Acid', 'Empty_Fluid_Tank', None, None, None)
        NA_Target += results['Amount of Input 1']
        EFT_Target += results['Amount of Input 2']
        PF_Target = 0
    elif y == "Packaged Nitrogen Gas":
        if y == Target_Resource:
            PNG_Target = Target_Resource_Amount
        results = craft(y, 'Packaged_Nitrogen_Gas', PNG_Target, 'Nitrogen_Gas', 'Empty_Fluid_Tank', None, None, None)
        Nitrogen_Gas_Target += results['Amount of Input 1']
        EFT_Target += results['Amount of Input 2']
        PNG_Target = 0
    elif y == "Packaged Oil":
        if y == Target_Resource:
          PO_Target = Target_Resource_Amount
        results = craft(y, 'Packaged_Oil', PO_Target, 'Crude_Oil', 'Empty_Canister', None, None, None)
        Crude_Oil_Target += results['Amount of Input 1']
        EC_Target += results['Amount of Input 2']
        PO_Target = 0
    elif y == "Packaged Sulfuric Acid":
        if y == Target_Resource:
          PSA_Target = Target_Resource_Amount
        results = craft(y, 'Packaged_Sulfuric_Acid', PSA_Target, 'Sulfuric_Acid', 'Empty_Canister', None, None, None)
        SA_Target += results['Amount of Input 1']
        EC_Target += results['Amount of Input 2']
        PSA_Target = 0
    elif y == "Packaged_Turbofuel": 
        if y == Target_Resource:
          PT_Target = Target_Resource_Amount
        results = craft(y, 'Packaged_Turbofuel', PT_Target, 'Turbofuel', 'Empty_Canister', None, None, None)
        Turbofuel_Target += results['Amount of Input 1']
        EC_Target += results['Amount of Input 2']
        PT_Target = 0
    elif y == "Packaged_Water": 
        if y == Target_Resource:
          PF_Target = Target_Resource_Amount
        results = craft(y, 'Packaged_Water', PW_Target, 'Water', 'Empty_Canister', None, None, None)
        Water_Target += results['Amount of Input 1']
        EC_Target += results['Amount of Input 2']
        PF_Target = 0
    elif y == "Petroleum_Coke": 
        if y == Target_Resource:
          PC_Target = Target_Resource_Amount
        results = craft(y, 'Petroleum_Coke', PC_Target, 'Heavy_Oil_Residue', None, None, None, None)
        HOR_Target += results['Amount of Input 1']
        PC_Target = 0
    elif y == "Plastic": 
        print("1: Plastic, 2: Residual_Plastic, 3: Recycled_Plastic")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Plastic = "Plastic"
        elif alternate == 2:
            Plastic = "Residual_Plastic"
        elif alternate == 3:
            Plastic = "Recycled_Plastic"
        else:
            print('Invalid, quitting out')
            quit()
        if Plastic == 'Plastic':
            if y == Target_Resource:
                Plastic_Target= Target_Resource_Amount
            results = craft(y, Plastic, Plastic_Target, 'Crude_Oil', None, None, None, 'Heavy_Oil_Residue')
            Crude_Oil_Target += results['Amount of Input 1']
            HOR_Target -= results['Amount of Byproduct']
            Plastic_Target = 0
        elif Plastic == 'Residual_Plastic':
            if y == Target_Resource:
                Plastic_Target= Target_Resource_Amount
            results = craft(y, Plastic, Plastic_Target, 'Polymer_Resin', 'Water', None, None, None)
            PR_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            Plastic_Target = 0
        elif Plastic == 'Recycled_Plastic':
            if y == Target_Resource:
                Plastic_Target= Target_Resource_Amount
            results = craft(y, Plastic, Plastic_Target, 'Rubber', 'Fuel', None, None, None)
            Rubber_Target += results['Amount of Input 1']
            Fuel_Target += results['Amount of Input 2']
            Plastic_Target = 0
    elif y == "Plutonium_Fuel_Rod": 
        print("1: Plutonium_Fuel_Rod, 2: Plutonium_Fuel_Unit")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Plutonium_Fuel_Rod = "Plutonium_Fuel_Rod"
        elif alternate == 2:
            Plutonium_Fuel_Rod = "Plutonium_Fuel_Unit"
        else:
            print('Invalid, quitting out')
            quit()
        if Plutonium_Fuel_Rod == 'Plutonium_Fuel_Rod':
            if y == Target_Resource:
                PFR_Target = Target_Resource_Amount
            results = craft(y, Plutonium_Fuel_Rod, PFR_Target, 'Encased_Plutonium_Cell', 'Steel_Beam', 'Electromagnetic_Control_Rod', 'Heat_Sink', None)
            EPC_Target += results['Amount of Input 1']
            SB_Target += results['Amount of Input 2']
            ECR_Target += results['Amount of Input 3']
            HS_Target += results['Amount of Input 4']
            PFR_Target = 0
        elif Plutonium_Fuel_Rod == 'Plutonium_Fuel_Unit':
            if y == Target_Resource:
                PFR_Target = Target_Resource_Amount
            results = craft(y, Plutonium_Fuel_Rod, PFR_Target, 'Encased_Plutonium_Cell', 'Pressure_Conversion_Cube', None, None, None)
            EPC_Target += results['Amount of Input 1']
            PCC_Target += results['Amount of Input 2']
            PFR_Target = 0
    elif y == "Plutonium_Pellets": 
        if y == Target_Resource:
            PP_Target = Target_Resource_Amount
        results = craft(y, y, PP_Target, 'Non_Fissile_Uranium', 'Nuclear_Waste', None, None, None)
        NFU_Target += results['Amount of Input 1']
        NW_Target += results['Amount of Input 2']
        PP_Target = 0
    elif y == "Plutonium_Waste": 
        if y == Target_Resource:
            PW_Target = Target_Resource_Amount
        results = craft(y, y, PW_Target, 'Plutonium_Fuel_Rod', 'Water', None, None, None)
        PFR_Target += results['Amount of Input 1']
        Water_Target += results['Amount of Input 2']
        PW_Target = 0
    elif y == "Polymer_Resin": 
        print("Polymer_Resin: 1: Fuel, 2: Polymer_Resin, 3: Heavy_Oil_Residue")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Polymer_Resin = "Fuel"
        elif alternate == 2:
            Polymer_Resin = "Polymer_Resin"
        elif alternate == 3:
            Polymer_Resin = "Heavy_Oil_Residue"
        else:
            print('Invalid, quitting out')
            quit()
        if Polymer_Resin == 'Fuel':
            if y == Target_Resource:
                PR_Target= Target_Resource_Amount
            results = craft(y, Polymer_Resin, PR_Target, 'Crude_Oil', None, None, None, 'Fuel')
            Crude_Oil_Target += results['Amount of Input 1']
            Fuel_Target -= results['Amount of Byproduct']
            PR_Target = 0
        elif Polymer_Resin == 'Polymer_Resin':
            if y == Target_Resource:
                PR_Target= Target_Resource_Amount
            results = craft(y, Polymer_Resin, PR_Target, 'Crude_Oil', None, None, None, 'Heavy_Oil_Residue')
            Crude_Oil_Target += results['Amount of Input 1']
            HOR_Target -= results['Amount of Byproduct']
            PR_Target = 0
        elif Polymer_Resin == 'Heavy_Oil_Residue':
            if y == Target_Resource:
                PR_Target= Target_Resource_Amount
            results = craft(y, Polymer_Resin, PR_Target, 'Crude_Oil', None, None, None, 'Heavy_Oil_Residue')
            Crude_Oil_Target += results['Amount of Input 1']
            PR_Target = 0
    elif y == "Pressure_Conversion_Cube": 
        if y == Target_Resource:
            PCC_Target = Target_Resource_Amount
        results = craft(y, y, PCC_Target, 'Fused_Modular_Frame', 'Radio_Control_Unit', None, None, None)
        FMF_Target += results['Amount of Input 1']
        RCU_Target += results['Amount of Input 2']
        PCC_Target = 0
    elif y == "Quartz_Crystal": 
        print("1: Quartz_Crystal, 2: Pure_Quartz_Crystal")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Quartz_Crystal = "Quartz_Crystal"
        elif alternate == 2:
            Quartz_Crystal = "Pure_Quartz_Crystal"
        else:
            print('Invalid, quitting out')
            quit()
        if Quartz_Crystal == 'Quartz_Crystal':
            if y == Target_Resource:
                QCrystal_Target = Target_Resource_Amount
            results = craft(y, Quartz_Crystal, QCrystal_Target, 'Raw_Quartz', None, None, None, None)
            Raw_Quartz_Target += results['Amount of Input 1']
            QCrystal_Target = 0
        elif Quartz_Crystal == 'Pure_Quartz_Crystal':
            if y == Target_Resource:
                QCrystal_Target = Target_Resource_Amount
            results = craft(y, Quartz_Crystal, QCrystal_Target, 'Raw_Quartz', 'Water', None, None, None)
            Raw_Quartz_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            QCrystal_Target = 0
    elif y == "Quickwire": 
        print("1: Quickwire, 2: Fused_Quickwire")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Quickwire = "Quickwire"
        elif alternate == 2:
            Quickwire = "Fused_Quickwire"
        else:
            print('Invalid, quitting out')
            quit()
        if Quickwire == 'Quickwire':
            if y == Target_Resource:
                Quickwire_Target = Target_Resource_Amount
            results = craft(y, Quickwire, Quickwire_Target, 'Caterium_Ingot', None, None, None, None)
            CatI_Target += results['Amount of Input 1']
            Quickwire_Target = 0
        elif Quickwire == 'Fused_Quickwire':
            if y == Target_Resource:
                Quickwire_Target = Target_Resource_Amount
            results = craft(y, Quickwire, Quickwire_Target, 'Caterium_Ingot', 'Copper_Ingot', None, None, None)
            CatI_Target += results['Amount of Input 1']
            CopI_Target += results['Amount of Input 2']
            Quickwire_Target = 0
    elif y == "Radio_Control_Unit": 
        print("1: Radio_Control_Unit, 2: Radio_Control_System, 3: Radio_Connection_Unit")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Radio_Control_Unit = "Radio_Control_Unit"
        elif alternate == 2:
            Radio_Control_Unit = "Radio_Control_System"
        elif alternate == 3:
            Radio_Control_Unit = "Radio_Connection_Unit"
        else:
            print('Invalid, quitting out')
            quit()
        if Radio_Control_Unit == 'Radio_Control_Unit':
            if y == Target_Resource:
                RCU_Target = Target_Resource_Amount
            results = craft(y, Radio_Control_Unit, RCU_Target, 'Aluminum_Casing', 'Crystal_Oscillator', 'Computer', None, None)
            AC_Target += results['Amount of Input 1']
            COsc_Target += results['Amount of Input 2']
            Computer_Target += results['Amount of Input 3']
            RCU_Target = 0
        elif Radio_Control_Unit == 'Radio_Control_System':
            if y == Target_Resource:
                RCU_Target = Target_Resource_Amount
            results = craft(y, Radio_Control_Unit, RCU_Target, 'Crystal_Oscillator', 'Circuit_Board', 'Aluminum_Casing', 'Rubber', None)
            COsc_Target += results['Amount of Input 1']
            CB_Target += results['Amount of Input 2']
            AC_Target += results['Amount of Input 3']
            Rubber_Target += results['Amount of Input 4']
            RCU_Target = 0
        elif Radio_Control_Unit == 'Radio_Connection_Unit':
            if y == Target_Resource:
                RCU_Target = Target_Resource_Amount
            results = craft(y, Radio_Control_Unit, RCU_Target, 'Heat_Sink', 'High_Speed_Connector', 'Quartz_Crystal', None, None)
            HS_Target += results['Amount of Input 1']
            HSC_Target += results['Amount of Input 2']
            QCrystal_Target += results['Amount of Input 3']
            RCU_Target = 0
    elif y == "Raw_Quartz": 
        Inputs.append('Raw_Quartz')
    elif y == "Reinforced_Iron_Plate": 
        print("1: Reinforced_Iron_Plate, 2: Adhered_Iron_Plate, 3: Bolted_Iron_Plate, 4: Stitched_Iron_Plate")
        alternate = int(input('1, 2, 3, or 4?'))
        if alternate == 1:
            Reinforced_Iron_Plate = "Reinforced_Iron_Plate"
        elif alternate == 2:
            Reinforced_Iron_Plate = "Adhered_Iron_Plate"
        elif alternate == 3:
            Reinforced_Iron_Plate = "Bolted_Iron_Plate"
        elif alternate == 4:
            Reinforced_Iron_Plate = "Stitched_Iron_Plate"
        else:
            print('Invalid, quitting out')
            quit()
        if Reinforced_Iron_Plate == "Reinforced_Iron_Plate":
            if y == Target_Resource:
                RIP_Target = Target_Resource_Amount
            results = craft(y, Reinforced_Iron_Plate, RIP_Target, 'Iron_Plate', 'Screw', None, None, None)
            IP_Target += results['Amount of Input 1']
            Screw_Target += results['Amount of Input 2']
            RIP_Target = 0
        elif Reinforced_Iron_Plate == "Adhered_Iron_Plate":
            if y == Target_Resource:
                RIP_Target = Target_Resource_Amount
            results = craft(y, Reinforced_Iron_Plate, RIP_Target, 'Iron_Plate', 'Rubber', None, None, None)
            IP_Target += results['Amount of Input 1']
            Rotor_Target += results['Amount of Input 2']
            RIP_Target = 0
        elif Reinforced_Iron_Plate == "Bolted_Iron_Plate":
            if y == Target_Resource:
                RIP_Target = Target_Resource_Amount
            results = craft(y, Reinforced_Iron_Plate, RIP_Target, 'Iron_Plate', 'Screw', None, None, None)
            IP_Target += results['Amount of Input 1']
            Screw_Target += results['Amount of Input 2']
            RIP_Target = 0
        elif Reinforced_Iron_Plate == "Stitched_Iron_Plate":
            if y == Target_Resource:
                RIP_Target = Target_Resource_Amount
            results = craft(y, Reinforced_Iron_Plate, RIP_Target, 'Iron_Plate', 'Wire', None, None, None)
            IP_Target += results['Amount of Input 1']
            Wire_Target += results['Amount of Input 2']
            RIP_Target = 0
    elif y == "Rifle_Cartridge": 
        if y == Target_Resource:
            RC_Target = Target_Resource_Amount
        results = craft(y, y, RC_Target, 'Beacon', 'Steel_Pipe', 'Black_Powder', 'Rubber', None)
        Beacon_Target += results['Amount of Input 1']
        SP_Target += results['Amount of Input 2']
        BP_Target += results['Amount of Input 3']
        Rubber_Target += results['Amount of Input 4']
        RC_Target = 0
    elif y == "Rotor": 
        print("1: Rotor, 2: Copper_Rotor, 3: Steel_Rotor")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Rotor = "Rotor"
        elif alternate == 2:
            Rotor = "Copper_Rotor"
        elif alternate == 3:
            Rotor = "Steel_Rotor"
        else:
            print('Invalid, quitting out')
            quit()
        if Rotor == "Rotor":
            if y == Target_Resource:
                Rotor_Target = Target_Resource_Amount
            results = craft(y, Rotor, Rotor_Target, 'Iron_Rod', 'Screw', None, None, None)
            IR_Target += results['Amount of Input 1']
            Screw_Target += results['Amount of Input 2']
            Rotor_Target = 0
        elif Rotor == "Copper_Rotor":
            if y == Target_Resource:
                Rotor_Target = Target_Resource_Amount
            results = craft(y, Rotor, Rotor_Target, 'Copper_Sheet', 'Screw', None, None, None)
            CSheet_Target += results['Amount of Input 1']
            Screw_Target += results['Amount of Input 2']
            Rotor_Target = 0
        elif Rotor == "Steel_Rotor":
            if y == Target_Resource:
                Rotor_Target = Target_Resource_Amount
            results = craft(y, Rotor, Rotor_Target, 'Steel_Pipe', 'Wire', None, None, None)
            SP_Target += results['Amount of Input 1']
            Wire_Target += results['Amount of Input 2']
            Rotor_Target = 0
    elif y == "Rubber": 
        print("1: Rubber, 2: Residual_Rubber, 3: Recycled_Rubber")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Rubber = "Rubber"
        elif alternate == 2:
            Rubber = "Residual_Rubber"
        elif alternate == 3:
            Rubber = "Recycled_Rubber"
        else:
            print('Invalid, quitting out')
            quit()
        if Rubber == 'Rubber':
            if y == Target_Resource:
                Rubber_Target= Target_Resource_Amount
            results = craft(y, Rubber, Rubber_Target, 'Crude_Oil', None, None, None, 'Heavy_Oil_Residue')
            Crude_Oil_Target += results['Amount of Input 1']
            HOR_Target -= results['Amount of Byproduct']
            Rubber_Target = 0
        elif Rubber == 'Residual_Plastic':
            if y == Target_Resource:
                Rubber_Target= Target_Resource_Amount
            results = craft(y, Rubber, Rubber_Target, 'Polymer_Resin', 'Water', None, None, None)
            PR_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            Rubber_Target = 0
        elif Rubber == 'Recycled_Plastic':
            if y == Target_Resource:
                Rubber_Target= Target_Resource_Amount
            results = craft(y, Rubber, Rubber_Target, 'Rubber', 'Fuel', None, None, None)
            Plastic_Target += results['Amount of Input 1']
            Fuel_Target += results['Amount of Input 2']
            Rubber_Target = 0
    elif y == "Screw": 
        print("1: Screw, 2: Casted_Screw, 3: Steel_Screw")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Screw = "Screw"
        elif alternate == 2:
            Screw = "Casted_Screw"
        elif alternate == 3:
            Screw = "Steel_Screw"
        else:
            print('Invalid, quitting out')
            quit()
        if Screw == 'Screw':
            if y == Target_Resource:
                Screw_Target = Target_Resource_Amount
            results = craft(y, Screw, Screw_Target, 'Iron_Rod', None, None, None, None)
            IR_Target += results['Amount of Input 1']
            Screw_Target = 0
        elif Screw == 'Casted_Screw':
            if y == Target_Resource:
                Screw_Target = Target_Resource_Amount
            results = craft(y, Screw, Screw_Target, 'Iron_Ingot', None, None, None, None)
            II_Target += results['Amount of Input 1']
            Screw_Target = 0
        elif Screw == 'Steel_Screw':
            if y == Target_Resource:
                Screw_Target = Target_Resource_Amount
            results = craft(y, Screw, Screw_Target, 'Steel_Beam', None, None, None, None)
            SB_Target += results['Amount of Input 1']
            Screw_Target = 0
    elif y == "Silica": 
        print("1: Silica, 2: Alumina_Solution, 3: Cheap_Silica")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Silica = "Silica"
        elif alternate == 2:
            Silica = "Alumina_Solution"
        elif alternate == 3:
            Silica = "Cheap_Silica"
        else:
            print('Invalid, quitting out')
            quit()
        if Silica == 'Silica':
            if y == Target_Resource:
                Silica_Target = Target_Resource_Amount
            results = craft(y, Silica, Silica_Target, 'Raw_Quartz', None, None, None, None)
            Raw_Quartz_Target += results['Amount of Input 1']
            Silica_Target = 0
        elif Silica == 'Alumina_Solution':
            if y == Target_Resource:
                Silica_Target = Target_Resource_Amount
            results = craft(y, Silica, Silica_Target, 'Bauxite', 'Water', None, None, 'Alumina_Solution')
            Bauxite_Target += results['Amount of Input 1']
            Water_Target += results['Amount of Input 2']
            AS_Target -= results['Amount of Byproduct']
            Silica_Target = 0
        elif Silica == 'Cheap_Silica':
            if y == Target_Resource:
                Silica_Target = Target_Resource_Amount
            results = craft(y, Silica, Silica_Target, 'Raw_Quartz', 'Limestone', None, None, None)
            Raw_Quartz_Target += results['Amount of Input 1']
            Limestone_Target += results['Amount of Input 2']
            Silica_Target = 0
    elif y == "Smart_Plating": 
        print("1: Smart_Plating, 2: Plastic_Smart_Plating")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Smart_Plating = "Smart_Plating"
        elif alternate == 2:
            Smart_Plating = "Plastic_Smart_Plating"
        else:
            print('Invalid, quitting out')
            quit()
        if Smart_Plating == 'Smart_Plating':
            if y == Target_Resource:
                SP_Target = Target_Resource_Amount
            results = craft(y, Smart_Plating, SP_Target, 'Reinforced_Iron_Plate', 'Rotor', None, None, None)
            RIP_Target += results['Amount of Input 1']
            Rotor_Target += results['Amount of Input 2']
            SP_Target = 0
        elif Smart_Plating == 'Plastic_Smart_Plating':
            if y == Target_Resource:
                SP_Target = Target_Resource_Amount
            results = craft(y, Smart_Plating, SP_Target, 'Reinforced_Iron_Plate', 'Rotor', 'Plastic', None, None)
            RIP_Target += results['Amount of Input 1']
            Rotor_Target += results['Amount of Input 2']
            Plastic_Target += results['Amount of Input 3']
            SP_Target = 0
    elif y == "Solid_Biofuel": 
        if y == Target_Resource:
            SB_Target = Target_Resource_Amount
        results = craft(y, y, SB_Target, 'Biomass', None, None, None, None)
        Biomass_Target += results['Amount of Input 1']
        SB_Target = 0
    elif y == "Spiked_Rebar": 
        if y == Target_Resource:
            SR_Target = Target_Resource_Amount
        results = craft(y, y, SR_Target, 'Iron_Rod', None, None, None, None)
        IR_Target += results['Amount of Input 1']
        SR_Target = 0
    elif y == "Stator": 
        print("1: Stator, 2: Quickwire_Stator")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Stator = "Stator"
        elif alternate == 2:
            Stator = "Quickwire_Stator"
        else:
            print('Invalid, quitting out')
            quit()
        if Stator == 'Stator':
            if y == Target_Resource:
                Stator_Target = Target_Resource_Amount
            results = craft(y, Stator, Stator_Target, 'Steel_Pipe', 'Wire', None, None, None)
            RIP_Target += results['Amount of Input 1']
            Wire_Target += results['Amount of Input 2']
            Stator_Target = 0
        elif Stator == 'Quickwire_Stator':
            if y == Target_Resource:
                Stator_Target = Target_Resource_Amount
            results = craft(y, Stator, Stator_Target, 'Steel_Pipe', 'Quickwire_Target', None, None, None)
            RIP_Target += results['Amount of Input 1']
            Quickwire_Target += results['Amount of Input 2']
            Stator_Target = 0
    elif y == "Steel_Beam": 
        if y == Target_Resource:
            SB_Target = Target_Resource_Amount
        results = craft(y, y, SB_Target, 'Steel_Ingot', None, None, None, None)
        SI_Target += results['Amount of Input 1']
        z = 0
        SB_Target = 0
    elif y == "Steel_Ingot": 
        print("1: Steel_Ingot, 2: Coke_Steel_Ingot, 3: Compacted_Steel_Ingot, 4: Solid_Steel_Ingot")
        alternate = int(input('1, 2, 3, or 4?'))
        if alternate == 1:
            Steel_Ingot = "Steel_Ingot"
        elif alternate == 2:
            Steel_Ingot = "Coke_Steel_Ingot"
        elif alternate == 3:
            Steel_Ingot = "Compacted_Steel_Ingot"
        elif alternate == 4:
            Steel_Ingot = "Solid_Steel_Ingot"
        else:
            print('Invalid, quitting out')
            quit()
        if Steel_Ingot == "Steel_Ingot":
            if y == Target_Resource:
                SI_Target = Target_Resource_Amount
            results = craft(y, Steel_Ingot, SI_Target, 'Iron_Ore', 'Coal', None, None, None)
            Iron_Ore_Target += results['Amount of Input 1']
            Rotor_Target += results['Amount of Input 2']
            SI_Target = 0
        elif Steel_Ingot == "Coke_Steel_Ingot":
            if y == Target_Resource:
                SI_Target = Target_Resource_Amount
            results = craft(y, Steel_Ingot, SI_Target, 'Iron_Ore', 'Petroleum_Coke', None, None, None)
            Iron_Ore_Target += results['Amount of Input 1']
            PC_Target += results['Amount of Input 2']
            SI_Target = 0
        elif Steel_Ingot == "Compacted_Steel_Ingot":
            if y == Target_Resource:
                SI_Target = Target_Resource_Amount
            results = craft(y, Steel_Ingot, SI_Target, 'Iron_Ore', 'Compacted_Coal', None, None, None)
            Iron_Ore_Target += results['Amount of Input 1']
            Compacted_Coal += results['Amount of Input 2']
            SI_Target = 0
        elif Steel_Ingot == "Solid_Steel_Ingot":
            if y == Target_Resource:
                SI_Target = Target_Resource_Amount
            results = craft(y, Steel_Ingot, SI_Target, 'Iron_Ingot', 'Coal', None, None, None)
            II_Target += results['Amount of Input 1']
            Coal_Target += results['Amount of Input 2']
            SI_Target = 0
    elif y == "Steel_Pipe": 
        if y == Target_Resource:
            SP_Target = Target_Resource_Amount
        results = craft(y, y, SP_Target, 'Steel_Ingot', None, None, None, None)
        SI_Target += results['Amount of Input 1']
        SP_Target = 0
    elif y == "Sulfur": 
        Inputs.append('Sulfur')
    elif y == "Sulfuric_Acid": 
        if y == Target_Resource:
            SA_Target = Target_Resource_Amount
        results = craft(y, y, SA_Target, 'Sulfur', 'Water', None, None, None)
        Sulfur_Target += results['Amount of Input 1']
        Water_Target += results['Amount of Input 2']
        SA_Target = 0
    elif y == "Supercomputer": 
        print("1: Supercomputer, 2: OC_Supercomputer, 3: Super_State_Computer")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Supercomputer = "Supercomputer"
        elif alternate == 2:
            Supercomputer = "OC_Supercomputer"
        elif alternate == 3:
            Supercomputer = "Super_State_Computer"
        else:
            print('Invalid, quitting out')
            quit()
        if Supercomputer == 'Supercomputer':
            if y == Target_Resource:
                Supercomputer_Target = Target_Resource_Amount
            results = craft(y, Supercomputer, Supercomputer_Target, 'Computer', 'AI_Limiter', 'High_Speed_Connector', 'Plastic', None)
            Computer_Target += results['Amount of Input 1']
            AIL_Target += results['Amount of Input 2']
            HSC_Target += results['Amount of Input 3']
            Plastic_Target += results['Amount of Input 4']
        elif Supercomputer == 'OC_Supercomputer':
            if y == Target_Resource:
                Supercomputer_Target = Target_Resource_Amount
            results = craft(y, Supercomputer, Supercomputer_Target, 'Radio_Control_Unit', 'Cooling_System', None, None, None)
            RCU_Target += results['Amount of Input 1']
            CSys_Target += results['Amount of Input 2']
            Supercomputer_Target = 0
        elif Supercomputer == 'Super_State_Computer':
            if y == Target_Resource:
                Supercomputer_Target = Target_Resource_Amount
            results = craft(y, Supercomputer, Supercomputer_Target, 'Computer', 'Electromagnetic_Control_Rod', 'Battery', 'Wire', None)
            Computer_Target += results['Amount of Input 1']
            AIL_Target += results['Amount of Input 2']
            HSC_Target += results['Amount of Input 3']
            Plastic_Target += results['Amount of Input 4']
            Supercomputer_Target = 0
    elif y == "Thermal_Propulsion_Rocket": 
        if y == Target_Resource:
            TPR_Target = Target_Resource_Amount
        results = craft(y, y, TPR_Target, 'Modular_Engine', 'Turbo_Motor', 'Cooling_System', 'Fused_Modular_Frame', None)
        ME_Target += results['Amount of Input 1']
        TM_Target += results['Amount of Input 2']
        CSys_Target += results['Amount of Input 3']
        FMF_Target += results['Amount of Input 4']
        TPR_Target = 0
    elif y == "Turbo_Motor": 
        print("1: Turbo_Motor, 2: Turbo_Rigour_Motor, 3: Turbo_Pressure_Motor")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Turbo_Motor = "Turbo_Motor"
        elif alternate == 2:
            Turbo_Motor = "Turbo_Rigour_Motor"
        elif alternate == 3:
            Turbo_Motor = "Turbo_Pressure_Motor"
        else:
            print('Invalid, quitting out')
            quit()
        if Turbo_Motor == 'Turbo_Motor':
            if y == Target_Resource:
                TM_Target = Target_Resource_Amount
            results = craft(y, Turbo_Motor, TM_Target, 'Cooling_System', 'Radio_Control_Unit', 'Motor', 'Rubber', None)
            CSys_Target += results['Amount of Input 1']
            RCU_Target += results['Amount of Input 2']
            Motor_Target += results['Amount of Input 3']
            Rubber_Target += results['Amount of Input 4']
            TM_Target = 0
        elif Turbo_Motor == 'Turbo_Rigour_Motor':
            if y == Target_Resource:
                TM_Target = Target_Resource_Amount
            results = craft(y, Turbo_Motor, TM_Target, 'Motor', 'Radio_Control_Unit', 'Electromagnetic_Control_Rod', 'Rotor', None)
            Motor_Target += results['Amount of Input 1']
            RCU_Target += results['Amount of Input 2']
            ECR_Target += results['Amount of Input 3']
            Rotor_Target += results['Amount of Input 4']
            TM_Target = 0
        elif Turbo_Motor == 'Turbo_Pressure_Motor':
            if y == Target_Resource:
                TM_Target = Target_Resource_Amount
            results = craft(y, Turbo_Motor, TM_Target, 'Motor', 'Pressure_Conversion_Cube', 'Packaged_Nitrogen_Gas', 'Stator', None)
            Motor_Target += results['Amount of Input 1']
            PCC_Target += results['Amount of Input 2']
            PNG_Target += results['Amount of Input 3']
            Stator_Target += results['Amount of Input 4']
            z = 0
            TM_Target = 0
    elif y == "Turbofuel": 
        print("1: Turbofuel, 2: Turbo_Heavy_Fuel, 3: Turbo_Blend_Fuel")
        alternate = int(input('1, 2, or 3?'))
        if alternate == 1:
            Turbofuel = "Turbofuel"
        elif alternate == 2:
            Turbofuel = "Turbo_Heavy_Fuel"
        elif alternate == 3:
            Turbofuel = "Turbo_Blend_Fuel"
        else:
            print('Invalid, quitting out')
            quit()
        if Turbofuel == 'Turbofuel':
            if y == Target_Resource:
                Turbofuel_Target = Target_Resource_Amount
            results = craft(y, Turbofuel, Turbofuel_Target, 'Fuel', 'Compacted_Coal', None, None, None)
            Fuel_Target += results['Amount of Input 1']
            Compacted_Coal_Target += results['Amount of Input 2']
            Turbofuel_Target = 0
        elif Turbofuel == 'Turbo_Heavy_Fuel':
            if y == Target_Resource:
                Turbofuel_Target = Target_Resource_Amount
            results = craft(y, Turbofuel, Turbofuel_Target, 'Heavy_Oil_Residue', 'Compacted_Coal', None, None, None)
            HOR_Target += results['Amount of Input 1']
            Compacted_Coal_Target += results['Amount of Input 2']
            Turbofuel_Target = 0
        elif Turbofuel == 'Turbo_Blend_Fuel':
            if y == Target_Resource:
                Turbofuel_Target = Target_Resource_Amount
            results = craft(y, Turbofuel, Turbofuel_Target, 'Fuel', 'Heavy_Oil_Residue', 'Sulfur', 'Petroleum_Coke', None)
            Fuel_Target += results['Amount of Input 1']
            HOR_Target += results['Amount of Input 2']
            Sulfur_Target += results['Amount of Input 3']
            PC_Target += results['Amount of Input 4']
            Turbofuel_Target = 0
    elif y == "Uranium": 
        Inputs.append('Uranium')
    elif y == "Versatile_Framework": 
        print("1: Versatile_Framework, 2: Flexible_Framework")
        alternate = int(input('1 or 2'))
        if alternate == 1:
            Versatile_Framework = "Versatile_Framework"
        elif alternate == 2:
            Versatile_Framework = "Flexible_Framework"
        else:
            print('Invalid, quitting out')
            quit()
        if Versatile_Framework == 'Versatile_Framework':
            if y == Target_Resource:
                VF_Target = Target_Resource_Amount
            results = craft(y, Versatile_Framework, VF_Target, 'Modular_Frame', 'Steel_Beam', None, None, None)
            MF_Target += results['Amount of Input 1']
            SB_Target += results['Amount of Input 2']
            VF_Target = 0
        elif Versatile_Framework == 'Flexible_Framework':
            if y == Target_Resource:
                VF_Target = Target_Resource_Amount
            results = craft(y, Versatile_Framework, VF_Target, 'Modular_Frame', 'Steel_Beam', 'Rubber', None, None)
            MF_Target += results['Amount of Input 1']
            SB_Target += results['Amount of Input 2']
            Rubber_Target += results['Amount of Input 3']
            VF_Target = 0
    elif y == "Water": 
        Inputs.append('Water')
    elif y == "Wire": 
        print("1: Wire, 2: Fused_Wire, 3: Iron_Wire, 4: Caterium_Wire")
        alternate = int(input('1, 2, 3, or 4?'))
        if alternate == 1:
            Wire = "Wire"
        elif alternate == 2:
            Wire = "Fused_Wire"
        elif alternate == 3:
            Wire = "Iron_Wire"
        elif alternate == 4:
            Wire = "Caterium_Wire"
        else:
            print('Invalid, quitting out')
            quit()
        if Wire == 'Wire':
            if y == Target_Resource:
                Wire_Target = Target_Resource_Amount
            results = craft(y, Wire, Wire_Target, 'Copper_Ingot', None, None, None, None)
            CopI_Target += results['Amount of Input 1']
            Wire_Target = 0
        elif Wire == 'Fused_Wire':
            if y == Target_Resource:
                Wire_Target = Target_Resource_Amount
            results = craft(y, Wire, Wire_Target, 'Copper_Ingot', 'Caterium_Ingot', None, None, None)
            CopI_Target += results['Amount of Input 1']
            CatI_Target += results['Amount of Input 2']
            Wire_Target = 0
        elif Wire == 'Iron_Wire':
            if y == Target_Resource:
                Wire_Target = Target_Resource_Amount
            results = craft(y, Wire, Wire_Target, 'Iron_Ingot', None, None, None, None)
            II_Target += results['Amount of Input 1']
            Wire_Target = 0
        elif Wire == 'Caterium_Wire':
            if y == Target_Resource:
                Wire_Target = Target_Resource_Amount
            results = craft(y, Wire, Wire_Target, 'Caterium_Ingot', None, None, None, None)
            CatI_Target += results['Amount of Input 1']
            Wire_Target = 0
    elif y == "Wood":
        Inputs.append('Wood')
    else:
        print('Failed to find recipie for item:', y, '\n Please contact creator')
    table2 = table2.append(results, ignore_index=True)
# if CSV_Output:
table2 = table2.append(pd.DataFrame({'Recipe': 'Inputs', 'Building': 'Inputs', 'Amount of Buliding(s)': 'Inputs', 'Input 1': 'Inputs', 'Amount of Input 1': 'Inputs', 'Input 2': 'Inputs', 'Amount of Input 2': 'Inputs', 'Input 3': 'Inputs', 'Amount of Input 3': 'Inputs', 'Input 4': 'Inputs', 'Amount of Input 4': 'Inputs', 'Byproduct': 'Inputs', 'Amount of Byproduct': 'Inputs'}, index = ['Recipe', 'Building', 'AmountofBuliding(s)', 'Input1', 'AmountofInput1', 'Input2', 'AmountofInput2', 'Input3', 'AmountofInput3', 'Input4', 'AmountofInput4', 'Byproduct', 'AmountofByproduct']), ignore_index = True)
# for item in Inputs:
# if item == "Alien_Carapace":
table2 = table2.append(pd.DataFrame({'Recipe': "Alien_Carapace", 'Building': Alien_Carapace_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == "Alien_Organs":
table2 = table2.append(pd.DataFrame({'Recipe': 'Alien_Organs', 'Building': Alien_Organs_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == "Bauxite":
table2 = table2.append(pd.DataFrame({'Recipe': 'Bauxite', 'Building': Bauxite_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == "Caterium_Ore":
table2 = table2.append(pd.DataFrame({'Recipe': 'Caterium_Ore', 'Building': Caterium_Ore_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == "Coal":
table2 = table2.append(pd.DataFrame({'Recipe': 'Coal', 'Building': Coal_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Copper_Ore':
table2 = table2.append(pd.DataFrame({'Recipe': 'Copper_Ore', 'Building': Copper_Ore_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Crude_Oil':
table2 = table2.append(pd.DataFrame({'Recipe': 'Crude_Oil', 'Building': Crude_Oil_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Flower_Petals':
table2 = table2.append(pd.DataFrame({'Recipe': 'Flower_Petals', 'Building': Flower_Petals_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Iron_Ore':
table2 = table2.append(pd.DataFrame({'Recipe': 'Iron_Ore', 'Building': Iron_Ore_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Leaves':
table2 = table2.append(pd.DataFrame({'Recipe': 'Leaves', 'Building': Leaves_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Limestone':
table2 = table2.append(pd.DataFrame({'Recipe': 'Limestone', 'Building': Limestone_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Mycelia':
table2 = table2.append(pd.DataFrame({'Recipe': 'Mycelia', 'Building': Mycelia_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Nitrogen_Gas':
table2 = table2.append(pd.DataFrame({'Recipe': 'Nitrogen_Gas', 'Building': Nitrogen_Gas_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Raw_Quartz':
table2 = table2.append(pd.DataFrame({'Recipe': 'Raw_Quartz', 'Building': Raw_Quartz_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Sulfur':
table2 = table2.append(pd.DataFrame({'Recipe': 'Sulfur', 'Building': Sulfur_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Uranium':
table2 = table2.append(pd.DataFrame({'Recipe': 'Uranium', 'Building': Uranium_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Water':
table2 = table2.append(pd.DataFrame({'Recipe': 'Water', 'Building': Water_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# elif item == 'Wood':
table2 = table2.append(pd.DataFrame({'Recipe': 'Wood', 'Building': Wood_Target}, index = ['Recipe', 'Building']), ignore_index = True)
# else:
#   print('Mistake:', item, 'has not been added to input list, please contact creator')
# Inputs.remove(item)
print('Inputs:')
print('Alien_Carapace: ', Alien_Carapace_Target)
print('Alien_Organs: ', Alien_Organs_Target)
print('Bauxite: ', Bauxite_Target)
print('Caterium_Ore: ', Caterium_Ore_Target)
print('Coal: ', Coal_Target)
print('Copper_Ore: ', Copper_Ore_Target)
print('Crude_Oil: ', Crude_Oil_Target)
print('Flower_Petals: ', Flower_Petals_Target)
print('Iron_Ore: ', Iron_Ore_Target)
print('Leaves: ', Leaves_Target)
print('Limestone: ', Limestone_Target)
print('Mycelia: ', Mycelia_Target)
print('Nitrogen_Gas: ', Nitrogen_Gas_Target)
print('Raw_Quartz: ', Raw_Quartz_Target)
print('Sulfur: ', Sulfur_Target)
print('Uranium: ', Uranium_Target)
print('Water: ', Water_Target)
print('Wood: ', Wood_Target)

print('Byproducts:')
table2 = table2.append(pd.DataFrame({'Recipe': 'Byproducts', 'Building': 'Byproducts', 'Amount of Buliding(s)': 'Byproducts', 'Input 1': 'Byproducts', 'Amount of Input 1': 'Byproducts', 'Input 2': 'Byproducts', 'Amount of Input 2': 'Byproducts', 'Input 3': 'Byproducts', 'Amount of Input 3': 'Byproducts', 'Input 4': 'Byproducts', 'Amount of Input 4': 'Byproducts', 'Byproduct': 'Byproducts', 'Amount of Byproduct': 'Byproducts'}, index = ['Recipe', 'Building', 'AmountofBuliding(s)', 'Input1', 'AmountofInput1', 'Input2', 'AmountofInput2', 'Input3', 'AmountofInput3', 'Input4', 'AmountofInput4', 'Byproduct', 'AmountofByproduct']), ignore_index = True)
for item in Byproducts:
  print('\n')
  if item == 'Silica' and float(Silica_Target) < 0:
      table2 = table2.append(pd.DataFrame({'Recipe': 'Silica Byproduct', 'Building': abs(Silica_Target)}, index = ['Recipe', 'Building']), ignore_index = True)
      print('Silica Byproduct:', abs(Silica_Target))
  elif item == 'Water' and float(Water_Target) < 0:
      table2 = table2.append(pd.DataFrame({'Recipe': 'Water Byproduct', 'Building': abs(Water_Target)}, index = ['Recipe', 'Building']), ignore_index = True)
      print('Water Byproduct:', abs(Water_Target))
  elif item == 'Polymer_Resin' and float(PR_Target) < 0:
      table2 = table2.append(pd.DataFrame({'Recipe': 'Polymer Resin Byproduct', 'Building': abs(PR_Target)}, index = ['Recipe', 'Building']), ignore_index = True)
      print('Polymer Resin Byproduct:', abs(PR_Target))
  elif item == 'Heavy_Oil_Residue' and float(HOR_Target) < 0:
      table2 = table2.append(pd.DataFrame({'Recipe': 'Heavy Oil Residue Byproduct', 'Building': abs(HOR_Target)}, index = ['Recipe', 'Building']), ignore_index = True)
      print('Heavy Oil Residue Byproduct:', abs(HOR_Target))
  elif item == 'Fuel' and float(Fuel_Target) < 0:
      table2 = table2.append(pd.DataFrame({'Recipe': 'Fuel Byproduct', 'Building': abs(Fuel_Target)}, index = ['Recipe', 'Building']), ignore_index = True)
      print('Fuel Byproduct:', abs(Fuel_Target))
  else:
      print('Mistake:', item, 'has not been added to byproduct list, please contact creator')
  Byproducts.remove(item)
table2 = table2.drop_duplicates(ignore_index=True)
table2 = table2.dropna(subset=['Building'])
print(table2)
table2.to_csv(save_location)
