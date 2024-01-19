## Computational_tool_experimental_validation - Reduced Scale

## Measurement Methods

### Low-Frequency Fall-of-Potential Method using Flat-slope-rule

In Figure 1, we illustrate the application of the Fall-of-Potential (FoP) method to measure the low-frequency grounding resistance in our case study grounding system. The measuring leads have been laid along a line orthogonal to the horizontal electrode's length. A voltage $Vp$ (V) was applied by a low-frequency instrument between the electrode of interest (EE) and the auxiliary current-return electrode (CE), inducing a current $Ic$ (A) to circulate. To minimize mutual resistances, the CE was strategically placed at a substantial distance XC (m) 45 meters from EE.

Next, a Potential Electrode (PE) was positioned at a distance XP (m) from the current injection point in EE. The precise placement of the PE termed the compensation point, is crucial. It must be free from the influences of both the EE and CE. To ensure this, we systematically moved the PE in 0.1XC increments between EE and CE, capturing resistance reading at each step calculated as $( \frac{V_p}{I_c} )$. The detection of three consecutive, evenly spaced, and constant resistance readings (differences lower than 3%) was indicative of true EE grounding resistance, a principle known as the Flat-slope-rule [^4]. 

For comparison purposes with other approaches aiming to estimate just the individual grounding resistances of turbines in the case study's grounding system, the FoP low-frequency measurements $Zmed_{FoP}^{LF}$ ($\Omega$) were taken at three different current injection points in EE, identified as 1, 2, and 3. However, it is essential to highlight that such a value is representative of the true grounding resistance of the entire grounding system of the case study. The instrument used was the MTR-1522.

[^4]: IEEE guide for measuring earth resistivity, ground impedance, and earth surface potentials of a grounding system, IEEE Std 81-2012 (Revision of IEEE Std 81-1983) (2012) 1–86.


**Figure 1**
<img width="2076" alt="image" src="https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/assets/96079504/0e2ae89d-a060-4546-9149-f108f7bcc970">


### High-Frequency Fall-of-Potential Method using Flat-slope-rule

Ground resistance meters typically operate at low frequencies, carefully chosen to avoid interference from the power system frequency and its lower harmonics. Exceptions to this general rule exist, particularly in the case of instruments operating at 25 kHz. These instruments have gained popularity due to their presumed ability to measure grounding impedance without the need to disconnect shielded wires. Originally designed for evaluating the grounding impedance of transmission line towers, these high-frequency meters have found practical applications beyond their initial scope.

One notable application is in wind farms, where these 25 kHz instruments have been repurposed to estimate the impedance of the grounding resistances of individual turbines. This adaptation involves leveraging the frequency decoupling of grounding adjacent to the measurement point.

Figure 2 shows an illustration of the High-frequency method (HFM) in the case study's grounding system. The high-frequency method consists of an adaption of the Fop method using a high-frequency current injection between the electrode of interest (EE) and the current electrode (CE). The fundamental concept behind the high-frequency method is to inject a current $Ic$ (A) at a higher frequency, allowing it to predominantly circulate through the grounding turbine of interest, canceling the impact of the surrounding ground circuit. Thus, the ratio of the voltage potential $Vp$ (V) to the injected current $Ic$ provides the grounding impedance of the turbine at 25 kHz $Zmed_{FoP}^{HF}$ ($\Omega$).

**Figure 2**
<img width="2436" alt="image" src="https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/assets/96079504/874cbb0d-c3c0-48d3-9f7f-d570b1b35d16">


A common issue in measuring grounding resistance at the specific frequency of 25 kHz is the pronounced coupling effect between the leads connected to auxiliary electrodes for current and potential. This effect becomes particularly significant when these leads are laid in parallel within the ground. To address this challenge, it is recommended to adopt the configuration outlined in Figure 2. In this setup, the auxiliary electrodes for the current and the potential probes should be positioned in opposite directions along a line orthogonal to the horizontal electrode direction. This arrangement mitigates the coupling effect, providing a more accurate measurement of grounding resistance at 25 kHz [^1].

For comparison purposes with other approaches aiming to estimate just the individual grounding resistances of turbines in the case study's grounding system, the FoP high-frequency measurements $Zmed_{FoP}^{HF}$ ($\Omega$) were taken at three different current injection points in EE, identified as 1, 2, and 3. It's noteworthy that the assessment of grounding impedance at high frequencies is particularly suited for understanding the behavior of the grounding circuit under the influence of atmospheric discharge-related currents.


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






