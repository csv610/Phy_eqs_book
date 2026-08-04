# Physics Equations Reference

A self-contained LaTeX book that derives the most important equations of physics from first principles. Every chapter takes a single equation, derives it step by step, states its assumptions and limitations, and connects it to the broader physical picture.

## Overview

Physics is built on a small number of fundamental equations — from the fall of an apple to the expansion of the universe. This book collects the most important expressions from classical mechanics, electromagnetism, thermodynamics, fluid dynamics, relativity, and quantum mechanics, and derives each one from scratch.

Understanding where an equation comes from and what it truly means is the difference between memorizing physics and thinking like a physicist. The derivations are kept self-contained, so the book works both as a reference and as a study companion.

## Features

- **77 equations derived from first principles** across the full spectrum of physics
- **Mathematical derivations** that are self-contained and reproducible
- **Assumptions & limitations** stated explicitly for every equation
- **Reality Mapping** — connects each result to the physical world and real phenomena
- **Cross-references** that encourage nonlinear, topic-driven reading
- **Equation summary & comprehensive index** for quick lookup
- **Historical notes** on the discoverers and context of each equation

## Table of Contents

The book is organized into three parts:

1. **Fundamental Equations** — conservation laws, Newton's laws, Maxwell's equations, thermodynamics, relativity, and quantum mechanics in one overview chapter.
2. **Individual Equations** — one chapter per equation, including:

   | Field | Equations |
   |---|---|
   | Classical Mechanics | Kinematic Equations, Work–Energy, Conservation of Energy, Torque, Rotational Kinetic Energy, Euler–Lagrange, Hamilton's Equations, Kepler's Third Law |
   | Electromagnetism | Gauss's Law (E & M), Faraday's Law, Ampère–Maxwell, Lorentz Force, Biot–Savart, Liénard–Wiechert Potentials, Maxwell Relations |
   | Thermodynamics & Statistical Mechanics | Carnot Efficiency, Clausius–Clapeyron, Entropy, Ideal Gas, Maxwell–Boltzmann, Fermi–Dirac, Bose–Einstein, Partition Function, Sackur–Tetrode |
   | Fluid & Continuum Mechanics | Continuity, Euler Equation, Navier–Stokes, Bernoulli, Boundary Layer, Vorticity, Reynolds Transport Theorem, Euler–Bernoulli Beam, Plate Equation, Stress Equilibrium, Stress–Strain |
   | Waves, Optics & Acoustics | Wave Equation, Wave Equation in Solids, Electromagnetic Wave, Snell's Law, Fresnel Equations, Thin Lens, Mirror, Single-Slit & Fraunhofer Diffraction, Young's Double Slit, Skin Depth, Telegraph |
   | Relativity & Gravitation | Time Dilation, Length Contraction, Mass–Energy Equivalence, Relativistic Momentum & Energy, Schwarzschild Metric, Geodesic Equation, Friedmann Equation |
   | Quantum Mechanics | Schrödinger Equation, Dirac Equation, Klein–Gordon, Pauli Equation, Heisenberg Equation & Uncertainty, De Broglie Wavelength, Probability Current, Quantum Continuity |
   | Statistical & Other | Diffusion, Heat, Laplace's and Poisson's Equations, Planck Radiation, Wien's Law, Stefan–Boltzmann, Boltzmann Transport |

3. **Appendices** — equation summary, comprehensive index, and historical notes.

## Building

The book is written in LaTeX and requires a standard TeX distribution (e.g., [TeX Live](https://tug.org/texlive/) or [MacTeX](https://tug.org/mactex/)).

```bash
pdflatex physics_equations.tex
pdflatex physics_equations.tex
```

Run `pdflatex` a second time to resolve the table of contents and cross-references, or use `latexmk`:

```bash
latexmk -pdf physics_equations.tex
```

The compiled book is written to `physics_equations.pdf`.

## Project Structure

```
physics_equations.tex         Main LaTeX source (document setup + structure)
chapters/
  Fundamental_Equations.tex   Overview of the fundamental laws
  *.tex                       One file per equation (77 chapters)
  Equation_Summary.tex        Quick-reference summary appendix
  Index.tex                   Comprehensive index
  Historical_Notes.tex        Historical context and bibliography
physics_equations.pdf         Compiled book
```

Each chapter file follows a consistent template:

1. **Introduction** — motivation and physical context
2. **The equation** — boxed, with a label for cross-referencing
3. **Fundamental equations used** — the building blocks of the derivation
4. **Assumptions & limitations** — the domain of validity
5. **Mathematical derivation** — step-by-step, self-contained
6. **Bibliography** — primary sources and further reading

## License

All rights reserved. The content of this book is copyright by Chaman Singh Verma unless otherwise noted.
