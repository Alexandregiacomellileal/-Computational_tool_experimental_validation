## Computational_tool_experimental_validation - Reduced Scale

<img width="935" alt="image" src="https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/assets/96079504/65399b18-67e1-4f0a-b62e-33b8e6a44171">


### Overview

This repository contains the experimental validation details for the computational tool presented in the associated research paper. The validation experiments were conducted using a scaled-down multi-grounded system, as described below.

### Experimental Setup

The proposed lumped parameter model underwent experimental validation using a reduced-scale model of the grounding system detailed in Section 2.2 of the associated research paper. The grounding system was constructed with three 4 mm thick steel cylinders spaced 7.5 m apart, interconnected to a 15 m horizontal electrode. Each steel cylinder, symbolizing a turbine grounding, boasted a radius of 19.7 cm and a height of 43 cm, while the copper horizontal electrode had a cross-sectional area of 35 $mm^2$. The horizontal electrode was buried 12 cm below the ground. Each cylinder electrode was positioned on the same side at a distance of 28.5 cm from the horizontal electrode. The radial connection between the cylinder and horizontal electrodes was established using an insulated wire with a cross-sectional area of 10 $mm^2$, with a length of $s$ + 0.1 $(m)$. The soil had an average low-frequency resistivity of 86.8 Ω·m.  In Figure 1, the schematic of the grounding system is presented, capturing key moments during both its construction and the measurement process.

**Figure 1**
![experiment_git_hub (003)](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/assets/96079504/9a3bbea2-8b20-4a73-ab05-3252bbfae3fe)


### Measurements clamp-on ground meter

Measurements Zmed <sub>meter</sub> were conducted using the UT-278A clamp-on meter attached to the interconnection cable linking each cylinder (representing the turbine grounding) to the horizontal electrode. The measurements were compared with simulated readings Zmed <sub>LPM</sub> obtained from the proposed equivalent electrical circuit model. The instrument resolution is 0.1 Ω, and its accuracy is ± (1.0% + 1 dig) for a range from 1.0 to 49.9 Ω. For a range from 50.0 to 99.5 Ω, its resolution is 0.5 Ω, and its accuracy is ± (1.5% + 1 dig).

### Circuit Theory Modeling

The electrical circuit for the measurements was established and simulated in ATP to acquire the meter readings Zmed<sub>LPM</sub>, adhering to the procedures outlined in Section 2.2 of the corresponding research paper. Additionally, for comparative analysis, both the lumped parameter modeling from our previous work [^1] and the distributed parameter model used in [^2] were established and simulated in ATP. The ATP files used by the authors are [[23_model_rod1.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/23_model_rod1.acp)], [[23_model.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/23_model.acp)], [[23_model_rod3.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/23_model_rod3.acp)], [[celulapi_COMSOL_k_RLC.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/celulapi_COMSOL_k_RLC.acp)], [[celulapi_COMSOL_k_RLC_rod1.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/celulapi_COMSOL_k_RLC_rod1.acp)], [[celulapi_COMSOL_k_RLC_rod3.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/celulapi_COMSOL_k_RLC_rod3.acp)], and [[dpm_cgm_3_paper_Nappu.acp](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/dpm_cgm_3_paper_Nappu.acp)].

### Measuring Apparent Resistivities

The apparent resistivity ($\rho_a^{wtg}$) of the turbines is computed using the formula $\ \rho_a^{wtg} = 2 \ \pi \ r_{eq}^{wtg} \ R_{FoP}^{wtg} \ (\Omega.m) $, where $R_{FoP}^{wtg}$ represents the grounding resistance measured by the low-frequency Fall-of-Potential Method ($\Omega$), and $r_{eq}^{wtg}$ is the radius of a semi-spherical electrode with an equivalent ground contact area as the turbine foundation (m).

The apparent resistivity ($\rho_a^{he}$) observed by the horizontal electrode is determined by averaging the apparent resistivities ($\rho_a^{wtg}$) of the turbines in their extremities, and this is cross-validated using the low-frequency Fall-of-Potential method.

In this study, the apparent resistivity for the cylinder electrodes was determined to be 81.1, 99.3, and 80.1 Ω·m, while the apparent resistivity for the horizontal electrode sections was recorded at 90.2 and 89.7 Ω·m. The measurements were conducted using the digital earth meter MTR-1522. The instrument resolution is 0.01 Ω, and its accuracy is ± (2.0% + 20 dig) for a range from 0.01 to 39.99 Ω. For a range from 40.0 to 400.0 Ω, its resolution is 0.1 Ω, and its accuracy is ± (2.0% + 3 dig).


### $k$ Parameter Estimation

In our quest to mitigate the impact of mutual coupling in measurements and address distortions arising from the utilization of an equivalent semi-spherical representation of the horizontal electrode, we are engaged in refining the estimation process. Our focus is on enhancing accuracy and reliability by systematically assessing and adjusting the parameters involved in the measurement system.

According to Subsection 2.2.1 of the associated research article, the parameter k was estimated to be 0.69 for an s value of 28.5 cm. The COMSOL models for k estimation are [[turbine_reduce_two_sphere_k.mph](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/turbine_reduce_two_sphere_k.mph)] and [[turbine_reduce_he_k.mph](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/turbine_reduce_he_k.mph)]. Figure 2 displays images generated through the COMSOL Multiphysics computer simulation software. The framed image above the Figure 2 is associated with the estimation of $Zmed_{lumped}^{short} (\Omega)$ using the COMSOL model [[turbine_reduce_two_sphere_k.mph](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/turbine_reduce_two_sphere_k.mph)], while the one below is related to the estimation of $Zmed_{wire}^\infty (\Omega)$ using [[turbine_reduce_he_k.mph](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/turbine_reduce_he_k.mph)]. 



**Figure 2**
![COMSOL_top](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/assets/96079504/511ee963-843b-4130-85e0-bb90eaf88c03)

$Zmed_{wire}^\infty (\Omega)$ is the clamp-on reading taken with the turbine grounding and the horizontal electrode separated by a large distance, in a such way that the mutual couplings between these elements can be considered negligible. On the other hand, the $Zmed_{lumped}^{short} (\Omega)$ is the clamp-on reading taken with the turbine grounding and the horizontal electrode separated by a smaller distance $s$ and with the horizontal electrode being represented by two semi-spherical electrodes spaced so that one does not be influenced by the other. In this manner, the grounding of the turbine under test will only influence a section of the horizontal electrode defined by the nearest hemispherical electrode and will not affect its furthest portion, characterized by the farthest hemispherical electrode. In other words, we are dividing the horizontal electrode into two parts: one that has mutual coupling with the turbine grounding and another that does not. This representation introduces an error term that we call hemispheric error. This error attempts to quantify the distortion introduced by the modeling approach, acknowledging that the situation is not entirely realistic. The cumulative impact of the hemispheric error and the actual mutual impedance between turbine grounding and the horizontal electrode on the measurement loop determines the value of the parameter $k$. This parameter is crucial for the precision of our proposal and can be estimated using the formula $k = \frac{Zmed_{lumped}^{short}} {Zmed_{wire}^\infty}$. Check out [Lumped-parameter-modeling-for-wind-farm-grounding](https://github.com/Alexandregiacomellileal/Lumped-parameter-modeling-for-wind-farm-grounding) for more details.

Table 1 displays results obtained at an average soil resistivity of 86.8 $(\Omega.m)$. Notably, the COMSOL simulation results reveal that the parameter $k$ remains consistent for a specified value of $s$ across a wide range of soil resistivities, spanning from 20 to 10240 $(\Omega.m)$.

**Table 1**
| $s \ (m)$ | $\rho \ (\Omega.m)$| ${Zmed}_{lumped}^{short} (\Omega) $ | ${Zmed}_{wire}^\infty (\Omega)$| $k$             |
|---------|---------|------------------------|-----------------------|-----------------|
| 0.28   | 86.8  | 41.62               | 60.63              | 0.69     |

In situations where access to simulation software for investigating the parameter $k$ in the measuring circuit is not available, the graph presented in Figure 3 becomes a valuable resource for estimating $k$ based on the distance $s$ between the grounding elements. To facilitate this estimation, we have developed a Python algorithm, available in [[k_parameter_estimator.py](https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/blob/main/k_parameter_estimator.py)], which proves particularly useful in scenarios involving reduced-scale 1:40 cylindrical-shaped turbine foundations with multiple driven pillars made of reinforced concrete and horizontal electrodes


**Figure 3**                   

<img src="https://github.com/Alexandregiacomellileal/lumped_parameter_model_experimental_validation_alternative/assets/96079504/abe2c145-1357-4577-b243-e09fb58d44f7" width="600" height="400">
