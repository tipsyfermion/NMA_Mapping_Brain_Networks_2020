# Mapping Brain Networks - NMA 2020 Project

The [Neuromatch Academy](https://www.neuromatchacademy.org/) was a summer school that happened in the summer of 2020. In the midst of a pandemic, the school emerged on an online platform reaching out to everyone across the world. The academy served the purpose of training neuroscientists to learn computational tools, make connections to real world neuroscience problems, and promote networking with researchers.

The academy also provided an opportunity for the students to carry out their own mini-project that would last three weeks. Several datasets were provided for exploration. Our group Les Souris Grises, from the pod 063-Gay-Ladybug have decided to go with the Steinmetz data set. Below us is a description of the Steinmetz data set that we chose.


## Description and objectives

During a decision making task like the one in the Steinmetz experiment, a number of different brain regions are involved in the processing of sensory information to decision making to motor action. These regions act together in particular networks. We’re aware of the anatomical organisation of these regions but the dynamical interactions among them, is not well established.

How do the different brain regions interact with one another in terms of functional connectivity? Can we attribute behaviour to large-scale brain wide circuits? Are different networks involved in different tasks? What can the neural activity from distinct regions reveal about their interaction on a temporal scale? These are some broad questions that we set out to answer.

Our questions were inspired by some of the original questions from some [exemplary projects](https://docs.google.com/presentation/d/1WAHfJcBPM4rmwwvreAAS92sRYtltJRwklxH-82NzCYo/preview?pru=AAABc3cRwPE*S0Y87T5BNFvf9wvSREdLUQ&slide=id.p).

We decided to focus on one rodent’s data, from one session (Session no. 11). Our chosen regions were the primary visual area (VISp) and the secondary motor area (MOs). These two are anatomically and functionally distinct, hence they were our best shot at investigating differences in activity. 

We believe that the dataset has enough potential, and given enough time we can build better models to represent the temporal activations of regions. However for the time being we shall settle on the simpler task.

## Status - *Completed*

We have successfully completed the project. All the relevant details can be found in our supporting documentation file. which can be accessed [here](https://docs.google.com/document/d/1mL7ljkdmnF2BEkKMqvfbHuLIimTxdGObVxFDGKeNcCA/edit?usp=sharing). 

## Dataset

The dataset used for this purpose was the dataset procured by [Steinmetz et al. 2019](https://figshare.com/articles/steinmetz/9598406).

The Steinmetz dataset is an electrophysiological recording from multiple regions of the mouse brain during a 2-Alternative Forced Choice Task paradigm. Neuropixel probes were used to record from approx. 30,000 neurons from 42 regions, while the mouse performed a visual discrimination task. In each trial (multiple trials conducted over each session; and a total of 39 sessions), a mouse was placed on a wheel with its head fixed, surrounded by 3 screens (left, right and in front). Images of differential contrast were presented to either the left, right or both the screens and the mouse had to turn the wheel in the correct direction in order to bring the greater-contrast image to the front-screen. If there was no image presented on either side, the correct response was to hold the wheel steady for 1.5s. Neural activity was continuously recorded for the entire duration of the task. 

The locations in the dataset have been mapped according to the [Allen Mouse Brain Atlas](https://mouse.brain-map.org/static/atlas)

Code for the analysis was written in Python, with the help of scientific packages; Numpy, Scipy, Sklearn

To load the data into our notebooks for further analysis, we used some [code](https://github.com/MouseLand/steinmetz2019_NMA) provided by Dr. Marius Pachitariu.

For a detailed description of the dataset see [this](https://github.com/nsteinme/steinmetz-et-al-2019/wiki/data-files) document by Dr. Nick Steinmetz and [this](https://docs.google.com/document/d/15YZOHIa6rZ8kx1bcIEH5j7-j-pj0GzmjLoevHVT1LIg/edit) writeup by us.


## Resources

**Literature:**
* [Distributed coding of choice, action and engagement across the mouse brain](https://www.nature.com/articles/s41586-019-1787-x)
* [Methods to identify spike patterns/activation from spike train](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5908877/)
* [Theoretical Neuroscience](https://mitpress.mit.edu/books/theoretical-neuroscience)

**Packages:**
* [Anaconda](https://www.anaconda.com/products/individual)
* [NumPy](https://numpy.org/)
* [SciPy](https://www.scipy.org/)
* [MatPlotLib](https://matplotlib.org/)
* [Elephant - Electrophysiology Analysis Toolkit](https://elephant.readthedocs.io/en/latest/)
* [Neo](https://neo.readthedocs.io/en/stable/index.html)

**Code References:**
* [steinmetz-et-al-2019 data description](https://github.com/nsteinme/steinmetz-et-al-2019/wiki/data-files)
* [steinmetz2019_NMA by Dr. Marius Pachitariu](https://github.com/MouseLand/steinmetz2019_NMA)
* [Neuromatch Academy](https://github.com/NeuromatchAcademy/course-content)

**Documentation:**
* [GitHub Repo](https://github.com/Debu922/NMA_Mapping_Brain_Networks_2020)
* [YouTube Video](https://www.youtube.com/watch?v=4PEkslpuU9g)
* [Presentation](https://docs.google.com/presentation/d/1r8z8EMO1Zn923V8UnlLNPfjxw4M_okCQIUM7TIZY6EI/edit?usp=sharing)
* [Documentation](https://docs.google.com/document/d/1mL7ljkdmnF2BEkKMqvfbHuLIimTxdGObVxFDGKeNcCA/edit?usp=sharing)
* [Google Drive](https://drive.google.com/drive/folders/189v0_3NXdAK9bZxwRaltW8WP9nB39a1O?usp=sharing)
* [Resources File](https://docs.google.com/spreadsheets/d/1ht3E8thgBagDLVfr7rQMQGv8Qvxr6UqTvYqZzfY16NE/edit?usp=sharing)
* [Data Descrtiption File](https://docs.google.com/document/d/15YZOHIa6rZ8kx1bcIEH5j7-j-pj0GzmjLoevHVT1LIg/edit?usp=sharing)
* [Project TImeline](https://docs.google.com/spreadsheets/d/1VhvLymLOod-aL8rPxVxytRc7LW-v2gd4IjHp_vjXFBU/edit#gid=0)

## People

* [John Butler(Mentor)](https://github.com/john-s-butler-dit)
* [Arun Garimella](https://github.com/kilimanjaro2)
* [Anna Marinou](https://github.com/AnnaMarinou)
* [Anwesha Das](https://github.com/anwesha-das)
* [Debaditya Bhattacharya](https://github.com/Debu922)
