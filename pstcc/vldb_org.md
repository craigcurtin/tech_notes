
https://www.vldb.org/tutorials.html

# Basic Topics:
1. Relational Database Systems and Extensions
1. Implementation and tuning of relational database applications
1. Object-Oriented databases: modeling, design and implementation
1. Database Languages and Application Development Tools
1. Interoperability and Heterogeneous Database Management
1. Geographic Information Systems
1. Object-Oriented Database Application Methodologies

# Advanced Topics:
1. Active Databases
1. Real-time Databases
1. Multimedia database management
1. Spatial and Temporal Data Management
1. Semistructured Data and XML
1. Mediators, Meta-searchers and Web-DB query languages
1. Data Warehousing
1. Data Mining
1. Performance Measurement and Database Tuning
1. Parallel Databases: architectures, data organization and query processing




# formal organizations ...
[ACM SIGMOD - ACM Special Interest Group on Management of Data](https://sigmod.org/)
[SIGKDD](https://www.kdd.org/)


# FOUNDATIONS (COURSE 1)
# INTRODUCTION
Basic concepts of data mining, including motivation, definition, the relationships of data mining with database systems, statistics, machine learning, different kinds of data repositories on which data mining can be performed, different kind of patterns and knowledge to be mined, the concept of interestingness, and the current trends and developments of data mining. The material can probably be introduced by showing a few case studies.
1. Concepts of data mining: motivation, definition, the relationships of data mining with database systems, statistics, machine learning, and information retrieval.
1. Knowledge discovery process: An overview of the Knowledge Discovery Process. Emphasis on the iterative and interactive nature of the KDD Process.
1. Mining on different kinds of data: relational, transactional, object-relational, heterogeneous, spatiotemporal, text, multimedia, Web, stream, mobile, and so on.
1. Mining for different kind of knowledge: classification, regression, clustering, frequent patterns, discriminant, outliers, and so on.
1. Evaluation of knowledge: interestingness or quality of knowledge, including accuracy, utility (such as support), and relevance (such as correlation).
1. Applications of data mining: market analysis, scientific and engineering process analysis, bioinformatics, homeland security, and so on.
# DATA PREPROCESSING
1. This unit will cover the following topics: (1) why preprocess the data? (2) basic data cleaning techniques, (3) data integration and transformation, and (4) data reduction methods. In particular, the following topics will be covered.
1. Descriptive data summarization: This unit covers basic techniques for summarizing and describing data. It will cover: (1) computing the measures of central tendency such as mean, and mode, (2) computing the measures of data dispersion such as quantiles, boxplots, variances, standard deviation, and outliers, and (3) graphic display of basic statistical descriptions, such as histogram, scatter plot, boxplot, quantile-quantile plot, and local regression curves.
1. Data cleaning methods: Basic techniques for handling missing values, noisy data, and inconsistent data, including typical binning, clustering, and regression methods for data cleaning.
1. Data integration and transformation methods: This includes data smoothing, data aggregation, data generalization, normalization, attribute (or feature) construction.
1. Basic data reduction methods: It introduces binning (histograms), sampling, and data cube aggregation.
1. Discretization and concept hierarchy generation: It covers discretization and concept hierarchy generation for numeric data (including binning, clustering, histogram analysis), and for categorical data (automatic generation of concept hierarchies).


# ADVANCED TOPICS (COURSE II)

# ADVANCED DATA PROCESSING
1. This unit will cover advanced data reduction methods.
1. Advanced data reduction methods: (1) dimensionality reduction (feature or attribute subset reduction), (2) numerosity reduction (regression, histogram, clustering, sampling, singular value decomposition (SVD), and discretization), and (3) data compression (lossless versus lossy compression, Fourier and wavelet transformation, and principal component analysis).
1. 
# DATA WAREHOUSING, OLAP, AND DATA GENERALIZATION
1. This unit covers advanced material in data warehousing, OLAP, and data generalization
1. The multidimensional data model
1. Implementation of data warehouses: data integration, indexing OLAP data (bitmap index), efficient processing of OLAP queries, metadata repository, data warehouse back-end tools and utilities.
1. Efficient computation of data cubes: categorization of measures: distributive, algebraic, and holistic measures, cube computation methods, icburg cubes, top-down and bottom-up computation, computing closed and approximate data cubes.
1. Other data generalization approaches: Attribute-oriented induction, mining class comparisons; discriminating between different classes.
1. Exploration of data warehouse and data mining: Discovery-driven exploration of data cubes, complex aggregation at multiple granularity, cube gradient analysis, from online analytical processing to online analytical mining.
1. 
# ADVANCED ASSOCIATION, CORRELATION, AND FREQUENT PATTERN ANALYSIS
1. Advanced frequent pattern mining methods: (1) vertical format mining, (2) pattern-growth algorithm, (3) mining closed patterns and max-patterns
1. Constraint-based association mining: (1) rule- and query-guided association mining, (2) anti-monotonicity, monotonicity, succinctness in constraint mining, (3) convertible constraints
1. Extensions and applications of frequent pattern mining: (1) iceberg cube computation, (2) fascicles and semantic data compression, (3) frequent pattern-based classification and cluster analysis
1. 
#ADVANCED CLASSIFICATION
1. Bayesian belief networks: methods for (advanced) choosing BBN structure and training Bayesian belief networks
1. Advanced decision tree construction: (1) enhancements to basic classification tree induction, (2) scalable algorithms for classification tree induction, (3) integrating data warehousing techniques and classification tree induction, (4) classification with partially labeled data
1. Neural network approach for classification: (1) a multi-layer feed-forward neural network, (2) defining a network topology, (3) back-propagation, (4) interpretability of classification results
1. Kernel methods: (1) kernel logistic regression, (2) kernel discriminant analysis, (3) advanced SVM kernel methods
1. Introduction to learning theory: PAC-learnability, empirical, true and structural risk, VC-theory
1. Ensemble construction: Weighted voting, bagging, weak learner, boosting, AdaBoost
1. Other classification methods: (1) case-based reasoning, (2) genetic algorithms, (3) rough set approach, (4) fuzzy set approach
1. 
1. #ADVANCED CLUSTER ANALYSIS
1. Grid-based clustering: A statistical information grid approach, clustering by wavelet analysis, clustering high-dimensional space.
1. Clustering high-dimensional data: Subspace clustering, frequent pattern-based clustering, clustering wavelet analysis.
1. 
# Advanced outlier analysis: Statistical-based outlier detection, distance-based outlier detection, deviation-based outlier detection, analysis of local outliers.
1. Collaborative filtering
1. Advanced Time-Series and Sequential Data Mining
1. This unit covers the advanced techniques for mining sequential data, including the following topics.
1. Similarity search in time-series analysis
1. Hidden Markov models
1. Periodicity analysis: Transformation-based approach, mining partial periodicity.
1. Sequence segmentation: Hidden Markov model and Variable Markov model for sequence segmentation.
1. Sequence classification and clustering: (1) $q$-gram based methods, keyword-based methods; (2) (high order) Markov chain, hidden Markov model; (3) suffix tree, probabilistic suffix tree, and probabilistic automata.
1. 
# Mining Data Streams
1. This unit covers the techniques for mining stream data, including the following topics.
1. What is stream data?
1. Basic tools: Chernoff bounds, reservoir sampling
1. Stream sample counting and frequent pattern analysis
1. Classification of data streams
1. Clustering data streams
1. Online sensor data analysis
1. Mining Spatial, Spatiotemporal, and Multimedia data
1. This unit covers the techniques for mining spatial, spatiotemporal, and multimedia data, including the following topics.
1. Mining spatial and spatiotemporal databases: (1) Spatial data cube construction and spatial OLAP, (2) spatial association and co-location analysis, (3) spatial clustering methods, (4) spatial classification and spatial trend analysis, (5) spatiotemporal data miming, (6) mining moving objects and trajectories.
1. Mining multimedia databases: (1) multidimensional analysis of multimedia data, (2) similarity search in multimedia data, (3) classification and regression analysis of multimedia data, (4) mining association and correlation in multimedia data, (5) clustering multimedia data
1. Mining object databases: (1) multidimensional analysis of complex objects, (2) generalization on complex structured and semi-structured data, (3) methodology for mining complex object databases: aggregation, approximation, and progressive refinement.
1. 
# Mining Biological Data
1. This unit covers the techniques for mining biological data, including the following topics.
1. Mining DNA, RNA, and proteins: (1) Mining motif patterns, (2) searching homology in large databases, (3) phylogenetic and functional prediction.
1. Mining gene expression data: (1) clustering gene expression, e.g., for gene regulatory networks, (2) classifying gene expression, e.g., for disease-sensitive gene discovery.
1. Mining mass spectrometry data
1. Mining and integrating knowledge from biomedical literature
1. Mining inter-domain associations
1. 
# Text mining
1. This module will cover work that applies known mining techniques to the text media, emphasizing the new issues which arise.
1. Text representation: Set-of-words, bag-of-words, vector-space model; the issue of large raw dimensionality
1. Dimensionality reduction: PCA, SVD, latent semantic indexing
1. Text clustering: agglomerative, $k$-means, EM; effect of a large number of noise dimensions, partial supervision
1. Feature selection in high dimensions
1. Naive Bayes classification: Poor density estimates, small-degree Bayesian belief network induction
1. Discriminative learning: maximum entropy, logistic regression, and support vector learning
1. Shallow linguistics: Phrase detection, part-of-speech tagging, named entity extraction, word sense disambiguation
1. 
# Hypertext and Web mining
1. This module will cover work that is specific to analyzing hypermedia, i.e., involving hierarchical tagging languages and hyperlinks in conjunction with text.
1. Web modeling: The Web as an evolving,collaborative, populist social network: aggregate graph-structure of the Web, preferential attachment linking models and experimental validation
1. Link mining and social network analysis: Links as endorsement: PageRank and HITS algorithms to identify authoritative Web pages; connections with bibliometry
1. The PageRank algorithm: Integrating page content and page layout with link structure; topic-sensitive PageRanks; Google
1. Mining by exploiting text and links: Exploitingtext and links for better clustering and classification; unified probabilistic models for text and links
1. Structured data extraction: Information extraction,exploiting markup structure to extract structured data from pages meant for human consumption
1. Multidimensional Web databases: Automatic construction of multilayered Web information base; discovering entities and relations on the Web (WebKB)
1. Exploration and resource discovery on the Web: reinforcement learning, other approaches
1. Web usage mining and adaptive Web sites: Reorganizing Web sites by mining log data
1. 
# Data Mining Languages, Standards, and System Architectures
1. This unit covers the issues related to data mining languages, standards, and system architectures, including the following topics.
1. Data mining primitives: what defines a data mining task? task-relevant data, the kind of knowledge to be mined, background knowledge: concept hierarchies, user-specified constraints, interestingness measures, presentation of discovered patterns
1. Data mining languages, user interfaces, and standardization efforts
1. Architectures of data mining systems
1. 
# Data Mining Applications
1. This unit covers the issues related to domain-specific data mining applications, including the following topics. (Note: Some of these themes, if concrete and good materials are available, should go into the Foundations part as case studies.)
1. Data mining for financial data analysis
1. Data mining for the retail industry
1. Data mining for the telecommunication industry
1. Data mining for intrusion detection
1. Data mining in scientific and statistical applications
1. Data mining in software engineering and computer system analysis
1. 
# Data Mining and Society
1. This unit covers the issues related to social impacts of data mining, including the following topics.
1. Social impacts of data mining
1. Data mining vs. data security and privacy
1. Privacy-preserving data mining
1. 
# Trends in Data Mining
1. This unit covers the major trends in data mining, including the following topics.
1. Setting solid theoretical foundations for data mining
1. Mining deep in specific applications
1. Ubiquitous and invisible data mining
1. Integrated data and information systems
