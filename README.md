## Computational_tool_experimental_validation - Reduced Scale

## Measurement Methods

### Low-Frequency Fall-of-Potential Method 

**Figure 1**
<img width="2071" alt="image" src="https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/assets/96079504/93ecf1d2-bf40-417c-87ba-05becf5aef29">

### High-Frequency Fall-of-Potential Method

**Figure 2**
<img width="2435" alt="image" src="https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/assets/96079504/dca3dd3d-abc3-46c6-b430-6bc2db7ba648">

A common issue in measuring grounding resistance at the specific frequency of 25 kHz is the pronounced coupling effect between the leads connected to auxiliary electrodes for current and voltage. This effect becomes particularly significant when these leads are laid in parallel within the ground. To address this challenge, it is recommended to adopt the configuration outlined in Figure 1. In this setup, the auxiliary electrodes for the current and the voltage probes should be positioned in opposite directions along a line orthogonal to the horizontal electrode direction. This arrangement mitigates the coupling effect, providing a more accurate measurement of grounding resistance at 25 kHz [^1].


[^1]: S. Visacro, F. H. Silveira and C. H. D. Oliveira, "Measurements for Qualifying the Lightning Response of Tower-Footing Electrodes of Transmission Lines," in IEEE Transactions on Electromagnetic Compatibility, vol. 61, no. 3, pp. 719-726, June 2019, doi: 10.1109/TEMC.2019.2915188.

### Clamp-on Ground Meter Method

**Figure 3**

<img width="600" alt="image" src="https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/assets/96079504/224314f7-6d26-4264-884d-75a5cc9f7a91">

### Proposed Method

**Figure 4**
<img width="1752" alt="image" src="https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/assets/96079504/2fc2c2cf-371e-4eaf-b3ed-65a3858e3a96">




## Measurement Data and Percentage Error

### Table 1 - Measurement Data

| Turbine | Rf ($\Omega$) | $Zmed_{FoP}^{LF}$ ($\Omega$)| $Zmed_{FoP}^{HF}$ ($\Omega$) | $Zmed_{CGM}$ ($\Omega$)| $Zmed_{Proposed}$ ($\Omega$)|
|-------------|------------------------|--------------|-----------------|-----------------|-----------------|
| 1          | 40.0      | 6.28                    | 10.33        | 37.8            | 40.0            |
| 2          | 49.0      | 6.28                   | 9.61         | 40.5            | 48.3            |
| 3          | 39.5    | 6.25                   | 9.86         | 37.5            | 39.5            |

Actual Rf represents the actual turbine grounding resistance, and $Zmed_{method}$ represents the estimated turbine grounding resistance by the measurement method. The "Percentage Error" is then calculated as $((Zmed_{method} - Rf) / Rf) * 100$.

### Table 2 - Percentage error in estimated the turbine grounding resistance Rf

| Turbine  | $Error_{FoP}^{LF}$ (%) | $Error_{FoP}^{HF}$ (%)| $Error_{CGM}$ (%)| $Error_{Proposed}$ (%)|
|------------------------------|----------------|------------------|------------------|------------------|
| 1        | -84.3                   | -74.2         | -5.5            | -0.1            |
| 2         | -87.2                   | -80.4         | -17.3           | -1.5            |
| 3          | -84.2                | -75.0         | -5.1            | 0.1             |






