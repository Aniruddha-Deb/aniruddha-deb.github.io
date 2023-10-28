---
title: Inorganic Heterocyclic compounds
publishDate: '2020-05-03T10:40:00'
categories: Chemistry
slug: inorganic-heterocycles
---

The 45th IChO preparatory problem list had this as it's fifth problem:

> **5.1** The interaction of thionyl chloride and sodium azide at $-30^\circ \text{C}$ gives colorless crystals **X**, containing 36.4 wt.% of Cl. The crystals consist of cyclic trimers. Find the composition of **X** and give the reaction equation.
>
> **5.2** Draw two stereoisomers of **X**.
>
> **5.3** A colorless liquid **Y** was prepared by a reaction between **X** and antimony(III) fluoride. Addition of 1.00 g of **Y** to the excess of barium acetate aqueous solution gave the precipitate with the mass of 3.96 g. Determine the chemical formula of **Y**, draw its structure and write the reaction equation.
>
> **5.4** **Y** enters the substitution reactions with typical nucleophiles such as methylamine. What product will be formed in the reaction between **Y** and the excess of methylamine? Draw its structure.
>
> **5.5** Give two examples of molecules or ions which are isoelectronic to **Y**, draw their structures.
>
> **5.6** One of the substances isoelectronic to **Y** transforms in the presence of water traces into polymer **Z**. 1.00 g of **Z** was dissolved in water and the resulting solution was added to the excess of barium acetate solution. The precipitate with the mass of 2.91 g was formed. Determine the formula of **Z** and draw its structure.

This looks like a very sketchy problem: we know for a fact that:

1. X is a cyclic trimer, with 34.5% w/w of $\ce{Cl}$. 
2. The use of Sodium Azide suggests that the trimer also contains $\ce{N}$
3. The $\ce{Cl}$ atoms are substituted by $\ce{F}$ atoms in 5.3. The white precipitate in 5.3 is Barium Sulphate. Thus, the trimer of 5.1 has $\ce{Cl, O}$ and $\ce{S}$. 1 gram of Y thus gives $\pu{\frac{3.96}{233} mol }\ce{BaSO4}$. 
4. 5.6 is very similar to 5.3. The polymer has sulphur and oxygen, in order to produce $\ce{BaSO4}$ as precipitate.

The reaction of 5.1 can be written as $\ce{SOCl2 + NaN3 -> (S\_xO\_yCl\_zN\_a)3 }$ based on whatever information we have till now. Let's try getting some values for x,y,z and a. If we let all of them be 1, then the compound becomes $\ce{(SO(Cl)N)3}$. We can check if this is the correct compound by checking the mass % of $\ce{Cl}$ here. The mass % comes out to be
$$\frac{35.5}{35.5+14+16+32} \times 100 \approx 36.4\%$$

This perfectly matches what we are looking for. Thus, the formula of the compound is $\ce{(NSOCl)3}$. This compound has been synthesized and it's name is sulphanuric chloride (Hazell et al.)

Drawing the structure is a bit trickier. A possible stable trimeric structure is

![Initial guess](/articles/2020/res/X_1.png)

However, this is not the experimentally verified structure of sulphanuric chloride. Hazell et al. states that the structure (originally proposed by Kirsanov(1952)) has the $\ce{Cl}$ atoms attached to the $\ce{S}$ atom, with a formal charge of +1 on the $\ce{S}$ and -1 on the $\ce{N}$ atom. This structure has been proposed keeping in mind the physical properties of the compound.

![fig. showing (I) $\alpha$ and (II) $\beta$ forms](/articles/2020/res/X_2.png)

<del>Without knowing about these findings, drawing the correct structure is nigh impossible. This is what makes this a very hard question, as the first guess is to draw the structure that I have drawn above.</del> See edit

Once the structure is known, 5.2, 5.3 and 5.4 are very easy. 5.2 involves drawing the two stereoisomers, which consist of an all cis $\ce{Cl}$ isomer and a trans $\ce{Cl}$ isomer, both of which are shown below.

![stereoisomers](/articles/2020/res/X_3.png)

5.3 involves a simple halogen substitution reaction with Fluorine, giving us $\ce{(NSOF)3}$. This is isostructural with $\ce{(NSOCl)3}$. 5.4 involves a substitution reaction with methylamine, giving us $$\ce{(NSOF)3 + 3CH3NH2 -> (NSO(NHCH3))3 + 3HF}$$

5.5 again requires a bit of mental hardwork. Y contains 120 electrons. An easy choice would be to replace the $\ce{F}$ atoms with $\ce{O-}$ atoms, giving us $\ce{(NSO2)3^3-}$. Drawing a second one is much trickier. Keeping in line with the problem, if we think of other inorganic heterocycles, $\ce{(SO3)3}$, the cyclic trimer of $\ce{SO3}$ comes to mind. Indeed, this is isoelectronic as it has 120 electrons. Once $\ce{(SO3)3}$ is obtained, 5.6 becomes easy as $\ce{(SO3)3}$ polymerizes in aqueous solution to give polymeric $\ce{(SO3)\_n}$.

A very good problem, well above the regular inorganic standard. Breaking through the first step is the hardest, followed by obtaining the correct structure for the trimer and it's isoelectronic counterparts. The rest is quite easy.

###EDIT:

There is a better, mechanism-based way of solving this question, as pointed out by [Yusuf Hasan](https://chemistry.stackexchange.com/users/54655/yusuf-hasan) over at Chemistry StackExchange. Thionyl Chloride reacts with organic molecules via this reaction pathway:

![SNi pathway](/articles/2020/res/SNi.png)

To solve this problem, we need to formulate a similar reaction pathway, but with the Azide anion as the substrate instead of pentan-2-ol. Here's the proposed pathway:

![Monomer formation](/articles/2020/res/monomer.png)

Trimerization occurs through a pericyclic mechanism similar to the trimerization of $\ce{SO3}$. Note that the $\ce{Cl-}$ atoms shift from $\ce{N}$ to $\ce{S}$ in a concerted manner, similar to the mechanism proposed by [Okajima and Imafuku](https://www.researchgate.net/publication/11505683_Theoretical_Study_on_Chlorine_and_Hydrogen_Shift_in_Cycloheptatriene_and_Cyclopentadiene_Derivatives). 

![Trimer formation](/articles/2020/res/trimer.png)

This is a more concrete way to get to the answer and one that does not involve guesswork or hit and trial.

----------
<sup>P.S: Adding MHChem required an update to MathJax 3.x, which brings with it improved rendering (and stricter use of align and gather environments). The MathJax rendering bugs on mobile should be gone now.</sup>
