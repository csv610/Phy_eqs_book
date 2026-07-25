#!/usr/bin/env python3
"""Replace Feynman sections with detailed 5-category Feynman questioning style."""
import re

# Each entry: (chapter_title, replacement_text)
# The replacement text includes the \section* header and all content through the closing \end{enumerate}

CHAPTERS = []

CHAPTERS.append(("Fundamental Equations", r"""\section*{What Richard Feynman Would Have Asked}

\subsection*{1. The Plain-English Translation}
\textit{``Don't just repeat the symbols to me. What is this equation actually saying in plain, everyday language?''}

The Core Meaning: These equations are the grammar of the universe. Conservation laws say certain quantities---energy, momentum, charge---cannot be created or destroyed, only moved around. Maxwell's equations say that shaking an electric charge creates a ripple that travels at the speed of light, and that light itself is an electromagnetic wave. Einstein's $E = mc^2$ says that a tiny speck of matter holds a stupendous amount of energy, like a compressed spring waiting to release. The Schr\"odinger equation says that quantum particles behave like waves, with all the interference and fuzziness that implies.

The Metaphor: Think of these equations as the rules of a game. You did not invent the game---nature did. These equations describe what moves are legal. Conservation of energy says you cannot score points out of nothing. Maxwell's equations say that electromagnetic ``plays'' propagate at a fixed speed. The quantum equations say that the game has built-in randomness at its smallest scales.

\subsection*{2. The Localized Mechanics}
\textit{``Look at a tiny, microscopic point in space. What is happening there that these equations describe?''}

He would press you on what each conservation law means at a single point. Conservation of energy at a point means: if energy is increasing somewhere, it must be flowing in from somewhere else---there is no local ``source'' of energy. Conservation of charge at a point means: if charge is accumulating, current must be flowing in. These are continuity equations---the same mathematical structure appears in fluid dynamics, electromagnetism, and quantum mechanics.

The Smoothness Check: He would ask you to explain why Maxwell's equations predict that electromagnetic waves travel at a fixed speed $c = 1/\sqrt{\mu_0 \epsilon_0}$. This is not a coincidence---it is a consequence of the fact that electric and magnetic fields are two aspects of one thing, and their mutual induction creates a self-sustaining wave at a speed determined by the properties of empty space itself.

\subsection*{3. Testing the Extreme Limits}
\textit{``Let's push these equations to their breaking points. Where do they fail?''}

The High-Energy Limit: At very high energies (near the Big Bang), all four forces may have been unified into one. The Standard Model---our best collection of equations---does not include gravity. At the Planck scale ($10^{-35}$ m, $10^{19}$ GeV), spacetime itself may become quantum foam, and all our equations may break down.

The Low-Energy Limit: At everyday energies, quantum effects are negligible and classical equations work beautifully. But at the atomic scale ($10^{-10}$ m), quantum mechanics dominates. The equations do not ``break down'' at these limits---they reveal deeper structure that classical physics misses.

\subsection*{4. Dimensionality and Geometry}
\textit{``Does this equation care about the shape of the space it lives in?''}

He would point out that conservation laws are consequences of symmetries (Noether's theorem). If the laws of physics do not change when you shift time (translation in time symmetry), energy is conserved. If they do not change when you shift space (translation in space symmetry), momentum is conserved. If they do not change when you rotate (rotational symmetry), angular momentum is conserved. The equations we know are not arbitrary---they are dictated by the symmetries of spacetime itself.

\subsection*{5. Cross-Disciplinary Connection}
\textit{``You learned these in physics class, but where else do they appear?''}

Conservation laws appear everywhere: in economics (conservation of money), in ecology (conservation of biomass), in information theory (conservation of information in reversible computing). Maxwell's equations appear in any system where two fields regenerate each other---chemical reaction-diffusion systems, predator-prey populations, and even certain financial models. The deep reason is that the same mathematics describes any system where two quantities mutually sustain each other.
"""))

CHAPTERS.append(("Airy Disk", r"""\section*{What Richard Feynman Would Have Asked}

\subsection*{1. The Plain-English Translation}
\textit{``Don't just repeat the symbols to me. What is this equation actually saying in plain, everyday language?''}

The Core Meaning: No matter how perfect your lens is, light passing through a circular opening will always spread out into a fuzzy disk rather than focusing to a sharp point. The smaller the opening, the more it spreads. The 1.22 factor comes from the first zero of a Bessel function---a mathematical object that appears whenever circular symmetry meets wave physics.

The Metaphor: Imagine throwing a stone into a perfectly circular pond. The ripples spread in circles, but when they pass through a circular opening (like a drain), they produce a characteristic pattern. Light does the same thing. The Airy disk is nature's way of saying: ``You cannot confine a wave to a point without paying a price in spreading.''

\subsection*{2. The Localized Mechanics}
\textit{``Look at the center of the Airy disk. What is happening to the light waves there?''}

He would press you on why the central peak is brightest. At the exact center, all the wavelets from every part of the circular aperture arrive in phase---they all travel the same distance. They add constructively, producing maximum intensity. As you move away from the center, the wavelets arrive with increasing phase differences. At the first dark ring, the phase differences are such that the contributions exactly cancel---for every wavelet that arrives ``up,'' another arrives ``down.''

The Smoothness Check: He would ask you to explain why the central peak is twice as wide as the others. This is because the central peak spans from the first zero on one side to the first zero on the other side, while the side peaks span from one zero to the next. The zeros of the Bessel function are not equally spaced---they get closer together as you move outward.

\subsection*{3. Testing the Extreme Limits}
\textit{``What happens when we push the aperture to extreme sizes?''}

The Zero-Aperture Limit: As the aperture shrinks to zero, the Airy disk grows to infinity---you see nothing. This is the uncertainty principle in action: confining the photon's position ($\Delta x$ small) spreads out its momentum ($\Delta p$ large).

The Infinite-Aperture Limit: As the aperture grows to infinity, the Airy disk shrinks to a perfect point---geometric optics. But an infinite aperture is impossible, so there is always some blur.

The Quantum Limit: What happens when you send photons through one at a time? Each photon lands at a single point (particle behavior), but after many photons, the Airy disk pattern emerges (wave behavior). This is wave-particle duality in action.

\subsection*{4. Dimensionality and Geometry}
\textit{``What if the aperture were a slit instead of a circle? How would the pattern change?''}

He would point out that a circular aperture produces an Airy disk (Bessel function), while a slit produces a sinc-squared pattern (sine function). The mathematics changes because the symmetry changes---circular symmetry gives Bessel functions, rectangular symmetry gives sine functions. The general principle remains: the diffraction pattern is the Fourier transform of the aperture shape.

\subsection*{5. Cross-Disciplinary Connection}
\textit{``You learned this in optics class, but where else does this pattern appear?''}

The Airy disk appears in radio astronomy (the beam pattern of a circular dish antenna), in medical imaging (the resolution limit of CT and MRI scanners), in crystallography (the diffraction pattern of X-rays from crystals), and even in acoustics (the sound pattern of a circular speaker). The same mathematics---the Fourier transform of a circular function---appears in any field where waves pass through circular openings.
"""))

CHAPTERS.append(("Bernoulli Equation", r"""\section*{What Richard Feynman Would Have Asked}

\subsection*{1. The Plain-English Translation}
\textit{``Don't just repeat the symbols to me. What is this equation actually saying in plain, everyday language?''}

The Core Meaning: When a fluid speeds up, its pressure drops---not because something is ``sucking'' the pressure away, but because the energy that was in pressure form has been converted to kinetic energy. The total energy budget of a fluid parcel is strictly conserved: pressure energy + kinetic energy + gravitational potential energy = constant along a streamline.

The Metaphor: Imagine a crowded hallway that narrows. People must walk faster to get through. In doing so, they spread out and push less on the walls. The pressure (pushing on the walls) drops because the energy is now in motion (kinetic energy) rather than in pushing. Water in a pipe does exactly the same thing.

\subsection*{2. The Localized Mechanics}
\textit{``Look at a tiny fluid parcel as it speeds up. What is happening to the pressure right there?''}

He would press you on the energy trade-off. The equation $P + \frac{1}{2}\rho v^2 + \rho gh = \text{constant}$ says that if $v$ increases, $P$ must decrease (assuming $h$ is constant). This is not a force---it is an energy conservation statement applied to a fluid element. The fluid does not ``know'' about pressure drops; it simply follows the path of least resistance, which happens to be the path that conserves energy.

The Smoothness Check: He would ask why the equation applies only along a streamline. Because different streamlines can have different total energies (different constants), you cannot compare pressure between two streamlines using Bernoulli's equation. The equation is a statement about energy conservation along a single path, not across the entire flow.

\subsection*{3. Testing the Extreme Limits}
\textit{``What happens when we push the fluid to extreme speeds?''}

The Speed-of-Sound Limit: As fluid speed approaches the speed of sound, compressibility matters---the density changes, and Bernoulli's equation breaks down. You need the full equations of compressible fluid dynamics.

The Zero-Speed Limit: At $v = 0$ (static fluid), Bernoulli reduces to $P + \rho gh = \text{constant}$---hydrostatics. The pressure increases linearly with depth, which is why your ears pop when you dive underwater.

The Superfluid Limit: In superfluid helium (below 2.17 K), viscosity vanishes and Bernoulli's equation applies with perfect accuracy---there are no dissipative losses. The superfluid is the closest thing to an ideal fluid that exists in nature.

\subsection*{4. Dimensionality and Geometry}
\textit{``Does this equation care about the shape of the pipe or channel?''}

He would point out that Bernoulli's equation does not care about the shape---only about the changes in velocity, height, and pressure along a streamline. A pipe can be straight, curved, widening, or narrowing---as long as the flow is steady, incompressible, and inviscid, Bernoulli applies. The shape matters only insofar as it determines how the velocity changes.

\subsection*{5. Cross-Disciplinary Connection}
\textit{``You learned this in fluid dynamics class, but where else does this exact same principle appear?''}

The same energy trade-off appears in economics (velocity of money vs. ``pressure'' of interest rates), in traffic flow (when lanes narrow, cars speed up and ``pressure''---density---drops), and in electrical circuits (voltage is analogous to pressure, current to velocity, and the energy trade-off between kinetic and potential energy is analogous to the trade-off between kinetic and pressure energy in fluids).
"""))

CHAPTERS.append(("Boltzmann Transport Equation", r"""\section*{What Richard Feynman Would Have Asked}

\subsection*{1. The Plain-English Translation}
\textit{``Don't just repeat the symbols to me. What is this equation actually saying in plain, everyday language?''}

The Core Meaning: This equation tracks how the crowd of particles---each moving with its own velocity---redistributes itself over space and time. It says that the number of particles at a given position and velocity changes because of three effects: (1) particles stream from one place to another, (2) external forces push particles from one velocity to another, and (3) collisions transfer particles between velocities.

The Metaphor: Imagine watching a crowded dance floor from above. Each dancer moves according to the music (external forces) and bumps into other dancers (collisions). The Boltzmann equation tracks how the crowd's density changes at each location and velocity. When you heat one end of a metal rod, the atoms there vibrate more vigorously and collide with their neighbors, passing the energy along---this is heat conduction, and it emerges from the Boltzmann equation.

\subsection*{2. The Localized Mechanics}
\textit{``Look at a single particle in the distribution. What happens to it during a collision?''}

He would press you on the collision integral---the most complex part of the equation. A collision takes two particles with specific velocities and produces two particles with different velocities. The collision integral counts how many such collisions happen per unit time, and how they redistribute the particles among different velocities. The key insight is that collisions conserve mass, momentum, and energy---but they can change the distribution from non-equilibrium to equilibrium.

The Smoothness Check: He would ask why the collision term is quadratic in $f$ (the distribution function). Because collisions involve \emph{pairs} of particles---the rate of collisions is proportional to the number of pairs, which is $\sim f^2$. This nonlinearity makes the Boltzmann equation very hard to solve.

\subsection*{3. Testing the Extreme Limits}
\textit{``What happens when we push the gas to extreme conditions?''}

The Dilute Gas Limit: At very low densities, collisions vanish ($f \to 0$ in the collision integral) and the equation becomes a streaming equation---particles move freely without interacting. This is the ``free molecular flow'' regime, relevant for spacecraft in the upper atmosphere.

The Dense Gas Limit: At very high densities, the concept of binary (two-body) collisions breaks down---particles interact simultaneously with many neighbors. The Boltzmann equation must be replaced by the BBGKY hierarchy or molecular dynamics simulations.

The Equilibrium Limit: At long times, the collision term drives the distribution toward the Maxwell-Boltzmann distribution---the unique distribution where collisions produce no net change. This is the H-theorem: entropy increases monotonically until equilibrium is reached.

\subsection*{4. Dimensionality and Geometry}
\textit{``Does this equation care about the dimensionality of space?''}

He would point out that the Boltzmann equation lives in a 6-dimensional phase space (3 for position, 3 for velocity). In 2D, the velocity space is 2-dimensional and the collision dynamics are simpler. In 1D, the equation can sometimes be solved exactly. The physics is the same in all dimensions---transport, relaxation to equilibrium, and the H-theorem---but the mathematical complexity changes dramatically.

\subsection*{5. Cross-Disciplinary Connection}
\textit{``You learned this in kinetic theory, but where else does this exact same equation appear?''}

The Boltzmann equation appears in radiative transfer (photons scattering in stellar atmospheres), in neutron transport (neutrons diffusing in a nuclear reactor), in semiconductor physics (electrons scattering in a crystal lattice), and even in social dynamics (``opinions'' transported and ``colliding'' in a population). The same mathematical structure---streaming + forcing + collision---appears whenever a population of entities moves, interacts, and redistributes.
"""))

CHAPTERS.append(("Bose-Einstein Distribution", r"""\section*{What Richard Feynman Would Have Asked}

\subsection*{1. The Plain-English Translation}
\textit{``Don't just repeat the symbols to me. What is this equation actually saying in plain, everyday language?''}

The Core Meaning: Certain particles are social butterflies---they like to do the same thing at the same time. The minus sign in the denominator ($e^{(E-\mu)/kT} - 1$) is the key: it means that the more particles already in a state, the more likely another particle is to join them. This is the opposite of fermions, which avoid each other (plus sign in the denominator).

The Metaphor: Imagine a concert where everyone wants the same spot. As more people crowd in, the spot becomes more attractive---it must be the best view! Bosons are like these concert-goers. When you cool rubidium atoms to near absolute zero, they all collapse into one quantum state and move as a single entity---a Bose-Einstein condensate, a new state of matter where atoms lose their individual identity.

\subsection*{2. The Localized Mechanics}
\textit{``Look at a single quantum state. How does the presence of one boson affect the probability of another boson joining it?''}

He would press you on the stimulation factor. The occupation number of a state is $\langle n \rangle = 1/(e^{(E-\mu)/kT} - 1)$. If you already have $n$ bosons in a state, the probability of adding one more is proportional to $(n+1)$---not $n$. This ``bosonic stimulation'' is the mathematical expression of their social behavior. It is the same physics that makes lasers work: photons stimulate the emission of more photons, all in the same quantum state.

The Smoothness Check: He would ask why the chemical potential $\mu$ must be less than the ground state energy. Because if $\mu$ equaled the ground state energy, the denominator would be zero and the occupation number would diverge---an infinite number of particles in one state. This is exactly what happens in a Bose-Einstein condensate: the ground state macroscopically occupied.

\subsection*{3. Testing the Extreme Limits}
\textit{``What happens when we push the temperature to extreme values?''}

The High-Temperature Limit: As $T \to \infty$, the exponential dominates and $e^{(E-\mu)/kT} \gg 1$, so the minus sign becomes irrelevant. The Bose-Einstein distribution reduces to the classical Maxwell-Boltzmann distribution---quantum effects wash out.

The Zero-Temperature Limit: As $T \to 0$, all particles collapse into the ground state---the condensate. The occupation of the ground state becomes macroscopic ($\sim N$), while all excited states are empty. This is a phase transition: the gas suddenly changes from a collection of individual atoms to a single quantum entity.

\subsection*{4. Dimensionality and Geometry}
\textit{``Does this equation care about the dimensionality of space?''}

He would point out that Bose-Einstein condensation only occurs in 3D and higher. In 1D and 2D, the density of states is such that the integral for the total number of particles diverges---you cannot fit all the particles into the excited states at any finite temperature. But in 2D, a condensate can form if the particles are trapped in a harmonic potential (as in experiments with cold atoms).

\subsection*{5. Cross-Disciplinary Connection}
\textit{``You learned this in quantum statistics, but where else does this exact same principle appear?''}

The Bose-Einstein distribution appears in photon statistics (blackbody radiation is a gas of photons obeying this distribution), in phonon statistics (lattice vibrations in solids), and in the statistics of any indistinguishable particles with integer spin. The same ``social'' behavior appears in network theory: nodes with many connections tend to acquire even more connections (the ``rich get richer'' phenomenon), which is mathematically analogous to bosonic stimulation.
"""))

CHAPTERS.append(("Clausius-Clapeyron Equation", r"""\section*{What Richard Feynman Would Have Asked}

\subsection*{1. The Plain-English Translation}
\textit{``Don't just repeat the symbols to me. What is this equation actually saying in plain, everyday language?''}

The Core Meaning: When you increase the pressure on a liquid, you raise its boiling point---the molecules need more kinetic energy to escape the tighter packing. This is why pressure cookers work: by increasing the pressure, they delay boiling and allow temperatures above 100°C. For water, the equation also explains why ice floats: solid water is less dense than liquid water, so the solid-liquid boundary has a negative slope---increasing pressure actually lowers the melting point.

The Metaphor: Think of molecules at a phase boundary as people at a doorway. Pressure is like pushing the crowd together---it makes it harder for individuals to push through the door (escape into the gas phase). You need to give them more energy (higher temperature) to break free.

\subsection*{2. The Localized Mechanics}
\textit{``Look at the phase boundary itself. What is happening to the molecules right at the interface?''}

He would press you on the latent heat. The equation $dP/dT = L/(T\Delta V)$ says that the slope of the phase boundary in a $P$-$T$ diagram is determined by the latent heat $L$ (energy needed to convert one phase to another) and the volume change $\Delta V$. Large latent heat means a steep boundary---small temperature changes cause large pressure changes. Large volume change means a steep boundary---the two phases are very different.

The Smoothness Check: He would ask what happens when $L = 0$. The slope goes to zero---the phase boundary becomes horizontal. This is the triple point: three phases coexist at a single temperature and pressure. At the critical point, $L \to 0$ and $\Delta V \to 0$ simultaneously---the distinction between liquid and gas vanishes.

\subsection*{3. Testing the Extreme Limits}
\textit{``What happens when we push the system to extreme pressures and temperatures?''}

The Critical Point: At the critical point ($T_c$, $P_c$), the latent heat goes to zero and the Clausius-Clapeyron equation gives a divergence ($0/0$). The equation breaks down because there is no longer a sharp phase transition---liquid and gas become indistinguishable.

The Triple Point: At the triple point, three phases coexist. The Clausius-Clapeyron equation applies to each pairwise boundary, but the three boundaries meet at a single point. This is the unique thermodynamic state where ice, water, and steam coexist.

The Negative Slope: For water, $dP/dT < 0$ for the solid-liquid boundary because ice is less dense than water. Increasing pressure lowers the melting point---this is why glaciers flow under their own weight: the pressure at the base melts the ice, creating a lubricating layer of water.

\subsection*{4. Dimensionality and Geometry}
\textit{``Does this equation care about the shape of the container?''}

He would point out that the Clausius-Clapeyron equation is independent of container shape---it is a statement about bulk thermodynamic phases, not about geometry. The equation applies equally to a beaker of water, a sealed pressure cooker, or the ocean. The phase boundary is determined by temperature and pressure alone, not by the shape of the vessel.

\subsection*{5. Cross-Disciplinary Connection}
\textit{``You learned this in thermodynamics class, but where else does this exact same principle appear?''}

The same ``slope = latent heat / (temperature $\times$ volume change)'' structure appears in any first-order phase transition:磁性 transitions in magnets (the magnetic analogue of latent heat is the change in magnetization), structural phase transitions in crystals (the volume change is the change in lattice parameters), and even in economics (the ``latent heat'' of a market crash is the change in investor sentiment, and the ``volume change'' is the change in market liquidity).
"""))

CHAPTERS.append(("Continuity Equation", r"""\section*{What Richard Feynman Would Have Asked}

\subsection*{1. The Plain-English Translation}
\textit{``Don't just repeat the symbols to me. What is this equation actually saying in plain, everyday language?''}

The Core Meaning: Matter is a perfect accountant. If water level rises at one point, more water is flowing in than out. If it drops, more is flowing out than in. The continuity equation is the mathematical expression of this simple bookkeeping principle: the rate of change of mass in any region equals the net mass flowing in through the boundary.

The Metaphor: Imagine watching a river from a bridge. If the water level rises at one point, it must be because more water is flowing in than flowing out. If you squeeze a tube narrower, the fluid must speed up to maintain the same flow rate---this is why putting your thumb over a garden hose makes the water spray faster. The equation is the same whether the fluid is water, air, blood, or traffic on a highway.

\subsection*{2. The Localized Mechanics}
\textit{``Look at a tiny control volume in the fluid. What is the balance of mass right there?''}

He would press you on the divergence term. $\nabla \cdot (\rho \mathbf{v})$ measures the net outward flux of mass from a point. If it is positive, mass is flowing away and the local density decreases. If it is negative, mass is flowing in and the density increases. The continuity equation says these two effects exactly balance: $\partial \rho / \partial t + \nabla \cdot (\rho \mathbf{v}) = 0$.

The Smoothness Check: He would ask why the equation is first-order in time but first-order in space. Because it is a conservation law---it tracks how a conserved quantity (mass) flows. The time derivative tells you the local rate of change; the spatial derivative tells you the flux. Together, they ensure that mass is neither created nor destroyed.

\subsection*{3. Testing the Extreme Limits}
\textit{``What happens when we push the flow to extreme conditions?''}

The Incompressible Limit: For liquids (approximately incompressible), $\rho$ is constant and the equation simplifies to $\nabla \cdot \mathbf{v} = 0$---the velocity field is divergence-free. This is a powerful constraint: it says that fluid cannot be compressed or expanded, only redirected.

The Compressible Limit: For gases at high speeds (near the speed of sound), density changes matter and the full equation must be used. At supersonic speeds, shock waves form where density changes discontinuously---the continuity equation still holds, but the flow is no longer smooth.

The Vacuum Limit: In a vacuum ($\rho = 0$), the equation is trivially satisfied---there is nothing to conserve. But if you try to create a perfect vacuum, quantum effects (virtual particles) ensure that it is never truly empty.

\subsection*{4. Dimensionality and Geometry}
\textit{``Does this equation care about the dimensionality of space?''}

He would point out that the continuity equation has the same form in 1D, 2D, and 3D---only the divergence operator changes. In 1D, it is $d(\rho v)/dx = -\partial \rho / \partial t$. In 2D, it involves partial derivatives in $x$ and $y$. The physics is identical: mass is conserved, and the equation tracks how it flows.

\subsection*{5. Cross-Disciplinary Connection}
\textit{``You learned this in fluid dynamics, but where else does this exact same equation appear?''}

The continuity equation appears in electromagnetism (conservation of charge: $\partial \rho_e / \partial t + \nabla \cdot \mathbf{J} = 0$), in quantum mechanics (conservation of probability: $\partial |\psi|^2 / \partial t + \nabla \cdot \mathbf{J}_\psi = 0$), in heat transfer (conservation of energy), and in population dynamics (conservation of organisms). The same mathematical structure---the rate of change plus the divergence of a flux equals zero---is the universal signature of a conservation law.
"""))

CHAPTERS.append(("Diffusion Equation", r"""\section*{What Richard Feynman Would Have Asked}

\subsection*{1. The Plain-English Translation}
\textit{``Don't just repeat the symbols to me. What is this equation actually saying in plain, everyday language?''}

The Core Meaning: Nature abhors a gradient. When you drop ink into water, it does not stay as a concentrated blob---it spreads out, becoming more dilute until the color is uniform everywhere. The rate of spreading is proportional to how ``curved'' the concentration profile is: where the curve is steep, spreading is fast; where it is flat, spreading is slow.

The Metaphor: Think of a crowded room. People naturally spread out from the crowded area to the less crowded area, not because there is a force pushing them, but because there are more ways to be spread out than to be concentrated. The diffusion equation describes exactly how fast this spreading happens. The thermal diffusivity $\alpha$ is the material's ``spreading speed''---metals have high $\alpha$ (heat spreads quickly), wood has low $\alpha$ (heat spreads slowly).

\subsection*{2. The Localized Mechanics}
\textit{``Look at a single point in the material. What determines how fast the temperature changes there?''}

He would press you on the Laplacian. $\nabla^2 T$ measures how much the temperature at a point differs from the average temperature of its neighbors. If the point is hotter than its neighbors ($\nabla^2 T < 0$), the temperature there decreases---heat flows out. If it is colder ($\nabla^2 T > 0$), the temperature there increases---heat flows in. The diffusion equation says: the rate of temperature change equals the diffusivity times this ``neighborhood difference.''

The Smoothness Check: He would ask why the equation is first-order in time but second-order in space. Because diffusion is irreversible---you can unscramble an egg in principle (reverse the trajectories of all molecules), but you never see it happen in practice. The first time derivative means the equation has a preferred direction in time: forward.

\subsection*{3. Testing the Extreme Limits}
\textit{``What happens when we push the diffusion to extreme conditions?''}

The Short-Time Limit: At very short times after a sudden temperature change, the diffusion equation predicts infinite propagation speed---a sharp spike instantly affects points arbitrarily far away. This is physically impossible and signals the breakdown of the diffusion approximation. At very short times, you need the hyperbolic heat equation (which includes a finite speed of propagation).

The Long-Time Limit: At very long times, the temperature becomes uniform everywhere---maximum entropy. The diffusion equation predicts exponential decay of temperature differences, with a time constant that depends on the geometry and the diffusivity.

The Quantum Limit: The Schr\"odinger equation is the diffusion equation with imaginary time ($t \to i\tau$). This deep connection means that quantum mechanics and diffusion are mathematically the same process---just with different boundary conditions and different physical interpretations.

\subsection*{4. Dimensionality and Geometry}
\textit{``How does the dimensionality of space affect how things diffuse?''}

He would point out that in 1D, the diffusion length grows as $\sqrt{t}$ (the famous ``random walk'' scaling). In 2D, it also grows as $\sqrt{t}$ but with a different prefactor. In 3D, the same scaling applies. The $\sqrt{t}$ scaling is universal---it comes from the central limit theorem, which says that the sum of many random steps grows as the square root of the number of steps.

\subsection*{5. Cross-Disciplinary Connection}
\textit{``You learned this in heat transfer, but where else does this exact same equation appear?''}

The diffusion equation describes heat conduction in solids, pollutant dispersion in groundwater, drug diffusion through tissue, neutron diffusion in nuclear reactors, and even the random walk of stock prices (the Black-Scholes equation for financial options is a disguised diffusion equation). The same mathematics applies because all these processes involve the random redistribution of a conserved quantity.
"""))

CHAPTERS.append(("Dirac Equation", r"""\section*{What Richard Feynman Would Have Asked}

\subsection*{1. The Plain-English Translation}
\textit{``Don't just repeat the symbols to me. What is this equation actually saying in plain, everyday language?''}

The Core Meaning: When Dirac tried to write a quantum equation that obeyed Einstein's relativity, he discovered extra solutions---solutions that described particles with positive energy but negative charge. These were not mathematical artifacts; they were real particles (positrons), discovered in 1932. The equation also says that electrons have an intrinsic angular momentum (spin) even though they are point particles---spin is not the electron ``spinning'' like a top, but a fundamental quantum property that arises naturally from combining relativity with quantum mechanics.

The Metaphor: Dirac was looking for a description of the electron that was consistent with both quantum mechanics and relativity. He found it---but the equation had ``extra pages'' that he initially tried to throw away. Those extra pages turned out to describe antimatter. The universe, it seems, has more symmetry than we expected: for every particle, there is an antiparticle.

\subsection*{2. The Localized Mechanics}
\textit{``Look at the electron as described by the Dirac equation. What is spin, physically?''}

He would press you on the relationship between spin and relativity. In the non-relativistic limit, the Dirac equation reduces to the Pauli equation---which includes spin as an added ingredient. But in the Dirac equation, spin is not added---it emerges naturally. The electron's spin is a consequence of the requirement that the equation be Lorentz covariant (the same in all reference frames). Spin is not a classical property; it is a relativistic quantum property.

The Smoothness Check: He would ask why the Dirac equation uses $4 \times 4$ matrices (gamma matrices) instead of ordinary numbers. Because the electron has two internal degrees of freedom (spin up and spin down) and the equation must account for both left-handed and right-handed components. The $4 \times 4$ structure is the minimal representation of the Lorentz group that includes spin-1/2 particles.

\subsection*{3. Testing the Extreme Limits}
\textit{``What happens when we push the electron to extreme energies?''}

The Pair Production Limit: At energies above $2m_e c^2 = 1.022$ MeV, photons can create electron-positron pairs. The Dirac equation naturally describes this process: the negative-energy solutions (positrons) are essential for pair production.

The Ultra-Relativistic Limit: At energies much greater than $m_e c^2$, the electron behaves as if it were massless---the mass term becomes negligible and the Dirac equation simplifies. This is the regime of particle physics, where electrons and quarks are effectively massless compared to their kinetic energies.

The Planck Scale: At energies near $10^{19}$ GeV, gravity becomes important and the Dirac equation must be extended to include gravitational interactions. This is the frontier of theoretical physics---we do not yet have a consistent theory of quantum gravity.

\subsection*{4. Dimensionality and Geometry}
\textit{``Does this equation care about the geometry of spacetime?''}

He would point out that the Dirac equation can be formulated on any curved spacetime---you just replace the partial derivatives with covariant derivatives. This is how general relativity and quantum mechanics are combined (at least approximately). The spin connection---the gravitational analogue of the electromagnetic vector potential---couples the electron's spin to the curvature of spacetime.

\subsection*{5. Cross-Disciplinary Connection}
\textit{``You learned this in particle physics, but where else does this equation appear?''}

The Dirac equation appears in condensed matter physics, where it describes the behavior of electrons in graphene (a 2D material where electrons behave as massless Dirac fermions), in topological insulators (where surface states are described by the Dirac equation), and in the quantum Hall effect. The same mathematics describes any system where spin-1/2 particles move through a periodic potential.
"""))

CHAPTERS.append(("Electromagnetic Wave Equation", r"""\section*{What Richard Feynman Would Have Asked}

\subsection*{1. The Plain-English Translation}
\textit{``Don't just repeat the symbols to me. What is this equation actually saying in plain, everyday language?''}

The Core Meaning: Light, radio waves, X-rays, and gamma rays are all the same thing---electromagnetic waves traveling at the speed of light. When Maxwell derived this equation in 1865, he calculated the speed from the measured values of the electrical and magnetic constants and found it matched the speed of light exactly. This was one of the greatest unifications in physics.

The Metaphor: When you shake an electric charge, it creates a changing electric field. This changing electric field creates a changing magnetic field. This changing magnetic field creates a changing electric field. And so on---the disturbance propagates outward at the speed of light. Empty space itself has electrical and magnetic properties ($\epsilon_0$ and $\mu_0$) that determine how fast this wave travels.

\subsection*{2. The Localized Mechanics}
\textit{``Look at a single point in space as the wave passes. What is happening to the electric and magnetic fields right there?''}

He would press you on the mutual induction. At any point, the changing electric field creates a magnetic field, and the changing magnetic field creates an electric field. The two fields are not independent---they are two aspects of one thing, the electromagnetic field. The wave equation describes how this coupled system propagates through space.

The Smoothness Check: He would ask why the wave speed is $c = 1/\sqrt{\mu_0 \epsilon_0}$. Because $\epsilon_0$ determines how much electric field is created by a charge, and $\mu_0$ determines how much magnetic field is created by a current. The product $\mu_0 \epsilon_0$ determines how quickly the ``relay'' between electric and magnetic fields occurs, and therefore how fast the wave propagates.

\subsection*{3. Testing the Extreme Limits}
\textit{``What happens when we push electromagnetic waves to extreme frequencies?''}

The Gamma-Ray Limit: At very high frequencies (gamma rays), photons have enough energy to create particle-antiparticle pairs. The classical wave equation breaks down---you need quantum electrodynamics (QED).

The Radio-Wave Limit: At very low frequencies (radio waves), the wavelength can be kilometers long. The wave equation still applies, but the practical challenges of generating and detecting such long waves are enormous.

The Static Limit: At zero frequency, there is no wave---just a static electric or magnetic field. Is a static field a ``wave'' with infinite wavelength? Feynman would say: in a sense, yes---it is the zero-frequency limit of the wave equation.

\subsection*{4. Dimensionality and Geometry}
\textit{``Does this equation care about the shape of the space it lives in?''}

He would point out that the wave equation has the same form in any dimension---1D (waves on a string), 2D (waves on a drumhead), and 3D (electromagnetic waves in space). The only difference is the Laplacian operator: in 1D it is $d^2/dx^2$, in 2D it involves $x$ and $y$, and in 3D it involves $x$, $y$, and $z$. The physics is identical: disturbances propagate as waves at a speed determined by the medium.

\subsection*{5. Cross-Disciplinary Connection}
\textit{``You learned this in electromagnetism, but where else does this exact same equation appear?''}

The wave equation describes sound waves in air, seismic waves in the Earth, vibrations in guitar strings, and quantum mechanical probability waves. The Schr\"odinger equation is actually a modified wave equation (with a first time derivative instead of second). The same mathematics describes any system where a restoring force (proportional to displacement) and inertia (proportional to acceleration) are balanced.
"""))

# Continue with remaining chapters...
# (This is a large block - writing all 70)

def make_feynman_section(title, text):
    return (title, text)

# We need to build the full dictionary
FEYNMAN_DICT = {}
for title, text in CHAPTERS:
    FEYNMAN_DICT[title] = text.strip()

def find_chapter_positions(content):
    pattern = r'\\chapter\{([^}]+)\}'
    return [(m.start(), m.group(1)) for m in re.finditer(pattern, content)]

def find_feynman_section(content, chapter_start, next_chapter_start):
    """Find the Feynman section within a chapter's range."""
    section = content[chapter_start:next_chapter_start]
    match = re.search(r'\\section\*\{What Richard Feynman Would Have Asked\}', section)
    if match:
        return chapter_start + match.start()
    return None

def find_feynman_end(content, start):
    """Find the end of the Feynman section (the last \end{enumerate} after the section header)."""
    # Find all \end{enumerate} after the start position
    remaining = content[start:]
    matches = list(re.finditer(r'\\end\{enumerate\}', remaining))
    if matches:
        return start + matches[-1].end()
    return None

def replace_feynman_sections(input_file):
    with open(input_file, 'r') as f:
        content = f.read()

    chapters = find_chapter_positions(content)
    replaced = 0
    skipped = []

    # Process in reverse to preserve positions
    for i in range(len(chapters) - 1, -1, -1):
        start_pos, title = chapters[i]

        if title == "Historical Notes":
            continue

        # Find next chapter or end of file
        if i + 1 < len(chapters):
            next_pos = chapters[i + 1][0]
        else:
            next_pos = len(content)

        # Find Feynman section in this chapter
        feynman_start = find_feynman_section(content, start_pos, next_pos)
        if feynman_start is None:
            skipped.append(title)
            continue

        feynman_end = find_feynman_end(content, feynman_start)
        if feynman_end is None:
            skipped.append(title)
            continue

        if title not in FEYNMAN_DICT:
            skipped.append(title)
            continue

        # Replace the section
        new_text = FEYNMAN_DICT[title]
        content = content[:feynman_start] + new_text + '\n' + content[feynman_end:]
        replaced += 1

    with open(input_file, 'w') as f:
        f.write(content)

    print(f"Replaced: {replaced} sections")
    if skipped:
        print(f"Skipped: {skipped}")

if __name__ == '__main__':
    replace_feynman_sections('/Users/csv610/Projects/MyBooks/DeriveEqs/physics_equations.tex')
