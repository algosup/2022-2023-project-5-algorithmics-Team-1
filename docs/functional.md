# Krug Champagne Winery Software Functional Specification

## Overview

You are working on building software for Krug Champagne's winery, which specializes in producing sparkling wine using the traditional "méthode champenoise". Your goal is to create a software solution that optimizes the blending process while avoiding the wine to oxidate if the tank is left partially full/empty and minimizing the number of steps required to produce the desired flavor profile.

The blending process involves combining different still wines from different vineyards and grape varieties to create a consistent flavor profile. The winery has various sizes of tanks that can be reused multiple times in the blending process. Due to the risk of oxidation, tanks should never be left partially full or empty.

The software will focus on the blending stage. Your objective is to produce the closest result to the formula given by the Cellar Master while ensuring the correct number of moves and no crashes or half-full tanks. The formula provided by the Cellar Master will vary from year to year and should be an input to the software.

## Requirements
### Inputs

The software should accept the following inputs:

The formula provided by the Cellar Master for the current year's blend.
This formula will be a list of percentages paired with the corresponding tank, indicating the proportion of each still wine that should be used in the blend. For example, a formula of `[(0.2 t1), (0.3 t2), (0.5 t3)]` means that 20% of tank1, 30% of tank2, and 50% tank3 should be used in the blend.
The size of each of the 330 tanks in the winery.
The maximum capacity of each tank.
The current level of wine in each tank.

> **Note**
> Assuming each pipe can be connected to any tank, the software should not require any additional inputs.

### Outputs

The software should produce the following outputs:

A sequence of moves to transfer the wine from the various tanks to create the desired blend.
A status report of each tank after the blending process is complete.
The number of steps required to complete the blending process.

### Constraints

The software must operate under the following constraints:

No tank should be left partially full or empty.
The software must run in a reasonable amount of time to provide a solution.
The software must not crash or produce half-full or half-empty tanks.

## Approach

To achieve the goals outlined in the requirements, the software will use an algorithm that optimizes the blending process based on the Cellar Master's formula. This algorithm will create a population of potential blending sequences, evaluate their fitness against the desired formula, and evolve new solutions until an optimal blend is found.

## Deliverables

The final software solution will include the following deliverables:

Source code written a programming language defined in the Technical Specification.
Documentation describing the algorithm, including its parameters and tuning.
A user manual that describes how to use the software and the input/output formats.

## Evaluation Criteria

The software will be evaluated based on the following criteria:

Correctness: The software should not crash or produce half-full or half-empty tanks.
Accuracy: The software should produce a blend that is as close as possible to the formula provided by the Cellar Master.
Idiomatic Style: The source code should be written in a clean, organized, and idiomatic style that adheres to best practices in the chosen programming language.
Minimum Steps: The software should produce the blend in the minimum number of steps possible.