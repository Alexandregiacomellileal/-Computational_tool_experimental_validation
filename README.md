# Experimental validation of the computational tool

## Overview
This repository provides details on the experimental validation for the computational tool proposed in the associated research paper. Validation experiments were conducted using a scaled-down multi-grounded system, as described below. The study involved measurements using four methods: (i) Fall-of-Potential at low frequency, (ii) Fall-of-Potential at high frequency (25 kHz), (iii) Clamp-on ground meter, and (iv) Proposed. The primary objective was to compare the measurements results with the individual actual turbine grounding resistance (Rf, measured in Ω) obtained through Fall-of-Potential method at low frequency before the installation of horizontal electrodes.

## Experimental Setup

The proposed lumped parameter model underwent experimental validation using a reduced-scale model of the grounding system detailed in Section 2.2 of the associated research paper. The grounding system was constructed with three 4 mm thick steel cylinders spaced 7.5 m apart, interconnected to a 15 m horizontal electrode. Each steel cylinder, symbolizing a turbine grounding, boasted a radius of 19.7 cm and a height of 43 cm, while the copper horizontal electrode had a cross-sectional area of 35 $mm^2$. The horizontal electrode was buried 12 cm below the ground. Each cylinder electrode was positioned on the same side at a distance of 28.5 cm from the horizontal electrode. The radial connection between the cylinder and horizontal electrodes was established using an insulated wire with a cross-sectional area of 10 $mm^2$, with a length of $s$ + 0.1 $(m)$. The soil had an average low-frequency resistivity of 86.8 Ω·m.  In Figure 1, the schematic of the grounding system is presented, capturing key moments during both its construction and the measurement process.

**Figure 1**
![experiment_git_hub (003)](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/assets/96079504/9a3bbea2-8b20-4a73-ab05-3252bbfae3fe)

## Measurement Methods

### Low-Frequency Fall-of-Potential Method using Flat-slope-rule

In Figure 2, we illustrate the application of the Fall-of-Potential (FoP) method to measure the low-frequency grounding resistance in our case study grounding system. The measuring leads have been laid along a line orthogonal to the horizontal electrode's length. A voltage $Vp$ (V) was applied by a low-frequency instrument between the electrode of interest (EE) and the auxiliary current-return electrode (CE), inducing a current $Ic$ (A) to circulate. To minimize mutual resistances, the CE was strategically placed at a substantial distance XC (m) 45 meters from EE.

Next, a Potential Electrode (PE) was positioned at a distance XP (m) from the current injection point in EE. The precise placement of the PE termed the compensation point, is crucial. It must be free from the influences of both the EE and CE. To ensure this, we systematically moved the PE in 0.1XC increments between EE and CE, capturing resistance reading at each step calculated as $( \frac{V_p}{I_c} )$. The detection of three consecutive, evenly spaced, and constant resistance readings (differences lower than 3%) was indicative of true EE grounding resistance, a principle known as the Flat-slope-rule [^4]. 

For comparison purposes with other approaches aiming to estimate just the individual grounding resistances of turbines in the case study's grounding system, the FoP low-frequency measurements $Zmed_{FoP}^{LF}$ ($\Omega$) were taken at three different current injection points in EE, identified as 1, 2, and 3. However, it is essential to highlight that such a value is representative of the true grounding resistance of the entire grounding system of the case study. The instrument used in FoP Low-frequency Method was the Minipa MTR-1522.

[^4]: IEEE guide for measuring earth resistivity, ground impedance, and earth surface potentials of a grounding system, IEEE Std 81-2012 (Revision of IEEE Std 81-1983) (2012) 1–86.


**Figure 2**
<img width="2076" alt="image" src="https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/assets/96079504/0e2ae89d-a060-4546-9149-f108f7bcc970">


### High-Frequency Fall-of-Potential Method

Ground resistance meters typically operate at low frequencies, carefully chosen to avoid interference from the power system frequency and its lower harmonics. Exceptions to this general rule exist, particularly in the case of instruments operating at 25 kHz. These instruments have gained popularity due to their presumed ability to measure grounding impedance without the need to disconnect shielded wires. Originally designed for evaluating the grounding impedance of transmission line towers, these high-frequency meters have found practical applications beyond their initial scope.

One notable application is in wind farms, where these 25 kHz instruments have been repurposed to estimate the impedance of the grounding resistances of individual turbines. This adaptation involves leveraging the frequency decoupling of grounding adjacent to the measurement point.

Figure 3 shows an illustration of the High-frequency method (HFM) in the case study's grounding system. The high-frequency method consists of an adaption of the Fop method using a high-frequency current injection between the electrode of interest (EE) and the current electrode (CE). The fundamental concept behind the high-frequency method is to inject a current $Ic$ (A) at a higher frequency, allowing it to predominantly circulate through the grounding turbine of interest, canceling the impact of the surrounding ground circuit. Thus, the ratio of the voltage potential $Vp$ (V) to the injected current $Ic$ provides the grounding impedance of the turbine at 25 kHz. 

**Figure 3**
<img width="2436" alt="image" src="https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/assets/96079504/874cbb0d-c3c0-48d3-9f7f-d570b1b35d16">

To minimize mutual resistances, the CE was strategically placed at a substantial distance XC (m) 45 meters from EE. Next, a Potential Electrode (PE) was positioned at a distance XP (m) from the current injection point in EE. A common issue in measuring grounding resistance at the specific frequency of 25 kHz is the pronounced coupling effect between the leads connected to auxiliary electrodes for current and potential. This effect becomes particularly significant when these leads are laid in parallel within the ground. To address this challenge, it was adopted the configuration outlined in Figure 2. In this setup, the auxiliary electrodes for the current and the potential probes should be positioned in opposite directions along a line orthogonal to the horizontal electrode direction. This arrangement mitigates the coupling effect, providing a more accurate measurement of grounding resistance at 25 kHz [^1]. 

We systematically moved the PE in 0.1XC increments in the opposite direction away from CE, capturing resistance reading at each step calculated as $( \frac{V_p}{I_c} )$. The detection of three consecutive, evenly spaced, and constant resistance readings (differences lower than 3%) was indicative of the turbine of interest grounding impedance at 25 kHz.

For comparison purposes with other approaches aiming to estimate just the individual grounding resistances of turbines in the case study's grounding system, the FoP high-frequency measurements $Zmed_{FoP}^{HF}$ ($\Omega$) were taken at three different current injection points in EE, identified as 1, 2, and 3. It's noteworthy that the assessment of grounding impedance at high frequencies is particularly suited for understanding the behavior of the grounding circuit under the influence of atmospheric discharge-related currents. The instruments used in HFM method were Tektronix A6302 50 MHz AC Current Probe, Tektronix AM503 Current Probe Amplifier, Hantek DSO5102P 2 Channel Digital Storage Oscilloscope 100 Mhz.

[^1]: S. Visacro, F. H. Silveira and C. H. D. Oliveira, "Measurements for Qualifying the Lightning Response of Tower-Footing Electrodes of Transmission Lines," in IEEE Transactions on Electromagnetic Compatibility, vol. 61, no. 3, pp. 719-726, June 2019, doi: 10.1109/TEMC.2019.2915188.

### Clamp-on Ground Meter Method

Measurements Zmed <sub>CGM</sub> were conducted using the UT-278A clamp-on meter attached to the interconnection cable linking each cylinder (representing the turbine grounding) to the horizontal electrode.

**Figure 4**

<img width="450" alt="image" src="https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/assets/96079504/224314f7-6d26-4264-884d-75a5cc9f7a91">

### Proposed Method

The proposed solution, depicted in Figure 5, involves a systematic sequence of tasks. Initially, the process begins by accessing the technical documentation of the wind farm’s grounding system. Following this, a comprehensive survey of the parameters necessary for calculating the components of the equivalent electrical circuit is conducted. Next, an appropriate electrical circuit model is chosen for the wind farm’s grounding system. To account for variations and uncertainties, a sensitivity study is performed on parameters influencing the grounding resistance and capacitance of turbines and horizontal electrodes. Tolerance ranges are defined, considering factors such as construction non-conformities or soil and electrode deterioration. A sample vector $\textbf{P}$ is generated, with each element representing a specific grounding resistance or capacitance of a turbine or horizontal electrode. An element representing the parameter $k$ is also included to replicate the mutual coupling effect between the turbine and horizontal electrodes during clamp-on ground meter measurements. Uniform distributions are used to generate vector elements within their corresponding tolerance ranges set by the sensitivity study. The equivalent circuit of the grounding system is then loaded based on the values from the sample vector $\textbf{P}$. Subsequently, a computational simulation of the clamp-on method is performed in the equivalent electrical circuit. Instrument reading values are obtained in each turbine, resulting in an output sample vector **Z**<sub>med</sub>. This process is repeated $m$ times to generate input-output pairs [**Z**<sub>med</sub> ; **R**<sub>f</sub>] stored in a database $\mathbb{D}_{m\times2n}$ , being $n$ the numbers of turbines of the wind farm. The database is then utilized to train a machine-learning model. The trained model undergoes validation and testing to ensure accuracy and reliability. Finally, the trained model is used to predict the values of the resistances **R**<sub>f est</sub> for the n turbines based on the readings obtained via the clamp-on method during wind farm periodic inspections **Z**<sub>med </sub> . This systematic approach ensures a logical progression from data collection and circuit modeling to machine learning application, facilitating accurate predictions of turbine grounding resistances.


**Figure 5**
<img width="1752" alt="image" src="https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/assets/96079504/2fc2c2cf-371e-4eaf-b3ed-65a3858e3a96">

To assist readers who wish to replicate the experiment, we have attached two files python to the repository. The algorithm [[final_160124.py](https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/blob/main/final_160124.py)] generate the P vectors, involves performing the ATP simulation in mass, obtaining the input-output pairs [**Z**<sub>med</sub> ; **R**<sub>f</sub>], and storaging them in a database $\mathbb{D}_{1000\times6}$. Additionally, for creating the machine learning model to predict the target variables, we utilized [[final_varios_algoritmos.py](https://github.com/Alexandregiacomellileal/Computational_tool_experimental_validation/blob/main/final_varios_algoritmos.py)]. The use of 1000 input-output pairs [**Z**<sub>med</sub> ; **R**<sub>f</sub>] was sufficient to accurate results. The data was splited into two groups, with 70% of the pairs allocated for training and 30% for testing. The Mean Absolute Percentage Error obtained was 4.328 \%, and the percentage of predictions with an absolute error greater than 10\% was 5.111\%.

## Measurement Data and Percentage Error

### Table 1 - Measurement Data

| Turbine | Rf ($\Omega$) | $Zmed_{FoP}^{LF}$ ($\Omega$)| $Zmed_{FoP}^{HF}$ ($\Omega$) | $Zmed_{CGM}$ ($\Omega$)| $Zmed_{Proposed}$ ($\Omega$)|
|-------------|------------------------|--------------|-----------------|-----------------|-----------------|
| 1          | 40.0      | 6.28                    | 10.33        | 37.8            | 40.0            |
| 2          | 49.0      | 6.28                   | 9.61         | 40.5            | 48.3            |
| 3          | 39.5    | 6.25                   | 9.86         | 37.5            | 39.5            |

In Table 1, taken as benchmarked Rf ($\Omega$) represents the actual turbine grounding resistance measured by the Low-Frequency Fall-of-Potential Method using Flat-slope-rule, and $Zmed_{method}$ represents the estimated turbine grounding resistance by other measurement method evaluated in this research. The "Evaluated Measurement Method Percentage Error" is then calculated as $((Zmed_{method} - Rf) / Rf) * 100$.

### Table 2 - Percentage error in estimated the turbine grounding resistance Rf

| Turbine  | $Error_{FoP}^{LF}$ (%) | $Error_{FoP}^{HF}$ (%)| $Error_{CGM}$ (%)| $Error_{Proposed}$ (%)|
|------------------------------|----------------|------------------|------------------|------------------|
| 1        | -84.3                   | -74.2         | -5.5            | -0.1            |
| 2         | -87.2                   | -80.4         | -17.3           | -1.5            |
| 3          | -84.2                | -75.0         | -5.1            | 0.1             |






