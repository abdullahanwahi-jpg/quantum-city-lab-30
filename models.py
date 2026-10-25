"""Transparent, illustrative research models. No scientific superiority claims."""
from dataclasses import dataclass
from math import exp, log2, sqrt
from typing import Callable

@dataclass(frozen=True)
class Module:
    id: int
    title: str
    section: str
    description: str
    inputs: tuple  # (label, default, min, max, unit)
    output: str
    unit: str
    caveat: str

Q='Quantum Computing'; N='Carbon Nanomaterials'; C='Carbon Emissions'; S='Sensors & Diamond Sensors'; P='Quantum Photonics'
MODULES = [
 Module(1,'Bell-State Simulator',Q,'Ideal two-qubit Bell-state sampling.',(('Shots',1000,100,100000,'shots'),('Bit-flip probability',0.0,0.0,0.5,'fraction')),'Expected parity','%', 'Idealized independent bit-flip model, not a quantum hardware prediction.'),
 Module(2,'IBM Hardware Results',Q,'Explore recorded IBM Kingston counts from Experiment 02.',(('Shots',1000,100,100000,'shots'),('Observed mismatch',0.265,0,1,'fraction')),'Correct parity','%', 'Historical recorded experiment: 00=253, 01=208, 10=57, 11=482; changing inputs creates a scenario, not new IBM data.'),
 Module(3,'Statistical Confidence',Q,'Wilson interval for a binary outcome rate.',(('Shots',1000,30,100000,'shots'),('Mismatch proportion',0.265,0,1,'fraction')),'95% CI upper bound','%', 'Wilson interval assumes independent Bernoulli trials; hardware measurements can be correlated.'),
 Module(4,'Qubit Pair Screening',Q,'Compare estimated two-qubit operation success.',(('CZ error probability',0.00207,0,0.2,'fraction'),('CZ gate count',1,1,100,'gates')),'Estimated CZ survival','%', 'Heuristic based only on gate errors, excluding readout, decoherence and compilation effects.'),
 Module(5,'Optimized Hardware Results',Q,'Explore recorded IBM Kingston counts from Experiment 05.',(('Shots',1000,100,100000,'shots'),('Observed mismatch',0.008,0,1,'fraction')),'Correct parity','%', 'Historical recorded experiment: 00=481, 01=0, 10=8, 11=511; runs were not a controlled paired comparison.'),
 Module(6,'Circuit Depth Trade-off',Q,'Estimate success as circuit depth increases.',(('Gate error probability',0.005,0,0.2,'fraction'),('Circuit depth',8,1,500,'layers')),'Estimated survival','%', 'Simplified independent-error approximation; not measured circuit fidelity.'),
 Module(7,'Shots & Precision',Q,'Approximate binomial standard error.',(('Shots',1000,30,1000000,'shots'),('Event probability',0.5,0.001,0.999,'fraction')),'95% margin','percentage points', 'Normal approximation for independent measurements.'),
 Module(8,'Quantum Job Budget',Q,'Estimate runtime budget from average job duration.',(('Runtime budget',600,1,100000,'seconds'),('Seconds per job',30,1,10000,'seconds')),'Estimated jobs','jobs', 'Illustrative; IBM bills runtime based on actual usage and plan.'),
 Module(9,'Quantum vs Classical Benchmark',Q,'Compare measured runtimes from a supplied scenario.',(('Classical runtime',120,0.01,10000000,'seconds'),('Quantum runtime',80,0.01,10000000,'seconds')),'Speed ratio','x', 'Scenario only; comparable workloads and overheads must be documented.'),
 Module(10,'Quantum Pilot ROI',Q,'Estimate simple annual return on a quantum pilot.',(('Annual savings',300000,0,100000000,'USD'),('Annual operating cost',120000,0,100000000,'USD'),('Initial investment',600000,1,100000000,'USD')),'Simple annual ROI','%', 'Not discounted cash flow; speculative benefits must be validated.'),
 Module(11,'CNT CVD Production',N,'Estimate saleable nanotube output.',(('Feedstock input',1000,0,1000000,'kg'),('Conversion yield',0.3,0,1,'fraction'),('Quality acceptance',0.8,0,1,'fraction')),'Saleable CNT','kg', 'Illustrative yield assumptions, not a verified industrial recipe.'),
 Module(12,'Graphene Manufacturing',N,'Compare annual saleable graphene output.',(('Batch feed',1000,0,1000000,'kg'),('Process yield',0.4,0,1,'fraction'),('Quality acceptance',0.85,0,1,'fraction')),'Saleable graphene','kg', 'Production quality and grade depend on process and metrology.'),
 Module(13,'CNT Interconnect Design',N,'Explore simplified resistance scaling.',(('Baseline resistance',100,0.001,1000000,'ohm'),('Length multiplier',1,0.1,20,'x'),('Area multiplier',1,0.1,20,'x')),'Estimated resistance','ohm', 'R proportional to length/area is an illustrative bulk approximation, not a validated CNT device model.'),
 Module(14,'Nanomaterial Quality Control',N,'Estimate accepted production batches.',(('Total batches',100,1,100000,'batches'),('Defect rate',0.12,0,1,'fraction')),'Accepted batches','batches', 'Assumes independent uniform defect rate; actual QC requires measured distributions.'),
 Module(15,'Nanocarbon Factory Economics',N,'Estimate simplified annual operating profit.',(('Annual saleable output',10000,0,10000000,'kg'),('Selling price',200,0,1000000,'USD/kg'),('Variable cost',120,0,1000000,'USD/kg'),('Fixed annual cost',400000,0,100000000,'USD')),'Annual operating profit','USD', 'Excludes depreciation, financing, taxes, working capital and CAPEX.'),
 Module(16,'GHG Footprint (Scopes 1+2+3)',C,'Add separately supplied emissions inventories.',(('Scope 1',500,0,100000000,'tCO2e'),('Scope 2',300,0,100000000,'tCO2e'),('Scope 3',1200,0,100000000,'tCO2e')),'Total footprint','tCO2e', 'Scope boundaries, data quality, factor vintage and double counting must be checked.'),
 Module(17,'Industrial Energy Emissions',C,'Estimate electricity-associated emissions.',(('Electricity consumption',500000,0,10000000000,'kWh'),('Grid emission factor',0.4,0,5,'kgCO2e/kWh')),'Electricity emissions','tCO2e', 'Emission factor is an editable placeholder, not an official UAE factor.'),
 Module(18,'Carbon Reduction Portfolio',C,'Estimate residual emissions after reductions.',(('Baseline emissions',1000,0,100000000,'tCO2e'),('Efficiency reduction',0.15,0,1,'fraction'),('Clean power reduction',0.25,0,1,'fraction')),'Residual emissions','tCO2e', 'Sequential independent reductions assumed; avoid overlapping interventions.'),
 Module(19,'Carbon Capture Economics',C,'Estimate capture cost per net tonne avoided.',(('Gross CO2 captured',10000,1,100000000,'tCO2'),('Capture rate',0.9,0.01,1,'fraction'),('Project emissions',1000,0,100000000,'tCO2e'),('Annual cost',800000,0,1000000000,'USD')),'Cost per net tonne avoided','USD/tCO2e', 'Net avoided emissions require lifecycle accounting and permanent storage verification.'),
 Module(20,'Smart City Carbon Pathway',C,'Project emissions after compounded annual reduction.',(('Baseline emissions',100000,0,1000000000,'tCO2e'),('Annual reduction',0.05,0,0.99,'fraction'),('Years',10,1,100,'years')),'Projected emissions','tCO2e', 'Scenario forecast, not a city inventory or policy commitment.'),
 Module(21,'Sensor Signal-to-Noise',S,'Estimate SNR from signal amplitude and RMS noise.',(('Signal amplitude',10,0.000001,1000000,'mV'),('RMS noise',1,0.000001,1000000,'mV')),'Signal-to-noise ratio','dB','Signal and noise must use the same bandwidth and impedance; no calibration implied.'),
 Module(22,'NV Diamond Magnetic Sensitivity',S,'Illustrative NV-center shot-noise sensitivity.',(('Photon count rate',1000000,1,100000000000,'counts/s'),('Optical contrast',0.03,0.0001,1,'fraction'),('Linewidth',1000000,1,1000000000,'Hz')),'Estimated sensitivity','nT/sqrt(Hz)','Uses 28 GHz/T electron gyromagnetic ratio; simplified shot-noise bound, not measured sensitivity.'),
 Module(23,'NV Diamond Thermometry',S,'Temperature change from NV zero-field splitting frequency shift.',(('Frequency shift',74,0,1000000,'kHz'),('Temperature coefficient',74,1,1000,'kHz/K')),'Temperature change','K','Magnitude only; requires device-specific calibration and temperature-dependent coefficient.'),
 Module(24,'Optical Photon Statistics',S,'Photon shot-noise-limited relative uncertainty.',(('Incident photons',1000000,1,1000000000000,'counts'),('Collection efficiency',0.2,0.0001,1,'fraction')),'Relative photon noise','%','Poisson approximation, excluding dark counts and technical noise.'),
 Module(25,'Smart City Sensor Network',S,'Estimate number of sensors using density and redundancy.',(('Area',50,0.01,10000000,'km²'),('Sensor density',12,0.01,100000,'sensors/km²'),('Redundancy factor',1.25,1,10,'x')),'Installed sensors','sensors','Planning proxy, not a validated coverage or engineering network design.'),
 Module(26,'Photonic Qubit Fiber Transmission',P,'Estimate single-photon channel transmission over fiber.',(('Fiber distance',25,0,1000,'km'),('Fiber attenuation',0.2,0,10,'dB/km'),('Connector loss',1,0,30,'dB')),'Photon transmission probability','%','Loss-only model; ignores source statistics, detector efficiency, polarization drift and dark counts.'),
 Module(27,'Single-Photon Detection',P,'Estimate detected photon rate from source flux and efficiencies.',(('Source photon rate',1000000,0,1e12,'photons/s'),('Channel transmission',0.5,0,1,'fraction'),('Detector efficiency',0.8,0,1,'fraction')),'Expected detection rate','counts/s','Ideal efficiency model; ignores dead time, saturation, afterpulsing and background.'),
 Module(28,'Photonic Interferometer Visibility',P,'Estimate interference visibility from maximum and minimum intensity.',(('Maximum intensity',100,0.000001,1e9,'counts'),('Minimum intensity',10,0,1e9,'counts')),'Fringe visibility','%','Visibility is not proof of single-photon interference or quantum advantage.'),
 Module(29,'Quantum Key Distribution Link Budget',P,'Illustrative sifted-key throughput for BB84-like basis selection.',(('Optical pulse rate',1000000,1,1e12,'pulses/s'),('Detection probability',0.02,0,1,'fraction'),('Basis sift fraction',0.5,0,1,'fraction')),'Sifted bits per second','bits/s','Not a secure key rate; QBER, finite-key analysis and device assumptions are required.'),
 Module(30,'Photonic Chip Power Budget',P,'Estimate optical output power after chip insertion loss.',(('Input optical power',10,0,1e9,'mW'),('Chip insertion loss',3,0,100,'dB'),('Coupling loss',2,0,100,'dB')),'Output optical power','mW','Passive loss only; excludes nonlinearities, thermal drift and amplifiers.'),
]

def calculate(module_id: int, values: list[float]) -> float:
    m=MODULES[module_id-1]
    if len(values)!=len(m.inputs): raise ValueError('Input count mismatch')
    v=[float(x) for x in values]
    for x, spec in zip(v,m.inputs):
        if not spec[2] <= x <= spec[3]: raise ValueError(f'{spec[0]} out of allowed range')
    if module_id==1: return 100*(1-v[1])
    if module_id in (2,5): return 100*(1-v[1])
    if module_id==3:
        n,p=v; z=1.96; center=(p+z*z/(2*n))/(1+z*z/n); radius=z*sqrt((p*(1-p)+z*z/(4*n))/n)/(1+z*z/n); return 100*(center+radius)
    if module_id==4: return 100*(1-v[0])**v[1]
    if module_id==6: return 100*(1-v[0])**v[1]
    if module_id==7: return 196*sqrt(v[1]*(1-v[1])/v[0])
    if module_id==8: return int(v[0]//v[1])
    if module_id==9: return v[0]/v[1]
    if module_id==10: return 100*(v[0]-v[1])/v[2]
    if module_id in (11,12): return v[0]*v[1]*v[2]
    if module_id==13: return v[0]*v[1]/v[2]
    if module_id==14: return v[0]*(1-v[1])
    if module_id==15: return v[0]*(v[1]-v[2])-v[3]
    if module_id==16: return sum(v)
    if module_id==17: return v[0]*v[1]/1000
    if module_id==18: return v[0]*(1-v[1])*(1-v[2])
    if module_id==19:
        net=v[0]*v[1]-v[2]
        if net<=0: raise ValueError('Net avoided emissions must be positive')
        return v[3]/net
    if module_id==20: return v[0]*(1-v[1])**v[2]
    if module_id==21: return 20*__import__('math').log10(v[0]/v[1])
    if module_id==22: return 1e9*v[2]/(28e9*v[1]*sqrt(v[0]))
    if module_id==23: return v[0]/v[1]
    if module_id==24: return 100/sqrt(v[0]*v[1])
    if module_id==25: return v[0]*v[1]*v[2]
    if module_id==26: return 100*10**(-(v[0]*v[1]+v[2])/10)
    if module_id==27: return v[0]*v[1]*v[2]
    if module_id==28:
        if v[1]>v[0]: raise ValueError('Minimum intensity must not exceed maximum')
        return 100*(v[0]-v[1])/(v[0]+v[1])
    if module_id==29: return v[0]*v[1]*v[2]
    if module_id==30: return v[0]*10**(-(v[1]+v[2])/10)
    raise ValueError('Unknown module')

HISTORICAL = {
 'experiment_01': {'source':'user PowerShell screenshot','type':'local simulation','shots':1000,'00':520,'01':0,'10':0,'11':480},
 'experiment_02': {'source':'user PowerShell screenshot','type':'IBM hardware','backend':'ibm_kingston','shots':1000,'00':253,'01':208,'10':57,'11':482,'mismatch_percent':26.5},
 'experiment_03': {'source':'user PowerShell screenshot','type':'local analysis','wilson_interval_percent':[23.86,29.32],'note':'Wilson interval of Experiment 02, no new hardware job'},
 'experiment_04': {'source':'user PowerShell screenshot','type':'backend calibration screening','pair':[148,149],'cz_error_estimate':0.00207,'note':'No new hardware job'},
 'experiment_05': {'source':'user PowerShell screenshot','type':'IBM hardware','backend':'ibm_kingston','pair':[148,149],'shots':1000,'00':481,'01':0,'10':8,'11':511,'mismatch_percent':0.8},
}
