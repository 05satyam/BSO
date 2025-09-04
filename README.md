# Blindfolded Spriderman Optimization
- Blindfolded Spider-man Optimization: A Single-Point Metaheuristics Suitable for Continuous and Discrete Spaces (arXiv:2505.17069, May 19, 2025).
- This was my research thesis work during my M.S.
- If you use this repository for research or teaching, please cite the paper above.

## Overview
- Blindfolded Spider-man Optimization (BSO) is a single-point metaheuristic designed to work in both continuous and discrete search spaces.
- The search traces a piecewise-linear trajectory—at each step, it “jumps” from the current solution to a better neighbor, echoing how Spider-man would leap between buildings toward a taller one, but blindfolded (guided only by objective feedback).
- The research evaluates BSO on 16 continuous benchmarks and a discrete Unbounded Knapsack instance, comparing against Whale Optimization, Grey Wolf Optimization, Particle Swarm Optimization, Simulated Annealing, Threshold Accepting, and Buggy Pinball Optimization;
- BSO shows strong results, outperforming other single-point methods considered.
- Main script: BlindfoldedSpidermanOptimization.py


## Note:
- This repository contains an end-to-end implementation of Blindfolded Spider-man Optimization (BSO) as described in the paper.
- The codebase is older and not fully polished (limited tests, sparse docs), but the core algorithm and evaluation workflow are in place.
- I’ve included simple runners to reproduce paper-style results; expect minor deviations due to randomness and implementation details.
- If you have any questions, kindly connect.

### Thank you
